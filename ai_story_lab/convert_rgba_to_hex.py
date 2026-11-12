import json
from level_content import LEVEL_CONTENT

# Hex replacements mapping
replacements = {
    "rgba(16,185,129,0.1)": "#10b9811a",
    "rgba(239,68,68,0.1)": "#ef44441a",
    "rgba(124,77,255,0.1)": "#7c4dff1a",
    "rgba(255,255,255,0.2)": "#ffffff33",
    "rgba(0,0,0,0.5)": "#00000080"
}

def replace_all(text):
    for k, v in replacements.items():
        text = text.replace(k, v)
    return text

# Iterate through all blocks
for ep in LEVEL_CONTENT['6']['episodes']:
    for b in ep['blocks']:
        if 'code' in b and b['type'] == 'visual':
            b['code'] = replace_all(b['code'])
        
        if 'steps' in b:
            for s in b['steps']:
                if 'mermaid_code' in s:
                    s['mermaid_code'] = replace_all(s['mermaid_code'])

with open('level_content.py', 'w', encoding='utf-8') as f:
    f.write("LEVEL_CONTENT = \\\n")
    json.dump(LEVEL_CONTENT, f, indent=4, ensure_ascii=False)

print("Replaced rgba with hex!")
