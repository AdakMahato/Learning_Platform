import json
from level_content import LEVEL_CONTENT

# Add explanations to all quizzes in Case 00
# And expand Module 4 to explain ML types

# Mod 1 Quiz
LEVEL_CONTENT['0']['episodes'][0]['blocks'][-1]['explanation'] = "Traditional Programming relies on human-written logical branches (like massive 'if/else' blocks). Machine Learning requires the machine to generate the logic itself from data."

# Mod 2 Quiz
LEVEL_CONTENT['0']['episodes'][1]['blocks'][-1]['explanation'] = "Cognitive Modeling focuses on mimicking the internal psychological processes of human thought. The Rational Agent approach (the modern standard) only cares about the mathematical outcome."

# Mod 3 Quiz
LEVEL_CONTENT['0']['episodes'][2]['blocks'][-1]['explanation'] = "The Chinese Room argument proves that a system can perfectly simulate conversational fluency (passing the Turing Test) without possessing any actual conscious 'understanding' of the words."

# Re-write Mod 4 blocks to explain the ML branches
mod4_blocks = LEVEL_CONTENT['0']['episodes'][3]['blocks']
new_mod4_blocks = []

for b in mod4_blocks:
    if b.get("title") == "The AI Umbrella":
        # Insert new concept blocks right before the visual
        new_mod4_blocks.append({
            "type": "concept",
            "title": "Supervised vs Unsupervised Learning",
            "content": "**Supervised Learning:** You give the AI a massive dataset of pictures labeled 'Dog' and 'Cat'. It learns to predict the label of a new picture. (Used for Classification).\n\n**Unsupervised Learning:** You give the AI a massive dataset of pictures with NO labels. It figures out how to group them together based on visual similarities. (Used for Clustering)."
        })
        new_mod4_blocks.append({
            "type": "concept",
            "title": "Reinforcement Learning",
            "content": "You don't give the AI any data. You drop it into a simulated environment (like a video game) and give it a 'Score'. It takes random actions, learns what actions increase its Score, and eventually becomes a superhuman master of the environment."
        })
    new_mod4_blocks.append(b)

# Update Mod 4 Quiz explanation
new_mod4_blocks[-1]['explanation'] = "Symbolic AI (GOFAI) dominated early AI research because computers didn't have enough power to run Neural Networks. It relied on hard-coded 'Symbols' and logical rules."

LEVEL_CONTENT['0']['episodes'][3]['blocks'] = new_mod4_blocks

with open('level_content.py', 'w', encoding='utf-8') as f:
    f.write("LEVEL_CONTENT = \\\n")
    json.dump(LEVEL_CONTENT, f, indent=4, ensure_ascii=False)

print("Fixed Case 00 explanations!")
