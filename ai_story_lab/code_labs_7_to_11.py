# High-Quality Code Labs for Cases 7 to 11
# Complete Executable Python Laboratories with Starter Code, Solution Code, Test Cases, and In-Depth Explanations

CODE_LABS_7_TO_11 = {
    # Case 07: Constraint Satisfaction Problems
    ("7", 0): {
        "title": "CSP Map Coloring Formulation Lab",
        "starter_code": """# Lab: Formulate Map Coloring as a CSP
# Given 3 regions (WA, NT, SA) and 3 colors (Red, Green, Blue)
# where WA borders NT and SA, and NT borders SA.

variables = ['WA', 'NT', 'SA']
domains = {v: ['Red', 'Green', 'Blue'] for v in variables}
neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA'],
    'SA': ['WA', 'NT']
}

def is_consistent(var, color, assignment):
    \"\"\"Return True if assigning 'color' to 'var' satisfies all binary constraints.\"\"\"
    # TODO: Check if any assigned neighbor already has this color
    for neighbor in neighbors[var]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

# Test an assignment
assignment = {'WA': 'Red', 'NT': 'Green'}
print("Can SA be Red?", is_consistent('SA', 'Red', assignment))
print("Can SA be Blue?", is_consistent('SA', 'Blue', assignment))
""",
        "solution_code": """# Complete Solution: CSP Map Coloring Formulation
variables = ['WA', 'NT', 'SA']
domains = {v: ['Red', 'Green', 'Blue'] for v in variables}
neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA'],
    'SA': ['WA', 'NT']
}

def is_consistent(var, color, assignment):
    for neighbor in neighbors[var]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

assignment = {'WA': 'Red', 'NT': 'Green'}
print("Can SA be Red?", is_consistent('SA', 'Red', assignment))
print("Can SA be Blue?", is_consistent('SA', 'Blue', assignment))
""",
        "expected_output": "Can SA be Red? False\nCan SA be Blue? True\n",
        "explanation": """### 💡 Code Mechanics & Engineering Insights
**How it Works:**
A Constraint Satisfaction Problem (CSP) is defined by three components $(X, D, C)$:
1. **Variables ($X$):** The entities requiring values (`['WA', 'NT', 'SA']`).
2. **Domains ($D$):** The allowable values for each variable (`{'Red', 'Green', 'Blue'}`).
3. **Constraints ($C$):** Explicit binary restrictions ($WA \neq NT$, $WA \neq SA$, $NT \neq SA$).
The `is_consistent` function checks whether an incremental assignment violates any existing binary constraints in $O(d)$ time where $d$ is the vertex degree.

**Alternative Paradigms:**
- *Integer Linear Programming (ILP):* Encodes constraints as linear inequalities ($x_{i, c} + x_{j, c} \le 1$). Excellent for continuous/mixed constraints.
- *SAT Solvers (Boolean Satisfiability):* Converts constraints to Conjunctive Normal Form (CNF) and executes CDCL (Conflict-Driven Clause Learning), handling millions of variables."""
    },
    ("7", 1): {
        "title": "Backtracking Search Lab",
        "starter_code": """# Lab: Recursive Backtracking Search for CSP
variables = ['A', 'B', 'C']
domains = {v: ['1', '2'] for v in variables}
# Constraint: A != B and B != C
neighbors = {'A': ['B'], 'B': ['A', 'C'], 'C': ['B']}

def backtrack(assignment):
    if len(assignment) == len(variables):
        return assignment
    
    # Pick next unassigned variable
    var = [v for v in variables if v not in assignment][0]
    
    for val in domains[var]:
        # Check consistency
        conflict = False
        for n in neighbors[var]:
            if n in assignment and assignment[n] == val:
                conflict = True
                break
        if not conflict:
            assignment[var] = val
            result = backtrack(assignment)
            if result is not None:
                return result
            del assignment[var] # Backtrack!
            
    return None

solution = backtrack({})
print("Found Valid Assignment:", solution)
""",
        "solution_code": """# Complete Solution: Recursive Backtracking Search
variables = ['A', 'B', 'C']
domains = {v: ['1', '2'] for v in variables}
neighbors = {'A': ['B'], 'B': ['A', 'C'], 'C': ['B']}

def backtrack(assignment):
    if len(assignment) == len(variables):
        return assignment
    var = [v for v in variables if v not in assignment][0]
    for val in domains[var]:
        conflict = False
        for n in neighbors[var]:
            if n in assignment and assignment[n] == val:
                conflict = True
                break
        if not conflict:
            assignment[var] = val
            result = backtrack(assignment)
            if result is not None:
                return result
            del assignment[var]
    return None

solution = backtrack({})
print("Found Valid Assignment:", solution)
""",
        "expected_output": "Found Valid Assignment: {'A': '1', 'B': '2', 'C': '1'}\n",
        "explanation": """### 💡 Code Mechanics & Engineering Insights
**How it Works:**
Backtracking search is Depth-First Search for CSPs with single-variable assignments per level:
1. It chooses an unassigned variable.
2. It tests a domain value; if consistent, it recurses.
3. If an assignment leads to a dead-end, it undoes the variable binding (`del assignment[var]`) and backtracks to try alternative branches.

**Why this matters in Engineering:**
Brute force explores $d^n = 2^3 = 8$ states. Backtracking prunes entire subtrees immediately when a constraint is violated, reducing average search complexity by exponential factors."""
    },
    ("7", 2): {
        "title": "MRV and Degree Heuristic Lab",
        "starter_code": """# Lab: Minimum Remaining Values (MRV) & Degree Heuristic
variables = ['WA', 'NT', 'SA', 'Q']
domains = {
    'WA': ['Blue'],
    'NT': ['Red', 'Green'],
    'SA': ['Red', 'Green', 'Blue'],
    'Q':  ['Red', 'Green', 'Blue']
}
neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q'],
    'Q':  ['NT', 'SA']
}
assignment = {}

def select_unassigned_variable_mrv(domains, assignment):
    \"\"\"Select variable with fewest remaining legal values (Fail-First).\"\"\"
    unassigned = [v for v in variables if v not in assignment]
    # Pick variable with minimum domain size
    return min(unassigned, key=lambda var: len(domains[var]))

mrv_var = select_unassigned_variable_mrv(domains, assignment)
print(f"Selected Variable by MRV: {mrv_var} (Domain size: {len(domains[mrv_var])})")
""",
        "solution_code": """# Complete Solution: MRV Heuristic
variables = ['WA', 'NT', 'SA', 'Q']
domains = {
    'WA': ['Blue'],
    'NT': ['Red', 'Green'],
    'SA': ['Red', 'Green', 'Blue'],
    'Q':  ['Red', 'Green', 'Blue']
}
neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q'],
    'Q':  ['NT', 'SA']
}
assignment = {}

def select_unassigned_variable_mrv(domains, assignment):
    unassigned = [v for v in variables if v not in assignment]
    return min(unassigned, key=lambda var: len(domains[var]))

mrv_var = select_unassigned_variable_mrv(domains, assignment)
print(f"Selected Variable by MRV: {mrv_var} (Domain size: {len(domains[mrv_var])})")
""",
        "expected_output": "Selected Variable by MRV: WA (Domain size: 1)\n",
        "explanation": """### 💡 Code Mechanics & Engineering Insights
**How it Works:**
The **Minimum Remaining Values (MRV)** heuristic embodies the **Fail-First Principle**:
- By picking the variable with the smallest legal domain (`WA` with only 1 choice), if it is destined to fail, it fails immediately at shallow depth rather than after thousands of deep expansions.
- If MRV yields a tie, the **Degree Heuristic** breaks the tie by choosing the variable with the most constraints on other unassigned variables."""
    },
    ("7", 3): {
        "title": "AC-3 Constraint Propagation Lab",
        "starter_code": """# Lab: AC-3 Arc Consistency Algorithm
domains = {
    'X': [1, 2, 3],
    'Y': [2]
}
# Constraint: X < Y

def revise(x, y):
    \"\"\"Remove values from domains[x] that have no valid match in domains[y].\"\"\"
    revised = False
    new_domain_x = []
    for vx in domains[x]:
        # Check if there exists ANY vy in domains[y] such that vx < vy
        if any(vx < vy for vy in domains[y]):
            new_domain_x.append(vx)
        else:
            revised = True
    domains[x] = new_domain_x
    return revised

print("Before AC-3 Revision:", domains)
was_revised = revise('X', 'Y')
print("Did revise remove inconsistent values?", was_revised)
print("After AC-3 Revision:", domains)
""",
        "solution_code": """# Complete Solution: AC-3 Arc Consistency
domains = {
    'X': [1, 2, 3],
    'Y': [2]
}

def revise(x, y):
    revised = False
    new_domain_x = []
    for vx in domains[x]:
        if any(vx < vy for vy in domains[y]):
            new_domain_x.append(vx)
        else:
            revised = True
    domains[x] = new_domain_x
    return revised

print("Before AC-3 Revision:", domains)
was_revised = revise('X', 'Y')
print("Did revise remove inconsistent values?", was_revised)
print("After AC-3 Revision:", domains)
""",
        "expected_output": "Before AC-3 Revision: {'X': [1, 2, 3], 'Y': [2]}\nDid revise remove inconsistent values? True\nAfter AC-3 Revision: {'X': [1], 'Y': [2]}\n",
        "explanation": """### 💡 Code Mechanics & Engineering Insights
**How it Works:**
An arc $(X, Y)$ is **Arc Consistent** if for every value $x \in Domain(X)$, there exists some valid $y \in Domain(Y)$ satisfying the binary constraint.
Here, $X < Y$. For $x=2$ or $x=3$, no $y \in [2]$ satisfies $x < 2$. Thus, $2$ and $3$ are pruned from $X$'s domain.
AC-3 runs in $O(c \cdot d^3)$ time (where $c$ is constraints and $d$ is max domain size), drastically shrinking the search space before backtracking search even starts."""
    },

    # Case 08: Knowledge Graphs
    ("8", 0): {
        "title": "RDF Triples & Entity-Relation Lab",
        "starter_code": """# Lab: Knowledge Graph Representation using RDF Triples
# Triples format: (Subject, Predicate, Object)

triples = [
    ("Alan_Turing", "born_in", "London"),
    ("Alan_Turing", "field_of_work", "Computer_Science"),
    ("London", "located_in", "United_Kingdom"),
    ("Geoffrey_Hinton", "field_of_work", "Computer_Science"),
    ("Geoffrey_Hinton", "born_in", "London")
]

def query_kg(subject=None, predicate=None, obj=None):
    \"\"\"Find matching facts in the Knowledge Graph.\"\"\"
    results = []
    for s, p, o in triples:
        if (subject is None or s == subject) and \\
           (predicate is None or p == predicate) and \\
           (obj is None or o == obj):
            results.append((s, p, o))
    return results

# Query: Find all entities who work in Computer_Science
cs_researchers = query_kg(predicate="field_of_work", obj="Computer_Science")
print("Researchers in CS:", [s for s, p, o in cs_researchers])
""",
        "solution_code": """# Complete Solution: RDF Triples & KG Querying
triples = [
    ("Alan_Turing", "born_in", "London"),
    ("Alan_Turing", "field_of_work", "Computer_Science"),
    ("London", "located_in", "United_Kingdom"),
    ("Geoffrey_Hinton", "field_of_work", "Computer_Science"),
    ("Geoffrey_Hinton", "born_in", "London")
]

def query_kg(subject=None, predicate=None, obj=None):
    results = []
    for s, p, o in triples:
        if (subject is None or s == subject) and \\
           (predicate is None or p == predicate) and \\
           (obj is None or o == obj):
            results.append((s, p, o))
    return results

cs_researchers = query_kg(predicate="field_of_work", obj="Computer_Science")
print("Researchers in CS:", [s for s, p, o in cs_researchers])
""",
        "expected_output": "Researchers in CS: ['Alan_Turing', 'Geoffrey_Hinton']\n",
        "explanation": """### 💡 Code Mechanics & Engineering Insights
**How it Works:**
The Resource Description Framework (RDF) structures world knowledge as directed, labeled multigraphs using $(S, P, O)$ triples.
Because entities are standardized IRIs/strings and edges are typed semantic relations, querying can match patterns across heterogeneous data sources without brittle SQL table joins."""
    },
    ("8", 1): {
        "title": "Building a Graph Adjacency Index",
        "starter_code": """# Lab: Indexing Knowledge Graphs for O(1) Traversal
from collections import defaultdict

triples = [
    ("Alice", "knows", "Bob"),
    ("Alice", "knows", "Charlie"),
    ("Bob", "works_at", "DeepMind"),
    ("Charlie", "works_at", "Google")
]

forward_index = defaultdict(list)
for s, p, o in triples:
    forward_index[s].append((p, o))

# Inspect Alice's direct neighbors
print("Alice's Connections:", dict(forward_index)["Alice"])
""",
        "solution_code": """from collections import defaultdict

triples = [
    ("Alice", "knows", "Bob"),
    ("Alice", "knows", "Charlie"),
    ("Bob", "works_at", "DeepMind"),
    ("Charlie", "works_at", "Google")
]

forward_index = defaultdict(list)
for s, p, o in triples:
    forward_index[s].append((p, o))

print("Alice's Connections:", dict(forward_index)["Alice"])
""",
        "expected_output": "Alice's Connections: [('knows', 'Bob'), ('knows', 'Charlie')]\n",
        "explanation": """### 💡 Code Mechanics & Engineering Insights
**How it Works:**
Scanning a flat list of $N$ triples takes $O(N)$ time. Production graph databases (Neo4j, Amazon Neptune) build index-free adjacency tables (SPO, POS, OSP indices) so graph traversals execute in $O(\text{deg}(v))$ time regardless of total graph size."""
    },
    ("8", 2): {
        "title": "Multi-Hop Graph Reasoning Lab",
        "starter_code": """# Lab: 2-Hop Knowledge Graph Reasoning
# Find: Where do Alice's friends work?
# Path: (?person, knows, ?friend) AND (?friend, works_at, ?company)

graph = {
    "Alice": [("knows", "Bob"), ("knows", "Charlie")],
    "Bob": [("works_at", "DeepMind")],
    "Charlie": [("works_at", "Google")]
}

results = []
for rel1, friend in graph.get("Alice", []):
    if rel1 == "knows":
        for rel2, company in graph.get(friend, []):
            if rel2 == "works_at":
                results.append((friend, company))

print("Alice's friends and their workplaces:")
for friend, company in results:
    print(f"  {friend} -> {company}")
""",
        "solution_code": """graph = {
    "Alice": [("knows", "Bob"), ("knows", "Charlie")],
    "Bob": [("works_at", "DeepMind")],
    "Charlie": [("works_at", "Google")]
}

results = []
for rel1, friend in graph.get("Alice", []):
    if rel1 == "knows":
        for rel2, company in graph.get(friend, []):
            if rel2 == "works_at":
                results.append((friend, company))

print("Alice's friends and their workplaces:")
for friend, company in results:
    print(f"  {friend} -> {company}")
""",
        "expected_output": "Alice's friends and their workplaces:\n  Bob -> DeepMind\n  Charlie -> Google\n",
        "explanation": """### 💡 Code Mechanics & Engineering Insights
**How it Works:**
Multi-hop queries form the basis of SPARQL graph pattern matching and Graph Neural Networks (GNNs). By composing relations $R_1 \circ R_2$, the system infers indirect connections that were never explicitly hardcoded."""
    },
    ("8", 3): {
        "title": "Transitive Rule Inference on Graphs",
        "starter_code": """# Lab: Transitive Closure Inference (SubClassOf)
# If A subClassOf B, and B subClassOf C, then A subClassOf C

hierarchy = {
    "GoldenRetriever": "Dog",
    "Dog": "Mammal",
    "Mammal": "Animal"
}

def is_subclass(entity, target_class):
    curr = entity
    while curr in hierarchy:
        parent = hierarchy[curr]
        if parent == target_class:
            return True
        curr = parent
    return False

print("Is GoldenRetriever an Animal?", is_subclass("GoldenRetriever", "Animal"))
print("Is GoldenRetriever a Bird?", is_subclass("GoldenRetriever", "Bird"))
""",
        "solution_code": """hierarchy = {
    "GoldenRetriever": "Dog",
    "Dog": "Mammal",
    "Mammal": "Animal"
}

def is_subclass(entity, target_class):
    curr = entity
    while curr in hierarchy:
        parent = hierarchy[curr]
        if parent == target_class:
            return True
        curr = parent
    return False

print("Is GoldenRetriever an Animal?", is_subclass("GoldenRetriever", "Animal"))
print("Is GoldenRetriever a Bird?", is_subclass("GoldenRetriever", "Bird"))
""",
        "expected_output": "Is GoldenRetriever an Animal? True\nIs GoldenRetriever a Bird? False\n",
        "explanation": """### 💡 Code Mechanics & Engineering Insights
**How it Works:**
Ontological reasoning engines (like OWL / RDFS reasoners) compute deductive entailment by tracing transitive axioms. This enables modern search engines (Google Knowledge Graph) to understand that a query for 'mammals' includes Golden Retrievers."""
    },

    # Case 09: Logic Engine
    ("9", 0): {
        "title": "Propositional Truth Table Evaluator",
        "starter_code": """# Lab: Propositional Logic Truth Table
# Verify De Morgan's Law: not (A and B) == (not A) or (not B)

print("A | B | not(A and B) | (not A) or (not B) | Equivalent?")
print("-" * 55)
for A in [True, False]:
    for B in [True, False]:
        lhs = not (A and B)
        rhs = (not A) or (not B)
        equiv = (lhs == rhs)
        print(f"{A!s:5} | {B!s:5} | {lhs!s:14} | {rhs!s:19} | {equiv}")
""",
        "solution_code": """print("A | B | not(A and B) | (not A) or (not B) | Equivalent?")
print("-" * 55)
for A in [True, False]:
    for B in [True, False]:
        lhs = not (A and B)
        rhs = (not A) or (not B)
        equiv = (lhs == rhs)
        print(f"{A!s:5} | {B!s:5} | {lhs!s:14} | {rhs!s:19} | {equiv}")
""",
        "expected_output": """A | B | not(A and B) | (not A) or (not B) | Equivalent?
-------------------------------------------------------
True  | True  | False          | False               | True
True  | False | True           | True                | True
False | True  | True           | True                | True
False | False | True           | True                | True
""",
        "explanation": """### 💡 Code Mechanics & Engineering Insights
**How it Works:**
Propositional logic evaluates Boolean truth functions across $2^N$ model valuations.
Because both columns produce identical truth assignments across all rows, the two formulas are **logically equivalent** (semantic entailment)."""
    },
    ("9", 1): {
        "title": "First-Order Logic Unification Lab",
        "starter_code": """# Lab: First-Order Logic Term Substitution
# Replace variable ?x with 'Socrates' in Mortal(?x)

def substitute(term, var, val):
    return term.replace(f"?{var}", val)

statement = "Mortal(?x) if Human(?x)"
concrete = substitute(statement, "x", "Socrates")
print("Concrete Instantiation:", concrete)
""",
        "solution_code": """def substitute(term, var, val):
    return term.replace(f"?{var}", val)

statement = "Mortal(?x) if Human(?x)"
concrete = substitute(statement, "x", "Socrates")
print("Concrete Instantiation:", concrete)
""",
        "expected_output": "Concrete Instantiation: Mortal(Socrates) if Human(Socrates)\n",
        "explanation": """### 💡 Code Mechanics & Engineering Insights
**How it Works:**
Universal Instantiation allows replacing universally quantified variables with ground constants from the domain universe, translating abstract first-order rules into actionable propositional instances."""
    },
    ("9", 2): {
        "title": "Forward Chaining on Horn Clauses",
        "starter_code": """# Lab: Forward Chaining on Definite Clauses
# Rules:
# 1. A and B -> C
# 2. C -> D
# Initial Facts: A, B

facts = {"A", "B"}
rules = [
    ({"A", "B"}, "C"),
    ({"C"}, "D")
]

inferred_new = True
while inferred_new:
    inferred_new = False
    for premises, conclusion in rules:
        if conclusion not in facts and premises.issubset(facts):
            facts.add(conclusion)
            inferred_new = True
            print(f"Fired rule! Inferred: {conclusion}")

print("Final Working Memory Facts:", sorted(facts))
""",
        "solution_code": """facts = {"A", "B"}
rules = [
    ({"A", "B"}, "C"),
    ({"C"}, "D")
]

inferred_new = True
while inferred_new:
    inferred_new = False
    for premises, conclusion in rules:
        if conclusion not in facts and premises.issubset(facts):
            facts.add(conclusion)
            inferred_new = True
            print(f"Fired rule! Inferred: {conclusion}")

print("Final Working Memory Facts:", sorted(facts))
""",
        "expected_output": "Fired rule! Inferred: C\nFired rule! Inferred: D\nFinal Working Memory Facts: ['A', 'B', 'C', 'D']\n",
        "explanation": """### 💡 Code Mechanics & Engineering Insights
**How it Works:**
Forward chaining runs Modus Ponens repeatedly over Horn clauses in linear time $O(KB)$, monotonically expanding the known fact set until a fixed point (quiescence) is reached."""
    },
    ("9", 3): {
        "title": "Resolution Refutation Step Lab",
        "starter_code": """# Lab: Propositional Resolution Rule
# Clause 1: P or Q
# Clause 2: not P or R
# Resolvent: Q or R

def resolve(clause1, clause2):
    resolvents = []
    for lit1 in clause1:
        # Check for complementary literal
        comp = f"~{lit1}" if not lit1.startswith("~") else lit1[1:]
        if comp in clause2:
            new_c = (set(clause1) - {lit1}) | (set(clause2) - {comp})
            resolvents.append(new_c)
    return resolvents

c1 = {"P", "Q"}
c2 = {"~P", "R"}
resolvents = resolve(c1, c2)
print("Resolvent Clause:", [sorted(r) for r in resolvents])
""",
        "solution_code": """def resolve(clause1, clause2):
    resolvents = []
    for lit1 in clause1:
        comp = f"~{lit1}" if not lit1.startswith("~") else lit1[1:]
        if comp in clause2:
            new_c = (set(clause1) - {lit1}) | (set(clause2) - {comp})
            resolvents.append(new_c)
    return resolvents

c1 = {"P", "Q"}
c2 = {"~P", "R"}
resolvents = resolve(c1, c2)
print("Resolvent Clause:", [sorted(r) for r in resolvents])
""",
        "expected_output": "Resolvent Clause: [['Q', 'R']]\n",
        "explanation": """### 💡 Code Mechanics & Engineering Insights
**How it Works:**
Resolution is sound and refutation-complete: if a set of clauses is unsatisfiable, repeated resolution is guaranteed to derive the empty clause $\square$ (Contradiction)."""
    },

    # Case 10: Situation Calculus & Frame Problem
    ("10", 0): {
        "title": "Situations and Actions Lab",
        "starter_code": """# Lab: Modeling Change with Situations
# s0 -> do(TurnOnLight, s0) -> do(TurnOffLight, ...)

class Situation:
    def __init__(self, name, parent=None, action=None):
        self.name = name
        self.parent = parent
        self.action = action

s0 = Situation("S0")
s1 = Situation("S1", parent=s0, action="turn_on_light")
print(f"Situation {s1.name} reached from {s1.parent.name} via action '{s1.action}'")
""",
        "solution_code": """class Situation:
    def __init__(self, name, parent=None, action=None):
        self.name = name
        self.parent = parent
        self.action = action

s0 = Situation("S0")
s1 = Situation("S1", parent=s0, action="turn_on_light")
print(f"Situation {s1.name} reached from {s1.parent.name} via action '{s1.action}'")
""",
        "expected_output": "Situation S1 reached from S0 via action 'turn_on_light'\n",
        "explanation": """### 💡 Code Mechanics & Engineering Insights
**How it Works:**
Situation Calculus represents time and causality as a branched tree of discrete situations rooted at $S_0$. The function $do(a, s)$ returns the new situation that results from performing action $a$ in situation $s$."""
    },
    ("10", 1): {
        "title": "Action Preconditions and Effects Lab",
        "starter_code": """# Lab: Executing Action with Preconditions
def can_execute(action, state):
    if action == "paint_car_green":
        return state.get("has_green_paint", False) and state.get("car_clean", False)
    return False

state = {"has_green_paint": True, "car_clean": True, "car_color": "red"}
print("Can paint car green?", can_execute("paint_car_green", state))
""",
        "solution_code": """def can_execute(action, state):
    if action == "paint_car_green":
        return state.get("has_green_paint", False) and state.get("car_clean", False)
    return False

state = {"has_green_paint": True, "car_clean": True, "car_color": "red"}
print("Can paint car green?", can_execute("paint_car_green", state))
""",
        "expected_output": "Can paint car green? True\n",
        "explanation": """### 💡 Code Mechanics & Engineering Insights
**How it Works:**
Possibility Axioms ($\text{Poss}(a, s) \iff \text{Preconditions}$) formalize physical feasibility: an action can only occur if the agent satisfies all requirements in the current situation."""
    },
    ("10", 2): {
        "title": "Successor-State Axioms (Reiter's Solution)",
        "starter_code": """# Lab: Successor-State Axiom for Fluent 'CarIsGreen'
# Car is green in do(a, s) iff:
# (a was paint_car_green) OR (Car was already green in s AND a was NOT paint_car_other_color)

def fluent_car_is_green(prev_is_green, action):
    # Action effects
    action_causes_green = (action == "paint_car_green")
    action_removes_green = (action in ["paint_car_blue", "strip_paint"])
    
    # Successor state axiom
    return action_causes_green or (prev_is_green and not action_removes_green)

print("Was red, action=paint_car_green -> Green?", fluent_car_is_green(False, "paint_car_green"))
print("Was green, action=turn_on_radio   -> Green?", fluent_car_is_green(True, "turn_on_radio"))
print("Was green, action=paint_car_blue  -> Green?", fluent_car_is_green(True, "paint_car_blue"))
""",
        "solution_code": """def fluent_car_is_green(prev_is_green, action):
    action_causes_green = (action == "paint_car_green")
    action_removes_green = (action in ["paint_car_blue", "strip_paint"])
    return action_causes_green or (prev_is_green and not action_removes_green)

print("Was red, action=paint_car_green -> Green?", fluent_car_is_green(False, "paint_car_green"))
print("Was green, action=turn_on_radio   -> Green?", fluent_car_is_green(True, "turn_on_radio"))
print("Was green, action=paint_car_blue  -> Green?", fluent_car_is_green(True, "paint_car_blue"))
""",
        "expected_output": """Was red, action=paint_car_green -> Green? True
Was green, action=turn_on_radio   -> Green? True
Was green, action=paint_car_blue  -> Green? False
""",
        "explanation": """### 💡 Code Mechanics & Engineering Insights
**How it Works:**
Raymond Reiter's **Successor-State Axioms** solved the classical **Frame Problem**:
Instead of writing $O(A \times F)$ frame axioms stating what doesn't change when each action occurs, each fluent has exactly one axiom stating all actions that make it true, and all actions that make it false. Everything else preserves its state."""
    },
    ("10", 3): {
        "title": "Goal Progression Verification Lab",
        "starter_code": """# Lab: Verify Goal Achievement in Situation Calculus
initial_state = {"holding_key": True, "door_locked": True}

def step(state, action):
    new_s = state.copy()
    if action == "unlock_door" and state.get("holding_key"):
        new_s["door_locked"] = False
    return new_s

s1 = step(initial_state, "unlock_door")
print("Is door unlocked after step 1?", s1["door_locked"] == False)
""",
        "solution_code": """initial_state = {"holding_key": True, "door_locked": True}

def step(state, action):
    new_s = state.copy()
    if action == "unlock_door" and state.get("holding_key"):
        new_s["door_locked"] = False
    return new_s

s1 = step(initial_state, "unlock_door")
print("Is door unlocked after step 1?", s1["door_locked"] == False)
""",
        "expected_output": "Is door unlocked after step 1? True\n",
        "explanation": """### 💡 Code Mechanics & Engineering Insights
**How it Works:**
Planning in situation calculus is automated theorem proving: find a situation term $s = do(a_n, do(a_1, S_0))$ such that $\text{KB} \models \text{Goal}(s)$."""
    },

    # Case 11: Classical Planning
    ("11", 0): {
        "title": "STRIPS Action Operator Engine",
        "starter_code": """# Lab: STRIPS Action Execution
# Transition: State' = (State - Del) + Add

class Action:
    def __init__(self, name, pre, add_list, del_list):
        self.name = name
        self.pre = set(pre)
        self.add = set(add_list)
        self.del_list = set(del_list)

    def is_applicable(self, state):
        return self.pre.issubset(state)

    def apply(self, state):
        return (state - self.del_list) | self.add

state = {"At(A)", "Empty(Gripper)", "BoxAt(A)"}
pickup = Action("PickUp(Box)", pre=["At(A)", "Empty(Gripper)", "BoxAt(A)"],
                add_list=["Holding(Box)"], del_list=["Empty(Gripper)", "BoxAt(A)"])

if pickup.is_applicable(state):
    new_state = pickup.apply(state)
    print("New State:", sorted(new_state))
""",
        "solution_code": """class Action:
    def __init__(self, name, pre, add_list, del_list):
        self.name = name
        self.pre = set(pre)
        self.add = set(add_list)
        self.del_list = set(del_list)

    def is_applicable(self, state):
        return self.pre.issubset(state)

    def apply(self, state):
        return (state - self.del_list) | self.add

state = {"At(A)", "Empty(Gripper)", "BoxAt(A)"}
pickup = Action("PickUp(Box)", pre=["At(A)", "Empty(Gripper)", "BoxAt(A)"],
                add_list=["Holding(Box)"], del_list=["Empty(Gripper)", "BoxAt(A)"])

if pickup.is_applicable(state):
    new_state = pickup.apply(state)
    print("New State:", sorted(new_state))
""",
        "expected_output": "New State: ['At(A)', 'Holding(Box)']\n",
        "explanation": """### 💡 Code Mechanics & Engineering Insights
**How it Works:**
The STRIPS operator applies set operations in $O(1)$ amortized time: remove the delete list and add the add list. All other facts persist without extra code."""
    },
    ("11", 1): {
        "title": "Forward Progression Planner",
        "starter_code": """# Lab: Simple Forward Progression Search
# Find sequence of actions to reach Goal from Initial State

actions = [
    {"name": "Move(A, B)", "pre": {"At(A)"}, "add": {"At(B)"}, "del": {"At(A)"}},
    {"name": "Move(B, C)", "pre": {"At(B)"}, "add": {"At(C)"}, "del": {"At(B)"}}
]

initial_state = {"At(A)"}
goal = {"At(C)"}

def forward_plan(init, goal):
    queue = [(init, [])]
    visited = [init]
    while queue:
        curr, plan = queue.pop(0)
        if goal.issubset(curr):
            return plan
        for a in actions:
            if a["pre"].issubset(curr):
                nxt = (curr - a["del"]) | a["add"]
                if nxt not in visited:
                    visited.append(nxt)
                    queue.append((nxt, plan + [a["name"]]))
    return None

plan = forward_plan(initial_state, goal)
print("Synthesized Plan:", plan)
""",
        "solution_code": """actions = [
    {"name": "Move(A, B)", "pre": {"At(A)"}, "add": {"At(B)"}, "del": {"At(A)"}},
    {"name": "Move(B, C)", "pre": {"At(B)"}, "add": {"At(C)"}, "del": {"At(B)"}}
]

initial_state = {"At(A)"}
goal = {"At(C)"}

def forward_plan(init, goal):
    queue = [(init, [])]
    visited = [init]
    while queue:
        curr, plan = queue.pop(0)
        if goal.issubset(curr):
            return plan
        for a in actions:
            if a["pre"].issubset(curr):
                nxt = (curr - a["del"]) | a["add"]
                if nxt not in visited:
                    visited.append(nxt)
                    queue.append((nxt, plan + [a["name"]]))
    return None

plan = forward_plan(initial_state, goal)
print("Synthesized Plan:", plan)
""",
        "expected_output": "Synthesized Plan: ['Move(A, B)', 'Move(B, C)']\n",
        "explanation": """### 💡 Code Mechanics & Engineering Insights
**How it Works:**
Forward progression explores the concrete state space using graph search (BFS or A*), expanding only legally applicable actions until the goal subset is satisfied."""
    },
    ("11", 2): {
        "title": "Backward Goal Regression Lab",
        "starter_code": """# Lab: Backward Goal Regression
# Goal G regressed through action A:
# Regressed_G = (G - Add(A)) + Pre(A)

goal = {"At(C)", "Holding(Box)"}
action = {
    "name": "Move(B, C)",
    "pre": {"At(B)"},
    "add": {"At(C)"},
    "del": {"At(B)"}
}

def regress(goal, action):
    # Action is relevant if it adds something in goal and deletes nothing in goal
    if action["add"].intersection(goal) and not action["del"].intersection(goal):
        return (goal - action["add"]) | action["pre"]
    return None

subgoal = regress(goal, action)
print("Regressed Subgoal:", sorted(subgoal))
""",
        "solution_code": """goal = {"At(C)", "Holding(Box)"}
action = {
    "name": "Move(B, C)",
    "pre": {"At(B)"},
    "add": {"At(C)"},
    "del": {"At(B)"}
}

def regress(goal, action):
    if action["add"].intersection(goal) and not action["del"].intersection(goal):
        return (goal - action["add"]) | action["pre"]
    return None

subgoal = regress(goal, action)
print("Regressed Subgoal:", sorted(subgoal))
""",
        "expected_output": "Regressed Subgoal: ['At(B)', 'Holding(Box)']\n",
        "explanation": """### 💡 Code Mechanics & Engineering Insights
**How it Works:**
Backward regression searches backward from the goal: it drops what the action provides (`Add`) and adds what the action requires (`Pre`), guaranteeing that irrelevant actions are never considered."""
    },
    ("11", 3): {
        "title": "Partial-Order Causal Link Checking",
        "starter_code": """# Lab: Detect Causal Link Threats in Partial-Order Planning
# Causal link: Step1 --[At(RoomA)]--> Step2
# Threat: Step3 deletes At(RoomA)

causal_link = {"producer": "Step1", "condition": "At(RoomA)", "consumer": "Step2"}
step3 = {"name": "Step3", "del": ["At(RoomA)"]}

def is_threat(step, link):
    return link["condition"] in step.get("del", [])

print("Is Step3 a threat to the causal link?", is_threat(step3, causal_link))
""",
        "solution_code": """causal_link = {"producer": "Step1", "condition": "At(RoomA)", "consumer": "Step2"}
step3 = {"name": "Step3", "del": ["At(RoomA)"]}

def is_threat(step, link):
    return link["condition"] in step.get("del", [])

print("Is Step3 a threat to the causal link?", is_threat(step3, causal_link))
""",
        "expected_output": "Is Step3 a threat to the causal link? True\n",
        "explanation": """### 💡 Code Mechanics & Engineering Insights
**How it Works:**
Threat detection guarantees plan correctness in non-linear planners: whenever a parallel action threatens a causal link, the planner adds an ordering constraint (Promotion or Demotion) to prevent the threat from executing in between."""
    }
}
print("Loaded CODE_LABS_7_TO_11 successfully!")
