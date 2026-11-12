import json
import traceback

from level_content import LEVEL_CONTENT
import sys
sys.path.append("/Users/aadarshamahato/Downloads/LEARNING_PLATFORM/dbms_story_lab/")

try:
    from deep_01_05 import CONTENT_01_05
    LEVEL_CONTENT.update(CONTENT_01_05)
except Exception as e:
    print(f"Error loading 01-05: {e}")
    traceback.print_exc()

try:
    from deep_07_11 import CONTENT_07_11
    LEVEL_CONTENT.update(CONTENT_07_11)
except Exception as e:
    print(f"Error loading 07-11: {e}")
    traceback.print_exc()

try:
    from deep_12_16 import CONTENT_12_16
    LEVEL_CONTENT.update(CONTENT_12_16)
except Exception as e:
    print(f"Error loading 12-16: {e}")
    traceback.print_exc()

try:
    from deep_17_24 import CONTENT_17_24
    LEVEL_CONTENT.update(CONTENT_17_24)
except Exception as e:
    print(f"Error loading 17-24: {e}")
    traceback.print_exc()

with open("level_content.py", "w", encoding="utf-8") as f:
    f.write("LEVEL_CONTENT = \\\n")
    json.dump(LEVEL_CONTENT, f, indent=4, ensure_ascii=False)

print(f"Successfully merged extreme depth curriculum! Total cases: {len(LEVEL_CONTENT)}")
