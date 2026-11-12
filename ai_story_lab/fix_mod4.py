import json
from level_content import LEVEL_CONTENT

mod4 = [
    {
        "type": "markdown",
        "content": "Theory is great, but an AI is useless if it cannot be executed in code. Before we implement the A* algorithm, we must understand the core data structure that makes it fast: **The Priority Queue**."
    },
    {
        "type": "concept",
        "title": "Why not a regular List?",
        "content": "In Breadth-First Search (BFS), we use a standard Queue (First-In, First-Out). In A*, we must always expand the node with the lowest `f(n)` value.\n\nIf we use a regular Python list for our frontier, we would have to search the entire list every single time to find the lowest `f` value. This takes `O(N)` time. For a large graph, this is disastrously slow."
    },
    {
        "type": "concept",
        "title": "The Min-Heap (Priority Queue)",
        "content": "A Min-Heap is a specialized binary tree where the parent is always smaller than its children. In Python, the `heapq` library implements this over a standard list.\n\nFinding the lowest `f(n)` in a min-heap takes `O(1)` time (it's always at the top). Pushing a new node into the heap takes `O(log N)` time. This makes A* blazing fast."
    },
    {
        "type": "visual",
        "title": "Visualizing the Min-Heap",
        "code": """
graph TD
    classDef top fill:#10b9811a,stroke:#34D399,stroke-width:2px;
    classDef node fill:#7c4dff1a,stroke:#7C4DFF,stroke-width:2px;
    
    A["f=9 (Node B)"]:::top --> B["f=12 (Node G)"]:::node
    A --> C["f=10 (Node C)"]:::node
    
    B --> D["f=15 (Node X)"]:::node
    B --> E["f=13 (Node Y)"]:::node
    
    C --> F["f=20 (Node Z)"]:::node
        """
    },
    {
        "type": "markdown",
        "content": "> [!NOTE] \n> Notice how the lowest value (9) is perfectly at the top. The rest of the tree is not perfectly sorted, but it guarantees that parents are smaller than children."
    },
    {
        "type": "concept",
        "title": "Tracking the Costs",
        "content": "To implement A*, we need two dictionaries:\n1. `cost_so_far`: Tracks the exact `g(n)` cost from the start to any node we have visited. If we find a *cheaper* path to a node we've already visited, we update this dictionary!\n2. `came_from`: Tracks which node we used to reach the current node. This allows us to re-construct the path backwards from the goal to the start once we find the solution."
    },
    {
        "type": "code_lab",
        "title": "Implementing A* Priority Queue",
        "starter_code": "import heapq\n\ndef a_star_search(start, goal, graph, h_costs):\n    # graph is a dict: {'A': [('B', 3), ('C', 2)], ...}\n    # h_costs is a dict: {'A': 10, 'B': 6, ...}\n    \n    frontier = []\n    # heapq.heappush(frontier, (priority, current_node))\n    heapq.heappush(frontier, (h_costs[start], start))\n    \n    cost_so_far = {start: 0}\n    came_from = {start: None}\n    \n    while frontier:\n        # TODO: 1. Pop the lowest f_score node using heapq.heappop()\n        # TODO: 2. If current == goal, break out of the loop!\n        # TODO: 3. Loop through neighbors in graph[current]\n        # TODO: 4. Calculate new_cost = cost_so_far[current] + step_cost\n        # TODO: 5. If neighbor is unvisited OR new_cost < cost_so_far[neighbor]:\n        #          Update cost_so_far, push to frontier, update came_from\n        pass\n        \n    return came_from",
        "solution_code": "import heapq\n\ndef a_star_search(start, goal, graph, h_costs):\n    frontier = []\n    heapq.heappush(frontier, (h_costs[start], start))\n    cost_so_far = {start: 0}\n    came_from = {start: None}\n    \n    while frontier:\n        current_f, current = heapq.heappop(frontier)\n        \n        if current == goal:\n            break\n            \n        for next_node, cost in graph[current]:\n            new_cost = cost_so_far[current] + cost\n            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:\n                cost_so_far[next_node] = new_cost\n                priority = new_cost + h_costs[next_node]\n                heapq.heappush(frontier, (priority, next_node))\n                came_from[next_node] = current\n                \n    return came_from",
        "expected_output": "",
        "explanation": "**Why it works:** By using `heapq`, we guarantee that every time we call `heappop()`, we are expanding the node that is mathematically most likely to lead us to the shortest path.",
        "test_cases": []
    }
]

LEVEL_CONTENT['4']['episodes'][3]['blocks'] = mod4

with open('level_content.py', 'w', encoding='utf-8') as f:
    f.write("LEVEL_CONTENT = \\\n")
    json.dump(LEVEL_CONTENT, f, indent=4, ensure_ascii=False)

print("Injected heavy explanation into Module 4!")
