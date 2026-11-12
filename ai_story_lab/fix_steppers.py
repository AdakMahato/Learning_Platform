import json
from level_content import LEVEL_CONTENT

for case_id, case_data in LEVEL_CONTENT.items():
    if case_id in ['4', '6']: continue # Leave gold standards alone!
    
    if "episodes" not in case_data: continue
    
    for episode in case_data["episodes"]:
        for block in episode.get("blocks", []):
            if block.get("type") == "visual_stepper":
                steps = block.get("steps", [])
                if len(steps) == 2:
                    code1 = steps[0].get("mermaid_code", "").strip()
                    code2 = steps[1].get("mermaid_code", "").strip()
                    
                    if code1 == code2 or not code1:
                        # It's a static or empty diagram masquerading as a stepper.
                        # Convert it to a standard visual block.
                        block["type"] = "visual"
                        block["title"] = "Architecture Diagram"
                        block["code"] = code2 if code2 else "graph TD\n  Empty[\"Empty Diagram\"]"
                        del block["steps"]

with open("level_content.py", "w", encoding="utf-8") as f:
    f.write("LEVEL_CONTENT = \\\n")
    json.dump(LEVEL_CONTENT, f, indent=4, ensure_ascii=False)

print("Converted fake steppers to static diagrams!")
