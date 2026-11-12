import json
import random

from level_content import LEVEL_CONTENT

random.seed(42) # For reproducibility

for case_id, case_data in LEVEL_CONTENT.items():
    if "episodes" not in case_data: continue
    
    for episode in case_data["episodes"]:
        for block in episode.get("blocks", []):
            if block.get("type") == "interactive":
                
                # 1. Add explanation if missing
                if "explanation" not in block:
                    ans = block.get("answer", "")
                    block["explanation"] = f"The correct answer is **{ans}**. Understanding why the other approaches fail here is critical for designing robust AI architectures."
                
                # 2. Convert some to fill_in_the_blank
                if random.random() < 0.35: # 35% chance
                    question = block.get("question", "")
                    answer = block.get("answer", "")
                    
                    # Try to formulate a fill-in-the-blank question
                    # E.g. "What does an agent use to perceive?" -> "An agent uses _____ to perceive its environment."
                    # If we can't do it smartly, just append "_____"
                    
                    new_q = question
                    if question.startswith("What is "):
                        new_q = question.replace("What is ", "_____ is ", 1).replace("?", ".")
                    elif question.startswith("What does "):
                        new_q = question.replace("What does ", "_____ ", 1).replace("?", ".")
                    else:
                        new_q = f"{question}\n\nAnswer: _____"
                    
                    block["type"] = "fill_in_the_blank"
                    block["question"] = new_q
                    # Keep the answer the same
                    # Remove options
                    if "options" in block:
                        del block["options"]

with open("level_content.py", "w", encoding="utf-8") as f:
    f.write("LEVEL_CONTENT = \\\n")
    json.dump(LEVEL_CONTENT, f, indent=4, ensure_ascii=False)

print("Upgraded all quizzes across the platform!")
