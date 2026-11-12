import json
from level_content import LEVEL_CONTENT

# Get the blocks we just injected
blocks = LEVEL_CONTENT['6']["episodes"][0]["blocks"]

# Let's break them into multiple episodes
ep1_blocks = blocks[0:5] # Story, Objective, Problem, Concept, Visual
ep2_blocks = blocks[5:9] # Tracing, Beginner Mistake, Leaf node code lab, Time Complexity
ep3_blocks = blocks[9:]  # Alpha-beta concept, Visual, Note, Code Lab

LEVEL_CONTENT['6'] = {
    "episodes": [
        {
            "title": "Module 1: The Nemesis Protocol",
            "blocks": ep1_blocks
        },
        {
            "title": "Module 2: The Minimax Algorithm",
            "blocks": ep2_blocks
        },
        {
            "title": "Module 3: Alpha-Beta Pruning",
            "blocks": ep3_blocks
        }
    ]
}

with open('level_content.py', 'w', encoding='utf-8') as f:
    f.write("LEVEL_CONTENT = \\\n")
    json.dump(LEVEL_CONTENT, f, indent=4, ensure_ascii=False)

print("Split Case 06 into 3 modules!")
