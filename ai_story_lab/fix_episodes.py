import json
from level_content import LEVEL_CONTENT

for key, data in LEVEL_CONTENT.items():
    if "modules" in data:
        data["episodes"] = data.pop("modules")

with open("level_content.py", "w", encoding="utf-8") as f:
    f.write("LEVEL_CONTENT = \\\n")
    json.dump(LEVEL_CONTENT, f, indent=4, ensure_ascii=False)

print("Fixed modules -> episodes keys!")
