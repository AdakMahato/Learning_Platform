import json
import os

PART1_CASES = {}

# CASE 00: The Software Crisis
PART1_CASES["0"] = {
    "title": "Case 00: The Software Crisis",
    "episodes": [
        {
            "title": "Module 1: The 1968 NATO Conference & The Crisis",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "In October 1968, fifty of the world's leading computer scientists gathered in Garmisch, Germany, under the auspices of the NATO Science Committee. The industry was reeling from astronomical cost overruns, delayed deliveries, and disastrous software crashes. For the first time, leaders recognized that coding without engineering discipline was unsustainable: the **Software Crisis** was officially declared."
                },
                {
                    "type": "objective",
                    "title": "Module Objective",
                    "content": "Understand the historical origins of Software Engineering, the causes of the 1968 Software Crisis, and why software systems fail differently from physical structures."
                },
                {
                    "type": "concept",
                    "title": "Software Crisis Symptoms & Root Causes",
                    "content": "The Software Crisis manifested in four catastrophic symptoms:\n\n1. **Budget Overruns:** Projects routinely cost 200% to 500% of their initial estimates.\n2. **Schedule Slippage:** Delays stretched into years as unmanaged dependencies created cascading blockers.\n3. **Defective Quality:** Systems shipped with critical flaws that caused loss of life and financial ruin.\n4. **Unmaintainability:** Modifying one routine broke three unrelated subroutines because code was an unstructured web of global variables and GOTO statements."
                },
                {
                    "type": "visual",
                    "title": "The Software Crisis Causality Matrix",
                    "code": """graph TD
  subgraph Roots ["Underlying Systemic Causes"]
    C1["Exponential Hardware Growth (Moore's Law)"]
    C2["Lack of Formal Software Methodologies"]
    C3["Informal Ad-Hoc 'Cowboy Coding'"]
  end
  subgraph Symptoms ["The Software Crisis (1968)"]
    S1["Massive Budget Overruns (>300%)"]
    S2["Chronic Project Schedule Delays"]
    S3["Severe Defect Rates & Fragile Spaghettification"]
    C1 & C2 & C3 --> S1 & S2 & S3
  end
  subgraph Resolution ["The Birth of Software Engineering"]
    SE["Formal Engineering Discipline: Processes, Architectures, QA, Metrics"]
    S1 & S2 & S3 --> SE
  end
  style Roots fill:#3f1a1a,stroke:#ef4444
  style Symptoms fill:#1e1b4b,stroke:#6366f1
  style Resolution fill:#064e3b,stroke:#10b981"""
                },
                {
                    "type": "interactive",
                    "title": "Historical Analysis Challenge",
                    "question": "What was the fundamental insight of the 1968 NATO Conference regarding why software projects failed?",
                    "options": [
                        "Hardware was too slow to execute complex logical statements efficiently.",
                        "Building large software systems is an engineering discipline requiring formal processes, not merely solitary mathematical programming.",
                        "Compilers were introducing non-deterministic bugs into assembly instructions.",
                        "Programmers were not working enough overtime hours to meet deadlines."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nThe conference recognized that as software grew in scale, solitary ad-hoc programming could not scale. Software construction required standard engineering principles: lifecycle phases, rigorous specification, quality verification, and configuration control."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Core Terminology Challenge",
                    "question": "The historical period characterized by budget overruns, severe unreliability, and unmaintainable code is known as the Software _____.\n\nAnswer: _____",
                    "answer": "Crisis",
                    "alternatives": ["Crisis", "Software Crisis", "crisis"],
                    "explanation": "**Why Crisis is Correct:**\nThe **Software Crisis** term was coined in the late 1960s to describe the widening gap between hardware computing capabilities and our ability to reliably build software to harness them."
                }
            ]
        },
        {
            "title": "Module 2: Why Software Differs from Physical Engineering",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Civil and mechanical engineers build with concrete, steel, and titanium. Software engineers build with pure conceptual logic. In his seminal 1986 paper *'No Silver Bullet — Essence and Accident in Software Engineering'*, Turing Award laureate Fred Brooks explained why software engineering is fundamentally harder."
                },
                {
                    "type": "concept",
                    "title": "Essential vs. Accidental Difficulties (Brooks)",
                    "content": "Brooks divided software development challenges into two categories:\n\n- **Essential Difficulties:** Inherent to the nature of software and cannot be eliminated by any technology. These include:\n  1. **Complexity:** No two software parts are alike; scaling creates non-linear state spaces.\n  2. **Conformity:** Software must conform to arbitrary human institutions, legacy APIs, and legal rules.\n  3. **Changeability:** Software is subject to intense pressure for constant modification because it is perceived as easily altered.\n  4. **Invisibility:** Software cannot be visualized in physical space; geometric representations fail to capture full control and data flow.\n- **Accidental Difficulties:** Difficulties attending the current production environment (e.g., slow compilers, memory limits, cryptic syntax), which technology can solve."
                },
                {
                    "type": "visual",
                    "title": "Software Wear Curve vs. Hardware Bathtub Curve",
                    "code": """graph TD
  subgraph Hardware ["Hardware Lifecycle (Physical Bathtub Curve)"]
    H1["Infant Mortality (Manufacturing Flaws)"] --> H2["Low Constant Burn-In Failure Rate"] --> H3["Physical Wear-Out (Fatigue & Friction)"]
  end
  subgraph Software ["Software Lifecycle (Deterioration Curve)"]
    S1["Initial Defect Discovery & Remediation"] --> S2["Stable Baseline Release"]
    S2 -->|"Continuous Scope Changes & Patches"| S3["Side-Effect Defects Introduced"]
    S3 --> S4["Architectural Erosion & Decay"]
  end
  style Hardware fill:#0f172a,stroke:#3b82f6
  style Software fill:#1e1b4b,stroke:#6366f1"""
                },
                {
                    "type": "interactive",
                    "title": "Artifact Characteristics Challenge",
                    "question": "Which of the following is a fundamental distinguishing property of software compared to physical hardware?",
                    "options": [
                        "Software degrades due to physical friction and thermal oxidation.",
                        "Software is manufactured on assembly lines with physical component tolerances.",
                        "Software does not wear out physically, but deteriorates as successive changes erode its conceptual integrity.",
                        "Software cannot be modified once installed into production environments."
                    ],
                    "answer": 2,
                    "explanation": "**Why this is Correct:**\nFred Brooks emphasized in 'No Silver Bullet' that software's essential complexity stems from its conceptual, invisible nature. It does not wear out from mechanical fatigue; it deteriorates because environmental and feature changes break original architectural assumptions."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Conceptual Property Challenge",
                    "question": "Because software is constructed of pure thought-stuff without physical constraints, it possesses high _____ (the ease with which it can be altered, which paradoxically makes it fragile).\n\nAnswer: _____",
                    "answer": "Malleability",
                    "alternatives": ["Malleability", "Plasticity", "Flexibility", "Changeability", "malleability"],
                    "explanation": "**Why Malleability is Correct:**\n**Malleability** is software's blessing and curse: unlike concrete or steel, code can be changed with keystrokes, which tempts engineers to make hasty modifications that compromise system integrity."
                }
            ]
        },
        {
            "title": "Module 3: Technical Debt & The Compounding Curve",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Ward Cunningham coined the metaphor of **Technical Debt** in 1992: shipping sub-optimal code to meet short-term deadlines is like taking out a financial loan. It accelerates delivery today, but incurs compound interest in the form of elevated future maintenance costs and bug fixing drag."
                },
                {
                    "type": "concept",
                    "title": "Technical Debt Compounding Model",
                    "content": "When technical debt is neglected:\n1. **Principal:** The direct engineering effort required to refactor the code into a clean, modular architecture.\n2. **Interest:** The extra friction, debugging time, and regression bugs incurred during every subsequent sprint.\n3. **Bankruptcy:** When 90%+ of engineering capacity is consumed merely fighting fires and keeping fragile servers alive, leaving zero time for new features."
                },
                {
                    "type": "code_lab",
                    "title": "Technical Debt Simulator Lab",
                    "instructions": "Implement a Python simulator `calculate_project_effort(base_feature_hours, sprints, debt_rate)` that computes how total development effort explodes when technical debt compounds each sprint.",
                    "starter_code": """def calculate_project_effort(base_feature_hours: float, sprints: int, debt_rate: float) -> dict:
    \"\"\"
    Calculate the total engineering hours spent over N sprints when technical debt
    adds interest to each sprint's feature delivery effort.
    
    Formula:
    Sprint 1 effort = base_feature_hours
    Sprint k effort = base_feature_hours * ((1 + debt_rate) ** (k - 1))
    
    Returns a dict with:
      - 'sprint_efforts': list of hours per sprint (rounded to 2 decimals)
      - 'total_effort': sum of all sprint efforts (rounded to 2 decimals)
      - 'debt_overhead_percent': percentage of effort caused purely by debt overhead (rounded to 2 decimals)
    \"\"\"
    # TODO: Implement simulation
    pass
""",
                    "solution_code": """def calculate_project_effort(base_feature_hours: float, sprints: int, debt_rate: float) -> dict:
    sprint_efforts = []
    for k in range(1, sprints + 1):
        effort = base_feature_hours * ((1.0 + debt_rate) ** (k - 1))
        sprint_efforts.append(round(effort, 2))
    
    total_effort = round(sum(sprint_efforts), 2)
    ideal_effort = base_feature_hours * sprints
    overhead_hours = total_effort - ideal_effort
    overhead_pct = round((overhead_hours / ideal_effort) * 100.0, 2) if ideal_effort > 0 else 0.0
    
    return {
        'sprint_efforts': sprint_efforts,
        'total_effort': total_effort,
        'debt_overhead_percent': overhead_pct
    }
""",
                    "test_code": """res = calculate_project_effort(100.0, 4, 0.10)
assert len(res['sprint_efforts']) == 4
assert res['sprint_efforts'][0] == 100.0
assert res['sprint_efforts'][1] == 110.0
assert res['sprint_efforts'][2] == 121.0
assert res['sprint_efforts'][3] == 133.1
assert res['total_effort'] == 464.1
assert abs(res['debt_overhead_percent'] - 16.02) < 0.1
print("All technical debt simulator tests passed successfully!")
""",
                    "why_works": "**Why This Solution Works:**\nTechnical debt compounds exponentially like financial interest: $(1 + r)^{k-1}$. By calculating each sprint's penalty and comparing the aggregate to the zero-debt baseline ($N \\times \\text{base}$), the simulator quantifies the exact engineering overhead consumed by debt.",
                    "alternatives": "**Alternative Approaches & Trade-offs:**\n- **Linear Friction Model:** Models debt as a constant additive penalty $(base + k \\times c)$. Suitable for minor static debt, but underestimates real-world coupling cascade failures.\n- **Sonde-based SonarQube Remediation Index:** Industrial tools estimate debt by assigning standard repair times (e.g. 15 min per cognitive complexity point) to detected static analysis violations.",
                    "edge_cases": "**Edge Cases & Failure Modes:**\n- `debt_rate = 0.0`: Must yield zero overhead and flat sprint efforts.\n- `sprints = 1`: No interest accumulated; overhead percent is exactly 0.0%.\n- Extremely high debt rates ($r > 0.5$): Reflects legacy systems where every change induces severe regressions."
                }
            ]
        },
        {
            "title": "Module 4: Engineering Ethics & The ACM/IEEE Code",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Software engineers build systems that control radiation therapy machines (Therac-25), commercial airliners (Boeing 737 MAX MCAS), nuclear reactors, and global financial transactions. Software failures can kill. This confers profound ethical responsibilities."
                },
                {
                    "type": "concept",
                    "title": "The 8 Principles of the ACM/IEEE Software Engineering Code of Ethics",
                    "content": "1. **Public:** Software engineers shall act consistently with the public interest.\n2. **Client and Employer:** Act in the best interest of client/employer, consistent with public interest.\n3. **Product:** Ensure products meet highest professional standards possible.\n4. **Judgment:** Maintain integrity and independence in professional judgment.\n5. **Management:** Managers shall promote ethical management of software development.\n6. **Profession:** Advance the integrity and reputation of the profession.\n7. **Colleagues:** Be fair to and supportive of colleagues.\n8. **Self:** Participate in lifelong learning regarding software engineering practice."
                },
                {
                    "type": "visual",
                    "title": "ACM/IEEE Ethical Hierarchy",
                    "code": """graph TD
  subgraph PrimeDirective ["Primary Inviolable Directive"]
    PUB["1. PUBLIC INTEREST (Health, Safety, Welfare)"]
  end
  subgraph SecondaryDuties ["Subordinate Professional Obligations"]
    CE["2. Client & Employer Expectations"]
    PROD["3. Technical Quality & Safety Verification"]
    JUDGE["4. Independent Professional Judgment"]
  end
  PUB -->|"Overrides"| CE
  PUB -->|"Governs"| PROD
  PUB -->|"Guides"| JUDGE
  style PrimeDirective fill:#064e3b,stroke:#10b981
  style SecondaryDuties fill:#1e1b4b,stroke:#6366f1"""
                },
                {
                    "type": "interactive",
                    "title": "Ethical Conflict Resolution Challenge",
                    "question": "According to the ACM/IEEE Code of Ethics, when a software engineer discovers a conflict between employer profit and public safety, which obligation holds supreme authority?",
                    "options": [
                        "The obligation to obey employer instructions, as employment contracts are legally binding.",
                        "The obligation to the public interest, health, safety, and welfare overrides employer or client interests.",
                        "The obligation to protect the company's stock price from negative publicity.",
                        "The obligation to deliver the product on the agreed deadline regardless of defects."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nPrinciple 1.01 states explicitly: Software engineers shall accept full responsibility for their work and approve software only if they have a well-founded belief that it is safe, meets specifications, and does not diminish quality of life. The Public Interest is the overriding prime directive."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Famous Disaster Challenge",
                    "question": "The tragic medical radiation therapy disaster caused by race conditions and lack of software interlocks in the 1980s was the _____ machine.\n\nAnswer: _____",
                    "answer": "Therac-25",
                    "alternatives": ["Therac-25", "Therac 25", "therac-25", "Therac25"],
                    "explanation": "**Why Therac-25 is Correct:**\nThe **Therac-25** disaster is the classic case study in software engineering failures: software race conditions delivered lethal radiation doses to patients because hardware safety interlocks were removed in favor of unverified software controls."
                }
            ]
        }
    ]
}

# CASE 01: The Sequential Trap (Waterfall & V-Model)
PART1_CASES["1"] = {
    "title": "Case 01: The Sequential Trap",
    "episodes": [
        {
            "title": "Module 1: Winston Royce & The Linear Waterfall",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "In 1970, Dr. Winston W. Royce published *'Managing the Development of Large Software Systems'*. In it, he illustrated a purely sequential pipeline: Requirements -> Design -> Implementation -> Verification -> Maintenance. Ironically, Royce presented this linear sequence as **flawed and invitation to failure**, advocating feedback loops; yet the defense industry codified the pure linear version into military standards like DoD-STD-2167A."
                },
                {
                    "type": "objective",
                    "title": "Module Objective",
                    "content": "Analyze the mechanics of the classic Waterfall lifecycle, recognize the catastrophic risks of delayed integration, and determine when sequential development is valid."
                },
                {
                    "type": "concept",
                    "title": "Waterfall Phases & Phase Gates",
                    "content": "Waterfall enforces strict unidirectional gates:\n1. **Requirements Analysis:** Complete, unambiguous requirements are frozen in an SRS.\n2. **System Design:** Architectural and module blueprints are documented.\n3. **Coding/Implementation:** Programs are written to match the design specifications.\n4. **Integration & Testing:** Separate components are combined and tested as a unified system.\n5. **Deployment & Operations:** The system is released to end users.\n\n**The Phase-Gate Rule:** No phase begins until the preceding phase is 100% complete and signed off in formal documentation."
                },
                {
                    "type": "visual",
                    "title": "Classic Waterfall Phase Gates & The Late Feedback Defect Trap",
                    "code": """graph TD
  subgraph Upstream ["Upstream Phases (Cheap to Fix Defects)"]
    R["1. Requirements Gathering & Analysis"] --> D["2. Architectural & Detailed Design"]
  end
  subgraph Midstream ["Midstream Phase"]
    D --> C["3. Implementation / Code Construction"]
  end
  subgraph Downstream ["Downstream Phases (Catastrophic Defect Costs)"]
    C --> T["4. System Integration & Verification Testing"]
    T --> M["5. Deployment & Long-Term Operations"]
    T -.->|"Requirement Flaws Discovered Here! (100x Cost)"| R
  end
  style Upstream fill:#064e3b,stroke:#10b981
  style Midstream fill:#1e1b4b,stroke:#6366f1
  style Downstream fill:#3f1a1a,stroke:#ef4444"""
                },
                {
                    "type": "interactive",
                    "title": "Waterfall Risk Analysis Challenge",
                    "question": "What is the primary architectural vulnerability of a strict, uniterated Waterfall process?",
                    "options": [
                        "It uses too few formal documents and review meetings.",
                        "Testing and integration occur only at the very end of the lifecycle, delaying critical risk discovery until budgets are nearly exhausted.",
                        "Software developers are required to write automated unit tests prior to writing business code.",
                        "It requires customers to test working software at the end of every two weeks."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nIn Waterfall, working software does not exist until integration testing. Discrepancies between requirements and user reality, or fundamental architectural flaws, are discovered at the end when the cost of rework is 50x to 200x higher than during design."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Lifecycle Milestone Challenge",
                    "question": "The formal checkpoints in Waterfall where a phase must be fully documented and approved before subsequent work can begin are called phase _____.\n\nAnswer: _____",
                    "answer": "Gates",
                    "alternatives": ["Gates", "gates", "Phase Gates", "phase gates"],
                    "explanation": "**Why Gates is Correct:**\n**Phase gates** (or tollgates) enforce strict linear separation between lifecycle stages. Work cannot flow past the gate until all sign-off artifacts are validated."
                }
            ]
        },
        {
            "title": "Module 2: The V-Model: Dual Verification & Validation",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "To address Waterfall's testing bottleneck, the German federal administration and international avionics standards created the **V-Model**. It explicitly links every upstream specification activity on the left descent with a corresponding testing activity on the right ascent."
                },
                {
                    "type": "concept",
                    "title": "Verification vs. Validation (Boehm's Dichotomy)",
                    "content": "Barry Boehm famously distinguished between the two V's:\n- **Verification:** *'Are we building the product right?'*\n  - Confirms that each phase's output satisfies the specifications established at the start of that phase (e.g., Code matches Design).\n- **Validation:** *'Are we building the right product?'*\n  - Confirms that the delivered system fulfills its intended real-world user needs and operational goals."
                },
                {
                    "type": "visual",
                    "title": "The Dual V-Model Architecture",
                    "code": """graph LR
  subgraph Decomposition ["Left Wing: Specification & Decomposition"]
    UR["User Requirements"] --> SR["System Specifications"]
    SR --> AD["Architectural Design"]
    AD --> MD["Module Design"]
    MD --> CODE["Coding / Implementation"]
  end
  subgraph VerificationWing ["Right Wing: Integration & Verification"]
    CODE --> UT["Unit Testing"]
    UT --> IT["Integration Testing"]
    IT --> ST["System Testing"]
    ST --> UAT["User Acceptance Testing (UAT)"]
  end
  MD -.-|"Verifies"| UT
  AD -.-|"Verifies"| IT
  SR -.-|"Verifies"| ST
  UR -.-|"Validates"| UAT
  style Decomposition fill:#0f172a,stroke:#3b82f6
  style VerificationWing fill:#1e1b4b,stroke:#6366f1"""
                },
                {
                    "type": "interactive",
                    "title": "V&V Distinction Challenge",
                    "question": "An engineering team proves that a braking module executes its mathematical deceleration formula with zero bugs, but pilots report that the formula fails on icy runways. What failed?",
                    "options": [
                        "Verification failed, but Validation succeeded.",
                        "Both Verification and Validation succeeded.",
                        "Verification succeeded (product built right), but Validation failed (built the wrong product).",
                        "Neither Verification nor Validation applies to avionics systems."
                    ],
                    "answer": 2,
                    "explanation": "**Why this is Correct:**\nThe code accurately satisfied its written formula specification (successful Verification). However, the formula failed to satisfy the real-world operational safety requirement on icy runways (failed Validation)."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Testing Level Challenge",
                    "question": "In the V-Model, User Acceptance Testing (UAT) directly validates against the original _____ requirements.\n\nAnswer: _____",
                    "answer": "User",
                    "alternatives": ["User", "user", "User Requirements", "Customer", "Business"],
                    "explanation": "**Why User Requirements is Correct:**\nUAT represents the final validation gate where real users verify whether the system fulfills their operational needs as defined in the **User Requirements** specification."
                }
            ]
        },
        {
            "title": "Module 3: Defect Cost Escalation (Boehm's Law)",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Why is late discovery so lethal? In *'Software Engineering Economics'*, Barry Boehm established what is now known as **Boehm's Law of Defect Cost Amplification**: the cost of finding and fixing a defect increases exponentially as software progresses through the lifecycle."
                },
                {
                    "type": "concept",
                    "title": "Cost of Change Multipliers",
                    "content": "| Phase Detected | Relative Cost to Fix | Why Cost Multiplies |\n|---|---|---|\n| **Requirements** | 1x | Update a sentence in the SRS doc |\n| **Design** | 3x - 5x | Redraw UML diagrams & adjust interface contracts |\n| **Coding** | 10x | Rewrite classes and update unit test mocks |\n| **Integration / Testing** | 40x - 50x | Rerun regression test suites; rebuild staging environments |\n| **Production Release** | 100x - 200x | Emergency patches, database migrations, legal liabilities, customer loss |"
                },
                {
                    "type": "code_lab",
                    "title": "Defect Cost Escalation Calculator",
                    "instructions": "Implement `calculate_remediation_cost(defects_by_phase, phase_multipliers)` to calculate the financial impact of defect escape rates.",
                    "starter_code": """def calculate_remediation_cost(defects_by_phase: dict, phase_multipliers: dict, base_cost: float = 100.0) -> dict:
    \"\"\"
    Compute total cost to repair escaped defects across lifecycle phases.
    
    defects_by_phase: dict of {phase_name: int_count}
    phase_multipliers: dict of {phase_name: float_multiplier}
    base_cost: cost to fix defect during requirements phase (default $100)
    
    Returns dict:
      - 'cost_per_phase': {phase: float_total_cost}
      - 'total_remediation_cost': float
      - 'highest_cost_phase': str (name of phase with maximum total dollar impact)
    \"\"\"
    # TODO: Implement defect cost calculation
    pass
""",
                    "solution_code": """def calculate_remediation_cost(defects_by_phase: dict, phase_multipliers: dict, base_cost: float = 100.0) -> dict:
    cost_per_phase = {}
    for phase, count in defects_by_phase.items():
        multiplier = phase_multipliers.get(phase, 1.0)
        cost_per_phase[phase] = round(count * multiplier * base_cost, 2)
        
    total_cost = round(sum(cost_per_phase.values()), 2)
    highest_phase = max(cost_per_phase.items(), key=lambda item: item[1])[0] if cost_per_phase else ""
    
    return {
        'cost_per_phase': cost_per_phase,
        'total_remediation_cost': total_cost,
        'highest_cost_phase': highest_phase
    }
""",
                    "test_code": """defects = {'requirements': 10, 'design': 8, 'coding': 5, 'testing': 3, 'production': 2}
multipliers = {'requirements': 1.0, 'design': 5.0, 'coding': 10.0, 'testing': 40.0, 'production': 150.0}
res = calculate_remediation_cost(defects, multipliers, base_cost=100.0)

assert res['cost_per_phase']['requirements'] == 1000.0
assert res['cost_per_phase']['production'] == 30000.0
assert res['highest_cost_phase'] == 'production'
assert res['total_remediation_cost'] == 52000.0
print("Defect escalation tests passed successfully!")
""",
                    "why_works": "**Why This Solution Works:**\nBoehm's Law demonstrates that even a tiny number of escaped defects in production ($N=2$) can dwarf the cost of dozens of defects caught in upstream phases because fixing production code requires hotfix deployments, database schema rollbacks, customer support, and regression sweeps.",
                    "alternatives": "**Alternative Approaches & Trade-offs:**\n- **Static Analysis Shift-Left:** Catching syntax, nullability, and security defects during IDE editing (Cost $\\approx 0.1\\times$).\n- **Chaos Engineering:** Intentionally injecting faults into production staging to validate resilience before customer exposure.",
                    "edge_cases": "**Edge Cases & Failure Modes:**\n- `defects_by_phase` is empty: Returns total cost 0.0 and empty string for highest phase.\n- Unknown phase key: Gracefully falls back to default multiplier $1.0$."
                }
            ]
        },
        {
            "title": "Module 4: When Sequential Models Are Still Appropriate",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Despite modern preference for Agile, Waterfall and the V-Model remain mandatory or optimal in specific industry niches. Knowing when to use sequential engineering is a mark of professional architectural maturity."
                },
                {
                    "type": "concept",
                    "title": "Criteria for Selecting Sequential Methodologies",
                    "content": "Waterfall and V-Model thrive under five strict conditions:\n1. **Fixed, Immutable Requirements:** The problem domain is completely understood and will not change (e.g., implementing an internationally standardized protocol like USB 4.0 or TLS 1.3).\n2. **High Cost of Failure:** Life-critical, avionics, medical, or railway interlocking software (DO-178C, ISO 26262, IEC 62304).\n3. **Hardware-Coordinated Deadlines:** Software must ship burned into ASIC microchips whose fabrication cannot be patched post-production.\n4. **Stable Technology Stack:** Well-understood tools, mature compilers, and well-known libraries.\n5. **Strict Regulatory Audits:** Government or aerospace regulators require certified end-to-end traceability before flight clearance."
                },
                {
                    "type": "interactive",
                    "title": "Methodology Selection Challenge",
                    "question": "For which of the following projects would a strict V-Model process with formal phase gates be MOST justifiable?",
                    "options": [
                        "An early-stage social media photo sharing app testing consumer market fit.",
                        "A flight control computer firmware update for commercial passenger jets under FAA DO-178C certification.",
                        "An internal company holiday party RSVP web application.",
                        "A machine learning recommendation engine updated daily based on user clicks."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nCommercial passenger flight control firmware is safety-critical; failure can cause loss of life. Certification authorities like the FAA mandate formal traceability from system requirements down to verified assembly code (DO-178C Level A), where strict V-Model verification matrices are industry law."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Safety Standard Challenge",
                    "question": "The primary international safety standard for automotive functional safety software is ISO _____.\n\nAnswer: _____",
                    "answer": "26262",
                    "alternatives": ["26262", "ISO 26262", "ISO26262"],
                    "explanation": "**Why ISO 26262 is Correct:**\n**ISO 26262** defines the Automotive Safety Integrity Level (ASIL A through D) and prescribes rigorous V-model verification and validation activities for road vehicles."
                }
            ]
        }
    ]
}

# CASE 02: The Risk Spiral (Spiral & Prototyping)
PART1_CASES["2"] = {
    "title": "Case 02: The Risk Spiral",
    "episodes": [
        {
            "title": "Module 1: Barry Boehm's Spiral Lifecycle",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "In 1986, Barry Boehm proposed the **Spiral Model** to marry the structured discipline of Waterfall with the iterative agility of prototyping. Rather than marching blindly along a linear path, development moves through outward concentric cycles driven entirely by **Risk Analysis**."
                },
                {
                    "type": "objective",
                    "title": "Module Objective",
                    "content": "Master the 4 quadrants of the Spiral Model, understand how risk evaluation drives iteration boundaries, and distinguish between throwaway and evolutionary prototypes."
                },
                {
                    "type": "concept",
                    "title": "The Four Quadrants of Every Spiral Cycle",
                    "content": "Every revolution around the spiral traverses four distinct quadrants:\n1. **Quadrant 1 (Top-Left) — Determine Objectives:** Identify project goals, alternative paths, and operational constraints.\n2. **Quadrant 2 (Top-Right) — Identify & Resolve Risks:** Evaluate alternatives; identify technical and business risks; build prototypes and simulations to neutralize top risks.\n3. **Quadrant 3 (Bottom-Right) — Develop & Verify:** Implement the next-level product artifact (benchmarks, detailed design, or functional code) and verify against benchmarks.\n4. **Quadrant 4 (Bottom-Left) — Plan Next Phase:** Review progress with stakeholders, secure commitments, and formulate the plan for the next loop."
                },
                {
                    "type": "visual",
                    "title": "The 4 Quadrants of the Spiral Model",
                    "code": """graph TD
  subgraph Q1 ["Q1: Determine Objectives & Constraints"]
    O1["Define Functional Targets"]
    O2["Identify Architectural Constraints"]
  end
  subgraph Q2 ["Q2: Evaluate Alternatives & Mitigate Risks"]
    R1["Risk Identification & Ranking"]
    R2["Construct Prototypes & Benchmarks"]
  end
  subgraph Q3 ["Q3: Develop & Verify Next-Level Product"]
    D1["System Implementation"]
    D2["Rigorous Verification & Testing"]
  end
  subgraph Q4 ["Q4: Review & Plan Next Phase"]
    P1["Stakeholder Milestone Review"]
    P2["Commitment for Next Cycle"]
  end
  Q1 --> Q2 --> Q3 --> Q4 --> Q1
  style Q1 fill:#0f172a,stroke:#3b82f6
  style Q2 fill:#3f1a1a,stroke:#ef4444
  style Q3 fill:#1e1b4b,stroke:#6366f1
  style Q4 fill:#064e3b,stroke:#10b981"""
                },
                {
                    "type": "interactive",
                    "title": "Spiral Model Driving Force Challenge",
                    "question": "What is the primary driving mechanism that determines whether a project proceeds to the next cycle in the Spiral Model?",
                    "options": [
                        "Exhaustion of the allocated calendar duration for that month.",
                        "Rigorous risk assessment and resolution of critical project risks.",
                        "Delivery of a 100% completed graphical user interface.",
                        "Lines of code written per software engineer per week."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nThe hallmark of Boehm's Spiral Model is that it is **risk-driven**. If critical risks (performance, feasibility, market fit) cannot be satisfactorily resolved in Quadrant 2 via prototypes or benchmarks, the project may be safely terminated before capital is wasted."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Quadrant Focus Challenge",
                    "question": "In the Spiral Model, prototypes, simulations, and benchmarking are primarily executed in Quadrant _____ to evaluate alternatives.\n\nAnswer: _____",
                    "answer": "2",
                    "alternatives": ["2", "Two", "two", "Quadrant 2", "second"],
                    "explanation": "**Why Quadrant 2 is Correct:**\n**Quadrant 2** is dedicated to Risk Assessment and Alternative Evaluation: this is where throwaway prototypes and technical spikes are built to prove feasibility."
                }
            ]
        },
        {
            "title": "Module 2: Throwaway vs. Evolutionary Prototyping",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Prototyping is software engineering's wind tunnel. However, confusing a disposable proof-of-concept with a production foundation has caused some of the worst architectural collapses in history."
                },
                {
                    "type": "concept",
                    "title": "Prototyping Paradigms",
                    "content": "### 1. Throwaway (Rapid) Prototyping\n- **Purpose:** Clarify poorly understood user requirements or test technical feasibility (a 'spike').\n- **Lifecycle:** Built quickly with hardcoded data and minimal architecture, demonstrated to users/stakeholders, documented, and **discarded**.\n- **Danger:** Stakeholders see a working UI and demand: *'Just ship this to production tomorrow!'*\n\n### 2. Evolutionary Prototyping\n- **Purpose:** Deliver a functional core system that incrementally evolves into the final production product.\n- **Lifecycle:** Built from day one with production-grade engineering, automated testing, and clean architecture; new features are added in successive releases."
                },
                {
                    "type": "visual",
                    "title": "Throwaway vs. Evolutionary Lifecycle Paths",
                    "code": """graph LR
  subgraph Throwaway ["Throwaway Prototyping (Exploratory)"]
    T_REQ["Vague Requirements"] --> T_SPIKE["Quick-and-Dirty Hack / Spike"]
    T_SPIKE --> T_FEED["Extract Learned Specs"]
    T_FEED --> T_TRASH["Discard Prototype Code 🗑️"]
    T_TRASH --> T_CLEAN["Engineer Production System Cleanly"]
  end
  subgraph Evolutionary ["Evolutionary Prototyping (Iterative)"]
    E_CORE["Core High-Priority Specs"] --> E_BUILD["High-Quality Minimal Architecture"]
    E_BUILD --> E_TEST["Continuous Automated QA"]
    E_TEST --> E_EVOLVE["Incorporate User Feedback & Evolve"]
  end
  style Throwaway fill:#3f1a1a,stroke:#ef4444
  style Evolutionary fill:#064e3b,stroke:#10b981"""
                },
                {
                    "type": "interactive",
                    "title": "Prototyping Pitfall Challenge",
                    "question": "What is the primary danger when management mistakes a Throwaway Prototype for an Evolutionary Prototype?",
                    "options": [
                        "The developers will spend too much time writing automated unit tests.",
                        "Disposable code lacking security, error handling, and scalability is rushed into production, creating massive technical debt.",
                        "The software will become too modular and decoupled.",
                        "End users will reject the user interface because it looks too polished."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nThrowaway prototypes deliberately ignore security, concurrency, input validation, and database constraints. If pressed into production, they crash under real loads and expose critical security vulnerabilities."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Agile Terminology Challenge",
                    "question": "In modern Agile terminology, a timeboxed throwaway experiment built to explore technical feasibility is called a technical _____.\n\nAnswer: _____",
                    "answer": "Spike",
                    "alternatives": ["Spike", "spike", "Technical Spike", "technical spike"],
                    "explanation": "**Why Spike is Correct:**\nAn **Extreme Programming (XP) Spike** is a short, focused experiment where developers write disposable code to answer a specific technical question or estimate a story."
                }
            ]
        },
        {
            "title": "Module 3: Quantitative Risk Exposure (RE)",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "To prioritize which risks to mitigate in Quadrant 2, software project managers use formal quantitative risk metrics. The fundamental metric is **Risk Exposure (RE)**, also called Risk Impact."
                },
                {
                    "type": "concept",
                    "title": "The Risk Exposure Formula",
                    "content": "$$\\text{Risk Exposure (RE)} = P(\\text{Loss}) \\times \\text{Cost}(\\text{Loss})$$\n\nWhere:\n- $P(\\text{Loss})$ is the probability of the risk event occurring ($0.0 \\le P \\le 1.0$).\n- $\\text{Cost}(\\text{Loss})$ is the financial or operational impact if it occurs (in dollars, person-hours, or days of delay).\n\nRisks with the highest Risk Exposure must be attacked first in the next iteration."
                },
                {
                    "type": "code_lab",
                    "title": "Risk Exposure Prioritization Engine",
                    "instructions": "Implement `prioritize_project_risks(risks)` that computes Risk Exposure for a portfolio of project risks and sorts them for immediate mitigation in the next Spiral cycle.",
                    "starter_code": """def prioritize_project_risks(risks: list) -> list:
    \"\"\"
    Calculate Risk Exposure (RE) for each risk item and return the list
    sorted from highest exposure to lowest exposure.
    
    Each item in risks is a dict:
      {'id': str, 'name': str, 'probability': float, 'impact_cost': float}
      
    Returns list of dicts with:
      {'id': str, 'name': str, 'exposure': float (rounded to 2 decimals), 'priority': int (1-based)}
    \"\"\"
    # TODO: Implement risk calculation and sorting
    pass
""",
                    "solution_code": """def prioritize_project_risks(risks: list) -> list:
    evaluated = []
    for r in risks:
        prob = r.get('probability', 0.0)
        impact = r.get('impact_cost', 0.0)
        exposure = round(prob * impact, 2)
        evaluated.append({
            'id': r['id'],
            'name': r['name'],
            'exposure': exposure
        })
        
    evaluated.sort(key=lambda x: x['exposure'], reverse=True)
    
    for rank, item in enumerate(evaluated, start=1):
        item['priority'] = rank
        
    return evaluated
""",
                    "test_code": """risks = [
    {'id': 'R1', 'name': 'Third-party API deprecation', 'probability': 0.20, 'impact_cost': 50000.0},
    {'id': 'R2', 'name': 'Database scalability bottleneck', 'probability': 0.60, 'impact_cost': 80000.0},
    {'id': 'R3', 'name': 'Key architect departure', 'probability': 0.10, 'impact_cost': 120000.0}
]
res = prioritize_project_risks(risks)

assert res[0]['id'] == 'R2'
assert res[0]['exposure'] == 48000.0
assert res[0]['priority'] == 1
assert res[1]['id'] == 'R3'
assert res[1]['exposure'] == 12000.0
assert res[2]['id'] == 'R1'
assert res[2]['exposure'] == 10000.0
print("Risk prioritization engine tests passed successfully!")
""",
                    "why_works": "**Why This Solution Works:**\nPrioritizing by exposure ensures that high-probability moderate-impact events (e.g. database bottleneck: $0.60 \\times \\$80k = \\$48k$) take precedence over low-probability high-impact events ($0.10 \\times \\$120k = \\$12k$), aligning engineering effort with expected financial loss.",
                    "alternatives": "**Alternative Approaches & Trade-offs:**\n- **Qualitative Risk Matrix (5x5):** Classifies likelihood and severity into Low/Med/High bands. Easier for non-technical stakeholders to grasp, but prone to subjective scoring.\n- **Value at Risk (VaR):** Financial model assessing tail-risk percentiles under non-normal distributions.",
                    "edge_cases": "**Edge Cases & Failure Modes:**\n- Zero probability: Risk Exposure evaluates to 0.0 and correctly receives lowest priority.\n- Tie in exposure: Python's `sort` preserves original insertion order (stable sort)."
                }
            ]
        },
        {
            "title": "Module 4: Spiral vs. Waterfall Trade-off Matrix",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Choosing between Spiral and Waterfall is not a matter of modern vs ancient; it is a question of **uncertainty vs repeatability**."
                },
                {
                    "type": "concept",
                    "title": "Lifecycle Decision Comparison",
                    "content": "| Attribute | Waterfall | Spiral Model |\n|---|---|---|\n| **Primary Driver** | Documented milestones & phase gates | Risk analysis & mitigation |\n| **Requirements** | Must be locked upfront | Discovered iteratively across cycles |\n| **Cost Profile** | High downstream surprise costs | Higher upfront risk analysis costs |\n| **Customer Involvement** | At start (specs) and end (acceptance) | At the end of every spiral quadrant cycle |\n| **Management Complexity** | Low (linear tracking via Gantt charts) | High (requires experienced risk analysts) |\n| **Best For** | Low-uncertainty, regulated systems | High-uncertainty, R&D, unprecedented systems |"
                },
                {
                    "type": "interactive",
                    "title": "Lifecycle Governance Challenge",
                    "question": "Why is the Spiral Model rarely used on small, low-budget software projects?",
                    "options": [
                        "It requires writing code in C++ rather than Python.",
                        "The overhead of continuous risk analysis, prototyping, and multi-quadrant reviews exceeds the total budget of small projects.",
                        "It strictly forbids automated testing.",
                        "It requires at least 500 developers to form teams."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nThe Spiral Model requires significant risk management expertise, formal prototype reviews, and stakeholder governance at each cycle. For a small 2-month project, this overhead would swallow more time than simply building the software."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Model Author Challenge",
                    "question": "The computer scientist who created both the Spiral Model and the COCOMO estimation model was Barry _____.\n\nAnswer: _____",
                    "answer": "Boehm",
                    "alternatives": ["Boehm", "boehm", "Barry Boehm", "barry boehm"],
                    "explanation": "**Why Barry Boehm is Correct:**\n**Dr. Barry Boehm** was one of the most influential figures in software engineering, introducing the Spiral Model, COCOMO, and foundational empirical studies on software economics."
                }
            ]
        }
    ]
}

# CASE 03: The Agile Manifesto (Agile & Lean)
PART1_CASES["3"] = {
    "title": "Case 03: The Agile Manifesto",
    "episodes": [
        {
            "title": "Module 1: The Snowbird Summit of 2001",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "In February 2001, seventeen software practitioners met at the The Lodge at Snowbird ski resort in Utah. Frustrated by heavyweight, plan-driven methodologies (such as RUP and ISO 9000-based processes) that produced massive binders of documentation while projects collapsed, they sought common ground. Together, they authored the **Manifesto for Agile Software Development**."
                },
                {
                    "type": "objective",
                    "title": "Module Objective",
                    "content": "Master the 4 core values and 12 principles of Agile, differentiate Agile from ad-hoc cowboy coding, and understand Lean waste reduction in software workflows."
                },
                {
                    "type": "concept",
                    "title": "The 4 Core Agile Values",
                    "content": "The manifesto established four value pairs:\n\n1. **Individuals and interactions** over *processes and tools*\n2. **Working software** over *comprehensive documentation*\n3. **Customer collaboration** over *contract negotiation*\n4. **Responding to change** over *following a plan*\n\n> *'That is, while there is value in the items on the right, we value the items on the left more.'*"
                },
                {
                    "type": "visual",
                    "title": "The Agile Value Spectrum",
                    "code": """graph LR
  subgraph AgileValues ["Higher Valued (Adaptive Engine)"]
    V1["Individuals & Interactions"]
    V2["Working Software"]
    V3["Customer Collaboration"]
    V4["Responding to Change"]
  end
  subgraph TraditionalValues ["Lower Valued (Bureaucratic Overhead)"]
    T1["Processes & Tools"]
    T2["Comprehensive Documentation"]
    T3["Contract Negotiation"]
    T4["Following a Rigid Plan"]
  end
  V1 -.->|"Prioritized over"| T1
  V2 -.->|"Prioritized over"| T2
  V3 -.->|"Prioritized over"| T3
  V4 -.->|"Prioritized over"| T4
  style AgileValues fill:#064e3b,stroke:#10b981
  style TraditionalValues fill:#1e1b4b,stroke:#6366f1"""
                },
                {
                    "type": "interactive",
                    "title": "Agile Value Interpretation Challenge",
                    "question": "What is the common misconception about the Agile Manifesto statement 'Working software over comprehensive documentation'?",
                    "options": [
                        "It means Agile teams should never write tests.",
                        "It implies Agile teams must eliminate all documentation and rely strictly on oral memory.",
                        "It means documentation is valuable only when it directly enables the delivery and maintenance of working software, rather than serving as an end in itself.",
                        "It mandates that all design must be written in markdown format."
                    ],
                    "answer": 2,
                    "explanation": "**Why this is Correct:**\nThe manifesto explicitly clarifies: *'while there is value in the items on the right, we value the items on the left more'*. Agile does not prohibit architecture documents or API contracts; it eliminates bureaucratic documentation that does not contribute to delivering functional software."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Manifesto Signatory Challenge",
                    "question": "The total number of software visionaries who met in Utah to sign the Agile Manifesto in 2001 was _____.\n\nAnswer: _____",
                    "answer": "17",
                    "alternatives": ["17", "seventeen", "Seventeen"],
                    "explanation": "**Why 17 is Correct:**\n**17** practitioners signed the manifesto, including Kent Beck, Martin Fowler, Ward Cunningham, Robert C. Martin (Uncle Bob), Ken Schwaber, and Jeff Sutherland."
                }
            ]
        },
        {
            "title": "Module 2: The 12 Principles of Agile",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Supporting the 4 values are the **12 Principles of Agile Software**. These principles articulate how teams should structure delivery cadences, welcome requirement shifts, and foster self-organizing teams."
                },
                {
                    "type": "concept",
                    "title": "Key Agile Principles Highlight",
                    "content": "- **Principle 1:** Our highest priority is to satisfy the customer through early and continuous delivery of valuable software.\n- **Principle 2:** Welcome changing requirements, even late in development. Agile processes harness change for the customer's competitive advantage.\n- **Principle 3:** Deliver working software frequently, from a couple of weeks to a couple of months, with a preference to the shorter timescale.\n- **Principle 7:** Working software is the primary measure of progress.\n- **Principle 8:** Agile processes promote sustainable development. Sponsors, developers, and users should be able to maintain a constant pace indefinitely (no death marches)."
                },
                {
                    "type": "visual",
                    "title": "The Agile Fast-Feedback Loop",
                    "code": """graph TD
  subgraph Customer ["Customer & Market Domain"]
    FEEDBACK["Live Operational Feedback & Pivot"]
  end
  subgraph AgileLoop ["Agile Iteration (1 to 2 Weeks)"]
    PLAN["Sprint Planning"] --> DEV["Test-Driven Construction"]
    DEV --> DEMO["Sprint Review & Working Demo"]
    DEMO --> RETRO["Continuous Retrospective Refactoring"]
  end
  DEMO --> FEEDBACK --> PLAN
  style Customer fill:#0f172a,stroke:#3b82f6
  style AgileLoop fill:#064e3b,stroke:#10b981"""
                },
                {
                    "type": "interactive",
                    "title": "Agile Metric Challenge",
                    "question": "According to Principle 7 of the Agile Manifesto, what is the primary measure of progress?",
                    "options": [
                        "Number of lines of code written.",
                        "Total pages of approved specification documents.",
                        "Working software delivered to users.",
                        "Percentage of allocated budget consumed."
                    ],
                    "answer": 2,
                    "explanation": "**Why this is Correct:**\nPrinciple 7 states unambiguously: **'Working software is the primary measure of progress.'** Status reports, Gantt charts, and architecture slides are vanity metrics until tested, working software is running."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Team Pacing Challenge",
                    "question": "Principle 8 emphasizes _____ development, where developers and sponsors can maintain a constant pace indefinitely without burnout.\n\nAnswer: _____",
                    "answer": "Sustainable",
                    "alternatives": ["Sustainable", "sustainable", "Sustainable Pace"],
                    "explanation": "**Why Sustainable is Correct:**\n**Sustainable development** rejects the chronic crunch ('death marches') common in Waterfall, recognizing that exhausted engineers produce buggy code that destroys delivery velocity."
                }
            ]
        },
        {
            "title": "Module 3: Lean Software Development & The 7 Wastes (Muda)",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Mary and Tom Poppendieck translated the **Toyota Production System (TPS)** into software engineering, establishing **Lean Software Development**. Lean focuses relentlessly on eliminating *Muda* (Waste) to optimize end-to-end value flow."
                },
                {
                    "type": "concept",
                    "title": "The 7 Software Wastes (Poppendieck Mapping)",
                    "content": "1. **Partially Done Work:** Unmerged branches, unreviewed PRs, and untested code that sits idle.\n2. **Extra Features (Gold Plating):** Features built because 'they might be cool', but which 80% of users never touch.\n3. **Relearning:** Lost tribal knowledge, lack of automated regression tests, and poor documentation causing engineers to solve the same bug twice.\n4. **Task Switching:** Multitasking across 4 projects, incurring high cognitive context-switching penalties.\n5. **Waiting:** Waiting for database approvals, QA environment provisioning, or design sign-offs.\n6. **Motion (Handoffs):** Passing documents from business analyst to architect to coder to tester, losing nuance at every handoff.\n7. **Defects:** Bugs that escape into staging or production, requiring emergency interrupt work."
                },
                {
                    "type": "code_lab",
                    "title": "Lean Waste Analyzer Lab",
                    "instructions": "Implement `calculate_process_cycle_efficiency(active_coding_hours, wait_hours)` to compute Process Cycle Efficiency (PCE), measuring how much of lead time is genuine value creation versus idle waste.",
                    "starter_code": """def calculate_process_cycle_efficiency(value_add_hours: float, non_value_add_hours: float) -> dict:
    \"\"\"
    Compute Process Cycle Efficiency (PCE) from Lean Manufacturing.
    
    PCE = (Value Add Time / Total Lead Time) * 100%
    Total Lead Time = Value Add Time + Non Value Add (Wait/Friction) Time
    
    Returns dict:
      - 'value_add_hours': float
      - 'total_lead_time_hours': float
      - 'pce_percent': float (rounded to 2 decimals)
      - 'lean_health': str ('World Class' if PCE >= 25%, 'Average' if 10% <= PCE < 25%, 'Wasteful' if PCE < 10%)
    \"\"\"
    # TODO: Implement PCE calculation
    pass
""",
                    "solution_code": """def calculate_process_cycle_efficiency(value_add_hours: float, non_value_add_hours: float) -> dict:
    total_lead = value_add_hours + non_value_add_hours
    if total_lead <= 0:
        return {'value_add_hours': 0.0, 'total_lead_time_hours': 0.0, 'pce_percent': 0.0, 'lean_health': 'Wasteful'}
        
    pce = round((value_add_hours / total_lead) * 100.0, 2)
    
    if pce >= 25.0:
        health = 'World Class'
    elif pce >= 10.0:
        health = 'Average'
    else:
        health = 'Wasteful'
        
    return {
        'value_add_hours': round(value_add_hours, 2),
        'total_lead_time_hours': round(total_lead, 2),
        'pce_percent': pce,
        'lean_health': health
    }
""",
                    "test_code": """res = calculate_process_cycle_efficiency(12.0, 48.0)
assert res['total_lead_time_hours'] == 60.0
assert res['pce_percent'] == 20.0
assert res['lean_health'] == 'Average'

res2 = calculate_process_cycle_efficiency(5.0, 95.0)
assert res2['pce_percent'] == 5.0
assert res2['lean_health'] == 'Wasteful'
print("Lean PCE tests passed successfully!")
""",
                    "why_works": "**Why This Solution Works:**\nIn most traditional software delivery pipelines, true value-add coding time accounts for less than 10% of total lead time; the remaining 90% is spent waiting for approvals, unblocking merge conflicts, or waiting for manual QA.",
                    "alternatives": "**Alternative Approaches & Trade-offs:**\n- **Value Stream Mapping (VSM):** A comprehensive visual modeling technique that records cycle time, uptime, and changeover time for each workstation in the pipeline.\n- **DORA Lead Time for Changes:** Measures the elapsed time from code commit to running in production.",
                    "edge_cases": "**Edge Cases & Failure Modes:**\n- Zero lead time: Returns zero percent without crashing on division by zero.\n- Zero wait time ($PCE = 100\\%$): Correctly categorized as 'World Class'."
                }
            ]
        },
        {
            "title": "Module 4: Agile vs. Cowboy Coding: The Discipline Distinction",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "A destructive myth claims that Agile means *'no rules, no architecture, and no discipline'*. In reality, disciplined Agile development requires **more** technical rigor than Waterfall."
                },
                {
                    "type": "concept",
                    "title": "Cowboy Coding vs. Disciplined Agile",
                    "content": "| Characteristic | Cowboy Coding | Disciplined Agile |\n|---|---|---|\n| **Planning** | No plan; ad-hoc whim | Continuous adaptive planning (backlogs, sprints) |\n| **Testing** | Manual trial-and-error in production | 100% automated CI/CD test suites & TDD |\n| **Architecture** | Uncontrolled spaghetti code | Emergent architecture with continuous refactoring |\n| **Transparency** | Black box; individual silo | Open daily standups, burn-down metrics, public demos |\n| **Customer Sync** | None until delivery disaster | Direct customer validation every 1-2 weeks |"
                },
                {
                    "type": "interactive",
                    "title": "Methodology Hygiene Challenge",
                    "question": "A team claims to be 'Agile' because they don't write automated tests, skip design discussions, and change database schemas directly on production on Friday afternoon. How should this be classified?",
                    "options": [
                        "Pure Extreme Programming.",
                        "Uncontrolled Cowboy Coding disguised under the Agile label.",
                        "Standard Scrum practice for high-velocity teams.",
                        "Continuous Deployment under Lean principles."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nAgile requires rigorous technical discipline (test automation, continuous integration, refactoring). Skipping tests and hacking production without safety nets is reckless **cowboy coding**, the exact antipattern that caused the 1968 Software Crisis."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Japanese Concept Challenge",
                    "question": "The Japanese Lean term for non-value-adding waste that must be systematically eliminated from software workflows is _____.\n\nAnswer: _____",
                    "answer": "Muda",
                    "alternatives": ["Muda", "muda"],
                    "explanation": "**Why Muda is Correct:**\nIn Lean methodology, **Muda** is any activity that consumes resources (time, money, compute) without delivering value to the customer."
                }
            ]
        }
    ]
}

# CASE 04: The Sprints of Chaos (Scrum & Kanban)
PART1_CASES["4"] = {
    "title": "Case 04: The Sprints of Chaos",
    "episodes": [
        {
            "title": "Module 1: The Scrum Framework: Roles, Ceremonies, Artifacts",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Formulated by Ken Schwaber and Jeff Sutherland, **Scrum** is the world's most widely adopted Agile framework. It operates on empirical process control: decisions are based on observation, experimentation, and transparency."
                },
                {
                    "type": "objective",
                    "title": "Module Objective",
                    "content": "Master the 3 Scrum Roles, 5 Ceremonies, and 3 Artifacts; calibrate story points and velocity; and understand Kanban Work-in-Progress (WIP) limits via Little's Law."
                },
                {
                    "type": "concept",
                    "title": "The Scrum Triad (3-5-3)",
                    "content": "### 3 Roles\n1. **Product Owner (PO):** Maximizes value; owns and prioritizes the Product Backlog.\n2. **Scrum Master (SM):** Serves the team; removes impediments; coaches Scrum principles.\n3. **Developers:** Self-organizing cross-functional professionals who build the increment.\n\n### 5 Ceremonies (Events)\n1. **Sprint Planning:** Commit to sprint goal and scope.\n2. **Daily Scrum (Standup):** 15-minute sync on progress and blockers.\n3. **Sprint Review:** Demonstrate working product increment to stakeholders.\n4. **Sprint Retrospective:** Inspect team dynamics and enact process improvements.\n5. **The Sprint Itself:** Fixed timebox (1 to 4 weeks).\n\n### 3 Artifacts\n1. **Product Backlog** (Commitment: Product Goal)\n2. **Sprint Backlog** (Commitment: Sprint Goal)\n3. **Increment** (Commitment: Definition of Done - DoD)"
                },
                {
                    "type": "visual",
                    "title": "The Complete Scrum Cadence",
                    "code": """graph LR
  subgraph Inputs ["Backlog Input"]
    PB["Product Backlog (Owned by PO)"]
  end
  subgraph SprintExecution ["Sprint Timebox (1-4 Weeks)"]
    PLAN["Sprint Planning"] --> SB["Sprint Backlog"]
    SB --> SPRINT["Daily Scrum (15 min)"]
    SPRINT --> INC["Working Potentially Shippable Increment"]
  end
  subgraph ReviewLoop ["Feedback Loops"]
    INC --> REV["Sprint Review (Demo)"]
    REV --> RETRO["Sprint Retrospective"]
    RETRO -.->|"Process Improvements"| PLAN
  end
  PB --> PLAN
  style Inputs fill:#0f172a,stroke:#3b82f6
  style SprintExecution fill:#1e1b4b,stroke:#6366f1
  style ReviewLoop fill:#064e3b,stroke:#10b981"""
                },
                {
                    "type": "interactive",
                    "title": "Scrum Role Boundaries Challenge",
                    "question": "A CEO approaches a developer mid-sprint and orders them to drop their committed sprint tasks to immediately build an unvetted feature. Who is responsible for protecting the team from this interruption?",
                    "options": [
                        "The Lead Architect.",
                        "The Scrum Master shields the team from external disruptions, while redirecting the CEO to negotiate with the Product Owner.",
                        "The developer should work unpaid overtime at night to complete both.",
                        "The QA Manager."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nA core responsibility of the **Scrum Master** is safeguarding the team's sprint commitment from external scope thrash. Any new feature requests must be vetted by the **Product Owner** and prioritized into future sprints."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Scrum Quality Standard Challenge",
                    "question": "The formal checklist of engineering standards (e.g., tests pass, code reviewed, deployed to staging) that an item must meet to be considered completed is the Definition of _____ (DoD).\n\nAnswer: _____",
                    "answer": "Done",
                    "alternatives": ["Done", "done", "DoD"],
                    "explanation": "**Why Done is Correct:**\nThe **Definition of Done (DoD)** provides an objective quality gate ensuring that 'done' means truly production-ready, not merely 'coded on my laptop'."
                }
            ]
        },
        {
            "title": "Module 2: Estimation, Story Points & Team Velocity",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Estimating software in hours is notoriously inaccurate because humans are terrible at absolute estimation but excellent at **relative sizing**. Agile teams use **Story Points** and modified Fibonacci sequences (1, 2, 3, 5, 8, 13, 21)."
                },
                {
                    "type": "concept",
                    "title": "Story Points & Planning Poker",
                    "content": "- **Story Points:** A dimensionless measure combining **effort**, **complexity**, and **uncertainty**.\n- **Reference Story:** A known, well-understood baseline task is assigned 2 points; all other stories are sized relative to it.\n- **Planning Poker:** Developers simultaneously reveal cards to prevent anchoring bias. Outliers (highest and lowest estimators) explain their reasoning before re-voting.\n- **Velocity:** The total number of story points successfully delivered (meeting the Definition of Done) per sprint."
                },
                {
                    "type": "visual",
                    "title": "Burn-Down Chart Trajectory",
                    "code": """graph TD
  subgraph SprintBurnDown ["Sprint Burn-Down Dynamics"]
    DAY0["Day 0: 50 Story Points Committed"] --> DAY3["Day 3: 42 Points Remaining"]
    DAY3 --> DAY7["Day 7: 24 Points Remaining (On Track)"]
    DAY7 --> DAY10["Day 10: 0 Points Remaining (Goal Met 🎯)"]
    DAY3 -.->|"Scope Creep Danger Line"| DANGER["Day 7: 58 Points (Blockers & New Scope ⚠️)"]
  end
  style SprintBurnDown fill:#1e1b4b,stroke:#6366f1
  style DANGER fill:#3f1a1a,stroke:#ef4444"""
                },
                {
                    "type": "interactive",
                    "title": "Velocity Antipattern Challenge",
                    "question": "A vice president notices Team A has a velocity of 60 points while Team B has a velocity of 30 points, and concludes Team A is twice as productive. Why is this comparison invalid?",
                    "options": [
                        "Team B might be writing in a more modern programming language.",
                        "Story points are an internal relative calibration unique to each team; comparing raw point totals across different teams is meaningless.",
                        "Team A is probably working weekends.",
                        "Velocity must always be multiplied by the team's salary to determine productivity."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nStory points have no universal metric unit. Team A's 5-point story might represent the exact same effort as Team B's 2-point story. Comparing cross-team velocity incentivizes point inflation (story point gaming) without increasing delivered customer value."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Agile Tool Challenge",
                    "question": "The graphical chart that plots remaining work (in story points) on the Y-axis against time (in sprint days) on the X-axis is the Sprint _____ chart.\n\nAnswer: _____",
                    "answer": "Burn-down",
                    "alternatives": ["Burn-down", "Burndown", "burn-down", "burndown"],
                    "explanation": "**Why Burndown is Correct:**\nA **Sprint Burn-Down Chart** tracks daily progress towards the sprint goal, making scope creep or stalled tickets immediately visible."
                }
            ]
        },
        {
            "title": "Module 3: Kanban & Little's Law (WIP Limits)",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "While Scrum packages work into fixed timeboxed sprints, **Kanban** focuses on continuous flow. Originating from David J. Anderson's work in software, Kanban's core mechanism is the enforcement of **Work-in-Progress (WIP) Limits**."
                },
                {
                    "type": "concept",
                    "title": "Little's Law in Software Engineering",
                    "content": "From operations research, **Little's Law** states:\n$$\\text{Cycle Time} = \\frac{\\text{Work-in-Progress (WIP)}}{\\text{Throughput}}$$\n\n### Practical Implication:\n- When a team starts 20 features simultaneously (high WIP), work sits waiting in queues, multitasking overhead explodes, and Cycle Time stretches from 3 days to 40 days.\n- **To deliver faster, stop starting and start finishing!** Reducing WIP limits directly slashes lead time."
                },
                {
                    "type": "visual",
                    "title": "Kanban Board with Strict WIP Limits",
                    "code": """graph LR
  subgraph BacklogCol ["1. Backlog (No Limit)"]
    B1["User Story A"]
    B2["User Story B"]
  end
  subgraph InProgressCol ["2. In-Progress (WIP Limit: 3)"]
    P1["Task #101"]
    P2["Task #102"]
    P3["Task #103"]
  end
  subgraph CodeReviewCol ["3. Review / QA (WIP Limit: 2)"]
    R1["PR #88"]
    R2["PR #89"]
  end
  subgraph DoneCol ["4. Done (Deployed)"]
    D1["Shipped Features"]
  end
  BacklogCol --> InProgressCol --> CodeReviewCol --> DoneCol
  style BacklogCol fill:#0f172a,stroke:#3b82f6
  style InProgressCol fill:#1e1b4b,stroke:#6366f1
  style CodeReviewCol fill:#3f1a1a,stroke:#ef4444
  style DoneCol fill:#064e3b,stroke:#10b981"""
                },
                {
                    "type": "code_lab",
                    "title": "Kanban WIP & Cycle Time Engine",
                    "instructions": "Implement `calculate_kanban_metrics(wip_count, throughput_per_day)` to model Little's Law and calculate the impact of adjusting WIP limits.",
                    "starter_code": """def calculate_kanban_metrics(wip_items: int, throughput_items_per_day: float) -> dict:
    \"\"\"
    Apply Little's Law to calculate average Cycle Time.
    Cycle Time = WIP / Throughput
    
    Returns dict:
      - 'cycle_time_days': float (rounded to 2 decimals)
      - 'annual_capacity': float (projected throughput over 250 working days)
      - 'bottleneck_warning': bool (True if cycle_time_days > 14.0 days)
    \"\"\"
    # TODO: Implement Little's Law calculation
    pass
""",
                    "solution_code": """def calculate_kanban_metrics(wip_items: int, throughput_items_per_day: float) -> dict:
    if throughput_items_per_day <= 0:
        return {'cycle_time_days': 0.0, 'annual_capacity': 0.0, 'bottleneck_warning': True}
        
    cycle_time = round(wip_items / throughput_items_per_day, 2)
    annual_capacity = round(throughput_items_per_day * 250.0, 2)
    warning = cycle_time > 14.0
    
    return {
        'cycle_time_days': cycle_time,
        'annual_capacity': annual_capacity,
        'bottleneck_warning': warning
    }
""",
                    "test_code": """res = calculate_kanban_metrics(12, 1.5)
assert res['cycle_time_days'] == 8.0
assert res['annual_capacity'] == 375.0
assert res['bottleneck_warning'] is False

res2 = calculate_kanban_metrics(30, 1.0)
assert res2['cycle_time_days'] == 30.0
assert res2['bottleneck_warning'] is True
print("Kanban metrics tests passed successfully!")
""",
                    "why_works": "**Why This Solution Works:**\nLittle's Law mathematically proves that reducing Work-in-Progress from 30 items to 12 items slashes cycle time from 30 days to 8 days, enabling features to reach real customers nearly 4 times faster.",
                    "alternatives": "**Alternative Approaches & Trade-offs:**\n- **Cumulative Flow Diagram (CFD):** Visualizes the quantity of work in each state over time, showing widening bands where bottlenecks develop.\n- **Monte Carlo Forecasting:** Uses historical throughput distribution to compute confidence intervals (e.g., '85% probability of completing 15 stories within 2 weeks').",
                    "edge_cases": "**Edge Cases & Failure Modes:**\n- `throughput <= 0`: Handled gracefully to prevent ZeroDivisionError.\n- Very large WIP: Correctly triggers the `bottleneck_warning` flag."
                }
            ]
        },
        {
            "title": "Module 4: Scrum vs. Kanban: The Scrumban Synthesis",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Modern high-performing engineering teams frequently blend Scrum and Kanban into **Scrumban**, preserving sprint planning and retrospectives while using Kanban WIP limits to manage day-to-day workflow."
                },
                {
                    "type": "concept",
                    "title": "Comparative Framework Matrix",
                    "content": "| Dimension | Scrum | Kanban | Scrumban |\n|---|---|---|---|\n| **Cadence** | Regular fixed timeboxes (1-4 wk) | Continuous flow | Sprints for planning; continuous execution |\n| **Work Release** | At end of sprint (or continuous) | Continuous as items complete | Continuous release |\n| **Roles** | Strict: PO, SM, Devs | None prescribed | Flexible PO and Facilitator |\n| **Metrics** | Velocity (Story Points) | Cycle Time & Lead Time | Lead Time & Velocity |\n| **Change Policy** | No changes mid-sprint | Changes anytime at column top | Pull next priority from queue |"
                },
                {
                    "type": "interactive",
                    "title": "Incident Support Framework Selection Challenge",
                    "question": "A team handles unpredictable emergency production bug fixes, server outages, and regulatory patches alongside regular work. Why is pure Scrum's fixed sprint commitment ill-suited for this team?",
                    "options": [
                        "Scrum requires all code to be written by senior architects.",
                        "Frequent unpredictable emergencies continuously blow up the committed sprint scope, making 2-week timebox planning useless; Kanban's continuous pull flow fits incident response far better.",
                        "Scrum only works for mobile applications.",
                        "Kanban forbids teams from fixing security bugs."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nScrum assumes a relatively stable sprint commitment. When a team operates under unpredictable interrupts (DevOps, SRE, IT support), fixed sprint backlogs break immediately. Kanban allows incoming high-priority emergency tickets to be pulled directly into the WIP limit without disrupting an arbitrary sprint cadence."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "WIP Acronym Challenge",
                    "question": "In Kanban, the fundamental rule that restricts the number of active tasks permitted in any workflow column is known as the _____ Limit.\n\nAnswer: _____",
                    "answer": "WIP",
                    "alternatives": ["WIP", "wip", "Work in Progress", "work in progress"],
                    "explanation": "**Why WIP is Correct:**\n**Work-in-Progress (WIP) Limits** prevent multitasking, expose bottlenecks immediately, and enforce a 'stop starting, start finishing' engineering culture."
                }
            ]
        }
    ]
}

print(f"Loaded {len(PART1_CASES)} cases for Part 1 (Cases 00-04).")

with open('/Users/aadarshamahato/Downloads/LEARNING_PLATFORM/se_story_lab/cases_part1.json', 'w', encoding='utf-8') as f:
    json.dump(PART1_CASES, f, indent=4)
