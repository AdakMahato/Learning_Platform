import json
import re

print("Loading level_content...")
with open('/Users/aadarshamahato/Downloads/LEARNING_PLATFORM/ai_story_lab/level_content.py', 'r', encoding='utf-8') as f:
    text = f.read()

ns = {}
exec(text, ns)
LEVEL_CONTENT = ns['LEVEL_CONTENT']

ARCHITECTURES_PART2 = {
    # Case 12 Ep 3
    ("12", 3, "Visualization"): """graph TD
  subgraph Sensors ["Autonomous Telemetry Inputs"]
    CAM["RGB Camera (Object Bounding Boxes)"]
    LIDAR["LiDAR Point Cloud (3D Spatial Depth)"]
    RADAR["Doppler Radar (Velocity & Range)"]
  end
  subgraph Fusion ["Sensor Fusion Engine"]
    SYNC["Spatial-Temporal Synchronization"]
    EST["Fused Kinematic State Vector [x, y, z, v_x, v_y]"]
    CAM & LIDAR & RADAR --> SYNC --> EST
  end
  style Sensors fill:#0f172a,stroke:#3b82f6
  style Fusion fill:#1e1b4b,stroke:#6366f1""",

    # Case 13
    ("13", 0, "Visualization"): """graph LR
  subgraph Priors ["Prior & Likelihood Models"]
    P["Prior Probability P(H): Historical Baseline"]
    L["Likelihood P(E | H): Physical Sensor Model"]
  end
  subgraph Evidence ["Marginal Evidence"]
    E["Total Probability P(E) = Σ P(E | H_i) P(H_i)"]
    P & L --> E
  end
  subgraph Posterior ["Posterior Belief Output"]
    POST["Posterior P(H | E) = [P(E | H) · P(H)] / P(E)"]
    E --> POST
  end
  style Priors fill:#0f172a,stroke:#3b82f6
  style Evidence fill:#1e1b4b,stroke:#6366f1
  style Posterior fill:#064e3b,stroke:#10b981""",

    ("13", 0, "Architecture Diagram"): """graph TD
  subgraph HypothesisLoop ["Bayesian Diagnostic Inference Engine"]
    HYPO["Hypotheses H = {Healthy, Sensor_Fault, Component_Degradation}"]
    OBS["Observe Incoming Telemetry Vector E"]
    BAYES["Compute Posterior via Bayes Rule for each H_i"]
    MAP["Maximum A Posteriori (MAP) Decision: argmax_H P(H | E)"]
    HYPO & OBS --> BAYES --> MAP
  end
  style HypothesisLoop fill:#1e1b4b,stroke:#6366f1""",

    ("13", 1, "Visualization"): """graph TD
  subgraph Population ["Total Patient Cohort (N = 100,000)"]
    INFECT["True Disease Prevalence: P(D) = 0.1% (100 patients)"]
    HEALTHY["Healthy Population: P(¬D) = 99.9% (99,900 patients)"]
  end
  subgraph TestResults ["Diagnostic Screening Test (99% Sensitivity, 95% Specificity)"]
    TP["True Positives: 99 patients"]
    FP["False Positives (5% of 99,900): 4,995 patients!"]
    INFECT --> TP
    HEALTHY --> FP
  end
  subgraph TrueRisk ["Real Clinical Posterior P(D | +)"]
    POST["True Positive Rate = 99 / (99 + 4995) ≈ 1.94%!"]
    TP & FP --> POST
  end
  style Population fill:#0f172a,stroke:#3b82f6
  style TestResults fill:#312e81,stroke:#818cf8
  style TrueRisk fill:#064e3b,stroke:#10b981""",

    ("13", 1, "Architecture Diagram"): """graph LR
  subgraph BaseRateAnalysis ["Base Rate Fallacy Engineering Guardrail"]
    BASE["Base Rate P(Fault) << 1%"]
    TEST["Sensor False Positive Rate FPR > Base Rate"]
    RISK["High False Alarm Ratio in Automated Anomaly Alerting"]
    FIX["Mitigation: Sequential Multi-Sensor Bayesian Confirmation"]
    BASE & TEST --> RISK --> FIX
  end
  style BaseRateAnalysis fill:#0f172a,stroke:#3b82f6""",

    ("13", 2, "Architecture Diagram"): """graph LR
  subgraph JointVsFactored ["Full Joint vs Factored Distribution Scaling"]
    JOINT["Full Joint Table: 2^N Parameters (Combinatorial Explosion)"]
    COND_IND["Conditional Independence Assertions"]
    FACTOR["Factored Bayes Network: O(N · 2^k) Parameters (k << N)"]
    JOINT --> COND_IND --> FACTOR
  end
  style JointVsFactored fill:#1e1b4b,stroke:#6366f1""",

    # Case 14
    ("14", 0, "Architecture Diagram"): """graph TD
  subgraph Causes ["Root / Exogenous Variables"]
    B["Burglary P(B)"]
    E["Earthquake P(E)"]
  end
  subgraph Intermediate ["Mediating Evidence Variables"]
    A["Alarm System P(A | B, E)"]
    B & E --> A
  end
  subgraph SensorAlerts ["Observational Effects"]
    J["JohnCalls P(J | A)"]
    M["MaryCalls P(M | A)"]
    A --> J & M
  end
  style Causes fill:#0f172a,stroke:#3b82f6
  style Intermediate fill:#1e1b4b,stroke:#6366f1
  style SensorAlerts fill:#064e3b,stroke:#10b981""",

    ("14", 1, "Visualization"): """graph LR
  subgraph Chain ["1. Causal Chain: X -> Y -> Z"]
    C1["X independent of Z given Y (Y blocks path)"]
  end
  subgraph Fork ["2. Common Cause: X <- Y -> Z"]
    F1["X independent of Z given Y (Common cause observed)"]
  end
  subgraph Collider ["3. Collider: X -> Y <- Z"]
    COL1["X independent of Z when Y is UN-observed"]
    COL2["Observing Y opens path!"]
    COL1 --> COL2
  end
  style Chain fill:#0f172a,stroke:#3b82f6
  style Fork fill:#1e1b4b,stroke:#6366f1
  style Collider fill:#064e3b,stroke:#10b981""",

    ("14", 1, "Architecture Diagram"): """graph TD
  subgraph DSeparationEngine ["D-Separation Independence Query Engine"]
    GRAPH["Directed Acyclic Graph Topology G"]
    SETS["Disjoint Variable Sets X, Y and Evidence Z"]
    TRAIL["Active Trail Search (Blocked vs Unblocked Paths)"]
    RESULT["Output: Conditional Independence Holds X ⊥ Y | Z"]
    GRAPH & SETS --> TRAIL --> RESULT
  end
  style DSeparationEngine fill:#1e1b4b,stroke:#6366f1""",

    ("14", 2, "Architecture Diagram"): """graph LR
  subgraph FactorOps ["Variable Elimination Pipeline"]
    FACT["Extract CPT Factors φ_1 ... φ_m"]
    PROD["Pointwise Factor Product: Combine factors mentioning Z"]
    SUM["Marginalization (Sum-out Z): φ_new = Σ_z φ_prod"]
    NORM["Normalize Final Query Distribution"]
    FACT --> PROD --> SUM --> NORM
  end
  style FactorOps fill:#1e1b4b,stroke:#6366f1""",

    ("14", 3, "Visualization"): """graph TD
  subgraph MonteCarloApprox ["Monte Carlo Approximate Inference"]
    BN["Bayesian Belief Network G"]
    SAMPLE["Forward / Likelihood-Weighted Sampling Engine"]
    TUPLES["Generate N Monte Carlo Realization Vectors"]
    ESTIMATE["Posterior Probability Estimation: Counts / Total Weight"]
    BN --> SAMPLE --> TUPLES --> ESTIMATE
  end
  style MonteCarloApprox fill:#1e1b4b,stroke:#6366f1""",

    ("14", 3, "Architecture Diagram"): """graph TD
  subgraph MCMCGibbs ["Gibbs Sampling MCMC Engine"]
    INIT["Initialize All Non-Evidence Variables Randomly"]
    SELECT["Select Variable X_i at Random"]
    SAMPLE["Sample new x_i ~ P(X_i | MarkovBlanket(X_i))"]
    RECORD["Record State Vector after Burn-in Period"]
    INIT --> SELECT --> SAMPLE --> RECORD --> SELECT
  end
  style MCMCGibbs fill:#0f172a,stroke:#3b82f6""",

    # Case 15
    ("15", 0, "Visualization"): """graph TD
  subgraph UtilityFoundation ["Utility Function Mapping"]
    OUTCOME["Physical Engineering State S"]
    UTIL["Utility Function U(S) ∈ ℝ (Captures Value, Cost, Risk)"]
    PREF["Preferences: S1 ≻ S2 iff U(S1) > U(S2)"]
    OUTCOME --> UTIL --> PREF
  end
  style UtilityFoundation fill:#1e1b4b,stroke:#6366f1""",

    ("15", 0, "Architecture Diagram"): """graph LR
  subgraph MEUEngine ["Maximum Expected Utility (MEU) Action Optimizer"]
    ACTIONS["Candidate Actions A = {a1, a2, a3}"]
    TRANS["Transition Dynamics P(s' | s, a)"]
    EU["Expected Utility: EU(a) = Σ P(s' | s, a) · U(s')"]
    BEST["Selected Action a* = argmax_a EU(a)"]
    ACTIONS & TRANS --> EU --> BEST
  end
  style MEUEngine fill:#0f172a,stroke:#3b82f6""",

    ("15", 1, "Visualization"): """graph LR
  subgraph RiskAversion ["Risk Aversion & Concave Utility Curves"]
    CONCAVE["Concave U(W): Diminishing Marginal Utility of Wealth (Risk Averse)"]
    LINEAR["Linear U(W): Expected Monetary Value Neutrality (Risk Neutral)"]
    CONVEX["Convex U(W): Risk Seeking (Prefers High-Variance Gambles)"]
    CONCAVE & LINEAR & CONVEX --> DESIGN["Select Appropriate Risk Profile for System"]
  end
  style RiskAversion fill:#1e1b4b,stroke:#6366f1""",

    ("15", 1, "Architecture Diagram"): """graph TD
  subgraph IndustrialRisk ["Industrial Risk Management Architecture"]
    HAZARD["Hazard Assessment & Fault Tree Analysis"]
    QUANT["Quantify Monetary Losses ($) and Safety Penalties"]
    UTILITY_DEF["Formulate Strict Safety-Constrained Utility Function"]
    POLICY["Deploy Risk-Averse Controller with Proven Safety Invariants"]
    HAZARD --> QUANT --> UTILITY_DEF --> POLICY
  end
  style IndustrialRisk fill:#064e3b,stroke:#10b981""",

    ("15", 2, "Visualization"): """graph TD
  subgraph DecisionNetwork ["Decision Network (Influence Diagram) Topology"]
    DEC["Decision Node □: Plant Cooling Throttle Level"]
    CHANCE["Chance Node ○: Reactor Temperature"]
    UTIL["Utility Node ◊: Net Operating Profit minus Heat Wear"]
    DEC --> CHANCE & UTIL
    CHANCE --> UTIL
  end
  style DecisionNetwork fill:#1e1b4b,stroke:#6366f1""",

    ("15", 2, "Architecture Diagram"): """graph LR
  subgraph DecisionNetInference ["Influence Diagram Evaluation Algorithm"]
    SET_DEC["Instantiate Decision Node d ∈ D"]
    PROP["Run Bayesian Belief Propagation on Chance Nodes"]
    EVAL_U["Compute Expected Value of Utility Node EU(d)"]
    ARGMAX["Select d* with Maximum Expected Utility"]
    SET_DEC --> PROP --> EVAL_U --> ARGMAX
  end
  style DecisionNetInference fill:#0f172a,stroke:#3b82f6""",

    ("15", 3, "Visualization"): """graph LR
  subgraph VPICalc ["Value of Perfect Information (VPI)"]
    PRIOR_EU["Current Optimal Expected Utility EU(α)"]
    POST_EU["Expected Utility Knowing Evidence E: Σ P(e) EU(α_e)"]
    VPI["VPI(E) = EU(α | E) - EU(α) (Non-Negative Invariant)"]
    PRIOR_EU & POST_EU --> VPI
  end
  style VPICalc fill:#1e1b4b,stroke:#6366f1""",

    # Case 16
    ("16", 2, "Visualization"): """graph LR
  subgraph FitTradeoff ["Generalization, Bias and Variance Spectrum"]
    UNDER["Underfitting (High Bias): Model Too Simple to Capture Patterns"]
    BALANCED["Optimal Generalization: Low Bias, Low Variance on Test Data"]
    OVER["Overfitting (High Variance): Model Memorizes Training Noise"]
    UNDER --> BALANCED --> OVER
  end
  style FitTradeoff fill:#1e1b4b,stroke:#6366f1""",

    # Case 17: KNN
    ("17", 1, "Visualization"): """graph TD
  subgraph MetricKNN ["K-Nearest Neighbors Classification Pipeline"]
    QUERY["Query Telemetry Sample x_new"]
    DIST["Compute Metric Distance to All N Training Points"]
    SORT["Sort & Extract K Smallest Distances"]
    VOTE["Majority Vote / Weighted Inverse Distance Scoring"]
    QUERY --> DIST --> SORT --> VOTE
  end
  style MetricKNN fill:#1e1b4b,stroke:#6366f1""",

    ("17", 2, "Visualization"): """graph TD
  subgraph KDTreeSearch ["KD-Tree O(log N) Space Partitioning Search"]
    ROOT["Root Node Split (Dimension 0: Temperature)"]
    L1["Left Branch (Dimension 1: Pressure)"]
    R1["Right Branch (Dimension 1: Pressure)"]
    ROOT --> L1 & R1
    BOUNDS["Hyper-Rectangle Bounding Box Distance Check"]
    L1 & R1 --> BOUNDS
  end
  style KDTreeSearch fill:#1e1b4b,stroke:#6366f1""",

    ("17", 3, "Visualization"): """graph LR
  subgraph DistanceMetrics ["Metric Space Distance Formulations"]
    EUCLID["Euclidean L2: d(x, y) = √ Σ (x_i - y_i)²"]
    MANHAT["Manhattan L1: d(x, y) = Σ |x_i - y_i|"]
    MINK["Minkowski Lp: d(x, y) = (Σ |x_i - y_i|^p)^(1/p)"]
    EUCLID & MANHAT --> MINK
  end
  style DistanceMetrics fill:#0f172a,stroke:#3b82f6""",

    ("17", 3, "Architecture Diagram"): """graph LR
  subgraph StandardizationPipeline ["Feature Normalization Architecture"]
    RAW["Raw Heterogeneous Sensor Feeds"]
    STD["Z-Score Standardization: z = (x - μ) / σ"]
    ROBUST["Robust Scaler: (x - Median) / IQR (Outlier Resistant)"]
    READY["Uniform Metric Feature Space for Distance-Based Models"]
    RAW --> STD & ROBUST --> READY
  end
  style StandardizationPipeline fill:#064e3b,stroke:#10b981""",

    # Case 18: Naive Bayes
    ("18", 0, "Visualization"): """graph TD
  subgraph NaiveBayesModel ["Naive Bayes Conditional Independence DAG"]
    C["Target Class C ∈ {Nominal, Warning, Critical}"]
    F1["Feature X1: Vibration"]
    F2["Feature X2: Current Draw"]
    F3["Feature X3: Acoustic Peak"]
    C --> F1 & F2 & F3
  end
  style NaiveBayesModel fill:#1e1b4b,stroke:#6366f1""",

    ("18", 0, "Architecture Diagram"): """graph LR
  subgraph NBInference ["Naive Bayes Scoring Pipeline"]
    FEATURES["Input Feature Vector X = [x1, x2, ... xd]"]
    PRIOR["Prior Probability Table P(C)"]
    LIKELIHOOD["Class-Conditional Likelihood Products Π P(x_i | C)"]
    POSTERIOR["Argmax Decision: c* = argmax_C P(C) · Π P(x_i | C)"]
    FEATURES & PRIOR --> LIKELIHOOD --> POSTERIOR
  end
  style NBInference fill:#0f172a,stroke:#3b82f6""",

    ("18", 1, "Visualization"): """graph LR
  subgraph TextVectorization ["Log & Telemetry Vectorization Pipeline"]
    RAW["Maintenance Incident Reports"]
    TOKEN["Tokenization & Stopword Elimination"]
    VOCAB["Vocabulary Index Mapping (Size |V|)"]
    VECTOR["Sparse Count / TF-IDF Feature Vector"]
    RAW --> TOKEN --> VOCAB --> VECTOR
  end
  style TextVectorization fill:#1e1b4b,stroke:#6366f1""",

    ("18", 1, "Architecture Diagram"): """graph TD
  subgraph TextClassifierArch ["Enterprise Fault Log Classifier"]
    STREAM["Log Ingestion Stream"]
    PREPROC["Text Preprocessor"]
    MULTINOMIAL["Multinomial Naive Bayes Model"]
    ALERT["Automated Severity Routing & Maintenance Ticket Generation"]
    STREAM --> PREPROC --> MULTINOMIAL --> ALERT
  end
  style TextClassifierArch fill:#064e3b,stroke:#10b981""",

    ("18", 2, "Visualization"): """graph LR
  subgraph LaplaceMechanism ["Additive Laplace Smoothing Engine"]
    RAW_RATIO["Raw Empirical Count: Count(w, c) / Total(c) (Prone to 0)"]
    SMOOTH["Laplace Smoothed: (Count(w, c) + 1) / (Total(c) + |V|)"]
    STABLE["Guarantees No Zero-Probability Catastrophic Collapse"]
    RAW_RATIO --> SMOOTH --> STABLE
  end
  style LaplaceMechanism fill:#1e1b4b,stroke:#6366f1""",

    ("18", 2, "Architecture Diagram"): """graph LR
  subgraph SmoothingComparison ["Smoothing Hyperparameter Tuning α"]
    LAPLACE["Laplace Smoothing: α = 1.0 (Standard Uniform Prior)"]
    LIDSTONE["Lidstone Smoothing: α = 0.1 (Less Prior Weight)"]
    CV["Tune α on Validation Set to Minimize Cross-Entropy Loss"]
    LAPLACE & LIDSTONE --> CV
  end
  style SmoothingComparison fill:#0f172a,stroke:#3b82f6""",

    ("18", 3, "Visualization"): """graph TD
  subgraph NBVariants ["Naive Bayes Architectural Variants"]
    GAUSS["Gaussian NB: Continuous Features with Normal P(x | C)"]
    MULTI["Multinomial NB: Discrete Word / Occurrence Counts"]
    BERN["Bernoulli NB: Binary Feature Presence / Absence {0, 1}"]
  end
  style NBVariants fill:#1e1b4b,stroke:#6366f1""",

    ("18", 3, "Architecture Diagram"): """graph LR
  subgraph ModelSelector ["Industrial Naive Bayes Deployment Selector"]
    SENSOR["Continuous Sensor Feeds -> Deploy Gaussian NB"]
    LOGS["Incident Text Logs -> Deploy Multinomial NB"]
    FLAGS["Binary Alarm Checklists -> Deploy Bernoulli NB"]
  end
  style ModelSelector fill:#064e3b,stroke:#10b981""",

    # Case 19: Decision Trees
    ("19", 0, "Visualization"): """graph TD
  subgraph RecursiveTree ["Decision Tree Recursive Partitioning"]
    ROOT["Root Split: Axis-Aligned Threshold Test x_j <= θ"]
    LEFT["Left Subtree Partition D_left"]
    RIGHT["Right Subtree Partition D_right"]
    ROOT --> LEFT & RIGHT
    LEAF1["Leaf Prediction Class A"]
    LEAF2["Leaf Prediction Class B"]
    LEFT --> LEAF1
    RIGHT --> LEAF2
  end
  style RecursiveTree fill:#1e1b4b,stroke:#6366f1""",

    ("19", 0, "Architecture Diagram"): """graph LR
  subgraph CARTArchitecture ["Classification and Regression Tree (CART) Engine"]
    DATA["Training Dataset D"]
    SCAN["Threshold Evaluator: Scan all sorted feature cut-points"]
    IMPURITY["Compute Split Criterion (Gini / Entropy / Variance)"]
    SPLIT["Execute Best Binary Split & Recurse Until Stopping Criteria"]
    DATA --> SCAN --> IMPURITY --> SPLIT
  end
  style CARTArchitecture fill:#0f172a,stroke:#3b82f6""",

    ("19", 1, "Visualization"): """graph LR
  subgraph EntropyReduction ["Information Gain & Shannon Entropy"]
    H_PARENT["Parent Dataset Entropy: H(D) = - Σ p_i · log2(p_i)"]
    H_CHILD["Weighted Children Entropy: H(D | A) = Σ (|D_v| / |D|) · H(D_v)"]
    IG["Information Gain: IG(D, A) = H(D) - H(D | A)"]
    H_PARENT & H_CHILD --> IG
  end
  style EntropyReduction fill:#1e1b4b,stroke:#6366f1""",

    ("19", 1, "Architecture Diagram"): """graph TD
  subgraph FeatureSelectionTree ["Tree-Based Feature Importance Ranking"]
    SPLITS["Collect All Decision Node Splits in Trained Tree"]
    WEIGHT["Weight Impurity Decrease by Proportion of Samples Reaching Node"]
    IMPORTANCE["Summed Feature Importance Vector (MDI: Mean Decrease Impurity)"]
    SPLITS --> WEIGHT --> IMPORTANCE
  end
  style FeatureSelectionTree fill:#064e3b,stroke:#10b981""",

    ("19", 2, "Visualization"): """graph LR
  subgraph SplitMetrics ["Impurity Function Properties"]
    GINI["Gini Impurity: 1 - Σ p_i² (Max = 0.5 for binary)"]
    ENTROPY["Entropy: - Σ p_i log2(p_i) (Max = 1.0 for binary)"]
    MISCLASS["Misclassification Rate: 1 - max(p_i)"]
    GINI & ENTROPY & MISCLASS --> PLOT["Both Gini & Entropy are strictly concave functions"]
  end
  style SplitMetrics fill:#0f172a,stroke:#3b82f6""",

    ("19", 2, "Architecture Diagram"): """graph TD
  subgraph PruningPipeline ["Cost-Complexity Tree Pruning (ccp_alpha)"]
    FULL["Fully Grown Overfitted Tree T_max"]
    COST["Cost Function: R_α(T) = R(T) + α · |T|"]
    PRUNE["Collapse Weak Branches Minimizing R_α on Validation Set"]
    OPTIMAL["Optimal Subtree with High Generalization"]
    FULL --> COST --> PRUNE --> OPTIMAL
  end
  style PruningPipeline fill:#1e1b4b,stroke:#6366f1""",

    ("19", 3, "Visualization"): """graph TD
  subgraph RandomTreeForest ["Random Forest Ensemble Architecture"]
    D["Training Data (N Samples, d Features)"]
    B1["Bootstrap Sample 1"]
    B2["Bootstrap Sample 2"]
    D --> B1 & B2
    T1["Tree 1 (Trained on m = √d Features)"]
    T2["Tree 2 (Trained on m = √d Features)"]
    B1 --> T1
    B2 --> T2
    VOTE["Ensemble Aggregate: Average Probabilities / Majority Vote"]
    T1 & T2 --> VOTE
  end
  style RandomTreeForest fill:#1e1b4b,stroke:#6366f1""",

    ("19", 3, "Architecture Diagram"): """graph LR
  subgraph OutOfBagValidation ["Out-of-Bag (OOB) Error Evaluation"]
    SAMPLES["Each Tree trained on ~63.2% of data"]
    OOB["Remaining ~36.8% Unseen Data acts as Free Validation Set"]
    METRIC["Compute Unbiased OOB Accuracy without Separate Holdout Set"]
    SAMPLES --> OOB --> METRIC
  end
  style OutOfBagValidation fill:#064e3b,stroke:#10b981""",

    # Case 21: Prolog
    ("21", 0, "Visualization"): """graph LR
  subgraph LogicEngine ["Prolog Declarative Knowledge Base"]
    FACTS["Ground Facts: component(motor_1, high_torque)."]
    RULES["Logic Rules: requires_maintenance(X) :- hours(X, H), H > 5000."]
  end
  subgraph QueryProcessor ["Inference & Goal Evaluation"]
    Q["Query: ?- requires_maintenance(motor_1)."]
    SEARCH["Resolution Engine with Pattern Matching"]
    Q & FACTS & RULES --> SEARCH
  end
  subgraph Result ["Truth Value"]
    ANS["Result: True / False with Variable Substitution"]
    SEARCH --> ANS
  end
  style LogicEngine fill:#0f172a,stroke:#3b82f6
  style QueryProcessor fill:#1e1b4b,stroke:#6366f1
  style Result fill:#064e3b,stroke:#10b981""",

    ("21", 0, "Architecture Diagram"): """graph TD
  subgraph WAMArchitecture ["Warren Abstract Machine (WAM) Execution Architecture"]
    REG["Argument & Temporary Registers A1..An"]
    HEAP["Global Heap: Compound Terms & Structures"]
    STACK["Local Stack: Environments & Choice Points for Backtracking"]
    TRAIL["Trail Stack: Tracks Variable Bindings to Undo on Backtrack"]
    REG & HEAP & STACK --> TRAIL
  end
  style WAMArchitecture fill:#1e1b4b,stroke:#6366f1""",

    ("21", 1, "Visualization"): """graph TD
  subgraph RuleStructure ["Horn Clause Structure"]
    HEAD["Rule Head (Conclusion)"]
    NECK[":- (Logical Implication 'If')"]
    BODY["Rule Body (Conjunctive Subgoals A ∧ B ∧ C)"]
    HEAD --> NECK --> BODY
  end
  style RuleStructure fill:#1e1b4b,stroke:#6366f1""",

    ("21", 1, "Architecture Diagram"): """graph LR
  subgraph SLDSearchSpace ["SLD Resolution Search Strategy"]
    GOAL["Current Goal Stack"]
    RULE_SELECT["Rule Selection Order: Top-to-Bottom in File"]
    GOAL_SELECT["Goal Selection Order: Left-to-Right in Clause Body"]
    DEPTH["Depth-First Search with Chronological Backtracking"]
    GOAL & RULE_SELECT & GOAL_SELECT --> DEPTH
  end
  style SLDSearchSpace fill:#0f172a,stroke:#3b82f6""",

    ("21", 2, "Visualization"): """graph LR
  subgraph UnifyTerms ["Prolog Unification Mechanics"]
    TERM1["Term 1: f(X, b)"]
    TERM2["Term 2: f(a, Y)"]
    MGU["MGU Substitution: {X = a, Y = b}"]
    UNIFIED["Unified Result: f(a, b)"]
    TERM1 & TERM2 --> MGU --> UNIFIED
  end
  style UnifyTerms fill:#1e1b4b,stroke:#6366f1""",

    ("21", 2, "Architecture Diagram"): """graph TD
  subgraph CutOperatorMechanism ["Prolog Cut Operator (!) Semantics"]
    CALL["Goal Invoked: parent_clause(X, Y)"]
    SUB1["Execute Subgoal 1"]
    CUT["Execute Cut (!) Operator"]
    SUB2["Execute Subgoal 2"]
    COMMIT["Freezes Choices: Prunes all alternative solutions for parent goal"]
    CALL --> SUB1 --> CUT --> SUB2
    CUT --> COMMIT
  end
  style CutOperatorMechanism fill:#064e3b,stroke:#10b981""",

    ("21", 3, "Visualization"): """graph TD
  subgraph ListStructure ["Prolog Recursive List Representation"]
    LIST["List: [10, 20, 30]"]
    CONS["Pair Cons Cell .(10, .(20, .(30, [])))"]
    HEAD["Head: 10"]
    TAIL["Tail: [20, 30]"]
    LIST --> CONS --> HEAD & TAIL
  end
  style ListStructure fill:#1e1b4b,stroke:#6366f1""",

    ("21", 3, "Architecture Diagram"): """graph LR
  subgraph AccumulatorPattern ["Tail-Recursive Accumulator Architecture"]
    CALL["sum_list(List, Result) :- sum_acc(List, 0, Result)."]
    ACC["sum_acc([H|T], Acc, Res) :- NewAcc is Acc + H, sum_acc(T, NewAcc, Res)."]
    BASE["sum_acc([], Final, Final)."]
    CALL --> ACC --> BASE
    TAIL_OPT["Enables Constant-Space Tail Call Optimization (TCO) in WAM"]
    BASE --> TAIL_OPT
  end
  style AccumulatorPattern fill:#064e3b,stroke:#10b981""",

    # Case 22: Expert Systems
    ("22", 0, "Architecture Diagram"): """graph TD
  subgraph ExpertSystemCore ["Enterprise Expert System Architecture"]
    USER["Plant Operator"]
    UI["Interactive Diagnosis Console & Explanation Viewer"]
    USER <--> UI
    UI <--> IE["Inference Engine (Forward/Backward Reasoning)"]
    KB["Rule Base (Domain Expert Heuristics)"]
    WM["Working Memory (Real-Time Sensor Telemetry)"]
    KB & WM <--> IE
  end
  style ExpertSystemCore fill:#1e1b4b,stroke:#6366f1""",

    ("22", 1, "Architecture Diagram"): """graph LR
  subgraph ProductionCycle ["Production System Match-Resolve-Act Cycle"]
    WM["Working Memory Telemetry Facts"]
    RULES["Production Rules: IF condition THEN action"]
    CONFLICT["Conflict Set: All Activated Rules"]
    RESOLVE["Conflict Resolution: Fire Highest Priority Rule"]
    WM & RULES --> CONFLICT --> RESOLVE --> WM
  end
  style ProductionCycle fill:#0f172a,stroke:#3b82f6""",

    ("22", 2, "Visualization"): """graph TD
  subgraph DiagnosticHypothesis ["Backward-Chaining Goal Tree"]
    HYP["Goal Hypothesis: Main Bearing Wear Failure"]
    RULE["Rule 104: IF HighVibration ∧ HighLubeTemp THEN Main Bearing Wear"]
    HYP --> RULE
    SUB1["Subgoal 1: Query Sensor for Vibration Amplitude"]
    SUB2["Subgoal 2: Query Sensor for Oil Sump Temperature"]
    RULE --> SUB1 & SUB2
  end
  style DiagnosticHypothesis fill:#1e1b4b,stroke:#6366f1""",

    ("22", 2, "Architecture Diagram"): """graph LR
  subgraph InteractiveDiagnosis ["Interactive Automated Diagnostic Interview"]
    GOAL["Inference Engine Seeks Unknown Evidence"]
    PROMPT["UI Prompts Operator: 'Is there audible cavitation at the impeller?'"]
    INPUT["Operator Enters Observation: Yes (Confidence: 0.8)"]
    UPDATE["Working Memory Updated -> Prunes Irrelevant Fault Branches"]
    GOAL --> PROMPT --> INPUT --> UPDATE
  end
  style InteractiveDiagnosis fill:#064e3b,stroke:#10b981""",

    ("22", 3, "Visualization"): """graph LR
  subgraph CertaintyFactorScale ["Certainty Factor Metric Scale (-1.0 to +1.0)"]
    FALSE["-1.0: Definitely False"]
    UNKNOWN["0.0: Unknown / No Evidence"]
    TRUE["+1.0: Definitely True"]
    FALSE --> UNKNOWN --> TRUE
  end
  style CertaintyFactorScale fill:#0f172a,stroke:#3b82f6""",

    ("22", 3, "Architecture Diagram"): """graph TD
  subgraph CFEngine ["MYCIN Certainty Factor Combination Engine"]
    RULE_CF["Evidence CF: CF(E) = min(CF(E1), CF(E2)) for AND"]
    INFERRED["Inferred Hypothesis CF: CF(H, E) = CF(E) · CF_rule"]
    COMBINE["Combine Multiple Independent Rules: CF1 + CF2 - (CF1 · CF2)"]
    RULE_CF --> INFERRED --> COMBINE
  end
  style CFEngine fill:#1e1b4b,stroke:#6366f1""",

    # Case 23: MLOps
    ("23", 0, "Architecture Diagram"): """graph LR
  subgraph CICD ["End-to-End Enterprise MLOps Architecture"]
    DATA["Data Validation (Great Expectations)"]
    TRAIN["Distributed Training & Ray Hyperband"]
    REG["Model Registry (MLflow Artifact Lineage)"]
    DEPLOY["Canary Release on Kubernetes (KServe)"]
    MONITOR["Prometheus / Evidently Drift Monitor"]
    DATA --> TRAIN --> REG --> DEPLOY --> MONITOR
    MONITOR -->|"Auto-Trigger Retraining"| TRAIN
  end
  style CICD fill:#1e1b4b,stroke:#6366f1""",

    ("23", 1, "Visualization"): """graph LR
  subgraph ServingModes ["Serving Architecture Modalities"]
    ONLINE["Real-Time Online Serving: Low-Latency REST/gRPC (< 20ms)"]
    BATCH["Batch Scoring: High-Throughput Distributed Spark / Ray"]
    STREAM["Event-Driven Stream Processing: Kafka + Flink"]
  end
  style ServingModes fill:#0f172a,stroke:#3b82f6""",

    ("23", 1, "Architecture Diagram"): """graph TD
  subgraph MicroserviceArch ["Containerized High-Availability Inference"]
    INGRESS["Ingress Controller & TLS Termination"]
    POD1["Triton Inference Container 1 (GPU Dynamic Batching)"]
    POD2["Triton Inference Container 2 (GPU Dynamic Batching)"]
    REDIS["Redis Result Cache (Sub-millisecond hit)"]
    INGRESS --> REDIS
    INGRESS --> POD1 & POD2
  end
  style MicroserviceArch fill:#1e1b4b,stroke:#6366f1""",

    ("23", 3, "Architecture Diagram"): """graph LR
  subgraph DriftDetection ["Production Drift Detection Engine"]
    REF["Baseline Reference Distribution P_ref(X)"]
    CURR["Live Production Telemetry Window P_live(X)"]
    KS["Kolmogorov-Smirnov & Wasserstein Distance Calculation"]
    ALERT["Alert On-Call ML Engineer & Schedule Pipeline Retraining"]
    REF & CURR --> KS --> ALERT
  end
  style DriftDetection fill:#064e3b,stroke:#10b981""",

    # Case 24: AI Safety & Ethics
    ("24", 0, "Architecture Diagram"): """graph LR
  subgraph QualityGates ["Production AI Release Certification Gates"]
    ACC["1. Performance: Test F1 > 0.92, Latency p95 < 30ms"]
    ROBUST["2. Robustness: Epsilon-Perturbation Error < 3%"]
    FAIR["3. Fairness: Disparate Impact Ratio >= 0.80"]
    GATE["Automated CI/CD Release Gate"]
    ACC & ROBUST & FAIR --> GATE
  end
  style QualityGates fill:#1e1b4b,stroke:#6366f1""",

    ("24", 1, "Visualization"): """graph TD
  subgraph BiasSources ["Algorithmic Bias Sources in Engineering AI"]
    HIST["Historical Bias: Past human discriminatory practices in dataset"]
    REP["Representation Bias: Underrepresented demographic or sensor operating modes"]
    MEAS["Measurement Bias: Inconsistent calibration across sensor brands"]
    HIST & REP & MEAS --> HARMFUL["Disparate Model Performance"]
  end
  style BiasSources fill:#0f172a,stroke:#3b82f6""",

    ("24", 1, "Architecture Diagram"): """graph LR
  subgraph FairnessInterventions ["Fairness Mitigation Intervention Points"]
    PRE["Pre-Processing: Re-weighting & Resampling"]
    IN["In-Processing: Adversarial Debiasing & Equalized Odds Constraints"]
    POST["Post-Processing: Group-Specific Decision Thresholding"]
    PRE --> IN --> POST
  end
  style FairnessInterventions fill:#1e1b4b,stroke:#6366f1""",

    ("24", 2, "Visualization"): """graph TD
  subgraph InterpretabilitySpectrum ["Interpretability vs Model Capacity Trade-off"]
    WHITE["Linear Models / Decision Stumps: High Interpretability, Lower Capacity"]
    MED["Ensembles / GAMs: Balanced Explainability"]
    BLACK["Deep Neural Networks: Maximum Expressivity, Black-Box Weights"]
    WHITE --> MED --> BLACK
  end
  style InterpretabilitySpectrum fill:#1e1b4b,stroke:#6366f1""",

    ("24", 2, "Architecture Diagram"): """graph LR
  subgraph SHAPArchitecture ["SHAP Feature Attribution Architecture"]
    SAMPLE["Input Telemetry Vector x"]
    KERNEL["KernelSHAP / TreeSHAP Sampling Engine"]
    SHAPLEY["Cooperative Game Theory Shapley Value Calculation"]
    FORCE["Force Plot & Feature Attribution Breakdown"]
    SAMPLE --> KERNEL --> SHAPLEY --> FORCE
  end
  style SHAPArchitecture fill:#064e3b,stroke:#10b981""",

    ("24", 3, "Visualization"): """graph LR
  subgraph AlignmentMechanisms ["Modern AI Alignment Stack"]
    PRETRAIN["Self-Supervised Representation Pre-training"]
    SFT["Supervised Fine-Tuning (Instruction Dataset)"]
    RLHF["Reinforcement Learning from Human Feedback (PPO / DPO)"]
    PRETRAIN --> SFT --> RLHF
  end
  style AlignmentMechanisms fill:#0f172a,stroke:#3b82f6"""
}

replaced = 0
for case_num, case in LEVEL_CONTENT.items():
    for ep_idx, ep in enumerate(case.get('episodes', [])):
        for b_idx, b in enumerate(ep.get('blocks', [])):
            if b.get('type') == 'visual':
                title = b.get('title', 'Architecture Diagram')
                if (case_num, ep_idx, title) in ARCHITECTURES_PART2:
                    b['code'] = ARCHITECTURES_PART2[(case_num, ep_idx, title)]
                    b['height'] = None
                    replaced += 1
                    print(f"Upgraded Case {case_num} Ep {ep_idx} [{title}]")

print(f"Total Part 2 upgraded diagrams: {replaced}")

dumped = json.dumps(LEVEL_CONTENT, indent=4, ensure_ascii=False)
dumped = re.sub(r':\s*true\b', ': True', dumped)
dumped = re.sub(r':\s*false\b', ': False', dumped)
dumped = re.sub(r':\s*null\b', ': None', dumped)

with open('/Users/aadarshamahato/Downloads/LEARNING_PLATFORM/ai_story_lab/level_content.py', 'w', encoding='utf-8') as f:
    f.write("# Master Curriculum Database for AI Story Lab\n")
    f.write("LEVEL_CONTENT = \\\n")
    f.write(dumped)
    f.write("\n")

print("Successfully written back level_content.py!")
