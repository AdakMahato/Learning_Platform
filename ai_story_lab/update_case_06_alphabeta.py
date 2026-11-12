import json
from level_content import LEVEL_CONTENT

blocks = LEVEL_CONTENT['6']['episodes'][2]['blocks'] # Module 3

# Wait, Module 3 is currently blocks_mod_3 which was about Depth-Limited Search!
# Where did Alpha-Beta go?
# Alpha-Beta was at the end of Module 1!
blocks_mod_1 = LEVEL_CONTENT['6']['episodes'][0]['blocks']

# Find the static visual block for Alpha-Beta
try:
    idx = next(i for i, b in enumerate(blocks_mod_1) if b.get('title') == 'Visualizing the Prune')

    stepper_block = {
        "type": "visual_stepper",
        "title": "Interactive: Alpha-Beta Pruning Step-by-Step",
        "height": 450,
        "steps": [
            {
                "explanation": "We evaluate Node B. MIN chooses the lowest value (3). The best guarantee for MAX (alpha) is now 3.",
                "mermaid_code": '''
    graph TD
        classDef maxNode fill:rgba(16, 185, 129, 0.1),stroke:#34D399,stroke-width:2px;
        classDef minNode fill:rgba(239, 68, 68, 0.1),stroke:#FCA5A5,stroke-width:2px;

        A[MAX: α=3, β=∞]:::maxNode --> B[MIN: 3]:::minNode
        A --> C[MIN: ?]:::minNode
        
        B --> D[3]
        B --> E[12]
        
        C --> F[2]
        C --> G[?]
        C --> H[?]
                '''
            },
            {
                "explanation": "Now we move to Node C. MIN evaluates its first child, which is 2.",
                "mermaid_code": '''
    graph TD
        classDef maxNode fill:rgba(16, 185, 129, 0.1),stroke:#34D399,stroke-width:2px;
        classDef minNode fill:rgba(239, 68, 68, 0.1),stroke:#FCA5A5,stroke-width:2px;
        classDef focus fill:rgba(255, 255, 255, 0.2),stroke:#FFF,stroke-width:4px;

        A[MAX: α=3, β=∞]:::maxNode --> B[MIN: 3]:::minNode
        A --> C[MIN: ≤2]:::focus
        
        B --> D[3]
        B --> E[12]
        
        C --> F[2]:::focus
        C --> G[?]
        C --> H[?]
                '''
            },
            {
                "explanation": "PRUNE! Node C is currently at ≤2. MAX already has a guaranteed 3 from Node B. Since 2 is worse than 3, and MIN will only make it even worse, MAX will NEVER choose Node C. We can instantly skip evaluating the rest of Node C's children!",
                "mermaid_code": '''
    graph TD
        classDef maxNode fill:rgba(16, 185, 129, 0.1),stroke:#34D399,stroke-width:2px;
        classDef minNode fill:rgba(239, 68, 68, 0.1),stroke:#FCA5A5,stroke-width:2px;
        classDef pruned fill:rgba(0,0,0,0.5),stroke:#333,stroke-width:1px,stroke-dasharray: 5 5;

        A[MAX: 3]:::maxNode --> B[MIN: 3]:::minNode
        A -.-> C[MIN: 2]:::minNode
        
        B --> D[3]
        B --> E[12]
        
        C --> F[2]
        C -.-> G[Pruned]:::pruned
        C -.-> H[Pruned]:::pruned
                '''
            }
        ]
    }

    blocks_mod_1[idx] = stepper_block
    del blocks_mod_1[idx+1] # Remove the manual explanation text

    with open('level_content.py', 'w', encoding='utf-8') as f:
        f.write("LEVEL_CONTENT = \\\n")
        json.dump(LEVEL_CONTENT, f, indent=4, ensure_ascii=False)
except Exception as e:
    print(e)
