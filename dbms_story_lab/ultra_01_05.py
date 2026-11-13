CONTENT_01_05 = {
    "1": {
        "modules": [
            {
                "title": "Module 1.1: The Essence of Rational Agents",
                "episodes": [
                    {"type": "markdown", "content": "Welcome to Case 1! In Artificial Intelligence, an agent is anything that perceives its environment through sensors and acts upon that environment through actuators."},
                    {"type": "concept", "content": "Rationality: A rational agent chooses whichever action maximizes the expected value of the performance measure given the percept sequence to date."},
                    {"type": "visual", "content": "graph TD\n  Environment[\"Environment\"] -->|Percepts| Sensors[\"Sensors\"]\n  Sensors --> Agent[\"Agent\"]\n  Agent --> Actuators[\"Actuators\"]\n  Actuators -->|Actions| Environment\n  style Environment fill:#10b9811a"},
                    {"type": "markdown", "content": "The concept of an agent provides a unifying framework for studying AI. We can consider humans, robots, and softbots all as agents."},
                    {"type": "interactive", "content": "Question: What does an agent use to perceive its environment? \nOptions: 1) Actuators 2) Sensors 3) Heuristics. \nAnswer: 2"},
                    {"type": "concept", "content": "Omniscience vs Rationality: An omniscient agent knows the actual outcome of its actions and can act accordingly; but omniscience is impossible in reality. Rationality maximizes *expected* performance."},
                    {"type": "markdown", "content": "Let's explore the PEAS framework, which helps us design agents by specifying the task environment."},
                    {"type": "visual_stepper", "content": "graph TD\n  P[\"Performance Measure\"]\n  E[\"Environment\"]\n  A[\"Actuators\"]\n  S[\"Sensors\"]\n  style P fill:#3b82f61a"},
                    {"type": "concept", "content": "PEAS stands for Performance measure, Environment, Actuators, and Sensors."},
                    {"type": "code_lab", "content": "class SimpleAgent:\n    def __init__(self):\n        self.percepts = []\n    def act(self, percept):\n        self.percepts.append(percept)\n        return 'ACTION_DEFAULT'"}
                ]
            },
            {
                "title": "Module 1.2: Structuring the Task Environment (PEAS)",
                "episodes": [
                    {"type": "markdown", "content": "To design a rational agent, we must first specify its task environment as fully as possible using the PEAS description."},
                    {"type": "concept", "content": "Performance Measure: Defines the criteria for success of the agent's behavior."},
                    {"type": "interactive", "content": "Question: In a self-driving car, what is NOT a good performance measure? \nOptions: 1) Safety 2) Speed 3) Number of pedestrians hit 4) Fuel usage. \nAnswer: 3"},
                    {"type": "visual", "content": "graph LR\n  Task[\"Automated Taxi\"]\n  Task --> P[\"P: Safe, Fast, Legal\"]\n  Task --> E[\"E: Roads, Traffic, Pedestrians\"]\n  Task --> A[\"A: Steering, Accelerator, Brake\"]\n  Task --> S[\"S: Cameras, Sonar, Speedometer\"]\n  style Task fill:#8b5cf61a"},
                    {"type": "markdown", "content": "Consider a medical diagnosis system. The performance measure might be healthy patient, reduced costs, and minimized lawsuits."},
                    {"type": "concept", "content": "Environment properties: Fully vs Partially Observable, Single vs Multi-agent, Deterministic vs Stochastic, Episodic vs Sequential, Static vs Dynamic, Discrete vs Continuous, Known vs Unknown."},
                    {"type": "visual_stepper", "content": "graph TD\n  Fully[\"Fully Observable\"]\n  Partially[\"Partially Observable\"]\n  Fully -->|Chess| Deterministic[\"Deterministic\"]\n  Partially -->|Poker| Stochastic[\"Stochastic\"]"},
                    {"type": "markdown", "content": "Chess with a clock is fully observable, deterministic, sequential, dynamic, discrete, and known. Poker is partially observable and stochastic."},
                    {"type": "interactive", "content": "Question: Is the real world discrete or continuous? \nOptions: 1) Discrete 2) Continuous. \nAnswer: 2"},
                    {"type": "code_lab", "content": "def check_environment_type(is_fully_observable):\n    if is_fully_observable:\n        return 'Easy to plan'\n    else:\n        return 'Need memory/state'"}
                ]
            },
            {
                "title": "Module 1.3: Types of Agent Programs",
                "episodes": [
                    {"type": "markdown", "content": "Agent programs map percepts to actions. We will explore four basic types of agent programs in order of increasing generality."},
                    {"type": "concept", "content": "Simple Reflex Agents: These agents select actions on the basis of the current percept, ignoring the rest of the percept history."},
                    {"type": "visual", "content": "graph TD\n  Sensors[\"Sensors\"] --> Rules[\"Condition-Action Rules\"]\n  Rules --> Actuators[\"Actuators\"]\n  style Rules fill:#ef44441a"},
                    {"type": "markdown", "content": "Simple reflex agents are simple but of limited intelligence. They only work if the environment is fully observable."},
                    {"type": "interactive", "content": "Question: What do simple reflex agents rely on? \nOptions: 1) Percept history 2) Current percept only 3) Future predictions. \nAnswer: 2"},
                    {"type": "concept", "content": "Model-based Reflex Agents: These agents maintain an internal state that depends on the percept history and thereby reflects at least some of the unobserved aspects of the current state."},
                    {"type": "visual_stepper", "content": "graph TD\n  State[\"State\"]\n  Evolution[\"How the world evolves\"]\n  Effect[\"What my actions do\"]\n  State --> Rules[\"Condition-Action Rules\"]\n  style State fill:#10b9811a"},
                    {"type": "markdown", "content": "A model-based agent updates its internal state based on its model of how the world evolves independently of the agent, and how the agent's own actions affect the world."},
                    {"type": "interactive", "content": "Question: Why maintain an internal state? \nOptions: 1) To handle partially observable environments 2) To increase speed. \nAnswer: 1"},
                    {"type": "code_lab", "content": "class ModelBasedAgent:\n    def __init__(self):\n        self.state = {}\n    def update_state(self, percept):\n        self.state['latest'] = percept\n        return 'ACTION_BASED_ON_STATE'"}
                ]
            },
            {
                "title": "Module 1.4: Goal and Utility-Based Agents",
                "episodes": [
                    {"type": "markdown", "content": "Knowing the current state of the environment is not always enough to decide what to do. The agent needs some sort of goal information that describes situations that are desirable."},
                    {"type": "concept", "content": "Goal-based Agents: These agents use goal information combined with the environment model to choose actions that achieve the goal."},
                    {"type": "visual", "content": "graph TD\n  State[\"State\"] --> WhatIf[\"What it will be like if I do action A\"]\n  WhatIf --> Goals[\"Goals\"]\n  Goals --> Action[\"Action\"]\n  style Goals fill:#f59e0b1a"},
                    {"type": "markdown", "content": "Search and planning are the subfields of AI devoted to finding action sequences that achieve the agent's goals."},
                    {"type": "interactive", "content": "Question: Does a goal-based agent consider the future? \nOptions: 1) Yes, it evaluates action outcomes against goals 2) No, it only uses rules. \nAnswer: 1"},
                    {"type": "concept", "content": "Utility-based Agents: Goals just provide a crude binary distinction between 'happy' and 'unhappy' states. A more general performance measure should allow a comparison of different world states according to exactly how happy they would make the agent."},
                    {"type": "visual_stepper", "content": "graph TD\n  State[\"State\"] --> Utility[\"Utility Function\"]\n  Utility --> Maximize[\"Maximize Expected Utility\"]\n  style Utility fill:#6366f11a"},
                    {"type": "markdown", "content": "An agent's utility function is essentially an internalization of the performance measure."},
                    {"type": "interactive", "content": "Question: What is the main advantage of utility over goals? \nOptions: 1) Handles trade-offs and uncertainty 2) Requires less memory. \nAnswer: 1"},
                    {"type": "code_lab", "content": "def calculate_utility(state):\n    reward = state.get('reward', 0)\n    cost = state.get('cost', 0)\n    return reward - cost"}
                ]
            }
        ]
    },
    "2": {
        "modules": [
            {
                "title": "Module 2.1: Formalizing Problems and State Spaces",
                "episodes": [
                    {"type": "markdown", "content": "In Case 2, we dive into problem-solving agents. These are goal-based agents that decide what to do by finding sequences of actions that lead to desirable states."},
                    {"type": "concept", "content": "Problem Formulation: The process of deciding what actions and states to consider, given a goal."},
                    {"type": "visual", "content": "graph TD\n  Goal[\"Goal Formulation\"] --> Problem[\"Problem Formulation\"]\n  Problem --> Search[\"Search\"]\n  Search --> Execute[\"Execution\"]\n  style Search fill:#10b9811a"},
                    {"type": "markdown", "content": "Before an agent can start searching for solutions, it must formulate a goal and then formulate the problem."},
                    {"type": "interactive", "content": "Question: Which comes first in problem-solving? \nOptions: 1) Search 2) Goal Formulation 3) Execution. \nAnswer: 2"},
                    {"type": "concept", "content": "A problem can be defined formally by five components: Initial State, Actions, Transition Model, Goal Test, and Path Cost."},
                    {"type": "visual_stepper", "content": "graph LR\n  Init[\"Initial State: In(Arad)\"]\n  Actions[\"Actions: Go(Zerind), Go(Sibiu), Go(Timisoara)\"]\n  Model[\"Transition: Result(In(Arad), Go(Zerind)) = In(Zerind)\"]\n  style Init fill:#3b82f61a"},
                    {"type": "markdown", "content": "The set of all states reachable from the initial state by any sequence of actions is the State Space of the problem."},
                    {"type": "interactive", "content": "Question: What function defines the resulting state after taking an action? \nOptions: 1) Goal Test 2) Path Cost 3) Transition Model. \nAnswer: 3"},
                    {"type": "code_lab", "content": "class Problem:\n    def __init__(self, initial, goal):\n        self.initial = initial\n        self.goal = goal\n    def goal_test(self, state):\n        return state == self.goal"}
                ]
            },
            {
                "title": "Module 2.2: The Toy Problems",
                "episodes": [
                    {"type": "markdown", "content": "To illustrate problem formulation, AI researchers often use toy problems like the Vacuum World or the 8-puzzle."},
                    {"type": "concept", "content": "Vacuum World State Space: Consider 2 locations, each can be clean or dirty, and the agent can be in either location. Total states: 2 * 2^2 = 8."},
                    {"type": "visual", "content": "graph TD\n  State1[\"Both Dirty, Agent Left\"]\n  State2[\"Left Clean, Right Dirty, Agent Left\"]\n  State1 -->|Suck| State2\n  style State1 fill:#ef44441a"},
                    {"type": "markdown", "content": "The 8-puzzle consists of a 3x3 board with 8 numbered tiles and a blank space. A tile adjacent to the blank space can slide into the space."},
                    {"type": "interactive", "content": "Question: How many possible states are there in the 8-puzzle? \nOptions: 1) 9! 2) 8! 3) 9!/2. \nAnswer: 3"},
                    {"type": "concept", "content": "The state space size for the 8-puzzle is 9!/2 = 181,440. For the 15-puzzle, it's 16!/2, which is roughly 10 trillion. This highlights the problem of state explosion."},
                    {"type": "visual_stepper", "content": "graph LR\n  S1[\"1 2 3\"]\n  S2[\"4 5 6\"]\n  S3[\"7 8  \"]\n  S1 -.-> S2 -.-> S3\n  style S1 fill:#f59e0b1a"},
                    {"type": "markdown", "content": "Path cost is usually the number of steps in the path, so each step costs 1. The goal is to reach a specific configuration."},
                    {"type": "interactive", "content": "Question: Why do we care about path cost? \nOptions: 1) To find the optimal solution 2) To formulate the goal. \nAnswer: 1"},
                    {"type": "code_lab", "content": "def path_cost(c, state1, action, state2):\n    return c + 1  # Uniform step cost"}
                ]
            },
            {
                "title": "Module 2.3: Real World Problems",
                "episodes": [
                    {"type": "markdown", "content": "While toy problems are great for understanding, AI is applied to complex real-world problems."},
                    {"type": "concept", "content": "Route-Finding: Used in routing video streams, military operations planning, and airline travel planning. It involves finding the best path between locations."},
                    {"type": "visual", "content": "graph LR\n  A[\"City A\"]\n  B[\"City B\"]\n  C[\"City C\"]\n  A -->|100km| B\n  A -->|150km| C\n  B -->|80km| C\n  style A fill:#10b9811a"},
                    {"type": "markdown", "content": "Touring Problems: The agent must visit every state at least once. The Traveling Salesperson Problem (TSP) is a famous example where the goal is to find the shortest tour."},
                    {"type": "interactive", "content": "Question: Is the Traveling Salesperson Problem NP-hard? \nOptions: 1) Yes 2) No. \nAnswer: 1"},
                    {"type": "concept", "content": "Robot Navigation: This is a generalization of route-finding. Rather than a discrete set of routes, a robot can move in a continuous space with an infinite set of possible actions."},
                    {"type": "visual_stepper", "content": "graph TD\n  Start[\"Start Position\"]\n  Obstacle[\"Obstacle\"]\n  Goal[\"Goal Position\"]\n  Start -->|Avoid| Obstacle\n  Start -->|Path| Goal"},
                    {"type": "markdown", "content": "Protein Design: The goal is to find a sequence of amino acids that will fold into a 3D protein with the right properties. This state space is massive."},
                    {"type": "interactive", "content": "Question: In real-world problems, state spaces are typically: \nOptions: 1) Small and discrete 2) Large or infinite. \nAnswer: 2"},
                    {"type": "code_lab", "content": "class TSPNode:\n    def __init__(self, city, visited):\n        self.city = city\n        self.visited = visited"}
                ]
            },
            {
                "title": "Module 2.4: Measuring Problem-Solving Performance",
                "episodes": [
                    {"type": "markdown", "content": "Before we evaluate search algorithms, we need to establish the criteria by which they will be judged."},
                    {"type": "concept", "content": "We evaluate an algorithm's performance in four ways: Completeness, Optimality, Time Complexity, and Space Complexity."},
                    {"type": "visual", "content": "graph TD\n  P[\"Performance\"]\n  P --> C[\"Completeness\"]\n  P --> O[\"Optimality\"]\n  P --> T[\"Time Complexity\"]\n  P --> S[\"Space Complexity\"]\n  style P fill:#6366f11a"},
                    {"type": "markdown", "content": "Completeness answers the question: Is the algorithm guaranteed to find a solution when there is one?"},
                    {"type": "interactive", "content": "Question: What does optimality guarantee? \nOptions: 1) Finds a solution quickly 2) Finds the lowest path-cost solution. \nAnswer: 2"},
                    {"type": "concept", "content": "Time and Space Complexity are often measured in terms of the branching factor (b), the depth of the shallowest goal node (d), and the maximum length of any path in the state space (m)."},
                    {"type": "visual_stepper", "content": "graph TD\n  Root[\"Root Node\"]\n  Child1[\"Child 1\"]\n  Child2[\"Child 2\"]\n  Root --> Child1\n  Root --> Child2\n  style Root fill:#8b5cf61a"},
                    {"type": "markdown", "content": "In AI, space complexity is often the biggest bottleneck because search trees can grow exponentially, quickly exhausting available memory."},
                    {"type": "interactive", "content": "Question: Which parameter represents the maximum length of any path in the state space? \nOptions: 1) b 2) d 3) m. \nAnswer: 3"},
                    {"type": "code_lab", "content": "def calculate_complexity(b, d):\n    # Calculates O(b^d)\n    return b ** d"}
                ]
            }
        ]
    },
    "3": {
        "modules": [
            {
                "title": "Module 3.1: Uninformed Search Strategies",
                "episodes": [
                    {"type": "markdown", "content": "Case 3 introduces Uninformed Search, also known as blind search. These strategies have no additional information about states beyond that provided in the problem definition."},
                    {"type": "concept", "content": "Breadth-First Search (BFS): A simple strategy in which the root node is expanded first, then all the successors of the root node are expanded next, then their successors, and so on."},
                    {"type": "visual", "content": "graph TD\n  A[\"Level 0 (A)\"] --> B[\"Level 1 (B)\"]\n  A --> C[\"Level 1 (C)\"]\n  B --> D[\"Level 2 (D)\"]\n  B --> E[\"Level 2 (E)\"]\n  style A fill:#3b82f61a\n  style B fill:#3b82f61a\n  style C fill:#3b82f61a"},
                    {"type": "markdown", "content": "BFS uses a FIFO (First-In-First-Out) queue. It systematically searches level by level."},
                    {"type": "interactive", "content": "Question: Is Breadth-First Search complete? \nOptions: 1) Yes, if branching factor is finite 2) No, it can get stuck in infinite loops. \nAnswer: 1"},
                    {"type": "concept", "content": "BFS Optimality: BFS is optimal if the path cost is a non-decreasing function of the depth of the node (e.g., when all actions have the same cost)."},
                    {"type": "visual_stepper", "content": "graph TD\n  F[\"Frontier: FIFO Queue\"]\n  N1[\"Node 1\"]\n  N2[\"Node 2\"]\n  F --> N1\n  F --> N2\n  style F fill:#10b9811a"},
                    {"type": "markdown", "content": "The main issue with BFS is its space complexity. Every node generated must remain in memory. The space complexity is O(b^d)."},
                    {"type": "interactive", "content": "Question: What is the time complexity of BFS? \nOptions: 1) O(b^d) 2) O(b*d) 3) O(d^b). \nAnswer: 1"},
                    {"type": "code_lab", "content": "from collections import deque\ndef bfs(problem):\n    frontier = deque([problem.initial])\n    explored = set()\n    while frontier:\n        node = frontier.popleft()\n        # ... check goal and expand ..."}
                ]
            },
            {
                "title": "Module 3.2: Depth-First Search (DFS)",
                "episodes": [
                    {"type": "markdown", "content": "Depth-First Search always expands the deepest node in the current frontier of the search tree."},
                    {"type": "concept", "content": "DFS uses a LIFO (Last-In-First-Out) queue, also known as a stack. It proceeds immediately to the deepest level of the search tree, where the nodes have no successors."},
                    {"type": "visual", "content": "graph TD\n  A[\"Root (A)\"] --> B[\"Deepest (B)\"]\n  B --> C[\"Deeper (C)\"]\n  C --> D[\"Leaf (D)\"]\n  A --> E[\"Other Branch (E)\"]\n  style A fill:#ef44441a\n  style B fill:#ef44441a\n  style C fill:#ef44441a\n  style D fill:#ef44441a"},
                    {"type": "markdown", "content": "Once a node is expanded and it has no successors, the search 'backs up' to the next deepest node that still has unexplored successors."},
                    {"type": "interactive", "content": "Question: What data structure does DFS use for its frontier? \nOptions: 1) FIFO Queue 2) LIFO Queue (Stack) 3) Priority Queue. \nAnswer: 2"},
                    {"type": "concept", "content": "Properties of DFS: The tree-search version of DFS is incomplete because it can fail in infinite spaces or spaces with loops. It is also not optimal."},
                    {"type": "visual_stepper", "content": "graph TD\n  F[\"Frontier: Stack\"]\n  Top[\"Top of Stack\"]\n  Bottom[\"Bottom of Stack\"]\n  F --> Top\n  style F fill:#f59e0b1a"},
                    {"type": "markdown", "content": "The advantage of DFS is its space complexity. For a state space with maximum depth m and branching factor b, DFS requires storage of only O(bm) nodes."},
                    {"type": "interactive", "content": "Question: Why might DFS be preferred over BFS? \nOptions: 1) Better time complexity 2) Drastically lower space complexity. \nAnswer: 2"},
                    {"type": "code_lab", "content": "def dfs(problem):\n    frontier = [problem.initial] # Stack\n    explored = set()\n    while frontier:\n        node = frontier.pop() # LIFO behavior\n        # ... expand ..."}
                ]
            },
            {
                "title": "Module 3.3: Uniform-Cost Search",
                "episodes": [
                    {"type": "markdown", "content": "Breadth-first search is optimal when all step costs are equal. Uniform-cost search generalizes BFS for any step-cost function."},
                    {"type": "concept", "content": "Uniform-Cost Search (UCS) expands the node n with the lowest path cost g(n). This is done by storing the frontier as a priority queue ordered by g."},
                    {"type": "visual", "content": "graph TD\n  S[\"Start\"] --10--> A[\"Node A, g=10\"]\n  S --5--> B[\"Node B, g=5\"]\n  B --2--> C[\"Node C, g=7\"]\n  style B fill:#10b9811a\n  style C fill:#10b9811a"},
                    {"type": "markdown", "content": "UCS does not care about the number of steps a path has, but only about their total cost. Therefore, it will get stuck in an infinite loop if there is a path with an infinite sequence of zero-cost actions."},
                    {"type": "interactive", "content": "Question: UCS is optimal if all step costs are strictly greater than some small positive constant epsilon. \nOptions: 1) True 2) False. \nAnswer: 1"},
                    {"type": "concept", "content": "In UCS, the goal test is applied to a node when it is selected for *expansion*, rather than when it is first generated, to ensure optimality."},
                    {"type": "visual_stepper", "content": "graph TD\n  F[\"Frontier: Priority Queue\"]\n  Min[\"Node with min g(n)\"]\n  F --> Min\n  style F fill:#6366f11a"},
                    {"type": "markdown", "content": "UCS is complete and optimal (assuming step costs >= epsilon > 0), but its time and space complexity can be high because it explores large trees of small steps before exploring paths involving large steps."},
                    {"type": "interactive", "content": "Question: What data structure does UCS use? \nOptions: 1) Stack 2) Priority Queue ordered by path cost. \nAnswer: 2"},
                    {"type": "code_lab", "content": "import heapq\ndef uniform_cost_search(problem):\n    frontier = []\n    heapq.heappush(frontier, (0, problem.initial)) # (cost, node)\n    # ... loop and pop lowest cost ..."}
                ]
            },
            {
                "title": "Module 3.4: Depth-Limited and Iterative Deepening Search",
                "episodes": [
                    {"type": "markdown", "content": "The failure of DFS in infinite spaces can be alleviated by supplying DFS with a predetermined depth limit 'l'."},
                    {"type": "concept", "content": "Depth-Limited Search (DLS): Nodes at depth 'l' are treated as if they have no successors. This solves the infinite path problem but introduces a completeness problem if the goal is deeper than 'l'."},
                    {"type": "visual", "content": "graph TD\n  L0[\"Level 0\"] --> L1[\"Level 1\"]\n  L1 --> L2[\"Level 2 (Limit)\"]\n  L2 -.-x L3[\"Level 3 (Unexplored)\"]\n  style L2 fill:#ef44441a"},
                    {"type": "markdown", "content": "Iterative Deepening Search (IDS) is a general strategy that gradually increases the limit until a goal is found."},
                    {"type": "interactive", "content": "Question: What happens in DLS if the shallowest goal is at depth d > l? \nOptions: 1) It finds the goal slowly 2) It fails to find the goal. \nAnswer: 2"},
                    {"type": "concept", "content": "IDS combines the benefits of depth-first and breadth-first search. It has the modest memory requirements of DFS and the completeness of BFS."},
                    {"type": "visual_stepper", "content": "graph TD\n  Iter0[\"Limit = 0\"]\n  Iter1[\"Limit = 1\"]\n  Iter2[\"Limit = 2\"]\n  Iter0 --> Iter1 --> Iter2\n  style Iter2 fill:#10b9811a"},
                    {"type": "markdown", "content": "It might seem wasteful that IDS generates the upper levels of the tree multiple times, but for most problems where the branching factor is > 1, the vast majority of nodes are in the bottom level, so the repeated overhead is small."},
                    {"type": "interactive", "content": "Question: What is the space complexity of IDS? \nOptions: 1) O(bd) 2) O(b^d). \nAnswer: 1"},
                    {"type": "code_lab", "content": "def iterative_deepening_search(problem):\n    for depth in range(sys.maxsize):\n        result = depth_limited_search(problem, depth)\n        if result != 'cutoff': return result"}
                ]
            }
        ]
    },
    "5": {
        "modules": [
            {
                "title": "Module 5.1: Informed Search and Heuristics",
                "episodes": [
                    {"type": "markdown", "content": "Case 5 moves beyond blind search. Informed search strategies use problem-specific knowledge beyond the definition of the problem itself to find solutions more efficiently."},
                    {"type": "concept", "content": "The key to informed search is a heuristic function, h(n). h(n) = estimated cost of the cheapest path from the state at node n to a goal state."},
                    {"type": "visual", "content": "graph TD\n  Node[\"Current Node n\"]\n  Goal[\"Goal Node\"]\n  Node -.->|h(n): Estimated Cost| Goal\n  style Node fill:#3b82f61a"},
                    {"type": "markdown", "content": "Heuristic functions are the most common form in which additional knowledge of the problem is imparted to the search algorithm."},
                    {"type": "interactive", "content": "Question: If n is a goal node, what must h(n) equal? \nOptions: 1) Infinity 2) Zero 3) 1. \nAnswer: 2"},
                    {"type": "concept", "content": "Greedy Best-First Search tries to expand the node that is closest to the goal, on the grounds that this is likely to lead to a solution quickly. Thus, it evaluates nodes by using just the heuristic function: f(n) = h(n)."},
                    {"type": "visual_stepper", "content": "graph LR\n  A[\"Node A, h=5\"]\n  B[\"Node B, h=2\"]\n  C[\"Node C, h=9\"]\n  Start --> A\n  Start --> B\n  Start --> C\n  style B fill:#10b9811a"},
                    {"type": "markdown", "content": "Greedy search is often very fast, but like DFS, it is incomplete and not optimal. It can get stuck in dead ends."},
                    {"type": "interactive", "content": "Question: Does Greedy Best-First Search consider the cost to reach a node from the start state? \nOptions: 1) Yes 2) No. \nAnswer: 2"},
                    {"type": "code_lab", "content": "def greedy_best_first_search(problem, h):\n    # Sort frontier by h(n)\n    pass"}
                ]
            },
            {
                "title": "Module 5.2: A* Search",
                "episodes": [
                    {"type": "markdown", "content": "A* (A-star) search is the most widely known form of best-first search. It evaluates nodes by combining g(n) (cost to reach the node) and h(n) (estimated cost to get from the node to the goal)."},
                    {"type": "concept", "content": "Evaluation function: f(n) = g(n) + h(n). Since g(n) is the exact cost to reach n, and h(n) is the estimated cost from n to the goal, f(n) is the estimated total cost of the cheapest solution path going through n."},
                    {"type": "visual", "content": "graph TD\n  Start[\"Start\"] --g(n)--> Node[\"Node n\"]\n  Node -.h(n).-> Goal[\"Goal\"]\n  style Node fill:#8b5cf61a"},
                    {"type": "markdown", "content": "A* search is identical to Uniform-Cost Search except that A* uses g + h instead of just g."},
                    {"type": "interactive", "content": "Question: What does f(n) represent in A*? \nOptions: 1) Estimated total path cost 2) Cost from start only. \nAnswer: 1"},
                    {"type": "concept", "content": "For A* to be optimal with Tree Search, the heuristic h(n) must be Admissible. An admissible heuristic never overestimates the cost to reach the goal."},
                    {"type": "visual_stepper", "content": "graph TD\n  Admissible[\"h(n) <= true_cost(n, goal)\"]\n  Admissible --> Optimal[\"Optimal Tree Search\"]\n  style Admissible fill:#10b9811a"},
                    {"type": "markdown", "content": "Think of an admissible heuristic as being optimistic; it always thinks the cost to solve the problem is less than or equal to the actual cost. Straight-line distance is an admissible heuristic for routing problems."},
                    {"type": "interactive", "content": "Question: If actual cost is 10, which heuristic value is NOT admissible? \nOptions: 1) 8 2) 10 3) 12. \nAnswer: 3"},
                    {"type": "code_lab", "content": "def a_star_search(problem, h):\n    # Priority queue ordered by f(n) = g(n) + h(n)\n    # f_cost = node.path_cost + h(node)\n    pass"}
                ]
            },
            {
                "title": "Module 5.3: Consistency and Graph Search Optimality",
                "episodes": [
                    {"type": "markdown", "content": "If we use Graph Search (which keeps an 'explored' set to avoid repeated states) with A*, Admissibility is not quite enough to guarantee optimality. We need a stronger condition called Consistency."},
                    {"type": "concept", "content": "A heuristic h(n) is consistent (or monotonic) if, for every node n and every successor n' of n generated by any action a, the estimated cost of reaching the goal from n is no greater than the step cost of getting to n' plus the estimated cost of reaching the goal from n'."},
                    {"type": "visual", "content": "graph LR\n  N[\"n (h=4)\"] --cost=1--> Nprime[\"n' (h=2)\"]\n  style N fill:#f59e0b1a\n  style Nprime fill:#3b82f61a"},
                    {"type": "markdown", "content": "Formal definition of consistency: h(n) <= c(n, a, n') + h(n'). This is a form of the triangle inequality."},
                    {"type": "interactive", "content": "Question: Consistency is required for optimality in which type of search? \nOptions: 1) Tree Search 2) Graph Search. \nAnswer: 2"},
                    {"type": "concept", "content": "If a heuristic is consistent, then the values of f(n) along any path are non-decreasing. Therefore, the first time Graph Search expands a node, it has found the optimal path to that node."},
                    {"type": "visual_stepper", "content": "graph TD\n  Consistent[\"Consistent Heuristic\"]\n  Consistent --> NonDecreasing[\"f(n) is non-decreasing along paths\"]\n  NonDecreasing --> Optimal[\"A* Graph Search is Optimal\"]\n  style Optimal fill:#10b9811a"},
                    {"type": "markdown", "content": "Every consistent heuristic is also admissible. However, an admissible heuristic is not necessarily consistent (though most admissible heuristics you invent will naturally be consistent)."},
                    {"type": "interactive", "content": "Question: Does consistency imply admissibility? \nOptions: 1) Yes 2) No. \nAnswer: 1"},
                    {"type": "code_lab", "content": "def check_consistency(h_n, cost, h_n_prime):\n    return h_n <= cost + h_n_prime"}
                ]
            },
            {
                "title": "Module 5.4: Designing Good Heuristics",
                "episodes": [
                    {"type": "markdown", "content": "The performance of A* depends highly on the quality of the heuristic. How do we design a good one?"},
                    {"type": "concept", "content": "Effective Branching Factor (b*): A measure of heuristic quality. If A* generates N nodes to find a solution at depth d, b* is the branching factor a uniform tree of depth d would need to have N nodes."},
                    {"type": "visual", "content": "graph TD\n  N_Nodes[\"N nodes generated\"]\n  Depth[\"Depth d\"]\n  Formula[\"N + 1 = 1 + b* + (b*)^2 + ... + (b*)^d\"]\n  N_Nodes --> Formula\n  Depth --> Formula\n  style Formula fill:#6366f11a"},
                    {"type": "markdown", "content": "A well-designed heuristic will have a b* close to 1.0, meaning the search goes almost straight to the goal."},
                    {"type": "interactive", "content": "Question: Is a lower or higher effective branching factor better? \nOptions: 1) Lower (closer to 1) 2) Higher. \nAnswer: 1"},
                    {"type": "concept", "content": "Domination: If heuristic h2(n) >= h1(n) for all n (and neither overestimates), then h2 dominates h1. A* using h2 will never expand more nodes than A* using h1."},
                    {"type": "visual_stepper", "content": "graph TD\n  H2[\"h2(n)\"]\n  H1[\"h1(n)\"]\n  H2 -->|Dominates| H1\n  H2 -->|Expands Fewer Nodes| H1\n  style H2 fill:#10b9811a"},
                    {"type": "markdown", "content": "One way to invent admissible heuristics is to relax the problem. A relaxed problem removes constraints on actions, making it easier to solve. The exact cost of a solution to a relaxed problem is an admissible heuristic for the original problem."},
                    {"type": "interactive", "content": "Question: In the 8-puzzle, is 'Manhattan Distance' a relaxed problem heuristic? \nOptions: 1) Yes, it assumes tiles can move through other tiles 2) No. \nAnswer: 1"},
                    {"type": "code_lab", "content": "def manhattan_distance(state, goal):\n    # Sum of vertical and horizontal distances of tiles from goal positions\n    pass"}
                ]
            }
        ]
    }
}
