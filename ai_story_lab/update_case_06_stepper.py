import json
from level_content import LEVEL_CONTENT

blocks = LEVEL_CONTENT['6']['episodes'][0]['blocks']

# Find the static visual block
idx = next(i for i, b in enumerate(blocks) if b.get('title') == 'The Minimax Decision Tree')

stepper_block = {
    "type": "visual_stepper",
    "title": "Interactive: Minimax Evaluation Step-by-Step",
    "height": 450,
    "steps": [
        {
            "explanation": "We start at the root (Node A). It is MAX's turn. But MAX cannot make a decision until the entire tree is expanded down to the leaf nodes.",
            "mermaid_code": '''
graph TD
    classDef maxNode fill:rgba(16, 185, 129, 0.1),stroke:#34D399,stroke-width:2px;
    classDef minNode fill:rgba(239, 68, 68, 0.1),stroke:#FCA5A5,stroke-width:2px;
    classDef leafNode fill:rgba(124, 77, 255, 0.1),stroke:#7C4DFF,stroke-width:2px;
    classDef focus fill:rgba(255, 255, 255, 0.2),stroke:#FFF,stroke-width:4px;

    A[MAX: ?]:::focus --> B[MIN: ?]:::minNode
    A --> C[MIN: ?]:::minNode
    
    B --> D[+3]:::leafNode
    B --> E[+12]:::leafNode
    B --> F[+8]:::leafNode
    
    C --> G[+2]:::leafNode
    C --> H[+4]:::leafNode
    C --> I[+6]:::leafNode
            '''
        },
        {
            "explanation": "We expand down to Node B. It is MIN's turn. MIN looks at its children (the leaf nodes) which evaluate to +3, +12, and +8.",
            "mermaid_code": '''
graph TD
    classDef maxNode fill:rgba(16, 185, 129, 0.1),stroke:#34D399,stroke-width:2px;
    classDef minNode fill:rgba(239, 68, 68, 0.1),stroke:#FCA5A5,stroke-width:2px;
    classDef leafNode fill:rgba(124, 77, 255, 0.1),stroke:#7C4DFF,stroke-width:2px;
    classDef focus fill:rgba(255, 255, 255, 0.2),stroke:#FFF,stroke-width:4px;

    A[MAX: ?]:::maxNode --> B[MIN: ?]:::focus
    A --> C[MIN: ?]:::minNode
    
    B --> D[+3]:::focus
    B --> E[+12]:::focus
    B --> F[+8]:::focus
    
    C --> G[+2]:::leafNode
    C --> H[+4]:::leafNode
    C --> I[+6]:::leafNode
            '''
        },
        {
            "explanation": "Because MIN wants to minimize the score (to hurt you), MIN chooses the lowest available number: +3. Node B is now definitively worth +3.",
            "mermaid_code": '''
graph TD
    classDef maxNode fill:rgba(16, 185, 129, 0.1),stroke:#34D399,stroke-width:2px;
    classDef minNode fill:rgba(239, 68, 68, 0.1),stroke:#FCA5A5,stroke-width:2px;
    classDef leafNode fill:rgba(124, 77, 255, 0.1),stroke:#7C4DFF,stroke-width:2px;
    classDef focus fill:rgba(255, 255, 255, 0.2),stroke:#FFF,stroke-width:4px;

    A[MAX: ?]:::maxNode --> B[MIN: +3]:::focus
    A --> C[MIN: ?]:::minNode
    
    B --> D[+3]:::focus
    B --> E[+12]:::leafNode
    B --> F[+8]:::leafNode
    
    C --> G[+2]:::leafNode
    C --> H[+4]:::leafNode
    C --> I[+6]:::leafNode
            '''
        },
        {
            "explanation": "Next, the algorithm evaluates Node C. MIN looks at its options: +2, +4, and +6. MIN chooses the minimum: +2.",
            "mermaid_code": '''
graph TD
    classDef maxNode fill:rgba(16, 185, 129, 0.1),stroke:#34D399,stroke-width:2px;
    classDef minNode fill:rgba(239, 68, 68, 0.1),stroke:#FCA5A5,stroke-width:2px;
    classDef leafNode fill:rgba(124, 77, 255, 0.1),stroke:#7C4DFF,stroke-width:2px;
    classDef focus fill:rgba(255, 255, 255, 0.2),stroke:#FFF,stroke-width:4px;

    A[MAX: ?]:::maxNode --> B[MIN: +3]:::minNode
    A --> C[MIN: +2]:::focus
    
    B --> D[+3]:::leafNode
    B --> E[+12]:::leafNode
    B --> F[+8]:::leafNode
    
    C --> G[+2]:::focus
    C --> H[+4]:::leafNode
    C --> I[+6]:::leafNode
            '''
        },
        {
            "explanation": "Finally, the scores propagate back up to the root (Node A). It is MAX's turn. MAX looks at the guaranteed values of B (+3) and C (+2). MAX chooses the maximum: +3. You will move to Node B.",
            "mermaid_code": '''
graph TD
    classDef maxNode fill:rgba(16, 185, 129, 0.1),stroke:#34D399,stroke-width:2px;
    classDef minNode fill:rgba(239, 68, 68, 0.1),stroke:#FCA5A5,stroke-width:2px;
    classDef leafNode fill:rgba(124, 77, 255, 0.1),stroke:#7C4DFF,stroke-width:2px;
    classDef focus fill:rgba(255, 255, 255, 0.2),stroke:#FFF,stroke-width:4px;

    A[MAX: +3]:::focus --> B[MIN: +3]:::focus
    A --> C[MIN: +2]:::minNode
    
    B --> D[+3]:::leafNode
    B --> E[+12]:::leafNode
    B --> F[+8]:::leafNode
    
    C --> G[+2]:::leafNode
    C --> H[+4]:::leafNode
    C --> I[+6]:::leafNode
            '''
        }
    ]
}

# Replace the visual and the text explanation (idx and idx+1) with the stepper
blocks[idx] = stepper_block
del blocks[idx+1]

with open('level_content.py', 'w', encoding='utf-8') as f:
    f.write("LEVEL_CONTENT = \\\n")
    json.dump(LEVEL_CONTENT, f, indent=4, ensure_ascii=False)

