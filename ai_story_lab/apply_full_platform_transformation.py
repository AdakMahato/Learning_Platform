# Master Transformation Script for AI Story Lab
# Upgrades all quizzes, code labs, architecture diagrams, and interactive steppers across Cases 0 to 24

import json
import os
import sys

# Ensure local imports work
sys.path.insert(0, '/Users/aadarshamahato/Downloads/LEARNING_PLATFORM/ai_story_lab')

import level_content
from quizzes_part1 import QUIZZES_0_TO_6
from quizzes_part2 import QUIZZES_7_TO_11
from quizzes_part3 import QUIZZES_12_TO_16
from quizzes_part4 import QUIZZES_17_TO_20
from quizzes_part5 import QUIZZES_21_TO_24
from code_labs_7_to_11 import CODE_LABS_7_TO_11

# Combine all quizzes
ALL_QUIZZES = {}
ALL_QUIZZES.update(QUIZZES_0_TO_6)
ALL_QUIZZES.update(QUIZZES_7_TO_11)
ALL_QUIZZES.update(QUIZZES_12_TO_16)
ALL_QUIZZES.update(QUIZZES_17_TO_20)
ALL_QUIZZES.update(QUIZZES_21_TO_24)

# Define Rich Interactive Steppers
RICH_STEPPERS = {
    ("1", 0): {
        "type": "visual_stepper",
        "title": "Interactive: The Rational Agent Loop",
        "steps": [
            {
                "explanation": "Step 1: The Environment exists in an objective physical state S(t) and continuously emits raw signals (light waves, acoustic vibrations, telemetry).",
                "mermaid_code": """graph LR
  classDef active fill:#10b98126,stroke:#10b981,stroke-width:2px;
  classDef idle fill:#1e293b,stroke:#475569,stroke-width:1px;
  E["Environment S(t)"]:::active -->|Raw Signals| S["Sensors"]:::idle
  S --> A["Agent Program"]:::idle
  A --> AC["Actuators"]:::idle
  AC --> E"""
            },
            {
                "explanation": "Step 2: Sensors filter noise and convert raw signals into digital Percepts (P1, P2, ... Pn) received by the agent.",
                "mermaid_code": """graph LR
  classDef active fill:#3b82f626,stroke:#3b82f6,stroke-width:2px;
  classDef visited fill:#10b98126,stroke:#10b981,stroke-width:1px;
  classDef idle fill:#1e293b,stroke:#475569,stroke-width:1px;
  E["Environment S(t)"]:::visited -->|Percept Stream| S["Sensors"]:::active
  S -->|Percept Vector| A["Agent Program"]:::idle
  A --> AC["Actuators"]:::idle
  AC --> E"""
            },
            {
                "explanation": "Step 3: The Agent Program maps the percept history and internal belief state to an optimal Action A(t) that maximizes its performance measure.",
                "mermaid_code": """graph LR
  classDef active fill:#6366f126,stroke:#6366f1,stroke-width:2px;
  classDef visited fill:#10b98126,stroke:#10b981,stroke-width:1px;
  classDef idle fill:#1e293b,stroke:#475569,stroke-width:1px;
  E["Environment S(t)"]:::visited --> S["Sensors"]:::visited
  S --> A["Agent Program (Policy & Belief)"]:::active
  A -->|Selected Action| AC["Actuators"]:::idle
  AC --> E"""
            },
            {
                "explanation": "Step 4: Actuators execute Action A(t), physically altering the environment into new state S(t+1). The rational loop repeats indefinitely.",
                "mermaid_code": """graph LR
  classDef active fill:#f59e0b26,stroke:#f59e0b,stroke-width:2px;
  classDef visited fill:#10b98126,stroke:#10b981,stroke-width:1px;
  E["Environment S(t+1)"]:::active --> S["Sensors"]:::visited
  S --> A["Agent Program"]:::visited
  A --> AC["Actuators"]:::active
  AC -->|Executes Action| E"""
            }
        ]
    },
    ("3", 0): {
        "type": "visual_stepper",
        "title": "Interactive: Breadth-First Search (BFS) Traversal",
        "steps": [
            {
                "explanation": "Step 1: BFS initializes the FIFO Queue with Root node A. Visited = {A}.",
                "mermaid_code": """graph TD
  classDef active fill:#3b82f626,stroke:#3b82f6,stroke-width:2px;
  classDef idle fill:#1e293b,stroke:#475569,stroke-width:1px;
  A["Root A (In Queue)"]:::active --> B["B (Unvisited)"]:::idle
  A --> C["C (Unvisited)"]:::idle
  B --> D["D"]:::idle
  B --> E["E"]:::idle
  C --> F["Goal F"]:::idle"""
            },
            {
                "explanation": "Step 2: Node A popped from queue; all Depth-1 children (B, C) enqueued. FIFO Queue: [B, C].",
                "mermaid_code": """graph TD
  classDef visited fill:#10b98126,stroke:#10b981,stroke-width:1px;
  classDef active fill:#3b82f626,stroke:#3b82f6,stroke-width:2px;
  classDef idle fill:#1e293b,stroke:#475569,stroke-width:1px;
  A["Root A (Visited)"]:::visited --> B["B (In Queue)"]:::active
  A --> C["C (In Queue)"]:::active
  B --> D["D"]:::idle
  B --> E["E"]:::idle
  C --> F["Goal F"]:::idle"""
            },
            {
                "explanation": "Step 3: Node B popped; children D, E enqueued. Queue: [C, D, E]. Entire depth layer 1 evaluated before deeper nodes.",
                "mermaid_code": """graph TD
  classDef visited fill:#10b98126,stroke:#10b981,stroke-width:1px;
  classDef active fill:#3b82f626,stroke:#3b82f6,stroke-width:2px;
  classDef idle fill:#1e293b,stroke:#475569,stroke-width:1px;
  A["Root A"]:::visited --> B["B (Visited)"]:::visited
  A --> C["C (In Queue)"]:::active
  B --> D["D (In Queue)"]:::active
  B --> E["E (In Queue)"]:::active
  C --> F["Goal F"]:::idle"""
            },
            {
                "explanation": "Step 4: Node C popped; child Goal F discovered! BFS guarantees finding the shallowest, shortest path in uniform step-cost graphs.",
                "mermaid_code": """graph TD
  classDef visited fill:#10b98126,stroke:#10b981,stroke-width:1px;
  classDef goal fill:#10b98140,stroke:#34d399,stroke-width:3px;
  A["Root A"]:::visited --> B["B"]:::visited
  A --> C["C"]:::visited
  B --> D["D"]:::visited
  B --> E["E"]:::visited
  C --> F["Goal F FOUND!"]:::goal"""
            }
        ]
    },
    ("7", 3): {
        "type": "visual_stepper",
        "title": "Interactive: AC-3 Constraint Propagation",
        "steps": [
            {
                "explanation": "Step 1: Arc Queue initialized with all binary arcs between regions: [(WA, NT), (NT, WA), (WA, SA), (SA, WA), (NT, SA), (SA, NT)].",
                "mermaid_code": """graph LR
  classDef init fill:#3b82f626,stroke:#3b82f6,stroke-width:2px;
  WA["WA: [Red]"]:::init ---|WA != NT| NT["NT: [Red, Green, Blue]"]:::init
  WA ---|WA != SA| SA["SA: [Red, Green, Blue]"]:::init
  NT ---|NT != SA| SA"""
            },
            {
                "explanation": "Step 2: Arc (NT, WA) evaluated. For WA = Red, NT cannot be Red. Color 'Red' is pruned from NT's domain. Domain(NT) -> [Green, Blue].",
                "mermaid_code": """graph LR
  classDef active fill:#6366f126,stroke:#6366f1,stroke-width:2px;
  classDef done fill:#10b98126,stroke:#10b981,stroke-width:1px;
  WA["WA: [Red]"]:::done --- NT["NT: [Green, Blue]"]:::active
  WA --- SA["SA: [Red, Green, Blue]"]
  NT --- SA"""
            },
            {
                "explanation": "Step 3: Arc (SA, WA) evaluated. For WA = Red, 'Red' pruned from SA. Domain(SA) -> [Green, Blue].",
                "mermaid_code": """graph LR
  classDef done fill:#10b98126,stroke:#10b981,stroke-width:1px;
  classDef active fill:#6366f126,stroke:#6366f1,stroke-width:2px;
  WA["WA: [Red]"]:::done --- NT["NT: [Green, Blue]"]:::done
  WA --- SA["SA: [Green, Blue]"]:::active
  NT --- SA"""
            },
            {
                "explanation": "Step 4: All remaining arcs checked and consistent. Inconsistent branches were pruned before search even began, saving exponential CPU time!",
                "mermaid_code": """graph LR
  classDef final fill:#10b98133,stroke:#10b981,stroke-width:2px;
  WA["WA: [Red]"]:::final --- NT["NT: [Green, Blue]"]:::final
  WA --- SA["SA: [Green, Blue]"]:::final
  NT --- SA"""
            }
        ]
    },
    ("12", 3): {
        "type": "visual_stepper",
        "title": "Interactive: Bayesian Diagnostic Updating",
        "steps": [
            {
                "explanation": "Step 1: Prior Distribution established. Base rate of rare condition P(Disease) = 1% (0.01). Healthy population P(Healthy) = 99%.",
                "mermaid_code": """graph TD
  classDef base fill:#1e293b,stroke:#475569,stroke-width:1px;
  classDef highlight fill:#3b82f626,stroke:#3b82f6,stroke-width:2px;
  P["Population (100%)"]:::base --> D["P(Disease) = 1%"]:::highlight
  P --> H["P(Healthy) = 99%"]:::base"""
            },
            {
                "explanation": "Step 2: Patient tests Positive. Diagnostic test accuracy: True Positive Rate (Sensitivity) = 99%, False Positive Rate = 5%.",
                "mermaid_code": """graph TD
  classDef base fill:#1e293b,stroke:#475569,stroke-width:1px;
  classDef pos fill:#f59e0b26,stroke:#f59e0b,stroke-width:2px;
  D["Disease (1%)"] --> TP["Test Positive: 0.01 × 0.99 = 0.0099"]:::pos
  H["Healthy (99%)"] --> FP["False Positive: 0.99 × 0.05 = 0.0495"]:::pos"""
            },
            {
                "explanation": "Step 3: Marginal Evidence calculated by Law of Total Probability: P(Test+) = 0.0099 + 0.0495 = 0.0594 (5.94% of total population).",
                "mermaid_code": """graph LR
  classDef total fill:#6366f126,stroke:#6366f1,stroke-width:2px;
  TP["True Positives: 0.0099"] --> N["Total Positive Evidence P(T+): 0.0594"]:::total
  FP["False Positives: 0.0495"] --> N"""
            },
            {
                "explanation": "Step 4: Bayes' Rule Normalization: P(Disease | Test+) = 0.0099 / 0.0594 = 16.67%. Despite a 99% accurate test, most positive tests are false positives due to the rare base rate!",
                "mermaid_code": """graph TD
  classDef result fill:#10b98133,stroke:#10b981,stroke-width:3px;
  B["Prior P(D) = 1%"] --> RES["Posterior P(Disease | Test+) = 16.67%"]:::result
  E["Evidence: Test+ (99% acc)"] --> RES"""
            }
        ]
    },
    ("20", 0): {
        "type": "visual_stepper",
        "title": "Interactive: Q-Learning Bellman TD Backup",
        "steps": [
            {
                "explanation": "Step 1: The Agent sits at State S(t) with Q-table estimates. Using an epsilon-greedy policy, it selects Action A(t).",
                "mermaid_code": """graph LR
  classDef active fill:#3b82f626,stroke:#3b82f6,stroke-width:2px;
  classDef idle fill:#1e293b,stroke:#475569,stroke-width:1px;
  S["State S(t)"]:::active -->|"Action A(t)"| ENV["Environment"]:::idle
  ENV --> S2["Next State S(t+1)"]:::idle
  ENV --> R["Reward R(t+1)"]:::idle"""
            },
            {
                "explanation": "Step 2: Environment executes Action A(t), emitting numeric Reward R(t+1) and transitioning the agent to Next State S(t+1).",
                "mermaid_code": """graph LR
  classDef active fill:#f59e0b26,stroke:#f59e0b,stroke-width:2px;
  classDef visited fill:#3b82f626,stroke:#3b82f6,stroke-width:1px;
  S["State S(t)"]:::visited --> ENV["Environment"]:::active
  ENV -->|"Observed Reward"| R["Reward R(t+1)"]:::active
  ENV -->|"New State"| S2["Next State S(t+1)"]:::active"""
            },
            {
                "explanation": "Step 3: The Agent inspects Q(S(t+1), a') across all allowable next actions to identify max Q(S(t+1), a') and computes the discounted Bellman Target.",
                "mermaid_code": """graph TD
  classDef calc fill:#6366f126,stroke:#6366f1,stroke-width:2px;
  R["Reward R(t+1)"] --> TARGET["Bellman Target = R + γ × max Q(S', a')"]:::calc
  S2["Max Q over S(t+1)"] --> TARGET"""
            },
            {
                "explanation": "Step 4: Temporal Difference Error δ = Target - Q(S(t), A(t)) is calculated. Q(S(t), A(t)) updates via learning rate α: Q <- Q + α × δ.",
                "mermaid_code": """graph LR
  classDef update fill:#10b98133,stroke:#10b981,stroke-width:3px;
  T["Bellman Target"] --> TD["TD Error: Target - Q_old"]
  TD --> Q["Q_new(S, A) = Q_old + α × TD_Error"]:::update"""
            }
        ]
    }
}

# Rich Architecture Diagrams with Structural Descriptions
RICH_ARCHITECTURES = {
    ("12", 3, 8): {
        "type": "visual",
        "title": "Multimodal Probabilistic Inference Pipeline",
        "code": """graph LR
  subgraph DataStream ["Multimodal Sensory & Diagnostic Stream"]
    S1["Clinical Biomarkers & Vitals"]
    S2["Historical Patient Cohorts"]
  end
  subgraph ProbEngine ["Probabilistic Reasoning Engine"]
    P1["Prior Distribution P(Disease)"]
    P2["Likelihood Model P(Symptoms | Disease)"]
    P3["Bayes Normalization ∫ P(S|D)P(D)"]
    P1 & P2 --> P3
  end
  subgraph DecisionAction ["Clinical Decision & Risk Management"]
    A1["Posterior Belief P(D | Symptoms)"]
    A2["Expected Loss / Minimum Risk Action"]
    P3 --> A1 --> A2
  end
  DataStream --> ProbEngine
  style DataStream fill:#1e293b,stroke:#475569
  style ProbEngine fill:#312e81,stroke:#6366f1
  style DecisionAction fill:#064e3b,stroke:#10b981"""
    },
    ("20", 0, 6): {
        "type": "visual",
        "title": "Reinforcement Learning MDP Architecture",
        "code": """graph TD
  subgraph Agent ["Reinforcement Learning Agent"]
    POL["Policy π(a | s)"]
    VAL["Value Function / Q-Table Q(s, a)"]
    UPDATE["Bellman TD Learning Rule"]
    VAL --> POL
    UPDATE --> VAL
  end
  subgraph MDP ["Markov Decision Process Environment"]
    TRANS["Transition Dynamics P(s' | s, a)"]
    REW["Reward Function R(s, a, s')"]
  end
  POL -->|"Action A(t)"| MDP
  MDP -->|"Next State S(t+1)"| UPDATE
  MDP -->|"Reward R(t+1)"| UPDATE
  style Agent fill:#1e1b4b,stroke:#6366f1
  style MDP fill:#0f172a,stroke:#3b82f6"""
    }
}

# Execute master update
content = level_content.LEVEL_CONTENT
replaced_questions = 0
updated_code_labs = 0
injected_steppers = 0

for cid_int in range(25):
    cid = str(cid_int)
    cdata = content.get(cid, {})
    episodes = cdata.get("episodes", [])
    
    quiz_case_data = ALL_QUIZZES.get(cid, {})
    
    for ep_idx, ep in enumerate(episodes):
        blocks = ep.get("blocks", [])
        quiz_list = quiz_case_data.get(ep_idx, [])
        q_cursor = 0
        
        # 1. Update/replace questions in this episode
        for b_idx, b in enumerate(blocks):
            btype = b.get("type")
            
            # Check if this is a broken question markdown block
            if btype == "markdown" and ("Question:" in b.get("content", "") or "**Question:**" in b.get("content", "")):
                if q_cursor < len(quiz_list):
                    q_data = quiz_list[q_cursor]
                    blocks[b_idx] = {
                        "type": "interactive",
                        "question": q_data["question"],
                        "options": q_data["options"],
                        "answer": q_data["answer"],
                        "explanation": q_data["explanation"]
                    }
                    q_cursor += 1
                    replaced_questions += 1
                    
            # Check if this is an existing interactive/quiz block to enrich
            elif btype in ("interactive", "micro_challenge", "mastery_challenge", "fill_in_the_blank"):
                if q_cursor < len(quiz_list):
                    q_data = quiz_list[q_cursor]
                    # Update with deep explanation and validated options
                    b["explanation"] = q_data["explanation"]
                    if "options" in q_data and len(q_data["options"]) >= 2:
                        b["options"] = q_data["options"]
                    if "answer" in q_data:
                        b["answer"] = q_data["answer"]
                    q_cursor += 1

        # 2. Update empty code labs
        if (cid, ep_idx) in CODE_LABS_7_TO_11:
            lab_data = CODE_LABS_7_TO_11[(cid, ep_idx)]
            for b_idx, b in enumerate(blocks):
                if b.get("type") == "code_lab":
                    st = b.get("starter_code", "")
                    if not st.strip():
                        blocks[b_idx]["title"] = lab_data["title"]
                        blocks[b_idx]["starter_code"] = lab_data["starter_code"]
                        blocks[b_idx]["solution_code"] = lab_data["solution_code"]
                        blocks[b_idx]["expected_output"] = lab_data["expected_output"]
                        blocks[b_idx]["explanation"] = lab_data["explanation"]
                        updated_code_labs += 1

        # 3. Upgrade Architecture Diagrams
        for (a_cid, a_ep, a_bidx), arch_data in RICH_ARCHITECTURES.items():
            if cid == a_cid and ep_idx == a_ep and a_bidx < len(blocks):
                blocks[a_bidx] = arch_data
                # Add architectural explanation directly after
                if a_bidx + 1 < len(blocks) and blocks[a_bidx + 1].get("type") == "markdown":
                    if a_cid == "12":
                        blocks[a_bidx + 1]["content"] = """### 🏗️ Why this Architecture Works: The Diagnostic Engine
**Mathematical Rationale:**
Real-world medical diagnosis and robotics operate under severe partial observability. A diagnostic test or optical sensor does not observe the true latent state (disease or obstacle) directly; it only observes noisy symptoms.
- **Why Naive Rules Fail:** A deterministic rule (`IF test_positive THEN patient_diseased`) triggers massive false alarm rates when disease prevalence is low (Base Rate Fallacy).
- **Why Bayes Engine Works:** By multiplying the Likelihood $P(\\text{Symptoms} \\mid \\text{Disease})$ by the Population Prior $P(\\text{Disease})$ and normalizing by total evidence, the architecture guarantees mathematically optimal belief updates.
- **Alternative Architectural Paradigms:**
  - *Fuzzy Logic / Certainty Factors:* Computationally lighter, but lacks axiomatic consistency over multi-step reasoning.
  - *End-to-End Neural Networks:* Can predict diagnosis directly from raw pixels/vitals, but acts as an uninterpretable black box without causal guarantees."""
                    elif a_cid == "20":
                        blocks[a_bidx + 1]["content"] = """### 🏗️ Why this Architecture Works: The MDP Interaction Loop
**Mathematical Rationale:**
Unlike Supervised Learning (which requires human ground-truth labels for every input), Reinforcement Learning architectures solve the Credit Assignment Problem over extended time horizons:
- **The State Space $S$:** Satisfies the **Markov Property** ($P(S_{t+1} \\mid S_t, A_t) = P(S_{t+1} \\mid S_t, A_t, \\dots S_0, A_0)$)—the future depends solely on the current state.
- **The Bellman Operator:** Provides a recursive contraction mapping $T^*(Q) = R + \\gamma \\max_{a'} Q(S', a')$ that is mathematically guaranteed to converge to the unique optimal Q-function $Q^*$ in finite MDPs.
- **Alternative Architectural Paradigms:**
  - *Policy Gradients (PPO / TRPO):* Directly optimizes parameter weights $\\theta$ of $\\pi_\\theta(a|s)$ via gradient ascent, essential for continuous action spaces (robotics).
  - *Model-Based RL (MuZero / World Models):* Learns an internal simulator of the transition dynamics, enabling deep tree search ahead of execution."""

        # 4. Inject Rich Interactive Steppers
        if (cid, ep_idx) in RICH_STEPPERS:
            stepper_data = RICH_STEPPERS[(cid, ep_idx)]
            # Check if stepper already exists
            has_stepper = any(b.get("type") == "visual_stepper" for b in blocks)
            if not has_stepper:
                # Insert stepper right after first concept or visual block
                insert_idx = min(3, len(blocks))
                blocks.insert(insert_idx, stepper_data)
                injected_steppers += 1

print(f"Replaced {replaced_questions} broken question blocks in-place with rich interactive quizzes!")
print(f"Updated {updated_code_labs} empty code labs with complete executable Python labs!")
print(f"Injected {injected_steppers} rich multi-step interactive steppers!")

# Save back to level_content.py
with open('/Users/aadarshamahato/Downloads/LEARNING_PLATFORM/ai_story_lab/level_content.py', 'w', encoding='utf-8') as f:
    f.write("# Master Curriculum Database for AI Story Lab\nLEVEL_CONTENT = \\\n")
    json.dump(content, f, indent=4, ensure_ascii=False)

print("Master curriculum database updated and serialized successfully!")
