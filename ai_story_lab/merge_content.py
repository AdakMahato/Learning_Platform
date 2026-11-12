import json
import traceback

from level_content import LEVEL_CONTENT

try:
    from content_01_07 import CONTENT_01_07
    LEVEL_CONTENT.update(CONTENT_01_07)
except Exception as e:
    print(f"Error loading 01-07: {e}")

try:
    from content_08_15 import CONTENT_08_15
    LEVEL_CONTENT.update(CONTENT_08_15)
except Exception as e:
    print(f"Error loading 08-15: {e}")

try:
    from content_16_24 import CONTENT_16_24
    LEVEL_CONTENT.update(CONTENT_16_24)
except Exception as e:
    print(f"Error loading 16-24: {e}")

with open("level_content.py", "w", encoding="utf-8") as f:
    f.write("LEVEL_CONTENT = \\\n")
    json.dump(LEVEL_CONTENT, f, indent=4, ensure_ascii=False)

print(f"Successfully merged curriculum! Total cases: {len(LEVEL_CONTENT)}")
