import json

with open("/Users/aadarshamahato/Downloads/LEARNING_PLATFORM/se_story_lab/level_content.py") as f:
    text = f.read()

data = json.loads(text.split("LEVEL_CONTENT = ", 1)[1])

found = 0
for cid, case in data.items():
    for m_idx, ep in enumerate(case.get("episodes", [])):
        for b_idx, b in enumerate(ep.get("blocks", [])):
            if b.get("type") in ("visual", "mermaid_diagram"):
                code = b.get("code", "")
                header = code.strip().splitlines()[0] if code.strip() else ""
                title = b.get("title", "Untitled")
                
                # Check for <<interface>> in flowchart/graph
                if ("graph TD" in header or "graph LR" in header or "flowchart" in header):
                    if "<<" in code or ">>" in code:
                        print(f"SUSPICIOUS in Case {cid} M{m_idx+1} '{title}': contains '<<' or '>>' in graph TD/LR")
                        found += 1
                    if "&" in code and ("-->" in code or "-.->" in code):
                        # Multiple targets with & like 'C1 & C2 --> S1 & S2' can sometimes fail depending on mermaid version
                        pass

print(f"Scan complete. Found {found} suspicious diagrams.")
