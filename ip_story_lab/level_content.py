"""Master Curriculum Database for Image & Video Processing Story Lab."""

import importlib.util
import os

_DIR = os.path.dirname(os.path.abspath(__file__))


def _load_dict(filename: str, attr: str) -> dict:
    path = os.path.join(_DIR, filename)
    spec = importlib.util.spec_from_file_location(f"ip_story_lab_{filename[:-3]}", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return getattr(mod, attr)


LEVEL_CONTENT = {}
LEVEL_CONTENT.update(_load_dict("cases_00_07.py", "CASES_00_07"))
LEVEL_CONTENT.update(_load_dict("cases_08_15.py", "CASES_08_15"))
