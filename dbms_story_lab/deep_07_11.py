CONTENT_07_11 = {
    "case_07": {
        "title": "Case 07: The Impossible Puzzle (CSP, Backtracking)",
        "modules": [
            {
                "id": "c7_ep1",
                "title": "Episode 1: The Constraint Model",
                "blocks": [
                    {"type": "narrative", "content": "You stand before a massive stone door embedded with crystal nodes. They glow with an eerie light. A message on the wall reads: 'No two connected crystals may share the same hue.'"},
                    {"type": "concept", "content": "This is a classic Constraint Satisfaction Problem (CSP). In a CSP, you must find an assignment of values to a set of variables such that all constraints are satisfied."},
                    {"type": "detail", "content": "Variables: X = {C1, C2, C3, C4}. Domains: D = {Red, Green, Blue}. Constraints: C = {C1 != C2, C2 != C3...}."},
                    {"type": "visual_stepper", "title": "Building the Constraint Graph", "steps": [
                        {"description": "Step 1: Identify the variables as nodes.", "mermaid": "graph TD\n  C1[\"Crystal 1\"]\n  C2[\"Crystal 2\"]\n  style C1 fill:#ffffff,stroke:#000000\n  style C2 fill:#ffffff,stroke:#000000"},
                        {"description": "Step 2: Add edges for constraints.", "mermaid": "graph TD\n  C1[\"Crystal 1\"] --- C2[\"Crystal 2\"]\n  style C1 fill:#ffffff,stroke:#000000\n  style C2 fill:#ffffff,stroke:#000000"}
                    ]},
                    {"type": "narrative", "content": "The simplest way to solve this is to try combinations until one works. But with many nodes, this 'generate and test' approach takes too long."},
                    {"type": "concept", "content": "Backtracking Search is a depth-first search that chooses values for one variable at a time and backtracks when a variable has no legal values left to assign."},
                    {"type": "visual_stepper", "title": "Backtracking in Action", "steps": [
                        {"description": "Assign Red to C1.", "mermaid": "graph TD\n  C1[\"Crystal 1: Red\"] --- C2[\"Crystal 2\"]\n  style C1 fill:#ff0000,stroke:#000000\n  style C2 fill:#ffffff,stroke:#000000"},
                        {"description": "Assign Green to C2.", "mermaid": "graph TD\n  C1[\"Crystal 1: Red\"] --- C2[\"Crystal 2: Green\"]\n  style C1 fill:#ff0000,stroke:#000000\n  style C2 fill:#00ff00,stroke:#000000"}
                    ]},
                    {"type": "concept", "content": "Forward Checking: Whenever a variable X is assigned, look at each unassigned variable Y connected to X, and delete from Y's domain any value inconsistent with the value chosen for X."},
                    {"type": "narrative", "content": "Applying these strategies, the crystals resonate in harmony. The stone door grinds open."},
                    {"type": "quiz", "question": "What is the primary benefit of Forward Checking in CSPs?", "options": ["It guarantees a solution exists.", "It reduces the search space by pruning inconsistent values early.", "It converts the problem into a linear programming model."], "answer": 1}
                ]
            }
        ]
    },
    "case_08": {
        "title": "Case 08: The Knowledge Vault (Ontologies, Knowledge Graphs)",
        "modules": [
            {
                "id": "c8_ep1",
                "title": "Episode 1: Structuring the Unknown",
                "blocks": [
                    {"type": "narrative", "content": "Inside the vault, billions of loose documents swirl in a holographic vortex. You need a way to organize this chaos so the AI can understand relationships."},
                    {"type": "concept", "content": "An Ontology provides a formal naming and definition of the types, properties, and interrelationships of the entities that really exist in a particular domain of discourse."},
                    {"type": "detail", "content": "We use triples: (Subject, Predicate, Object). For example: (AI, is_a, Technology)."},
                    {"type": "visual_stepper", "title": "Constructing the Knowledge Graph", "steps": [
                        {"description": "Identify entities.", "mermaid": "graph LR\n  A[\"AI\"]\n  B[\"Technology\"]\n  style A fill:#aaddff,stroke:#000000\n  style B fill:#ffaadd,stroke:#000000"},
                        {"description": "Link entities with predicates.", "mermaid": "graph LR\n  A[\"AI\"] -->|is_a| B[\"Technology\"]\n  style A fill:#aaddff,stroke:#000000\n  style B fill:#ffaadd,stroke:#000000"}
                    ]},
                    {"type": "concept", "content": "Knowledge Graphs power semantic search, allowing the system to infer facts not explicitly stated. If A is-a B, and B is-a C, then A is-a C."},
                    {"type": "visual_stepper", "title": "Inference through Transitivity", "steps": [
                        {"description": "Base facts.", "mermaid": "graph LR\n  A[\"Machine Learning\"] -->|is_a| B[\"AI\"]\n  B[\"AI\"] -->|is_a| C[\"Technology\"]\n  style A fill:#aaddff,stroke:#000000\n  style B fill:#aaddff,stroke:#000000\n  style C fill:#ffaadd,stroke:#000000"},
                        {"description": "Inferred fact.", "mermaid": "graph LR\n  A[\"Machine Learning\"] -->|is_a| B[\"AI\"]\n  B[\"AI\"] -->|is_a| C[\"Technology\"]\n  A -.->|inferred is_a| C\n  style A fill:#aaddff,stroke:#000000\n  style B fill:#aaddff,stroke:#000000\n  style C fill:#ffaadd,stroke:#000000"}
                    ]},
                    {"type": "narrative", "content": "By defining the ontology, the chaotic vortex settles into an ordered lattice of interconnected glowing nodes."},
                    {"type": "concept", "content": "SPARQL can be used to query this structured RDF graph data."},
                    {"type": "detail", "content": "SELECT ?tech WHERE { ?tech is_a Technology }"},
                    {"type": "quiz", "question": "In a knowledge graph triple (Subject, Predicate, Object), what does the Predicate represent?", "options": ["An entity", "The relationship between two entities", "A constraint on the graph size"], "answer": 1}
                ]
            }
        ]
    },
    "case_09": {
        "title": "Case 09: The Logic Engine (Propositional & FOL)",
        "modules": [
            {
                "id": "c9_ep1",
                "title": "Episode 1: The Foundations of Reason",
                "blocks": [
                    {"type": "narrative", "content": "You reach the core terminal. The system demands logical proof before granting access. It presents a series of true/false statements."},
                    {"type": "concept", "content": "Propositional Logic uses simple symbols to represent propositions (statements that are true or false). Connectives like AND, OR, NOT, and IMPLIES combine them."},
                    {"type": "visual_stepper", "title": "Propositional Logic Evaluation", "steps": [
                        {"description": "P = True, Q = False", "mermaid": "graph TD\n  P[\"P (True)\"]\n  Q[\"Q (False)\"]\n  style P fill:#00ff00,stroke:#000\n  style Q fill:#ff0000,stroke:#000"},
                        {"description": "P AND Q", "mermaid": "graph TD\n  P[\"P (True)\"] --> AND[\"AND\"]\n  Q[\"Q (False)\"] --> AND\n  AND --> Res[\"False\"]\n  style P fill:#00ff00,stroke:#000\n  style Q fill:#ff0000,stroke:#000\n  style Res fill:#ff0000,stroke:#000"}
                    ]},
                    {"type": "narrative", "content": "Propositional logic is too rigid. You can't easily express 'All humans are mortal' without writing a rule for every human."},
                    {"type": "concept", "content": "First-Order Logic (FOL) introduces objects, relations, and quantifiers (Universal and Existential)."},
                    {"type": "detail", "content": "Universal (∀x): For all x. Existential (∃x): There exists an x."},
                    {"type": "visual_stepper", "title": "FOL Representation", "steps": [
                        {"description": "∀x (Human(x) => Mortal(x))", "mermaid": "graph TD\n  A[\"Human(Socrates)\"] --> B[\"Mortal(Socrates)\"]\n  style A fill:#aaccff,stroke:#000\n  style B fill:#aaccff,stroke:#000"}
                    ]},
                    {"type": "narrative", "content": "The terminal parses your FOL statements and accepts the proof."},
                    {"type": "quiz", "question": "Which quantifier asserts that a property holds for at least one object in the domain?", "options": ["Universal quantifier", "Existential quantifier", "Propositional quantifier"], "answer": 1},
                    {"type": "concept", "content": "Resolution is a rule of inference leading to a refutation theorem-proving technique for sentences in propositional logic and FOL."}
                ]
            }
        ]
    },
    "case_10": {
        "title": "Case 10: The Machine That Could Reason (Situation Calculus)",
        "modules": [
            {
                "id": "c10_ep1",
                "title": "Episode 1: State and Change",
                "blocks": [
                    {"type": "narrative", "content": "The AI needs to interact with the physical world. It must understand how actions change the state of the environment over time."},
                    {"type": "concept", "content": "Situation Calculus is a logic formalism designed for representing and reasoning about dynamical domains."},
                    {"type": "detail", "content": "The world is formalized in terms of situations (states), actions, and fluents (properties that change over time, like Location(robot, S))."},
                    {"type": "visual_stepper", "title": "State Transition in Situation Calculus", "steps": [
                        {"description": "Initial Situation S0", "mermaid": "graph LR\n  S0[\"S0: At(Robot, RoomA)\"]\n  style S0 fill:#ffffaa,stroke:#000"},
                        {"description": "Applying action Move(RoomB)", "mermaid": "graph LR\n  S0[\"S0: At(Robot, RoomA)\"] -->|Move(RoomB)| S1[\"S1: At(Robot, RoomB)\"]\n  style S0 fill:#ffffaa,stroke:#000\n  style S1 fill:#aaffaa,stroke:#000"}
                    ]},
                    {"type": "concept", "content": "The Frame Problem: How do we compactly represent the things that DO NOT change when an action is performed?"},
                    {"type": "narrative", "content": "If the robot moves to Room B, the color of the walls in Room A doesn't change. Writing axioms for every non-effect is tedious."},
                    {"type": "concept", "content": "Successor State Axioms provide an elegant solution by defining exactly what makes a fluent true in the next situation: An action made it true, OR it was already true and the action didn't make it false."},
                    {"type": "visual_stepper", "title": "Successor State Axiom Flow", "steps": [
                        {"description": "Checking truth in S(a, s)", "mermaid": "graph TD\n  A[\"Fluent F true in s?\"] --> B[\"Action 'a' makes F false?\"]\n  style A fill:#dddddd,stroke:#000"},
                        {"description": "Resolution", "mermaid": "graph TD\n  A[\"Fluent F true in s?\"] --> B[\"Action 'a' makes F false?\"]\n  B -->|No| C[\"F remains true in S(a, s)\"]\n  style C fill:#00ff00,stroke:#000"}
                    ]},
                    {"type": "narrative", "content": "The machine successfully models its environment and begins moving safely."},
                    {"type": "quiz", "question": "What problem deals with representing properties that remain unchanged after an action?", "options": ["The Qualification Problem", "The Ramification Problem", "The Frame Problem"], "answer": 2}
                ]
            }
        ]
    },
    "case_11": {
        "title": "Case 11: The Planner (Action Representation, Planning Graphs)",
        "modules": [
            {
                "id": "c11_ep1",
                "title": "Episode 1: Striking a Plan",
                "blocks": [
                    {"type": "narrative", "content": "To escape the facility, the AI must devise a complex sequence of actions, considering preconditions and effects."},
                    {"type": "concept", "content": "Automated Planning is the realization of strategies or action sequences for execution by intelligent agents."},
                    {"type": "detail", "content": "STRIPS (Stanford Research Institute Problem Solver) represents actions with Preconditions (what must be true before) and Effects (what becomes true/false after)."},
                    {"type": "visual_stepper", "title": "STRIPS Action Representation", "steps": [
                        {"description": "Action: OpenDoor", "mermaid": "graph TD\n  Pre[\"Precond: HasKey(Agent)\"]\n  style Pre fill:#aaddff,stroke:#000"},
                        {"description": "Applying Action", "mermaid": "graph TD\n  Pre[\"Precond: HasKey(Agent)\"] --> Act[\"Action: OpenDoor\"]\n  Act --> Eff[\"Effect: DoorOpen(True)\"]\n  style Pre fill:#aaddff,stroke:#000\n  style Act fill:#ffffaa,stroke:#000\n  style Eff fill:#aaffaa,stroke:#000"}
                    ]},
                    {"type": "concept", "content": "Planning Graphs are directed leveled graphs used to estimate the cost of reaching a goal and can extract plans efficiently (e.g., GraphPlan algorithm)."},
                    {"type": "narrative", "content": "The graph alternates between state levels and action levels."},
                    {"type": "visual_stepper", "title": "Planning Graph Construction", "steps": [
                        {"description": "Level S0 (Initial State)", "mermaid": "graph LR\n  S0[\"S0: ~DoorOpen, HasKey\"]\n  style S0 fill:#eeeeee,stroke:#000"},
                        {"description": "Level A0 (Possible Actions)", "mermaid": "graph LR\n  S0[\"S0: ~DoorOpen, HasKey\"] --> A0[\"A0: OpenDoor, NoOp\"]\n  style S0 fill:#eeeeee,stroke:#000\n  style A0 fill:#ffffaa,stroke:#000"},
                        {"description": "Level S1 (Next State)", "mermaid": "graph LR\n  A0[\"A0: OpenDoor, NoOp\"] --> S1[\"S1: DoorOpen, HasKey\"]\n  style A0 fill:#ffffaa,stroke:#000\n  style S1 fill:#eeeeee,stroke:#000"}
                    ]},
                    {"type": "concept", "content": "Mutex (Mutually Exclusive) links in the graph indicate actions or states that cannot occur simultaneously (e.g., an action deletes a precondition of another)."},
                    {"type": "narrative", "content": "Through the planning graph, the AI finds the shortest path to freedom."},
                    {"type": "quiz", "question": "In a Planning Graph, what does a Mutex link between two actions signify?", "options": ["They must be executed sequentially in any valid plan", "They can be executed at the same time", "They cannot occur together at the same level"], "answer": 2}
                ]
            }
        ]
    }
}
