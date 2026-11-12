import json
import os

SYLLABUS_PART1 = {}

# CASE 00: Software Engineering Foundations & Evolution
SYLLABUS_PART1["0"] = {
    "title": "Case 00: Software Engineering Foundations & Evolution",
    "episodes": [
        {
            "title": "Module 1: The 1968 NATO Conference & The Dual Role of Software",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "In October 1968 in Garmisch, Germany, computer scientists convened under the NATO Science Committee to address astronomical budget overruns, delayed deliveries, and disastrous software crashes. The term **Software Engineering** was formally established to transform software development from an uncoordinated craft into a disciplined engineering science."
                },
                {
                    "type": "objective",
                    "title": "Module Objective",
                    "content": "Understand the historical origins of Software Engineering, the IEEE definition of software engineering, and software's dual nature as both a product and a vehicle for delivering value."
                },
                {
                    "type": "concept",
                    "title": "IEEE Definition of Software Engineering (IEEE 610.12)",
                    "content": "> *(1) The application of a systematic, disciplined, quantifiable approach to the development, operation, and maintenance of software; that is, the application of engineering to software.*\n> *(2) The study of approaches as in (1).*\n\n### The Dual Nature:\n- **As a Product:** Software delivers computing potential: operating systems, banking ledgers, flight control, and web portals.\n- **As a Medium / Vehicle:** Software acts as the infrastructure through which other software is built: compilers, operating systems, CASE tools, CI/CD pipelines, and version control repositories."
                },
                {
                    "type": "visual",
                    "title": "The Engineering Transformation Pipeline",
                    "code": """graph LR
  subgraph Inputs ["Problem Domain"]
    REQ["User Needs & Real-World Constraints"]
  end
  subgraph EngineeringDiscipline ["Software Engineering Discipline"]
    SYS["Systematic Process Models (SDLC)"]
    DISC["Disciplined Architectural Design"]
    QUANT["Quantifiable Verification Metrics"]
    SYS --> DISC --> QUANT
  end
  subgraph Outputs ["Solution Domain"]
    PROD["Reliable, Maintainable Software Product"]
  end
  REQ --> SYS
  QUANT --> PROD
  style Inputs fill:#0f172a,stroke:#3b82f6
  style EngineeringDiscipline fill:#1e1b4b,stroke:#6366f1
  style Outputs fill:#064e3b,stroke:#10b981"""
                },
                {
                    "type": "interactive",
                    "title": "Foundational Definition Challenge",
                    "question": "According to IEEE Standard 610.12, which triad of attributes distinguishes software engineering from solitary programming?",
                    "options": [
                        "Theoretical, unconstrained, and fast",
                        "Systematic, disciplined, and quantifiable",
                        "Informal, speculative, and subjective",
                        "Hardware-dependent, manual, and unversioned"
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nIEEE Standard 610.12 mandates that engineering requires a **systematic** approach (following established processes), **disciplined** execution (adhering to architecture and standards), and **quantifiable** metrics (measuring defect density, complexity, and performance)."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Historical Genesis Challenge",
                    "question": "The historic 1968 conference that officially declared the Software Crisis and birthed Software Engineering was sponsored by the _____ Science Committee.\n\nAnswer: _____",
                    "answer": "NATO",
                    "alternatives": ["NATO", "nato", "N.A.T.O."],
                    "explanation": "**Why NATO is Correct:**\nThe **NATO Science Committee** organized the landmark 1968 conference in Garmisch, Germany, bringing together world leaders in computing."
                }
            ]
        },
        {
            "title": "Module 2: Software Characteristics & The Wear Curve",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Why can't civil or mechanical engineering techniques be copy-pasted into software? Software is constructed of pure thought-stuff; it is intangible, invisible, and does not wear out in the physical sense."
                },
                {
                    "type": "concept",
                    "title": "Fundamental Software Characteristics",
                    "content": "1. **Software is engineered or developed, not manufactured:** Unlike physical cars or microchips on an assembly line, the dominant cost of software is in intellectual design, not physical reproduction.\n2. **Software does NOT wear out:** Physical hardware exhibits a classic **Bathtub Curve** (infant mortality flaws, constant low failure burn-in, then physical wear-out from friction, heat, and oxidation). Software exhibits a **Deterioration Curve**: defects decline as initial bugs are patched, but rise over time because repeated scope changes and hurried patches erode its conceptual integrity.\n3. **High Malleability:** Software can be altered with simple keystrokes, which creates the dangerous illusion that changing complex systems is trivial.\n4. **Invisibility & Complexity:** Software cannot be laid out in physical 3D space; no geometric diagram can depict all possible state transitions."
                },
                {
                    "type": "visual",
                    "title": "Hardware Bathtub Curve vs. Software Deterioration Curve",
                    "code": """graph TD
  subgraph Hardware ["Hardware Failure Rate (Bathtub Curve)"]
    H1["Infant Mortality (Manufacturing Defects)"] --> H2["Low Constant Operating Failure Rate"]
    H2 --> H3["Physical Wear-Out (Thermal Fatigue & Friction)"]
  end
  subgraph Software ["Software Failure Rate (Deterioration Curve)"]
    S1["Initial Discovery & Patching"] --> S2["Lowest Stable Baseline"]
    S2 -->|"Scope Creep & Hurried Patches"| S3["Side-Effect Defects Introduced"]
    S3 --> S4["Architectural Erosion & Decay ⚠️"]
  end
  style Hardware fill:#0f172a,stroke:#3b82f6
  style Software fill:#1e1b4b,stroke:#6366f1"""
                },
                {
                    "type": "interactive",
                    "title": "Wear Mechanism Challenge",
                    "question": "What is the primary reason software failure rates increase over time if software does not suffer from physical friction or mechanical fatigue?",
                    "options": [
                        "The computer monitor burns out.",
                        "Successive maintenance modifications and urgent patches introduce side-effects that degrade architectural integrity.",
                        "The bits stored on magnetic hard drives physically oxidize.",
                        "Compilers degrade after 5 years."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nSoftware does not wear out physically. It degrades because customer requirements evolve, and engineers make quick patches that violate original architectural assumptions, causing **architectural erosion** and unexpected regression defects."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Failure Curve Terminology Challenge",
                    "question": "Physical hardware reliability follows the well-known _____ curve, featuring infant mortality and wear-out phases.\n\nAnswer: _____",
                    "answer": "Bathtub",
                    "alternatives": ["Bathtub", "bathtub", "Bathtub Curve"],
                    "explanation": "**Why Bathtub is Correct:**\nThe **Bathtub Curve** graphically resembles a bathtub: high failure at the beginning (infant mortality), a long flat bottom of low failures, and a sharp upward slope at the end due to physical fatigue."
                }
            ]
        },
        {
            "title": "Module 3: Lehman's Laws of Software Evolution",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Between 1974 and 1996, Meir M. Lehman formulated eight empirical laws governing **E-type systems** (software that models real-world business activities). Lehman demonstrated that software must either evolve continuously or die."
                },
                {
                    "type": "concept",
                    "title": "The Core Lehman Laws",
                    "content": "- **Law 1: Continuing Change:** An E-type system must continually adapt to its operational environment, or it becomes progressively less satisfactory.\n- **Law 2: Increasing Complexity:** As an evolving program is continuously modified, its internal complexity increases unless explicit work (refactoring) is done to reduce it.\n- **Law 4: Conservation of Organizational Stability:** Over a system's lifetime, the average effective work rate of an organization is invariant regardless of resource allocation.\n- **Law 6: Continuing Growth:** The functional content of systems must continually increase to maintain user satisfaction over time.\n- **Law 7: Declining Quality:** An E-type system will appear to decline in quality unless rigorously maintained and adapted to changing operational environments."
                },
                {
                    "type": "visual",
                    "title": "Lehman's Law of Increasing Complexity & The Refactoring Interrupter",
                    "code": """graph TD
  subgraph EntropyLoop ["Natural Entropy Trajectory"]
    V1["Baseline System Release"] --> FEAT["Add New Features Rapidly"]
    FEAT --> COMP["Internal Complexity Multiplies"]
    COMP --> FRAG["High Regression Defect Rate"]
    FRAG --> FEAT
  end
  subgraph ActiveCountermeasure ["Engineering Countermeasure"]
    REFACTOR["Explicit Refactoring Investment (Reducing Complexity)"]
  end
  COMP -.->|"Requires Intervention"| REFACTOR
  REFACTOR -.->|"Restores Modularity"| V1
  style EntropyLoop fill:#3f1a1a,stroke:#ef4444
  style ActiveCountermeasure fill:#064e3b,stroke:#10b981"""
                },
                {
                    "type": "interactive",
                    "title": "Lehman Law Interpretation Challenge",
                    "question": "A hospital management software hasn't been modified in 4 years. The hardware and hospital regulations changed, and doctors report the software is now full of issues. Which Lehman Law explains this?",
                    "options": [
                        "Law of Conservation of Familiarity.",
                        "Law of Continuing Change (a system must adapt or become progressively less satisfactory in real-world usage).",
                        "Law of Self Regulation.",
                        "Moore's Law."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\n**Lehman's First Law (Continuing Change)** states that real-world software must continually adapt to environmental changes. Even if the code didn't change, the hospital's operational environment changed, causing the unchanged software to become obsolete and unsatisfactory."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Evolution Researcher Challenge",
                    "question": "The computer scientist who formulated the 8 Laws of Software Evolution is Meir _____.\n\nAnswer: _____",
                    "answer": "Lehman",
                    "alternatives": ["Lehman", "lehman", "Meir Lehman"],
                    "explanation": "**Why Lehman is Correct:**\n**Meir M. Lehman** established the empirical laws governing long-term software evolution, maintenance, and entropy."
                }
            ]
        },
        {
            "title": "Module 4: Engineering Dilemma: Refactoring vs. The Second-System Rewrite",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Every senior software engineer eventually faces an existential decision: should an aging, complex codebase be continuously refactored, or thrown away and completely rewritten from scratch?"
                },
                {
                    "type": "concept",
                    "title": "The Second-System Effect (Fred Brooks)",
                    "content": "In *The Mythical Man-Month*, Fred Brooks warned of the **Second-System Effect**: when architects design their second system, they try to include all the ideas and features that were cautiously left out of the first system. As a result, the rewrite becomes hopelessly bloated, delayed, and frequently fails before completion."
                },
                {
                    "type": "scenario_decision",
                    "title": "Architectural Crossroads Dilemma",
                    "scenario": "You are the Principal Architect at a logistics company. The core routing system is a 12-year-old monolith with high technical debt. It generates $80M annual revenue. The business wants to launch real-time drone delivery in 6 months. Two camps emerge: the VP of Product demands a complete 'greenfield rewrite from scratch in Rust and microservices', while the Lead SRE argues for 'incremental strangler refactoring'.",
                    "question": "Which strategic path should you choose to ensure business continuity and minimize project risk?",
                    "options": [
                        "Approve the complete rewrite from scratch: freeze all legacy updates and promise delivery in 6 months.",
                        "Apply the Strangler Fig Pattern: incrementally extract drone routing capabilities into clean modular microservices while maintaining the proven monolith.",
                        "Do nothing: forbid any new features and tell the business that the system cannot support drones.",
                        "Rewrite only the database queries in assembly language."
                    ],
                    "answer": 1,
                    "rationale": "**Why the Strangler Fig Pattern is Optimal:**\nMartin Fowler's **Strangler Fig Pattern** incrementally replaces legacy components one by one behind an API gateway. The business continues generating $80M revenue, new drone features ship within the 6-month window, and the company avoids the catastrophic risk of a multi-year frozen 'second-system' rewrite that fails to ship."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Refactoring Pattern Challenge",
                    "question": "The incremental migration design pattern named after an Australian vine that gradually surrounds and replaces a host tree is the _____ Fig pattern.\n\nAnswer: _____",
                    "answer": "Strangler",
                    "alternatives": ["Strangler", "strangler", "Strangler Fig"],
                    "explanation": "**Why Strangler is Correct:**\nThe **Strangler Fig Pattern** (or Strangler Pattern) safely modernizes monolithic systems by intercepting calls and gradually migrating functionality without big-bang rewrites."
                }
            ]
        }
    ]
}

# CASE 01: Process Lifecycles: Linear to Evolutionary
SYLLABUS_PART1["1"] = {
    "title": "Case 01: Process Lifecycles: Linear to Evolutionary",
    "episodes": [
        {
            "title": "Module 1: The Classic Waterfall Lifecycle",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "In 1970, Dr. Winston W. Royce presented the sequential lifecycle model. Ironically, Royce presented the strict linear sequence as risky, but the aerospace and defense industries adopted it as standard (DoD-STD-2167A)."
                },
                {
                    "type": "objective",
                    "title": "Module Objective",
                    "content": "Analyze the phases, phase-gate mechanics, advantages, and catastrophic failure modes of the classic Waterfall model."
                },
                {
                    "type": "concept",
                    "title": "Waterfall Phases & Phase-Gate Enforcement",
                    "content": "1. **Requirements Analysis:** Gather and document complete system capabilities into an SRS document.\n2. **System Design:** Architectural blueprints, database schemas, and interface contracts are frozen.\n3. **Implementation (Coding):** Developers construct code to match design specifications.\n4. **Integration & System Testing:** Disparate modules are assembled and verified as a whole.\n5. **Deployment & Operations:** Handover to production operations and long-term maintenance.\n\n**The Phase Gate:** Work cannot flow past a gate until the preceding phase's documentation is 100% complete and approved by stakeholder signatures."
                },
                {
                    "type": "visual",
                    "title": "Waterfall Phase Gates & Defect Feedback Delay",
                    "code": """graph TD
  subgraph Upstream ["Upstream Phases"]
    R["1. Requirements Gathering (SRS)"] -->|"Gate 1: Approved SRS"| D["2. System Architectural Design"]
  end
  subgraph Construction ["Construction Phase"]
    D -->|"Gate 2: Approved Design"| C["3. Implementation / Coding"]
  end
  subgraph Downstream ["Downstream Verification (Late Feedback!)"]
    C -->|"Gate 3: Code Complete"| T["4. System Integration & Testing"]
    T -->|"Gate 4: UAT Signoff"| M["5. Deployment & Maintenance"]
    T -.->|"Fundamental Requirements Flaw Caught Here (100x Cost!)"| R
  end
  style Upstream fill:#064e3b,stroke:#10b981
  style Construction fill:#1e1b4b,stroke:#6366f1
  style Downstream fill:#3f1a1a,stroke:#ef4444"""
                },
                {
                    "type": "interactive",
                    "title": "Waterfall Risk Challenge",
                    "question": "What is the primary systemic flaw of a rigid Waterfall lifecycle on unprecedented software projects?",
                    "options": [
                        "It uses too few documents.",
                        "Working software is only integrated at the very end, deferring discovery of critical architectural and requirement defects until budgets are exhausted.",
                        "It forces developers to pair program every day.",
                        "It allows requirements to change continuously mid-project."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nIn Waterfall, working software is not integrated until the testing phase. If assumptions made during requirements analysis 18 months earlier were flawed, the error is discovered after 90% of the project budget has been spent, making remediation catastrophic."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Author Identification Challenge",
                    "question": "The computer scientist who originally illustrated the linear software development pipeline in 1970 was Winston _____.\n\nAnswer: _____",
                    "answer": "Royce",
                    "alternatives": ["Royce", "royce", "Winston Royce"],
                    "explanation": "**Why Royce is Correct:**\n**Dr. Winston W. Royce** published *Managing the Development of Large Software Systems* in 1970, illustrating the classic sequential stages."
                }
            ]
        },
        {
            "title": "Module 2: The Dual V-Model: Verification & Validation",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "To solve Waterfall's delayed testing problem, the German defense administration and avionics standards developed the **V-Model**. It establishes direct bidirectional links between each specification phase on the left descent and a corresponding testing phase on the right ascent."
                },
                {
                    "type": "concept",
                    "title": "Boehm's Verification vs. Validation Distinction",
                    "content": "- **Verification:** *'Are we building the product right?'*\n  - Confirms that each phase's output satisfies the specifications established at the start of that phase (e.g. Unit testing verifies Module Design; Integration testing verifies Architectural Design).\n- **Validation:** *'Are we building the right product?'*\n  - Confirms that the delivered system fulfills its intended real-world operational user needs (Acceptance Testing validates against User Requirements)."
                },
                {
                    "type": "visual",
                    "title": "The Dual V-Model Mapping",
                    "code": """graph LR
  subgraph LeftWing ["Decomposition Wing (Specification)"]
    UR["User Requirements"] --> SR["System Specifications"]
    SR --> AD["Architectural Design"]
    AD --> MD["Module Detailed Design"]
    MD --> CODE["Coding / Implementation"]
  end
  subgraph RightWing ["Integration Wing (Testing)"]
    CODE --> UT["Unit Testing"]
    UT --> IT["Integration Testing"]
    IT --> ST["System Testing"]
    ST --> UAT["User Acceptance Testing (UAT)"]
  end
  MD -.-|"Verifies"| UT
  AD -.-|"Verifies"| IT
  SR -.-|"Verifies"| ST
  UR -.-|"Validates"| UAT
  style LeftWing fill:#0f172a,stroke:#3b82f6
  style RightWing fill:#1e1b4b,stroke:#6366f1"""
                },
                {
                    "type": "interactive",
                    "title": "V&V Distinction Challenge",
                    "question": "A banking team proves that the interest calculation function satisfies its math specification with 100% precision. However, bank auditors reject the software because federal tax withholding rules were omitted. How is this classified?",
                    "options": [
                        "Verification failed, but Validation passed.",
                        "Verification passed (built the product right according to specification), but Validation failed (built the wrong product).",
                        "Both Verification and Validation passed.",
                        "Neither applies to financial software."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nVerification confirmed that the code executed the written math formula accurately. However, Validation failed because the resulting system did not meet the regulatory legal reality of the financial business."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "V-Model Alignment Challenge",
                    "question": "In the standard V-Model, Integration Testing directly verifies against the _____ Design specification.\n\nAnswer: _____",
                    "answer": "Architectural",
                    "alternatives": ["Architectural", "architectural", "System Design", "Architecture"],
                    "explanation": "**Why Architectural Design is Correct:**\n**Architectural Design** defines the interfaces and component interactions, which are verified during Integration Testing."
                }
            ]
        },
        {
            "title": "Module 3: Iterative, Incremental & Evolutionary Models",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Rather than building the entire system in one monolithic sequential push, modern engineering uses **Iterative**, **Incremental**, and **Evolutionary** lifecycles."
                },
                {
                    "type": "concept",
                    "title": "Iterative vs. Incremental vs. Evolutionary Models",
                    "content": "### 1. Incremental Model\n- Delivers software in pieces: Release 1 contains Core Features; Release 2 adds Reporting; Release 3 adds Analytics.\n- Each increment delivers a fully functional, usable subset of the overall product.\n\n### 2. Iterative Model\n- Refines the entire system across successive passes: Pass 1 is a sketch/rough framework; Pass 2 refines the logic; Pass 3 optimizes and hardens performance.\n\n### 3. Evolutionary Models (Boehm's Spiral & Prototyping)\n- Acknowledges that requirements cannot be fully known upfront. The system evolves through outward cycles driven by **Risk Analysis** and user feedback."
                },
                {
                    "type": "visual",
                    "title": "Incremental vs. Iterative Delivery Comparison",
                    "code": """graph TD
  subgraph Incremental ["Incremental: Building Piece-by-Piece (Slice of Cake)"]
    INC1["Increment 1: Working Auth & Core Account"] --> INC2["Increment 2: Add Fund Transfer Engine"]
    INC2 --> INC3["Increment 3: Add International Wire Transfers"]
  end
  subgraph Iterative ["Iterative: Refining the Entire Canvas Across Passes"]
    IT1["Pass 1: Low-Fidelity Prototype (Skeleton System)"] --> IT2["Pass 2: Functional Core Logic Added"]
    IT2 --> IT3["Pass 3: Production-Hardened Performance & Security"]
  end
  style Incremental fill:#064e3b,stroke:#10b981
  style Iterative fill:#1e1b4b,stroke:#6366f1"""
                },
                {
                    "type": "interactive",
                    "title": "Process Classification Challenge",
                    "question": "A team delivers a functional banking app with only checking account balance checks in Month 1. In Month 2, they release bill-pay features. In Month 3, they add stock trading. What process model is this?",
                    "options": [
                        "Pure Sequential Waterfall.",
                        "Incremental Model (delivering usable functional software slices in successive releases).",
                        "Throwaway Prototyping.",
                        "Big-Bang Delivery."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nIn an **Incremental Model**, the product is divided into functional subsystems. Each release adds new working capabilities to the existing operational product."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Risk-Driven Model Challenge",
                    "question": "The famous evolutionary software process model that cycles through four quadrants driven explicitly by Risk Analysis is Barry Boehm's _____ Model.\n\nAnswer: _____",
                    "answer": "Spiral",
                    "alternatives": ["Spiral", "spiral", "Spiral Model"],
                    "explanation": "**Why Spiral is Correct:**\n**Barry Boehm's Spiral Model** is risk-driven: every revolution around the 4 quadrants assesses risks before proceeding to detailed construction."
                }
            ]
        },
        {
            "title": "Module 4: Process Model Selection Strategy",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Professional software engineers do not dogmatically favor one process model. They select the lifecycle that matches project risk, regulatory constraints, and requirement volatility."
                },
                {
                    "type": "concept",
                    "title": "Process Selection Decision Matrix",
                    "content": "| Characteristic | Waterfall / V-Model | Evolutionary Spiral | Agile / Scrum |\n|---|---|---|---|\n| **Requirement Clarity** | Well understood, stable, locked | Highly uncertain, exploratory | Evolving, discovered through usage |\n| **Cost of Defect** | Catastrophic (Avionics, Medical) | High financial or mission risk | Low to moderate (Web / Mobile) |\n| **Customer Availability** | At start (SRS) and end (Acceptance) | At end of each spiral cycle | Continuously every 1-2 weeks |\n| **Technology Stack** | Mature, proven, well-understood | Unprecedented, novel tech | Rapidly evolving frameworks |\n| **Release Cadence** | Single delivery at project end | Incremental prototypes | Working software every sprint |"
                },
                {
                    "type": "scenario_decision",
                    "title": "Methodology Selection Dilemma",
                    "scenario": "You are hired as Director of Engineering for a medical device company building software for an automated insulin pump that will be surgically implanted in patients. The firmware must undergo strict FDA Class III medical device regulatory approval with complete mathematical verification proofs. The product owner suggests: 'Let's use 1-week Agile sprints with no formal documentation and push updates over Bluetooth daily.'",
                    "question": "How should you evaluate this methodology proposal?",
                    "options": [
                        "Agree immediately: Agile is always the most modern and fastest approach.",
                        "Reject the proposal: Life-critical Class III medical devices mandate rigorous V-Model verification, formal traceability, and locked specifications under IEC 62304 standards.",
                        "Use Waterfall, but skip the testing phase to save time.",
                        "Switch to pure cowboy coding without version control."
                    ],
                    "answer": 1,
                    "rationale": "**Why the V-Model is Mandatory:**\nMedical devices with lethal failure potential (FDA Class III, IEC 62304) legally require documented bidirectional traceability from requirements to verified unit tests. 'Move fast and break things' can kill patients. The **V-Model** ensures formal verification gates at every level of abstraction."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Medical Standard Challenge",
                    "question": "The international benchmark standard governing medical device software lifecycles is IEC _____.\n\nAnswer: _____",
                    "answer": "62304",
                    "alternatives": ["62304", "IEC 62304", "IEC-62304"],
                    "explanation": "**Why IEC 62304 is Correct:**\n**IEC 62304** defines the lifecycle requirements for medical device software, establishing mandatory verification and safety classifications."
                }
            ]
        }
    ]
}

# CASE 02: Investigation: The Agile Transformation Breakdown
SYLLABUS_PART1["2"] = {
    "title": "Case 02: Investigation: The Agile Transformation Breakdown",
    "episodes": [
        {
            "title": "Module 1: The Agile Manifesto & Core Philosophy",
            "blocks": [
                {
                    "type": "problem",
                    "content": "A high-profile retail bank spent $14M hiring consultants to 'become Agile'. Nine months later, releases are stalled, developers are burned out from endless meetings, and the CTO calls an emergency audit: 'We have Daily Standups and Jira, so why is velocity zero?'"
                },
                {
                    "type": "objective",
                    "title": "Module Objective",
                    "content": "Audit the 4 core values and 12 principles of the Agile Manifesto, identify cargo-cult Agile antipatterns, and restore genuine agility."
                },
                {
                    "type": "concept",
                    "title": "The 4 Core Values (Snowbird, 2001)",
                    "content": "1. **Individuals and interactions** over processes and tools\n2. **Working software** over comprehensive documentation\n3. **Customer collaboration** over contract negotiation\n4. **Responding to change** over following a plan\n\n> *'While there is value in the items on the right, we value the items on the left more.'*\n\n**The Cargo Cult Antipattern:** Adopting rituals (Jira tickets, 15-minute standing meetings, post-it notes) without embracing technical discipline (automated tests, customer collaboration, continuous refactoring)."
                },
                {
                    "type": "interactive",
                    "title": "Agile Value Misconception Challenge",
                    "question": "During the audit, you discover developers have stopped writing architecture documentation or API contracts, claiming: 'The Agile Manifesto says working software over documentation, so documentation is banned!' How do you correct them?",
                    "options": [
                        "Fire the developers and return to Waterfall.",
                        "Clarify that the manifesto explicitly states there is value in documentation, but documentation is valuable only when it directly supports delivering working software rather than serving as bureaucratic waste.",
                        "Require 500 pages of UML diagrams before any line of code is written.",
                        "Documentation is indeed banned under pure Agile."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nThe Agile Manifesto never said 'never document'. It specifically clarified: *'while there is value in the items on the right, we value the items on the left more'*. Clean API contracts and concise architecture diagrams are critical assets that accelerate working software."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Manifesto Signatory Year Challenge",
                    "question": "The 17 software visionaries met at Snowbird, Utah to author the Agile Manifesto in the year _____.\n\nAnswer: _____",
                    "answer": "2001",
                    "alternatives": ["2001", "February 2001"],
                    "explanation": "**Why 2001 is Correct:**\nIn **February 2001**, signatories including Kent Beck, Martin Fowler, Ward Cunningham, and Ken Schwaber forged the manifesto."
                }
            ]
        },
        {
            "title": "Module 2: Extreme Programming (XP) Practices",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Formulated by Kent Beck on the Chrysler C3 payroll project, **Extreme Programming (XP)** is the most technically rigorous Agile methodology. If Scrum is the project management framework, XP is the engineering engine."
                },
                {
                    "type": "concept",
                    "title": "The Core Technical Practices of XP",
                    "content": "1. **Test-Driven Development (TDD):** Write failing automated unit tests before writing production code (Red-Green-Refactor).\n2. **Pair Programming:** Two developers at one workstation: the **Driver** writes tactical code, while the **Navigator** thinks strategically, reviewing syntax and anticipating edge cases.\n3. **Continuous Integration:** Merge code into the main branch multiple times a day; automated CI builds must always stay green.\n4. **Refactoring:** Continuously clean up and simplify design without altering observable behavior.\n5. **Collective Ownership:** Anyone on the team can improve any line of code anywhere in the system at any time.\n6. **Simple Design & YAGNI:** *'You Aren't Gonna Need It'* — implement only what is required for current stories, never speculative future architectures.\n7. **Sustainable Pace (40-Hour Week):** Overtime is forbidden two weeks in a row because exhausted engineers write defective code."
                },
                {
                    "type": "visual",
                    "title": "Pair Programming Cognitive Dynamic",
                    "code": """graph LR
  subgraph Workstation ["Shared Workstation"]
    DRIVER["Driver (Tactical Focus)"]
    NAV["Navigator (Strategic Focus)"]
    DRIVER <-->|"Continuous Real-Time Dialogue"| NAV
  end
  subgraph Roles ["Cognitive Responsibilities"]
    D_DUTY["Keyboard & Mouse: Clean Syntax, Method Names, Test Assertions"]
    N_DUTY["Review Architecture, Catch Off-by-One Bugs, Plan Edge Cases"]
  end
  DRIVER -.-> D_DUTY
  NAV -.-> N_DUTY
  style Workstation fill:#0f172a,stroke:#3b82f6
  style Roles fill:#1e1b4b,stroke:#6366f1"""
                },
                {
                    "type": "interactive",
                    "title": "XP Technical Practice Challenge",
                    "question": "Which XP practice directly eliminates the 'Truck Factor' (risk of a project stalling if a key developer departs)?",
                    "options": [
                        "Planning Poker.",
                        "Collective Code Ownership combined with Pair Programming.",
                        "Writing Gantt charts.",
                        "Working 60-hour weeks."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nWhen pairs rotate across the entire codebase and everyone has **Collective Ownership**, structural code knowledge is distributed across the entire team, preventing any single developer from becoming an irreplaceable silo."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "XP Principle Challenge",
                    "question": "The foundational Extreme Programming rule that forbids implementing speculative features before they are needed is known by the acronym _____.\n\nAnswer: _____",
                    "answer": "YAGNI",
                    "alternatives": ["YAGNI", "yagni", "You Aren't Gonna Need It"],
                    "explanation": "**Why YAGNI is Correct:**\n**YAGNI** (You Aren't Gonna Need It) prevents premature optimization and wasteful speculative coding."
                }
            ]
        },
        {
            "title": "Module 3: The Scrum Framework: Roles, Ceremonies, Artifacts",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Ken Schwaber and Jeff Sutherland created **Scrum** around empirical process control: transparency, inspection, and adaptation. It operates in strict timeboxed cycles called Sprints."
                },
                {
                    "type": "concept",
                    "title": "The Scrum 3-5-3 Triad",
                    "content": "### 3 Roles:\n- **Product Owner (PO):** Owns the Product Backlog, defines priorities, and maximizes business value.\n- **Scrum Master (SM):** Servant leader who coaches the team, removes blockers, and protects the team from external disruption.\n- **Developers:** Cross-functional professionals who build the shippable increment.\n\n### 5 Ceremonies:\n1. **Sprint Planning:** Commit to Sprint Goal and pull backlog items.\n2. **Daily Scrum:** 15-minute sync on yesterday's progress, today's focus, and blockers.\n3. **Sprint Review:** Demonstrate working software increment to stakeholders.\n4. **Sprint Retrospective:** Inspect team process and enact continuous improvements.\n5. **The Sprint Itself:** Fixed timebox (typically 2 weeks).\n\n### 3 Artifacts:\n- **Product Backlog** (Commitment: Product Goal)\n- **Sprint Backlog** (Commitment: Sprint Goal)\n- **Increment** (Commitment: Definition of Done - DoD)"
                },
                {
                    "type": "interactive",
                    "title": "Scrum Boundary Dispute Challenge",
                    "question": "During week 2 of a 2-week sprint, the VP of Sales walks up to a developer and orders them: 'Drop everything and build this custom report for my client immediately!' How must Scrum governance respond?",
                    "options": [
                        "The developer should work late at night to finish both tasks.",
                        "The Scrum Master must intervene to protect the sprint commitment, redirecting the VP of Sales to negotiate with the Product Owner for inclusion in future sprint planning.",
                        "The Scrum Master should cancel the sprint immediately.",
                        "The developer should immediately obey the VP."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nA core responsibility of the **Scrum Master** is shielding the development team from external disruptions. Only the **Product Owner** can alter backlog priorities, which must be planned for subsequent sprints to preserve the active Sprint Goal."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Quality Definition Challenge",
                    "question": "The formal shared checklist ensuring a backlog item meets all testing, coding, and deployment standards before being declared complete is the Definition of _____ (DoD).\n\nAnswer: _____",
                    "answer": "Done",
                    "alternatives": ["Done", "done", "DoD"],
                    "explanation": "**Why Done is Correct:**\nThe **Definition of Done (DoD)** prevents unfinished, unverified code from being passed off as completed work."
                }
            ]
        },
        {
            "title": "Module 4: User Stories, User Story Cards & The INVEST Criteria",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Requirements in Agile are not 200-page specifications; they are captured as **User Stories** written on physical or virtual cards, following Bill Wake's **INVEST** criteria."
                },
                {
                    "type": "concept",
                    "title": "User Story Cards & The 3 C's (Ron Jeffries)",
                    "content": "1. **Card:** The physical index card capturing the core intent: *'As a [role], I want [capability], so that [business benefit].'*\n2. **Conversation:** The verbal dialogue between developers and the Product Owner discussing nuances and edge cases.\n3. **Confirmation:** The acceptance tests written on the back of the card (e.g. Given/When/Then).\n\n### The INVEST Quality Filter:\n- **I — Independent:** Stories should be decoupled so they can be worked on in any order.\n- **N — Negotiable:** Details are open for trade-off discussions, not rigid contracts.\n- **V — Valuable:** Delivers observable outcome to real users (not internal tech chores).\n- **E — Estimable:** Team understands domain well enough to assign story points.\n- **S — Small:** Sized to comfortably finish within a single sprint (2-3 days).\n- **T — Testable:** Accompanied by clear, binary acceptance tests."
                },
                {
                    "type": "diagram_critique",
                    "title": "User Story Card Quality Audit",
                    "scenario": "A junior Product Owner presents this user story card for the upcoming sprint:",
                    "code": """graph TD
  subgraph StoryCard ["User Story Card: US-402"]
    ROLE["As a: System Developer"]
    WANT["I want: To rewrite entire backend into Rust & upgrade MySQL to Cassandra"]
    SO_THAT["So that: Our tech stack is more modern"]
    ROLE --> WANT --> SO_THAT
  end""",
                    "question": "Which critical INVEST principle is most severely violated by this story card?",
                    "options": [
                        "It violates the Negotiable principle.",
                        "It violates the Valuable principle: stories must express tangible value to an end-user or business stakeholder, not an internal technical chore written from the 'developer' persona.",
                        "It violates the Testable principle.",
                        "It is fully compliant with INVEST."
                    ],
                    "answer": 1,
                    "remedy": "**Remediation:**\nRewrite technical infrastructure tasks into architectural enablers tied to measurable customer outcomes, or split them into small, valuable vertical slices (e.g., 'As an account holder, I want multi-factor biometric authentication so that my banking funds are protected against unauthorized credential theft')."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "INVEST Acronym Challenge",
                    "question": "In the INVEST acronym for user stories, the letter 'S' stands for _____ (sized to fit within a single sprint).\n\nAnswer: _____",
                    "answer": "Small",
                    "alternatives": ["Small", "small"],
                    "explanation": "**Why Small is Correct:**\n**Small** user stories minimize risk and enable rapid feedback, typically taking 2 to 3 days of development."
                }
            ]
        }
    ]
}

# CASE 03: Requirements Engineering & QFD Analysis
SYLLABUS_PART1["3"] = {
    "title": "Case 03: Requirements Engineering & QFD Analysis",
    "episodes": [
        {
            "title": "Module 1: Problem Analysis, Elicitation & Requirements Validation",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Fred Brooks observed: *'No other part of the work so cripples the resulting system if done wrong.'* Requirements Engineering encompasses Problem Analysis, Elicitation, Specification, and Validation."
                },
                {
                    "type": "objective",
                    "title": "Module Objective",
                    "content": "Master requirement elicitation techniques (Interviews, Shadowing, JAD), distinguish between functional and non-functional requirements, and validate requirements against ambiguity."
                },
                {
                    "type": "concept",
                    "title": "The Requirements Engineering Triad",
                    "content": "1. **Problem Analysis:** Understanding the root business problem before jumping to software solutions. Use Ishikawa (Fishbone) diagrams and Root Cause Analysis.\n2. **Elicitation Techniques:**\n   - *Contextual Inquiries & Shadowing:* Watching users perform their real jobs to detect unstated workarounds.\n   - *Structured Interviews:* Gathering explicit requirements.\n   - *Joint Application Development (JAD):* Intensive cross-functional workshops with stakeholders and architects.\n3. **Requirements Validation:** Inspecting requirements to ensure they are complete, consistent, verifiable, and unambiguous."
                },
                {
                    "type": "interactive",
                    "title": "Requirements Precision Challenge",
                    "question": "Which of the following requirement statements is verifiable and testable according to IEEE standards?",
                    "options": [
                        "The web application shall be extremely fast, robust, and user friendly.",
                        "The system shall display the search results page within 800 milliseconds for 95% of queries under a concurrent load of 2,000 requests per second.",
                        "The database must gracefully handle errors.",
                        "The software should be modular enough to handle future business growth."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nStatement B defines a mathematically verifiable threshold: 800 ms at the 95th percentile under 2,000 req/sec load. A QA engineer can construct an automated benchmark test to definitively prove whether the requirement passes or fails. The other options use subjective, untestable fluff ('fast', 'gracefully', 'future growth')."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Elicitation Acronym Challenge",
                    "question": "The facilitated collaborative workshop where business clients and developers work together in intensive sessions to elicit requirements is called _____ (Joint Application Development).\n\nAnswer: _____",
                    "answer": "JAD",
                    "alternatives": ["JAD", "jad", "Joint Application Development"],
                    "explanation": "**Why JAD is Correct:**\n**JAD (Joint Application Development)** breaks down stakeholder communication barriers through structured, facilitated group sessions."
                }
            ]
        },
        {
            "title": "Module 2: Quality Function Deployment (QFD) & The Kano Model",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "How do you translate subjective customer desires into concrete engineering specifications? **Quality Function Deployment (QFD)**, originating from Yoji Akao in Japan, uses the **House of Quality** and the **Kano Model** to classify requirements."
                },
                {
                    "type": "concept",
                    "title": "The Three QFD Requirement Categories",
                    "content": "1. **Normal Requirements (One-Dimensional / Spoken):**\n   - Capabilities that customers explicitly ask for during interviews (e.g. 'The banking app must show my transaction history and calculate interest').\n   - Customer satisfaction increases linearly with their implementation.\n2. **Expected Requirements (Must-Be / Basic):**\n   - Fundamental capabilities that the customer does **not** explicitly state because they assume they are obvious (e.g. 'The app must not crash when I log in', 'My password must be securely encrypted', 'The ATM must dispense real currency').\n   - If present, customer satisfaction is neutral; if missing, customer dissatisfaction is catastrophic.\n3. **Excited Requirements (Attractive / Delighters):**\n   - Features beyond the customer's imagination that create unexpected joy (e.g. 'The app automatically detects subscription price hikes and cancels unwanted recurring charges with one click').\n   - If absent, customer does not notice; if present, customer loyalty soars."
                },
                {
                    "type": "visual",
                    "title": "The QFD / Kano Requirement Spectrum",
                    "code": """graph TD
  subgraph Excited ["Excited Requirements (Delighters)"]
    E1["Unexpected Joy: Proactive fraud warnings, instant auto-categorization"]
  end
  subgraph Normal ["Normal Requirements (Explicitly Requested)"]
    N1["Stated Features: Search, download PDF statements, fund transfers"]
  end
  subgraph Expected ["Expected Requirements (Unspoken Baselines)"]
    B1["Assumed Invariants: High uptime, data encryption, zero data corruption"]
  end
  Excited --> Normal --> Expected
  style Excited fill:#064e3b,stroke:#10b981
  style Normal fill:#1e1b4b,stroke:#6366f1
  style Expected fill:#3f1a1a,stroke:#ef4444"""
                },
                {
                    "type": "interactive",
                    "title": "QFD Classification Challenge",
                    "question": "A customer is testing a new mobile banking app. When asked what they think of the fact that logging in requires entering a password, they say: 'Well of course it requires authentication, that's obvious.' How does QFD classify this requirement?",
                    "options": [
                        "Excited Requirement.",
                        "Expected Requirement (a basic unstated requirement whose presence is taken for granted).",
                        "Normal Requirement.",
                        "Gold Plating."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nIn QFD, **Expected Requirements** are fundamental baseline expectations that users do not explicitly request because they take them for granted. If missing, the customer is furious; if present, satisfaction is merely baseline."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Methodology Acronym Challenge",
                    "question": "The Japanese engineering technique for translating customer voice into technical software specifications is _____ (Quality Function Deployment).\n\nAnswer: _____",
                    "answer": "QFD",
                    "alternatives": ["QFD", "qfd", "Quality Function Deployment"],
                    "explanation": "**Why QFD is Correct:**\n**QFD (Quality Function Deployment)** uses matrices like the House of Quality to map customer needs directly to technical requirements."
                }
            ]
        },
        {
            "title": "Module 3: Requirements Modeling: Use Case Scenarios & Templates",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Ivar Jacobson introduced **Use Cases** in 1992 to capture functional requirements as a series of interactions between external **Actors** and the **System Under Consideration**."
                },
                {
                    "type": "concept",
                    "title": "Standard Use Case Template Components",
                    "content": "A formal Use Case specification template includes:\n- **Use Case ID & Title:** (e.g. `UC-101: Withdraw Cash from ATM`)\n- **Primary Actor:** The entity initiating the interaction (e.g. `Bank Customer`).\n- **Preconditions:** System state that must be True before the use case can start (e.g. `Customer card inserted and PIN verified`).\n- **Main Success Scenario (Happy Path):** Chronological numbered steps from trigger to successful goal completion.\n- **Extensions / Alternate Flows:** Numbered branches handling errors and edge conditions (e.g. `4a. Insufficient ATM cash -> Display error and eject card`).\n- **Postconditions:** Guarantees of system state upon completion (e.g. `Account debited and cash dispensed`)."
                },
                {
                    "type": "interactive",
                    "title": "Use Case Modeling Challenge",
                    "question": "In a formal Use Case template, what is the role of an Extension (Alternate Flow)?",
                    "options": [
                        "It lists the marketing team's contact phone numbers.",
                        "It documents the exception and alternative execution paths when the main success scenario cannot complete.",
                        "It describes the database indexes used by the SQL query.",
                        "It lists the compiler flags used to build the binary."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nThe **Extensions (Alternate Flows)** capture error handling, exceptional events (e.g., network disconnect, insufficient funds, expired credentials), and alternative user choices that branch off from the happy path."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Use Case Pioneer Challenge",
                    "question": "The computer scientist who invented Use Cases in 1992 is Ivar _____.\n\nAnswer: _____",
                    "answer": "Jacobson",
                    "alternatives": ["Jacobson", "jacobson", "Ivar Jacobson"],
                    "explanation": "**Why Jacobson is Correct:**\n**Dr. Ivar Jacobson** introduced Use Cases in his 1992 book *Object-Oriented Software Engineering* (OOSE), later co-creating UML."
                }
            ]
        },
        {
            "title": "Module 4: Documenting the Software Requirement Specification (SRS)",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "The **Software Requirements Specification (SRS)** is the formal legal and technical baseline governed internationally by **IEEE 830** and **ISO/IEC/IEEE 29148**."
                },
                {
                    "type": "concept",
                    "title": "The 8 IEEE 830 SRS Quality Invariants",
                    "content": "An SRS must be:\n1. **Correct:** Every requirement matches an actual customer need.\n2. **Unambiguous:** Has exactly one interpretation for all readers.\n3. **Complete:** Specifies responses to both valid and invalid inputs.\n4. **Consistent:** No requirement conflicts with another.\n5. **Ranked for Importance/Stability:** Distinguishes mandatory vs optional features.\n6. **Verifiable:** A finite, cost-effective test can prove conformance.\n7. **Modifiable:** Easily updated without breaking structural integrity.\n8. **Traceable:** Can be traced forward to design/test and backward to business need."
                },
                {
                    "type": "scenario_decision",
                    "title": "SRS Requirement Conflict Dilemma",
                    "scenario": "During an SRS review, you find two requirements: REQ-14 states: 'The mobile app must never store customer cryptographic tokens in local device storage for security compliance.' REQ-89 states: 'The mobile app must allow full offline transaction processing when the device has zero internet connectivity.' The product team says: 'Just approve both.'",
                    "question": "What is your professional action as lead requirements engineer?",
                    "options": [
                        "Approve both: let developers figure it out during coding.",
                        "Flag an SRS Inconsistency defect: REQ-14 and REQ-89 are fundamentally contradictory; convene a CCB meeting to renegotiate the security baseline before signing the SRS.",
                        "Delete REQ-14 and ignore security.",
                        "Delete REQ-89 and ignore offline mode without telling the customer."
                    ],
                    "answer": 1,
                    "rationale": "**Why Flagging an Inconsistency is Mandatory:**\nIEEE 830 mandates that an SRS must be **Consistent**. Signing off on contradictory requirements creates massive confusion during implementation and guarantees failed acceptance testing. The contradiction must be formally resolved via the Change Control Board before baselining."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "IEEE Standard Number Challenge",
                    "question": "The landmark IEEE standard specification for Software Requirements Specifications is IEEE _____.\n\nAnswer: _____",
                    "answer": "830",
                    "alternatives": ["830", "IEEE 830", "IEEE-830"],
                    "explanation": "**Why 830 is Correct:**\n**IEEE 830** (Recommended Practice for Software Requirements Specifications) is the classic global standard for structured software specifications."
                }
            ]
        }
    ]
}

print("Built Syllabus Part 1 (Cases 00-03) successfully!")

with open('/Users/aadarshamahato/Downloads/LEARNING_PLATFORM/se_story_lab/cases_part1.json', 'w', encoding='utf-8') as f:
    json.dump(SYLLABUS_PART1, f, indent=4)
