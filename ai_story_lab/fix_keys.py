import json
from level_content import LEVEL_CONTENT

new_level_content = {}

for k, v in LEVEL_CONTENT.items():
    if k.startswith("case_"):
        new_k = str(int(k.replace("case_", "")))
        new_level_content[new_k] = v
    else:
        # Keep it unless it's going to be overwritten by a case_ key
        if k not in new_level_content:
            new_level_content[k] = v

with open("level_content.py", "w", encoding="utf-8") as f:
    f.write("LEVEL_CONTENT = \\\n")
    json.dump(new_level_content, f, indent=4, ensure_ascii=False)

print(f"Fixed keys! Total cases: {len(new_level_content)}")
