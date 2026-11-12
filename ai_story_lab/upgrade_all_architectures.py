import json
import re

print("Loading level_content...")
with open('/Users/aadarshamahato/Downloads/LEARNING_PLATFORM/ai_story_lab/level_content.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Parse LEVEL_CONTENT by executing in dedicated namespace
ns = {}
exec(text, ns)
LEVEL_CONTENT = ns['LEVEL_CONTENT']

print(f"Loaded {len(LEVEL_CONTENT)} cases.")

# Dictionary of rich architectural diagrams for all episodes that were previously trivial or empty
ARCHITECTURES = {
    # Case 1
    ("1", 2, "Architecture Diagram"): """graph LR
  subgraph Sensors ["Sensory Telemetry"]
    S1["Wheel Encoders"]
    S2["Proximity Sonar"]
  end
  subgraph Agent ["Model-Based Reflex Agent Internal State"]
    TRANS["Transition Model: How World Evolves"]
    WORLD["Internal Estimated World State"]
    RULES["Condition-Action Rules Engine"]
    S1 & S2 --> TRANS --> WORLD --> RULES
  end
  subgraph Actuators ["Actuator Output"]
    ACT["Motor Throttle & Steering"]
    RULES --> ACT
  end
  style Sensors fill:#0f172a,stroke:#3b82f6
  style Agent fill:#1e1b4b,stroke:#6366f1
  style Actuators fill:#064e3b,stroke:#10b981""",

    ("1", 3, "Architecture Diagram"): """graph TD
  subgraph Perception ["Perception & State Tracker"]
    STATE["Current World State S(t)"]
    PREDICT["Predictive Action Model: S(t+1) = f(S(t), a)"]
    STATE --> PREDICT
  end
  subgraph UtilityEngine ["Utility Maximization Engine"]
    UTIL["Utility Function: Multi-Attribute Score U(S)"]
    MEU["Max Expected Utility: argmax E[U(Result(s, a))]"]
    PREDICT --> UTIL --> MEU
  end
  subgraph Control ["Actuation"]
    MEU --> ACT["Dispatched Control Action a*"]
  end
  style Perception fill:#0f172a,stroke:#3b82f6
  style UtilityEngine fill:#1e1b4b,stroke:#6366f1
  style Control fill:#064e3b,stroke:#10b981""",

    # Case 2
    ("2", 1, "Architecture Diagram"): """graph LR
  subgraph PuzzleState ["8-Puzzle State Representation"]
    S1["Initial State Config"]
    LEGAL["Legal Moves: Slide Empty Tile {Up, Down, Left, Right}"]
    S1 --> LEGAL
  end
  subgraph Evaluation ["Heuristic Evaluation"]
    MAN["Manhattan Distance h(n) = Σ |x_i - x_goal| + |y_i - y_goal|"]
    LEGAL --> MAN
  end
  subgraph Goal ["Goal Test"]
    GOAL["Target State Config [1 2 3 / 4 5 6 / 7 8 _]"]
    MAN --> GOAL
  end
  style PuzzleState fill:#0f172a,stroke:#3b82f6
  style Evaluation fill:#1e1b4b,stroke:#6366f1
  style Goal fill:#064e3b,stroke:#10b981""",

    ("2", 2, "Architecture Diagram"): """graph TD
  subgraph RoadNetwork ["Autonomous Delivery Logistics Network"]
    START["Distribution Center (Start Waypoint)"]
    WAY1["Transit Junction Alpha (Weight: 14 km, Congestion: Low)"]
    WAY2["Beltway Waypoint Beta (Weight: 22 km, Speed: 80 km/h)"]
    GOAL["Customer Fulfillment Depot (Goal Waypoint)"]
    START -->|"Path A: Urban Grid"| WAY1 -->|"Highway Leg"| GOAL
    START -->|"Path B: Bypass"| WAY2 -->|"Express Connector"| GOAL
  end
  style RoadNetwork fill:#0f172a,stroke:#3b82f6""",

    ("2", 3, "Architecture Diagram"): """graph TD
  subgraph SearchPerformance ["Search Algorithm Performance Evaluation Dimensions"]
    C["Completeness: Guarantees finding a solution if one exists?"]
    T["Time Complexity: Number of generated nodes O(b^d)"]
    S["Space Complexity: Maximum memory consumed in RAM O(b^d) or O(b·d)"]
    O["Optimality: Guarantees finding highest-quality / lowest-cost path?"]
    EVAL["Search Algorithm Evaluation Benchmark"]
    EVAL --> C & T & S & O
  end
  style SearchPerformance fill:#1e1b4b,stroke:#6366f1""",

    # Case 5
    ("5", 0, "Visualization"): """graph LR
  subgraph CostComponents ["A* Evaluation Function"]
    G["Known Path Cost g(n): Start to n"]
    H["Heuristic Estimate h(n): n to Goal"]
  end
  subgraph TotalCost ["Priority Evaluation"]
    F["Total f(n) = g(n) + h(n)"]
    G & H --> F
    F --> PQ["Frontier Priority Min-Heap"]
  end
  style CostComponents fill:#0f172a,stroke:#3b82f6
  style TotalCost fill:#1e1b4b,stroke:#6366f1""",

    ("5", 1, "Architecture Diagram"): """graph TD
  subgraph AdmissibilityInvariants ["Admissible Heuristic Mathematical Bound"]
    HN["Estimated Cost h(n)"]
    HSTAR["True Minimal Cost h*(n)"]
    HN -.->|"Invariant: h(n) <= h*(n)"| HSTAR
  end
  subgraph OptimalityProof ["Optimality Guarantee"]
    SUB["Suboptimal Goal G2 has f(G2) = g(G2) > C*"]
    OPT["Optimal Goal G has f(G) = C*"]
    HN --> SUB & OPT
    OPT -->|"A* will never expand G2 before G"| WIN["Guaranteed Optimal Path"]
  end
  style AdmissibilityInvariants fill:#0f172a,stroke:#3b82f6
  style OptimalityProof fill:#064e3b,stroke:#10b981""",

    ("5", 2, "Architecture Diagram"): """graph LR
  subgraph Monotonicity ["Consistency / Monotonicity Triangle Inequality"]
    N["Node n (Heuristic h(n))"]
    STEP["Step Cost c(n, a, n')"]
    NPRIME["Successor n' (Heuristic h(n'))"]
    GOAL["Goal Node (h = 0)"]
    N -->|"Action a"| NPRIME
    N -.->|"h(n)"| GOAL
    NPRIME -.->|"h(n')"| GOAL
    INEQ["h(n) <= c(n, a, n') + h(n')"]
  end
  style Monotonicity fill:#1e1b4b,stroke:#6366f1""",

    # Case 7: CSPs
    ("7", 0, "Visualization"): """graph LR
  subgraph CSP ["Constraint Satisfaction Problem Formalism"]
    X["Variables X = {X1, X2, ... Xn}"]
    D["Domains D = {D1, D2, ... Dn}"]
    C["Constraints C = {C1, C2, ... Cm}"]
    X -->|"Each Xi takes value from"| D
    D -->|"Allowable combinations bounded by"| C
  end
  style CSP fill:#1e1b4b,stroke:#6366f1""",

    ("7", 0, "Architecture Diagram"): """graph TD
  subgraph Variables ["CSP Scheduling Variables"]
    T1["Assembly_Station_1"]
    T2["Quality_Inspection_2"]
    T3["Packaging_Bay_3"]
  end
  subgraph Domains ["Resource Domains"]
    D1["Time Slots: {08:00, 10:00, 14:00}"]
  end
  subgraph Constraints ["Explicit Constraints"]
    C1["Temporal Order: Finish(T1) <= Start(T2)"]
    C2["Resource Mutex: Station(T2) != Station(T3)"]
  end
  Variables --> Domains --> Constraints
  style Variables fill:#0f172a,stroke:#3b82f6
  style Domains fill:#1e1b4b,stroke:#6366f1
  style Constraints fill:#064e3b,stroke:#10b981""",

    ("7", 1, "Visualization"): """graph TD
  subgraph BacktrackingFlow ["Backtracking Search with Dynamic Heuristics"]
    VAR["Select Variable via MRV: Minimum Remaining Values"]
    VAL["Order Values via LCV: Least Constraining Value"]
    TRY["Assign Variable = Value & Check Consistency"]
    VAR --> VAL --> TRY
    TRY -->|"Valid"| RECURSE["Recurse on Next Unassigned Variable"]
    TRY -->|"Conflict"| BT["Backtrack & Restore Pruned Domains"]
  end
  style BacktrackingFlow fill:#1e1b4b,stroke:#6366f1""",

    ("7", 1, "Architecture Diagram"): """graph LR
  subgraph SelectionHeuristics ["Variable & Value Selection Heuristics"]
    MRV["MRV (Fail-First): Pick variable with smallest legal domain"]
    DEG["Degree Heuristic: Pick variable with most constraints on others"]
    LCV["LCV (Fail-Last): Pick value that leaves most options for neighbors"]
    MRV --> DEG --> LCV
  end
  style SelectionHeuristics fill:#0f172a,stroke:#3b82f6""",

    ("7", 2, "Visualization"): """graph TD
  subgraph AC3Engine ["AC-3 Arc Consistency Algorithm"]
    Q["Initialize Queue with all directed Arcs (Xi, Xj)"]
    POP["Pop Arc (Xi, Xj) from Queue"]
    REV["Revise(Xi, Xj): Remove x from D(Xi) if no valid y in D(Xj)"]
    Q --> POP --> REV
    REV -->|"D(Xi) modified?"| ADD["Add all incoming arcs (Xk, Xi) back to Queue"]
    REV -->|"No change"| CHECK["Check if Queue Empty"]
    ADD --> CHECK
    CHECK -->|"Queue not empty"| POP
    CHECK -->|"Queue empty"| DONE["Consistent Constraint Network"]
  end
  style AC3Engine fill:#1e1b4b,stroke:#6366f1""",

    ("7", 2, "Architecture Diagram"): """graph LR
  subgraph ArcCheck ["Arc Consistency Invariant for Arc (Xi, Xj)"]
    XI["Variable Xi with Domain D(Xi)"]
    XJ["Variable Xj with Domain D(Xj)"]
    REL["Constraint C(Xi, Xj)"]
    XI --> REL --> XJ
    COND["For every x in D(Xi), there MUST exist y in D(Xj) satisfying C"]
  end
  style ArcCheck fill:#0f172a,stroke:#3b82f6""",

    ("7", 3, "Visualization"): """graph TD
  subgraph ForwardChecking ["Forward Checking vs Full Lookahead"]
    ASSIGN["Assign Current Variable Xi = v"]
    FC["Forward Checking: Prune immediately inconsistent values in neighbors"]
    MAC["Maintaining Arc Consistency (MAC): Run AC-3 on affected subnetwork"]
    ASSIGN --> FC --> MAC
  end
  style ForwardChecking fill:#1e1b4b,stroke:#6366f1""",

    ("7", 3, "Architecture Diagram"): """graph TD
  subgraph IntelligentBacktracking ["Conflict-Directed Backjumping (CBJ)"]
    DEAD["Dead End: Domain of current variable becomes empty"]
    CONF["Compute Conflict Set: Variables that caused the domain eliminations"]
    JUMP["Backjump directly to deepest variable in Conflict Set"]
    NOGOOD["Store Nogood Constraint to Prevent Re-exploring Subtree"]
    DEAD --> CONF --> JUMP --> NOGOOD
  end
  style IntelligentBacktracking fill:#064e3b,stroke:#10b981""",

    # Case 8: Knowledge Representation
    ("8", 0, "Visualization"): """graph LR
  subgraph KnowledgeGraph ["Industrial Semantic Knowledge Graph"]
    E1["Asset: Generator_G1"]
    E2["Facility: Substation_Alpha"]
    E3["Spec: Max_Output_500MW"]
    E1 -->|"locatedAt"| E2
    E1 -->|"ratedCapacity"| E3
  end
  style KnowledgeGraph fill:#1e1b4b,stroke:#6366f1""",

    ("8", 0, "Architecture Diagram"): """graph TD
  subgraph Architecture ["Enterprise Knowledge Graph Pipeline"]
    INGEST["Telemetry & ERP Ingestion"]
    EXTRACT["Entity Resolution & Triple Extraction (S, P, O)"]
    GRAPH["Graph Database (Neo4j / Amazon Neptune RDF)"]
    REASON["OWL / RDFS Rule Inference Engine"]
    APP["Diagnostic & Predictive AI Applications"]
    INGEST --> EXTRACT --> GRAPH --> REASON --> APP
  end
  style Architecture fill:#0f172a,stroke:#3b82f6""",

    ("8", 1, "Visualization"): """graph TD
  subgraph ClassHierarchy ["Ontology Taxonomy: rdfs:subClassOf"]
    ROOT["IndustrialComponent"]
    PUMP["HydraulicPump"]
    CENT["CentrifugalPump"]
    ROOT --> PUMP --> CENT
    P1["Pump_Unit_042 (rdf:type)"]
    CENT -->|"Instantiates"| P1
  end
  style ClassHierarchy fill:#1e1b4b,stroke:#6366f1""",

    ("8", 1, "Architecture Diagram"): """graph LR
  subgraph OntologyStack ["W3C Semantic Web Standards Stack"]
    XML["XML & URI Grounding"]
    RDF["RDF: Graph Data Model (Triples)"]
    RDFS["RDFS: Vocabularies & Subclass Inheritance"]
    OWL["OWL: Description Logic & Axiomatic Reasoning"]
    SPARQL["SPARQL: Graph Query Language"]
    XML --> RDF --> RDFS --> OWL --> SPARQL
  end
  style OntologyStack fill:#0f172a,stroke:#3b82f6""",

    ("8", 2, "Visualization"): """graph TD
  subgraph DescriptionLogic ["Description Logic Axioms (TBox vs ABox)"]
    TBOX["TBox: Concept Definitions: SafeAsset ≡ Asset ⊓ ∀hasSafetyCert.Valid"]
    ABOX["ABox: Instance Assertions: Compressor_A : Asset, (Compressor_A, Cert_101) : hasSafetyCert"]
    REASON["Tableau Inference Algorithm: Proves Compressor_A is a SafeAsset"]
    TBOX & ABOX --> REASON
  end
  style DescriptionLogic fill:#1e1b4b,stroke:#6366f1""",

    ("8", 2, "Architecture Diagram"): """graph LR
  subgraph TableauEngine ["Description Logic Tableau Reasoning Engine"]
    INPUT["Input Knowledge Base (TBox + ABox)"]
    NORM["Negation Normal Form (NNF) Converter"]
    EXPAND["Tableau Expansion Rules (⊓-rule, ⊔-rule, ∃-rule, ∀-rule)"]
    CLASH["Clash Detection: Search for Contradictory A ⊓ ¬A"]
    INPUT --> NORM --> EXPAND --> CLASH
  end
  style TableauEngine fill:#0f172a,stroke:#3b82f6""",

    ("8", 3, "Visualization"): """graph LR
  subgraph QueryPattern ["SPARQL Triple Pattern Matching"]
    PAT["Triple Pattern: ?pump :locatedIn :Facility_A . ?pump :status :Critical"]
    GRAPH["Knowledge Graph Triples"]
    MATCH["Graph Pattern Matcher / Subgraph Isomorphism"]
    BIND["Variable Binding Solution Set: {?pump: CentrifugalPump_03}"]
    PAT & GRAPH --> MATCH --> BIND
  end
  style QueryPattern fill:#1e1b4b,stroke:#6366f1""",

    ("8", 3, "Architecture Diagram"): """graph TD
  subgraph SPARQLEngine ["Enterprise SPARQL Query Execution Engine"]
    PARSER["SPARQL Lexer & Abstract Syntax Tree Parser"]
    OPTIMIZER["Cost-Based Query Optimizer (Reorder Join Triple Patterns)"]
    EXEC["SPO / POS / OSP B-Tree Index Join Operator"]
    RESULTS["JSON / CSV / RDF Tuple Serializer"]
    PARSER --> OPTIMIZER --> EXEC --> RESULTS
  end
  style SPARQLEngine fill:#0f172a,stroke:#3b82f6""",

    # Case 9: Propositional Logic
    ("9", 0, "Visualization"): """graph TD
  subgraph LogicAST ["Propositional Logic Abstract Syntax Tree"]
    OR["∨ (Disjunction)"]
    AND["∧ (Conjunction)"]
    NOT["¬ (Negation)"]
    P["P: SensorActive"]
    Q["Q: ValveOpen"]
    R["R: TankFull"]
    OR --> AND & R
    AND --> P & NOT
    NOT --> Q
  end
  style LogicAST fill:#1e1b4b,stroke:#6366f1""",

    ("9", 0, "Architecture Diagram"): """graph LR
  subgraph TruthTableEngine ["Propositional Truth Table & Model Checking"]
    PROPS["Input Propositions: P, Q, R (2^3 = 8 Worlds)"]
    EVAL["Evaluate Sentences across all 8 Interpretations"]
    ENT["Entailment Verification: KB |= α iff M(KB) ⊆ M(α)"]
    PROPS --> EVAL --> ENT
  end
  style TruthTableEngine fill:#0f172a,stroke:#3b82f6""",

    ("9", 1, "Visualization"): """graph LR
  subgraph CNFPipeline ["CNF Transformation Sequence"]
    IMP["1. Eliminate Implication: A => B ≡ ¬A ∨ B"]
    DEM["2. De Morgan: ¬(A ∧ B) ≡ ¬A ∨ ¬B"]
    DIST["3. Distribute ∨ over ∧: A ∨ (B ∧ C) ≡ (A ∨ B) ∧ (A ∨ C)"]
    CNF["4. Canonical CNF Clause Set"]
    IMP --> DEM --> DIST --> CNF
  end
  style CNFPipeline fill:#1e1b4b,stroke:#6366f1""",

    ("9", 1, "Architecture Diagram"): """graph TD
  subgraph CNFValidation ["CNF Equisatisfiability & Tseitin Transformation"]
    INPUT["Arbitrary Boolean Logic Formula φ"]
    TSEITIN["Tseitin Transform: Introduce Auxiliary Variable per Sub-Formula"]
    LINEAR["Guarantees Linear Formula Size O(N) vs Exponential Distribution O(2^N)"]
    SAT_SOLVE["Ready for Modern CDCL SAT Solvers"]
    INPUT --> TSEITIN --> LINEAR --> SAT_SOLVE
  end
  style CNFValidation fill:#0f172a,stroke:#3b82f6""",

    ("9", 2, "Visualization"): """graph TD
  subgraph DPLLSatSolver ["DPLL Decision Tree"]
    INIT["CNF Clause Database"]
    UP["Unit Propagation: If clause has 1 unassigned literal, assign it True"]
    PLE["Pure Literal Elimination: If literal has single polarity across all clauses"]
    DECIDE["Decision Variable Selection & Branching"]
    INIT --> UP --> PLE --> DECIDE
    DECIDE -->|"Conflict"| BT["Backtrack to Previous Assignment"]
    DECIDE -->|"All Variables Assigned"| SAT["Return SAT Model"]
  end
  style DPLLSatSolver fill:#1e1b4b,stroke:#6366f1""",

    ("9", 2, "Architecture Diagram"): """graph TD
  subgraph CDCLArchitecture ["Modern CDCL (Conflict-Driven Clause Learning) SAT Solver"]
    ASSIGN["Decision Engine: VSIDS Variable Activity Heuristic"]
    BCP["Two-Watched Literals Boolean Constraint Propagation (BCP)"]
    CONF["Conflict Analysis & Implication Graph (UIP Cut)"]
    LEARN["Learn Conflict Clause & Non-Chronological Backjump"]
    ASSIGN --> BCP
    BCP -->|"No Conflict"| ASSIGN
    BCP -->|"Conflict"| CONF --> LEARN --> BCP
  end
  style CDCLArchitecture fill:#064e3b,stroke:#10b981""",

    ("9", 3, "Visualization"): """graph TD
  subgraph ResolutionRefutation ["Resolution Refutation Theorem Proving"]
    KB["Knowledge Base Clauses"]
    NEG["Negated Query Clause ¬Query"]
    RESOLVE["Resolution Rule: (A ∨ P) and (B ∨ ¬P) derives (A ∨ B)"]
    EMPTY["Empty Clause □ (Contradiction Found!)"]
    KB & NEG --> RESOLVE --> EMPTY
  end
  style ResolutionRefutation fill:#1e1b4b,stroke:#6366f1""",

    ("9", 3, "Architecture Diagram"): """graph LR
  subgraph SoundCompleteness ["Logical Invariant Guarantees"]
    SOUND["Soundness: Any derived formula is mathematically entailed"]
    COMPL["Refutation Completeness: If KB |= α, resolution will ALWAYS find □"]
    SOUND & COMPL --> PROOF["Formal Safety Certificate Verified"]
  end
  style SoundCompleteness fill:#0f172a,stroke:#3b82f6""",

    # Case 10: First-Order Logic
    ("10", 0, "Visualization"): """graph LR
  subgraph FirstOrderLogic ["First-Order Logic Grammar Architecture"]
    CONST["Constants: Robot1, StationB"]
    VAR["Variables: ?x, ?y"]
    FUNC["Functions: MotherOf(?x), Position(?r)"]
    PRED["Predicates: Connected(?a, ?b), FaultDetected(?dev)"]
    QUANT["Quantifiers: ∀ (Universal), ∃ (Existential)"]
    CONST & VAR & FUNC --> PRED --> QUANT
  end
  style FirstOrderLogic fill:#1e1b4b,stroke:#6366f1""",

    ("10", 0, "Architecture Diagram"): """graph TD
  subgraph FOLSemanticInterpretation ["First-Order Logic Model Semantics"]
    DOM["Domain of Discourse Δ (Concrete Real-World Objects)"]
    INTERP["Interpretation Function I: Maps Constant -> Object, Predicate -> Relation"]
    SAT["Truth Value Evaluation: Sentence holds in Model M = (Δ, I)"]
    DOM --> INTERP --> SAT
  end
  style FOLSemanticInterpretation fill:#0f172a,stroke:#3b82f6""",

    ("10", 1, "Visualization"): """graph TD
  subgraph UnificationPipeline ["Unification Algorithm Flow"]
    T1["Term 1: Connects(RouterA, ?x)"]
    T2["Term 2: Connects(?y, ServerRack3)"]
    OCCUR["Occur Check: Ensure variable does not occur inside binding term"]
    MGU["Most General Unifier θ = {?x: ServerRack3, ?y: RouterA}"]
    T1 & T2 --> OCCUR --> MGU
    MGU --> UNIFIED["Connects(RouterA, ServerRack3)"]
  end
  style UnificationPipeline fill:#1e1b4b,stroke:#6366f1""",

    ("10", 1, "Architecture Diagram"): """graph LR
  subgraph UnificationMechanics ["Substitution & Composition Algebra"]
    SUB1["Substitution θ1 = {?x: f(?y)}"]
    SUB2["Substitution θ2 = {?y: ConstantA}"]
    COMP["Composition θ1 ∘ θ2 = {?x: f(ConstantA), ?y: ConstantA}"]
    SUB1 & SUB2 --> COMP
  end
  style UnificationMechanics fill:#0f172a,stroke:#3b82f6""",

    ("10", 2, "Visualization"): """graph TD
  subgraph ForwardChaining ["Forward Chaining Engine"]
    KB["Definite Horn Clause Knowledge Base"]
    FACTS["Working Memory: Known Ground Facts"]
    MATCH["Unify Fact Premises with Rule Antecedents"]
    FIRE["Add Inferred Consequents to Working Memory"]
    KB & FACTS --> MATCH --> FIRE --> FACTS
  end
  style ForwardChaining fill:#1e1b4b,stroke:#6366f1""",

    ("10", 2, "Architecture Diagram"): """graph LR
  subgraph ReteNetwork ["Rete Fast Pattern-Matching Network"]
    ROOT["Root Token Stream (Working Memory Changes)"]
    ALPHA["Alpha Nodes: 1-Input Intra-Element Feature Tests"]
    BETA["Beta Nodes: 2-Input Inter-Element Variable Joins"]
    AGENDA["Conflict Resolution Agenda: Fire Activated Rules"]
    ROOT --> ALPHA --> BETA --> AGENDA
  end
  style ReteNetwork fill:#064e3b,stroke:#10b981""",

    ("10", 3, "Visualization"): """graph TD
  subgraph BackwardChaining ["Backward Chaining Proof Tree"]
    GOAL["Top Query Goal: SafeToLaunch(Rocket)"]
    SUB1["Subgoal 1: WeatherClear(LaunchPad)"]
    SUB2["Subgoal 2: TelemetryNominal(Rocket)"]
    GOAL --> SUB1 & SUB2
    FACT1["Fact in KB: GroundSensor(LaunchPad) == Clear"]
    FACT2["Fact in KB: AvionicsCheck(Rocket) == Pass"]
    SUB1 --> FACT1
    SUB2 --> FACT2
  end
  style BackwardChaining fill:#1e1b4b,stroke:#6366f1""",

    ("10", 3, "Architecture Diagram"): """graph TD
  subgraph SLDProofArchitecture ["SLD Resolution (Selective Linear Definite)"]
    GOAL_STACK["Goal Stack (Subgoals to Resolve)"]
    RULE_INDEX["Predicate Index Table (Indexed by Predicate Name & Arity)"]
    UNIFY["Unify Selected Goal with Rule Head"]
    PUSH["Replace Goal with Rule Body Subgoals & Apply Substitution θ"]
    GOAL_STACK & RULE_INDEX --> UNIFY --> PUSH --> GOAL_STACK
  end
  style SLDProofArchitecture fill:#0f172a,stroke:#3b82f6""",

    # Case 11: Classical Planning
    ("11", 0, "Visualization"): """graph LR
  subgraph PDDLSchema ["PDDL Action Representation: PickUp(robot, part, bin)"]
    PARAMS["Parameters: ?r - robot, ?p - part, ?b - bin"]
    PRECOND["Preconditions: At(?r, ?b) ∧ InBin(?p, ?b) ∧ HandEmpty(?r)"]
    EFFECTS["Effects: Add { Holding(?r, ?p) } Delete { InBin(?p, ?b), HandEmpty(?r) }"]
    PARAMS --> PRECOND --> EFFECTS
  end
  style PDDLSchema fill:#1e1b4b,stroke:#6366f1""",

    ("11", 0, "Architecture Diagram"): """graph TD
  subgraph AutomatedPlanningFramework ["Classical Planning State Transition System Σ = (S, A, γ)"]
    S["State Space S: Sets of Ground Atomic Propositions"]
    A["Action Space A: Ground Action Instances with Precond/Effect"]
    GAMMA["State Transition Function: γ(s, a) = (s \\ Delete(a)) ∪ Add(a)"]
    S & A --> GAMMA --> S
  end
  style AutomatedPlanningFramework fill:#0f172a,stroke:#3b82f6""",

    ("11", 1, "Visualization"): """graph TD
  subgraph SearchDirections ["Planning Search Direction Topologies"]
    PROG["Forward State Progression: Expand actions from S0 toward Goal G"]
    REG["Backward Goal Regression: Regress subgoals from G back toward S0"]
    BIDIR["Bidirectional Search: Frontier intersection reduces branching"]
    PROG & REG --> BIDIR
  end
  style SearchDirections fill:#1e1b4b,stroke:#6366f1""",

    ("11", 1, "Architecture Diagram"): """graph LR
  subgraph RegressionMechanics ["Goal Regression Invariant"]
    GOAL["Current Subgoal Set G'"]
    ACTION["Relevant Action a (Adds at least one literal in G')"]
    CONSIST["Consistency Check: Action must not delete any literal in G'"]
    REGRESSED["Regressed Goal: (G' \\ Add(a)) ∪ Preconditions(a)"]
    GOAL & ACTION --> CONSIST --> REGRESSED
  end
  style RegressionMechanics fill:#0f172a,stroke:#3b82f6""",

    ("11", 2, "Visualization"): """graph LR
  subgraph PlanningGraph ["Graphplan Alternating Graph Levels"]
    P0["Proposition Level P0"]
    A0["Action Level A0 (Actions + No-Op Persistences)"]
    P1["Proposition Level P1"]
    MUTEX["Mutex Relations: Inconsistent Effects, Interference, Competing Needs"]
    P0 --> A0 --> MUTEX --> P1
  end
  style PlanningGraph fill:#1e1b4b,stroke:#6366f1""",

    ("11", 2, "Architecture Diagram"): """graph TD
  subgraph MutexAnalysis ["Graphplan Mutual Exclusion (Mutex) Conditions"]
    M1["Inconsistent Effects: One action negates an effect of another"]
    M2["Interference: One action negates a precondition of another"]
    M3["Competing Needs: Preconditions of two actions are mutually exclusive"]
    M4["Inconsistent Support: Every action pair achieving two propositions is mutex"]
    M1 & M2 & M3 --> ACTION_MUTEX["Action Mutex"]
    M4 --> PROP_MUTEX["Proposition Mutex"]
  end
  style MutexAnalysis fill:#0f172a,stroke:#3b82f6""",

    ("11", 3, "Visualization"): """graph TD
  subgraph FastForwardHeuristic ["Delete-Relaxed Planning Graph (h_FF)"]
    STATE["Current Search State S"]
    RELAX["Delete-Relaxation: Remove all Delete-Lists from actions"]
    EXPAND["Expand Relaxed Graph until Goal Propositions achieved"]
    COUNT["Extract Relaxed Plan: Count actions -> Heuristic value h_FF(S)"]
    STATE --> RELAX --> EXPAND --> COUNT
  end
  style FastForwardHeuristic fill:#1e1b4b,stroke:#6366f1""",

    ("11", 3, "Architecture Diagram"): """graph LR
  subgraph IndustrialPlanningDispatcher ["Enterprise Automated Planning Engine"]
    PDDL["PDDL Domain & Problem Files"]
    GROUND["Fast Downward / SAS+ Grounding Engine"]
    SEARCH["A* Search Guided by LM-Cut or h_FF Heuristic"]
    PLAN["Optimal / Satisficing Action Plan Sequence"]
    DISPATCH["Robotic Workcell Action Dispatcher & Monitor"]
    PDDL --> GROUND --> SEARCH --> PLAN --> DISPATCH
  end
  style IndustrialPlanningDispatcher fill:#064e3b,stroke:#10b981""",

    # Case 12: Probability & Uncertainty
    ("12", 0, "Visualization"): """graph TD
  subgraph UncertaintyTypes ["Engineering Uncertainty Classification"]
    U["Observed Sensor & Process Uncertainty"]
    ALEA["Aleatoric: Inherent Physical Randomness (Sensor Thermal Noise)"]
    EPIS["Epistemic: Model Knowledge Deficit (Unmeasured Variables)"]
    U --> ALEA & EPIS
    M1["Mitigate via Stochastic Filtering & Probabilistic Bounds"]
    M2["Mitigate via Calibration & Additional Training Samples"]
    ALEA --> M1
    EPIS --> M2
  end
  style UncertaintyTypes fill:#1e1b4b,stroke:#6366f1""",

    ("12", 0, "Architecture Diagram"): """graph LR
  subgraph BeliefTrackingPipeline ["Probabilistic Belief State Estimator"]
    PRIOR["Prior Belief b(s)"]
    ACTION["Action Executed a"]
    PRED["Motion / Dynamics Model: P(s' | s, a)"]
    OBS["Sensor Observation z"]
    LIKELIHOOD["Sensor Likelihood Model: P(z | s')"]
    POST["Updated Posterior Belief b'(s')"]
    PRIOR & ACTION --> PRED
    PRED & OBS & LIKELIHOOD --> POST
  end
  style BeliefTrackingPipeline fill:#0f172a,stroke:#3b82f6""",

    ("12", 1, "Visualization"): """graph TD
  subgraph RandomVariables ["Random Variables & Distribution Forms"]
    RV["Random Variable X: Function mapping sample space Ω -> ℝ"]
    DISC["Discrete RV: PMF P(X = x), e.g. Bernoulli, Poisson"]
    CONT["Continuous RV: PDF f(x), e.g. Gaussian Normal, Exponential"]
    RV --> DISC & CONT
  end
  style RandomVariables fill:#1e1b4b,stroke:#6366f1""",

    ("12", 1, "Architecture Diagram"): """graph LR
  subgraph MomentsPipeline ["Statistical Parameter Estimation Engine"]
    SAMPLES["Sensor Telemetry Stream x_1 ... x_N"]
    MEAN["Sample Mean μ = (1/N) Σ x_i"]
    VAR["Sample Variance σ² = (1/(N-1)) Σ (x_i - μ)²"]
    GAUSS["Parametric Normal Model N(μ, σ²)"]
    CI["95% Confidence Interval: [μ - 1.96σ, μ + 1.96σ]"]
    SAMPLES --> MEAN & VAR --> GAUSS --> CI
  end
  style MomentsPipeline fill:#0f172a,stroke:#3b82f6""",

    ("12", 2, "Visualization"): """graph TD
  subgraph ProbabilityRules ["Foundational Probability Axioms & Factorizations"]
    JOINT["Joint Probability: P(A, B)"]
    COND["Conditional Probability: P(A | B) = P(A, B) / P(B)"]
    PROD["Product Rule: P(A, B) = P(A | B) · P(B)"]
    CHAIN["Chain Rule: P(X1...Xn) = Π P(Xi | Parents(Xi))"]
    JOINT --> COND --> PROD --> CHAIN
  end
  style ProbabilityRules fill:#1e1b4b,stroke:#6366f1""",

    ("12", 2, "Architecture Diagram"): """graph LR
  subgraph IndependenceInference ["Independence & Conditional Independence Flow"]
    IND["Marginal Independence: P(X, Y) = P(X) · P(Y)"]
    COND_IND["Conditional Independence: P(X, Y | Z) = P(X | Z) · P(Y | Z)"]
    FACTOR["Graph Factorization: Reduces Parameter Complexity from O(2^n) to O(n · 2^k)"]
    IND & COND_IND --> FACTOR
  end
  style IndependenceInference fill:#064e3b,stroke:#10b981""",

    # Case 20: Reinforcement Learning
    ("20", 0, "Visualization"): """graph LR
  subgraph Agent ["Reinforcement Learning Agent"]
    POL["Policy π(a | s)"]
    LEARN["Value Iteration & TD Update Engine"]
    POL --> ACT["Action A(t)"]
  end
  subgraph Env ["Environment (MDP Dynamics)"]
    STATE["Current State S(t)"]
    TRANS["Transition Function P(S(t+1) | S(t), A(t))"]
    REW["Reward Model R(S(t), A(t))"]
  end
  ACT --> TRANS --> STATE
  TRANS -->|"S(t+1)"| LEARN & POL
  TRANS --> REW -->|"R(t+1)"| LEARN
  style Agent fill:#1e1b4b,stroke:#6366f1
  style Env fill:#0f172a,stroke:#3b82f6""",

    ("20", 1, "Visualization"): """graph TD
  subgraph ValueFunctions ["Value Function Hierarchy"]
    STATE_VAL["State-Value Function V(s): Expected Return from state s under policy π"]
    ACTION_VAL["Action-Value Function Q(s, a): Expected Return taking action a in state s"]
    OPT_Q["Optimal Q*(s, a) = max_π Q^π(s, a)"]
    STATE_VAL --> ACTION_VAL --> OPT_Q
  end
  style ValueFunctions fill:#1e1b4b,stroke:#6366f1""",

    ("20", 1, "Architecture Diagram"): """graph LR
  subgraph QTableEngine ["Q-Table Lookup & Action Selection Pipeline"]
    OBS["Observe State S(t)"]
    INDEX["Lookup Row Q(S(t), ·) in Q-Table"]
    DECIDE["Greedy Policy: a* = argmax_a Q(S(t), a)"]
    EXEC["Send a* to Actuator Driver"]
    OBS --> INDEX --> DECIDE --> EXEC
  end
  style QTableEngine fill:#0f172a,stroke:#3b82f6""",

    ("20", 2, "Visualization"): """graph LR
  subgraph BellmanBackup ["Bellman Optimality Backup Diagram"]
    S["Current State s"]
    A["Action a"]
    R["Immediate Reward R"]
    SPRIME["Next State s'"]
    MAXQ["max_a' Q(s', a')"]
    S --> A --> R & SPRIME
    SPRIME --> MAXQ
  end
  style BellmanBackup fill:#1e1b4b,stroke:#6366f1""",

    ("20", 2, "Architecture Diagram"): """graph TD
  subgraph TDUpdatePipeline ["Temporal Difference Q-Learning Update"]
    TUPLE["Experience Step: (s, a, r, s')"]
    TARGET["Compute Bellman Target = r + γ · max_a' Q(s', a')"]
    ERROR["Compute TD Error δ = Target - Q(s, a)"]
    APPLY["Update Q(s, a) ← Q(s, a) + α · δ"]
    TUPLE --> TARGET --> ERROR --> APPLY
  end
  style TDUpdatePipeline fill:#064e3b,stroke:#10b981""",

    ("20", 3, "Visualization"): """graph TD
  subgraph ExplorationTradeoff ["Exploration vs Exploitation Trade-off"]
    DILEMMA["Agent Dilemma: Maximize current reward vs Learn better long-term actions"]
    EXPLORE["Exploration: Try novel actions to discover higher peaks"]
    EXPLOIT["Exploitation: Capitalize on known high-value actions"]
    DILEMMA --> EXPLORE & EXPLOIT
  end
  style ExplorationTradeoff fill:#1e1b4b,stroke:#6366f1""",

    ("20", 3, "Architecture Diagram"): """graph LR
  subgraph EpsilonScheduler ["Epsilon-Greedy Scheduler Architecture"]
    SAMPLE["Uniform Random Roll p ~ U(0, 1)"]
    CHECK{"Is p < ε ?"}
    SAMPLE --> CHECK
    CHECK -->|"Yes (Explore)"| RAND["Random Legal Action"]
    CHECK -->|"No (Exploit)"| GREEDY["argmax_a Q(s, a)"]
    DECAY["Decay Schedule: ε ← max(ε_min, ε · decay)"]
    RAND & GREEDY --> DECAY
  end
  style EpsilonScheduler fill:#0f172a,stroke:#3b82f6"""
}

# Count replacements
replaced = 0
for case_num, case in LEVEL_CONTENT.items():
    for ep_idx, ep in enumerate(case.get('episodes', [])):
        for b_idx, b in enumerate(ep.get('blocks', [])):
            if b.get('type') == 'visual':
                title = b.get('title', 'Architecture Diagram')
                code = b.get('code', '').strip()
                
                # Check if exact match in ARCHITECTURES
                if (case_num, ep_idx, title) in ARCHITECTURES:
                    b['code'] = ARCHITECTURES[(case_num, ep_idx, title)]
                    b['height'] = None # Allow dynamic snug height
                    replaced += 1
                    print(f"Upgraded Case {case_num} Ep {ep_idx} [{title}]")
                elif 'Empty Diagram' in code:
                    # Provide default rich diagram based on episode title
                    ep_title = ep.get('title', 'Engineering Pipeline')
                    b['code'] = f"""graph LR
  subgraph Ingestion ["Telemetry & State Stream"]
    S1["Raw Feature Stream"]
    S2["Historical Baseline Parameters"]
  end
  subgraph CoreEngine ["{ep_title} Processing Engine"]
    P1["Invariant State Filter"]
    P2["Mathematical Transformation Matrix"]
    P1 --> P2
  end
  subgraph OutputControl ["Action & Control Verification"]
    OUT1["Validated Output Metric"]
    OUT2["Safety Guardrail Monitor"]
    P2 --> OUT1 --> OUT2
  end
  Ingestion --> CoreEngine
  style Ingestion fill:#0f172a,stroke:#3b82f6
  style CoreEngine fill:#1e1b4b,stroke:#6366f1
  style OutputControl fill:#064e3b,stroke:#10b981"""
                    b['title'] = f"{ep_title} Architecture"
                    b['height'] = None
                    replaced += 1
                    print(f"Replaced Empty Diagram in Case {case_num} Ep {ep_idx}")

print(f"Total upgraded diagrams: {replaced}")

# Check Case 2 Ep 0 Block 2 to remove hardcoded 280 height
try:
    if 'height' in LEVEL_CONTENT['2']['episodes'][0]['blocks'][2]:
        del LEVEL_CONTENT['2']['episodes'][0]['blocks'][2]['height']
        print("Removed explicit height 280 from Case 2 Ep 0 Block 2!")
except Exception as e:
    print("Case 2 height removal:", e)

# Write back LEVEL_CONTENT
dumped = json.dumps(LEVEL_CONTENT, indent=4, ensure_ascii=False)
dumped = re.sub(r':\s*true\b', ': True', dumped)
dumped = re.sub(r':\s*false\b', ': False', dumped)
dumped = re.sub(r':\s*null\b', ': None', dumped)

with open('/Users/aadarshamahato/Downloads/LEARNING_PLATFORM/ai_story_lab/level_content.py', 'w', encoding='utf-8') as f:
    f.write("# Master Curriculum Database for AI Story Lab\n")
    f.write("LEVEL_CONTENT = \\\n")
    f.write(dumped)
    f.write("\n")

print("Successfully updated level_content.py!")
