"""
DSA Story Lab - Unified Level Content Loader (Cases 0..18, 76 Modules, 38 Judge Problems)
Uses importlib.util.spec_from_file_location so loading works cleanly even when called
from core_loader.py without adding dsa_story_lab/ to sys.path.
"""

import importlib.util
import os

_HERE = os.path.dirname(os.path.abspath(__file__))


def _load_part(filename: str, attr: str):
    path = os.path.join(_HERE, filename)
    spec = importlib.util.spec_from_file_location(f"dsa_story_lab.{filename[:-3]}", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return getattr(mod, attr)


CASES_PART1 = _load_part("dsa_part1.py", "CASES_PART1")
CASES_PART2 = _load_part("dsa_part2.py", "CASES_PART2")
CASES_PART3 = _load_part("dsa_part3.py", "CASES_PART3")
CASES_PART4 = _load_part("dsa_part4.py", "CASES_PART4")
CASES_PART5 = _load_part("dsa_part5.py", "CASES_PART5")

LEVEL_CONTENT = {}
for _part in (CASES_PART1, CASES_PART2, CASES_PART3, CASES_PART4, CASES_PART5):
    LEVEL_CONTENT.update(_part)
