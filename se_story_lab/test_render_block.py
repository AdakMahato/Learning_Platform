import json
import ui
from unittest.mock import MagicMock

with open("/Users/aadarshamahato/Downloads/LEARNING_PLATFORM/se_story_lab/level_content.py") as f:
    data = json.loads(f.read().split("LEVEL_CONTENT = ", 1)[1])

# Case 00 Module 3 has the code_lab block:
m3_blocks = data["0"]["episodes"][2]["blocks"]
codelab_block = next(b for b in m3_blocks if b.get("type") == "code_lab")

print("Found codelab block:", codelab_block.get("title"))
print("edge_cases type:", type(codelab_block.get("edge_cases")))
print("why_works type:", type(codelab_block.get("why_works")))
print("alternatives type:", type(codelab_block.get("alternatives")))

# Test that the block has all expected keys
assert "edge_cases" in codelab_block
assert "why_works" in codelab_block
assert "alternatives" in codelab_block
print("All keys present and verified!")
