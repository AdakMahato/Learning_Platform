import json
import os

PART4_CASES = {}

# CASE 15: The Dynamic Behavior (Behavioral Design Patterns)
PART4_CASES["15"] = {
    "title": "Case 15: The Dynamic Behavior",
    "episodes": [
        {
            "title": "Module 1: The Observer Pattern & Reactive Event Buses",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Behavioral patterns are concerned with algorithms and the assignment of responsibilities between objects. They characterize complex control flow that is difficult to follow at runtime. The most ubiquitous behavioral pattern is **Observer** (the foundation of event-driven GUIs, RxJS, and Model-View-Controller)."
                },
                {
                    "type": "objective",
                    "title": "Module Objective",
                    "content": "Master Behavioral Design Patterns: Observer, Strategy, and Command; implement dynamic event broadcasting, hot-swappable algorithms, and transactional undo/redo."
                },
                {
                    "type": "concept",
                    "title": "Observer Pattern Architecture",
                    "content": "- **Intent:** Define a one-to-many dependency between objects so that when one object (Subject) changes state, all its dependents (Observers) are notified and updated automatically.\n- **Subject (Publisher):** Maintains a collection of observers; exposes `attach(observer)`, `detach(observer)`, and `notify()`.\n- **Observer (Subscriber):** Implements an `update(state)` interface.\n- **Push vs. Pull:**\n  - *Push Model:* Subject sends detailed state data as arguments in `notify(event_data)`.\n  - *Pull Model:* Subject simply signals that something changed; observers query the subject for the specific state attributes they care about."
                },
                {
                    "type": "visual",
                    "title": "Observer Event Broadcast Topology",
                    "code": """classDiagram
  class Subject {
    -observers : List~Observer~
    +attach(o : Observer)
    +detach(o : Observer)
    +notify(eventData)
  }
  class Observer {
    <<interface>>
    +update(eventData)
  }
  class EmailNotifier {
    +update(eventData)
  }
  class AuditLogger {
    +update(eventData)
  }

  Subject o--> "0..*" Observer : Notifies
  Observer <|.. EmailNotifier : Implements
  Observer <|.. AuditLogger : Implements"""
                },
                {
                    "type": "interactive",
                    "title": "Observer Decoupling Challenge",
                    "question": "What is the primary architectural advantage of using the Observer pattern over hardcoded direct method calls?",
                    "options": [
                        "It eliminates the need for unit testing.",
                        "The Subject knows nothing about concrete observer implementations; new observers can be added or removed at runtime without altering the Subject's code.",
                        "It makes all function execution synchronous.",
                        "It reduces memory consumption to zero."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nThe Observer pattern adheres to the Open/Closed Principle: the Subject depends only on an abstract `Observer` interface. You can attach 50 new notification listeners (SMS, Slack, Webhook, Analytics) at runtime without changing or recompiling the Subject."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Pattern Synonym Challenge",
                    "question": "In architectural distributed messaging, the Observer pattern is widely known as the Publish-_____ pattern.\n\nAnswer: _____",
                    "answer": "Subscribe",
                    "alternatives": ["Subscribe", "subscribe", "PubSub", "Pub-Sub"],
                    "explanation": "**Why Subscribe is Correct:**\n**Publish-Subscribe (Pub/Sub)** generalizes the Observer pattern across network boundaries using topics and message queues."
                }
            ]
        },
        {
            "title": "Module 2: The Strategy Pattern: Hot-Swappable Algorithms",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "When business rules require multiple variations of an algorithm (e.g. navigation routing for Walking vs Driving vs Biking, or shipping cost calculation for FedEx vs UPS vs DHL), giant `if/elif/else` blocks create unmaintainable code. The **Strategy Pattern** encapsulates each algorithm into its own class."
                },
                {
                    "type": "concept",
                    "title": "Strategy Pattern Mechanics",
                    "content": "- **Intent:** Define a family of algorithms, encapsulate each one, and make them interchangeable. Strategy lets the algorithm vary independently from clients that use it.\n- **Context:** Maintains a reference to a Strategy object and delegates computation to it.\n- **Strategy Interface:** Common interface implemented by all concrete algorithm variants.\n- **Runtime Swapping:** The Context can switch strategies on the fly (e.g. user toggles GPS route mode from 'Fastest Route' to 'Avoid Tolls')."
                },
                {
                    "type": "visual",
                    "title": "Strategy Pattern Routing Engine",
                    "code": """graph TD
  subgraph NavigatorContext ["Navigator Context"]
    NAV["Navigator.buildRoute(origin, destination)"]
  end
  subgraph StrategyInterface ["RoutingStrategy Interface"]
    INT["RoutingStrategy: calculateRoute(A, B)"]
  end
  subgraph ConcreteAlgorithms ["Concrete Strategy Implementations"]
    ROAD["FastestHighwayStrategy (Dijkstra)"]
    SCENIC["ScenicRouteStrategy (A* Elevation)"]
    PUBLIC["TransitStrategy (Timetable Graph)"]
  end
  NAV --> INT
  ROAD -.->|"Implements"| INT
  SCENIC -.->|"Implements"| INT
  PUBLIC -.->|"Implements"| INT
  style NavigatorContext fill:#0f172a,stroke:#3b82f6
  style StrategyInterface fill:#1e1b4b,stroke:#6366f1
  style ConcreteAlgorithms fill:#064e3b,stroke:#10b981"""
                },
                {
                    "type": "interactive",
                    "title": "Strategy vs. Inheritance Challenge",
                    "question": "A developer wants to support 5 compression formats (ZIP, GZIP, TAR, BZIP2, 7Z). Why is the Strategy pattern cleaner than creating 5 subclasses of `FileArchiver`?",
                    "options": [
                        "Subclassing couples compression to file archiving; Strategy lets archivers dynamically switch compression algorithms at runtime without creating new classes.",
                        "Subclasses cannot execute in parallel in Python.",
                        "Strategy automatically encrypts the files.",
                        "Subclasses cannot use third-party libraries."
                    ],
                    "answer": 0,
                    "explanation": "**Why this is Correct:**\nBy delegating compression to an injected `CompressionStrategy`, the archiver is decoupled from concrete compression formats. A single `FileArchiver` can compress to ZIP, swap strategy at runtime, and compress to TAR without subclassing."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Strategy Role Challenge",
                    "question": "In the Strategy pattern, the class that holds a reference to a strategy object and delegates algorithmic execution to it is called the _____.\n\nAnswer: _____",
                    "answer": "Context",
                    "alternatives": ["Context", "context"],
                    "explanation": "**Why Context is Correct:**\nThe **Context** configures and holds the active strategy, exposing high-level domain operations to client code."
                }
            ]
        },
        {
            "title": "Module 3: The Command Pattern & Transactional Undo/Redo",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "In traditional procedural programming, clicking a button directly calls a function. The **Command Pattern** turns a request into a standalone object containing all information needed to execute the action, enabling queuing, logging, macro execution, and **undo/redo**."
                },
                {
                    "type": "concept",
                    "title": "Command Pattern Mechanics",
                    "content": "- **Command Interface:** Declares `execute()` and optional `undo()`.\n- **Receiver:** The business object that actually performs the work (e.g. `Document`).\n- **Invoker:** Triggers the command (e.g. a GUI button, menu shortcut, or queue processor).\n- **History Stack:** Pushing executed command objects onto an undo stack allows full reversal by calling `command.undo()` in LIFO order."
                },
                {
                    "type": "code_lab",
                    "title": "Command Undo/Redo Engine Lab",
                    "instructions": "Implement a transactional `TextEditor` with `InsertCommand` supporting `execute()` and `undo()`, managed by a `CommandManager` that maintains undo and redo stacks.",
                    "starter_code": """class TextEditor:
    def __init__(self):
        self.content = ""
        
    def write(self, text: str):
        self.content += text
        
    def erase_last(self, length: int):
        self.content = self.content[:-length]

class InsertCommand:
    def __init__(self, editor: TextEditor, text_to_insert: str):
        self.editor = editor
        self.text = text_to_insert
        
    def execute(self):
        # TODO: Execute insertion
        pass
        
    def undo(self):
        # TODO: Reverse insertion
        pass

class CommandManager:
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []
        
    def execute_command(self, cmd):
        # TODO: Execute and manage history
        pass
        
    def undo(self):
        # TODO: Pop and undo
        pass
""",
                    "solution_code": """class TextEditor:
    def __init__(self):
        self.content = ""
        
    def write(self, text: str):
        self.content += text
        
    def erase_last(self, length: int):
        self.content = self.content[:-length]

class InsertCommand:
    def __init__(self, editor: TextEditor, text_to_insert: str):
        self.editor = editor
        self.text = text_to_insert
        
    def execute(self):
        self.editor.write(self.text)
        
    def undo(self):
        self.editor.erase_last(len(self.text))

class CommandManager:
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []
        
    def execute_command(self, cmd):
        cmd.execute()
        self.undo_stack.append(cmd)
        self.redo_stack.clear() # Clear redo history on new action
        
    def undo(self):
        if self.undo_stack:
            cmd = self.undo_stack.pop()
            cmd.undo()
            self.redo_stack.append(cmd)
            return True
        return False
""",
                    "test_code": """editor = TextEditor()
manager = CommandManager()

cmd1 = InsertCommand(editor, "Hello ")
manager.execute_command(cmd1)
assert editor.content == "Hello "

cmd2 = InsertCommand(editor, "World!")
manager.execute_command(cmd2)
assert editor.content == "Hello World!"

# Test Undo
manager.undo()
assert editor.content == "Hello "

manager.undo()
assert editor.content == ""

# Undo on empty stack
assert manager.undo() is False
print("Command Undo/Redo tests passed successfully!")
""",
                    "why_works": "**Why This Solution Works:**\nBy encapsulating the insertion as an object that knows both how to perform (`write`) and invert (`erase_last`) its operation, `CommandManager` can manage multi-level undo without knowing anything about text editing internals.",
                    "alternatives": "**Alternative Approaches & Trade-offs:**\n- **Memento Pattern:** Instead of storing inverse operations, Memento saves a complete snapshot of the editor state. Simpler to implement for complex states, but consumes much more memory.\n- **Event Sourcing:** Enterprise pattern where all state changes are stored as an append-only event stream; state is reconstructed by replaying events.",
                    "edge_cases": "**Edge Cases & Failure Modes:**\n- `undo()` called on empty stack: Safely returns `False` without IndexError.\n- Executing a new command after undos: Properly clears `redo_stack` to prevent branching history anomalies."
                }
            ]
        },
        {
            "title": "Module 4: Behavioral Patterns Synthesis",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Behavioral patterns solve distinct architectural coordination challenges. Knowing which pattern fits which scenario prevents convoluted designs."
                },
                {
                    "type": "concept",
                    "title": "Behavioral Pattern Selector Matrix",
                    "content": "| Problem | Best Pattern | Why |\n|---|---|---|\n| One object's state change must notify multiple unknown listeners | **Observer** | Decouples publisher from subscribers |\n| Select from several interchangeable algorithms at runtime | **Strategy** | Encapsulates algorithms into swappable classes |\n| Need undo/redo, command queues, or transaction logging | **Command** | Reifies actions into first-class objects |\n| Object's behavior changes dramatically based on internal state | **State** | Eliminates giant switch statements on status codes |\n| Traverse a complex collection without exposing its internal representation | **Iterator** | Standardizes sequential access across trees/lists |"
                },
                {
                    "type": "interactive",
                    "title": "Pattern Disambiguation Challenge",
                    "question": "A graphical design tool needs to support 'Undo' and 'Redo' for operations like Move, Resize, and Rotate. Which GoF pattern should be the foundation?",
                    "options": [
                        "Observer Pattern.",
                        "Command Pattern (encapsulates requests as objects with execute and un-execute methods).",
                        "Singleton Pattern.",
                        "Decorator Pattern."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nThe **Command Pattern** is the universal design pattern for undo/redo mechanisms. Every user action is instantiated as a Command object with `execute()` and `undo()` methods stored in an execution stack."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "GoF Pattern Count Challenge",
                    "question": "In the original Gang of Four book, the total number of documented behavioral design patterns was _____.\n\nAnswer: _____",
                    "answer": "11",
                    "alternatives": ["11", "eleven", "Eleven"],
                    "explanation": "**Why 11 is Correct:**\nThe GoF book catalogs **11 Behavioral patterns** (out of 23 total): Chain of Responsibility, Command, Interpreter, Iterator, Mediator, Memento, Observer, State, Strategy, Template Method, and Visitor."
                }
            ]
        }
    ]
}

# CASE 16: The Quality Pyramid (Testing Fundamentals)
PART4_CASES["16"] = {
    "title": "Case 16: The Quality Pyramid",
    "episodes": [
        {
            "title": "Module 1: Verification, Validation & The Seven Principles",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Edsger W. Dijkstra famously stated in 1969: *'Program testing can be used to show the presence of bugs, but never to show their absence!'* Software testing is an empirical verification discipline governed by rigorous testing axioms."
                },
                {
                    "type": "objective",
                    "title": "Module Objective",
                    "content": "Master the ISTQB 7 Fundamental Principles of Software Testing, the Test Pyramid architecture, and the distinction between Unit, Integration, and End-to-End (E2E) testing."
                },
                {
                    "type": "concept",
                    "title": "The ISTQB 7 Principles of Testing",
                    "content": "1. **Testing shows the presence of defects, not their absence:** Passing 10,000 tests does not prove zero defects exist.\n2. **Exhaustive testing is impossible:** Testing all possible input combinations ($2^{32} \\times 2^{32}$) would take billions of years; use equivalence partitioning instead.\n3. **Early testing saves time and money:** Shift testing left to catch defects early.\n4. **Defects cluster together (Pareto 80/20 Rule):** 80% of bugs are concentrated in 20% of modules.\n5. **Beware of the Pesticide Paradox:** Running the exact same test cases repeatedly stops finding new bugs; test suites must be continuously evolved.\n6. **Testing is context-dependent:** Testing an air traffic control system is radically different from testing a mobile game.\n7. **Absence-of-errors is a fallacy:** Building a defect-free system is useless if it fails to fulfill user business needs."
                },
                {
                    "type": "visual",
                    "title": "The Pesticide Paradox Breakdown",
                    "code": """graph TD
  subgraph Cycle ["The Pesticide Paradox Cycle"]
    T1["Write Static Regression Test Suite"] --> T2["Developers Patch Detected Bugs"]
    T2 --> T3["Code Evolves & Creates New Bug Classes"]
    T3 --> T4["Old Tests Run Green (100% Pass) ✅"]
    T4 --> T5["False Sense of Security: New Bugs Escape to Production! ⚠️"]
    T5 -.->|"Remedy: Continuously Diversify Tests"| T1
  end
  style Cycle fill:#1e1b4b,stroke:#6366f1
  style T5 fill:#3f1a1a,stroke:#ef4444"""
                },
                {
                    "type": "interactive",
                    "title": "Testing Axiom Challenge",
                    "question": "A QA team has run the exact same 500 regression test cases on every build for 6 months. For the last 4 months, zero defects were detected, yet customer bug reports in production are increasing. What ISTQB principle explains this?",
                    "options": [
                        "Exhaustive testing is impossible.",
                        "The Pesticide Paradox (tests that are never changed or diversified cease to detect new defect varieties).",
                        "Early testing saves time.",
                        "Testing is context dependent."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nThe **Pesticide Paradox** observes that, just like insects develop immunity to unchanged pesticides, software and developers evolve to pass static regression suites. If test suites are not regularly updated with new edge cases and exploratory scenarios, new bugs slip through."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Dijkstra Quote Challenge",
                    "question": "Dijkstra stated that software testing can only show the _____ of defects, but never their absence.\n\nAnswer: _____",
                    "answer": "Presence",
                    "alternatives": ["Presence", "presence"],
                    "explanation": "**Why Presence is Correct:**\nTesting can prove that bugs **exist** by demonstrating a failure, but no amount of testing can mathematically guarantee that zero bugs remain."
                }
            ]
        },
        {
            "title": "Module 2: Mike Cohn's Test Pyramid",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "In *Succeeding with Agile*, Mike Cohn introduced the **Test Automation Pyramid**. It provides a structural blueprint for a fast, resilient, and cost-effective automated testing portfolio."
                },
                {
                    "type": "concept",
                    "title": "The Three Tiers of the Test Pyramid",
                    "content": "1. **Base Tier (Unit Tests — 70%):**\n   - Test isolated classes or functions in memory with dependencies mocked out.\n   - *Speed:* Milliseconds per test (entire suite of 5,000 runs in 10 seconds).\n   - *Cost:* Extremely cheap to write and maintain.\n2. **Middle Tier (Integration Tests — 20%):**\n   - Test interaction between components (e.g. Service interacting with real Postgres DB via Docker Testcontainers).\n   - *Speed:* Seconds per test.\n3. **Top Tier (End-to-End / UI Tests — 10%):**\n   - Spin up entire system and automate user interactions via Selenium or Playwright.\n   - *Speed:* Minutes per test; prone to flaky false positives due to network or UI timing glitches."
                },
                {
                    "type": "visual",
                    "title": "The Test Pyramid vs. The Ice Cream Cone Antipattern",
                    "code": """graph TD
  subgraph IdealPyramid ["IDEAL: The Test Pyramid (Fast & Robust)"]
    UI["10% End-to-End (Playwright / Selenium)"]
    INT["20% Integration (Database / API Contracts)"]
    UNIT["70% Unit Tests (Fast In-Memory Assertions)"]
    UI --- INT --- UNIT
  end
  subgraph AntiPattern ["ANTIPATTERN: The Ice Cream Cone (Flaky & Slow)"]
    MANUAL["70% Flaky E2E & Manual Regression (Hours to Run)"]
    INT_A["20% Integration Tests"]
    UNIT_A["10% Sparse Unit Tests"]
    MANUAL --- INT_A --- UNIT_A
  end
  style IdealPyramid fill:#064e3b,stroke:#10b981
  style AntiPattern fill:#3f1a1a,stroke:#ef4444"""
                },
                {
                    "type": "interactive",
                    "title": "Pyramid Architecture Challenge",
                    "question": "A company has an 'Ice Cream Cone' test suite: 1,200 slow Selenium browser tests that take 4 hours to run on every commit and fail 15% of the time due to animation timing issues, with almost no unit tests. What is the primary remedy?",
                    "options": [
                        "Buy faster CI/CD servers to run the Selenium tests faster.",
                        "Invert the pyramid: push test assertions down to fast, isolated unit tests, leaving only critical user smoke journeys for end-to-end automation.",
                        "Stop testing completely.",
                        "Hire more manual testers."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nThe **Ice Cream Cone** antipattern creates slow feedback loops and developer cynicism due to test flakiness. The remedy is pushing business logic verification down into sub-millisecond unit tests, reserving high-level E2E tests strictly for critical end-to-end user smoke workflows."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Antipattern Shape Challenge",
                    "question": "The software testing antipattern that inverts the test pyramid with massive slow UI tests and minimal unit tests is called the Ice Cream _____ antipattern.\n\nAnswer: _____",
                    "answer": "Cone",
                    "alternatives": ["Cone", "cone", "Ice Cream Cone"],
                    "explanation": "**Why Cone is Correct:**\nThe **Ice Cream Cone** antipattern is a primary bottleneck in enterprise delivery pipelines."
                }
            ]
        },
        {
            "title": "Module 3: Test Automation Portfolio ROI Lab",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Let's build a test portfolio analyzer that calculates the execution time and stability of test suites across different pyramid distribution ratios."
                },
                {
                    "type": "code_lab",
                    "title": "Test Suite Execution Time & Flakiness Simulator",
                    "instructions": "Implement `simulate_test_portfolio(unit_count, int_count, e2e_count)` using realistic benchmark execution times (Unit: 0.005s, Integration: 0.2s, E2E: 5.0s) and failure risk factors.",
                    "starter_code": """def simulate_test_portfolio(unit_count: int, int_count: int, e2e_count: int) -> dict:
    \"\"\"
    Calculate test suite execution metrics.
    Execution benchmarks:
      - Unit test: 0.005 seconds, flake probability: 0.0001
      - Integration test: 0.200 seconds, flake probability: 0.005
      - E2E test: 5.000 seconds, flake probability: 0.05
      
    Returns dict:
      - 'total_tests': int
      - 'total_runtime_seconds': float (rounded to 2 decimals)
      - 'pyramid_health': 'Healthy Pyramid' (unit >= 60% and e2e <= 15%), 'Inverted Cone' (e2e >= 40%), or 'Unbalanced'
    \"\"\"
    # TODO: Implement metrics calculation
    pass
""",
                    "solution_code": """def simulate_test_portfolio(unit_count: int, int_count: int, e2e_count: int) -> dict:
    total = unit_count + int_count + e2e_count
    if total == 0:
        return {'total_tests': 0, 'total_runtime_seconds': 0.0, 'pyramid_health': 'Healthy Pyramid'}
        
    runtime = (unit_count * 0.005) + (int_count * 0.200) + (e2e_count * 5.000)
    
    unit_pct = (unit_count / total) * 100.0
    e2e_pct = (e2e_count / total) * 100.0
    
    if unit_pct >= 60.0 and e2e_pct <= 15.0:
        health = 'Healthy Pyramid'
    elif e2e_pct >= 40.0:
        health = 'Inverted Cone'
    else:
        health = 'Unbalanced'
        
    return {
        'total_tests': total,
        'total_runtime_seconds': round(runtime, 2),
        'pyramid_health': health
    }
""",
                    "test_code": """# Healthy pyramid: 700 unit, 200 int, 100 e2e
res1 = simulate_test_portfolio(700, 200, 100)
assert res1['total_tests'] == 1000
assert res1['total_runtime_seconds'] == 543.5 # 3.5 + 40 + 500
assert res1['pyramid_health'] == 'Healthy Pyramid'

# Inverted cone: 50 unit, 50 int, 400 e2e
res2 = simulate_test_portfolio(50, 50, 400)
assert res2['pyramid_health'] == 'Inverted Cone'
assert res2['total_runtime_seconds'] == 2010.25
print("Test Portfolio Simulator tests passed successfully!")
""",
                    "why_works": "**Why This Solution Works:**\nEven though E2E tests constitute only 10% of tests in a healthy pyramid, they account for over 90% of total runtime ($500s$ out of $543.5s$). In an inverted cone, runtime balloons to over 33 minutes ($2010s$), destroying rapid CI feedback loops.",
                    "alternatives": "**Alternative Approaches & Trade-offs:**\n- **Parallel Sharding:** Running E2E tests across 20 parallel cloud containers. Cuts wall-clock time, but increases cloud computing costs.\n- **Test Impact Analysis (TIA):** Using code coverage graphs to execute only the subset of tests affected by the latest Git diff.",
                    "edge_cases": "**Edge Cases & Failure Modes:**\n- Zero tests: Handled safely without division by zero.\n- Extreme numbers ($10^6$ tests): Efficient floating point arithmetic without performance degradation."
                }
            ]
        },
        {
            "title": "Module 4: Defect Severity vs. Priority",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "In bug tracking systems (Jira, Bugzilla), engineering leads must triage issues using two orthogonal axes: **Severity** and **Priority**."
                },
                {
                    "type": "concept",
                    "title": "Severity vs. Priority Matrix",
                    "content": "- **Severity:** The technical impact of a defect on system functionality (Critical, Major, Minor, Trivial).\n- **Priority:** The business urgency of fixing the defect (High, Medium, Low).\n\n### The Surprising Combinations:\n- **High Severity, Low Priority:** A catastrophic buffer overflow that crashes the server with data loss, but occurs only on obsolete 32-bit Solaris systems that no paying customer uses.\n- **Low Severity, High Priority:** The company name or logo is misspelled ('Microsft') on the homepage. Technically trivial (1 character HTML fix), but an urgent PR disaster that must be hotfixed immediately."
                },
                {
                    "type": "interactive",
                    "title": "Triage Calibration Challenge",
                    "question": "A typo exists in the primary logo image on the company's publicly traded homepage displaying 'Googel' instead of 'Google'. How should this bug be triaged?",
                    "options": [
                        "High Severity, High Priority.",
                        "Low Severity (pure cosmetic/trivial technical impact), High Priority (urgent public brand embarrassment).",
                        "High Severity, Low Priority.",
                        "Low Severity, Low Priority."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\n**Severity** measures technical operational destruction (the site does not crash; transactions still process: Low Severity). **Priority** measures business urgency (severe reputational damage to a public corporation: High Priority)."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Triage Dimension Challenge",
                    "question": "The metric representing the technical degree of system impact (as opposed to business urgency) is defect _____.\n\nAnswer: _____",
                    "answer": "Severity",
                    "alternatives": ["Severity", "severity"],
                    "explanation": "**Why Severity is Correct:**\n**Severity** assesses technical malfunction, while **Priority** dictates scheduled triage order."
                }
            ]
        }
    ]
}

# CASE 17: The Dark Box (Black-Box Testing)
PART4_CASES["17"] = {
    "title": "Case 17: The Dark Box",
    "episodes": [
        {
            "title": "Module 1: Equivalence Class Partitioning (ECP)",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "**Black-Box Testing** treats software as an opaque container: tests are derived strictly from specifications without inspecting internal source code. The fundamental black-box efficiency technique is **Equivalence Class Partitioning (ECP)**."
                },
                {
                    "type": "objective",
                    "title": "Module Objective",
                    "content": "Master Black-Box test design techniques: Equivalence Partitioning, Boundary Value Analysis (BVA), and Decision Tables to uncover boundary faults."
                },
                {
                    "type": "concept",
                    "title": "Equivalence Partitioning Principles",
                    "content": "- **Concept:** Divide the infinite domain of input data into finite partitions such that all values within a partition are treated equivalently by the software.\n- **Axiom:** If one test case in an equivalence partition detects a defect, all other values in that partition will likely detect the same defect. Conversely, if one value passes, all others will likely pass.\n- **Partitions:**\n  - *Valid Equivalence Classes:* Values that conform to the specification.\n  - *Invalid Equivalence Classes:* Values that violate constraints (out-of-range, null, wrong data types)."
                },
                {
                    "type": "visual",
                    "title": "Equivalence Partitioning Topology for Age Input [18 to 65]",
                    "code": """graph LR
  subgraph InvalidUnder ["Invalid Class 1 (Underage)"]
    U["Age < 18 (e.g. -5, 0, 17) -> Error Rejected ❌"]
  end
  subgraph ValidRange ["Valid Equivalence Class"]
    V["18 <= Age <= 65 (e.g. 35) -> Accepted ✅"]
  end
  subgraph InvalidOver ["Invalid Class 2 (Overage)"]
    O["Age > 65 (e.g. 66, 120) -> Error Rejected ❌"]
  end
  style InvalidUnder fill:#3f1a1a,stroke:#ef4444
  style ValidRange fill:#064e3b,stroke:#10b981
  style InvalidOver fill:#3f1a1a,stroke:#ef4444"""
                },
                {
                    "type": "interactive",
                    "title": "Equivalence Partitioning Challenge",
                    "question": "A form accepts an integer representing flight seat quantity from 1 to 9. According to Equivalence Partitioning, what is the minimum number of test cases required to test valid and invalid ranges?",
                    "options": [
                        "9 test cases (test every single valid number).",
                        "3 test cases: one invalid low (e.g. 0), one valid (e.g. 5), and one invalid high (e.g. 10).",
                        "1,000 randomized inputs.",
                        "1 test case."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nECP divides the domain into 3 partitions: $(-\\infty, 0]$ (Invalid Low), $[1, 9]$ (Valid), and $[10, \\infty)$ (Invalid High). Testing one representative value from each partition covers all equivalence classes."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Technique Acronym Challenge",
                    "question": "The abbreviation for Equivalence Class Partitioning is _____.\n\nAnswer: _____",
                    "answer": "ECP",
                    "alternatives": ["ECP", "ecp", "Equivalence Partitioning"],
                    "explanation": "**Why ECP is Correct:**\n**ECP** allows engineers to test infinite input spaces with a minimal, mathematically optimal set of test cases."
                }
            ]
        },
        {
            "title": "Module 2: Boundary Value Analysis (BVA)",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Defects cluster disproportionately at boundaries. Programmers routinely make off-by-one errors: using `<` instead of `<=`, or starting loops at index 1 instead of 0. **Boundary Value Analysis (BVA)** specifically targets these transition edges."
                },
                {
                    "type": "concept",
                    "title": "2-Value and 3-Value BVA",
                    "content": "For a valid input range $[A, B]$:\n\n### 2-Value BVA (Standard):\nTest boundary and its immediate neighbor outside:\n- Minimum boundary: $A$ (valid), $A - 1$ (invalid)\n- Maximum boundary: $B$ (valid), $B + 1$ (invalid)\n- Total test cases: $A-1, A, B, B+1$\n\n### 3-Value BVA (Robustness):\nTest boundary, one below, and one above:\n- $A-1, A, A+1$ and $B-1, B, B+1$"
                },
                {
                    "type": "visual",
                    "title": "Boundary Value Test Points for Range [1, 100]",
                    "code": """graph LR
  subgraph LeftEdge ["Lower Boundary: 1"]
    L_OUT["0 (Invalid)"]
    L_MIN["1 (Min Valid)"]
    L_IN["2 (Valid)"]
  end
  subgraph RightEdge ["Upper Boundary: 100"]
    R_IN["99 (Valid)"]
    R_MAX["100 (Max Valid)"]
    R_OUT["101 (Invalid)"]
  end
  LeftEdge --- RightEdge
  style L_OUT fill:#3f1a1a,stroke:#ef4444
  style L_MIN fill:#064e3b,stroke:#10b981
  style R_MAX fill:#064e3b,stroke:#10b981
  style R_OUT fill:#3f1a1a,stroke:#ef4444"""
                },
                {
                    "type": "interactive",
                    "title": "BVA Test Selection Challenge",
                    "question": "A banking password input requires between 8 and 16 characters. Using 2-value Boundary Value Analysis, which string lengths must be tested?",
                    "options": [
                        "8, 9, 10, 11, 12, 13, 14, 15, 16.",
                        "7, 8, 16, 17.",
                        "0 and 1,000.",
                        "1, 8, 16, 32."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nFor range $[8, 16]$, 2-value BVA tests the lower boundary edge ($8 - 1 = 7$, and $8$) and the upper boundary edge ($16$, and $16 + 1 = 17$)."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Common Bug Nickname Challenge",
                    "question": "The notorious programming boundary error where a programmer confuses '<' with '<=' is known as an off-by-_____ error.\n\nAnswer: _____",
                    "answer": "One",
                    "alternatives": ["One", "one", "1", "OBOE"],
                    "explanation": "**Why One is Correct:**\n**Off-by-one errors (OBOE)** are the most common source of boundary calculation flaws in software engineering."
                }
            ]
        },
        {
            "title": "Module 3: Decision Table Testing Lab",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "When business logic depends on combinations of multiple inputs and conditions, simple range checking is insufficient. Architects use **Decision Tables** to ensure all logic branches are verified."
                },
                {
                    "type": "code_lab",
                    "title": "Decision Table Rule Engine",
                    "instructions": "Implement `evaluate_credit_card_application(age, income, credit_score)` according to business rules: Approve if `income >= 50000` and `credit_score >= 700`; Manual Review if `income >= 50000` and `600 <= credit_score < 700`; otherwise Decline. Reject applicants with `age < 18` immediately.",
                    "starter_code": """def evaluate_credit_card_application(age: int, annual_income: float, credit_score: int) -> str:
    \"\"\"
    Decision Table Logic:
      - age < 18 -> 'DECLINE_UNDERAGE'
      - income >= 50000 and credit_score >= 700 -> 'APPROVED'
      - income >= 50000 and 600 <= credit_score < 700 -> 'MANUAL_REVIEW'
      - all other cases -> 'DECLINED'
    \"\"\"
    # TODO: Implement decision rules
    pass
""",
                    "solution_code": """def evaluate_credit_card_application(age: int, annual_income: float, credit_score: int) -> str:
    if age < 18:
        return 'DECLINE_UNDERAGE'
        
    if annual_income >= 50000.0:
        if credit_score >= 700:
            return 'APPROVED'
        elif credit_score >= 600:
            return 'MANUAL_REVIEW'
            
    return 'DECLINED'
""",
                    "test_code": """# Underage
assert evaluate_credit_card_application(17, 100000.0, 800) == 'DECLINE_UNDERAGE'

# Approved
assert evaluate_credit_card_application(25, 65000.0, 720) == 'APPROVED'

# Boundary: exactly 50000 income, 700 credit score
assert evaluate_credit_card_application(18, 50000.0, 700) == 'APPROVED'

# Manual review
assert evaluate_credit_card_application(30, 55000.0, 650) == 'MANUAL_REVIEW'

# Low income
assert evaluate_credit_card_application(40, 35000.0, 750) == 'DECLINED'
print("Decision Table tests passed successfully!")
""",
                    "why_works": "**Why This Solution Works:**\nThe implementation systematically encodes all combinations of boolean conditions derived from the truth table, ensuring mutually exclusive, non-overlapping outcomes.",
                    "alternatives": "**Alternative Approaches & Trade-offs:**\n- **Rule Engine (Drools / PyKnow):** For enterprise applications with hundreds of dynamic business rules altered weekly by non-programmers.\n- **Cause-Effect Graphing:** Formal technique translating requirements into boolean graphs to derive decision tables.",
                    "edge_cases": "**Edge Cases & Failure Modes:**\n- Age boundary: Age 17 is declined; Age 18 proceeds.\n- Income boundary: Exactly 50,000 qualifies for approved/manual review tiers."
                }
            ]
        },
        {
            "title": "Module 4: Black-Box vs. White-Box Synthesis",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Professional testing strategies never rely on black-box or white-box techniques alone; they harmonize both."
                },
                {
                    "type": "concept",
                    "title": "Black-Box vs. White-Box Comparison",
                    "content": "| Characteristic | Black-Box Testing | White-Box Testing |\n|---|---|---|\n| **Knowledge Required** | Specifications & user requirements | Internal source code, logic, data structures |\n| **Tester Persona** | QA Engineers, Product Owners, End Users | Software Engineers, Compiler Tooling |\n| **Primary Goal** | Validate system against requirements | Verify internal paths, loops, and conditions |\n| **Techniques** | ECP, BVA, Decision Tables, State Transitions | Statement, Branch, MC/DC, Cyclomatic Complexity |\n| **Blind Spots** | Cannot detect hidden backdoors or unused dead code | Misses missing requirements (cannot test what isn't coded) |"
                },
                {
                    "type": "interactive",
                    "title": "Testing Blind Spot Challenge",
                    "question": "What is the critical blind spot of pure White-Box testing that Black-Box testing easily detects?",
                    "options": [
                        "White-box testing cannot measure execution time.",
                        "White-box testing cannot detect missing requirements: if a developer completely forgot to implement a required feature, there is no code to inspect or achieve coverage on.",
                        "White-box testing requires Python.",
                        "White-box testing cannot be automated in CI/CD."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nIf an entire requirement was omitted during coding (e.g., forgetting to check session timeouts), a white-box test suite can achieve 100% statement and branch coverage on existing code while remaining completely oblivious to the missing capability."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Hybrid Testing Term Challenge",
                    "question": "The testing methodology that combines knowledge of internal data structures with user-facing specification testing is called _____ box testing.\n\nAnswer: _____",
                    "answer": "Gray",
                    "alternatives": ["Gray", "gray", "Grey", "grey", "Gray-Box"],
                    "explanation": "**Why Gray is Correct:**\n**Gray-Box testing** uses high-level knowledge of databases and architecture to guide black-box functional testing."
                }
            ]
        }
    ]
}

# CASE 18: The Glass Box (White-Box Testing)
PART4_CASES["18"] = {
    "title": "Case 18: The Glass Box",
    "episodes": [
        {
            "title": "Module 1: Control Flow Graphs (CFG) & Cyclomatic Complexity",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "**White-Box Testing** (also called Glass-Box or Clear-Box testing) inspects internal code structures. In 1976, Thomas J. McCabe introduced **Cyclomatic Complexity**, a mathematical metric that measures the number of linearly independent paths through program source code."
                },
                {
                    "type": "objective",
                    "title": "Module Objective",
                    "content": "Construct Control Flow Graphs (CFGs), calculate McCabe's Cyclomatic Complexity $V(G)$, and master Statement, Branch, Condition, and MC/DC coverage."
                },
                {
                    "type": "concept",
                    "title": "McCabe's Cyclomatic Complexity Formulas",
                    "content": "Cyclomatic Complexity $V(G)$ can be calculated in three equivalent ways:\n\n1. **Graph Theory Formula:**\n   $$V(G) = E - N + 2P$$\n   Where $E = \\text{Edges}$, $N = \\text{Nodes}$, and $P = \\text{Connected Components}$ (typically $P=1$).\n2. **Predicate Node Formula:**\n   $$V(G) = P_n + 1$$\n   Where $P_n$ is the number of decision/predicate nodes (`if`, `while`, `for`, `and`, `or`).\n3. **Enclosed Regions:**\n   $$V(G) = \\text{Number of enclosed regions in planar CFG} + 1$$"
                },
                {
                    "type": "visual",
                    "title": "Control Flow Graph for If-Else Construct",
                    "code": """graph TD
  START(["1. Entry Node"]) --> IF{"2. Predicate: x > 0"}
  IF -->|"True"| THEN["3. Then Branch: y = x * 2"]
  IF -->|"False"| ELSE["4. Else Branch: y = 0"]
  THEN --> MERGE["5. Join Node"]
  ELSE --> MERGE
  MERGE --> END_NODE(["6. Exit / Return"])
  style START fill:#064e3b,stroke:#10b981
  style IF fill:#1e1b4b,stroke:#6366f1
  style MERGE fill:#1e1b4b,stroke:#6366f1
  style END_NODE fill:#3f1a1a,stroke:#ef4444"""
                },
                {
                    "type": "interactive",
                    "title": "McCabe Complexity Calculation Challenge",
                    "question": "A Python function contains 3 `if` statements and 1 `while` loop, with no boolean operators like `and`/`or`. What is its McCabe Cyclomatic Complexity?",
                    "options": [
                        "4.",
                        "5 (using V(G) = Predicate Nodes + 1 = (3 + 1) + 1 = 5).",
                        "10.",
                        "1."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nEach `if` and `while` represents a decision predicate ($P_n = 3 + 1 = 4$). Using the formula $V(G) = P_n + 1$, the complexity is $4 + 1 = 5$. This means exactly 5 linearly independent test paths are required for complete basis path coverage."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Complexity Creator Challenge",
                    "question": "The computer scientist who created Cyclomatic Complexity in 1976 was Thomas _____.\n\nAnswer: _____",
                    "answer": "McCabe",
                    "alternatives": ["McCabe", "mccabe", "Thomas McCabe"],
                    "explanation": "**Why McCabe is Correct:**\n**Thomas J. McCabe** published *A Complexity Measure*, establishing mathematical foundations for software testability and risk assessment."
                }
            ]
        },
        {
            "title": "Module 2: The Code Coverage Hierarchy",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Not all 100% coverage numbers are equal. A test suite can achieve 100% Statement Coverage while missing critical execution bugs because it failed to test alternative branches."
                },
                {
                    "type": "concept",
                    "title": "The Coverage Hierarchy Spectrum",
                    "content": "1. **Statement Coverage ($C_0$):** Has every line of code been executed at least once? (Weakest metric; misses empty `else` branches).\n2. **Branch / Decision Coverage ($C_1$):** Has every decision outcome (both True and False) been evaluated at least once?\n3. **Condition Coverage:** Has every atomic boolean sub-expression in compound conditions evaluated to both True and False?\n4. **Multiple Condition Coverage (MCC):** Tests all $2^k$ truth-table combinations of atomic conditions (exponential test explosion).\n5. **Modified Condition / Decision Coverage (MC/DC):** Industry standard for commercial avionics (DO-178C Level A). Requires each condition to independently affect the decision outcome, scaling linearly in $N + 1$ test cases."
                },
                {
                    "type": "visual",
                    "title": "Coverage Hierarchy Strength",
                    "code": """graph TD
  subgraph RigorHierarchy ["Test Coverage Strength Spectrum"]
    STMT["Statement Coverage (Weakest)"] --> BRANCH["Branch Coverage"]
    BRANCH --> COND["Condition Coverage"]
    COND --> MCDC["MC/DC Coverage (Avionics Standard)"]
    MCDC --> MCC["Multiple Condition Coverage (2^N Combos)"]
  end
  style STMT fill:#3f1a1a,stroke:#ef4444
  style BRANCH fill:#1e1b4b,stroke:#6366f1
  style MCDC fill:#064e3b,stroke:#10b981"""
                },
                {
                    "type": "interactive",
                    "title": "Statement vs. Branch Coverage Challenge",
                    "question": "Consider: `if x > 0: y = 10; return y`. A single test with `x = 5` runs. What coverage was achieved?",
                    "options": [
                        "100% Statement Coverage, but only 50% Branch Coverage (the False branch was never taken).",
                        "100% Branch Coverage.",
                        "0% Coverage.",
                        "MC/DC Coverage."
                    ],
                    "answer": 0,
                    "explanation": "**Why this is Correct:**\nThe test `x = 5` executes every physical line in the snippet (100% statement coverage). However, the implicit `else` branch (when `x <= 0`) was never evaluated, leaving 50% branch coverage untested where an uninitialized variable bug might lurk."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Avionics Standard Challenge",
                    "question": "The rigorous FAA avionics testing coverage standard that scales linearly as N + 1 test cases is _____ (Modified Condition / Decision Coverage).\n\nAnswer: _____",
                    "answer": "MC/DC",
                    "alternatives": ["MC/DC", "MCDC", "mcdc", "mc/dc"],
                    "explanation": "**Why MC/DC is Correct:**\n**MC/DC** is mandated by the FAA for safety-critical Flight Control software (DO-178C Level A)."
                }
            ]
        },
        {
            "title": "Module 3: Cyclomatic Complexity Calculator Lab",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Let's build a static analysis engine in Python that parses raw Python source code and computes its McCabe Cyclomatic Complexity."
                },
                {
                    "type": "code_lab",
                    "title": "AST Cyclomatic Complexity Analyzer",
                    "instructions": "Implement `compute_cyclomatic_complexity(python_code)` using Python's `ast` module to count decision points (`If`, `While`, `For`, `And`, `Or`, `ExceptHandler`).",
                    "starter_code": """import ast

def compute_cyclomatic_complexity(code_snippet: str) -> dict:
    \"\"\"
    Parse Python source code AST and calculate Cyclomatic Complexity.
    Formula: V(G) = Predicates + 1
    
    Decision AST nodes to count:
      - ast.If
      - ast.While
      - ast.For
      - ast.ExceptHandler
      - ast.And
      - ast.Or
      
    Returns dict:
      - 'predicate_count': int
      - 'complexity': int (predicate_count + 1)
      - 'risk_rating': 'Low' (1-10), 'Moderate' (11-20), 'High' (21+)
    \"\"\"
    # TODO: Parse AST and compute complexity
    pass
""",
                    "solution_code": """import ast

def compute_cyclomatic_complexity(code_snippet: str) -> dict:
    tree = ast.parse(code_snippet)
    predicates = 0
    
    for node in ast.walk(tree):
        if isinstance(node, (ast.If, ast.While, ast.For, ast.ExceptHandler)):
            predicates += 1
        elif isinstance(node, ast.BoolOp):
            # For 'a and b and c', values has 3 items, meaning 2 operators
            predicates += len(node.values) - 1
            
    complexity = predicates + 1
    
    if complexity <= 10:
        rating = 'Low'
    elif complexity <= 20:
        rating = 'Moderate'
    else:
        rating = 'High'
        
    return {
        'predicate_count': predicates,
        'complexity': complexity,
        'risk_rating': rating
    }
""",
                    "test_code": """simple_code = \"\"\"
def check_val(x):
    if x > 10 and x < 50:
        return True
    return False
\"\"\"
res = compute_cyclomatic_complexity(simple_code)
# 1 If + 1 And = 2 predicates -> complexity = 3
assert res['predicate_count'] == 2
assert res['complexity'] == 3
assert res['risk_rating'] == 'Low'

loop_code = \"\"\"
def process_data(items):
    for i in items:
        if i > 0:
            print(i)
        elif i < -10:
            print(-i)
\"\"\"
res2 = compute_cyclomatic_complexity(loop_code)
# 1 For + 2 Ifs = 3 predicates -> complexity = 4
assert res2['complexity'] == 4
print("Cyclomatic Complexity AST analyzer tests passed successfully!")
""",
                    "why_works": "**Why This Solution Works:**\nWalking the Python Abstract Syntax Tree (AST) counts structural branches rather than relying on brittle regex text searches. Each `If`, `While`, `For`, and boolean operator adds a decision branch, yielding the exact McCabe metric.",
                    "alternatives": "**Alternative Approaches & Trade-offs:**\n- **Radon Tool:** Industry standard CLI tool in Python (`radon cc . -a`).\n- **Cognitive Complexity (SonarQube):** Penalizes nested loops/conditionals more heavily than flat switches to better measure human readability.",
                    "edge_cases": "**Edge Cases & Failure Modes:**\n- Empty code string: Yields complexity 1 (a straight-line path with no decisions).\n- Syntax errors: Handled by standard `ast.parse` exceptions."
                }
            ]
        },
        {
            "title": "Module 4: Basis Path Testing",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Basis Path Testing is a white-box technique that uses Cyclomatic Complexity to guarantee that **every independent linear path through code is executed at least once**."
                },
                {
                    "type": "concept",
                    "title": "Basis Path Set Invariant",
                    "content": "- An **Independent Path** is any path through the CFG that introduces at least one new edge that has not been traversed before.\n- The Cyclomatic Complexity $V(G)$ defines the **exact number of independent paths** that form the basis set for the program.\n- If $V(G) = 4$, testing exactly 4 carefully chosen test paths guarantees 100% statement coverage and 100% branch coverage."
                },
                {
                    "type": "interactive",
                    "title": "Basis Path Guarantee Challenge",
                    "question": "If a software module has a Cyclomatic Complexity of $V(G) = 6$, what is the minimum number of basis path test cases needed to guarantee all edges are traversed?",
                    "options": [
                        "6 test cases.",
                        "1 test case.",
                        "64 test cases ($2^6$).",
                        "36 test cases ($6^2$)."
                    ],
                    "answer": 0,
                    "explanation": "**Why this is Correct:**\nBy definition, McCabe's Cyclomatic Complexity $V(G)$ equals the maximum number of linearly independent paths. Deriving a basis set of exactly $V(G) = 6$ test vectors is sufficient to traverse every edge in the control flow graph."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Linear Algebra Metaphor Challenge",
                    "question": "Because independent paths form a vector space that spans all possible execution paths, the set of test cases is called the _____ Path Set.\n\nAnswer: _____",
                    "answer": "Basis",
                    "alternatives": ["Basis", "basis", "Basis Path"],
                    "explanation": "**Why Basis is Correct:**\nThe term **Basis** is borrowed from linear algebra: every execution path can be represented as a linear combination of basis paths."
                }
            ]
        }
    ]
}

# CASE 19: The Test-Driven Heartbeat (TDD & Test Doubles)
PART4_CASES["19"] = {
    "title": "Case 19: The Test-Driven Heartbeat",
    "episodes": [
        {
            "title": "Module 1: Gerard Meszaros' Test Double Taxonomy",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "In *xUnit Test Patterns*, Gerard Meszaros resolved decades of confusion over test isolation by formally defining the 5 distinct types of **Test Doubles** (the software testing equivalent of stunt doubles)."
                },
                {
                    "type": "objective",
                    "title": "Module Objective",
                    "content": "Master the 5 Test Double types (Dummy, Stub, Spy, Mock, Fake), implement state verification vs behavioral verification, and isolate unit tests using Pytest mocks."
                },
                {
                    "type": "concept",
                    "title": "The 5 Types of Test Doubles",
                    "content": "1. **Dummy:** Objects passed around but never actually used; merely used to fill parameter lists (e.g. `None` or an empty object).\n2. **Stub:** Provides canned answers to calls made during the test, usually not responding to anything outside what is programmed for the test.\n3. **Spy:** A stub that also records telemetry about how it was called (e.g. recording how many times `send_email()` was invoked and with what arguments).\n4. **Mock:** An object pre-programmed with expectations which form a specification of the calls they are expected to receive. Verified via **Behavioral Verification**.\n5. **Fake:** Has a working implementation, but takes shortcuts which make it unsuitable for production (e.g. an `InMemoryDatabase` using a Python dictionary instead of PostgreSQL)."
                },
                {
                    "type": "visual",
                    "title": "Test Double Taxonomy Matrix",
                    "code": """graph LR
  subgraph SimpleDoubles ["Passive Test Doubles"]
    DUMMY["Dummy: Fills parameter slots"]
    STUB["Stub: Returns hardcoded canned answers"]
  end
  subgraph VerificationDoubles ["Active / Verifying Doubles"]
    SPY["Spy: Stubs + records call telemetry"]
    MOCK["Mock: Pre-programmed behavioral expectations"]
  end
  subgraph FunctionalDoubles ["Working Implementations"]
    FAKE["Fake: Lightweight in-memory shortcut (e.g. Dict DB)"]
  end
  style SimpleDoubles fill:#0f172a,stroke:#3b82f6
  style VerificationDoubles fill:#1e1b4b,stroke:#6366f1
  style FunctionalDoubles fill:#064e3b,stroke:#10b981"""
                },
                {
                    "type": "interactive",
                    "title": "Test Double Classification Challenge",
                    "question": "In a unit test, you replace a Stripe API client with an object that records how many times `charge()` was invoked and checks that the amount was $50. What type of test double is this?",
                    "options": [
                        "Dummy.",
                        "Mock (verifies behavioral interactions and invocation expectations).",
                        "Fake.",
                        "Pesticide."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nA **Mock** is designed for behavioral verification: rather than asserting on return state, it asserts that specific methods were invoked with specific parameters a specific number of times."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Taxonomy Author Challenge",
                    "question": "The author of 'xUnit Test Patterns' who formalized the 5 test double definitions is Gerard _____.\n\nAnswer: _____",
                    "answer": "Meszaros",
                    "alternatives": ["Meszaros", "meszaros", "Gerard Meszaros"],
                    "explanation": "**Why Gerard Meszaros is Correct:**\n**Gerard Meszaros** wrote the definitive encyclopedia of automated unit testing patterns and terminology."
                }
            ]
        },
        {
            "title": "Module 2: State Verification vs. Behavioral Verification",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Martin Fowler distinguishes between two schools of TDD: **Classic TDD (Detroit / Chicago School)** and **Mockist TDD (London School)**."
                },
                {
                    "type": "concept",
                    "title": "Classicist vs. Mockist Testing Philosophy",
                    "content": "- **Classic TDD (State Verification):**\n  - Focus: Run the system, then assert on the **resulting state** (`assert user.balance == 50`).\n  - Preference: Real collaborators and Fakes; avoids mocks unless crossing out-of-process boundaries.\n  - Benefit: Tests are resilient to refactoring; internal implementation can change completely as long as the output state matches.\n- **Mockist TDD (Behavioral Verification):**\n  - Focus: Assert on **how objects communicate** (`mock_mailer.assert_called_once_with('user@corp.com')`).\n  - Preference: Mocks all external collaborators.\n  - Danger: Tests become tightly coupled to internal implementation details, breaking whenever private methods are refactored."
                },
                {
                    "type": "interactive",
                    "title": "Testing Fragility Challenge",
                    "question": "Why do over-mocked tests often become a maintenance nightmare during code refactoring?",
                    "options": [
                        "Mocks can only run on Linux.",
                        "Because behavioral mocks assert on exact private method call sequences; refactoring the internal algorithm breaks the mocks even if the external feature behavior is 100% correct.",
                        "Mocks delete production databases.",
                        "Mocks run 100x slower than real databases."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nOver-mocking creates **fragile tests**. If a test asserts that method A calls method B twice, refactoring the algorithm to call method C once breaks the test suite even though the system output is identical."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "TDD School Challenge",
                    "question": "The TDD school that champions state verification over excessive mocking is known as the Detroit (or _____) School.\n\nAnswer: _____",
                    "answer": "Chicago",
                    "alternatives": ["Chicago", "chicago", "Classic"],
                    "explanation": "**Why Chicago is Correct:**\nThe **Chicago (Detroit) School** favors black-box state assertions using real collaborators, while the **London School** favors mock-driven outside-in development."
                }
            ]
        },
        {
            "title": "Module 3: Custom Spy & Stub Implementation Lab",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Let's build a custom Spy test double in pure Python without third-party libraries to understand how mocking frameworks record invocation telemetry."
                },
                {
                    "type": "code_lab",
                    "title": "Custom Email Notification Spy Lab",
                    "instructions": "Implement `EmailServiceSpy` that implements `send_email(to, subject)` and records calls in `call_history`. Build `OrderDispatcher` and verify it calls the spy with correct parameters.",
                    "starter_code": """class EmailServiceSpy:
    \"\"\"Custom Spy Double: records all calls made to it.\"\"\"
    def __init__(self):
        self.call_history = []
        
    def send_email(self, recipient: str, subject: str) -> bool:
        # TODO: Record call in call_history and return True
        pass
        
    def was_called_with(self, recipient: str, subject: str) -> bool:
        # TODO: Check if exact call exists in history
        pass

class OrderDispatcher:
    def __init__(self, email_service):
        self.email_service = email_service
        
    def dispatch_order(self, order_id: str, customer_email: str):
        # TODO: Process order and notify customer
        pass
""",
                    "solution_code": """class EmailServiceSpy:
    def __init__(self):
        self.call_history = []
        
    def send_email(self, recipient: str, subject: str) -> bool:
        self.call_history.append({'recipient': recipient, 'subject': subject})
        return True
        
    def was_called_with(self, recipient: str, subject: str) -> bool:
        return any(c['recipient'] == recipient and c['subject'] == subject for c in self.call_history)

class OrderDispatcher:
    def __init__(self, email_service):
        self.email_service = email_service
        
    def dispatch_order(self, order_id: str, customer_email: str):
        subject = f"Order {order_id} Dispatched"
        return self.email_service.send_email(customer_email, subject)
""",
                    "test_code": """spy = EmailServiceSpy()
dispatcher = OrderDispatcher(spy)

dispatcher.dispatch_order("ORD-501", "alice@test.com")

assert len(spy.call_history) == 1
assert spy.was_called_with("alice@test.com", "Order ORD-501 Dispatched") is True
assert spy.was_called_with("bob@test.com", "Order ORD-501 Dispatched") is False
print("Custom Spy Double tests passed successfully!")
""",
                    "why_works": "**Why This Solution Works:**\nThe `EmailServiceSpy` acts as a spy double: it intercepts calls, stubs successful return (`True`), and records all arguments in `call_history`. The test can then assert on exact behavioral expectations without sending real network emails.",
                    "alternatives": "**Alternative Approaches & Trade-offs:**\n- **`unittest.mock.MagicMock`:** Standard library mock object with built-in assertions (`assert_called_once_with`).\n- **WireMock / VCR.py:** Record and replay actual HTTP network interactions at the socket level."
                }
            ]
        },
        {
            "title": "Module 4: AAA Pattern (Arrange-Act-Assert)",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "To maintain readability, every clean automated unit test is structured into three distinct chronological phases: **Arrange, Act, Assert (AAA)**."
                },
                {
                    "type": "concept",
                    "title": "The AAA Triad",
                    "content": "1. **Arrange:** Set up test fixtures, instantiate objects, seed database states, and configure mock expectations.\n2. **Act:** Invoke the single method under test with the inputs being evaluated.\n3. **Assert:** Verify that expected state mutations, return values, or exceptions occurred.\n\n*Rule of Thumb:* A clean unit test should contain exactly one 'Act' step and fit on a single screen without scrolling."
                },
                {
                    "type": "interactive",
                    "title": "Test Structure Hygiene Challenge",
                    "question": "In the AAA pattern, which activity belongs in the 'Act' phase?",
                    "options": [
                        "Configuring mock return values.",
                        "Instantiating database connections.",
                        "Invoking the specific function or method being tested (e.g. `result = calculator.add(2, 3)`).",
                        "Writing `assert result == 5`."
                    ],
                    "answer": 2,
                    "explanation": "**Why this is Correct:**\nThe **Act** phase is the central execution trigger where the specific system-under-test (SUT) method is invoked. Setting up is Arrange; verifying outcomes is Assert."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Pattern Acronym Challenge",
                    "question": "The three-step test structure pattern of Arrange, Act, Assert is abbreviated as _____.\n\nAnswer: _____",
                    "answer": "AAA",
                    "alternatives": ["AAA", "aaa", "3A"],
                    "explanation": "**Why AAA is Correct:**\nThe **AAA pattern** (equivalent to BDD's Given-When-Then) provides universal structural consistency across automated testing suites."
                }
            ]
        }
    ]
}

print(f"Loaded {len(PART4_CASES)} cases for Part 4 (Cases 15-19).")

with open('/Users/aadarshamahato/Downloads/LEARNING_PLATFORM/se_story_lab/cases_part4.json', 'w', encoding='utf-8') as f:
    json.dump(PART4_CASES, f, indent=4)
