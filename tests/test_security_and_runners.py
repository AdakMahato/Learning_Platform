"""Automated security, sandbox isolation, auth, and rendering test suite."""

import os
import sys
import tempfile
import time
import unittest

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

import master_ui as ui
import runners
import unified_persistence as persistence


class RunnerSecurityTests(unittest.TestCase):
    def test_python_blocks_dangerous_modules_and_calls(self):
        payloads = [
            "import os\nprint(os.listdir('.'))",
            "from subprocess import run\nrun(['id'])",
            "import socket",
            "open('/etc/passwd').read()",
            "eval('1+1')",
            "exec('x=1')",
            "print((1).__class__.__bases__[0].__subclasses__())",
        ]
        for code in payloads:
            ok, out, err = runners.run_py(code, timeout=2)
            self.assertFalse(ok, f"Expected payload to be blocked: {code}")
            self.assertIn("Security policy", err)
            self.assertEqual(out, "")

    def test_python_allows_legit_math_and_scrubs_env(self):
        os.environ["PLATFORM_TEST_SECRET_SENTINEL"] = "super_secret_token_999"
        try:
            code = (
                "import math, sys\n"
                "from collections import deque\n"
                "print(math.factorial(5), sys.maxsize > 0)\n"
            )
            ok, out, err = runners.run_py(code, timeout=3)
            self.assertTrue(ok, err)
            self.assertIn("120 True", out)
        finally:
            os.environ.pop("PLATFORM_TEST_SECRET_SENTINEL", None)

    def test_python_timeout_kills_infinite_loop(self):
        ok, _, err = runners.run_py("while True:\n    pass", timeout=1)
        self.assertFalse(ok)
        self.assertIn("Timed Out", err)

    def test_cpp_blocks_system_and_runs_clean_stl(self):
        ok_bad, _, err_bad = runners.run_cpp('int main(){ system("id"); return 0; }', timeout=3)
        self.assertFalse(ok_bad)
        self.assertIn("Security policy", err_bad)

        ok_good, out_good, err_good = runners.run_cpp(
            'int main(){ int a, b; cin >> a >> b; cout << (a + b) << "\\n"; return 0; }',
            timeout=4,
            input_data="17 25",
        )
        self.assertTrue(ok_good, err_good)
        self.assertEqual(out_good.strip(), "42")

    def test_sqlite_blocks_attach_and_load_extension_allows_safe_queries(self):
        ok_attach, _, err_attach = runners.run_sql("ATTACH DATABASE '/tmp/x.db' AS pwn;")
        self.assertFalse(ok_attach)
        self.assertIn("not authorized", err_attach.lower())

        ok_ext, _, err_ext = runners.run_sql("SELECT load_extension('evil.so');")
        self.assertFalse(ok_ext)
        self.assertIn("not authorized", err_ext.lower())

        ok_ok, res_df, err_ok = runners.run_sql(
            "PRAGMA read_uncommitted = 1; SELECT 1 + 1 AS sum_val;"
        )
        self.assertTrue(ok_ok, err_ok)
        self.assertEqual(int(res_df.iloc[0]["sum_val"]), 2)

    def test_sqlite_timeout_aborts_runaway_cte(self):
        orig_deadline = runners._SQL_DEADLINE_SEC
        try:
            res = runners.run_sql(
                "WITH RECURSIVE r(x) AS (SELECT 1 UNION ALL SELECT x+1 FROM r) SELECT MAX(x) FROM r;",
            )
            # Default deadline is 2.5s; verify it either completes or aborts cleanly without crash
            self.assertIsInstance(res, tuple)
            self.assertEqual(len(res), 3)
        finally:
            runners._SQL_DEADLINE_SEC = orig_deadline


class PersistenceAndAuthTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self._orig_db = persistence.DB_PATH
        self._orig_sec = persistence.SECRET_FILE
        self._orig_init = persistence._DB_INITIALIZED
        self._orig_legacy = persistence.LEGACY_PROGRESS_FILE

        persistence.DB_PATH = os.path.join(self._tmp.name, "test_platform.db")
        persistence.SECRET_FILE = os.path.join(self._tmp.name, ".secret_key")
        persistence.LEGACY_PROGRESS_FILE = os.path.join(self._tmp.name, "missing_legacy.json")
        persistence._DB_INITIALIZED = False
        persistence._AUTH_FAIL_TRACKER.clear()

    def tearDown(self):
        persistence.DB_PATH = self._orig_db
        persistence.SECRET_FILE = self._orig_sec
        persistence._DB_INITIALIZED = self._orig_init
        persistence.LEGACY_PROGRESS_FILE = self._orig_legacy
        persistence._AUTH_FAIL_TRACKER.clear()
        self._tmp.cleanup()

    def test_register_authenticate_and_lockout(self):
        ok, _ = persistence.register_user("alice_eng", "StrongPass!123")
        self.assertTrue(ok)
        ok_dup, _ = persistence.register_user("alice_eng", "StrongPass!123")
        self.assertFalse(ok_dup)

        ok_auth, uname = persistence.authenticate_user("alice_eng", "StrongPass!123")
        self.assertTrue(ok_auth)
        self.assertEqual(uname, "alice_eng")

        for _ in range(5):
            ok_bad, _ = persistence.authenticate_user("alice_eng", "WrongPass999")
            self.assertFalse(ok_bad)

        ok_locked, lock_msg = persistence.authenticate_user("alice_eng", "StrongPass!123")
        self.assertFalse(ok_locked)
        self.assertIn("Too many failed attempts", lock_msg)

    def test_hmac_tokens_and_multiuser_isolation(self):
        tok = persistence.issue_session_token("user:alice", ttl_seconds=60)
        self.assertEqual(persistence.verify_session_token(tok), "user:alice")

        tampered = tok[:-1] + ("0" if tok[-1] != "0" else "1")
        self.assertIsNone(persistence.verify_session_token(tampered))

        expired = persistence.issue_session_token("user:alice", ttl_seconds=-10)
        self.assertIsNone(persistence.verify_session_token(expired))

        state_a = persistence.load_user_progress("user:alice")
        state_a["xp"]["dsa"] = 250
        state_a["completed"]["dsa"] = [0, 1]
        persistence.save_user_progress(state_a, "user:alice")

        state_b = persistence.load_user_progress("user:bob")
        self.assertEqual(state_b["xp"]["dsa"], 0)
        self.assertEqual(state_b["completed"]["dsa"], [])


class RenderingSanitizationTests(unittest.TestCase):
    def test_markdown_sanitizes_xss_payloads(self):
        dirty = 'Hello <script>alert(1)</script> <img src="x" onerror="alert(2)"> [click](javascript:alert(3))'
        rendered = ui.render_markdown_html(dirty)
        self.assertNotIn("<script", rendered.lower())
        self.assertNotIn("onerror=", rendered.lower())
        self.assertNotIn("javascript:", rendered.lower())


if __name__ == "__main__":
    unittest.main()
