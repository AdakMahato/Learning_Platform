CONTENT_01_05 = {
    "case_01": {
        "title": "Case 01: The Agent Awakens (PEAS, Environments)",
        "modules": [
            {
                "title": "Module 1.1: What is an Agent?",
                "blocks": [
                    {"type": "narrative", "content": "You are a spark of logic in an empty room. The void surrounds you."},
                    {"type": "concept", "title": "Agents", "content": "An agent is anything that can be viewed as perceiving its environment through sensors and acting upon that environment through actuators."},
                    {"type": "narrative", "content": "Your first task: define your purpose. What is PEAS?"},
                    {"type": "concept", "title": "PEAS Framework", "content": "PEAS stands for Performance measure, Environment, Actuators, Sensors. It helps in defining the task environment of an AI agent."},
                    {"type": "interactive", "question": "What does the 'P' in PEAS stand for?", "options": ["Performance", "Perception", "Planning"], "answer": "Performance"},
                    {"type": "narrative", "content": "Consider a self-driving car. What are its actuators?"},
                    {"type": "concept", "title": "Actuators in Practice", "content": "Steering wheel, accelerator, brake, signal lights, horn."},
                    {"type": "interactive", "question": "Which of these is a sensor for a self-driving car?", "options": ["Brakes", "Camera", "Engine"], "answer": "Camera"}
                ]
            },
            {
                "title": "Module 1.2: The Environment",
                "blocks": [
                    {"type": "narrative", "content": "The world around you is complex. You must analyze its properties."},
                    {"type": "concept", "title": "Properties of Environments", "content": "Environments can be Fully vs Partially Observable, Single vs Multi-agent, Deterministic vs Stochastic, Episodic vs Sequential, Static vs Dynamic, Discrete vs Continuous."},
                    {"type": "interactive", "question": "If an agent's sensors give it access to the complete state of the environment at each point in time, the environment is:", "options": ["Fully Observable", "Partially Observable", "Deterministic"], "answer": "Fully Observable"},
                    {"type": "narrative", "content": "Think about poker. Is it fully observable?"},
                    {"type": "concept", "title": "Partially Observable", "content": "In poker, you cannot see your opponents' cards. Thus, it is partially observable."},
                    {"type": "interactive", "question": "Is chess fully or partially observable?", "options": ["Fully Observable", "Partially Observable"], "answer": "Fully Observable"},
                    {"type": "narrative", "content": "You now understand your surroundings. The awakening is complete."}
                ]
            }
        ]
    },
    "case_02": {
        "title": "Case 02: The World Inside the Machine (State Spaces)",
        "modules": [
            {
                "title": "Module 2.1: State Spaces",
                "blocks": [
                    {"type": "narrative", "content": "You need to model the world. A map of all possibilities."},
                    {"type": "concept", "title": "State Space", "content": "A state space represents all possible states the environment can be in. It is often modeled as a graph where nodes are states and edges are actions."},
                    {"type": "concept", "title": "Initial State & Goal State", "content": "The initial state is where the agent begins. The goal state (or states) is what the agent wants to achieve."},
                    {"type": "interactive", "question": "In a state space graph, what do edges typically represent?", "options": ["Actions/Transitions", "States", "Goals"], "answer": "Actions/Transitions"},
                    {"type": "narrative", "content": "Consider a vacuum cleaner in a 2-room grid. How many states are there?"},
                    {"type": "concept", "title": "State Calculation", "content": "2 rooms, each can be clean or dirty (2x2 = 4 combinations). The vacuum can be in either room (2). Total states = 4 x 2 = 8."},
                    {"type": "interactive", "question": "How many total states in the 2-room vacuum world?", "options": ["4", "8", "16"], "answer": "8"}
                ]
            },
            {
                "title": "Module 2.2: Formulation",
                "blocks": [
                    {"type": "concept", "title": "Problem Formulation", "content": "The process of deciding what actions and states to consider, given a goal."},
                    {"type": "narrative", "content": "If you don't define the state space correctly, the agent is lost in irrelevant details."},
                    {"type": "interactive", "question": "What is the result of problem formulation?", "options": ["A state space, initial state, actions, transition model, and goal test", "The optimal path", "A heuristic function"], "answer": "A state space, initial state, actions, transition model, and goal test"},
                    {"type": "concept", "title": "Transition Model", "content": "Describes what each action does; formally, RESULT(s, a) returns the state that results from doing action a in state s."},
                    {"type": "concept", "title": "Path Cost", "content": "A function that assigns a numeric cost to each path. We want to minimize this cost."},
                    {"type": "narrative", "content": "Now, we have a map of the world inside the machine, ready to be searched."}
                ]
            }
        ]
    },
    "case_03": {
        "title": "Case 03: The Maze Without a Map (BFS, DFS, UCS)",
        "modules": [
            {
                "title": "Module 3.1: Breadth-First Search (BFS)",
                "blocks": [
                    {"type": "narrative", "content": "You are blindfolded in a maze. You can only feel the walls."},
                    {"type": "concept", "title": "Uninformed Search", "content": "Search algorithms that have no additional information about states beyond that provided in the problem definition."},
                    {"type": "concept", "title": "BFS", "content": "Expands the shallowest unexpanded node. Implemented with a FIFO queue."},
                    {
                        "type": "visual_stepper",
                        "title": "BFS Algorithm",
                        "steps": [
                            {
                                "step_title": "Step 1: Start at Root",
                                "explanation": "We begin at node A.",
                                "mermaid": "graph TD\n  A[\"A\"]:::active --> B[\"B\"]\n  A --> C[\"C\"]\n  B --> D[\"D\"]\n  B --> E[\"E\"]\n  classDef active fill:#FF5733,stroke:#333333,stroke-width:2px;"
                            },
                            {
                                "step_title": "Step 2: Expand Level 1",
                                "explanation": "Expand A's children, B and C. They are placed in the FIFO queue.",
                                "mermaid": "graph TD\n  A[\"A\"]:::visited --> B[\"B\"]:::active\n  A --> C[\"C\"]:::active\n  B --> D[\"D\"]\n  B --> E[\"E\"]\n  classDef active fill:#FF5733,stroke:#333333,stroke-width:2px;\n  classDef visited fill:#C0C0C0,stroke:#333333,stroke-width:2px;"
                            },
                            {
                                "step_title": "Step 3: Expand Level 2",
                                "explanation": "Expand B's and C's children across the entire breadth.",
                                "mermaid": "graph TD\n  A[\"A\"]:::visited --> B[\"B\"]:::visited\n  A --> C[\"C\"]:::visited\n  B --> D[\"D\"]:::active\n  B --> E[\"E\"]:::active\n  classDef active fill:#FF5733,stroke:#333333,stroke-width:2px;\n  classDef visited fill:#C0C0C0,stroke:#333333,stroke-width:2px;"
                            }
                        ]
                    },
                    {"type": "interactive", "question": "What data structure is typically used for the frontier in BFS?", "options": ["FIFO Queue", "LIFO Stack", "Priority Queue"], "answer": "FIFO Queue"},
                    {"type": "concept", "title": "BFS Properties", "content": "BFS is complete. It is optimal if step costs are identical. Its time and space complexity is O(b^d)."}
                ]
            },
            {
                "title": "Module 3.2: Depth-First Search (DFS) & UCS",
                "blocks": [
                    {"type": "concept", "title": "DFS", "content": "Expands the deepest unexpanded node. Implemented with a LIFO stack."},
                    {
                        "type": "visual_stepper",
                        "title": "DFS Algorithm",
                        "steps": [
                            {
                                "step_title": "Step 1: Start",
                                "explanation": "Start at node A.",
                                "mermaid": "graph TD\n  A[\"A\"]:::active --> B[\"B\"]\n  A --> C[\"C\"]\n  B --> D[\"D\"]\n  B --> E[\"E\"]\n  classDef active fill:#FF5733,stroke:#333333,stroke-width:2px;"
                            },
                            {
                                "step_title": "Step 2: Dive Deep",
                                "explanation": "Go to B.",
                                "mermaid": "graph TD\n  A[\"A\"]:::visited --> B[\"B\"]:::active\n  A --> C[\"C\"]\n  B --> D[\"D\"]\n  B --> E[\"E\"]\n  classDef active fill:#FF5733,stroke:#333333,stroke-width:2px;\n  classDef visited fill:#C0C0C0,stroke:#333333,stroke-width:2px;"
                            },
                            {
                                "step_title": "Step 3: Dive Deeper",
                                "explanation": "Go straight down to D before visiting siblings like C or E.",
                                "mermaid": "graph TD\n  A[\"A\"]:::visited --> B[\"B\"]:::visited\n  A --> C[\"C\"]\n  B --> D[\"D\"]:::active\n  B --> E[\"E\"]\n  classDef active fill:#FF5733,stroke:#333333,stroke-width:2px;\n  classDef visited fill:#C0C0C0,stroke:#333333,stroke-width:2px;"
                            }
                        ]
                    },
                    {"type": "concept", "title": "Uniform-Cost Search (UCS)", "content": "Expands the node n with the lowest path cost g(n). Implemented with a priority queue."},
                    {"type": "interactive", "question": "If step costs are equal, UCS behaves like:", "options": ["BFS", "DFS", "Random Search"], "answer": "BFS"},
                    {"type": "narrative", "content": "Uninformed search has limits. We need a compass."}
                ]
            }
        ]
    },
    "case_04": {
        "title": "Case 04: The Search for the Better Path (Heuristics, A*)",
        "modules": [
            {
                "title": "Module 4.1: Heuristics",
                "blocks": [
                    {"type": "narrative", "content": "You found a compass in the maze. It gives you a sense of direction."},
                    {"type": "concept", "title": "Informed Search", "content": "Uses problem-specific knowledge beyond the definition of the problem itself. It can find solutions more efficiently than uninformed strategies."},
                    {"type": "concept", "title": "Heuristic Function h(n)", "content": "Estimated cost of the cheapest path from the state at node n to a goal state. For example, straight-line distance to the destination."},
                    {"type": "interactive", "question": "What does a heuristic function h(n) estimate?", "options": ["Cost to goal", "Cost from start", "Total path cost"], "answer": "Cost to goal"},
                    {"type": "narrative", "content": "With a heuristic, we can guide our search towards the goal instead of wandering blindly."}
                ]
            },
            {
                "title": "Module 4.2: A* Search",
                "blocks": [
                    {"type": "concept", "title": "A* Search", "content": "Evaluates nodes by combining g(n), the cost to reach the node, and h(n), the estimated cost to get from the node to the goal: f(n) = g(n) + h(n)."},
                    {
                        "type": "visual_stepper",
                        "title": "A* Algorithm",
                        "steps": [
                            {
                                "step_title": "Step 1: Start Node",
                                "explanation": "Start at node A. f(A) = g(A) + h(A) = 0 + 10 = 10.",
                                "mermaid": "graph TD\n  A[\"A f=10\"]:::active --> B[\"B h=6\"]\n  A --> C[\"C h=8\"]\n  classDef active fill:#FF5733,stroke:#333333,stroke-width:2px;"
                            },
                            {
                                "step_title": "Step 2: Expand A",
                                "explanation": "Calculate f for B and C. Path to B cost 3, f(B) = 3 + 6 = 9. Path to C cost 2, f(C) = 2 + 8 = 10.",
                                "mermaid": "graph TD\n  A[\"A f=10\"]:::visited --> B[\"B f=9\"]:::active\n  A --> C[\"C f=10\"]\n  classDef active fill:#FF5733,stroke:#333333,stroke-width:2px;\n  classDef visited fill:#C0C0C0,stroke:#333333,stroke-width:2px;"
                            },
                            {
                                "step_title": "Step 3: Expand B (lowest f)",
                                "explanation": "Expand B because it has the lowest f-value (9 < 10).",
                                "mermaid": "graph TD\n  A[\"A\"]:::visited --> B[\"B f=9\"]:::visited\n  A --> C[\"C f=10\"]:::active\n  B --> D[\"Goal f=8\"]:::active\n  classDef active fill:#FF5733,stroke:#333333,stroke-width:2px;\n  classDef visited fill:#C0C0C0,stroke:#333333,stroke-width:2px;"
                            }
                        ]
                    },
                    {"type": "interactive", "question": "In A*, what is f(n)?", "options": ["g(n) + h(n)", "g(n) - h(n)", "h(n) / g(n)"], "answer": "g(n) + h(n)"},
                    {"type": "concept", "title": "Optimality", "content": "A* is complete and optimal if the heuristic is admissible (for tree search) or consistent (for graph search)."}
                ]
            }
        ]
    },
    "case_05": {
        "title": "Case 05: The Heuristic Detective (Deep A*, Admissibility)",
        "modules": [
            {
                "title": "Module 5.1: Admissibility and Consistency",
                "blocks": [
                    {"type": "narrative", "content": "Is the compass reliable? We must investigate the nature of our heuristic."},
                    {"type": "concept", "title": "Admissible Heuristics", "content": "An admissible heuristic never overestimates the cost to reach the goal. It is optimistic. It thinks the goal is closer or cheaper to reach than it actually is."},
                    {"type": "concept", "title": "Consistent Heuristics", "content": "A heuristic h is consistent if, for every node n and every successor n' of n generated by any action a, the estimated cost of reaching the goal from n is no greater than the step cost of getting to n' plus the estimated cost of reaching the goal from n'."},
                    {"type": "interactive", "question": "An admissible heuristic is always:", "options": ["Optimistic", "Pessimistic", "Accurate"], "answer": "Optimistic"},
                    {"type": "narrative", "content": "Consistency implies admissibility, but not vice versa. Consistency ensures that f(n) values are non-decreasing along any path."}
                ]
            },
            {
                "title": "Module 5.2: Dominance and Deep A*",
                "blocks": [
                    {"type": "concept", "title": "Dominance", "content": "If h2(n) >= h1(n) for all n (both admissible), then h2 dominates h1, and A* using h2 will expand fewer nodes."},
                    {"type": "narrative", "content": "We want the most dominant admissible heuristic to search faster."},
                    {
                        "type": "visual_stepper",
                        "title": "Heuristic Comparison",
                        "steps": [
                            {
                                "step_title": "Step 1: Weak Heuristic",
                                "explanation": "Using h1 (weak), A* explores many nodes, almost like BFS.",
                                "mermaid": "graph TD\n  A[\"A\"]:::visited --> B[\"B\"]:::visited\n  A --> C[\"C\"]:::visited\n  B --> D[\"D\"]:::visited\n  C --> E[\"E\"]:::visited\n  classDef visited fill:#C0C0C0,stroke:#333333,stroke-width:2px;"
                            },
                            {
                                "step_title": "Step 2: Strong Heuristic",
                                "explanation": "Using h2 (strong, dominates h1), A* zeroes in on the goal immediately.",
                                "mermaid": "graph TD\n  A[\"A\"]:::visited --> C[\"C\"]:::visited\n  C --> E[\"Goal E\"]:::active\n  classDef active fill:#FF5733,stroke:#333333,stroke-width:2px;\n  classDef visited fill:#C0C0C0,stroke:#333333,stroke-width:2px;"
                            }
                        ]
                    },
                    {"type": "interactive", "question": "If h2 dominates h1, which one is generally better for A*?", "options": ["h2", "h1"], "answer": "h2"},
                    {"type": "narrative", "content": "You have mastered the search. The path is clear and optimal."}
                ]
            }
        ]
    }
}
