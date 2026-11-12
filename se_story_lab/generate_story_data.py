import json

STORIES = [
    {
        "id": 0,
        "title": "The Software Crisis",
        "icon": "⚠️",
        "genre": "Software Engineering",
        "difficulty": "Beginner",
        "hook": "Garmisch, 1968: Projects are collapsing under astronomical budget overruns, unmaintainable spaghetti code, and fatal bugs. Step into the NATO conference that birthed Software Engineering and discover why software differs fundamentally from physical hardware.",
        "primary": "Engineering Foundations"
    },
    {
        "id": 1,
        "title": "The Sequential Trap",
        "icon": "🌊",
        "genre": "Software Engineering",
        "difficulty": "Beginner",
        "hook": "Winston Royce's classic Waterfall and the dual V-Model promised military-grade discipline. Investigate a space telescope mission to uncover the deadly flaw of phase gates: why deferring testing until the end guarantees catastrophic failure.",
        "primary": "Waterfall & V-Model"
    },
    {
        "id": 2,
        "title": "The Risk Spiral",
        "icon": "🌀",
        "genre": "Software Engineering",
        "difficulty": "Beginner",
        "hook": "Barry Boehm realized that uncertainty requires risk-driven cycles rather than linear marching. Trace a healthcare platform through the 4 quadrants of the Spiral Model, mastering throwaway vs evolutionary prototyping to tame existential project risks.",
        "primary": "Spiral & Prototyping"
    },
    {
        "id": 3,
        "title": "The Agile Manifesto",
        "icon": "⚡",
        "genre": "Software Engineering",
        "difficulty": "Beginner",
        "hook": "Snowbird, 2001: 17 software rebels revolted against heavy documentation and bureaucratic processes. Analyze the 4 core values and 12 principles of Agile, learning how lean waste elimination and rapid feedback loops outperform rigid master plans.",
        "primary": "Agile Manifesto & Lean"
    },
    {
        "id": 4,
        "title": "The Sprints of Chaos",
        "icon": "🏃",
        "genre": "Software Engineering",
        "difficulty": "Beginner",
        "hook": "A fintech startup is drowning in missed deadlines and scope creep. Take charge as Scrum Master: calibrate story points, facilitate Daily Standups and Sprint Retrospectives, and enforce Kanban WIP limits to rescue delivery velocity.",
        "primary": "Scrum & Kanban"
    },
    {
        "id": 5,
        "title": "The Clean Coder",
        "icon": "🥋",
        "genre": "Software Engineering",
        "difficulty": "Beginner",
        "hook": "Kent Beck's Extreme Programming (XP) mandates radical technical discipline. Pair program with automated test suites, enforce continuous refactoring, and experience why writing tests BEFORE implementation creates fearless engineering teams.",
        "primary": "Extreme Programming & TDD"
    },
    {
        "id": 6,
        "title": "The Elusive Specification",
        "icon": "🔍",
        "genre": "Software Engineering",
        "difficulty": "Intermediate",
        "hook": "A client says they want 'a fast, user-friendly banking portal'. Unravel vague requirements into rigorous Functional and Non-Functional specifications using FURPS+, stakeholder elicitation techniques, and INVEST user stories.",
        "primary": "Requirements Elicitation"
    },
    {
        "id": 7,
        "title": "The Blueprint Contract",
        "icon": "📜",
        "genre": "Software Engineering",
        "difficulty": "Intermediate",
        "hook": "Transform messy requirements into an industry-standard IEEE 830 / ISO 29148 Software Requirements Specification (SRS). Build a Requirements Traceability Matrix (RTM) to ensure zero orphaned features and 100% test coverage.",
        "primary": "SRS & Traceability"
    },
    {
        "id": 8,
        "title": "The Structural Anatomy",
        "icon": "🏛️",
        "genre": "Software Engineering",
        "difficulty": "Intermediate",
        "hook": "Visualizing complex systems before writing code is the hallmark of senior architects. Master UML Class Diagrams, Component Diagrams, and Deployment Topologies, distinguishing association, aggregation, and deep composition.",
        "primary": "UML Structural Diagrams"
    },
    {
        "id": 9,
        "title": "The Symphony of Messages",
        "icon": "🎼",
        "genre": "Software Engineering",
        "difficulty": "Intermediate",
        "hook": "A payment gateway crashes under concurrent distributed requests. Map the dynamic message flows using UML Sequence Diagrams with asynchronous lifelines, State Machine transition tables, and parallel Activity Diagrams.",
        "primary": "UML Behavioral Diagrams"
    },
    {
        "id": 10,
        "title": "The Architecture Decision",
        "icon": "🗼",
        "genre": "Software Engineering",
        "difficulty": "Intermediate",
        "hook": "Monolith vs Microservices vs Event-Driven vs Hexagonal: every architectural choice is a trade-off between latency, team independence, and operational overhead. Lead an architectural migration for an e-commerce giant.",
        "primary": "Software Architecture"
    },
    {
        "id": 11,
        "title": "The Tangled Web",
        "icon": "🕸️",
        "genre": "Software Engineering",
        "difficulty": "Intermediate",
        "hook": "Larry Constantine's metrics govern system maintainability: High Cohesion and Low Coupling. Dissect legacy codebases to classify coincidental vs functional cohesion and content vs data coupling, dismantling monolithic dependency webs.",
        "primary": "Cohesion & Coupling"
    },
    {
        "id": 12,
        "title": "The SOLID Foundations",
        "icon": "💎",
        "genre": "Software Engineering",
        "difficulty": "Intermediate",
        "hook": "Robert C. Martin's 5 Object-Oriented commandments. Refactor brittle inheritance hierarchies using Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, and Dependency Inversion into resilient, extensible code.",
        "primary": "SOLID Principles"
    },
    {
        "id": 13,
        "title": "The Object Foundry",
        "icon": "🏭",
        "genre": "Software Engineering",
        "difficulty": "Intermediate",
        "hook": "Hard-coding 'new Object()' ties client code to concrete implementations. Master the Gang of Four Creational patterns: Factory Method, Abstract Factory, Builder, and thread-safe Singletons to decouple object instantiation.",
        "primary": "Creational Patterns"
    },
    {
        "id": 14,
        "title": "The Structural Bridge",
        "icon": "🌉",
        "genre": "Software Engineering",
        "difficulty": "Intermediate",
        "hook": "How do you connect incompatible legacy third-party APIs without modifying core business logic? Employ Structural patterns: Adapter, Decorator, Facade, Composite, and Proxy to create clean architectural interfaces.",
        "primary": "Structural Patterns"
    },
    {
        "id": 15,
        "title": "The Dynamic Behavior",
        "icon": "🎭",
        "genre": "Software Engineering",
        "difficulty": "Intermediate",
        "hook": "Manage complex run-time algorithms and state transitions cleanly. Implement Behavioral patterns: Observer for reactive event buses, Strategy for hot-swappable routing algorithms, and Command for transactional undo/redo operations.",
        "primary": "Behavioral Patterns"
    },
    {
        "id": 16,
        "title": "The Quality Pyramid",
        "icon": "🔺",
        "genre": "Software Engineering",
        "difficulty": "Advanced",
        "hook": "'Testing can prove the presence of bugs, but never their absence.' Explore the V&V distinction and the Test Pyramid: balancing thousands of millisecond unit tests against integration tests and end-to-end browser automation.",
        "primary": "Testing Fundamentals"
    },
    {
        "id": 17,
        "title": "The Dark Box",
        "icon": "📦",
        "genre": "Software Engineering",
        "difficulty": "Advanced",
        "hook": "Test critical software without inspecting a single line of internal code. Master Black-Box techniques: Equivalence Class Partitioning, Boundary Value Analysis (BVA), and Decision Tables to expose off-by-one errors and edge-case faults.",
        "primary": "Black-Box Testing"
    },
    {
        "id": 18,
        "title": "The Glass Box",
        "icon": "🔬",
        "genre": "Software Engineering",
        "difficulty": "Advanced",
        "hook": "Peer into the control-flow graph of safety-critical avionics code. Calculate McCabe's Cyclomatic Complexity V(G) = E - N + 2P and construct test suites that achieve Statement, Branch, Condition, and rigorous MC/DC coverage.",
        "primary": "White-Box Testing"
    },
    {
        "id": 19,
        "title": "The Test-Driven Heartbeat",
        "icon": "❤️‍🩹",
        "genre": "Software Engineering",
        "difficulty": "Advanced",
        "hook": "Experience the rhythmic flow of Test-Driven Development (TDD): Red, Green, Refactor. Master test doubles (Dummies, Stubs, Spies, Mocks, and Fakes) in pytest to isolate microservices from network and database dependencies.",
        "primary": "TDD & Test Doubles"
    },
    {
        "id": 20,
        "title": "The Divergent Tree",
        "icon": "🌿",
        "genre": "Software Engineering",
        "difficulty": "Advanced",
        "hook": "Peel back the hood of Git's Directed Acyclic Graph (DAG) of cryptographic SHA-1 hashes, Blobs, Trees, and Commits. Compare Trunk-Based Development with GitFlow and master fast-forward merges, three-way merges, and rebasing.",
        "primary": "Git & Version Control"
    },
    {
        "id": 21,
        "title": "The Continuous Assembly",
        "icon": "🚀",
        "genre": "Software Engineering",
        "difficulty": "Advanced",
        "hook": "Manual deployments on Friday nights are a recipe for downtime. Construct an enterprise CI/CD pipeline from scratch: static analysis linting, automated test gates, Docker containerization, and canary deployment rollouts.",
        "primary": "CI/CD & DevOps"
    },
    {
        "id": 22,
        "title": "The Legacy Curse",
        "icon": "🏚️",
        "genre": "Software Engineering",
        "difficulty": "Advanced",
        "hook": "Software is never done; it either evolves or decays. Study Lehman's Laws of Software Evolution, calculate Technical Debt interest, identify Martin Fowler's code smells (God Classes, Feature Envy), and apply safe refactorings.",
        "primary": "Maintenance & Refactoring"
    },
    {
        "id": 23,
        "title": "The Estimation Mirage",
        "icon": "⏳",
        "genre": "Software Engineering",
        "difficulty": "Advanced",
        "hook": "Why are software schedules notoriously inaccurate? Apply formal estimation models: Boehm's COCOMO II, Albrecht's Function Point Analysis (FPA), and Agile Planning Poker to calculate project effort, team size, and delivery duration.",
        "primary": "Project Estimation"
    },
    {
        "id": 24,
        "title": "The Reliable Fortress",
        "icon": "🛡️",
        "genre": "Software Engineering",
        "difficulty": "Advanced",
        "hook": "Bridge software engineering into Site Reliability Engineering (SRE). Implement the ISO 25010 Quality Model, mitigate OWASP Top 10 vulnerabilities, and establish Service Level Objectives (SLOs) and Error Budgets to guarantee 99.99% uptime.",
        "primary": "Quality Assurance & SRE"
    }
]

with open('/Users/aadarshamahato/Downloads/LEARNING_PLATFORM/se_story_lab/story_data.py', 'w', encoding='utf-8') as f:
    f.write("# Master Investigation Catalog for SE Story Lab\n")
    f.write("STORIES = \\\n")
    json.dump(STORIES, f, indent=4, ensure_ascii=False)
    f.write("\n")

print(f"Generated story_data.py with {len(STORIES)} cases!")
