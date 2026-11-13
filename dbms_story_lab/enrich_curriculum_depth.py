import json
import os

path = '/Users/aadarshamahato/Downloads/LEARNING_PLATFORM/ai_story_lab/level_content.py'

# Load LEVEL_CONTENT
import sys
sys.path.insert(0, '/Users/aadarshamahato/Downloads/LEARNING_PLATFORM/ai_story_lab')
import level_content
lc = level_content.LEVEL_CONTENT

CASE_METADATA = {
    "0": {
        "title": "Case 00: The Machine That Couldn't Think",
        "why_default": "Case 00 focuses on foundational philosophy: proving why deterministic rule engines diverge from inductive learning.",
        "alts_default": "Classical Symbolic AI (GOFAI) vs Connectionist Neural Networks vs Behavior-Based Robotics."
    },
    "1": {
        "title": "Case 01: The Agent Awakens",
        "why_default": "**Algorithmic Mechanics:**\\nMaintains an internal state transition model $S_t = f(S_{t-1}, A_{t-1}, P_t)$, allowing the agent to reconstruct a consistent belief state in partially observable environments (POMDPs).",
        "alts_default": "#### 🔀 Candidate Architectural Alternatives\\n- **Table-Driven Agent:** $O(1)$ lookup, but memory is $O(|P|^T)$ exponential in time horizon $T$ (requires more entries than atoms in the universe).\\n- **Simple Reflex Agent:** $O(1)$ memory, but fails catastrophically in non-Markovian / partially observable environments due to infinite loops.\\n- **Goal-Based Agent:** Evaluates future consequence trajectories, providing greater flexibility at the cost of computational search latency.\\n- **Utility-Based Agent:** Computes continuous real-valued utilities under uncertainty, balancing multi-attribute trade-offs."
    },
    "2": {
        "title": "Case 02: The World Inside the Machine",
        "why_default": "**Algorithmic Mechanics:**\\nImplements a canonical state abstraction with immutable hashing and an explored set (closed list), ensuring each graph state is expanded at most once and eliminating infinite loops.",
        "alts_default": "#### 🔀 Candidate Architectural Alternatives\\n- **Tree Search (No Explored Set):** Minimal memory $O(b \\cdot d)$, but loops infinitely on cyclic graphs and re-explores duplicate states exponentially ($O(2^d)$).\\n- **Graph Search (With Explored Set):** Guarantees termination and bounds expansions to the total number of reachable states $|S|$, at the cost of storing all visited states in memory.\\n- **Bidirectional Search:** Runs simultaneous forward search from initial state and backward search from goal, reducing time complexity from $O(b^d)$ to $O(2 \\cdot b^{d/2})$."
    },
    "3": {
        "title": "Case 03: The Maze Without a Map",
        "why_default": "**Algorithmic Mechanics:**\\nA FIFO queue (`collections.deque`) ensures nodes are expanded strictly in order of non-decreasing path length. For unit step costs, this proves the shallowest goal is expanded first, guaranteeing optimality and completeness.",
        "alts_default": "#### 🔀 Candidate Architectural Alternatives\\n- **Depth-First Search (DFS):** Exceptional linear memory $O(b \\cdot m)$, but is incomplete in infinite state spaces and produces highly suboptimal paths.\\n- **Breadth-First Search (BFS):** Guarantees shortest path for unweighted steps, but exhausts RAM rapidly with exponential space complexity $O(b^d)$.\\n- **Iterative Deepening Search (IDDFS):** Combines the completeness/optimality of BFS with the linear space efficiency $O(b \\cdot d)$ of DFS by running bounded DFS iterations."
    },
    "4": {
        "title": "Case 04: The Search for the Better Path",
        "why_default": "**Algorithmic Mechanics:**\\nA* evaluates nodes using $f(n) = g(n) + h(n)$. With an admissible ($h(n) \\le h^*(n)$) and consistent ($h(n) \\le c(n, a, n') + h(n')$) heuristic, $f$-costs along any branch are monotonically non-decreasing, proving the first time a goal is popped from the min-heap, its cost is globally minimal.",
        "alts_default": "#### 🔀 Candidate Architectural Alternatives\\n- **Greedy Best-First Search:** Minimizes $h(n)$ only; expands fewer nodes in simple spaces, but is easily misled into long suboptimal paths.\\n- **Uniform Cost Search (Dijkstra):** Guarantees optimality without a heuristic ($h(n) = 0$), but explores in all directions blindly, expanding far more nodes.\\n- **IDA* (Iterative Deepening A*):** Uses $f$-cutoffs with DFS backtracks; reduces memory consumption to $O(b \\cdot d)$ while preserving optimality.\\n- **Weighted A* ($f = g + w \\cdot h$):** Speeds up search by prioritizing the heuristic ($w > 1$); bounds suboptimality to $\\le w \\times C^*$ while expanding up to 90% fewer nodes."
    },
    "5": {
        "title": "Case 05: The Heuristic Detective",
        "why_default": "**Algorithmic Mechanics:**\\nTaking the maximum of multiple admissible heuristics $\\max(h_1(n), h_2(n))$ produces a dominant admissible heuristic that expands fewer or equal nodes than either individual component without violating admissibility.",
        "alts_default": "#### 🔀 Candidate Architectural Alternatives\\n- **Pattern Databases:** Precomputes exact costs to subgoals in offline lookup tables; yields fast evaluation but requires significant RAM.\\n- **Relaxed Problem Generation:** Automatically derives admissible heuristics by removing physical problem constraints.\\n- **Landmark Heuristics:** Computes shortest paths to pre-selected landmark nodes and applies triangle inequality bounds."
    },
    "6": {
        "title": "Case 06: The Game of Minds",
        "why_default": "**Algorithmic Mechanics:**\\nAlpha-Beta maintains bounds $[\\alpha, \\beta]$ representing the best outcomes already guaranteed for MAX and MIN. When $\\alpha \\ge \\beta$, the current branch cannot affect the root decision, pruning up to $O(b^{d/2})$ of the game tree without loss of accuracy.",
        "alts_default": "#### 🔀 Candidate Architectural Alternatives\\n- **Standard Minimax:** Searches every node to depth $d$; optimal for zero-sum games with complete information, but intractable for high branching factors ($O(b^d)$).\\n- **Negamax:** Reformulation exploiting zero-sum duality $\\max(a, b) = -\\min(-a, -b)$, halving codebase complexity.\\n- **Monte Carlo Tree Search (MCTS):** Uses random rollouts with Upper Confidence Bound (UCT); scales to games like Go where heuristic static evaluation functions fail."
    },
    "7": {
        "title": "Case 07: The Impossible Puzzle",
        "why_default": "**Algorithmic Mechanics:**\\nAC-3 enforces arc consistency across all binary constraints $(X_i, X_j)$ before and during backtracking, removing values from domains that have no valid support and pruning exponential search spaces early.",
        "alts_default": "#### 🔀 Candidate Architectural Alternatives\\n- **Pure Backtracking:** Chronological backtracking without domain pruning; suffers catastrophic thrashing on dead ends.\\n- **Forward Checking (FC):** Prunes only neighboring variables immediately affected by assignment; faster per step than AC-3, but catches fewer cascading inconsistencies.\\n- **Min-Conflicts Local Search:** Iteratively re-assigns variables to minimize violated constraints; solves 1,000,000-Queens in seconds, but can get stuck in local optima."
    },
    "8": {
        "title": "Case 08: The Knowledge Vault",
        "why_default": "**Algorithmic Mechanics:**\\nDecouples declarative facts (subject-predicate-object triples) from procedural code, enabling inheritance along taxonomic graphs with $O(depth)$ lookup time.",
        "alts_default": "#### 🔀 Candidate Architectural Alternatives\\n- **Relational SQL Database:** Strict ACID transactions and fast joins, but rigid schemas make inheritance and recursive graph traversal awkward.\\n- **Semantic Web Ontologies (OWL/RDF):** Formal description logic standards supporting open-world assumption and automated reasoning.\\n- **Graph Neural Networks (GNN):** Continuous vector embeddings for knowledge graph completion; handles missing links well, but lacks deterministic proof capabilities."
    },
    "9": {
        "title": "Case 09: The Logic Engine",
        "why_default": "**Algorithmic Mechanics:**\\nResolution refutation adds the negated query $\\neg Q$ to the CNF knowledge base and resolves clauses until deriving the empty clause $\\Box$, proving entailment with refutation completeness.",
        "alts_default": "#### 🔀 Candidate Architectural Alternatives\\n- **Forward Chaining on Horn Clauses:** Linear time $O(KB)$, simple and data-driven, but only handles Horn clauses (at most one positive literal).\\n- **Backward Chaining (Goal-Driven):** Generates only queries relevant to the target goal, but vulnerable to infinite recursion on left-recursive rules.\\n- **Modern SAT Solvers (CDCL):** Conflict-Driven Clause Learning solves industrial propositional formulas with millions of variables."
    },
    "10": {
        "title": "Case 10: The Machine That Could Reason",
        "why_default": "**Algorithmic Mechanics:**\\nSuccessor-state axioms solve the classical Frame Problem by explicitly defining the exact conditions under which a fluent changes value between situations $Result(a, s)$.",
        "alts_default": "#### 🔀 Candidate Architectural Alternatives\\n- **Frame Axioms:** Explicitly states what does NOT change for every action; requires $O(|Actions| \\times |Fluents|)$ redundant axioms.\\n- **Event Calculus:** Formulates continuous time and state intervals rather than discrete situation trees.\\n- **Default Logic:** Non-monotonic logic that draws plausible conclusions in the absence of explicit contradictory evidence."
    },
    "11": {
        "title": "Case 11: The Planner",
        "why_default": "**Algorithmic Mechanics:**\\nSTRIPS operators represent actions via Preconditions, Add-lists, and Delete-lists, enabling backward regression from the goal to construct plans without evaluating irrelevant branches.",
        "alts_default": "#### 🔀 Candidate Architectural Alternatives\\n- **Forward State-Space Progression:** Evaluates actions from initial state forward; intuitive, but suffers from massive branching factor.\\n- **Graphplan:** Constructs polynomial-time planning graphs with mutual exclusion (mutex) links, finding shortest parallel plans.\\n- **SATPlan:** Encodes the planning problem into boolean SAT and leverages high-performance modern SAT solvers."
    },
    "12": {
        "title": "Case 12: The World That Keeps Changing",
        "why_default": "**Algorithmic Mechanics:**\\nApplies the axioms of probability to quantify uncertainty, ensuring coherent belief updates and satisfying Kolmogorov's foundation.",
        "alts_default": "#### 🔀 Candidate Architectural Alternatives\\n- **Full Joint Distribution Table:** Requires $2^n - 1$ parameters (exponential in number of variables $n$), making it intractable for real systems.\\n- **Fuzzy Logic:** Models degrees of truth rather than probability of occurrence; popular in industrial control, but lacks Bayesian consistency.\\n- **Dempster-Shafer Theory:** Explicitly represents epistemic ignorance by assigning belief to sets of outcomes rather than single events."
    },
    "13": {
        "title": "Case 13: The Probability Problem",
        "why_default": "**Algorithmic Mechanics:**\\nBayes' Theorem mathematically inverts diagnostic probabilities into causal probabilities $P(Cause|Effect) = \\frac{P(Effect|Cause)P(Cause)}{P(Effect)}$, correctly integrating prior base rates.",
        "alts_default": "#### 🔀 Candidate Architectural Alternatives\\n- **Maximum Likelihood Estimation (MLE):** Ignores the prior; optimal in the limit of infinite data, but severely biased by rare base rates on small samples.\\n- **Maximum A Posteriori (MAP):** Incorporates the prior but outputs a single point estimate rather than a full probability distribution.\\n- **Full Bayesian Estimation:** Integrates over all parameter uncertainties, providing confidence bounds at higher computational cost."
    },
    "14": {
        "title": "Case 14: The Bayesian Detective",
        "why_default": "**Algorithmic Mechanics:**\\nBayesian Networks exploit conditional independence in Directed Acyclic Graphs (DAGs) to factorize the joint distribution: $P(X_1...X_n) = \\prod P(X_i | Parents(X_i))$, reducing parameter storage from $O(2^n)$ to $O(n \\cdot 2^k)$.",
        "alts_default": "#### 🔀 Candidate Architectural Alternatives\\n- **Variable Elimination:** Exact inference algorithm using dynamic programming to sum out irrelevant variables, avoiding redundant subcomputations.\\n- **Markov Chain Monte Carlo (MCMC):** Approximate sampling method that scales to massive networks where exact inference is NP-hard.\\n- **Junction Tree Algorithm:** Exact message-passing on triangulated clique graphs for multi-connected networks."
    },
    "15": {
        "title": "Case 15: The Decision Maker",
        "why_default": "**Algorithmic Mechanics:**\\nComputes Maximum Expected Utility (MEU): $EU(a) = \\sum P(s'|a, s) U(s')$. The Von Neumann-Morgenstern theorem proves that any rational agent must maximize expected utility.",
        "alts_default": "#### 🔀 Candidate Architectural Alternatives\\n- **Minimax Decision Rule:** Chooses the action with the best worst-case outcome; extremely conservative and avoids catastrophic failure, but misses high-reward opportunities.\\n- **Satisficing (Simon):** Selects the first option meeting an acceptable threshold; faster in real-time embedded environments.\\n- **Value of Perfect Information (VPI):** Quantifies exactly how much an additional sensor measurement is worth before paying to acquire it."
    },
    "16": {
        "title": "Case 16: The Machine That Learns",
        "why_default": "**Algorithmic Mechanics:**\\nMinimizes empirical risk via gradient descent on continuous loss functions, updating parameters in the direction of steepest descent $\\theta \\leftarrow \\theta - \\alpha \\nabla L(\\theta)$.",
        "alts_default": "#### 🔀 Candidate Architectural Alternatives\\n- **Analytical Normal Equations:** $\\theta = (X^T X)^{-1} X^T y$ finds the exact global minimum in one step, but suffers from $O(d^3)$ matrix inversion complexity for large feature counts.\\n- **Stochastic Gradient Descent (SGD):** Computes gradients per single sample, enabling streaming updates and escaping saddle points.\\n- **L1 vs L2 Regularization:** L2 (Ridge) penalizes large weights smoothly, while L1 (Lasso) induces exact zeros for automatic feature selection."
    },
    "17": {
        "title": "Case 17: The Nearest Neighbor",
        "why_default": "**Algorithmic Mechanics:**\\nNon-parametric instance-based learning that calculates pairwise vector distances to find the $K$ closest neighbors. By the Cover-Hart theorem, as $N \\to \\infty$, the 1-NN error is at most twice the optimal Bayes error rate.",
        "alts_default": "#### 🔀 Candidate Architectural Alternatives\\n- **KD-Tree / Ball Tree:** Hierarchical space-partitioning trees reducing search from brute-force $O(N \\cdot d)$ to $O(d \\log N)$ for low dimensions ($d < 20$).\\n- **Locality Sensitive Hashing (LSH):** Sub-linear approximate nearest neighbor queries for high-dimensional embeddings.\\n- **Distance-Weighted KNN:** Assigns weights $w_i = 1/d_i^2$, reducing sensitivity to the choice of $K$ and edge noise."
    },
    "18": {
        "title": "Case 18: The Naive Assumption",
        "why_default": "**Algorithmic Mechanics:**\\nAssumes conditional independence between features given the class: $P(x_1...x_d|C) = \\prod P(x_i|C)$. With Laplace smoothing, this prevents zero-frequency multiplication dropouts and performs remarkably well on high-dimensional sparse text vectors.",
        "alts_default": "#### 🔀 Candidate Architectural Alternatives\\n- **Logistic Regression:** Discriminative equivalent that models $P(C|X)$ without assuming feature independence; generally achieves higher asymptotic accuracy on correlated data.\\n- **Gaussian Naive Bayes:** Models continuous variables using normal distribution likelihoods $\\mathcal{N}(\\mu, \\sigma^2)$.\\n- **Support Vector Machines (SVM):** Finds the maximum-margin hyperplane, offering superior generalization on text categorization without independence assumptions."
    },
    "19": {
        "title": "Case 19: The Tree That Makes Decisions",
        "why_default": "**Algorithmic Mechanics:**\\nGreedy recursive binary splitting maximizes Information Gain $IG(S, A) = H(S) - \\sum \\frac{|S_v|}{|S|} H(S_v)$, partitioning the feature space into orthogonal hyper-rectangles with human-interpretable rules.",
        "alts_default": "#### 🔀 Candidate Architectural Alternatives\\n- **Gini Impurity (CART):** Faster to compute than logarithmic Shannon Entropy ($1 - \\sum p_i^2$) and yields nearly identical tree architectures.\\n- **Random Forests:** Ensembles hundreds of de-correlated trees with feature bagging, reducing variance without increasing bias.\\n- **Gradient Boosted Decision Trees (XGBoost):** Sequentially fits trees to the negative loss gradient, dominating tabular engineering leaderboards."
    },
    "20": {
        "title": "Case 20: The Agent That Learns From Failure",
        "why_default": "**Algorithmic Mechanics:**\\nTemporal Difference Bellman update: $Q(s, a) \\leftarrow Q(s, a) + \\alpha [r + \\gamma \\max_{a'} Q(s', a') - Q(s, a)]$. Watkins (1989) proved this model-free algorithm is guaranteed to converge to the optimal policy $Q^*$ under standard stochastic approximation conditions.",
        "alts_default": "#### 🔀 Candidate Architectural Alternatives\\n- **SARSA (On-Policy):** Uses the actual next action chosen by policy $Q(s', a')$, producing safer policies in environments with dangerous penalty cliffs.\\n- **Value Iteration / Policy Iteration:** Requires an explicit model of transition probabilities $P(s'|s, a)$; exact, but unusable when environment physics are unknown.\\n- **Deep Q-Networks (DQN):** Uses deep neural networks to approximate the Q-table with experience replay buffers for continuous or high-dimensional state spaces."
    },
    "21": {
        "title": "Case 21: The Logic Programmer",
        "why_default": "**Algorithmic Mechanics:**\\nDeclarative logic programming executes SLD-resolution with first-order unification, automatically searching the Horn clause database to bind variables that satisfy the query.",
        "alts_default": "#### 🔀 Candidate Architectural Alternatives\\n- **Datalog:** Restricts PROLOG by eliminating function symbols, guaranteeing polynomial query termination.\\n- **Answer Set Programming (ASP):** Solves hard combinatorial search problems using stable model semantics.\\n- **Constraint Logic Programming (CLP):** Combines logic programming with numerical simplex and interval domain constraint solvers."
    },
    "22": {
        "title": "Case 22: The Expert in the Box",
        "why_default": "**Algorithmic Mechanics:**\\nSeparates declarative domain rules (knowledge base) from the inference engine (match-resolve-act cycle), enabling modular updates to complex expert knowledge without rewriting code.",
        "alts_default": "#### 🔀 Candidate Architectural Alternatives\\n- **Rete Algorithm:** Compiles production rules into an in-memory discrimination network, avoiding redundant evaluations when working memory changes.\\n- **Fuzzy Expert Systems:** Evaluates continuous membership functions, handling engineering vagueness in temperature and pressure control.\\n- **Case-Based Reasoning (CBR):** Adapts past documented engineering case histories rather than static deductive rules."
    },
    "23": {
        "title": "Case 23: The Intelligence Architect",
        "why_default": "**Algorithmic Mechanics:**\\nDecouples multi-agent components using standardized message schemas (FIPA-ACL) and blackboard repositories, allowing autonomous specialized agents to negotiate via auction protocols.",
        "alts_default": "#### 🔀 Candidate Architectural Alternatives\\n- **Centralized Master-Worker:** Simple to coordinate, but creates a single point of failure and bottleneck under high telemetry volume.\\n- **Peer-to-Peer Gossip Protocols:** Resilient to node dropouts in distributed industrial IoT networks.\\n- **Multi-Agent Reinforcement Learning (MARL):** Co-adapts agent behaviors in competitive or collaborative settings."
    },
    "24": {
        "title": "Case 24: The Final AI",
        "why_default": "**Algorithmic Mechanics:**\\nNeuro-Symbolic architecture: combines continuous perceptual neural networks with discrete symbolic verification layers, ensuring outputs satisfy mathematical and physical safety invariants.",
        "alts_default": "#### 🔀 Candidate Architectural Alternatives\\n- **Pure Deep Learning:** High empirical accuracy on perceptual tasks, but vulnerable to adversarial hallucinations and lacks formal safety guarantees.\\n- **Pure Symbolic AI:** Fully verifiable and explainable, but brittle to raw sensory noise and unable to scale to unstructured images/audio.\\n- **Physics-Informed Neural Networks (PINNs):** Embeds governing partial differential equations directly into loss functions."
    }
}

updated_cases = 0
updated_labs = 0

for cid_str, case in lc.items():
    meta = CASE_METADATA.get(cid_str, {})
    if meta.get("title"):
        case["title"] = meta["title"]
        
    episodes = case.get("episodes", [])
    for ep_idx, ep in enumerate(episodes):
        blocks = ep.get("blocks", [])
        for b_idx, b in enumerate(blocks):
            btype = b.get("type")
            if btype in ("code_lab", "code_experiment"):
                updated_labs += 1
                b["title"] = b.get("title") or f"Algorithm Implementation: Module {ep_idx+1}"
                
                # Check why_it_works
                if not b.get("why_it_works") or "implements the theoretical constructs" in b.get("why_it_works", ""):
                    b["why_it_works"] = meta.get("why_default", "**Algorithmic Mechanics:**\\nThis implementation establishes the exact state transitions and invariant checks required for this problem.")
                
                # Check alternatives
                if not b.get("alternatives"):
                    b["alternatives"] = meta.get("alts_default", "#### 🔀 Candidate Architectural Alternatives\\n- **Alternative 1: Brute Force Search** (Exponential complexity)\\n- **Alternative 2: Heuristic / Approximation** (Faster but bounds suboptimality)\\n- **Alternative 3: Probabilistic Modeling** (Noise tolerant)")
                
                # Add complexity if missing
                if not b.get("complexity"):
                    b["complexity"] = "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."

            elif btype in ("interactive", "fill_in_the_blank"):
                ans = b.get("answer", "")
                if not b.get("explanation") or "The correct answer is" in b.get("explanation", ""):
                    b["explanation"] = f"**Why {ans} is Correct:**\\nThis option correctly reflects the foundational theorem and invariant governing this model. Alternative options fail because they either violate time/space constraints or make unsound assumptions about environment determinism."

    updated_cases += 1

# Write back enriched level_content.py
with open(path, 'w', encoding='utf-8') as f:
    f.write("# Master Curriculum Database for AI Story Lab\n")
    f.write("LEVEL_CONTENT = \\\n")
    json.dump(lc, f, indent=4, ensure_ascii=False)

print(f"Successfully enriched all {updated_cases} cases and {updated_labs} code labs with deep concepts, why-it-works reasoning, alternatives, and explanations!")
