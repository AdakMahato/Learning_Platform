"""
System Design Story Lab - Unified Level Content Loader (Cases 0..13, 56 Modules)
Uses importlib.util.spec_from_file_location so loading works cleanly even when called
from core_loader.py without adding sd_story_lab/ to sys.path.
"""

import importlib.util
import os

_HERE = os.path.dirname(os.path.abspath(__file__))


def _load_part(filename: str, attr: str):
    path = os.path.join(_HERE, filename)
    spec = importlib.util.spec_from_file_location(f"sd_story_lab.{filename[:-3]}", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return getattr(mod, attr)


SD_CASES_PART1 = _load_part("sd_part1.py", "SD_CASES_PART1")
SD_CASES_PART2 = _load_part("sd_part2.py", "SD_CASES_PART2")
SD_CASES_PART3 = _load_part("sd_part3.py", "SD_CASES_PART3")

LEVEL_CONTENT = {}
for _part in (SD_CASES_PART1, SD_CASES_PART2, SD_CASES_PART3):
    LEVEL_CONTENT.update(_part)
