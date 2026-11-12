import json
from level_content import LEVEL_CONTENT

# Re-build Case 01 Stepper (The Agent Loop)
LEVEL_CONTENT['1']['episodes'][0]['blocks'][7] = {
    "type": "visual_stepper",
    "title": "Interactive: The Rational Agent Loop",
    "steps": [
        {
            "explanation": "Step 1: The Environment exists in a current state. It emits data.",
            "mermaid_code": "graph TD\n  classDef active fill:#10b9811a,stroke:#34D399,stroke-width:2px;\n  classDef idle fill:#ffffff1a,stroke:#333,stroke-width:2px;\n  E[\"Environment\"]:::active -->|Data| S[\"Sensors\"]:::idle\n  S --> A[\"Agent Program\"]:::idle\n  A --> AC[\"Actuators\"]:::idle\n  AC -->|Action| E"
        },
        {
            "explanation": "Step 2: The Agent's Sensors perceive the data (Percepts) from the Environment.",
            "mermaid_code": "graph TD\n  classDef active fill:#10b9811a,stroke:#34D399,stroke-width:2px;\n  classDef idle fill:#ffffff1a,stroke:#333,stroke-width:2px;\n  E[\"Environment\"]:::idle -->|Percepts| S[\"Sensors\"]:::active\n  S --> A[\"Agent Program\"]:::idle\n  A --> AC[\"Actuators\"]:::idle\n  AC -->|Action| E"
        },
        {
            "explanation": "Step 3: The Agent Program processes the Percepts and decides on the optimal Action.",
            "mermaid_code": "graph TD\n  classDef active fill:#10b9811a,stroke:#34D399,stroke-width:2px;\n  classDef idle fill:#ffffff1a,stroke:#333,stroke-width:2px;\n  E[\"Environment\"]:::idle --> S[\"Sensors\"]:::idle\n  S --> A[\"Agent Program\"]:::active\n  A --> AC[\"Actuators\"]:::idle\n  AC -->|Action| E"
        },
        {
            "explanation": "Step 4: The Actuators execute the decided Action, physically altering the Environment.",
            "mermaid_code": "graph TD\n  classDef active fill:#10b9811a,stroke:#34D399,stroke-width:2px;\n  classDef idle fill:#ffffff1a,stroke:#333,stroke-width:2px;\n  E[\"Environment\"]:::idle --> S[\"Sensors\"]:::idle\n  S --> A[\"Agent Program\"]:::idle\n  A --> AC[\"Actuators\"]:::active\n  AC -->|Action| E:::active"
        }
    ]
}

# Re-build Case 03 Stepper (BFS vs DFS)
# Let's find where Case 03 has its static diagram and upgrade it to a stepper.
# We will just inject it into Module 1 of Case 03.
LEVEL_CONTENT['3']['episodes'][0]['blocks'].insert(3, {
    "type": "visual_stepper",
    "title": "Interactive: Breadth-First Search (BFS)",
    "steps": [
        {
            "explanation": "Step 1: BFS starts at the root node. It checks if the root is the goal.",
            "mermaid_code": "graph TD\n  classDef active fill:#3b82f61a,stroke:#93C5FD,stroke-width:2px;\n  classDef idle fill:#ffffff1a,stroke:#333,stroke-width:2px;\n  A[\"Root\"]:::active --> B[\"Level 1\"]:::idle\n  A --> C[\"Level 1\"]:::idle\n  B --> D[\"Level 2\"]:::idle\n  B --> E[\"Level 2\"]:::idle"
        },
        {
            "explanation": "Step 2: It explores ALL nodes at Depth 1 before moving deeper.",
            "mermaid_code": "graph TD\n  classDef visited fill:#10b9811a,stroke:#34D399,stroke-width:2px;\n  classDef active fill:#3b82f61a,stroke:#93C5FD,stroke-width:2px;\n  classDef idle fill:#ffffff1a,stroke:#333,stroke-width:2px;\n  A[\"Root\"]:::visited --> B[\"Level 1\"]:::active\n  A --> C[\"Level 1\"]:::active\n  B --> D[\"Level 2\"]:::idle\n  B --> E[\"Level 2\"]:::idle"
        },
        {
            "explanation": "Step 3: Once Depth 1 is fully explored, it drops down to Depth 2. This guarantees finding the shortest path.",
            "mermaid_code": "graph TD\n  classDef visited fill:#10b9811a,stroke:#34D399,stroke-width:2px;\n  classDef active fill:#3b82f61a,stroke:#93C5FD,stroke-width:2px;\n  classDef idle fill:#ffffff1a,stroke:#333,stroke-width:2px;\n  A[\"Root\"]:::visited --> B[\"Level 1\"]:::visited\n  A --> C[\"Level 1\"]:::visited\n  B --> D[\"Level 2\"]:::active\n  B --> E[\"Level 2\"]:::active"
        }
    ]
})

with open('level_content.py', 'w', encoding='utf-8') as f:
    f.write("LEVEL_CONTENT = \\\n")
    json.dump(LEVEL_CONTENT, f, indent=4, ensure_ascii=False)

print("Restored real animated steppers!")
