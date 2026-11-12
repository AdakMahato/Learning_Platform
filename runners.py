"""
Secure Multi-Language Execution Runners for Python, C++, and SQL.
"""

import ast
import json
import os
import platform
import re
import signal
import sqlite3
import subprocess
import sys
import tempfile
import threading
import time
import pandas as pd
from typing import Tuple, Any, List, Dict, Optional

try:
    import resource as _resource
except ImportError:
    _resource = None

_MAX_SOURCE_BYTES = 65_536
_MAX_STDIN_BYTES = 16_384
_MAX_SQL_BYTES = 32_768
_MAX_OUTPUT_CHARS = 32_768
_MAX_SQL_ROWS = 1_000
_SQL_DEADLINE_SEC = float(os.environ.get("RUNNER_SQL_TIMEOUT_SEC", "2.5"))
_EXEC_CONCURRENCY = max(1, int(os.environ.get("RUNNER_MAX_CONCURRENCY", "4")))
_EXEC_SEMAPHORE = threading.BoundedSemaphore(_EXEC_CONCURRENCY)

_FORBIDDEN_PY_MODULES = frozenset({
    "os", "posix", "nt", "subprocess", "socket", "ctypes", "shutil",
    "urllib", "http", "requests", "httpx", "aiohttp", "pathlib",
    "pty", "tty", "termios", "fcntl", "signal", "multiprocessing",
    "resource", "importlib", "builtins", "gc", "inspect", "pickle",
    "marshal", "sqlite3", "tempfile", "glob", "webbrowser", "pwd",
    "grp", "ssl", "ftplib", "smtplib", "poplib", "imaplib", "telnetlib",
    "mmap", "sysconfig", "platform", "asyncio", "socketserver", "venv",
    "ensurepip", "pip", "distutils", "setuptools", "code", "codeop",
})
_FORBIDDEN_PY_CALLS = frozenset({
    "eval", "exec", "compile", "__import__", "open", "breakpoint",
})
_FORBIDDEN_PY_ATTRS = frozenset({
    "__subclasses__", "__globals__", "__builtins__", "__mro__",
    "__base__", "__bases__", "__code__", "__closure__", "__dict__",
    "_getframe", "modules", "executable", "path", "meta_path",
})
_SAFE_SQLITE_PRAGMAS = frozenset({
    "read_uncommitted", "foreign_keys", "table_info",
    "table_xinfo", "index_list", "index_info", "database_list",
})
_FORBIDDEN_SQL_FUNCS = frozenset({
    "load_extension", "sqlite_compileoption_get",
    "sqlite_compileoption_used", "fts3_tokenizer",
})
_FORBIDDEN_CPP_RE = re.compile(
    r"(#\s*include\s*[<\"][/.]"
    r"|#\s*include\s*\"[^\"]*\.\.[^\"]*\""
    r"|\bsystem\s*\(|\bpopen\s*\(|\bpclose\s*\("
    r"|\bfork\s*\(|\bvfork\s*\(|\bexecv\w*\s*\(|\bexecl\w*\s*\("
    r"|\b__asm__\b|\basm\s*\()",
    re.IGNORECASE,
)


def _truncate_output(text: str, sandbox_dir: str = "") -> str:
    if not text:
        return ""
    if sandbox_dir:
        text = text.replace(sandbox_dir, "<sandbox>")
    if len(text) > _MAX_OUTPUT_CHARS:
        return text[:_MAX_OUTPUT_CHARS] + "\n... [output truncated at 32 KB limit]"
    return text


def _sandbox_env(temp_dir: str) -> Dict[str, str]:
    """Minimal environment stripped of all host secrets and tokens."""
    py_bin = os.path.dirname(os.path.abspath(sys.executable))
    safe_path = os.pathsep.join(
        p for p in [py_bin, "/usr/local/bin", "/opt/homebrew/bin", "/usr/bin", "/bin"] if p
    )
    return {
        "PATH": safe_path,
        "HOME": temp_dir,
        "TMPDIR": temp_dir,
        "TEMP": temp_dir,
        "TMP": temp_dir,
        "LANG": "C.UTF-8",
        "LC_ALL": "C.UTF-8",
        "PYTHONDONTWRITEBYTECODE": "1",
        "PYTHONNOUSERSITE": "1",
        "OPENBLAS_NUM_THREADS": "1",
        "OMP_NUM_THREADS": "1",
        "MKL_NUM_THREADS": "1",
        "NUMEXPR_NUM_THREADS": "1",
    }


def _make_preexec(cpu_seconds: int):
    def _preexec():
        if hasattr(os, "setsid"):
            os.setsid()
        if _resource is None:
            return
        try:
            _resource.setrlimit(_resource.RLIMIT_CPU, (cpu_seconds, cpu_seconds))
            _resource.setrlimit(_resource.RLIMIT_FSIZE, (4 * 1024 * 1024, 4 * 1024 * 1024))
            _resource.setrlimit(_resource.RLIMIT_CORE, (0, 0))
            _, hard_fd = _resource.getrlimit(_resource.RLIMIT_NOFILE)
            fd_cap = min(hard_fd, 128) if hard_fd != _resource.RLIM_INFINITY else 128
            _resource.setrlimit(_resource.RLIMIT_NOFILE, (fd_cap, fd_cap))
            if platform.system() == "Linux" and hasattr(_resource, "RLIMIT_AS"):
                mem_bytes = int(os.environ.get("RUNNER_MAX_MEMORY_MB", "512")) * 1024 * 1024
                _, hard_as = _resource.getrlimit(_resource.RLIMIT_AS)
                as_cap = min(hard_as, mem_bytes) if hard_as != _resource.RLIM_INFINITY else mem_bytes
                _resource.setrlimit(_resource.RLIMIT_AS, (as_cap, as_cap))
        except Exception:
            pass
    return _preexec


def _run_sandboxed_popen(
    cmd: List[str],
    *,
    cwd: str,
    env: Dict[str, str],
    timeout: int,
    input_data: str = "",
) -> Tuple[Optional[int], str, str, bool]:
    """Runs command in isolated process group with resource limits and clean killpg timeout."""
    acquired = _EXEC_SEMAPHORE.acquire(timeout=6)
    if not acquired:
        return None, "", "Sandbox runner is busy handling concurrent requests. Please retry cleanly in a moment.", False
    proc = None
    try:
        preexec = _make_preexec(max(1, int(timeout) + 1)) if os.name == "posix" else None
        proc = subprocess.Popen(
            cmd,
            cwd=cwd,
            env=env,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            preexec_fn=preexec,
        )
        try:
            out, err = proc.communicate(input=input_data, timeout=timeout)
            return proc.returncode, _truncate_output(out or "", cwd), _truncate_output(err or "", cwd), False
        except subprocess.TimeoutExpired:
            try:
                if os.name == "posix":
                    os.killpg(proc.pid, signal.SIGKILL)
                else:
                    proc.kill()
            except Exception:
                pass
            try:
                out, err = proc.communicate(timeout=2)
            except Exception:
                out, err = "", ""
            return None, _truncate_output(out or "", cwd), _truncate_output(err or "", cwd), True
    finally:
        _EXEC_SEMAPHORE.release()


def _check_python_safety(user_code: str) -> Optional[str]:
    """Static AST defense-in-depth gate rejecting unsafe system/IO primitives in untrusted Python."""
    if not isinstance(user_code, str):
        return "Invalid source payload."
    if len(user_code.encode("utf-8", errors="ignore")) > _MAX_SOURCE_BYTES:
        return "Source code exceeds the 64 KB security limit."
    try:
        tree = ast.parse(user_code)
    except SyntaxError:
        return None  # Let Python interpreter surface the normal student SyntaxError
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                root = alias.name.split(".")[0]
                if root in _FORBIDDEN_PY_MODULES:
                    return f"Security policy: module '{root}' is disabled inside the learning sandbox."
        elif isinstance(node, ast.ImportFrom):
            root = (node.module or "").split(".")[0]
            if root in _FORBIDDEN_PY_MODULES:
                return f"Security policy: module '{root}' is disabled inside the learning sandbox."
        elif isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id in _FORBIDDEN_PY_CALLS:
                return f"Security policy: builtin '{node.func.id}()' is disabled inside the learning sandbox."
        elif isinstance(node, ast.Attribute):
            if node.attr in _FORBIDDEN_PY_ATTRS:
                return f"Security policy: attribute '{node.attr}' is restricted inside the learning sandbox."
    return None


def _check_cpp_safety(user_code: str) -> Optional[str]:
    if not isinstance(user_code, str):
        return "Invalid C++ source payload."
    if len(user_code.encode("utf-8", errors="ignore")) > _MAX_SOURCE_BYTES:
        return "C++ source code exceeds the 64 KB security limit."
    m = _FORBIDDEN_CPP_RE.search(user_code)
    if m:
        return f"Security policy: construct '{m.group(0).strip()}' is disabled inside the learning sandbox."
    return None


def _exec_python_source(full_src: str, timeout: int = 5, input_data: str = "") -> Tuple[bool, str, str]:
    stdin_str = "" if input_data is None else str(input_data)
    if len(stdin_str.encode("utf-8", errors="ignore")) > _MAX_STDIN_BYTES:
        return False, "", "Stdin input exceeds the 16 KB security limit."
    with tempfile.TemporaryDirectory(prefix="py_sandbox_") as temp_dir:
        py_file = os.path.join(temp_dir, "main.py")
        with open(py_file, "w", encoding="utf-8") as f:
            f.write(full_src)
        rc, out, err, timed_out = _run_sandboxed_popen(
            [sys.executable, "-I", py_file],
            cwd=temp_dir,
            env=_sandbox_env(temp_dir),
            timeout=timeout,
            input_data=stdin_str,
        )
        if timed_out:
            return False, out, "Execution Timed Out (Possible Infinite Loop or Resource Exhaustion)"
        if rc is None:
            return False, out, err
        if rc != 0:
            return False, out, f"Runtime Error:\n{err}"
        return True, out, ""


def run_py(code: str, timeout: int = 5, input_data: str = None, extra_code: str = "") -> Tuple[bool, str, str]:
    """Runs Python code securely in an isolated resource-bounded subprocess."""
    violation = _check_python_safety(code)
    if violation:
        return False, "", violation
    payload = code + ("\n\n" + extra_code if extra_code and extra_code.strip() else "")
    return _exec_python_source(payload, timeout=timeout, input_data="" if input_data is None else input_data)


def run_cpp(code: str, timeout: int = 4, input_data: str = None) -> Tuple[bool, str, str]:
    """Compiles with g++ and executes C++ code inside a resource-bounded isolated sandbox."""
    violation = _check_cpp_safety(code)
    if violation:
        return False, "", violation
    stdin_str = "" if input_data is None else str(input_data)
    if len(stdin_str.encode("utf-8", errors="ignore")) > _MAX_STDIN_BYTES:
        return False, "", "Stdin input exceeds the 16 KB security limit."

    with tempfile.TemporaryDirectory(prefix="cpp_sandbox_") as temp_dir:
        cpp_file = os.path.join(temp_dir, "main.cpp")
        exe_file = os.path.join(temp_dir, "main.out")
        env = _sandbox_env(temp_dir)

        with open(cpp_file, "w", encoding="utf-8") as f:
            std_headers = [
                "iostream", "vector", "string", "memory", "map",
                "unordered_map", "unordered_set", "set", "queue", "stack", "deque",
                "algorithm", "cmath", "climits", "numeric", "iomanip",
                "utility", "sstream", "cstring", "cassert", "cctype",
                "stdexcept", "functional", "chrono", "tuple"
            ]
            missing_includes = [
                f"#include <{hdr}>"
                for hdr in std_headers
                if f"<{hdr}>" not in code
            ]
            preamble = "\n".join(missing_includes)
            if "using namespace std;" not in code:
                preamble += ("\n" if preamble else "") + "using namespace std;"
            f.write((preamble + "\n" if preamble else "") + code)

        # Compile step
        rc_c, _, comp_err, comp_to = _run_sandboxed_popen(
            ["g++", "-std=c++17", "-O1", cpp_file, "-o", exe_file],
            cwd=temp_dir,
            env=env,
            timeout=6,
            input_data="",
        )
        if comp_to:
            return False, "", "C++ Compilation Timed Out."
        if rc_c is None:
            return False, "", comp_err or "C++ Compiler unavailable."
        if rc_c != 0:
            return False, "", f"Compilation Error:\n{comp_err}"

        # Run step
        rc_r, out, err, run_to = _run_sandboxed_popen(
            [exe_file],
            cwd=temp_dir,
            env=env,
            timeout=timeout,
            input_data=stdin_str,
        )
        if run_to:
            return False, out, "Execution Timed Out (Infinite Loop or Blocking Call)"
        if rc_r is None:
            return False, out, err
        if rc_r != 0:
            return False, out, f"Runtime Error (Exit Code {rc_r}):\n{err}"
        return True, out, ""


def _sqlite_authorizer(action: int, arg1: Optional[str], arg2: Optional[str], db_name: Optional[str], trigger_name: Optional[str]) -> int:
    if action in (sqlite3.SQLITE_ATTACH, sqlite3.SQLITE_DETACH):
        return sqlite3.SQLITE_DENY
    if action == sqlite3.SQLITE_PRAGMA:
        pname = (arg1 or "").strip().lower()
        return sqlite3.SQLITE_OK if pname in _SAFE_SQLITE_PRAGMAS else sqlite3.SQLITE_DENY
    if action == sqlite3.SQLITE_FUNCTION:
        fname = (arg2 or "").strip().lower()
        return sqlite3.SQLITE_DENY if fname in _FORBIDDEN_SQL_FUNCS else sqlite3.SQLITE_OK
    return sqlite3.SQLITE_OK


def _arm_sqlite_sandbox(conn: sqlite3.Connection, timeout_sec: float = _SQL_DEADLINE_SEC):
    deadline = time.monotonic() + max(0.5, timeout_sec)
    conn.set_authorizer(_sqlite_authorizer)
    conn.set_progress_handler(lambda: 1 if time.monotonic() > deadline else 0, 50_000)


def _split_sql_statements(query: str) -> List[str]:
    """Splits SQL script into statements while keeping CREATE TRIGGER ... BEGIN ... END intact."""
    if not query or not query.strip():
        return []
    stmts = []
    cur = []
    in_single = False
    in_double = False
    i = 0
    n = len(query)
    while i < n:
        ch = query[i]
        cur.append(ch)
        if ch == "'" and not in_double:
            if in_single and i + 1 < n and query[i + 1] == "'":
                cur.append(query[i + 1])
                i += 2
                continue
            in_single = not in_single
        elif ch == '"' and not in_single:
            in_double = not in_double
        elif ch == ";" and not in_single and not in_double:
            so_far = "".join(cur).strip()
            upper = so_far.upper()
            if re.search(r'\bCREATE\b.*\bTRIGGER\b', upper, re.DOTALL) and re.search(r'\bBEGIN\b', upper):
                if re.search(r'\bEND\s*;$', upper):
                    stmts.append(so_far)
                    cur = []
            else:
                stmts.append(so_far)
                cur = []
        i += 1
    tail = "".join(cur).strip()
    if tail:
        stmts.append(tail)
    return [s for s in stmts if s and s != ";"]


def _snapshot_db_state(conn: sqlite3.Connection) -> Dict[str, Any]:
    """Captures tables, indexes, triggers, and row data from an SQLite connection."""
    cur = conn.cursor()
    cur.execute("SELECT type, name FROM sqlite_master WHERE name NOT LIKE 'sqlite_%' ORDER BY type, name")
    objects = cur.fetchall()
    tables = {}
    for obj_type, obj_name in objects:
        if obj_type == "table":
            try:
                safe_tbl = obj_name.replace('"', '""')
                cur.execute(f'SELECT * FROM "{safe_tbl}" LIMIT {_MAX_SQL_ROWS}')
                cols = [d[0] for d in cur.description] if cur.description else []
                rows = cur.fetchall()
                tables[obj_name] = {"columns": cols, "rows": rows}
            except Exception:
                pass
    return {"objects": objects, "tables": tables}


def inspect_sql_schema(schema_ddl: str) -> Dict[str, pd.DataFrame]:
    """Runs setup DDL and returns DataFrames of all initial tables for interactive Schema Explorer."""
    if not schema_ddl or not schema_ddl.strip():
        return {}
    conn = sqlite3.connect(":memory:", isolation_level=None)
    try:
        conn.executescript(schema_ddl)
        cur = conn.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name")
        result = {}
        for (tbl_name,) in cur.fetchall():
            safe_tbl = tbl_name.replace('"', '""')
            df = pd.read_sql_query(f'SELECT * FROM "{safe_tbl}" LIMIT {_MAX_SQL_ROWS}', conn)
            result[tbl_name] = df
        return result
    except Exception:
        return {}
    finally:
        conn.close()


def _exec_sql_sequence(conn: sqlite3.Connection, query: str) -> Any:
    """Executes SQL statements cleanly with isolation_level=None and returns last query DataFrame if any."""
    statements = _split_sql_statements(query)
    if not statements:
        return None
    cur = conn.cursor()
    last_df = None
    for stmt in statements:
        clean = stmt.lstrip()
        first_kw = clean.split(None, 1)[0].lower() if clean else ""
        if first_kw in ("select", "with", "explain"):
            last_df = pd.read_sql_query(stmt, conn)
            if len(last_df) > _MAX_SQL_ROWS:
                last_df = last_df.head(_MAX_SQL_ROWS)
        else:
            cur.execute(stmt)
    return last_df


def run_sql(query: str, schema_ddl: str = None) -> Tuple[bool, Any, str]:
    """Executes SQL statements in a sandboxed, time-bounded in-memory SQLite database."""
    if query and len(query.encode("utf-8", errors="ignore")) > _MAX_SQL_BYTES:
        return False, None, "SQL query exceeds the 32 KB limit."
    conn = sqlite3.connect(":memory:", isolation_level=None)
    try:
        if schema_ddl:
            conn.executescript(schema_ddl)
        _arm_sqlite_sandbox(conn)
        statements = _split_sql_statements(query)
        if not statements:
            return True, "Query executed (No statements found).", ""
        last_df = _exec_sql_sequence(conn, query)
        if last_df is not None:
            return True, last_df, ""
        snap = _snapshot_db_state(conn)
        if snap["tables"]:
            return True, snap, ""
        return True, "Statements executed successfully.", ""
    except sqlite3.OperationalError as e:
        msg = str(e)
        if "interrupted" in msg.lower():
            return False, None, "SQL Execution Timed Out (Runaway loop or expensive query aborted)."
        return False, None, f"SQL Execution Error:\n{msg}"
    except Exception as e:
        msg = str(e)
        if "interrupted" in msg.lower():
            return False, None, "SQL Execution Timed Out (Runaway loop or expensive query aborted)."
        return False, None, f"SQL Execution Error:\n{msg}"
    finally:
        conn.close()


def verify_sql_sandbox(user_query: str, solution_query: str, schema_ddl: str = None) -> Dict[str, Any]:
    """Runs user SQL inside sandboxed SQLite and compares output / resulting DB state against solution_query."""
    if not user_query or not user_query.strip():
        return {"ok": False, "passed": False, "error": "Please enter a SQL query or statement."}
    if len(user_query.encode("utf-8", errors="ignore")) > _MAX_SQL_BYTES:
        return {"ok": False, "passed": False, "error": "SQL query exceeds the 32 KB limit."}
    conn_u = sqlite3.connect(":memory:", isolation_level=None)
    conn_s = sqlite3.connect(":memory:", isolation_level=None)
    try:
        if schema_ddl:
            conn_u.executescript(schema_ddl)
            conn_s.executescript(schema_ddl)
        _arm_sqlite_sandbox(conn_u)
        try:
            u_df = _exec_sql_sequence(conn_u, user_query)
            u_snap = _snapshot_db_state(conn_u)
        except Exception as e:
            msg = str(e)
            if "interrupted" in msg.lower():
                return {"ok": False, "passed": False, "error": "SQL Execution Timed Out (Runaway loop or expensive query aborted)."}
            return {"ok": False, "passed": False, "error": f"SQL Execution Error:\n{msg}"}

        if not solution_query or not solution_query.strip():
            return {"ok": True, "passed": True, "result_df": u_df, "snapshot": u_snap}

        s_df = _exec_sql_sequence(conn_s, solution_query)
        s_snap = _snapshot_db_state(conn_s)

        passed = False
        if s_df is not None and u_df is not None:
            if list(u_df.columns) == list(s_df.columns):
                passed = u_df.astype(str).equals(s_df.astype(str))
            elif u_df.shape == s_df.shape:
                passed = u_df.astype(str).values.tolist() == s_df.astype(str).values.tolist()
        elif s_df is None and u_df is None:
            if u_snap == s_snap:
                passed = True
            else:
                u_norm_tbls = {k.lower(): ([c.lower() for c in v["columns"]], v["rows"]) for k, v in u_snap["tables"].items()}
                s_norm_tbls = {k.lower(): ([c.lower() for c in v["columns"]], v["rows"]) for k, v in s_snap["tables"].items()}
                u_types = sorted([o[0] for o in u_snap["objects"]])
                s_types = sorted([o[0] for o in s_snap["objects"]])
                if u_norm_tbls == s_norm_tbls and u_types == s_types:
                    passed = True

        return {
            "ok": True,
            "passed": passed,
            "result_df": u_df,
            "expected_df": s_df,
            "snapshot": u_snap,
            "expected_snapshot": s_snap,
        }
    except Exception as e:
        return {"ok": False, "passed": False, "error": f"Verification Error:\n{str(e)}"}
    finally:
        conn_u.close()
        conn_s.close()


# =========================================================================
# DSA Dual-Language Online Judge Runner (Python 3 & C++17 STL)
# =========================================================================

_PY_DSA_PRELUDE = '''
import json as _dsa_json
import time as _dsa_time
import io as _dsa_io
import contextlib as _dsa_ctx
import collections as _dsa_collections
import heapq as _dsa_heapq
import bisect as _dsa_bisect
import math as _dsa_math
import functools as _dsa_functools
import itertools as _dsa_itertools
from typing import List, Optional, Dict, Tuple, Set, Any
from collections import defaultdict, Counter, deque
import heapq, bisect, math

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

def _dsa_build_list(arr):
    dummy = ListNode(0)
    cur = dummy
    for x in arr:
        cur.next = ListNode(x)
        cur = cur.next
    return dummy.next

def _dsa_dump_list(head, limit=5000):
    out = []
    steps = 0
    while head is not None and steps < limit:
        out.append(head.val)
        head = head.next
        steps += 1
    if head is not None:
        out.append("CYCLE_OR_TOO_LONG")
    return out

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

def _dsa_build_tree(arr):
    if not arr or arr[0] is None:
        return None
    root = TreeNode(arr[0])
    q = deque([root])
    i = 1
    while q and i < len(arr):
        node = q.popleft()
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            q.append(node.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            q.append(node.right)
        i += 1
    return root

def _dsa_dump_tree(root):
    if not root:
        return []
    out = []
    q = deque([root])
    while q:
        node = q.popleft()
        if node is None:
            out.append(None)
        else:
            out.append(node.val)
            q.append(node.left)
            q.append(node.right)
    while out and out[-1] is None:
        out.pop()
    return out

def _dsa_run_tests(specs, sample_only=False, n_samples=2):
    chosen = specs[:n_samples] if sample_only else specs
    results = []
    debug_chunks = []
    for item in chosen:
        if len(item) == 4:
            name, inp_str, fn, expected = item
            cmp_fn = None
        else:
            name, inp_str, fn, expected, cmp_fn = item
        buf = _dsa_io.StringIO()
        t0 = _dsa_time.perf_counter()
        try:
            with _dsa_ctx.redirect_stdout(buf):
                actual = fn()
            elapsed = (_dsa_time.perf_counter() - t0) * 1000.0
            passed = bool(cmp_fn(actual, expected)) if cmp_fn else (actual == expected)
            results.append({
                "name": str(name),
                "passed": passed,
                "input": str(inp_str),
                "expected": repr(expected),
                "actual": repr(actual),
                "time_ms": round(elapsed, 3),
                "error": ""
            })
        except Exception as exc:
            elapsed = (_dsa_time.perf_counter() - t0) * 1000.0
            results.append({
                "name": str(name),
                "passed": False,
                "input": str(inp_str),
                "expected": repr(expected),
                "actual": f"RuntimeError: {type(exc).__name__}: {exc}",
                "time_ms": round(elapsed, 3),
                "error": f"{type(exc).__name__}: {exc}"
            })
        printed = buf.getvalue()
        if printed:
            debug_chunks.append(f"[{name}]\\n{printed.rstrip()}")
    payload = {
        "cases": results,
        "debug_stdout": "\\n".join(debug_chunks)
    }
    print("__DSA_RESULT__:" + _dsa_json.dumps(payload))
'''

_CPP_DSA_PRELUDE = '''
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <deque>
#include <cmath>
#include <climits>
#include <numeric>
#include <functional>
#include <chrono>
#include <sstream>
#include <iomanip>
#include <memory>
#include <tuple>
#include <utility>
#include <cctype>
using namespace std;

#ifdef DSA_USE_LISTNODE
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
static inline ListNode* _dsa_build_list(const vector<int>& arr) {
    ListNode dummy(0);
    ListNode* cur = &dummy;
    for (int x : arr) { cur->next = new ListNode(x); cur = cur->next; }
    return dummy.next;
}
static inline vector<int> _dsa_dump_list(ListNode* head, int limit = 5000) {
    vector<int> out;
    int steps = 0;
    while (head && steps < limit) { out.push_back(head->val); head = head->next; ++steps; }
    return out;
}
#endif

#ifdef DSA_USE_TREENODE
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
static inline TreeNode* _dsa_build_tree(const vector<int>& arr, int null_val = INT_MIN) {
    if (arr.empty() || arr[0] == null_val) return nullptr;
    TreeNode* root = new TreeNode(arr[0]);
    queue<TreeNode*> q;
    q.push(root);
    size_t i = 1;
    while (!q.empty() && i < arr.size()) {
        TreeNode* cur = q.front(); q.pop();
        if (i < arr.size() && arr[i] != null_val) { cur->left = new TreeNode(arr[i]); q.push(cur->left); }
        ++i;
        if (i < arr.size() && arr[i] != null_val) { cur->right = new TreeNode(arr[i]); q.push(cur->right); }
        ++i;
    }
    return root;
}
#endif

static inline string _dsa_json_escape(const string& s) {
    string o; o.reserve(s.size() + 8);
    for (unsigned char c : s) {
        if (c == '"') o += "\\\\\\"";
        else if (c == '\\\\') o += "\\\\\\\\";
        else if (c == '\\n') o += "\\\\n";
        else if (c == '\\r') o += "\\\\r";
        else if (c == '\\t') o += "\\\\t";
        else if (c < 0x20) { o += ' '; }
        else o += static_cast<char>(c);
    }
    return o;
}

template <typename T>
static inline string _dsa_fmt(const T& v) { ostringstream oss; oss << v; return oss.str(); }
static inline string _dsa_fmt(bool v) { return v ? "true" : "false"; }
static inline string _dsa_fmt(const string& v) { return "\\"" + v + "\\""; }
template <typename T>
static inline string _dsa_fmt(const vector<T>& v) {
    string o = "[";
    for (size_t i = 0; i < v.size(); ++i) {
        if (i) o += ", ";
        o += _dsa_fmt(v[i]);
    }
    return o + "]";
}

struct _DSACaseOut {
    string name, input, expected, actual, error;
    bool passed;
    double time_ms;
};

static inline void _dsa_emit_json(const vector<_DSACaseOut>& cases, const string& dbg) {
    cout << "__DSA_RESULT__:{\\"cases\\":[";
    for (size_t i = 0; i < cases.size(); ++i) {
        if (i) cout << ",";
        const auto& c = cases[i];
        cout << "{\\"name\\":\\"" << _dsa_json_escape(c.name)
             << "\\",\\"passed\\":" << (c.passed ? "true" : "false")
             << ",\\"input\\":\\"" << _dsa_json_escape(c.input)
             << "\\",\\"expected\\":\\"" << _dsa_json_escape(c.expected)
             << "\\",\\"actual\\":\\"" << _dsa_json_escape(c.actual)
             << "\\",\\"time_ms\\":" << fixed << setprecision(3) << c.time_ms
             << ",\\"error\\":\\"" << _dsa_json_escape(c.error) << "\\"}";
    }
    cout << "],\\"debug_stdout\\":\\"" << _dsa_json_escape(dbg) << "\\"}\\n";
}
'''

def _parse_dsa_stdout(stdout: str) -> Tuple[List[Dict[str, Any]], str]:
    """Extracts structured __DSA_RESULT__ JSON payload and separate debug output."""
    cases = []
    debug_lines = []
    parsed = None
    for line in (stdout or "").splitlines():
        if line.startswith("__DSA_RESULT__:"):
            raw = line[len("__DSA_RESULT__:"):].strip()
            try:
                parsed = json.loads(raw)
            except Exception:
                pass
        else:
            debug_lines.append(line)
    if parsed and isinstance(parsed, dict):
        cases = parsed.get("cases", [])
        dbg = parsed.get("debug_stdout", "")
        combined_dbg = "\n".join(x for x in ["\n".join(debug_lines).strip(), dbg.strip()] if x)
        return cases, combined_dbg
    return [], "\n".join(debug_lines).strip()

def run_dsa_judge(
    language: str,
    user_code: str,
    harness_code: str,
    preamble_code: str = "",
    sample_only: bool = False,
    timeout: int = 8,
) -> Dict[str, Any]:
    """Executes user code against a multi-test-case DSA judge harness in Python 3 or C++17."""
    lang = (language or "python").strip().lower()
    if not user_code or not user_code.strip():
        return {
            "ok": False, "verdict": "Runtime Error", "passed_count": 0, "total_count": 0,
            "cases": [], "debug_stdout": "", "error_detail": "Editor is empty. Write your solution first."
        }

    if lang in ("python", "py", "python3"):
        violation = _check_python_safety(user_code)
        if violation:
            return {
                "ok": False, "verdict": "Security Violation", "passed_count": 0, "total_count": 0,
                "cases": [], "debug_stdout": "", "error_detail": violation
            }
        full_src = (
            _PY_DSA_PRELUDE
            + f"\n__DSA_SAMPLE_ONLY__ = {bool(sample_only)}\n"
            + (preamble_code + "\n" if preamble_code else "")
            + user_code
            + "\n\n"
            + harness_code
        )
        ok, stdout, stderr = _exec_python_source(full_src, timeout=timeout, input_data="")
        if not ok:
            verdict = "Time Limit Exceeded" if "Timed Out" in (stderr or "") else "Runtime Error"
            return {
                "ok": False, "verdict": verdict, "passed_count": 0, "total_count": 0,
                "cases": [], "debug_stdout": stdout.strip(), "error_detail": stderr or stdout
            }
    else:
        violation = _check_cpp_safety(user_code)
        if violation:
            return {
                "ok": False, "verdict": "Security Violation", "passed_count": 0, "total_count": 0,
                "cases": [], "debug_stdout": "", "error_detail": violation
            }
        macro_flag = f"#define DSA_SAMPLE_ONLY {1 if sample_only else 0}\n"
        full_cpp = macro_flag + (preamble_code + "\n" if preamble_code else "") + _CPP_DSA_PRELUDE + "\n" + user_code + "\n\n" + harness_code
        with tempfile.TemporaryDirectory(prefix="dsa_cpp_sandbox_") as temp_dir:
            cpp_file = os.path.join(temp_dir, "judge.cpp")
            exe_file = os.path.join(temp_dir, "judge.out")
            env = _sandbox_env(temp_dir)
            with open(cpp_file, "w", encoding="utf-8") as f:
                f.write(full_cpp)
            rc_c, _, comp_err, comp_to = _run_sandboxed_popen(
                ["g++", "-std=c++17", "-O1", cpp_file, "-o", exe_file],
                cwd=temp_dir, env=env, timeout=10, input_data="",
            )
            if comp_to:
                return {
                    "ok": False, "verdict": "Compile Error", "passed_count": 0, "total_count": 0,
                    "cases": [], "debug_stdout": "", "error_detail": "C++ Compilation Timed Out."
                }
            if rc_c is None:
                return {
                    "ok": False, "verdict": "Compile Error", "passed_count": 0, "total_count": 0,
                    "cases": [], "debug_stdout": "", "error_detail": comp_err or "C++ Compiler unavailable."
                }
            if rc_c != 0:
                return {
                    "ok": False, "verdict": "Compile Error", "passed_count": 0, "total_count": 0,
                    "cases": [], "debug_stdout": "", "error_detail": comp_err
                }
            rc_r, stdout, stderr, run_to = _run_sandboxed_popen(
                [exe_file], cwd=temp_dir, env=env, timeout=timeout, input_data="",
            )
            if run_to:
                return {
                    "ok": False, "verdict": "Time Limit Exceeded", "passed_count": 0, "total_count": 0,
                    "cases": [], "debug_stdout": "", "error_detail": "Execution Timed Out (Check loop termination or algorithm complexity)."
                }
            if rc_r is None:
                return {
                    "ok": False, "verdict": "Runtime Error", "passed_count": 0, "total_count": 0,
                    "cases": [], "debug_stdout": "", "error_detail": stderr or "Execution failed."
                }
            if rc_r != 0:
                return {
                    "ok": False, "verdict": "Runtime Error", "passed_count": 0, "total_count": 0,
                    "cases": [], "debug_stdout": stdout.strip(),
                    "error_detail": stderr or f"Process exited with signal/code {rc_r}"
                }

    cases, dbg = _parse_dsa_stdout(stdout)
    if not cases:
        return {
            "ok": False, "verdict": "Runtime Error", "passed_count": 0, "total_count": 0,
            "cases": [], "debug_stdout": dbg, "error_detail": "Judge harness returned no structured test results.\n" + stdout[:500]
        }
    passed_cnt = sum(1 for c in cases if c.get("passed"))
    total_cnt = len(cases)
    verdict = "Accepted" if passed_cnt == total_cnt else "Wrong Answer"
    return {
        "ok": True,
        "verdict": verdict,
        "passed_count": passed_cnt,
        "total_count": total_cnt,
        "cases": cases,
        "debug_stdout": dbg,
        "error_detail": ""
    }
