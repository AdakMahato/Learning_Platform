import json
import os

SYLLABUS_PART2 = {}

# CASE 04: Requirements Modeling & The IEEE SRS Specification
SYLLABUS_PART2["4"] = {
    "title": "Case 04: Requirements Modeling & The IEEE SRS Specification",
    "episodes": [
        {
            "title": "Module 1: Use Case Scenarios & Formal Use Case Template",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Requirements engineering bridges the informal, messy world of user desires and the rigorous world of software architecture. Without formal modeling, ambiguity festers, leading to the #1 cause of software project failure: building the wrong system perfectly."
                },
                {
                    "type": "objective",
                    "title": "Module Objective",
                    "content": "Master Use Case Scenario templates, define actors and preconditions, and structure robust Main Success Scenarios and Alternative/Exception Flows."
                },
                {
                    "type": "concept",
                    "title": "Anatomy of an Industry-Standard Use Case Template (Alistair Cockburn)",
                    "content": "A formal Use Case documents an actor interacting with the system to achieve an observable goal:\n- **Use Case ID & Title:** Unique identifier (e.g., `UC-04: Process Checkout`).\n- **Primary Actor:** The entity initiating the goal (e.g., `Registered Customer`).\n- **Secondary Actors:** External supporting systems (e.g., `Payment Gateway`, `Tax Calculation API`).\n- **Preconditions:** System state that must be strictly true before execution (e.g., `Customer authenticated, cart has >= 1 in-stock item`).\n- **Trigger:** Event initiating the use case (e.g., `User clicks 'Confirm Order'`).\n- **Main Success Scenario (Happy Path):** Numbered sequence of interactions.\n- **Alternative / Exceptional Flows:** Branches handling invalid card, out-of-stock inventory, or network timeout.\n- **Postconditions (Guarantees):** Guaranteed state upon completion (e.g., `Order stored in state 'PAID', invoice emailed, inventory decremented`)."
                },
                {
                    "type": "visual",
                    "title": "Use Case Lifecycle Flow",
                    "code": """graph TD
  PRE["Preconditions Verified"] --> TRIG["Trigger Event (User Action)"]
  TRIG --> HAPPY["Main Success Scenario (Happy Path)"]
  HAPPY --> POST["Guaranteed Postconditions"]
  
  HAPPY -.->|Validation Failed| ALT1["Alt Flow 3a: Payment Declined"]
  HAPPY -.->|Service Timeout| ALT2["Alt Flow 4a: Retry Circuit Breaker"]
  ALT1 --> HAPPY
  ALT2 --> CANCEL["Postcondition: Transaction Aborted"]"""
                },
                {
                    "type": "micro_challenge",
                    "title": "Use Case Preconditions",
                    "question": "What is the primary role of a 'Precondition' in a formal Use Case specification?",
                    "options": [
                        "It lists the programming languages used to write the backend.",
                        "It states the mandatory conditions and system state that must hold true before the use case can begin execution.",
                        "It defines the UI font and color palette.",
                        "It lists all the tests written by QA."
                    ],
                    "answer": 1,
                    "explanation": "**Why Preconditions is Correct:**\n**Preconditions** define the contractual state that must be guaranteed by the system before the trigger event is permitted to initiate the use case."
                }
            ]
        },
        {
            "title": "Module 2: The IEEE 830 / ISO 29148 Standard for SRS",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "The **Software Requirements Specification (SRS)** is the formal contract between stakeholders and software engineers. IEEE 830 (now codified under ISO/IEC/IEEE 29148) establishes the universal standard for SRS composition."
                },
                {
                    "type": "concept",
                    "title": "IEEE 830: The 7 Core Quality Characteristics of an SRS",
                    "content": "A high-quality SRS must satisfy 7 rigorous criteria:\n1. **Correct:** Every requirement reflects an actual verified customer need.\n2. **Unambiguous:** Every stated requirement has exactly one interpretation (prohibits words like 'fast', 'user-friendly', 'optimal').\n3. **Complete:** Defines all essential requirements, responses to both valid and invalid inputs, and external interfaces.\n4. **Consistent:** No requirement conflicts with another (e.g., REQ-14 does not contradict REQ-89).\n5. **Verifiable (Testable):** Quantifiable metrics exist so a cost-effective test can definitively PASS or FAIL the implementation.\n6. **Modifiable:** Structured and indexed with cross-references so changes can be made systematically.\n7. **Traceable:** Each requirement contains backward traceability to business origin and forward traceability to design classes and test cases."
                },
                {
                    "type": "scenario_decision",
                    "title": "Engineering Dilemma: Resolving Ambiguous Performance Requirements",
                    "scenario": "You are auditing an SRS draft submitted for an emergency healthcare dispatch system. Requirement REQ-204 states: 'The system must respond quickly and provide real-time updates to dispatchers under heavy load.' The junior architect argues this is acceptable for the preliminary baseline.",
                    "question": "How should the lead systems engineer remediate REQ-204 to satisfy IEEE 830 standards?",
                    "options": [
                        "Leave it as is; 'quickly' and 'real-time' are self-explanatory terms in emergency dispatching.",
                        "Rewrite REQ-204 with quantifiable thresholds: 'Under a peak load of 500 concurrent emergency incidents, 99.5% of dispatcher telemetry queries must return in <= 250 milliseconds.'",
                        "Change the requirement to: 'The system will use high-speed C++ multi-threading so that queries run as fast as possible.'",
                        "Delete REQ-204 because non-functional performance cannot be formally verified."
                    ],
                    "answer": 1,
                    "rationale": "**Why Quantifiable Precision is Essential:**\nIEEE 830 strictly prohibits subjective qualitative adjectives like 'quickly', 'robust', or 'real-time'. An unambiguous, verifiable requirement must specify concrete workload conditions (500 concurrent incidents), percentile metrics (99.5th percentile), and exact time bounds (<= 250 ms) that can be verified during load testing."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "IEEE Standard Number Challenge",
                    "question": "The classic global IEEE standard specification for Software Requirements Specifications is IEEE _____.\n\nAnswer: _____",
                    "answer": "830",
                    "alternatives": ["830", "IEEE 830", "IEEE-830"],
                    "explanation": "**Why 830 is Correct:**\n**IEEE 830** (Recommended Practice for Software Requirements Specifications) is the classic global benchmark for structured software requirements specifications."
                }
            ]
        },
        {
            "title": "Module 3: Requirement Validation & Traceability Matrix (RTM)",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "How do engineers ensure that every customer requirement is actually designed, implemented in code, and verified by test cases without scope creep or missed features?"
                },
                {
                    "type": "concept",
                    "title": "Requirements Traceability Matrix (RTM)",
                    "content": "An **RTM** is a multi-directional grid that links requirements through every stage of the software lifecycle:\n- **Backward Traceability:** Links a requirement to the specific business need, stakeholder interview, or regulation that justified it.\n- **Forward Traceability:** Links a requirement to its architectural design class, code module, and test case IDs.\n\n| Req ID | Requirement Description | Design Component | Code File | Test Case ID | Status |\n| :--- | :--- | :--- | :--- | :--- | :--- |\n| **REQ-01** | Support OAuth2 Login | `AuthService` | `auth.py` | `TC-AUTH-01` | Passed |\n| **REQ-02** | Export PDF Invoice | `PDFRenderer` | `invoice.py` | `TC-BILL-04` | Passed |\n| **REQ-03** | 2FA SMS Verification | `TwoFactorAdapter` | `sms_2fa.py` | `TC-AUTH-09` | In Progress |"
                },
                {
                    "type": "micro_challenge",
                    "title": "Traceability Direction",
                    "question": "What is the purpose of **Forward Traceability** in a Requirements Traceability Matrix?",
                    "options": [
                        "To trace who will pay for the software project.",
                        "To verify that every requirement in the SRS is mapped to a specific architectural design module, source code file, and verification test case.",
                        "To forecast the team's stock options.",
                        "To trace backward to the historical origins of the company."
                    ],
                    "answer": 1,
                    "explanation": "**Why Forward Traceability is Correct:**\nForward traceability ensures complete implementation coverage by demonstrating that every baselined requirement is carried forward into design, implementation, and test suites."
                }
            ]
        },
        {
            "title": "Module 4: Requirements Modeling & IEEE SRS Synthesis",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Let us evaluate formal SRS quality attributes in a real-world project crisis."
                },
                {
                    "type": "scenario_decision",
                    "title": "Engineering Dilemma: Scope Creep vs Baselines",
                    "scenario": "Two weeks before the scheduled release of an air traffic radar visualization system, the client sends an email: 'Can we also add 3D terrain rendering and drone flight path tracking?' The junior project manager wants to accept immediately to keep the client happy.",
                    "question": "As Lead Software Requirements Engineer, what is the correct professional process?",
                    "options": [
                        "Immediately add the features directly into the active sprint without telling the developers.",
                        "Submit the proposed changes as formal Change Requests (CR) to the Change Control Board (CCB), conduct an impact analysis on safety verification, cost, and schedule, and schedule the features for Phase 2 after baselining Version 1.0.",
                        "Refuse to ever speak to the client again.",
                        "Delete half of the radar features to make room for the 3D terrain."
                    ],
                    "answer": 1,
                    "rationale": "**Why Formal SCM and Impact Analysis are Essential:**\nUncontrolled requirements additions without impact analysis is the textbook definition of **Scope Creep**. In mission-critical software, introducing major architectural changes late without rigorous verification compromises system stability. Formal CCB review preserves baseline integrity."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "IEEE 830 Quality Attribute",
                    "question": "If a requirement can be verified by a concrete test procedure that conclusively yields a PASS or FAIL result, the requirement satisfies the IEEE 830 characteristic of being _____.\n\nAnswer: _____",
                    "answer": "Verifiable",
                    "alternatives": ["Verifiable", "Testable"],
                    "explanation": "**Why Verifiable is Correct:**\n**Verifiable** (or Testable) means that there exists a finite, cost-effective process by which a person or machine can verify that the software product meets the requirement."
                }
            ]
        }
    ]
}

# CASE 05: Process Modeling: DFDs, Data Dictionary & PSPEC
SYLLABUS_PART2["5"] = {
    "title": "Case 05: Process Modeling: DFDs, Data Dictionary & PSPEC",
    "episodes": [
        {
            "title": "Module 1: Data Flow Diagrams & Level Decomposition (0, 1, 2)",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Data Flow Diagrams (DFDs), pioneered by Larry Constantine, Edward Yourdon, and Tom DeMarco, model how data transforms as it moves through a system without implying execution sequence, loops, or timing constraints."
                },
                {
                    "type": "objective",
                    "title": "Module Objective",
                    "content": "Learn DFD notations across Level 0 (Context Diagram), Level 1, and Level 2 decompositions, and understand data flow transformation semantics."
                },
                {
                    "type": "concept",
                    "title": "The Four Primitive Elements of a DFD",
                    "content": "Regardless of whether Yourdon-DeMarco (circles) or Gane-Sarson (rounded rectangles) notation is used, all DFDs consist of 4 symbols:\n1. **External Entity (Source / Sink):** Rectangles representing entities outside the system boundary (users, external bank APIs, hardware sensors) that produce or consume data.\n2. **Process:** Circles or rounded rectangles that transform incoming data flows into outgoing data flows.\n3. **Data Store:** Parallel open lines or open rectangles representing data at rest (files, database tables, buffers).\n4. **Data Flow:** Directed arrows representing data in motion with descriptive noun labels."
                },
                {
                    "type": "visual",
                    "title": "Level 0 Context Diagram vs Level 1 Decomposition",
                    "code": """graph LR
  subgraph Level0 ["Level 0: System Context Diagram"]
    CUST["Customer Entity"] -->|Login & Order Data| SYS["0.0 E-Commerce System"]
    SYS -->|Invoice & Shipping Confirmation| CUST
    SYS -->|Payment Transaction| GATE["Payment Gateway"]
    GATE -->|Authorization Token| SYS
  end
  subgraph Level1 ["Level 1: System Decomposition"]
    P1["1.0 Authenticate User"]
    P2["2.0 Validate Cart & Pricing"]
    P3["3.0 Process Payment"]
    DB1[("User Store")]
    DB2[("Order Store")]
    P1 <--> DB1
    P1 -->|User Token| P2
    P2 -->|Order Items| DB2
    P2 -->|Billed Amount| P3
  end"""
                },
                {
                    "type": "micro_challenge",
                    "title": "Level 0 Context Diagram Process Count",
                    "question": "How many total processes are permitted to appear in a formal Level 0 System Context Diagram?",
                    "options": [
                        "Exactly 1 single process representing the entire software system boundary (e.g., '0.0 System')",
                        "As many as the developers want (typically 10 to 15)",
                        "Zero processes; only data stores appear in Level 0",
                        "Exactly 5 processes"
                    ],
                    "answer": 0,
                    "explanation": "**Why Exactly 1 Process is Correct:**\nA **Level 0 Context Diagram** represents the entire system as a single central bubble (`0.0`), surrounded solely by external entities and high-level input/output data flows."
                }
            ]
        },
        {
            "title": "Module 2: DFD Conservation Rules: Spotting Black Holes & Miracles",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "In process modeling, data cannot spontaneously generate out of nothing, nor can it vanish into thin air. Every DFD must obey the universal laws of data conservation."
                },
                {
                    "type": "concept",
                    "title": "The Golden Rules of DFD Conservation",
                    "content": "- **No Black Holes:** A process cannot have only input data flows with zero outputs.\n- **No Miracles (White Holes):** A process cannot have only output data flows with zero inputs.\n- **No Gray Holes:** A process where inputs are insufficient to generate the outputs (e.g., inputs: `Customer Name`, output: `Calculated Net Tax`).\n- **No Entity-to-Entity flows:** External entities cannot talk directly to each other within the system DFD.\n- **No Entity-to-Data Store flows:** External entities cannot directly read or write a Data Store without going through a mediating process.\n- **No Data Store-to-Data Store flows:** Data stores cannot directly exchange data without a process."
                },
                {
                    "type": "diagram_critique",
                    "title": "DFD Review: Detect the Data Conservation Violation",
                    "scenario": "Review the Level 1 DFD below for an ATM banking subsystem. A junior analyst modeled the cash replenishment and card verification processes.",
                    "code": """graph TD
  USER["Bank Customer"] -->|Card PIN & Request| P1["1.0 Verify Credentials"]
  P1 -->|Session Token| P2["2.0 Dispense Cash"]
  P2 -->|Dispense Command| CASH_BOX["Cash Dispenser Mechanism"]
  
  AUDIT_LOG[("D1: Security Audit Log")]
  DB_ACCTS[("D2: Core Accounts Database")]
  
  P1 -->|Log Auth Event| AUDIT_LOG
  DB_ACCTS -->|Direct Account Mirroring| AUDIT_LOG
  
  P3["3.0 Calculate Monthly Interest"]
  P3 -->|Accrued Interest Balance| DB_ACCTS""",
                    "question": "Which two critical DFD syntax and conservation defects are present in this diagram?",
                    "options": [
                        "P1 has too many outputs, and USER cannot be an external entity.",
                        "Process 3.0 is a Miracle (White Hole) having no inputs, and DB_ACCTS connects directly to AUDIT_LOG with no mediating process.",
                        "P2 cannot send commands to CASH_BOX, and D1 cannot have write flows.",
                        "There are no defects; direct data store sync is standard in modern DFDs."
                    ],
                    "answer": 1,
                    "remedy": "**Architectural Remediation:**\n1. **Miracle Violation:** Process 3.0 produces `Accrued Interest Balance` without receiving any inputs (account balance, interest rate, dates) - data cannot be created out of nothing.\n2. **Store-to-Store Violation:** Data Store D2 connects directly to D1 without a mediating process. In DFD theory, a data store is passive storage; it possesses no compute engine to copy data without a process (e.g., `4.0 Sync Database Logs`)."
                }
            ]
        },
        {
            "title": "Module 3: Data Dictionary Algebraic Notation Standard",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "A DFD shows the anatomy of data flow, but does not define the composition of data. The **Data Dictionary** formally specifies the exact structure of every data flow and data store."
                },
                {
                    "type": "concept",
                    "title": "The Data Dictionary Notation Standard (Tom DeMarco)",
                    "content": "A Data Dictionary formally describes composite data packets using structured algebraic symbols:\n- `=` : **Is composed of / Equivalent to**\n- `+` : **Sequence (AND)**\n- `[ | ]` : **Selection (OR / Mutually Exclusive Options)**\n- `{}` : **Iteration (Repetition / 0 or more occurrences)** (can specify bounds: `1{item}10`)\n- `()` : **Optional element (0 or 1 occurrence)**\n- `**` : **Comment / Clarification note**\n\n### Example:\n```text\nCustomer_Order = Order_ID + Customer_ID + 1{Item_Entry}50 + Payment_Method + (Discount_Coupon)\nPayment_Method = [ Credit_Card | Debit_Card | Net_Banking | UPI ]\nCredit_Card = Card_Number + Expiry_Date + CVV + Cardholder_Name\nDiscount_Coupon = * Alphanumeric promo code up to 12 chars *\n```"
                },
                {
                    "type": "micro_challenge",
                    "title": "Data Dictionary Notation Audit",
                    "question": "In a formal Data Dictionary, how is an optional middle name in a customer name record represented?",
                    "options": [
                        "Customer_Name = First_Name + [Middle_Name] + Last_Name",
                        "Customer_Name = First_Name + (Middle_Name) + Last_Name",
                        "Customer_Name = First_Name + {Middle_Name} + Last_Name",
                        "Customer_Name = First_Name + *Middle_Name* + Last_Name"
                    ],
                    "answer": 1,
                    "explanation": "**Why Parentheses `()` is Correct:**\nIn standard Data Dictionary notation, parentheses `()` designate an **optional** element (0 or 1 instance). Square brackets `[ | ]` denote selection (OR), braces `{}` denote iteration/repetition, and asterisks `**` denote comments."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Data Dictionary Repetition Symbol",
                    "question": "In standard Data Dictionary notation, the character symbols used to denote iteration or repetition of an element are curly braces, represented as _____.\n\nAnswer: _____",
                    "answer": "{}",
                    "alternatives": ["{}", "{ }", "braces", "curly braces"],
                    "explanation": "**Why `{}` is Correct:**\nIn Data Dictionary algebraic notation, curly braces `{}` designate 0 or more repetitions of a data component."
                }
            ]
        },
        {
            "title": "Module 4: Process Specification (PSPEC) & Decision Tables",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "A **PSPEC (Process Specification)** specifies the internal transformation logic for each primitive (lowest-level) process in a DFD."
                },
                {
                    "type": "concept",
                    "title": "PSPEC Tools & The Complete Analysis Model",
                    "content": "PSPECs are authored using three primary formats:\n1. **Structured English:** Algorithmic pseudo-prose using `IF-THEN-ELSE`, `CASE`, and `WHILE` without language-specific syntax.\n2. **Decision Tables:** Tabular mapping of complex condition combinations to resulting actions (ideal for combinatorial business logic).\n3. **Decision Trees:** Tree representations showing branching decision rules.\n\n### The Complete Structured Analysis Model:\n- **Data Dictionary:** Central repository defining all data attributes.\n- **Data Flow Diagram (DFD):** Functional model showing transformations.\n- **Entity-Relationship Diagram (ERD):** Data model showing persistent entities and relationships.\n- **State Transition Diagram (STD):** Behavioral model showing system states and transitions.\n- **PSPEC / CSPEC:** Detailed algorithmic logic and control specifications."
                },
                {
                    "type": "calculation_challenge",
                    "title": "Decision Table Completeness Calculation",
                    "formula": "Total\\ Combinations = 2^{Number\\ of\\ Binary\\ Conditions}",
                    "problem": "An insurance claim processing engine has 4 independent binary validation conditions:\n1. Policy active? (Yes/No)\n2. Premium paid up to date? (Yes/No)\n3. Claim amount <= Coverage limit? (Yes/No)\n4. Police report submitted for theft claims? (Yes/No)\n\nTo ensure 100% formal completeness with zero missing edge cases, how many total distinct decision rules (columns) must the comprehensive decision table contain?",
                    "answer": "16",
                    "alternatives": ["16", "16 rules", "16 columns"],
                    "step_by_step": "**Mathematical Derivation:**\n- Number of binary conditions $k = 4$.\n- Each condition has 2 possible boolean states (True/False).\n- Total mutually exclusive combinatorial states = $2^k = 2^4 = 16$.\n- Therefore, a complete decision table before rule reduction must evaluate exactly 16 distinct condition stubs/rules."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Lowest Level DFD Process Name",
                    "question": "A process in a Data Flow Diagram that is not decomposed any further and whose logic is directly specified by a PSPEC is called a _____ process.\n\nAnswer: _____",
                    "answer": "Primitive",
                    "alternatives": ["Primitive", "Functional Primitive"],
                    "explanation": "**Why Primitive is Correct:**\nIn structured analysis, a **primitive process** (or functional primitive) represents the atomic leaf level of functional decomposition."
                }
            ]
        }
    ]
}

# CASE 06: Design Principles: Modularity, Cohesion & Coupling
SYLLABUS_PART2["6"] = {
    "title": "Case 06: Design Principles: Modularity, Cohesion & Coupling",
    "episodes": [
        {
            "title": "Module 1: Core Design Principles & Information Hiding",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Software design translates requirements into a blueprint for construction. The hallmarks of sustainable architecture are high modularity, high cohesion, and low coupling."
                },
                {
                    "type": "objective",
                    "title": "Module Objective",
                    "content": "Master architectural abstraction, separation of concerns, David Parnas's principle of Information Hiding, and the structural metrics of fan-in and fan-out."
                },
                {
                    "type": "concept",
                    "title": "The Pillars of Software Design",
                    "content": "- **Levels of Abstraction:** Architectural design defines high-level subsystems, communication protocols, and databases; Detailed design specifies component algorithms, data structures, and interface signatures.\n- **Separation of Concerns (SoC):** A software system is decomposed into distinct, non-overlapping sections, each addressing a single concern (e.g., UI rendering, business rule evaluation, persistence, network transport).\n- **Modularity:** Dividing a program into distinct, independently testable units. High modularity reduces cognitive load and enables parallel development.\n- **Information Hiding (David Parnas, 1972):** Every module encapsulates an architectural secret (an algorithm, data structure, or hardware quirk). Clients interact only with a stable, abstract interface, remaining entirely insulated from internal representation changes."
                },
                {
                    "type": "concept",
                    "title": "Structural Metrics: Fan-In vs Fan-Out",
                    "content": "- **Fan-Out:** The number of subordinate modules called by a given module. A very high fan-out (> 7) indicates excessive coordination complexity and a lack of intermediate abstraction.\n- **Fan-In:** The number of superior modules that invoke a given module. High fan-in is a sign of good reusability (utility/shared library functions like `math.sin` or `auth.verify_token`).\n- **Target Structural Shape:** A healthy system architecture resembles an inverted pyramid or tree: low to moderate fan-out at top control layers, converging to high fan-in at bottom foundation utilities."
                },
                {
                    "type": "micro_challenge",
                    "title": "Information Hiding Principle",
                    "question": "Who formulated the seminal software engineering principle of Information Hiding in 1972 ('On the Criteria to Be Used in Decomposing Systems into Modules')?",
                    "options": [
                        "Alan Turing",
                        "David L. Parnas",
                        "Edsger W. Dijkstra",
                        "Barry Boehm"
                    ],
                    "answer": 1,
                    "explanation": "**Why David Parnas is Correct:**\n**David L. Parnas** authored the 1972 paper demonstrating that modules should be decomposed around design decisions that are likely to change (hiding the 'secret')."
                }
            ]
        },
        {
            "title": "Module 2: The 7 Levels of Cohesion (Worst to Best)",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "**Cohesion** measures the degree of functional relatedness and focus of elements within a single module. High cohesion is the primary goal of modular design."
                },
                {
                    "type": "concept",
                    "title": "The Complete Cohesion Spectrum (Larry Constantine & Edward Yourdon)",
                    "content": "Ranked from worst (undesirable) to best (ideal):\n\n1. **Coincidental (Worst):** Elements are grouped arbitrarily with zero meaningful relationship (e.g., a `CommonUtils` class containing `reverse_string()`, `calculate_tax()`, and `send_bluetooth_packet()`).\n2. **Logical:** Elements perform logically similar activities, but which one executes is determined by a passed-in flag or code (e.g., a function `print_all(type)` containing a giant switch-case for employees, products, and receipts).\n3. **Temporal:** Elements are grouped solely because they execute at the same point in time (e.g., `system_startup()` initializing logging, zeroing memory, and launching network sockets).\n4. **Procedural:** Elements execute in a specific sequence to accomplish a task, but work on unrelated data structures.\n5. **Communicational:** Elements operate on the exact same input dataset or produce the exact same output dataset (e.g., `analyze_customer()` which computes credit score, generates personalized ads, and updates spending habits from customer profile).\n6. **Sequential:** The output of one element serves as the direct input to the next element, like an assembly line or UNIX pipeline (e.g., `read_compressed_file() -> decompress() -> parse_json()`).\n7. **Functional (Best):** Every element within the module is dedicated to executing exactly one well-defined mathematical or business computation (e.g., `calculate_compound_interest()`, `compute_sha256()`)."
                },
                {
                    "type": "micro_challenge",
                    "title": "Classifying Module Cohesion",
                    "question": "A developer creates a module named `DataReporter` with a single method `process_records(int mode)` containing a `switch(mode)` that either prints student grades, prints inventory counts, or prints server ping statistics. What level of cohesion does this exhibit?",
                    "options": [
                        "Functional Cohesion",
                        "Logical Cohesion",
                        "Sequential Cohesion",
                        "Communicational Cohesion"
                    ],
                    "answer": 1,
                    "explanation": "**Why Logical Cohesion is Correct:**\nThe operations share an abstract semantic category ('printing / reporting'), but the specific code executed is selected by an arbitrary control parameter (`mode`). This is textbook **Logical Cohesion**, which is fragile and difficult to maintain."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Highest Cohesion Level",
                    "question": "The highest and most desirable level of cohesion, where all module parts contribute strictly to a single well-defined task, is _____ cohesion.\n\nAnswer: _____",
                    "answer": "Functional",
                    "alternatives": ["Functional", "Functional Cohesion"],
                    "explanation": "**Why Functional is Correct:**\n**Functional Cohesion** is the pinnacle of modular design because the module does one thing and does it completely without side effects."
                }
            ]
        },
        {
            "title": "Module 3: The 5 Levels of Coupling (Worst to Best)",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "**Coupling** measures the degree of interdependence and structural coupling between two modules. Our architectural objective is always: **Maximize Cohesion, Minimize Coupling**."
                },
                {
                    "type": "concept",
                    "title": "The Complete Coupling Spectrum",
                    "content": "Ranked from worst (tightly coupled / dangerous) to best (loosely coupled / clean):\n\n1. **Content Coupling (Worst / Pathological):** One module directly modifies or accesses the internal data, memory, or execution branch of another module (e.g., jumping into another function's middle with `goto` or modifying a private field directly).\n2. **Common Coupling:** Two or more modules share read/write access to the same global data environment or global variables (e.g., Module A and Module B both mutating `GLOBAL_SYSTEM_CONFIG`).\n3. **Control Coupling:** One module passes a control flag or boolean switch to another module with the explicit purpose of dictating its internal logic flow.\n4. **Stamp Coupling (Data-Structured Coupling):** Modules share a composite data structure (e.g., a `CustomerRecord` class with 40 fields), but the receiving module only uses 1 or 2 fields (e.g., `zip_code`). This exposes the module to changes in fields it doesn't need.\n5. **Data Coupling (Best):** Modules communicate strictly by passing elementary, primitive data items as parameters (e.g., `calculate_circle_area(radius: float)`). Each parameter is necessary and sufficient."
                },
                {
                    "type": "visual",
                    "title": "Coupling Architecture Comparison",
                    "code": """graph TD
  subgraph TightlyCoupled ["Common Coupling (Hazardous)"]
    M1["Billing Module"] -->|Mutates| G[("Global State")]
    M2["Shipping Module"] -->|Mutates| G
    M3["Auth Module"] -->|Reads & Writes| G
  end
  subgraph LooselyCoupled ["Data Coupling (Clean)"]
    O["Order Controller"] -->|order_id: int| B["Billing Service"]
    O -->|address: str, weight: float| S["Shipping Service"]
  end"""
                },
                {
                    "type": "micro_challenge",
                    "title": "Coupling Classification Challenge",
                    "question": "Module A invokes Module B by passing an entire `Employee` object (containing 50 attributes including medical history, salary, bank details, and home address). However, Module B only needs the employee's `department_id` to route an internal ticket. What type of coupling is this?",
                    "options": [
                        "Data Coupling",
                        "Stamp Coupling",
                        "Common Coupling",
                        "Content Coupling"
                    ],
                    "answer": 1,
                    "explanation": "**Why Stamp Coupling is Correct:**\n**Stamp Coupling** occurs when an entire structured composite record is passed, but only a fraction of its fields are actually consumed. This tightly binds Module B to changes in the `Employee` schema."
                }
            ]
        },
        {
            "title": "Module 4: Architectural Trade-off Audit & Refactoring Dilemma",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Now we synthesize modularity, cohesion, and coupling to solve a real-world enterprise architecture crisis."
                },
                {
                    "type": "scenario_decision",
                    "title": "Refactoring the God-Class Anti-Pattern",
                    "scenario": "You are auditing a 12,000-line monolith class called `OrderManager`. It handles credit card validation, SQL inserts, invoice PDF generation, SMS notifications, and delivery truck scheduling. Modifying the PDF template frequently breaks the database transaction logic. The team wants to keep it because 'everything is in one place'.",
                    "question": "What architectural refactoring strategy should the engineering team execute?",
                    "options": [
                        "Keep the class as is, but write more unit tests to catch regression errors.",
                        "Decompose `OrderManager` into distinct functionally cohesive services: `PaymentService`, `InvoiceGenerator`, `NotificationService`, and `FulfillmentService`, wired together via minimal data coupling or an event bus.",
                        "Merge `OrderManager` with `UserManager` to create a single unified central management controller.",
                        "Convert all private methods to public static methods so any module can call them directly."
                    ],
                    "answer": 1,
                    "rationale": "**Why Decomposition into Cohesive Services is Essential:**\n`OrderManager` is a classic **God Object** suffering from coincidental/procedural cohesion and widespread content/common coupling. Breaking it down into focused single-responsibility services elevates cohesion to **Functional** and reduces coupling to clean **Data Coupling**, isolating changes to PDF formatting from payment persistence."
                },
                {
                    "type": "calculation_challenge",
                    "title": "Card and Agresti Structural Complexity Metric",
                    "formula": "S(i) = (f_{out}(i))^2",
                    "problem": "In software metrics (Card and Agresti), the structural complexity $S(i)$ of an architectural module $i$ is proportional to the square of its fan-out $f_{out}(i)$.\n\nIf an orchestration controller calls 6 distinct subordinate worker modules ($f_{out} = 6$), what is its structural complexity score $S(i)$?",
                    "answer": "36",
                    "alternatives": ["36", "36.0"],
                    "step_by_step": "**Mathematical Derivation:**\n- Fan-out $f_{out} = 6$.\n- Structural Complexity $S(i) = (f_{out})^2 = 6^2 = 36$.\n- This quadratic growth illustrates why architects strive to limit fan-out to moderate bounds (typically $\\le 7 \\pm 2$)."
                }
            ]
        }
    ]
}

# CASE 07: Structured & Object-Oriented Design
SYLLABUS_PART2["7"] = {
    "title": "Case 07: Structured & Object-Oriented Design",
    "episodes": [
        {
            "title": "Module 1: Structured Design & Top-Down Functional Decomposition",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Before object-oriented programming became dominant, **Structured Design** formalized how software systems could be systematically engineered through hierarchical functional decomposition."
                },
                {
                    "type": "objective",
                    "title": "Module Objective",
                    "content": "Understand top-down functional decomposition, contrast structured design with object-oriented paradigms, and evaluate component-level design classes."
                },
                {
                    "type": "concept",
                    "title": "Principles of Top-Down Functional Decomposition",
                    "content": "- **Divide and Conquer:** A complex problem is broken down into a hierarchy of smaller, more manageable sub-problems.\n- **Stepwise Refinement (Niklaus Wirth):** Starting from high-level operational statements, each step decomposes procedural statements into lower-level operational primitives until direct code implementation is trivial.\n- **Structure Charts:** The graphical modeling tool for structured design. Boxes represent modules, directed arrows represent invocation, and annotations represent passed data couples (open circles) and control couples (solid circles).\n- **Limitations:** Data and procedures are separated. When business rules or data formats change, ripples spread across multiple decomposed functions."
                },
                {
                    "type": "micro_challenge",
                    "title": "Structured Design Representation",
                    "question": "In a formal Structure Chart, what does an arrow with an open circle ($\\\\circ\\\\rightarrow$) at its tail represent, compared to an arrow with a solid black circle ($\\\\bullet\\\\rightarrow$)?",
                    "options": [
                        "Open circle is a Data Couple; solid circle is a Control Couple (flag).",
                        "Open circle is a Database Write; solid circle is a Database Read.",
                        "Open circle is a Function Call; solid circle is a Return Value.",
                        "Open circle is a Class; solid circle is an Object instance."
                    ],
                    "answer": 0,
                    "explanation": "**Why Data Couple vs Control Couple is Correct:**\nIn Structure Chart syntax, an arrow with an open circle $\\circ\\rightarrow$ represents a **Data Couple** (pure data passed between modules). An arrow with a solid filled circle $\\bullet\\rightarrow$ represents a **Control Couple** (a control flag or status indicator that directs logic decisions)."
                }
            ]
        },
        {
            "title": "Module 2: Component-Level & Object-Oriented Design",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Object-Oriented Design (OOD) unifies data attributes with the operations that manipulate them, organizing software around stable problem-domain entities rather than ephemeral functional steps."
                },
                {
                    "type": "concept",
                    "title": "Core Tenets of Object-Oriented Design",
                    "content": "- **Encapsulation:** Packaging state and behavior together while hiding internal representation behind a public contract.\n- **Polymorphism:** The ability of different classes to respond to the same message with type-specific behavior, enabling dynamic dispatch.\n- **Component-Level Design:** In component-level design, software engineers specify:\n  1. **Boundary Classes:** Interface elements through which actors communicate.\n  2. **Entity Classes:** Persistent data models and business rules.\n  3. **Control Classes:** Coordinators managing transactional execution lifecycles."
                },
                {
                    "type": "concept",
                    "title": "Structured Design vs Object-Oriented Design",
                    "content": "| Dimension | Structured Design | Object-Oriented Design |\n| :--- | :--- | :--- |\n| **Core Unit** | Function / Procedure | Class / Object (Data + Behavior) |\n| **Focus** | Functional Decomposition (Actions) | Problem Domain Modeling (Entities) |\n| **Data Scope** | Data flows across decoupled routines | Data encapsulated inside class boundaries |\n| **Change Resilience** | Fragile when data structures change | Resilient; changes encapsulated inside objects |\n| **Primary Artifact** | DFD, Structure Chart, PSPEC | UML Class, Sequence & State diagrams |"
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Analysis Class Category",
                    "question": "In component-level design, classes that represent persistent information residing in databases or file storage are classified as _____ classes.\n\nAnswer: _____",
                    "answer": "Entity",
                    "alternatives": ["Entity", "Entity classes"],
                    "explanation": "**Why Entity is Correct:**\nAnalysis and design classes are formally categorized into **Boundary Classes** (UI/APIs), **Entity Classes** (persistent data models), and **Control Classes** (business logic/coordination)."
                }
            ]
        },
        {
            "title": "Module 3: User Interface Design Principles & Nielsen's 10 Heuristics",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "A system can possess flawless architecture and zero unit test bugs, yet fail catastrophically if its User Interface (UI) induces cognitive overload or operator error."
                },
                {
                    "type": "concept",
                    "title": "Theo Mandel's 3 Golden Rules of UI Design",
                    "content": "1. **Place the user in control:** Do not force users into compulsory rigid interactions; provide undo/redo, customizable workflows, and non-blocking dialogs.\n2. **Reduce the user's memory load:** Humans can only hold $7 \\pm 2$ chunks of information in short-term working memory. Never require users to re-enter or remember information across screens.\n3. **Make the interface consistent:** Visual cues, icons, keyboard shortcuts, and navigation mechanisms must remain uniform across every module."
                },
                {
                    "type": "concept",
                    "title": "Jakob Nielsen's 10 Usability Heuristics",
                    "content": "The global industry standard for interface usability evaluation:\n1. **Visibility of system status:** Always keep users informed through appropriate, timely feedback (progress bars, spinners).\n2. **Match between system and real world:** Use language, phrases, and concepts familiar to the user, not internal technical jargon.\n3. **User control and freedom:** Provide a clearly marked 'Emergency Exit' to leave unwanted states (Undo, Cancel).\n4. **Consistency and standards:** Follow platform conventions so users don't wonder whether different words mean the same thing.\n5. **Error prevention:** Eliminate error-prone conditions or check for them and present confirmation options before commit.\n6. **Recognition rather than recall:** Minimize the user's memory load by making elements, actions, and options visible.\n7. **Flexibility and efficiency of use:** Provide accelerators (hotkeys, macros) for expert users while keeping simplicity for novices.\n8. **Aesthetic and minimalist design:** Dialogues should not contain irrelevant or rarely needed information.\n9. **Help users recognize, diagnose, and recover from errors:** Error messages should be expressed in plain language (no raw hex stack traces), precisely indicate the problem, and constructively suggest a solution.\n10. **Help and documentation:** Easy to search and focused on concrete task steps."
                },
                {
                    "type": "diagram_critique",
                    "title": "UI Usability Audit: Identify the Violated Heuristic",
                    "scenario": "A hospital patient administration portal displays this error dialog when a nurse enters a patient ID during an emergency room admission:",
                    "code": """graph TD
  subgraph ErrorDialog ["Modal Dialog: Error Code 0x80040E14"]
    TITLE["❌ Fatal SQLException in Subroutine 4"]
    MSG["ORA-00942: table or view does not exist at DAL.PatientRepo.cs:L402"]
    BTN["[ OK ]"]
  end""",
                    "question": "Which of Jakob Nielsen's 10 Usability Heuristics is most severely violated by this error interface?",
                    "options": [
                        "Heuristic 7: Flexibility and efficiency of use.",
                        "Heuristic 9: Help users recognize, diagnose, and recover from errors (and Heuristic 2: Match between system and real world).",
                        "Heuristic 10: Help and documentation.",
                        "Heuristic 3: User control and freedom."
                    ],
                    "answer": 1,
                    "remedy": "**Usability Remediation:**\nThe interface displays raw SQL database stack traces (`ORA-00942`, `0x80040E14`) instead of plain language. It fails to tell the clinical user what happened (e.g., 'Patient record could not be found or connection interrupted') and offers zero constructive guidance on how to recover (e.g., 'Verify patient registration number or retry connection')."
                }
            ]
        },
        {
            "title": "Module 4: Usability Engineering Dilemma",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Let us evaluate high-stakes interface design under life-critical operational conditions."
                },
                {
                    "type": "scenario_decision",
                    "title": "Design Decision: Destructive Action Safeguards",
                    "scenario": "You are designing the nuclear turbine shutdown interface for a power plant control room. The junior developer suggests placing a simple red 'Emergency SCRAM Shutdown' button directly adjacent to the 'Screen Brightness Toggle' button to make it immediately accessible.",
                    "question": "Which UI design safeguard must be implemented to satisfy error prevention principles?",
                    "options": [
                        "Keep the buttons side-by-side; power plant operators are trained not to click the wrong button.",
                        "Apply physical/visual separation, a protective confirmation cover/two-stage modal verification, and distinct spatial color-coding so accidental activation is physically impossible.",
                        "Remove the shutdown button and require operators to type a 20-character SQL command in the terminal.",
                        "Make the button invisible until hovered over."
                    ],
                    "answer": 1,
                    "rationale": "**Why Error Prevention is Paramount:**\nUnder Nielsen's 5th Heuristic (**Error Prevention**), critical or irreversible destructive actions must be insulated from accidental clicks through physical separation, distinct tactile/visual feedback, and two-step confirmation mechanisms."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Human Cognitive Memory Bound",
                    "question": "According to George Miller's psychological law, human short-term memory can store approximately 7 plus or minus _____ chunks of information.\n\nAnswer: _____",
                    "answer": "2",
                    "alternatives": ["2", "two"],
                    "explanation": "**Why 2 is Correct:**\nMiller's Law ($7 \\pm 2$) dictates that human working memory is severely limited, providing the empirical foundation for Nielsen's **Recognition rather than recall** heuristic."
                }
            ]
        }
    ]
}

print("Built Syllabus Part 2 (Cases 04-07) successfully!")

with open('/Users/aadarshamahato/Downloads/LEARNING_PLATFORM/se_story_lab/cases_part2.json', 'w', encoding='utf-8') as f:
    json.dump(SYLLABUS_PART2, f, indent=4)
