import json
import re
from level_content import LEVEL_CONTENT

for case_id, case_data in LEVEL_CONTENT.items():
    if "episodes" not in case_data: continue
    
    for episode in case_data["episodes"]:
        for block in episode.get("blocks", []):
            if block.get("type") == "code_lab":
                
                # Check if it has print statements
                starter = block.get("starter_code", "")
                if starter and "print(" not in starter:
                    # Append a generic print statement to instantiate the class/function
                    # We can use regex to find the class or def name
                    
                    class_match = re.search(r'class (\w+):', starter)
                    def_match = re.search(r'def (\w+)\(', starter)
                    
                    addition = "\n\n# --- Execution Output ---\n"
                    if class_match:
                        cls_name = class_match.group(1)
                        addition += f"obj = {cls_name}()\nprint('Initialized', obj)\n"
                        if "act" in starter:
                            addition += f"print('Action:', obj.act('test_percept'))\n"
                    elif def_match:
                        func_name = def_match.group(1)
                        addition += f"print('Result:', {func_name}(None))\n"
                    else:
                        addition += "print('Execution Complete.')\n"
                    
                    block["starter_code"] = starter + addition
                    block["solution_code"] = block.get("solution_code", "") + addition
                    
            elif block.get("type") == "visual_stepper":
                # Fix broken graphs that have no arrows by adding dummy arrows if missing
                steps = block.get("steps", [])
                for step in steps:
                    code = step.get("mermaid_code", "")
                    if "-->" not in code and "-." not in code and "---" not in code:
                        # Find nodes like P["Performance"]
                        nodes = re.findall(r'([A-Za-z0-9_]+)\["([^"]+)"\]', code)
                        if len(nodes) >= 2:
                            # link them up linearly so it doesn't break rendering
                            links = []
                            for i in range(len(nodes)-1):
                                links.append(f"{nodes[i][0]} --> {nodes[i+1][0]}")
                            step["mermaid_code"] = code + "\n  " + "\n  ".join(links)

with open("level_content.py", "w", encoding="utf-8") as f:
    f.write("LEVEL_CONTENT = \\\n")
    json.dump(LEVEL_CONTENT, f, indent=4, ensure_ascii=False)

print("Fixed code labs and broken graphs!")
