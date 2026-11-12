import json
from level_content import LEVEL_CONTENT

# EXPAND MODULE 1
mod1 = LEVEL_CONTENT['4']['episodes'][0]['blocks']
mod1.extend([
    {
        "type": "concept",
        "title": "Admissible vs Inadmissible Heuristics",
        "content": "Not all compasses are reliable. An **admissible heuristic** is one that never overestimates the true cost to the goal. It is optimistic. It might think the goal is closer than it really is, but it never thinks it's further away."
    },
    {
        "type": "concept",
        "title": "Why Optimism Matters",
        "content": "If your heuristic overestimates the distance, your AI might look at a valid path and think, 'Oh, that path is too long, I won't even bother checking it.' It will then settle for a suboptimal path. By keeping the heuristic optimistic, we force the AI to thoroughly check all promising paths before settling."
    },
    {
        "type": "interactive",
        "question": "If the true distance to the goal is 10, which of these is an ADMISSIBLE heuristic?",
        "options": [
            "h(n) = 12",
            "h(n) = 15",
            "h(n) = 8"
        ],
        "answer": "h(n) = 8"
    },
    {
        "type": "markdown",
        "content": "> [!TIP] \n> In a grid where you can only move Up, Down, Left, and Right (no diagonals), **Manhattan Distance** is perfectly admissible. If you can move diagonally, Manhattan Distance might overestimate, so you must use **Euclidean Distance** or **Chebyshev Distance** instead."
    },
    {
        "type": "visual",
        "title": "Manhattan vs Euclidean",
        "code": """
graph TD
    classDef m fill:#ef44441a,stroke:#FCA5A5,stroke-width:2px;
    classDef e fill:#3b82f61a,stroke:#93C5FD,stroke-width:2px;
    
    A["Point A (0,0)"] --> M["Manhattan Distance: |dx| + |dy|"]:::m
    A --> E["Euclidean Distance: sqrt(dx^2 + dy^2)"]:::e
    
    M --> M2["Cost: 3 + 4 = 7"]:::m
    E --> E2["Cost: sqrt(9 + 16) = 5"]:::e
        """
    },
    {
        "type": "interactive",
        "question": "If you are allowed to move diagonally in a grid, is Manhattan Distance admissible?",
        "options": [
            "Yes, it is always admissible",
            "No, it will overestimate the cost",
            "Only if there are walls"
        ],
        "answer": "No, it will overestimate the cost"
    }
])

# EXPAND MODULE 2
mod2 = LEVEL_CONTENT['4']['episodes'][1]['blocks']
mod2.extend([
    {
        "type": "concept",
        "title": "The Danger of Myopia",
        "content": "Greedy Best-First Search is 'myopic'—nearsighted. It only looks at the immediate heuristic value `h(n)`. This means it will happily run straight into a dead-end if the dead-end is geographically closer to the goal than the escape route."
    },
    {
        "type": "visual",
        "title": "The Dead-End Trap",
        "code": """
graph LR
    classDef node fill:#10b9811a,stroke:#34D399,stroke-width:2px;
    classDef trap fill:#ef44441a,stroke:#FCA5A5,stroke-width:2px;
    classDef goal fill:#7c4dff1a,stroke:#7C4DFF,stroke-width:2px;
    
    A["Start (h=10)"]:::node --> B["Node B (h=5)"]:::node
    A --> C["Node C (h=8)"]:::node
    
    B --> D["Dead End (h=3)"]:::trap
    D --> E["Wall (h=1)"]:::trap
    
    C --> F["Node F (h=4)"]:::node
    F --> G["Goal (h=0)"]:::goal
        """
    },
    {
        "type": "markdown",
        "content": "In the diagram above, Greedy Search will go from Start to Node B (because h=5 is better than h=8). From B, it will go to the Dead End (h=3). It gets stuck at the Wall. It completely misses the actual optimal path through Node C."
    },
    {
        "type": "concept",
        "title": "Completeness",
        "content": "An algorithm is **complete** if it is guaranteed to find a solution if one exists. \n\nGreedy Best-First Search is *not* complete in infinite state spaces or graphs with loops. It can get caught in an infinite loop, oscillating between two nodes that look close to the goal."
    },
    {
        "type": "interactive",
        "question": "To fix the infinite loop problem in Greedy Search, what must we do?",
        "options": [
            "Keep a 'visited' set to remember where we've been",
            "Increase the heuristic value",
            "Use a queue instead of a stack"
        ],
        "answer": "Keep a 'visited' set to remember where we've been"
    },
    {
        "type": "markdown",
        "content": "> [!NOTE] \n> Even with a 'visited' set (making it a Graph Search rather than a Tree Search), Greedy Search is still not optimal. It will find a path, but rarely the shortest one."
    },
    {
        "type": "code_experiment",
        "title": "Simulating Greedy Choice",
        "starter_code": "def greedy_choice(current_node, neighbors, h_costs):\n    # neighbors is a list of node names: ['B', 'C']\n    # h_costs is a dict: {'B': 5, 'C': 8, 'D': 3}\n    \n    # TODO: Return the neighbor with the lowest heuristic value\n    pass\n\nprint(greedy_choice('A', ['B', 'C'], {'B': 5, 'C': 8}))",
        "solution_code": "def greedy_choice(current_node, neighbors, h_costs):\n    best_node = None\n    best_h = float('inf')\n    for neighbor in neighbors:\n        if h_costs[neighbor] < best_h:\n            best_h = h_costs[neighbor]\n            best_node = neighbor\n    return best_node\n\nprint(greedy_choice('A', ['B', 'C'], {'B': 5, 'C': 8}))",
        "expected_output": "B",
        "explanation": "**Why it works:** The algorithm blindly iterates through the immediate neighbors and picks the one with the lowest `h_cost`. It completely ignores any `g_cost` (distance traveled).",
        "test_cases": []
    }
])

with open('level_content.py', 'w', encoding='utf-8') as f:
    f.write("LEVEL_CONTENT = \\\n")
    json.dump(LEVEL_CONTENT, f, indent=4, ensure_ascii=False)

print("Massively expanded Modules 1 and 2!")
