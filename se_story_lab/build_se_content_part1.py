import json

CASES_PART1 = {}

# CASE 00: The Software Crisis
CASES_PART1["0"] = {
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
                },
                {
                    "type": "code_lab",
                    "title": "Technical Debt Compounding Simulator",
                    "instructions": "In software engineering, skipping design discipline creates 'Technical Debt' which compounds over time. Implement `simulate_debt(initial_cost, interest_rate, sprints)` that calculates total engineering effort after `sprints` iterations using compound growth: $Total = C_0 \\times (1 + r)^n$. Return the value rounded to 2 decimal places.",
                    "starter_code": "def simulate_debt(initial_cost: float, interest_rate: float, sprints: int) -> float:\n    # Return compounded maintenance cost\n    pass\n\n# --- Execution Check ---\nprint(simulate_debt(100.0, 0.10, 5))\n",
                    "solution_code": "def simulate_debt(initial_cost: float, interest_rate: float, sprints: int) -> float:\n    return round(initial_cost * ((1 + interest_rate) ** sprints), 2)\n",
                    "test_cases": [
                        {"input": "", "expected": "161.05"}
                    ],
                    "why_it_works": "**Technical Debt Compound Mechanics:**\nJust like financial debt, architectural shortcuts accrue interest. Every subsequent feature requires navigating around brittle workarounds, causing maintenance effort to grow exponentially rather than linearly.",
                    "complexity": "Time Complexity: O(1) closed-form calculation • Space Complexity: O(1)"
                }
            ]
        },
        {
            "title": "Module 2: Software vs Hardware: The Nature of the Artifact",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Why can't we build software the exact same way civil engineers build bridges or aerospace engineers build airplanes? Because software is **logical**, not physical. It does not wear out from friction, but it constantly deteriorates due to change."
                },
                {
                    "type": "concept",
                    "title": "The Bathtub Curve vs Software Failure Curves",
                    "content": "Physical hardware exhibits the classic **Bathtub Curve**: high infant mortality due to manufacturing defects, a long plateau of low failure rates, and wear-out due to physical erosion. Software, however, has **no physical wear-out**! Instead, software experiences spikes in failure rates whenever maintenance changes or new features introduce unintended side effects."
                },
                {
                    "type": "visual",
                    "title": "Hardware Wear-Out vs Software Deterioration",
                    "code": """graph LR
  subgraph Hardware ["Hardware Lifecycle: The Bathtub Curve"]
    H1["Infant Mortality (Manufacturing Defects)"]
    H2["Stable Operational Plateau (Low Failures)"]
    H3["Physical Wear-Out (Thermal / Fatigue Damage)"]
    H1 --> H2 --> H3
  end
  subgraph Software ["Software Lifecycle: The Change-Induced Curve"]
    S1["Initial Deployment (Bug Discovery)"]
    S2["Stable Baseline"]
    S3["Feature Change Spike (Side-Effect Defects)"]
    S4["Architectural Erosion & Decay"]
    S1 --> S2 --> S3 --> S4
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
                    "alternatives": ["Malleability", "Plasticity", "Flexibility", "Changeability"],
                    "explanation": "**Why Malleability is Correct:**\n**Malleability** is software's blessing and curse: unlike concrete or steel, code can be changed with keystrokes, which tempts engineers to make hasty modifications that compromise system integrity."
                }
            ]
        },
        {
            "title": "Module 3: The Dual Nature: Product & Medium",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Software plays a dual role in modern engineering: it is both a **Product** (an application that transforms data and delivers value to users) and a **Vehicle / Medium** (the operating systems, compilers, IDEs, and CI/CD pipelines through which other software is built)."
                },
                {
                    "type": "concept",
                    "title": "Software Engineering Definition (IEEE 610.12)",
                    "content": "The IEEE formally defines Software Engineering as:\n> *(1) The application of a systematic, disciplined, quantifiable approach to the development, operation, and maintenance of software; that is, the application of engineering to software.*\n> *(2) The study of approaches as in (1).*"
                },
                {
                    "type": "visual",
                    "title": "The Engineering Feedback Loop",
                    "code": """graph TD
  subgraph CustomerDomain ["Customer & Problem Domain"]
    REQ["Real-World Business Need & Constraints"]
    FEEDBACK["Operational Telemetry & User Feedback"]
  end
  subgraph EngineeringEngine ["Software Engineering Transformation"]
    SPEC["Formal Specification & Architecture"]
    IMPL["Disciplined Implementation & Unit Testing"]
    QA["Continuous Integration & Verification"]
    REQ --> SPEC --> IMPL --> QA
  end
  subgraph ProductionDelivery ["Delivered Product"]
    PROD["Reliable Production Release"]
    QA --> PROD --> FEEDBACK --> REQ
  end
  style CustomerDomain fill:#0f172a,stroke:#3b82f6
  style EngineeringEngine fill:#1e1b4b,stroke:#6366f1
  style ProductionDelivery fill:#064e3b,stroke:#10b981"""
                },
                {
                    "type": "interactive",
                    "title": "IEEE Engineering Standard Challenge",
                    "question": "Which three core attributes define the IEEE standard approach to software engineering?",
                    "options": [
                        "Ad-hoc, fast, and unconstrained",
                        "Systematic, disciplined, and quantifiable",
                        "Theoretical, non-reproducible, and informal",
                        "Hardware-dependent, manual, and unversioned"
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nIEEE standard 610.12 mandates that engineering requires a **systematic** process, **disciplined** execution, and **quantifiable** metrics."
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
                    "alternatives": ["Therac-25", "Therac 25", "therac-25"],
                    "explanation": "**Why Therac-25 is Correct:**\nThe **Therac-25** disaster is the classic case study in software engineering failures: software race conditions delivered lethal radiation doses to patients because hardware safety interlocks were removed in favor of unverified software controls."
                }
            ]
        }
    ]
}

print("Built Case 00 successfully!")

# Save to temporary intermediate file
with open('/Users/aadarshamahato/Downloads/LEARNING_PLATFORM/se_story_lab/cases_part1.json', 'w', encoding='utf-8') as f:
    json.dump(CASES_PART1, f, indent=4)
