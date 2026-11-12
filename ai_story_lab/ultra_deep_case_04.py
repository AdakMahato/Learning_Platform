import json
from level_content import LEVEL_CONTENT

mod1 = [
    {
        "type": "markdown",
        "content": "You are trapped in the center of a labyrinth. Until now, you have used algorithms like BFS and DFS. They are blind. They explore in all directions equally. \n\nBut this time, you have a compass. It points towards the goal. It tells you roughly how far away it is. You are no longer blind."
    },
    {
        "type": "objective",
        "title": "Module Objective",
        "content": "Understand Informed Search. Learn what a Heuristic is, and how to estimate distances in complex state spaces."
    },
    {
        "type": "problem",
        "content": "**The Think-First Challenge:** If a compass tells you the goal is straight North, should you *always* move North? What happens if there is a massive wall blocking the North path?"
    },
    {
        "type": "concept",
        "title": "The Heuristic Function: h(n)",
        "content": "A **heuristic**, denoted as `h(n)`, is an *estimate* of the cost to get from the current node `n` to the goal.\n\nIn a maze, the most common heuristic is **Manhattan Distance** (the sum of the horizontal and vertical distances) or **Euclidean Distance** (the straight-line distance)."
    },
    {
        "type": "code_experiment",
        "title": "Implementing the Heuristic",
        "starter_code": "import math\n\ndef euclidean_distance(node, goal):\n    # node and goal are tuples: (x, y)\n    # TODO: Calculate the straight-line distance between the two points\n    pass\n\nprint(euclidean_distance((0,0), (3,4)))",
        "solution_code": "import math\n\ndef euclidean_distance(node, goal):\n    x1, y1 = node\n    x2, y2 = goal\n    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)\n\nprint(euclidean_distance((0,0), (3,4)))",
        "expected_output": "5.0",
        "explanation": "**Why it works:** The Euclidean distance is a classic heuristic for 2D grids. It uses the Pythagorean theorem to calculate the exact distance 'as the crow flies'.",
        "test_cases": []
    }
]

mod2 = [
    {
        "type": "concept",
        "title": "Greedy Best-First Search",
        "content": "Greedy Best-First Search is incredibly simple: **Always expand the node that appears closest to the goal.**\n\nIt completely ignores how far you have already traveled. It only looks at `h(n)`. If Sibiu has an `h` of 253, and Zerind has an `h` of 374, it expands Sibiu. Period."
    },
    {
        "type": "visual",
        "title": "Straight-Line Distance Heuristic",
        "code": """
graph LR
    classDef node fill:#10b9811a,stroke:#34D399,stroke-width:2px;
    classDef goal fill:#7c4dff1a,stroke:#7C4DFF,stroke-width:2px;
    
    A["Arad (h=366)"]:::node --> S["Sibiu (h=253)"]:::node
    A --> Z["Zerind (h=374)"]:::node
    A --> T["Timisoara (h=329)"]:::node
    
    S --> F["Fagaras (h=176)"]:::node
    S --> R["Rimnicu Vilcea (h=193)"]:::node
    
    F --> B["Bucharest (h=0)"]:::goal
        """
    },
    {
        "type": "markdown",
        "content": "> [!WARNING] \n> **The Greedy Trap:** Because Greedy Search ignores the cost of the path taken so far, it can easily get stuck in dead ends or find a path that is technically valid, but horribly long and inefficient."
    }
]

mod3 = [
    {
        "type": "markdown",
        "content": "Greedy Search is fast, but it is not optimal. Uniform Cost Search (Dijkstra) is optimal, but it is slow because it is blind. What if we combine them?"
    },
    {
        "type": "concept",
        "title": "The A* Algorithm",
        "content": "A* (A-Star) is the holy grail of pathfinding. It combines the guaranteed optimality of Uniform Cost Search with the directed speed of Greedy Search.\n\nIt evaluates nodes by combining two values:\n*   **g(n):** The exact cost to reach node `n` from the start.\n*   **h(n):** The estimated cost to reach the goal from node `n`.\n\n**f(n) = g(n) + h(n)**\n\nA* always expands the node with the lowest `f(n)`."
    },
    {
        "type": "visual_stepper",
        "title": "Interactive: A* Search Step-by-Step",
        "height": 450,
        "steps": [
            {
                "explanation": "We start at Node A. The cost to get here is 0. The heuristic says the goal is 10 away. f(A) = 0 + 10 = 10.",
                "mermaid_code": '''
    graph TD
        classDef idle fill:#ffffff1a,stroke:#333,stroke-width:2px;
        classDef focus fill:#7c4dff1a,stroke:#7C4DFF,stroke-width:3px;
        
        A["A<br>g=0, h=10<br>f=10"]:::focus --> B["B<br>g=?, h=6<br>f=?"]:::idle
        A --> C["C<br>g=?, h=8<br>f=?"]:::idle
                '''
            },
            {
                "explanation": "We expand Node A. Path A->B costs 3. Path A->C costs 2. We calculate their f-values. f(B) = 3 + 6 = 9. f(C) = 2 + 8 = 10.",
                "mermaid_code": '''
    graph TD
        classDef idle fill:#ffffff1a,stroke:#333,stroke-width:2px;
        classDef focus fill:#7c4dff1a,stroke:#7C4DFF,stroke-width:3px;
        classDef active fill:#10b9811a,stroke:#34D399,stroke-width:2px;
        
        A["A<br>g=0, h=10<br>f=10"]:::idle -->|cost 3| B["B<br>g=3, h=6<br>f=9"]:::active
        A -->|cost 2| C["C<br>g=2, h=8<br>f=10"]:::active
                '''
            },
            {
                "explanation": "Which node does A* explore next? It picks the lowest f-value! Node B has an f-value of 9, while Node C has 10. We expand Node B.",
                "mermaid_code": '''
    graph TD
        classDef idle fill:#ffffff1a,stroke:#333,stroke-width:2px;
        classDef focus fill:#7c4dff1a,stroke:#7C4DFF,stroke-width:3px;
        classDef active fill:#10b9811a,stroke:#34D399,stroke-width:2px;
        
        A["A"]:::idle --> B["B<br>g=3, h=6<br>f=9"]:::focus
        A --> C["C<br>g=2, h=8<br>f=10"]:::active
        B -->|cost 5| D["Goal<br>g=?, h=0<br>f=?"]:::idle
                '''
            },
            {
                "explanation": "From Node B, we reach the Goal. The total path cost is g(B)+5 = 8. The heuristic at the goal is always 0. f(Goal) = 8 + 0 = 8. Since 8 < 10 (Node C), we found the optimal path!",
                "mermaid_code": '''
    graph TD
        classDef idle fill:#ffffff1a,stroke:#333,stroke-width:2px;
        classDef focus fill:#7c4dff1a,stroke:#7C4DFF,stroke-width:3px;
        classDef active fill:#10b9811a,stroke:#34D399,stroke-width:2px;
        classDef goal fill:#eab3081a,stroke:#FACC15,stroke-width:3px;
        
        A["A"]:::idle --> B["B"]:::idle
        A --> C["C<br>f=10"]:::active
        B --> D["Goal<br>g=8, h=0<br>f=8"]:::goal
                '''
            }
        ]
    }
]

mod4 = [
    {
        "type": "markdown",
        "content": "Theory is great, but code is absolute. Let's write the A* search loop."
    },
    {
        "type": "code_lab",
        "title": "Implementing A* Priority Queue",
        "starter_code": "import heapq\n\ndef a_star_search(start, goal, graph, h_costs):\n    # graph is a dict: {'A': [('B', 3), ('C', 2)], ...}\n    # h_costs is a dict: {'A': 10, 'B': 6, ...}\n    \n    frontier = []\n    # heapq.heappush(frontier, (f_score, current_node))\n    heapq.heappush(frontier, (h_costs[start], start))\n    \n    cost_so_far = {start: 0}\n    came_from = {start: None}\n    \n    while frontier:\n        # TODO: Pop the lowest f_score node\n        # TODO: If it's the goal, break\n        # TODO: Loop through neighbors, calculate new g_score and f_score\n        pass\n        \n    return came_from",
        "solution_code": "import heapq\n\ndef a_star_search(start, goal, graph, h_costs):\n    frontier = []\n    heapq.heappush(frontier, (h_costs[start], start))\n    cost_so_far = {start: 0}\n    came_from = {start: None}\n    \n    while frontier:\n        current_f, current = heapq.heappop(frontier)\n        \n        if current == goal:\n            break\n            \n        for next_node, cost in graph[current]:\n            new_cost = cost_so_far[current] + cost\n            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:\n                cost_so_far[next_node] = new_cost\n                priority = new_cost + h_costs[next_node]\n                heapq.heappush(frontier, (priority, next_node))\n                came_from[next_node] = current\n                \n    return came_from",
        "expected_output": "",
        "explanation": "**Why it works:** We use a Priority Queue (`heapq`) to always sort the frontier by the `f_score` (the `priority` variable). This guarantees that we always expand the most promising paths first.",
        "test_cases": []
    }
]

mod5 = [
    {
        "type": "markdown",
        "content": "A* is only guaranteed to find the absolute shortest path if the heuristic function obeys certain mathematical laws. If your heuristic is 'bad', A* becomes greedy and makes mistakes."
    },
    {
        "type": "concept",
        "title": "Admissibility",
        "content": "A heuristic is **admissible** if it NEVER overestimates the true cost to reach the goal. \n\nFor example, straight-line distance is always admissible because it is physically impossible to find a shorter path than a straight line between two points."
    },
    {
        "type": "concept",
        "title": "Consistency (Monotonicity)",
        "content": "A heuristic is **consistent** if, for every node N and every successor P, the estimated cost from N to the goal is no greater than the step cost to get to P plus the estimated cost from P to the goal.\n\n`h(N) <= c(N, P) + h(P)`"
    },
    {
        "type": "interactive",
        "question": "What happens if a heuristic OVERESTIMATES the true cost?",
        "options": [
            "A* expands more nodes",
            "A* becomes suboptimal",
            "A* becomes BFS"
        ],
        "answer": "A* becomes suboptimal"
    }
]

mod6 = [
    {
        "type": "markdown",
        "content": "A* keeps all generated nodes in memory. In complex games, A* will quickly consume all your RAM and crash the server."
    },
    {
        "type": "concept",
        "title": "IDA* (Iterative Deepening A*)",
        "content": "IDA* solves the memory problem. Instead of storing the entire frontier, it uses a depth-first search that cuts off any path whose `f`-cost exceeds a certain threshold. If no solution is found, the threshold is increased to the minimum `f`-cost that was previously rejected."
    },
    {
        "type": "concept",
        "title": "SMA* (Simplified Memory-Bounded A*)",
        "content": "SMA* uses all available memory. When memory is full, it drops the worst leaf node (the one with the highest `f`-value) from the tree to make room for a new one, but 'backs up' the value of the forgotten node to its parent so it can regenerate it later if needed."
    }
]


LEVEL_CONTENT['4'] = {
    "title": "Case 04: The Search for the Better Path",
    "episodes": [
        {
            "title": "Module 1: The Heuristic Compass",
            "blocks": mod1
        },
        {
            "title": "Module 2: The Greedy Trap",
            "blocks": mod2
        },
        {
            "title": "Module 3: The A* Algorithm",
            "blocks": mod3
        },
        {
            "title": "Module 4: Engineering the Queue",
            "blocks": mod4
        },
        {
            "title": "Module 5: Admissibility vs Consistency",
            "blocks": mod5
        },
        {
            "title": "Module 6: Escaping Memory Limits",
            "blocks": mod6
        }
    ]
}

with open('level_content.py', 'w', encoding='utf-8') as f:
    f.write("LEVEL_CONTENT = \\\n")
    json.dump(LEVEL_CONTENT, f, indent=4, ensure_ascii=False)

print("Injected ultra extreme depth into Case 04!")
