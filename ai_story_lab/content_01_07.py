CONTENT_01_07 = {
    "1": {
        "title": "Case 01: The Agent Awakens",
        "description": "Introduction to AI Agents, PEAS, and Environment Types",
        "episodes": [
            {
                "title": "Episode 1: The First Spark",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "# The First Spark\n\nYou are Dr. Alan Turing, but not the one from history. You are a Chief Architect at *Nexus Core*, a mega-corp building the next generation of autonomous systems. Today, you are booting up **Unit-7**, a prototype cleaning robot. But Unit-7 isn't just a machine; it's a *Rational Agent*.\n\nBefore Unit-7 can clean a room, it needs to understand what a room is, and what 'cleaning' means."
                    },
                    {
                        "type": "objective",
                        "content": "Define a Rational Agent using the PEAS framework."
                    },
                    {
                        "type": "concept",
                        "title": "The PEAS Framework",
                        "content": "To design a rational agent, we must specify its task environment. We use the **PEAS** description:\n\n*   **P**erformance Measure: How do we evaluate the agent's success? (e.g., dirt cleaned, time taken, battery used).\n*   **E**nvironment: Where does the agent operate? (e.g., a room with obstacles).\n*   **A**ctuators: How does the agent act upon the environment? (e.g., wheels, brushes, vacuum).\n*   **S**ensors: How does the agent perceive the environment? (e.g., cameras, dirt sensors, bump sensors)."
                    },
                    {
                        "type": "visual",
                        "content": "graph LR\n    A[Environment] -->|Percepts| S[Sensors]\n    S --> Agent\n    Agent -->|Actions| Ac[Actuators]\n    Ac --> A\n    P[Performance Measure] --> Agent"
                    },
                    {
                        "type": "code_lab",
                        "title": "Unit-7's First Logic",
                        "language": "python",
                        "starter_code": "def reflex_vacuum_agent(location, status):\n    # TODO: Implement a simple reflex agent\n    # If status is 'Dirty', return 'Suck'\n    # If location is 'A', return 'Right'\n    # If location is 'B', return 'Left'\n    pass\n",
                        "solution_code": "def reflex_vacuum_agent(location, status):\n    if status == 'Dirty':\n        return 'Suck'\n    elif location == 'A':\n        return 'Right'\n    elif location == 'B':\n        return 'Left'\n",
                        "expected_output": "Suck\nRight\nSuck\nLeft",
                        "explanation": "A Simple Reflex Agent selects actions based *only* on the current percept, ignoring the rest of the percept history. Here, if it sees dirt, it sucks. If it's in A and clean, it moves Right to check B.",
                        "test_cases": [
                            {"input": "reflex_vacuum_agent('A', 'Dirty')", "expected": "'Suck'"},
                            {"input": "reflex_vacuum_agent('A', 'Clean')", "expected": "'Right'"},
                            {"input": "reflex_vacuum_agent('B', 'Dirty')", "expected": "'Suck'"},
                            {"input": "reflex_vacuum_agent('B', 'Clean')", "expected": "'Left'"}
                        ]
                    }
                ]
            }
        ]
    },
    "2": {
        "title": "Case 02: The World Inside the Machine",
        "description": "Formulating Problems using State Spaces",
        "episodes": [
            {
                "title": "Episode 1: The Grid of Possibilities",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "# The Grid of Possibilities\n\nUnit-7 is functioning, but it's reacting blindly. To plan ahead, it needs an internal representation of the world. It needs a **State Space**."
                    },
                    {
                        "type": "concept",
                        "title": "Problem Formulation",
                        "content": "A search problem consists of:\n1.  **Initial State**: Where the agent starts.\n2.  **Actions(s)**: What the agent can do in state 's'.\n3.  **Transition Model Result(s, a)**: The state that results from doing action 'a' in state 's'.\n4.  **Goal Test**: Checks if a state is the goal.\n5.  **Path Cost**: Sum of step costs."
                    },
                    {
                        "type": "visual",
                        "content": "graph LR\n    S0((Start)) -->|Action 1| S1((State 1))\n    S0 -->|Action 2| S2((State 2))\n    S1 -->|Action 3| S3(((Goal)))"
                    },
                    {
                        "type": "code_lab",
                        "title": "Defining the Grid World",
                        "language": "python",
                        "starter_code": "class GridProblem:\n    def __init__(self, start, goal):\n        self.start = start\n        self.goal = goal\n\n    def get_actions(self, state):\n        # Return list of possible actions: 'Up', 'Down', 'Left', 'Right'\n        # For simplicity, assume a 3x3 grid (0,0 to 2,2) and no obstacles yet.\n        x, y = state\n        actions = []\n        # TODO: Add boundary checks and return valid actions\n        return actions\n\n    def result(self, state, action):\n        # TODO: Return the new state (x, y) based on the action\n        pass",
                        "solution_code": "class GridProblem:\n    def __init__(self, start, goal):\n        self.start = start\n        self.goal = goal\n\n    def get_actions(self, state):\n        x, y = state\n        actions = []\n        if y > 0: actions.append('Up')\n        if y < 2: actions.append('Down')\n        if x > 0: actions.append('Left')\n        if x < 2: actions.append('Right')\n        return actions\n\n    def result(self, state, action):\n        x, y = state\n        if action == 'Up': return (x, y - 1)\n        if action == 'Down': return (x, y + 1)\n        if action == 'Left': return (x - 1, y)\n        if action == 'Right': return (x + 1, y)\n        return state",
                        "expected_output": "['Down', 'Right']\n(0, 1)",
                        "explanation": "We formulate the grid as a set of (x, y) coordinates. The transition model dictates how coordinates change based on directional actions.",
                        "test_cases": [
                            {"input": "problem = GridProblem((0,0), (2,2)); problem.get_actions((0,0))", "expected": "['Down', 'Right']"},
                            {"input": "problem = GridProblem((0,0), (2,2)); problem.result((0,0), 'Down')", "expected": "(0, 1)"}
                        ]
                    }
                ]
            }
        ]
    },
    "3": {
        "title": "Case 03: The Maze Without a Map",
        "description": "Uninformed Search Strategies: BFS, DFS, UCS",
        "episodes": [
            {
                "title": "Episode 1: The Blind Explorer",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "# The Blind Explorer\n\nUnit-7 is dropped into an unmapped sector. It knows how to move (its state space), but it doesn't know where the target is. It must explore systematically."
                    },
                    {
                        "type": "concept",
                        "title": "Breadth-First Search (BFS)",
                        "content": "BFS explores the state space level by level. It expands the shallowest unexpanded node first. It guarantees finding the shortest path (least number of steps) in unweighted graphs."
                    },
                    {
                        "type": "visual",
                        "content": "graph TD\n    A --> B\n    A --> C\n    B --> D\n    B --> E\n    C --> F\n    C --> G\n    style A fill:#f9f,stroke:#333,stroke-width:2px"
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementing BFS",
                        "language": "python",
                        "starter_code": "from collections import deque\n\ndef bfs(graph, start, goal):\n    # graph is a dictionary mapping nodes to lists of neighbors\n    # e.g., {'A': ['B', 'C'], 'B': ['D', 'E'], ...}    queue = deque([start])\n    visited = set([start])\n    # TODO: Implement BFS to return True if goal is found, False otherwise\n    pass",
                        "solution_code": "from collections import deque\n\ndef bfs(graph, start, goal):\n    queue = deque([start])\n    visited = set([start])\n    \n    while queue:\n        node = queue.popleft()\n        if node == goal:\n            return True\n            \n        for neighbor in graph.get(node, []):\n            if neighbor not in visited:\n                visited.add(neighbor)\n                queue.append(neighbor)\n                \n    return False",
                        "expected_output": "True\nFalse",
                        "explanation": "BFS uses a FIFO queue. We must keep track of `visited` nodes to avoid infinite loops in cyclic graphs.",
                        "test_cases": [
                            {"input": "bfs({'A': ['B', 'C'], 'B': ['D'], 'C': []}, 'A', 'D')", "expected": "True"},
                            {"input": "bfs({'A': ['B', 'C'], 'B': ['D'], 'C': []}, 'A', 'Z')", "expected": "False"}
                        ]
                    }
                ]
            }
        ]
    },
    "4": {
        "title": "Case 04: The Search for the Better Path",
        "description": "Informed Search Strategies: Heuristics, Greedy, A*",
        "episodes": [
            {
                "title": "Episode 1: The Intuition Chip",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "# The Intuition Chip\n\nBlind search is too slow. We installed a 'heuristic' module in Unit-7—a way to guess how far it is from the goal. This lets it prioritize promising paths."
                    },
                    {
                        "type": "concept",
                        "title": "A* Search",
                        "content": "A* evaluates nodes by combining g(n), the cost to reach the node, and h(n), the estimated cost to get from the node to the goal:\n\n**f(n) = g(n) + h(n)**\n\nIf h(n) is admissible (never overestimates), A* is optimal."
                    },
                    {
                        "type": "code_lab",
                        "title": "Calculating Manhattan Distance",
                        "language": "python",
                        "starter_code": "def manhattan_distance(p1, p2):\n    # p1 and p2 are tuples (x, y)\n    # TODO: Calculate and return the Manhattan distance between p1 and p2\n    pass",
                        "solution_code": "def manhattan_distance(p1, p2):\n    x1, y1 = p1\n    x2, y2 = p2\n    return abs(x1 - x2) + abs(y1 - y2)",
                        "expected_output": "4\n0",
                        "explanation": "The Manhattan distance is a common admissible heuristic for grid problems where diagonal movement is not allowed.",
                        "test_cases": [
                            {"input": "manhattan_distance((0,0), (2,2))", "expected": "4"},
                            {"input": "manhattan_distance((5,5), (5,5))", "expected": "0"}
                        ]
                    }
                ]
            }
        ]
    },
    "5": {
        "title": "Case 05: The Heuristic Detective",
        "description": "Deep A*, Admissibility, Consistency, AO*",
        "episodes": [
            {
                "title": "Episode 1: The Flawed Oracle",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "# The Flawed Oracle\n\nUnit-7 is taking weird, suboptimal paths. The heuristic module might be broken. Is it overestimating the distance? We need to verify admissibility and consistency."
                    },
                    {
                        "type": "concept",
                        "title": "Admissibility vs. Consistency",
                        "content": "*   **Admissible**: h(n) <= true_cost(n, goal). It never overestimates.\n*   **Consistent**: h(n) <= cost(n, a, n') + h(n'). The triangle inequality holds."
                    },
                    {
                        "type": "code_lab",
                        "title": "Testing Admissibility",
                        "language": "python",
                        "starter_code": "def is_admissible(heuristic_values, true_costs):\n    # heuristic_values: dict of node -> h(n)\n    # true_costs: dict of node -> actual cost to goal\n    # TODO: Return True if the heuristic is admissible for all nodes, False otherwise\n    pass",
                        "solution_code": "def is_admissible(heuristic_values, true_costs):\n    for node, h_val in heuristic_values.items():\n        if node in true_costs and h_val > true_costs[node]:\n            return False\n    return True",
                        "expected_output": "True\nFalse",
                        "explanation": "An admissible heuristic guarantees A* will find the optimal path in a tree search.",
                        "test_cases": [
                            {"input": "is_admissible({'A': 2, 'B': 1}, {'A': 3, 'B': 2})", "expected": "True"},
                            {"input": "is_admissible({'A': 4, 'B': 1}, {'A': 3, 'B': 2})", "expected": "False"}
                        ]
                    }
                ]
            }
        ]
    },
    "6": {
        "title": "Case 06: The Game of Minds",
        "description": "Adversarial Search: Minimax and Alpha-Beta Pruning",
        "episodes": [
            {
                "title": "Episode 1: The Rival",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "# The Rival\n\nNexus Core has deployed a competitor: Unit-8. They are competing for resources in the same environment. Unit-7 must now plan not just against the environment, but against a hostile agent."
                    },
                    {
                        "type": "concept",
                        "title": "Minimax Algorithm",
                        "content": "In zero-sum games, MAX tries to maximize the score, while MIN tries to minimize it. Minimax computes the optimal move by recursively evaluating all possible futures."
                    },
                    {
                        "type": "code_lab",
                        "title": "Minimax Evaluation",
                        "language": "python",
                        "starter_code": "def minimax(node_value, is_max_turn, children_values):\n    # If the node is a leaf, children_values is empty.\n    # TODO: Implement a single step of minimax.\n    # Return the value for the current node based on its children.\n    pass",
                        "solution_code": "def minimax(node_value, is_max_turn, children_values):\n    if not children_values:\n        return node_value\n    if is_max_turn:\n        return max(children_values)\n    else:\n        return min(children_values)",
                        "expected_output": "5\n2",
                        "explanation": "MAX chooses the maximum of its children's values. MIN chooses the minimum.",
                        "test_cases": [
                            {"input": "minimax(None, True, [3, 5, 2])", "expected": "5"},
                            {"input": "minimax(None, False, [3, 5, 2])", "expected": "2"}
                        ]
                    }
                ]
            }
        ]
    },
    "7": {
        "title": "Case 07: The Impossible Puzzle",
        "description": "Constraint Satisfaction Problems (CSP), Backtracking, Arc Consistency",
        "episodes": [
            {
                "title": "Episode 1: The Timetable Dilemma",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "# The Timetable Dilemma\n\nUnit-7 is now managing the entire facility's charging schedules. Multiple robots need chargers, but not all robots can use the same charger, and chargers have limited slots. This isn't pathfinding; this is a Constraint Satisfaction Problem (CSP)."
                    },
                    {
                        "type": "concept",
                        "title": "CSPs and Backtracking",
                        "content": "A CSP consists of Variables, Domains, and Constraints. Backtracking search is a depth-first search that chooses values for one variable at a time and backtracks when a variable has no legal values left."
                    },
                    {
                        "type": "visual",
                        "content": "graph LR\n    R1((Robot 1)) ---|!=| R2((Robot 2))\n    R2 ---|!=| R3((Robot 3))"
                    },
                    {
                        "type": "code_lab",
                        "title": "Checking Constraints",
                        "language": "python",
                        "starter_code": "def is_consistent(variable, value, assignment, constraints):\n    # constraints is a list of tuples (var1, var2) meaning they cannot have the same value\n    # assignment is a dict mapping variables to their assigned values\n    # TODO: Check if assigning 'value' to 'variable' violates any constraints\n    pass",
                        "solution_code": "def is_consistent(variable, value, assignment, constraints):\n    for var1, var2 in constraints:\n        if variable == var1 and var2 in assignment and assignment[var2] == value:\n            return False\n        if variable == var2 and var1 in assignment and assignment[var1] == value:\n            return False\n    return True",
                        "expected_output": "True\nFalse",
                        "explanation": "Before assigning a value in a CSP, we check if it conflicts with existing assignments according to our constraint graph.",
                        "test_cases": [
                            {"input": "is_consistent('A', 1, {'B': 2}, [('A', 'B')])", "expected": "True"},
                            {"input": "is_consistent('A', 2, {'B': 2}, [('A', 'B')])", "expected": "False"}
                        ]
                    }
                ]
            }
        ]
    }
}
