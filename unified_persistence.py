"""
Unified Multi-User Persistence & Authentication Engine for Engineering Story Labs.
Backed by thread-safe SQLite WAL storage with PBKDF2-SHA256 credential hashing,
HMAC-SHA256 session tokens, and automatic local migration.
"""

import copy
import datetime
import hashlib
import hmac
import json
import os
import re
import secrets
import sqlite3
import threading
import time
from typing import Dict, Any, Tuple, Optional

import streamlit as st

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
LEGACY_PROGRESS_FILE = os.path.join(BASE_DIR, "platform_progress.json")
DB_PATH = os.environ.get("PLATFORM_DB_PATH") or os.path.join(DATA_DIR, "platform.db")
SECRET_FILE = os.path.join(DATA_DIR, ".secret_key")

SUBJECT_IDS = ("dbms", "ai", "se", "cloud", "oop", "dsa", "sd", "ip")
USERNAME_RE = re.compile(r"^[a-zA-Z0-9_.-]{3,32}$")
_PBKDF2_ITERS = 260_000
_DB_INIT_LOCK = threading.Lock()
_DB_INITIALIZED = False
_AUTH_RATE_LOCK = threading.Lock()
_AUTH_FAIL_TRACKER: Dict[str, Tuple[int, float]] = {}

DEFAULT_STATE = {
    "completed": {sid: [] for sid in SUBJECT_IDS},
    "active_modules": {},
    "completed_modules": [],
    "solved_challenges": [],
    "bookmarks": [],
    "xp": {sid: 0 for sid in SUBJECT_IDS},
    "last_activity": None,
}


def get_auth_mode() -> str:
    """Returns active deployment auth mode: 'local', 'multiuser', or 'required'."""
    mode = (os.environ.get("PLATFORM_AUTH_MODE") or "local").strip().lower()
    return mode if mode in ("local", "multiuser", "required") else "local"


def _ensure_data_dir():
    os.makedirs(DATA_DIR, mode=0o700, exist_ok=True)
    db_parent = os.path.dirname(os.path.abspath(DB_PATH))
    if db_parent:
        os.makedirs(db_parent, mode=0o700, exist_ok=True)


def _get_secret_key() -> bytes:
    env_key = os.environ.get("PLATFORM_SECRET_KEY", "").strip()
    if len(env_key) >= 16:
        return env_key.encode("utf-8")
    _ensure_data_dir()
    if os.path.exists(SECRET_FILE):
        with open(SECRET_FILE, "r", encoding="utf-8") as f:
            stored = f.read().strip()
            if len(stored) >= 32:
                return stored.encode("utf-8")
    generated = secrets.token_hex(32)
    fd = os.open(SECRET_FILE, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write(generated)
    return generated.encode("utf-8")


def _get_conn() -> sqlite3.Connection:
    _ensure_db_schema()
    conn = sqlite3.connect(DB_PATH, timeout=10.0, check_same_thread=False)
    conn.execute("PRAGMA busy_timeout = 5000;")
    return conn


def _normalize_state(data: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    out = copy.deepcopy(DEFAULT_STATE)
    if not isinstance(data, dict):
        return out
    comp = data.get("completed") or {}
    xp = data.get("xp") or {}
    for sid in SUBJECT_IDS:
        vals = comp.get(sid, [])
        out["completed"][sid] = [int(v) for v in vals if isinstance(v, (int, float)) or str(v).isdigit()]
        try:
            out["xp"][sid] = max(0, int(xp.get(sid, 0)))
        except (TypeError, ValueError):
            out["xp"][sid] = 0
    if isinstance(data.get("active_modules"), dict):
        out["active_modules"] = {
            str(k): int(v) for k, v in data["active_modules"].items() if isinstance(v, (int, float))
        }
    if isinstance(data.get("completed_modules"), list):
        out["completed_modules"] = [str(x) for x in data["completed_modules"]]
    if isinstance(data.get("solved_challenges"), list):
        out["solved_challenges"] = [str(x) for x in data["solved_challenges"]]
    if isinstance(data.get("bookmarks"), list):
        out["bookmarks"] = [str(x) for x in data["bookmarks"]]
    if isinstance(data.get("last_activity"), dict):
        out["last_activity"] = data["last_activity"]
    return out


def _ensure_db_schema():
    global _DB_INITIALIZED
    if _DB_INITIALIZED and os.path.exists(DB_PATH):
        return
    with _DB_INIT_LOCK:
        _ensure_data_dir()
        conn = sqlite3.connect(DB_PATH, timeout=10.0)
        try:
            conn.execute("PRAGMA journal_mode = WAL;")
            conn.execute("PRAGMA synchronous = NORMAL;")
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                    username TEXT PRIMARY KEY,
                    pw_hash TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    last_login TEXT NOT NULL
                )
                """
            )
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS user_progress (
                    user_key TEXT PRIMARY KEY,
                    state_json TEXT NOT NULL,
                    updated_at TEXT NOT NULL
                )
                """
            )
            # One-time migration from legacy platform_progress.json into 'local' profile
            row = conn.execute(
                "SELECT 1 FROM user_progress WHERE user_key = 'local'"
            ).fetchone()
            if row is None and os.path.exists(LEGACY_PROGRESS_FILE):
                try:
                    with open(LEGACY_PROGRESS_FILE, "r", encoding="utf-8") as f:
                        legacy = _normalize_state(json.load(f))
                    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
                    conn.execute(
                        "INSERT INTO user_progress (user_key, state_json, updated_at) VALUES (?, ?, ?)",
                        ("local", json.dumps(legacy), now),
                    )
                except Exception:
                    pass
            conn.commit()
            _DB_INITIALIZED = True
        finally:
            conn.close()


def _hash_password(password: str) -> str:
    salt = os.urandom(16)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, _PBKDF2_ITERS)
    return f"pbkdf2_sha256${_PBKDF2_ITERS}${salt.hex()}${digest.hex()}"


def _verify_password(password: str, stored_hash: str) -> bool:
    try:
        alg, iters_s, salt_hex, hash_hex = stored_hash.split("$", 3)
        if alg != "pbkdf2_sha256":
            return False
        iters = int(iters_s)
        salt = bytes.fromhex(salt_hex)
        expected = bytes.fromhex(hash_hex)
        actual = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, iters)
        return hmac.compare_digest(actual, expected)
    except Exception:
        return False


def issue_session_token(user_key: str, ttl_seconds: int = 7 * 86400) -> str:
    exp = int(time.time()) + ttl_seconds
    payload = f"{user_key}|{exp}"
    sig = hmac.new(_get_secret_key(), payload.encode("utf-8"), hashlib.sha256).hexdigest()
    return f"{payload}|{sig}"


def verify_session_token(token: str) -> Optional[str]:
    try:
        user_key, exp_s, sig = str(token).rsplit("|", 2)
        if int(exp_s) < int(time.time()):
            return None
        payload = f"{user_key}|{exp_s}"
        expected = hmac.new(_get_secret_key(), payload.encode("utf-8"), hashlib.sha256).hexdigest()
        if hmac.compare_digest(sig, expected):
            return user_key
    except Exception:
        return None
    return None


def register_user(username: str, password: str) -> Tuple[bool, str]:
    uname = (username or "").strip().lower()
    if not USERNAME_RE.match(uname):
        return False, "Username must be 3-32 characters (letters, digits, '.', '_', '-')."
    if not password or len(password) < 8:
        return False, "Password must be at least 8 characters long."
    if len(password) > 128:
        return False, "Password exceeds 128 character limit."

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    pw_hash = _hash_password(password)
    conn = _get_conn()
    try:
        exists = conn.execute("SELECT 1 FROM users WHERE username = ?", (uname,)).fetchone()
        if exists:
            return False, "That username is already registered."
        conn.execute(
            "INSERT INTO users (username, pw_hash, created_at, last_login) VALUES (?, ?, ?, ?)",
            (uname, pw_hash, now, now),
        )
        conn.commit()
        return True, uname
    finally:
        conn.close()


def authenticate_user(username: str, password: str) -> Tuple[bool, str]:
    uname = (username or "").strip().lower()
    if not USERNAME_RE.match(uname) or not password or len(password) > 128:
        return False, "Invalid username or password format."

    now_ts = time.time()
    with _AUTH_RATE_LOCK:
        fails, locked_until = _AUTH_FAIL_TRACKER.get(uname, (0, 0.0))
        if now_ts < locked_until:
            wait_s = int(locked_until - now_ts) + 1
            return False, f"Too many failed attempts for this account. Retry in {wait_s}s."

    conn = _get_conn()
    try:
        row = conn.execute("SELECT pw_hash FROM users WHERE username = ?", (uname,)).fetchone()
        if not row or not _verify_password(password, row[0]):
            with _AUTH_RATE_LOCK:
                fails, _ = _AUTH_FAIL_TRACKER.get(uname, (0, 0.0))
                fails += 1
                if fails >= 5:
                    _AUTH_FAIL_TRACKER[uname] = (0, now_ts + 30.0)
                else:
                    _AUTH_FAIL_TRACKER[uname] = (fails, 0.0)
            return False, "Invalid username or password."

        with _AUTH_RATE_LOCK:
            _AUTH_FAIL_TRACKER.pop(uname, None)
        now_iso = datetime.datetime.now(datetime.timezone.utc).isoformat()
        conn.execute("UPDATE users SET last_login = ? WHERE username = ?", (now_iso, uname))
        conn.commit()
        return True, uname
    finally:
        conn.close()


def set_authenticated_user(username: Optional[str]):
    """Switches active workspace identity and reloads user state cleanly."""
    if username:
        st.session_state["auth_username"] = username
        st.session_state["auth_token"] = issue_session_token(f"user:{username}")
    else:
        st.session_state.pop("auth_username", None)
        st.session_state.pop("auth_token", None)
    st.session_state.pop("platform_initialized", None)
    st.session_state.pop("_loaded_user_key", None)
    init_progress()


def get_current_identity() -> Tuple[Optional[str], str, bool]:
    """Returns (user_key, display_label, is_authenticated)."""
    token = st.session_state.get("auth_token")
    if token:
        verified = verify_session_token(token)
        if verified and verified.startswith("user:"):
            uname = verified.split(":", 1)[1]
            return verified, f"@{uname}", True
        st.session_state.pop("auth_token", None)
        st.session_state.pop("auth_username", None)

    mode = get_auth_mode()
    if mode == "required":
        return None, "Sign In Required", False
    if mode == "multiuser":
        guest_id = st.session_state.get("_guest_workspace_id")
        if not guest_id:
            guest_id = f"guest:{secrets.token_hex(8)}"
            st.session_state["_guest_workspace_id"] = guest_id
        return guest_id, "Guest Session", False
    return "local", "Local Workspace", False


def load_user_progress(user_key: Optional[str] = None) -> Dict[str, Any]:
    ukey = user_key or get_current_identity()[0]
    if not ukey:
        return copy.deepcopy(DEFAULT_STATE)
    conn = _get_conn()
    try:
        row = conn.execute(
            "SELECT state_json FROM user_progress WHERE user_key = ?", (ukey,)
        ).fetchone()
        if row:
            return _normalize_state(json.loads(row[0]))
    except Exception:
        pass
    finally:
        conn.close()
    return copy.deepcopy(DEFAULT_STATE)


def save_user_progress(data: Dict[str, Any], user_key: Optional[str] = None):
    ukey = user_key or get_current_identity()[0]
    if not ukey:
        return
    clean = _normalize_state(data)
    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    conn = _get_conn()
    try:
        conn.execute(
            """
            INSERT INTO user_progress (user_key, state_json, updated_at)
            VALUES (?, ?, ?)
            ON CONFLICT(user_key) DO UPDATE SET
                state_json = excluded.state_json,
                updated_at = excluded.updated_at
            """,
            (ukey, json.dumps(clean), now),
        )
        conn.commit()
    except Exception as exc:
        print(f"Warning: could not persist user progress: {exc}")
    finally:
        conn.close()


# Legacy wrapper aliases kept for compatibility
def load_disk_progress() -> Dict[str, Any]:
    return load_user_progress("local")


def save_disk_progress(data: Dict[str, Any]):
    save_user_progress(data, "local")


def init_progress():
    ukey, _, _ = get_current_identity()
    if not st.session_state.get("platform_initialized") or st.session_state.get("_loaded_user_key") != ukey:
        disk_data = load_user_progress(ukey)
        st.session_state["completed"] = {k: set(v) for k, v in disk_data["completed"].items()}
        st.session_state["active_modules"] = disk_data["active_modules"]
        st.session_state["completed_modules"] = set(disk_data.get("completed_modules", []))
        st.session_state["solved_challenges"] = set(disk_data.get("solved_challenges", []))
        st.session_state["bookmarks"] = set(disk_data.get("bookmarks", []))
        st.session_state["xp"] = disk_data["xp"]
        st.session_state["last_activity"] = disk_data["last_activity"]
        st.session_state["_loaded_user_key"] = ukey
        st.session_state["platform_initialized"] = True


def save_progress():
    if not st.session_state.get("platform_initialized"):
        return
    disk_data = {
        "completed": {k: sorted(list(v)) for k, v in st.session_state["completed"].items()},
        "active_modules": st.session_state["active_modules"],
        "completed_modules": sorted(list(st.session_state.get("completed_modules", set()))),
        "solved_challenges": sorted(list(st.session_state.get("solved_challenges", set()))),
        "bookmarks": sorted(list(st.session_state.get("bookmarks", set()))),
        "xp": st.session_state["xp"],
        "last_activity": st.session_state.get("last_activity"),
    }
    save_user_progress(disk_data)


def is_case_bookmarked(subject_id: str, case_id: int) -> bool:
    init_progress()
    return f"{subject_id}:{case_id}" in st.session_state.get("bookmarks", set())


def toggle_bookmark(subject_id: str, case_id: int) -> bool:
    init_progress()
    bset = st.session_state.setdefault("bookmarks", set())
    bkey = f"{subject_id}:{case_id}"
    if bkey in bset:
        bset.remove(bkey)
        added = False
    else:
        bset.add(bkey)
        added = True
    save_progress()
    return added


def get_active_module(subject_id: str, case_id: int) -> int:
    init_progress()
    key = f"{subject_id}_{case_id}"
    return st.session_state["active_modules"].get(key, 1)


def set_active_module(subject_id: str, case_id: int, module_num: int):
    init_progress()
    key = f"{subject_id}_{case_id}"
    st.session_state["active_modules"][key] = module_num
    st.session_state["last_activity"] = {"subject": subject_id, "case_id": case_id, "module": module_num}
    save_progress()


def complete_module(subject_id: str, case_id: int, current_module: int, total_modules: int):
    init_progress()
    next_mod = min(current_module + 1, total_modules)
    key = f"{subject_id}_{case_id}"
    st.session_state["active_modules"][key] = max(st.session_state["active_modules"].get(key, 1), next_mod)

    mod_key = f"{subject_id}_{case_id}_m{current_module}"
    completed_mods = st.session_state.setdefault("completed_modules", set())
    if mod_key not in completed_mods:
        completed_mods.add(mod_key)
        st.session_state["xp"][subject_id] = st.session_state["xp"].get(subject_id, 0) + 50

    if current_module == total_modules:
        st.session_state["completed"].setdefault(subject_id, set()).add(case_id)

    st.session_state["last_activity"] = {"subject": subject_id, "case_id": case_id, "module": next_mod}
    save_progress()


def has_solved_challenge(challenge_key: str) -> bool:
    init_progress()
    return challenge_key in st.session_state.get("solved_challenges", set())


def award_challenge_xp(subject_id: str, amount: int = 15, challenge_key: str = None) -> bool:
    init_progress()
    solved = st.session_state.setdefault("solved_challenges", set())
    if challenge_key:
        if challenge_key in solved:
            return False
        solved.add(challenge_key)
    st.session_state["xp"][subject_id] = st.session_state["xp"].get(subject_id, 0) + amount
    save_progress()
    return True


def get_case_status(subject_id: str, case_id: int, total_modules: int = 4) -> Tuple[str, str, int]:
    init_progress()
    completed_set = st.session_state["completed"].get(subject_id, set())
    if case_id in completed_set:
        return "Completed", "completed", total_modules

    active_mod = get_active_module(subject_id, case_id)
    if active_mod > 1:
        return f"In Progress · M{active_mod}", "progress", active_mod

    return "Unstarted", "locked", 1


def get_subject_stats(subject_id: str, total_cases: int) -> Tuple[int, int, int, int]:
    init_progress()
    completed = len(st.session_state["completed"].get(subject_id, set()))
    xp = st.session_state["xp"].get(subject_id, 0)
    pct = int((completed / max(1, total_cases)) * 100)
    return completed, total_cases, pct, xp


def get_global_stats(all_subjects: list) -> Dict[str, Any]:
    init_progress()
    total_cases = 0
    total_completed = 0
    total_xp = sum(st.session_state["xp"].values())

    for s in all_subjects:
        sid = s["meta"]["id"]
        cnt = len(s["stories"])
        total_cases += cnt
        total_completed += len(st.session_state["completed"].get(sid, set()))

    global_pct = int((total_completed / max(1, total_cases)) * 100)

    if total_xp >= 4000:
        rank = "Principal Architect"
    elif total_xp >= 2000:
        rank = "Staff Engineer"
    elif total_xp >= 1000:
        rank = "Senior Engineer"
    elif total_xp >= 400:
        rank = "Systems Engineer II"
    elif total_xp >= 100:
        rank = "Associate Engineer"
    else:
        rank = "Apprentice"

    return {
        "total_cases": total_cases,
        "total_completed": total_completed,
        "global_pct": global_pct,
        "total_xp": total_xp,
        "rank": rank,
        "last_activity": st.session_state.get("last_activity"),
    }


def reset_subject_progress(subject_id: str):
    init_progress()
    st.session_state["completed"][subject_id] = set()
    st.session_state["xp"][subject_id] = 0

    prefix = f"{subject_id}_"
    for k in list(st.session_state["active_modules"].keys()):
        if k.startswith(prefix):
            del st.session_state["active_modules"][k]
    st.session_state["completed_modules"] = {
        k for k in st.session_state.get("completed_modules", set()) if not k.startswith(prefix)
    }
    st.session_state["solved_challenges"] = {
        k for k in st.session_state.get("solved_challenges", set()) if not k.startswith(prefix)
    }
    st.session_state["bookmarks"] = {
        k for k in st.session_state.get("bookmarks", set()) if not k.startswith(f"{subject_id}:")
    }

    save_progress()


def reset_all_progress():
    init_progress()
    for sid in SUBJECT_IDS:
        st.session_state["completed"][sid] = set()
        st.session_state["xp"][sid] = 0
    st.session_state["active_modules"] = {}
    st.session_state["completed_modules"] = set()
    st.session_state["solved_challenges"] = set()
    st.session_state["bookmarks"] = set()
    st.session_state["last_activity"] = None
    save_progress()
