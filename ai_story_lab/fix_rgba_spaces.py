import json
import re
from level_content import LEVEL_CONTENT

def fix_spaces(code):
    # Find all rgba(..., ..., ...) and remove spaces inside the parentheses
    def repl(m):
        return m.group(0).replace(" ", "")
    
    return re.sub(r'rgba\([^)]+\)', repl, code)

# Iterate through all blocks
for ep in LEVEL_CONTENT['6']['episodes']:
    for b in ep['blocks']:
        if 'code' in b and b['type'] == 'visual':
            b['code'] = fix_spaces(b['code'])
        
        if 'steps' in b:
            for s in b['steps']:
                if 'mermaid_code' in s:
                    s['mermaid_code'] = fix_spaces(s['mermaid_code'])

with open('level_content.py', 'w', encoding='utf-8') as f:
    f.write("LEVEL_CONTENT = \\\n")
    json.dump(LEVEL_CONTENT, f, indent=4, ensure_ascii=False)

print("Fixed rgba spaces!")
