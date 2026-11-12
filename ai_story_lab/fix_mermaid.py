import json
import re
from level_content import LEVEL_CONTENT

def fix_mermaid(code):
    # Find all node definitions like A[Something] and replace with A["Something"]
    # But only if it doesn't already have quotes.
    # Be careful, we just want to replace the contents inside [] with quotes if they aren't there.
    def repl(m):
        content = m.group(1)
        if not content.startswith('"'):
            content = f'"{content}"'
        return f'[{content}]'
    
    return re.sub(r'\[(.*?)\]', repl, code)

# Iterate through all blocks in Case 6 and fix mermaid codes
for ep in LEVEL_CONTENT['6']['episodes']:
    for b in ep['blocks']:
        if 'code' in b and b['type'] == 'visual':
            b['code'] = fix_mermaid(b['code'])
        
        if 'steps' in b:
            for s in b['steps']:
                if 'mermaid_code' in s:
                    s['mermaid_code'] = fix_mermaid(s['mermaid_code'])

with open('level_content.py', 'w', encoding='utf-8') as f:
    f.write("LEVEL_CONTENT = \\\n")
    json.dump(LEVEL_CONTENT, f, indent=4, ensure_ascii=False)

print("Fixed mermaid syntax errors!")
