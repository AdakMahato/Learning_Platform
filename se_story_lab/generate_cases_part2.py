import json
import os

PART2_CASES = {}

# CASE 05: The Clean Coder (Extreme Programming & TDD)
PART2_CASES["5"] = {
    "title": "Case 05: The Clean Coder",
    "episodes": [
        {
            "title": "Module 1: Extreme Programming (XP) Core Practices",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "In 1996, Kent Beck created **Extreme Programming (XP)** during the Chrysler Comprehensive Compensation (C3) payroll project. Beck asked: *'If testing is good, let everyone test all the time. If code reviews are good, review code continuously via pair programming. If simplicity is good, always leave the system in the simplest possible state.'* XP took proven software practices to 'extreme' levels."
                },
                {
                    "type": "objective",
                    "title": "Module Objective",
                    "content": "Master the 12 classic practices of Extreme Programming, understand the psychological dynamics of Pair Programming, and apply Continuous Refactoring."
                },
                {
                    "type": "concept",
                    "title": "The 12 Core XP Practices",
                    "content": "1. **Planning Game:** Rapidly determine scope of next release by combining business priorities with technical estimates.\n2. **Small Releases:** Ship minimal useful increments frequently.\n3. **Metaphor:** Establish a shared mental story explaining how the system works.\n4. **Simple Design:** Implement only what is required today; eliminate speculative generality (YAGNI).\n5. **Testing (TDD):** Automated unit tests written before production code; 100% test pass rate required.\n6. **Refactoring:** Continuous design restructuring without altering external observable behavior.\n7. **Pair Programming:** Two developers write code together at one workstation (Driver and Navigator).\n8. **Collective Ownership:** Anyone can change any line of code anywhere in the project at any time.\n9. **Continuous Integration:** Merge and test code multiple times per day.\n10. **40-Hour Week (Sustainable Pace):** Overtime is a symptom of process failure and is forbidden two weeks in a row.\n11. **On-site Customer:** A real end user sits with the engineering team full-time.\n12. **Coding Standards:** Uniform naming and formatting rules across the entire codebase."
                },
                {
                    "type": "visual",
                    "title": "The XP Feedback Rings",
                    "code": """graph TD
  subgraph InnerLoop ["Second-by-Second & Minute-by-Minute Loop"]
    PAIR["Pair Programming (Driver & Navigator)"]
    UT["Automated Unit Tests & TDD"]
    PAIR <--> UT
  end
  subgraph MidLoop ["Hour-by-Hour & Daily Loop"]
    CI["Continuous Integration Server"]
    STANDUP["Daily Standup"]
    InnerLoop --> CI --> STANDUP
  end
  subgraph OuterLoop ["Weekly & Release Loop"]
    OSC["On-site Customer Acceptance"]
    RELEASE["Small Production Release"]
    MidLoop --> OSC --> RELEASE
  end
  style InnerLoop fill:#064e3b,stroke:#10b981
  style MidLoop fill:#1e1b4b,stroke:#6366f1
  style OuterLoop fill:#0f172a,stroke:#3b82f6"""
                },
                {
                    "type": "interactive",
                    "title": "Pair Programming Role Challenge",
                    "question": "In standard Extreme Programming Pair Programming, what is the division of cognitive responsibility between the Driver and the Navigator?",
                    "options": [
                        "The Driver writes the code while the Navigator checks emails and manages Jira tickets.",
                        "The Driver operates the keyboard focusing on tactical line-by-line syntax, while the Navigator observes strategically, checking for edge cases, design consistency, and test coverage.",
                        "The Driver dictates code verbally while the Navigator types as fast as possible.",
                        "The Driver writes unit tests while the Navigator writes the production classes on a separate computer."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nIn pair programming, the **Driver** has tactical control of the keyboard and mouse, focusing on writing clean syntax. The **Navigator** maintains strategic perspective: reviewing the code as it is typed, anticipating edge cases, validating against the larger architecture, and looking up documentation."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "XP Acronym Challenge",
                    "question": "The foundational XP principle that forbids implementing features based on speculation of future needs is known by the acronym _____ ('You Aren't Gonna Need It').\n\nAnswer: _____",
                    "answer": "YAGNI",
                    "alternatives": ["YAGNI", "yagni", "You Aren't Gonna Need It"],
                    "explanation": "**Why YAGNI is Correct:**\n**YAGNI** prevents speculative over-engineering. Building unrequested features wastes current development capacity and creates dead code that must be maintained indefinitely."
                }
            ]
        },
        {
            "title": "Module 2: The TDD Rhythm: Red-Green-Refactor",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Test-Driven Development (TDD) reverses traditional software construction: **you write the test before you write a single line of production code**. It operates in a rapid, heartbeat-like 3-step cycle."
                },
                {
                    "type": "concept",
                    "title": "The Red-Green-Refactor Cycle",
                    "content": "1. **RED:** Write a tiny automated test that expresses a single requirement or edge case. Run the test suite and verify that the new test **fails** (ideally because the feature does not exist yet). If it passes without code, your test is invalid!\n2. **GREEN:** Write the minimal, simplest production code necessary to make the test pass. 'Sinful' code (hardcoded returns, simple conditionals) is encouraged to reach green quickly.\n3. **REFACTOR:** With the safety net of passing tests, clean up the design: eliminate duplication, rename variables for clarity, extract helper functions, and enforce SOLID principles while keeping all tests 100% green."
                },
                {
                    "type": "visual",
                    "title": "The TDD Finite State Machine",
                    "code": """graph LR
  subgraph RedPhase ["1. RED"]
    R1["Write 1 Failing Test"]
    R2["Verify Test Fails! ❌"]
    R1 --> R2
  end
  subgraph GreenPhase ["2. GREEN"]
    G1["Write Simplest Code"]
    G2["All Tests Pass! ✅"]
    G1 --> G2
  end
  subgraph RefactorPhase ["3. REFACTOR"]
    RF1["Clean Code & Remove Duplication"]
    RF2["Verify Tests STILL Pass! 🛡️"]
    RF1 --> RF2
  end
  R2 --> G1
  G2 --> RF1
  RF2 -->|"Next Increment"| R1
  style RedPhase fill:#3f1a1a,stroke:#ef4444
  style GreenPhase fill:#064e3b,stroke:#10b981
  style RefactorPhase fill:#1e1b4b,stroke:#6366f1"""
                },
                {
                    "type": "interactive",
                    "title": "TDD Invariant Challenge",
                    "question": "Why is it mandatory in TDD to run the new test and watch it fail (RED) before writing any production code?",
                    "options": [
                        "To measure the execution speed of the test runner.",
                        "To prove that the test actually tests something and does not pass trivially due to a tautology or faulty assertion.",
                        "To trigger the continuous integration deployment pipeline.",
                        "To notify the QA department that a test was authored."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nA test that passes before code is written is either testing nothing, asserting on a tautology (`assert True`), or testing existing behavior. Seeing the test fail with the expected error verifies that the test correctly detects the absence of the requested feature."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Refactoring Definition Challenge",
                    "question": "Martin Fowler defines refactoring as the process of changing a software system's internal structure without altering its external _____.\n\nAnswer: _____",
                    "answer": "Behavior",
                    "alternatives": ["Behavior", "behavior", "Observable Behavior", "observable behavior"],
                    "explanation": "**Why Behavior is Correct:**\nRefactoring strictly preserves **observable behavior**. If functionality is added, removed, or changed, it is a feature modification or bug fix, not a refactoring."
                }
            ]
        },
        {
            "title": "Module 3: Code Refactoring in Action",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Let's put TDD refactoring into practice. Legacy code often contains duplicated calculations, deep nesting, and hardcoded magical literals."
                },
                {
                    "type": "code_lab",
                    "title": "TDD Invoice Tax Refactorer",
                    "instructions": "Implement `InvoiceCalculator` with methods `add_item(name, price, tax_category)` and `calculate_total()` supporting zero, standard (10%), and luxury (20%) tax categories, properly handling rounding and invalid inputs.",
                    "starter_code": """class InvoiceCalculator:
    \"\"\"
    A robust, refactored invoice calculator following clean code principles.
    \"\"\"
    TAX_RATES = {
        'exempt': 0.0,
        'standard': 0.10,
        'luxury': 0.20
    }
    
    def __init__(self):
        self.items = []
        
    def add_item(self, name: str, price: float, tax_category: str = 'standard'):
        # TODO: Validate and store line item
        pass
        
    def calculate_summary(self) -> dict:
        \"\"\"
        Returns dict:
          - 'subtotal': sum of prices (float rounded to 2 decimals)
          - 'total_tax': total tax computed per item (float rounded to 2 decimals)
          - 'grand_total': subtotal + total_tax (float rounded to 2 decimals)
          - 'item_count': int
        \"\"\"
        # TODO: Compute invoice breakdown
        pass
""",
                    "solution_code": """class InvoiceCalculator:
    TAX_RATES = {
        'exempt': 0.0,
        'standard': 0.10,
        'luxury': 0.20
    }
    
    def __init__(self):
        self.items = []
        
    def add_item(self, name: str, price: float, tax_category: str = 'standard'):
        if price < 0:
            raise ValueError("Price cannot be negative")
        if tax_category not in self.TAX_RATES:
            raise ValueError(f"Invalid tax category: {tax_category}")
        self.items.append({
            'name': name.strip(),
            'price': float(price),
            'tax_category': tax_category
        })
        
    def calculate_summary(self) -> dict:
        subtotal = 0.0
        total_tax = 0.0
        
        for item in self.items:
            price = item['price']
            rate = self.TAX_RATES[item['tax_category']]
            subtotal += price
            total_tax += price * rate
            
        subtotal = round(subtotal, 2)
        total_tax = round(total_tax, 2)
        grand_total = round(subtotal + total_tax, 2)
        
        return {
            'subtotal': subtotal,
            'total_tax': total_tax,
            'grand_total': grand_total,
            'item_count': len(self.items)
        }
""",
                    "test_code": """calc = InvoiceCalculator()
calc.add_item("Book", 20.0, "exempt")
calc.add_item("Headphones", 100.0, "standard")
calc.add_item("Champagne", 200.0, "luxury")

summary = calc.calculate_summary()
assert summary['item_count'] == 3
assert summary['subtotal'] == 320.0
assert summary['total_tax'] == 50.0  # 0 + 10 + 40
assert summary['grand_total'] == 370.0

try:
    calc.add_item("Bad Item", -10.0)
    assert False, "Should have raised ValueError"
except ValueError:
    pass

print("TDD Invoice Calculator tests passed successfully!")
""",
                    "why_works": "**Why This Solution Works:**\nThe refactored class encapsulates tax knowledge into a class-level dictionary (`TAX_RATES`), validates boundary inputs (rejecting negative prices and unvetted tax tiers), and rounds all currency values cleanly at presentation boundaries.",
                    "alternatives": "**Alternative Approaches & Trade-offs:**\n- **Strategy Pattern:** For complex enterprise tax systems with regional jurisdictions, encapsulate each tax rule into a `TaxStrategy` class.\n- **Decimal Module:** For banking applications, use `decimal.Decimal` instead of `float` to eliminate IEEE 754 floating-point inaccuracies.",
                    "edge_cases": "**Edge Cases & Failure Modes:**\n- Empty invoice: Returns 0.0 for subtotal, tax, and grand total with 0 item count.\n- Unknown tax category: Immediately raises `ValueError` before corrupting calculations."
                }
            ]
        },
        {
            "title": "Module 4: Collective Ownership vs. Code Silos",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Traditional organizations assign components to individual 'code owners'. In contrast, Extreme Programming mandates **Collective Code Ownership**."
                },
                {
                    "type": "concept",
                    "title": "The Truck (Bus) Factor",
                    "content": "- **Truck (Bus) Factor:** The minimum number of team members who, if hit by a bus (or quitting for a higher salary), would stall the project indefinitely.\n- **Individual Silos:** Bus Factor = 1. If Alice wrote the auth module alone and leaves, nobody understands how authentication works.\n- **Collective Ownership:** Bus Factor = Entire Team. Because pair programming rotates pairs across the whole codebase daily and automated tests verify everything, any engineer can modify or debug any subsystem."
                },
                {
                    "type": "interactive",
                    "title": "Engineering Resiliency Challenge",
                    "question": "What is the primary prerequisite for Collective Code Ownership to succeed without devolving into chaos?",
                    "options": [
                        "Requiring developers to get written permission from the CTO before editing someone else's file.",
                        "A comprehensive suite of automated tests that can be run on-demand in seconds to verify that modifications didn't break existing functionality.",
                        "Locking the repository so only one person can commit per day.",
                        "Rewriting the entire project in an interpreted language."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nCollective ownership fails catastrophically if developers are terrified of breaking code they didn't write. Fast, automated unit and integration tests provide the psychological safety net needed for developers to refactor freely across all modules."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Team Metric Challenge",
                    "question": "The software risk metric representing the minimum number of engineers who must suddenly leave before a project becomes unmaintainable is the _____ factor.\n\nAnswer: _____",
                    "answer": "Bus",
                    "alternatives": ["Bus", "Truck", "bus", "truck", "Bus Factor", "Truck Factor"],
                    "explanation": "**Why Bus Factor is Correct:**\nThe **Bus Factor** (or Truck Factor) measures structural knowledge concentration. High-performing engineering teams actively work to maximize their bus factor through pair programming and documentation."
                }
            ]
        }
    ]
}

# CASE 06: The Elusive Specification (Requirements Engineering)
PART2_CASES["6"] = {
    "title": "Case 06: The Elusive Specification",
    "episodes": [
        {
            "title": "Module 1: Requirements Engineering & FURPS+",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Fred Brooks stated in *The Mythical Man-Month*: *'The hardest single part of building a software system is deciding precisely what to build... No other part of the work so cripples the resulting system if done wrong.'* Requirements Engineering is the systematic process of discovering, analyzing, documenting, and validating the needs of stakeholders."
                },
                {
                    "type": "objective",
                    "title": "Module Objective",
                    "content": "Distinguish between Functional and Non-Functional Requirements, classify architectural constraints using FURPS+, and master stakeholder elicitation techniques."
                },
                {
                    "type": "concept",
                    "title": "Functional vs. Non-Functional Requirements",
                    "content": "### Functional Requirements (FR)\n- Define **what** the system must do: features, capabilities, calculations, and data processing.\n- *Example:* 'The system shall allow users to transfer funds between checking and savings accounts.'\n\n### Non-Functional Requirements (NFR) / Quality Attributes\n- Define **how** the system performs: criteria used to judge system operation rather than specific behaviors.\n- *Example:* 'The transaction shall complete within 200 milliseconds under a concurrent load of 5,000 requests per second with 99.999% availability.'"
                },
                {
                    "type": "visual",
                    "title": "The Hewlett-Packard FURPS+ Model",
                    "code": """graph TD
  subgraph FR ["Functional Requirements"]
    F["Functionality: Features, Capabilities, Security, Algorithms"]
  end
  subgraph NFR ["Non-Functional Quality Attributes (URPS+)"]
    U["Usability: Human factors, Aesthetics, Consistency, Documentation"]
    R["Reliability: Availability, MTBF, Failure frequency, Recoverability"]
    P["Performance: Latency, Throughput, Memory footprint, Response time"]
    S["Supportability: Maintainability, Testability, Modularity, Extensibility"]
    PLUS["Plus (+): Design, Implementation, Interface, Physical constraints"]
  end
  style FR fill:#064e3b,stroke:#10b981
  style NFR fill:#1e1b4b,stroke:#6366f1"""
                },
                {
                    "type": "interactive",
                    "title": "Requirements Classification Challenge",
                    "question": "A stakeholder requests: 'The system must encrypt all customer credit card numbers at rest using AES-256 and process refund requests in under 1.5 seconds.' How are these classified?",
                    "options": [
                        "Both are pure Functional Requirements.",
                        "Encryption at rest is a Security/Design Constraint (NFR) and refund latency is a Performance NFR.",
                        "Both are Usability Requirements.",
                        "Neither is a valid software requirement."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nAES-256 encryption is a Security/Implementation constraint (part of FURPS+ non-functional requirements), while the 1.5-second response time threshold is a classic Performance non-functional quality attribute."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Quality Attribute Challenge",
                    "question": "In the FURPS acronym, the letter 'R' stands for the quality attribute _____.\n\nAnswer: _____",
                    "answer": "Reliability",
                    "alternatives": ["Reliability", "reliability"],
                    "explanation": "**Why Reliability is Correct:**\n**Reliability** covers availability, fault tolerance, MTBF (Mean Time Between Failures), and disaster recovery."
                }
            ]
        },
        {
            "title": "Module 2: Stakeholder Elicitation & The Ambiguity Trap",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Users rarely know what they need; they only know what hurts. Asking 'What do you want the software to do?' produces vague, contradictory, and incomplete wishlists."
                },
                {
                    "type": "concept",
                    "title": "Elicitation Techniques & Ambiguity Traps",
                    "content": "### Elicitation Techniques:\n1. **Contextual Inquiries & Shadowing:** Watch real operators execute their daily workflows to identify unstated workarounds.\n2. **Structured Interviews & Questionnaires:** Gather quantitative baseline expectations.\n3. **Joint Application Development (JAD) Workshops:** Facilitated sessions bringing business sponsors, users, and architects together.\n\n### The Ambiguity Danger Words:\nRequirements containing words like *'fast'*, *'user-friendly'*, *'robust'*, *'scalable'*, or *'modular'* are untestable. Every requirement must be **quantifiable and verifiable**."
                },
                {
                    "type": "interactive",
                    "title": "Requirement Precision Challenge",
                    "question": "Which of the following requirement statements satisfies the IEEE standard for being verifiable and unambiguous?",
                    "options": [
                        "The checkout page shall be extremely responsive and easy to use.",
                        "The checkout page shall render the order confirmation screen within 500 ms for the 95th percentile of users over a 100 Mbps connection.",
                        "The system shall gracefully handle all possible user mistakes.",
                        "The architecture shall be modular enough to handle future growth."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nStatement B defines a mathematically testable threshold: 500 ms at the 95th percentile under specified network conditions. A QA engineer can build an automated test to definitively prove whether the system passes or fails. The other options use subjective fluff ('responsive', 'gracefully', 'future growth')."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Elicitation Technique Challenge",
                    "question": "The structured requirements-gathering technique where users and engineers collaborate in intensive facilitated workshop sessions is called _____ (Joint Application Development).\n\nAnswer: _____",
                    "answer": "JAD",
                    "alternatives": ["JAD", "jad", "Joint Application Development"],
                    "explanation": "**Why JAD is Correct:**\n**Joint Application Development (JAD)** accelerates requirements gathering by resolving stakeholder conflicts in real time through facilitated group workshops."
                }
            ]
        },
        {
            "title": "Module 3: INVEST Criteria for User Stories",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "In Agile methodologies, requirements are captured as **User Stories** from an end-user perspective: *'As a [persona], I want to [action], so that [business value].'* To evaluate whether a story is ready for development, Bill Wake formulated the **INVEST** mnemonic."
                },
                {
                    "type": "concept",
                    "title": "The INVEST Mnemonic",
                    "content": "- **I — Independent:** Stories should be decoupled so they can be prioritized, developed, and delivered in any order.\n- **N — Negotiable:** A story is not a rigid contract; it is a placeholder for conversation between PO and engineers.\n- **V — Valuable:** Must deliver tangible business value to the end user or customer (not pure technical chores).\n- **E — Estimable:** Team must understand the domain well enough to estimate effort/points.\n- **S — Small:** Sized to fit comfortably within a single sprint (typically 2-3 days of work).\n- **T — Testable:** Accompanied by clear, binary Acceptance Criteria (e.g., Given/When/Then Gherkin syntax)."
                },
                {
                    "type": "visual",
                    "title": "INVEST Quality Filter",
                    "code": """graph TD
  subgraph StoryDraft ["Incoming Raw User Story"]
    RAW["'Build the entire reporting system'"]
  end
  subgraph InvestFilter ["INVEST Evaluation Criteria"]
    I["Independent? (No dependencies)"]
    N["Negotiable? (Open for trade-offs)"]
    V["Valuable? (Delivers real user outcome)"]
    E["Estimable? (Clear enough to size)"]
    S["Small? (Fits in one sprint)"]
    T["Testable? (Clear acceptance criteria)"]
  end
  subgraph ReadyBacklog ["Sprint Ready Backlog"]
    EPIC["Split into 3 Small, Testable Stories! ✅"]
  end
  RAW --> InvestFilter --> ReadyBacklog
  style StoryDraft fill:#3f1a1a,stroke:#ef4444
  style InvestFilter fill:#1e1b4b,stroke:#6366f1
  style ReadyBacklog fill:#064e3b,stroke:#10b981"""
                },
                {
                    "type": "interactive",
                    "title": "INVEST Evaluation Challenge",
                    "question": "A developer is handed a user story: 'As a system, I want to upgrade the Oracle database from v19c to v21c so that the database is newer.' Which INVEST criterion is violated?",
                    "options": [
                        "Independent.",
                        "Valuable — user stories must express direct value to an end user or customer, not internal IT activities written from the 'system' persona.",
                        "Small.",
                        "Estimable."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nUser stories must deliver **Value** to real human users. 'The system' is not a persona, and making the database 'newer' delivers zero customer value. This is a technical infrastructure task or architectural enabler, not a customer user story."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Acceptance Syntax Challenge",
                    "question": "The standard Behavior-Driven Development (BDD) syntax for specifying testable acceptance criteria is Given-When-_____.\n\nAnswer: _____",
                    "answer": "Then",
                    "alternatives": ["Then", "then", "Given When Then"],
                    "explanation": "**Why Then is Correct:**\n**Given-When-Then** (Gherkin syntax) establishes preconditions (Given), actions (When), and expected verifiable outcomes (Then)."
                }
            ]
        },
        {
            "title": "Module 4: Acceptance Criteria Parser Lab",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Behavior-Driven Development (BDD) bridges the gap between non-technical stakeholders and automated test suites by parsing Gherkin scenarios into executable test steps."
                },
                {
                    "type": "code_lab",
                    "title": "Gherkin Acceptance Criteria Parser",
                    "instructions": "Implement `parse_gherkin_scenario(raw_text)` that extracts the Scenario Title, Given preconditions, When action, and Then assertion from a BDD user story specification.",
                    "starter_code": """def parse_gherkin_scenario(raw_text: str) -> dict:
    \"\"\"
    Parse a Gherkin BDD scenario into structured components.
    
    Expected format:
      Scenario: <title>
      Given <precondition>
      When <action>
      Then <expected outcome>
      
    Returns dict:
      {
        'scenario': str,
        'given': str,
        'when': str,
        'then': str,
        'is_valid': bool (True if all 4 components exist and are non-empty)
      }
    \"\"\"
    # TODO: Implement parser
    pass
""",
                    "solution_code": """def parse_gherkin_scenario(raw_text: str) -> dict:
    result = {
        'scenario': '',
        'given': '',
        'when': '',
        'then': '',
        'is_valid': False
    }
    
    for line in raw_text.strip().splitlines():
        line = line.strip()
        if line.startswith('Scenario:'):
            result['scenario'] = line.replace('Scenario:', '').strip()
        elif line.startswith('Given '):
            result['given'] = line[6:].strip()
        elif line.startswith('When '):
            result['when'] = line[5:].strip()
        elif line.startswith('Then '):
            result['then'] = line[5:].strip()
            
    if result['scenario'] and result['given'] and result['when'] and result['then']:
        result['is_valid'] = True
        
    return result
""",
                    "test_code": """raw = \"\"\"
Scenario: Customer transfers money with insufficient funds
Given the customer account balance is $50.00
When the customer attempts to withdraw $100.00
Then the transaction is declined with an OverdraftError
\"\"\"
parsed = parse_gherkin_scenario(raw)
assert parsed['is_valid'] is True
assert parsed['scenario'] == 'Customer transfers money with insufficient funds'
assert parsed['given'] == 'the customer account balance is $50.00'
assert parsed['when'] == 'the customer attempts to withdraw $100.00'
assert parsed['then'] == 'the transaction is declined with an OverdraftError'

invalid_raw = \"Scenario: Missing When\\nGiven user logged in\\nThen user sees dashboard\"
assert parse_gherkin_scenario(invalid_raw)['is_valid'] is False
print("Gherkin parser tests passed successfully!")
""",
                    "why_works": "**Why This Solution Works:**\nParsing BDD specifications ensures requirements are structured as formal test vectors. Automated frameworks like Cucumber and Behave consume these parsed blocks to execute functional verification suites against live APIs.",
                    "alternatives": "**Alternative Approaches & Trade-offs:**\n- **Regex Multiline Matcher:** Can parse complex scenarios with `And` / `But` extensions and data tables.\n- **Decision Table Testing:** Formats combinatorial inputs and outputs into truth tables for exhaustive testing.",
                    "edge_cases": "**Edge Cases & Failure Modes:**\n- Incomplete scenario missing one clause: Correctly sets `is_valid` to `False`.\n- Leading or trailing whitespace on lines: Stripped cleanly before keyword matching."
                }
            ]
        }
    ]
}

# CASE 07: The Blueprint Contract (SRS & Traceability)
PART2_CASES["7"] = {
    "title": "Case 07: The Blueprint Contract",
    "episodes": [
        {
            "title": "Module 1: The IEEE 830 / ISO 29148 Standard SRS",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "The **Software Requirements Specification (SRS)** is the formal legal and technical contract between customer and engineering team. Standardized by IEEE 830 and its modern successor **ISO/IEC/IEEE 29148**, it lays out the functional, performance, safety, and interface boundaries of the system."
                },
                {
                    "type": "objective",
                    "title": "Module Objective",
                    "content": "Understand the standard structure of an IEEE 830 / ISO 29148 SRS, master the 8 quality attributes of a good SRS, and construct a Requirements Traceability Matrix (RTM)."
                },
                {
                    "type": "concept",
                    "title": "The 8 Characteristics of an Excellent SRS",
                    "content": "According to IEEE 830, a well-formed SRS must be:\n1. **Correct:** Every requirement reflects an actual customer or regulatory need.\n2. **Unambiguous:** Every requirement has exactly one interpretation across developers and clients.\n3. **Complete:** Includes all significant requirements, responses to both valid and invalid inputs, and full label definitions.\n4. **Consistent:** No requirement contradicts another (e.g. Req A requires encryption, Req B forbids SSL overhead).\n5. **Ranked for Importance / Stability:** Distinguishes essential, desirable, and optional features.\n6. **Verifiable:** There exists a finite, cost-effective process by which a human or machine can prove the software satisfies the requirement.\n7. **Modifiable:** Structured with table of contents, modular sections, and cross-references so changes don't break document integrity.\n8. **Traceable:** The origin of each requirement is documented forward to design/test artifacts and backward to business drivers."
                },
                {
                    "type": "visual",
                    "title": "IEEE 830 Standard Document Structure",
                    "code": """graph TD
  subgraph Section1 ["1. Introduction"]
    S1A["1.1 Purpose & Scope"]
    S1B["1.2 Definitions, Acronyms, Abbreviations"]
    S1C["1.3 References & Overview"]
  end
  subgraph Section2 ["2. Overall Description"]
    S2A["2.1 Product Perspective & System Interfaces"]
    S2B["2.2 Product Functions & User Characteristics"]
    S2C["2.3 Constraints, Assumptions, Dependencies"]
  end
  subgraph Section3 ["3. Specific Requirements"]
    S3A["3.1 External Interface Requirements"]
    S3B["3.2 Functional Requirements (Req-01 ... Req-N)"]
    S3C["3.3 Non-Functional & Security Constraints"]
  end
  Section1 --> Section2 --> Section3
  style Section1 fill:#0f172a,stroke:#3b82f6
  style Section2 fill:#1e1b4b,stroke:#6366f1
  style Section3 fill:#064e3b,stroke:#10b981"""
                },
                {
                    "type": "interactive",
                    "title": "SRS Quality Flaw Challenge",
                    "question": "An SRS states: 'REQ-42: The system shall be completely safe from all unauthorized cyberattacks at all times.' Which IEEE 830 quality characteristic does this violate most severely?",
                    "options": [
                        "Ranked for Importance.",
                        "Modifiability.",
                        "Verifiability — it is impossible to construct a test that proves zero vulnerabilities exist against all conceivable attacks forever.",
                        "Product Perspective."
                    ],
                    "answer": 2,
                    "explanation": "**Why this is Correct:**\nA requirement must be **Verifiable**. No test exists that can prove a system is immune to all possible cyberattacks forever. A verifiable requirement must specify concrete standards, such as: 'The system shall enforce TLS 1.3 encryption and resist OWASP Top 10 automated test suites with zero High/Critical findings'."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Standard Number Challenge",
                    "question": "The classic IEEE standard for Software Requirements Specifications is IEEE _____.\n\nAnswer: _____",
                    "answer": "830",
                    "alternatives": ["830", "IEEE 830", "IEEE-830"],
                    "explanation": "**Why 830 is Correct:**\n**IEEE 830** (Recommended Practice for Software Requirements Specifications) remains the benchmark standard for formal software specification documentation."
                }
            ]
        },
        {
            "title": "Module 2: The Requirements Traceability Matrix (RTM)",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "How do you know if an essential requirement was forgotten during implementation? Or worse, how do you prove that a developer didn't sneak an unrequested feature (gold plating) into production? The answer is the **Requirements Traceability Matrix (RTM)**."
                },
                {
                    "type": "concept",
                    "title": "Forward and Backward Traceability",
                    "content": "- **Forward Traceability:** Traces from Business Need -> System Requirement (SRS) -> Design Module (UML) -> Code Component -> Test Case. Ensures 100% of requirements are implemented and verified.\n- **Backward Traceability:** Traces from Code/Test -> Design -> SRS -> Business Driver. Ensures that no 'orphaned' code or superfluous features exist without an authorized requirement justification.\n- **Impact Analysis:** When a customer requests a change to REQ-14, the RTM immediately highlights the exact design documents, code classes, and unit test suites that must be modified."
                },
                {
                    "type": "visual",
                    "title": "End-to-End Traceability Chain",
                    "code": """graph LR
  subgraph Stakeholder ["Business Need"]
    BN["BN-01: 2FA Authentication"]
  end
  subgraph Specification ["SRS Requirement"]
    REQ["REQ-101: SMS/TOTP Verification"]
  end
  subgraph Architecture ["Design Blueprint"]
    COMP["AuthTokenService.py"]
  end
  subgraph Quality ["Test Verification"]
    TEST["test_totp_validation()"]
  end
  BN -->|"Forward Trace"| REQ -->|"Allocates to"| COMP -->|"Verified by"| TEST
  TEST -.->|"Backward Trace"| COMP -.-> REQ -.-> BN
  style Stakeholder fill:#0f172a,stroke:#3b82f6
  style Specification fill:#1e1b4b,stroke:#6366f1
  style Architecture fill:#3f1a1a,stroke:#ef4444
  style Quality fill:#064e3b,stroke:#10b981"""
                },
                {
                    "type": "interactive",
                    "title": "Traceability Gap Challenge",
                    "question": "During an audit, QA discovers 500 lines of complex cryptography code in production that has no corresponding requirement in the SRS and no test case. What has occurred?",
                    "options": [
                        "Proper application of Extreme Programming simple design.",
                        "An orphaned implementation / gold plating defect violating backward traceability.",
                        "Successful forward traceability verification.",
                        "Normal behavior in Agile projects."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nCode that cannot be traced backward to an authorized requirement in the SRS is an **orphaned implementation** (unauthorized feature or gold plating). It introduces maintenance debt and security risk without business authorization."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Matrix Acronym Challenge",
                    "question": "The tabular grid linking user requirements to test cases to guarantee full coverage is called the _____ (Requirements Traceability Matrix).\n\nAnswer: _____",
                    "answer": "RTM",
                    "alternatives": ["RTM", "rtm", "Traceability Matrix"],
                    "explanation": "**Why RTM is Correct:**\nThe **Requirements Traceability Matrix (RTM)** is the primary audit artifact used by aerospace, medical, and defense regulators to prove system compliance."
                }
            ]
        },
        {
            "title": "Module 3: Automated RTM Coverage Engine Lab",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Let's build an automated RTM validation engine that verifies 100% test coverage for requirements and flags both orphaned requirements and untested modules."
                },
                {
                    "type": "code_lab",
                    "title": "Traceability Matrix Verifier",
                    "instructions": "Implement `verify_traceability(requirements, mappings)` that computes requirement coverage percentages and identifies untested requirements.",
                    "starter_code": """def verify_traceability(req_ids: list, rtm_mappings: list) -> dict:
    \"\"\"
    Validate requirement-to-test coverage.
    
    req_ids: list of str (e.g. ['REQ-01', 'REQ-02', 'REQ-03'])
    rtm_mappings: list of dicts [{'req_id': str, 'test_id': str, 'status': 'PASS'|'FAIL'}]
    
    Returns dict:
      - 'total_requirements': int
      - 'covered_requirements': int (number of reqs with at least one associated test)
      - 'passed_requirements': int (reqs where ALL associated tests PASS)
      - 'untested_requirements': list of str (req_ids with no test mappings)
      - 'coverage_percent': float (covered / total * 100, rounded to 2 decimals)
    \"\"\"
    # TODO: Implement RTM verification
    pass
""",
                    "solution_code": """def verify_traceability(req_ids: list, rtm_mappings: list) -> dict:
    total = len(req_ids)
    if total == 0:
        return {
            'total_requirements': 0,
            'covered_requirements': 0,
            'passed_requirements': 0,
            'untested_requirements': [],
            'coverage_percent': 100.0
        }
        
    req_tests = {rid: [] for rid in req_ids}
    for m in rtm_mappings:
        rid = m.get('req_id')
        if rid in req_tests:
            req_tests[rid].append(m.get('status', 'FAIL'))
            
    untested = [rid for rid, tests in req_tests.items() if len(tests) == 0]
    covered = total - len(untested)
    
    passed = 0
    for rid, tests in req_tests.items():
        if len(tests) > 0 and all(st == 'PASS' for st in tests):
            passed += 1
            
    coverage_pct = round((covered / total) * 100.0, 2)
    
    return {
        'total_requirements': total,
        'covered_requirements': covered,
        'passed_requirements': passed,
        'untested_requirements': untested,
        'coverage_percent': coverage_pct
    }
""",
                    "test_code": """reqs = ['REQ-01', 'REQ-02', 'REQ-03', 'REQ-04']
mappings = [
    {'req_id': 'REQ-01', 'test_id': 'T101', 'status': 'PASS'},
    {'req_id': 'REQ-01', 'test_id': 'T102', 'status': 'PASS'},
    {'req_id': 'REQ-02', 'test_id': 'T201', 'status': 'FAIL'},
    {'req_id': 'REQ-03', 'test_id': 'T301', 'status': 'PASS'}
]
res = verify_traceability(reqs, mappings)
assert res['total_requirements'] == 4
assert res['covered_requirements'] == 3
assert res['passed_requirements'] == 2 # REQ-01, REQ-03
assert res['untested_requirements'] == ['REQ-04']
assert res['coverage_percent'] == 75.0
print("RTM Verifier tests passed successfully!")
""",
                    "why_works": "**Why This Solution Works:**\nThis algorithm constructs an inverted index of requirements to test execution statuses. It accurately catches REQ-04 as untested, flags REQ-02 because one of its tests failed, and credits only REQ-01 and REQ-03 as fully passed requirements.",
                    "alternatives": "**Alternative Approaches & Trade-offs:**\n- **Bi-directional Graph Traversal:** Storing the RTM as a Directed Acyclic Graph (DAG) in Neo4j to run transitive impact queries across 6 tiers of artifacts.\n- **Git-commit Hook Enforcement:** Blocking merges if a commit diff touches code without referencing an open requirement ID.",
                    "edge_cases": "**Edge Cases & Failure Modes:**\n- `req_ids` is empty: Handled safely, returning 100% coverage without dividing by zero.\n- Mappings reference an unknown req_id: Filtered out gracefully without throwing KeyError."
                }
            ]
        },
        {
            "title": "Module 4: Change Control Boards (CCB) & Scope Creep",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Requirements never stand still. Uncontrolled requirement expansion without corresponding budget or timeline increases is called **Scope Creep**. To prevent projects from being crushed by continuous ad-hoc changes, formal engineering uses a **Change Control Board (CCB)**."
                },
                {
                    "type": "concept",
                    "title": "The Formal Change Control Process",
                    "content": "1. **Change Request (CR) Submission:** Stakeholder submits a formal ticket describing the proposed modification and business motivation.\n2. **Impact Analysis:** Lead architects and project managers evaluate the impact on cost, delivery date, architecture, and regression risk.\n3. **CCB Deliberation:** The Change Control Board (composed of Customer, Engineering Lead, and PM) meets to Approve, Defer, or Reject the CR.\n4. **Baseline Update:** If approved, a new version of the SRS is baselined, budgets and schedules are revised, and the RTM is updated."
                },
                {
                    "type": "interactive",
                    "title": "Scope Control Challenge",
                    "question": "A junior developer accepts a verbal request from a friendly client manager to add 3 new input fields and an email alert to the user profile screen without logging a ticket. What is this practice called?",
                    "options": [
                        "Agile responsiveness.",
                        "Uncontrolled Scope Creep (Gold Plating) bypassing the Change Control Board.",
                        "Continuous Integration.",
                        "Extreme Programming Metaphor."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nImplementing unvetted verbal requests bypasses formal impact analysis, budget allocation, and testing schedules. This informal scope creep is one of the leading causes of budget overruns and missed project milestones."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Governance Acronym Challenge",
                    "question": "The committee of stakeholders responsible for evaluating, approving, or rejecting proposed software requirement modifications is the _____ (Change Control Board).\n\nAnswer: _____",
                    "answer": "CCB",
                    "alternatives": ["CCB", "ccb", "Change Control Board"],
                    "explanation": "**Why CCB is Correct:**\nThe **Change Control Board (CCB)** enforces governance over the system baseline, ensuring every change is justified and budgeted."
                }
            ]
        }
    ]
}

# CASE 08: The Structural Anatomy (UML Structural Diagrams)
PART2_CASES["8"] = {
    "title": "Case 08: The Structural Anatomy",
    "episodes": [
        {
            "title": "Module 1: UML Structural Modeling & Class Diagrams",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "The **Unified Modeling Language (UML)** was unified in the late 1990s by the 'Three Amigos' — Grady Booch, James Rumbaugh, and Ivar Jacobson. UML provides a standardized visual language for specifying, constructing, and documenting software artifacts. Its most fundamental structural view is the **Class Diagram**."
                },
                {
                    "type": "objective",
                    "title": "Module Objective",
                    "content": "Master UML Class syntax (visibility, attributes, operations), differentiate precisely between Association, Aggregation, and Composition, and understand Component and Deployment diagrams."
                },
                {
                    "type": "concept",
                    "title": "UML Class Notation & Member Visibility",
                    "content": "A UML Class box is split into three compartments:\n1. **Top Compartment:** Class Name (Italicized for Abstract classes, `<<interface>>` for Interfaces).\n2. **Middle Compartment:** Attributes: `visibility name : type [multiplicity] = default`\n3. **Bottom Compartment:** Operations: `visibility name(param : type) : return_type`\n\n### Standard UML Visibility Modifiers:\n- `+` **Public:** Accessible by any class.\n- `-` **Private:** Accessible only within this class.\n- `#` **Protected:** Accessible within this class and its derived subclasses.\n- `~` **Package / Package-Private:** Accessible only within the same package."
                },
                {
                    "type": "visual",
                    "title": "UML Class Specification Example",
                    "code": """classDiagram
  class BankAccount {
    -accountNumber : String
    #balance : Double
    +isFrozen : Boolean
    +deposit(amount : Double) : Boolean
    +withdraw(amount : Double) : Boolean
    #calculateInterest() : Double
  }
  class SavingsAccount {
    -interestRate : Double
    +applyMonthlyInterest() : Void
  }
  BankAccount <|-- SavingsAccount : Generalization / Inheritance"""
                },
                {
                    "type": "interactive",
                    "title": "UML Visibility Syntax Challenge",
                    "question": "In a UML Class diagram, what does the '#' symbol prefixing an attribute or operation designate?",
                    "options": [
                        "Public access across all external packages.",
                        "Private access restricted only to the declaring class.",
                        "Protected access, meaning accessible within the class and its subclasses.",
                        "Static class-level member."
                    ],
                    "answer": 2,
                    "explanation": "**Why this is Correct:**\nIn UML standard syntax, `+` is public, `-` is private, `#` is protected, and `~` is package-private."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "UML Standard Body Challenge",
                    "question": "The international consortium that manages and standardizes the official UML specification is the _____ (Object Management Group).\n\nAnswer: _____",
                    "answer": "OMG",
                    "alternatives": ["OMG", "omg", "Object Management Group"],
                    "explanation": "**Why OMG is Correct:**\nThe **Object Management Group (OMG)** maintains the official UML specification, ensuring compatibility across modeling tools worldwide."
                }
            ]
        },
        {
            "title": "Module 2: Association vs. Aggregation vs. Composition",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "The most critical distinction in Object-Oriented design is relationship strength. Confusing **Aggregation** with **Composition** causes catastrophic memory leaks and architectural coupling bugs."
                },
                {
                    "type": "concept",
                    "title": "Relationship Strength Spectrum",
                    "content": "1. **Association (Uses-A / Knows-A):**\n   - A peer relationship where classes interact but their lifecycles are completely decoupled. Represented by a simple solid line with optional arrow.\n   - *Example:* `Doctor` and `Patient`.\n2. **Aggregation (Has-A / Shared Composition):**\n   - A whole-part relationship where the child part can exist independently of the whole container. Represented by an **open/hollow diamond** at the container end.\n   - *Example:* `Department` and `Professor` (if the department shuts down, the professors still exist).\n3. **Composition (Owns-A / Death-Binding Composition):**\n   - A strong whole-part relationship where the child parts **cannot exist without the parent**. The parent creates and destroys the parts. Represented by a **filled/solid black diamond** at the container end.\n   - *Example:* `House` and `Room`, or `Car` and `Engine` (destroying the car instance destroys its constituent rooms/cylinders)."
                },
                {
                    "type": "visual",
                    "title": "UML Relationship Typology",
                    "code": """classDiagram
  class University
  class Department
  class Professor
  class Course
  class Student

  University "1" *-- "1..*" Department : Composition (Filled Diamond)
  Department "1" o-- "1..*" Professor : Aggregation (Hollow Diamond)
  Professor "1" --> "1..*" Course : Association
  Student "1..*" --> "1..*" Course : Association / Enrollment"""
                },
                {
                    "type": "interactive",
                    "title": "Relationship Identification Challenge",
                    "question": "An e-commerce order contains multiple `OrderLine` items. If the `Order` is deleted from the database, the `OrderLine` items have no reason to exist and are deleted cascade-style. What UML relationship is this?",
                    "options": [
                        "Generalization.",
                        "Weak Aggregation (hollow diamond).",
                        "Composition (solid diamond), because the lifecycle of OrderLine is strictly owned by Order.",
                        "Interface Realization."
                    ],
                    "answer": 2,
                    "explanation": "**Why this is Correct:**\nBecause the lifetime of `OrderLine` is strictly bound to the lifetime of `Order` (they cannot exist independently), this is a textbook example of **Composition** (represented in UML with a filled black diamond)."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "UML Symbol Challenge",
                    "question": "In a UML Class diagram, Aggregation (shared whole-part where parts survive parent deletion) is denoted by an open (hollow) _____ shape.\n\nAnswer: _____",
                    "answer": "Diamond",
                    "alternatives": ["Diamond", "diamond", "Hollow Diamond"],
                    "explanation": "**Why Diamond is Correct:**\nA **hollow diamond** denotes Aggregation, while a **solid filled diamond** denotes Composition."
                }
            ]
        },
        {
            "title": "Module 3: Component & Deployment Topologies",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Class diagrams show compile-time logical abstractions. To model how software packages fit together into binary modules and how those modules map to physical hardware servers, architects use **Component** and **Deployment** diagrams."
                },
                {
                    "type": "concept",
                    "title": "Component vs. Deployment Diagrams",
                    "content": "### Component Diagrams (Binary Packaging)\n- Illustrate modular units of code with well-defined interfaces (JAR files, DLLs, Docker containers, Python packages).\n- Key notation: **Provided Interfaces** (ball / lollipop notation) define what the component exposes; **Required Interfaces** (socket notation) define what it consumes.\n\n### Deployment Diagrams (Physical Infrastructure)\n- Illustrate the runtime hardware nodes (physical servers, cloud VMs, Kubernetes clusters, database clusters) and communication links (HTTPS, gRPC, TCP/IP).\n- Represented by 3D box nodes containing software artifacts."
                },
                {
                    "type": "visual",
                    "title": "Enterprise Deployment Topology",
                    "code": """graph TD
  subgraph ClientNode ["Client Tier (Browser / Mobile)"]
    REACT["React SPA Artifact"]
  end
  subgraph CloudK8s ["Cloud Kubernetes Cluster"]
    INGRESS["NGINX Ingress Gateway"]
    API["Order Processing Microservice (Go Pod)"]
    AUTH["JWT Auth Microservice (Node.js Pod)"]
  end
  subgraph DataTier ["Managed Cloud Database Tier"]
    PG["PostgreSQL Primary Cluster (Multi-AZ)"]
    REDIS["Redis In-Memory Cache"]
  end
  REACT -->|"HTTPS / TLS 1.3"| INGRESS
  INGRESS --> API & AUTH
  API -->|"gRPC"| AUTH
  API -->|"TCP Connection Pool"| PG & REDIS
  style ClientNode fill:#0f172a,stroke:#3b82f6
  style CloudK8s fill:#1e1b4b,stroke:#6366f1
  style DataTier fill:#064e3b,stroke:#10b981"""
                },
                {
                    "type": "interactive",
                    "title": "UML Diagram Selection Challenge",
                    "question": "A DevOps engineer needs to document which Docker containers will run on AWS EC2 instances versus AWS Lambda, and specify the TCP ports open across the VPC security groups. Which UML diagram type should they draw?",
                    "options": [
                        "Use Case Diagram.",
                        "Deployment Diagram.",
                        "Sequence Diagram.",
                        "Class Diagram."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\n**Deployment Diagrams** model the physical execution architecture: mapping software artifacts (containers, binaries) to hardware/virtual compute nodes and specifying network protocols and communication links."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Interface Metaphor Challenge",
                    "question": "In UML component diagrams, the iconic notation for provided and required interfaces is often colloquially called the ball and _____ notation.\n\nAnswer: _____",
                    "answer": "Socket",
                    "alternatives": ["Socket", "socket", "Ball and Socket"],
                    "explanation": "**Why Socket is Correct:**\nThe **ball-and-socket** (or lollipop) notation visually shows how a provided interface (ball) plugs directly into another component's required interface (socket)."
                }
            ]
        },
        {
            "title": "Module 4: Python Class Structure Modeling Lab",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Let's translate a UML class design containing Composition and Aggregation into clean, idiomatic Python code with proper encapsulation and relationship semantics."
                },
                {
                    "type": "code_lab",
                    "title": "UML to Python Architecture Lab",
                    "instructions": "Implement classes `Department` and `University` demonstrating both Composition (University strictly creates and owns Campus buildings) and Aggregation (Department references Professors who can exist independently).",
                    "starter_code": """class Professor:
    def __init__(self, name: str, employee_id: str):
        self.name = name
        self.employee_id = employee_id

class CampusBuilding:
    def __init__(self, building_name: str, square_feet: float):
        self.building_name = building_name
        self.square_feet = square_feet

class University:
    \"\"\"
    University demonstrates:
      - Composition with CampusBuilding (buildings are owned & lifecycle-bound to university)
      - Aggregation with Professor (professors can be added or removed without being destroyed)
    \"\"\"
    def __init__(self, name: str):
        self.name = name
        self.buildings = []  # Composition
        self.faculty = []    # Aggregation
        
    def add_building(self, building_name: str, square_feet: float):
        # TODO: Implement composition (creates instance internally)
        pass
        
    def hire_professor(self, professor: Professor):
        # TODO: Implement aggregation (receives existing instance)
        pass
        
    def get_summary(self) -> dict:
        \"\"\"
        Returns dict:
          - 'name': str
          - 'building_count': int
          - 'total_square_feet': float
          - 'faculty_count': int
        \"\"\"
        # TODO: Return summary stats
        pass
""",
                    "solution_code": """class Professor:
    def __init__(self, name: str, employee_id: str):
        self.name = name
        self.employee_id = employee_id

class CampusBuilding:
    def __init__(self, building_name: str, square_feet: float):
        self.building_name = building_name
        self.square_feet = square_feet

class University:
    def __init__(self, name: str):
        self.name = name
        self.buildings = []
        self.faculty = []
        
    def add_building(self, building_name: str, square_feet: float):
        # Composition: University instantiates and encapsulates the building
        building = CampusBuilding(building_name, square_feet)
        self.buildings.append(building)
        return building
        
    def hire_professor(self, professor: Professor):
        # Aggregation: Professor exists externally and is aggregated
        if not isinstance(professor, Professor):
            raise TypeError("Must be a Professor instance")
        self.faculty.append(professor)
        
    def get_summary(self) -> dict:
        total_sqft = sum(b.square_feet for b in self.buildings)
        return {
            'name': self.name,
            'building_count': len(self.buildings),
            'total_square_feet': round(total_sqft, 2),
            'faculty_count': len(self.faculty)
        }
""",
                    "test_code": """uni = University("Stanford")
prof1 = Professor("Dr. John McCarthy", "E101")
prof2 = Professor("Dr. Donald Knuth", "E102")

uni.hire_professor(prof1)
uni.hire_professor(prof2)
uni.add_building("Gates Computer Science", 50000.0)
uni.add_building("Packard Hall", 35000.0)

summary = uni.get_summary()
assert summary['building_count'] == 2
assert summary['faculty_count'] == 2
assert summary['total_square_feet'] == 85000.0

# Verify aggregation: prof1 survives independent of university
assert prof1.name == "Dr. John McCarthy"
print("UML to Python Architecture tests passed successfully!")
""",
                    "why_works": "**Why This Solution Works:**\nIn Composition, `add_building` receives raw parameters and instantiates `CampusBuilding` internally, tightly coupling its existence to the `University`. In Aggregation, `hire_professor` accepts pre-existing `Professor` instances, ensuring professors have an independent lifecycle.",
                    "alternatives": "**Alternative Approaches & Trade-offs:**\n- **Dependency Injection Container:** For enterprise applications, use containers (like `injector` or Spring) to decouple instantiation while maintaining lifetime scopes (Singleton, Scoped, Transient).\n- **Data Classes:** Python 3.7+ `@dataclass` simplifies boilerplate for purely structural entity nodes.",
                    "edge_cases": "**Edge Cases & Failure Modes:**\n- Passing invalid type to `hire_professor`: Raises `TypeError`.\n- Empty university: Correctly returns 0 buildings, 0 faculty, and 0.0 square feet."
                }
            ]
        }
    ]
}

# CASE 09: The Symphony of Messages (UML Behavioral Diagrams)
PART2_CASES["9"] = {
    "title": "Case 09: The Symphony of Messages",
    "episodes": [
        {
            "title": "Module 1: UML Sequence Diagrams & Dynamic Interactions",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Class diagrams show static spatial structure, but systems live and die in time. How do objects communicate when a user clicks 'Buy Now'? The **UML Sequence Diagram** models object interactions arranged in strict chronological sequence."
                },
                {
                    "type": "objective",
                    "title": "Module Objective",
                    "content": "Master UML Sequence Diagram lifelines, activation bars, and synchronous vs asynchronous arrows; model State Machines; and construct Activity flowcharts."
                },
                {
                    "type": "concept",
                    "title": "Sequence Diagram Core Elements",
                    "content": "1. **Lifeline:** A vertical dashed line representing the existence of an object over time.\n2. **Activation Bar (Focus of Control):** A vertical rectangle placed on a lifeline indicating that the object is currently executing an operation.\n3. **Synchronous Call:** A solid line with a **filled triangular arrowhead** (`->>`). The sender blocks waiting for a return.\n4. **Asynchronous Call:** A solid line with an **open/stick arrowhead** (`->`). The sender fires the message and immediately continues without blocking (e.g. RabbitMQ / Kafka event).\n5. **Return Message:** A dashed line with an open arrowhead (`-->>`) returning control and data to the caller."
                },
                {
                    "type": "visual",
                    "title": "Payment Authorization Sequence",
                    "code": """sequenceDiagram
  autonumber
  actor User
  participant WebApp as Frontend WebApp
  participant PayService as Payment Gateway
  participant Bank as Issuer Bank

  User ->> WebApp: Click 'Authorize $100'
  activate WebApp
  WebApp ->> PayService: POST /charges (amount, token)
  activate PayService
  PayService ->> Bank: DebitRequest(CardToken, $100)
  activate Bank
  Bank -->> PayService: 200 OK (AuthCode: TX994)
  deactivate Bank
  PayService -->> WebApp: ChargeSuccess(ReceiptID)
  deactivate PayService
  WebApp -->> User: Display Confirmation Screen
  deactivate WebApp"""
                },
                {
                    "type": "interactive",
                    "title": "Sequence Arrow Distinction Challenge",
                    "question": "In a UML Sequence diagram, what does a solid line with a stick/open arrowhead (as opposed to a filled triangular arrowhead) represent?",
                    "options": [
                        "A synchronous blocking method call where the sender waits for completion.",
                        "An asynchronous non-blocking message where the caller continues execution without waiting for a reply.",
                        "A return message containing serialized JSON.",
                        "The deletion of an object."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nA filled triangle arrow represents a **synchronous blocking call**, whereas an open stick arrow represents an **asynchronous non-blocking message** (such as publishing a Kafka event or invoking an async background thread)."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Sequence Notation Challenge",
                    "question": "The vertical dashed line in a Sequence Diagram representing the lifetime of an active participant is called a _____.\n\nAnswer: _____",
                    "answer": "Lifeline",
                    "alternatives": ["Lifeline", "lifeline", "Life-line"],
                    "explanation": "**Why Lifeline is Correct:**\nA **Lifeline** traces an object's existence downward through time during an interaction."
                }
            ]
        },
        {
            "title": "Module 2: UML State Machine Diagrams",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Many software entities (such as TCP connections, order checkouts, or flight control autopilots) are **State-Dependent**: their reaction to an incoming message depends strictly on their current state. Architects model this using **UML State Machine Diagrams** (Harel Statecharts)."
                },
                {
                    "type": "concept",
                    "title": "State Transition Mechanics",
                    "content": "A transition connects a source state to a target state, governed by the syntax:\n$$\\text{Event} \\ [\\text{Guard Condition}] \\ / \\ \\text{Action}$$\n\n- **State:** A condition or situation in the life of an object during which it satisfies some condition or waits for an event.\n- **Initial State:** A solid black circle (`[*]`).\n- **Final State:** A solid circle surrounded by an outer ring (bullseye).\n- **Guard:** A boolean expression enclosed in brackets `[balance >= amount]`. The transition fires only if the guard evaluates to true.\n- **Action:** An atomic execution performed during the transition `/ logAuditTrail()`."
                },
                {
                    "type": "visual",
                    "title": "E-Commerce Order State Machine",
                    "code": """stateDiagram-v2
  [*] --> CartCreated
  CartCreated --> PendingPayment : CheckoutClicked
  PendingPayment --> Paid : PaymentSuccess [balanceSufficient]
  PendingPayment --> Cancelled : PaymentDeclined / alertCustomer()
  Paid --> Shipped : WarehouseDispatched
  Shipped --> Delivered : CourierConfirmed
  Delivered --> [*]
  Cancelled --> [*]"""
                },
                {
                    "type": "interactive",
                    "title": "State Transition Guard Challenge",
                    "question": "In the state transition expression: `Withdraw [balance >= amount] / dispenseCash()`, what role does `[balance >= amount]` play?",
                    "options": [
                        "It is the trigger event that initiates the transition.",
                        "It is the Guard Condition: a boolean check that must evaluate to True for the transition to occur.",
                        "It is the asynchronous callback method.",
                        "It is the final state reached after cash is dispensed."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nIn UML state machine syntax, bracketed clauses `[...]` represent **Guard Conditions**. The transition will not fire if the guard evaluates to False, even if the trigger event occurs."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Statechart Creator Challenge",
                    "question": "The computer scientist who invented Statecharts (the foundation of UML State Machine diagrams) in 1987 is David _____.\n\nAnswer: _____",
                    "answer": "Harel",
                    "alternatives": ["Harel", "harel", "David Harel"],
                    "explanation": "**Why David Harel is Correct:**\n**David Harel** invented Statecharts to model the complex reactive avionics of the Israeli Lavi fighter jet, introducing hierarchy, concurrency, and broadcast communication to state machines."
                }
            ]
        },
        {
            "title": "Module 3: Finite State Machine Implementation Lab",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Let's implement a production-grade State Machine in Python using the **State Pattern** to manage order processing transitions while rejecting invalid state leaps."
                },
                {
                    "type": "code_lab",
                    "title": "Deterministic Order State Machine",
                    "instructions": "Implement `OrderStateMachine` with valid transitions: `CREATED -> PAID -> SHIPPED -> DELIVERED`, with support for `CANCEL` only from `CREATED` or `PAID`. Reject invalid transitions with `InvalidStateTransitionError`.",
                    "starter_code": """class InvalidStateTransitionError(Exception):
    pass

class OrderStateMachine:
    \"\"\"
    Enforces deterministic state transitions for an e-commerce order.
    Allowed transitions:
      - CREATED -> PAID or CANCELLED
      - PAID -> SHIPPED or CANCELLED
      - SHIPPED -> DELIVERED
      - DELIVERED: Terminal state (no transitions allowed)
      - CANCELLED: Terminal state (no transitions allowed)
    \"\"\"
    VALID_TRANSITIONS = {
        'CREATED': ['PAID', 'CANCELLED'],
        'PAID': ['SHIPPED', 'CANCELLED'],
        'SHIPPED': ['DELIVERED'],
        'DELIVERED': [],
        'CANCELLED': []
    }
    
    def __init__(self, order_id: str):
        self.order_id = order_id
        self.state = 'CREATED'
        self.history = ['CREATED']
        
    def transition_to(self, new_state: str):
        # TODO: Validate and execute state change
        pass
""",
                    "solution_code": """class InvalidStateTransitionError(Exception):
    pass

class OrderStateMachine:
    VALID_TRANSITIONS = {
        'CREATED': ['PAID', 'CANCELLED'],
        'PAID': ['SHIPPED', 'CANCELLED'],
        'SHIPPED': ['DELIVERED'],
        'DELIVERED': [],
        'CANCELLED': []
    }
    
    def __init__(self, order_id: str):
        self.order_id = order_id
        self.state = 'CREATED'
        self.history = ['CREATED']
        
    def transition_to(self, new_state: str):
        allowed = self.VALID_TRANSITIONS.get(self.state, [])
        if new_state not in allowed:
            raise InvalidStateTransitionError(
                f"Cannot transition order {self.order_id} from {self.state} to {new_state}"
            )
        self.state = new_state
        self.history.append(new_state)
        return self.state
""",
                    "test_code": """sm = OrderStateMachine("ORD-9901")
assert sm.state == 'CREATED'

sm.transition_to('PAID')
assert sm.state == 'PAID'

sm.transition_to('SHIPPED')
sm.transition_to('DELIVERED')
assert sm.state == 'DELIVERED'
assert sm.history == ['CREATED', 'PAID', 'SHIPPED', 'DELIVERED']

# Test invalid leap: DELIVERED -> CREATED
try:
    sm.transition_to('CREATED')
    assert False, "Should have raised InvalidStateTransitionError"
except InvalidStateTransitionError:
    pass

# Test cancellation from terminal state
try:
    sm.transition_to('CANCELLED')
    assert False, "Should have raised InvalidStateTransitionError"
except InvalidStateTransitionError:
    pass

print("State Machine implementation tests passed successfully!")
""",
                    "why_works": "**Why This Solution Works:**\nBy encoding allowed transitions into an immutable adjacency dictionary (`VALID_TRANSITIONS`), the state machine guarantees mathematical determinism. Invalid leaps (e.g., trying to cancel an order after it has been delivered) are intercepted and rejected before database corruption can occur.",
                    "alternatives": "**Alternative Approaches & Trade-offs:**\n- **GoF State Pattern:** Creating distinct classes for each state (`CreatedState`, `PaidState`). Ideal when states have radically different behaviors, but introduces class explosion for simple pipelines.\n- **PyTransitions Library:** Mature open-source Python library offering hierarchical states, callback hooks, and automatic graph rendering.",
                    "edge_cases": "**Edge Cases & Failure Modes:**\n- Unknown state string: Rejected immediately with `InvalidStateTransitionError`.\n- Terminal state: Transition list is empty, preventing any further state changes."
                }
            ]
        },
        {
            "title": "Module 4: Activity Diagrams & Concurrency Forks",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "While State Machines track the status of a single object over time, **UML Activity Diagrams** model business workflows and parallel processing across multiple components."
                },
                {
                    "type": "concept",
                    "title": "Activity Diagram Forks and Joins",
                    "content": "- **Action State:** A step in the execution of a workflow.\n- **Fork Node:** A solid horizontal or vertical bar with one incoming edge and multiple outgoing edges; splits a single thread of control into **concurrent parallel flows**.\n- **Join Node:** A solid bar with multiple incoming parallel edges and one outgoing edge; **synchronizes parallel flows**, waiting for all upstream paths to complete before proceeding.\n- **Swimlanes:** Vertical or horizontal partitions that assign responsibility for actions to specific organizational departments or system microservices."
                },
                {
                    "type": "visual",
                    "title": "Order Fulfillment Activity Flow with Fork and Join",
                    "code": """graph TD
  START(["Start Node"]) --> AUTH["Authorize Payment"]
  AUTH --> FORK{"FORK (Parallel Split)"}
  FORK --> PACK["Warehouse: Pick & Pack Items"]
  FORK --> INVOICE["Finance: Generate PDF Invoice"]
  PACK --> JOIN{"JOIN (Synchronize)"}
  INVOICE --> JOIN
  JOIN --> SHIP["Logistics: Dispatch Courier"]
  SHIP --> END_NODE(["End Node"])
  style START fill:#064e3b,stroke:#10b981
  style FORK fill:#1e1b4b,stroke:#6366f1
  style JOIN fill:#1e1b4b,stroke:#6366f1
  style END_NODE fill:#3f1a1a,stroke:#ef4444"""
                },
                {
                    "type": "interactive",
                    "title": "Concurrency Synchronization Challenge",
                    "question": "In a UML Activity diagram, what is the behavioral difference between a Decision Diamond and a Fork Bar?",
                    "options": [
                        "Decision diamonds represent database queries, whereas fork bars represent REST APIs.",
                        "A Decision Diamond evaluates a boolean condition to choose exactly ONE alternative outgoing path; a Fork Bar splits execution into multiple concurrent parallel threads that run simultaneously.",
                        "Decision diamonds can only be used in class diagrams.",
                        "There is no difference; they are interchangeable symbols."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nA **Decision Diamond** is mutually exclusive (branching: if/else); exactly one path is selected based on a guard. A **Fork Bar** initiates true concurrency (parallelism); all outgoing paths are activated simultaneously."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Workflow Partition Challenge",
                    "question": "In UML Activity diagrams, the visual columns that partition actions according to which department or microservice performs them are called _____.\n\nAnswer: _____",
                    "answer": "Swimlanes",
                    "alternatives": ["Swimlanes", "swimlanes", "Swim lanes", "swim lanes", "Partitions"],
                    "explanation": "**Why Swimlanes is Correct:**\n**Swimlanes** visually delineate architectural or organizational boundaries, making it instantly apparent who is responsible for each action in the end-to-end workflow."
                }
            ]
        }
    ]
}

print(f"Loaded {len(PART2_CASES)} cases for Part 2 (Cases 05-09).")

with open('/Users/aadarshamahato/Downloads/LEARNING_PLATFORM/se_story_lab/cases_part2.json', 'w', encoding='utf-8') as f:
    json.dump(PART2_CASES, f, indent=4)
