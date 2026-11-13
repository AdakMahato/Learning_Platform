CONTENT_07_11 = {
    "7": {
        "title": "Case 07: Constraint Satisfaction Problems (CSP)",
        "modules": [
            {
                "title": "Module 1: Introduction to CSP",
                "episodes": [
                    {"type": "markdown", "content": "A Constraint Satisfaction Problem (CSP) involves finding assignments for variables that satisfy given constraints."},
                    {"type": "concept", "title": "Variables and Domains", "content": "Each variable has a domain of possible values."},
                    {"type": "visual", "content": "graph TD\n  A[\"Variable\"] --> B[\"Domain\"]\n  style A fill:#10b981,stroke:#333,stroke-width:2px"},
                    {"type": "interactive", "question": "What is a constraint?", "options": ["Rule restricting values", "A type of variable"], "correct": 0},
                    {"type": "markdown", "content": "Constraints can be unary, binary, or higher-order."},
                    {"type": "concept", "title": "Unary Constraints", "content": "A unary constraint restricts the value of a single variable."},
                    {"type": "visual_stepper", "steps": ["graph TD\n  A[\"V1\"]", "graph TD\n  A[\"V1!=1\"]"]},
                    {"type": "code_lab", "language": "python", "code": "def unary_constraint(v): return v > 0"},
                    {"type": "markdown", "content": "Binary constraints involve two variables."},
                    {"type": "concept", "title": "Binary Constraints", "content": "An example is X != Y in map coloring."}
                ]
            },
            {
                "title": "Module 2: Backtracking Search",
                "episodes": [
                    {"type": "markdown", "content": "Backtracking is a depth-first search for CSPs."},
                    {"type": "concept", "title": "Search Space", "content": "The search space is formed by assigning values to variables one by one."},
                    {"type": "visual", "content": "graph TD\n  A[\"Start\"] --> B[\"Assign V1\"]\n  style A fill:#10b981,stroke:#333,stroke-width:2px"},
                    {"type": "interactive", "question": "When does backtracking backtrack?", "options": ["On constraint violation", "When all assigned"], "correct": 0},
                    {"type": "markdown", "content": "It checks constraints at each step."},
                    {"type": "concept", "title": "Failing Early", "content": "If a constraint is violated, the current branch is abandoned."},
                    {"type": "visual_stepper", "steps": ["graph TD\n  A[\"V1=1\"]", "graph TD\n  A[\"V1=1\"] -.->|Fail| B[\"V2=1\"]"]},
                    {"type": "code_lab", "language": "python", "code": "def backtrack(assignment):\n  pass"},
                    {"type": "markdown", "content": "Backtracking is more efficient than generate-and-test."},
                    {"type": "concept", "title": "Efficiency", "content": "It eliminates large portions of the search space."}
                ]
            },
            {
                "title": "Module 3: Heuristics in CSP",
                "episodes": [
                    {"type": "markdown", "content": "Heuristics improve the efficiency of backtracking."},
                    {"type": "concept", "title": "Variable Ordering", "content": "Which variable should be assigned next?"},
                    {"type": "visual", "content": "graph TD\n  A[\"V1 (3 values)\"] --> B[\"V2 (1 value)\"]\n  style A fill:#3b82f6,stroke:#333,stroke-width:2px"},
                    {"type": "interactive", "question": "What is MRV?", "options": ["Minimum Remaining Values", "Most Restrictive Value"], "correct": 0},
                    {"type": "markdown", "content": "MRV chooses the variable with the fewest legal values left."},
                    {"type": "concept", "title": "Degree Heuristic", "content": "Used as a tie-breaker, it selects the variable involved in most constraints."},
                    {"type": "visual_stepper", "steps": ["graph TD\n  A[\"V1\"]", "graph TD\n  A[\"MRV chooses V2\"]"]},
                    {"type": "code_lab", "language": "python", "code": "def mrv(variables): return min(variables, key=lambda v: len(v.domain))"},
                    {"type": "markdown", "content": "Value ordering determines which value to try first."},
                    {"type": "concept", "title": "Least Constraining Value", "content": "Prefers the value that rules out the fewest choices for neighboring variables."}
                ]
            },
            {
                "title": "Module 4: Constraint Propagation",
                "episodes": [
                    {"type": "markdown", "content": "Constraint propagation reduces the domains of variables before search."},
                    {"type": "concept", "title": "Forward Checking", "content": "Whenever a variable is assigned, remove conflicting values from unassigned variables."},
                    {"type": "visual", "content": "graph TD\n  A[\"V1=Red\"] --> B[\"V2 removes Red\"]\n  style A fill:#f59e0b,stroke:#333,stroke-width:2px"},
                    {"type": "interactive", "question": "What does arc consistency do?", "options": ["Makes all arcs consistent", "Finds the solution immediately"], "correct": 0},
                    {"type": "markdown", "content": "AC-3 is a popular algorithm for arc consistency."},
                    {"type": "concept", "title": "Arc Consistency", "content": "An arc X -> Y is consistent if for every value in X, there is an allowed value in Y."},
                    {"type": "visual_stepper", "steps": ["graph TD\n  A[\"Check X->Y\"]", "graph TD\n  A[\"Remove values from X\"]"]},
                    {"type": "code_lab", "language": "python", "code": "def ac3(csp): pass"},
                    {"type": "markdown", "content": "Propagation can sometimes solve the CSP without search."},
                    {"type": "concept", "title": "Trade-off", "content": "More propagation means less search, but propagation takes time."}
                ]
            }
        ]
    },
    "8": {
        "title": "Case 08: Knowledge Graphs",
        "modules": [
            {
                "title": "Module 1: Introduction to Knowledge Graphs",
                "episodes": [
                    {"type": "markdown", "content": "A Knowledge Graph represents entities and their relationships."},
                    {"type": "concept", "title": "Entities", "content": "Entities are the nodes in the graph, representing real-world objects."},
                    {"type": "visual", "content": "graph TD\n  A[\"Entity: Person\"] --> B[\"Entity: City\"]\n  style A fill:#10b981,stroke:#333,stroke-width:2px"},
                    {"type": "interactive", "question": "What forms the edges in a KG?", "options": ["Relationships", "Attributes"], "correct": 0},
                    {"type": "markdown", "content": "Relationships are directed edges connecting entities."},
                    {"type": "concept", "title": "Triples", "content": "Data is stored as Subject-Predicate-Object triples."},
                    {"type": "visual_stepper", "steps": ["graph LR\n  A[\"Subject\"]", "graph LR\n  A[\"Subject\"] -->|Predicate| B[\"Object\"]"]},
                    {"type": "code_lab", "language": "python", "code": "triple = ('Alice', 'knows', 'Bob')"},
                    {"type": "markdown", "content": "KGs allow semantic queries and reasoning."},
                    {"type": "concept", "title": "Ontology", "content": "An ontology defines the schema and vocabulary of the KG."}
                ]
            },
            {
                "title": "Module 2: Building Knowledge Graphs",
                "episodes": [
                    {"type": "markdown", "content": "Building a KG involves data extraction and integration."},
                    {"type": "concept", "title": "Information Extraction", "content": "NLP techniques extract entities and relations from text."},
                    {"type": "visual", "content": "graph TD\n  A[\"Text\"] --> B[\"NER\"]\n  style A fill:#3b82f6,stroke:#333,stroke-width:2px"},
                    {"type": "interactive", "question": "What is Named Entity Recognition (NER)?", "options": ["Identifying entities in text", "Creating graphs"], "correct": 0},
                    {"type": "markdown", "content": "Relation extraction links entities found in the text."},
                    {"type": "concept", "title": "Entity Resolution", "content": "Disambiguating multiple mentions of the same entity."},
                    {"type": "visual_stepper", "steps": ["graph TD\n  A[\"J.F.K\"]", "graph TD\n  A[\"J.F.K\"] --> B[\"John F. Kennedy\"]"]},
                    {"type": "code_lab", "language": "python", "code": "def extract_entities(text): return []"},
                    {"type": "markdown", "content": "Data fusion resolves conflicting information from different sources."},
                    {"type": "concept", "title": "Schema Mapping", "content": "Aligning data from various sources to a common ontology."}
                ]
            },
            {
                "title": "Module 3: Querying Knowledge Graphs",
                "episodes": [
                    {"type": "markdown", "content": "SPARQL is the standard query language for RDF graphs."},
                    {"type": "concept", "title": "Graph Patterns", "content": "Queries consist of graph patterns to match against the KG."},
                    {"type": "visual", "content": "graph TD\n  A[\"?person\"] -->|knows| B[\"?friend\"]\n  style A fill:#f59e0b,stroke:#333,stroke-width:2px"},
                    {"type": "interactive", "question": "What does a SPARQL query match?", "options": ["Graph Patterns", "Tables"], "correct": 0},
                    {"type": "markdown", "content": "Variables in SPARQL are denoted by a question mark."},
                    {"type": "concept", "title": "SELECT Clause", "content": "Specifies which variables to return in the result set."},
                    {"type": "visual_stepper", "steps": ["graph TD\n  A[\"SELECT ?name\"]", "graph TD\n  A[\"WHERE { ?s name ?name }\"]"]},
                    {"type": "code_lab", "language": "python", "code": "query = 'SELECT ?s WHERE { ?s rdf:type Person }'"},
                    {"type": "markdown", "content": "Cypher is another popular query language, used by Neo4j."},
                    {"type": "concept", "title": "Path Traversal", "content": "Cypher excels at expressing complex graph traversals."}
                ]
            },
            {
                "title": "Module 4: Reasoning on Knowledge Graphs",
                "episodes": [
                    {"type": "markdown", "content": "Reasoning infers new knowledge from existing facts."},
                    {"type": "concept", "title": "Rule-based Reasoning", "content": "Applying logical rules like 'If X is Ys parent, X is older than Y'."},
                    {"type": "visual", "content": "graph TD\n  A[\"Parent\"] -->|Implies| B[\"Older\"]\n  style A fill:#ef4444,stroke:#333,stroke-width:2px"},
                    {"type": "interactive", "question": "What is inferred knowledge?", "options": ["Facts derived from rules", "Raw data"], "correct": 0},
                    {"type": "markdown", "content": "Transitive relations allow traversing hierarchies."},
                    {"type": "concept", "title": "Subclass Inferencing", "content": "If a Dog is a Mammal, and a Mammal is an Animal, a Dog is an Animal."},
                    {"type": "visual_stepper", "steps": ["graph TD\n  A[\"Dog\"] -->|is_a| B[\"Mammal\"]", "graph TD\n  B[\"Mammal\"] -->|is_a| C[\"Animal\"]"]},
                    {"type": "code_lab", "language": "python", "code": "def infer_transitive(a, rel, b): pass"},
                    {"type": "markdown", "content": "Knowledge Graph Embeddings represent entities as vectors."},
                    {"type": "concept", "title": "Link Prediction", "content": "Predicting missing edges in the graph using embeddings."}
                ]
            }
        ]
    },
    "9": {
        "title": "Case 09: Logic Engine & First Order Logic",
        "modules": [
            {
                "title": "Module 1: Propositional Logic",
                "episodes": [
                    {"type": "markdown", "content": "Propositional logic deals with statements that are true or false."},
                    {"type": "concept", "title": "Propositions", "content": "A proposition is a declarative sentence, e.g., 'It is raining'."},
                    {"type": "visual", "content": "graph TD\n  A[\"P: Raining\"] --> B[\"True/False\"]\n  style A fill:#10b981,stroke:#333,stroke-width:2px"},
                    {"type": "interactive", "question": "Which is a logical connective?", "options": ["AND", "NOUN"], "correct": 0},
                    {"type": "markdown", "content": "Connectives join propositions: AND, OR, NOT, IMPLIES."},
                    {"type": "concept", "title": "Truth Tables", "content": "Truth tables define the semantics of connectives."},
                    {"type": "visual_stepper", "steps": ["graph TD\n  A[\"P, Q\"]", "graph TD\n  A[\"P AND Q\"]"]},
                    {"type": "code_lab", "language": "python", "code": "def logical_and(p, q): return p and q"},
                    {"type": "markdown", "content": "A sentence is satisfiable if it can be true."},
                    {"type": "concept", "title": "Tautology", "content": "A tautology is true under all possible interpretations."}
                ]
            },
            {
                "title": "Module 2: First Order Logic (FOL)",
                "episodes": [
                    {"type": "markdown", "content": "FOL extends propositional logic with objects and quantifiers."},
                    {"type": "concept", "title": "Predicates", "content": "Predicates express properties or relations between objects."},
                    {"type": "visual", "content": "graph TD\n  A[\"Loves(x, y)\"] --> B[\"Relation\"]\n  style A fill:#3b82f6,stroke:#333,stroke-width:2px"},
                    {"type": "interactive", "question": "What is a universal quantifier?", "options": ["For all", "There exists"], "correct": 0},
                    {"type": "markdown", "content": "The Universal Quantifier (∀) means 'for all'."},
                    {"type": "concept", "title": "Existential Quantifier", "content": "The Existential Quantifier (∃) means 'there exists'."},
                    {"type": "visual_stepper", "steps": ["graph TD\n  A[\"∀x\"]", "graph TD\n  A[\"∀x Loves(x, y)\"]"]},
                    {"type": "code_lab", "language": "python", "code": "def for_all(domain, predicate): return all(predicate(x) for x in domain)"},
                    {"type": "markdown", "content": "Variables in FOL represent generic objects."},
                    {"type": "concept", "title": "Constants and Functions", "content": "Constants denote specific objects. Functions map objects to objects."}
                ]
            },
            {
                "title": "Module 3: Inference in FOL",
                "episodes": [
                    {"type": "markdown", "content": "Inference derives new sentences from a knowledge base."},
                    {"type": "concept", "title": "Modus Ponens", "content": "If P implies Q, and P is true, then Q is true."},
                    {"type": "visual", "content": "graph TD\n  A[\"P -> Q\"] --> B[\"P => Q\"]\n  style A fill:#f59e0b,stroke:#333,stroke-width:2px"},
                    {"type": "interactive", "question": "What is Unification?", "options": ["Matching terms", "Splitting rules"], "correct": 0},
                    {"type": "markdown", "content": "Unification finds substitutions to make expressions identical."},
                    {"type": "concept", "title": "Substitution", "content": "Replacing variables with terms, e.g., {x/John}."},
                    {"type": "visual_stepper", "steps": ["graph TD\n  A[\"P(x)\"]", "graph TD\n  A[\"P(John)\"]"]},
                    {"type": "code_lab", "language": "python", "code": "def unify(var, val): pass"},
                    {"type": "markdown", "content": "Forward chaining applies rules to infer new facts."},
                    {"type": "concept", "title": "Backward Chaining", "content": "Starts from a goal and works backward to find supporting facts."}
                ]
            },
            {
                "title": "Module 4: Resolution and Theorem Proving",
                "episodes": [
                    {"type": "markdown", "content": "Resolution is a sound and complete inference rule."},
                    {"type": "concept", "title": "Conjunctive Normal Form", "content": "Sentences must be converted to CNF for resolution."},
                    {"type": "visual", "content": "graph TD\n  A[\"A OR B\"] --> B[\"CNF\"]\n  style A fill:#ef4444,stroke:#333,stroke-width:2px"},
                    {"type": "interactive", "question": "What does resolution produce?", "options": ["A resolvent", "A tautology"], "correct": 0},
                    {"type": "markdown", "content": "A resolvent is formed by combining two clauses and resolving a complementary literal."},
                    {"type": "concept", "title": "Proof by Contradiction", "content": "To prove P, assume not P and derive the empty clause."},
                    {"type": "visual_stepper", "steps": ["graph TD\n  A[\"Assume ~P\"]", "graph TD\n  A[\"Empty Clause\"]"]},
                    {"type": "code_lab", "language": "python", "code": "def resolve(ci, cj): pass"},
                    {"type": "markdown", "content": "The empty clause represents a contradiction."},
                    {"type": "concept", "title": "Completeness", "content": "If a sentence is entailed, resolution will eventually derive a contradiction."}
                ]
            }
        ]
    },
    "10": {
        "title": "Case 10: Situation Calculus",
        "modules": [
            {
                "title": "Module 1: Modeling Change",
                "episodes": [
                    {"type": "markdown", "content": "Situation calculus models dynamic worlds using logic."},
                    {"type": "concept", "title": "Situations", "content": "A situation is a snapshot of the world at a particular time."},
                    {"type": "visual", "content": "graph TD\n  A[\"S0 (Initial)\"] --> B[\"S1\"]\n  style A fill:#10b981,stroke:#333,stroke-width:2px"},
                    {"type": "interactive", "question": "What connects situations?", "options": ["Actions", "Variables"], "correct": 0},
                    {"type": "markdown", "content": "Actions transition the world from one situation to the next."},
                    {"type": "concept", "title": "Result Function", "content": "Result(a, s) is the situation resulting from doing action a in situation s."},
                    {"type": "visual_stepper", "steps": ["graph TD\n  A[\"S0\"]", "graph TD\n  A[\"S0\"] -->|Action A| B[\"Result(A, S0)\"]"]},
                    {"type": "code_lab", "language": "python", "code": "def result(action, state): return new_state"},
                    {"type": "markdown", "content": "Fluents are properties that change over time."},
                    {"type": "concept", "title": "Fluent Example", "content": "At(Robot, Room1, S0) means the robot is in Room1 in situation S0."}
                ]
            },
            {
                "title": "Module 2: Axioms in Situation Calculus",
                "episodes": [
                    {"type": "markdown", "content": "Axioms describe the physics of the modeled world."},
                    {"type": "concept", "title": "Possibility Axioms", "content": "Preconditions that must hold for an action to be possible."},
                    {"type": "visual", "content": "graph TD\n  A[\"Precondition\"] --> B[\"Poss(A, S)\"]\n  style A fill:#3b82f6,stroke:#333,stroke-width:2px"},
                    {"type": "interactive", "question": "What is an effect axiom?", "options": ["Describes how actions change fluents", "Initial state"], "correct": 0},
                    {"type": "markdown", "content": "Effect axioms specify the changes caused by an action."},
                    {"type": "concept", "title": "Positive Effects", "content": "Fluents made true by the action."},
                    {"type": "visual_stepper", "steps": ["graph TD\n  A[\"Action\"]", "graph TD\n  A[\"Action\"] --> B[\"New Fluent True\"]"]},
                    {"type": "code_lab", "language": "python", "code": "def apply_effect(action): pass"},
                    {"type": "markdown", "content": "Negative effects specify fluents made false."},
                    {"type": "concept", "title": "The Frame Problem", "content": "How to succinctly represent what DOES NOT change."}
                ]
            },
            {
                "title": "Module 3: Solving the Frame Problem",
                "episodes": [
                    {"type": "markdown", "content": "The frame problem is a major challenge in AI."},
                    {"type": "concept", "title": "Frame Axioms", "content": "Explicitly stating that an action does not affect a specific fluent."},
                    {"type": "visual", "content": "graph TD\n  A[\"Action Move\"] --> B[\"Color Unchanged\"]\n  style A fill:#f59e0b,stroke:#333,stroke-width:2px"},
                    {"type": "interactive", "question": "Why are frame axioms problematic?", "options": ["Too many of them", "They are false"], "correct": 0},
                    {"type": "markdown", "content": "Writing frame axioms for everything is intractable (O(A*F))."},
                    {"type": "concept", "title": "Successor State Axioms", "content": "A solution that combines effect and frame axioms for each fluent."},
                    {"type": "visual_stepper", "steps": ["graph TD\n  A[\"Fluent F in S+1\"]", "graph TD\n  A[\"True if made true OR was true and not made false\"]"]},
                    {"type": "code_lab", "language": "python", "code": "def successor_state(fluent, action, state): pass"},
                    {"type": "markdown", "content": "This requires O(F) axioms instead of O(A*F)."},
                    {"type": "concept", "title": "Assumption", "content": "Requires the closed-world assumption for action effects."}
                ]
            },
            {
                "title": "Module 4: Planning with Situation Calculus",
                "episodes": [
                    {"type": "markdown", "content": "Planning is finding a sequence of actions to reach a goal."},
                    {"type": "concept", "title": "Goal State", "content": "A formula describing the desired properties of a situation."},
                    {"type": "visual", "content": "graph TD\n  A[\"Start\"] --> B[\"Goal Situation S_G\"]\n  style A fill:#ef4444,stroke:#333,stroke-width:2px"},
                    {"type": "interactive", "question": "How is planning treated in logic?", "options": ["Theorem proving", "Data entry"], "correct": 0},
                    {"type": "markdown", "content": "Planning can be formulated as proving a theorem: ∃s Goal(s)."},
                    {"type": "concept", "title": "Extracting the Plan", "content": "The proof yields a binding for 's' like Result(A2, Result(A1, S0))."},
                    {"type": "visual_stepper", "steps": ["graph TD\n  A[\"Prove ∃s\"]", "graph TD\n  A[\"s = Result(seq, S0)\"]"]},
                    {"type": "code_lab", "language": "python", "code": "def extract_plan(proof): return proof.binding('s')"},
                    {"type": "markdown", "content": "General theorem proving for planning is often inefficient."},
                    {"type": "concept", "title": "Specialized Planners", "content": "Led to the development of specialized representations like STRIPS."}
                ]
            }
        ]
    },
    "11": {
        "title": "Case 11: STRIPS Planning",
        "modules": [
            {
                "title": "Module 1: The STRIPS Representation",
                "episodes": [
                    {"type": "markdown", "content": "STRIPS simplifies action representation for efficient planning."},
                    {"type": "concept", "title": "States", "content": "States are conjunctions of positive, ground, function-free literals."},
                    {"type": "visual", "content": "graph TD\n  A[\"At(Robot, Room1)\"] --> B[\"State\"]\n  style A fill:#10b981,stroke:#333,stroke-width:2px"},
                    {"type": "interactive", "question": "What does STRIPS assume?", "options": ["Closed World Assumption", "Infinite states"], "correct": 0},
                    {"type": "markdown", "content": "Anything not listed in the state is assumed false."},
                    {"type": "concept", "title": "Actions", "content": "Defined by Preconditions, Add list, and Delete list."},
                    {"type": "visual_stepper", "steps": ["graph TD\n  A[\"Action schema\"]", "graph TD\n  A[\"Precond\"] --> B[\"Add/Delete Lists\"]"]},
                    {"type": "code_lab", "language": "python", "code": "class Action:\n  def __init__(self): self.pre = []"},
                    {"type": "markdown", "content": "The Add list contains new facts; the Delete list removes old ones."},
                    {"type": "concept", "title": "Applying Actions", "content": "New State = (Old State - Delete) U Add."}
                ]
            },
            {
                "title": "Module 2: Forward State-Space Search",
                "episodes": [
                    {"type": "markdown", "content": "Forward search starts at the initial state and applies actions."},
                    {"type": "concept", "title": "Applicability", "content": "An action is applicable if its preconditions are in the current state."},
                    {"type": "visual", "content": "graph TD\n  A[\"State S\"] -->|Applicable Action| B[\"State S'\"]\n  style A fill:#3b82f6,stroke:#333,stroke-width:2px"},
                    {"type": "interactive", "question": "What is the goal test?", "options": ["Check if goal literals are in state", "Check if time is up"], "correct": 0},
                    {"type": "markdown", "content": "The search stops when the goal state is reached."},
                    {"type": "concept", "title": "Branching Factor", "content": "Forward search can have a massive branching factor."},
                    {"type": "visual_stepper", "steps": ["graph TD\n  A[\"S0\"]", "graph TD\n  A[\"S0\"] --> B[\"Huge many children\"]"]},
                    {"type": "code_lab", "language": "python", "code": "def is_applicable(action, state): return all(p in state for p in action.pre)"},
                    {"type": "markdown", "content": "Many applicable actions might be irrelevant to the goal."},
                    {"type": "concept", "title": "Need for Heuristics", "content": "Heuristics are essential to guide forward search effectively."}
                ]
            },
            {
                "title": "Module 3: Backward Search and Heuristics",
                "episodes": [
                    {"type": "markdown", "content": "Backward search starts at the goal and regresses actions."},
                    {"type": "concept", "title": "Relevant Actions", "content": "An action is relevant if it achieves one of the goal literals."},
                    {"type": "visual", "content": "graph TD\n  A[\"Goal\"] -->|Regress Action| B[\"Subgoal\"]\n  style A fill:#f59e0b,stroke:#333,stroke-width:2px"},
                    {"type": "interactive", "question": "What is Regression?", "options": ["Computing subgoals", "Forgetting"], "correct": 0},
                    {"type": "markdown", "content": "Regression calculates the preconditions needed to reach the goal."},
                    {"type": "concept", "title": "Planning Graphs", "content": "A structure to extract powerful heuristics for planning."},
                    {"type": "visual_stepper", "steps": ["graph TD\n  A[\"State level 0\"]", "graph TD\n  A[\"State level 0\"] --> B[\"Action level 0\"]"]},
                    {"type": "code_lab", "language": "python", "code": "def regress(goal, action): pass"},
                    {"type": "markdown", "content": "Planning graphs estimate the cost to achieve a goal literal."},
                    {"type": "concept", "title": "Mutex Relations", "content": "Tracks actions and literals that cannot occur simultaneously."}
                ]
            },
            {
                "title": "Module 4: Partial-Order Planning",
                "episodes": [
                    {"type": "markdown", "content": "Partial-Order Planning (POP) searches in the space of plans, not states."},
                    {"type": "concept", "title": "Plan Structure", "content": "A plan is a set of steps, ordering constraints, and causal links."},
                    {"type": "visual", "content": "graph TD\n  A[\"Step A\"] -.->|Before| B[\"Step B\"]\n  style A fill:#ef4444,stroke:#333,stroke-width:2px"},
                    {"type": "interactive", "question": "What does a causal link record?", "options": ["Step A achieves a precondition for Step B", "Time limit"], "correct": 0},
                    {"type": "markdown", "content": "Causal links ensure that preconditions are met and protected."},
                    {"type": "concept", "title": "Threats", "content": "A threat occurs when a step might delete a protected precondition."},
                    {"type": "visual_stepper", "steps": ["graph TD\n  A[\"Link A->B\"]", "graph TD\n  A[\"Link A->B\"] -.->|Threat C| B[\"Link A->B\"]"]},
                    {"type": "code_lab", "language": "python", "code": "def resolve_threat(plan, threat): pass"},
                    {"type": "markdown", "content": "Threats are resolved by adding ordering constraints (promotion/demotion)."},
                    {"type": "concept", "title": "Least Commitment", "content": "POP only orders steps when necessary to resolve threats."}
                ]
            }
        ]
    }
}
