NEW_STORIES = {
    17: {
        "title": "The Codebase That Couldn't Change",
        "description": "Unravel the tangled web of a monolithic legacy system. Learn the SOLID principles to breathe life and flexibility back into rigidly coupled code.",
        "difficulty": "Advanced",
        "topic": "SOLID Principles",
        "modules": 8
    },
    18: {
        "title": "The Inheritance Trap",
        "description": "Discover the hidden dangers of deep class hierarchies. Learn to favor composition over inheritance and master delegation to build robust systems.",
        "difficulty": "Advanced",
        "topic": "Composition vs Inheritance",
        "modules": 8
    },
    19: {
        "title": "The Pattern Library",
        "description": "Explore the timeless solutions to recurring software design problems. Master key Design Patterns like Factory, Strategy, Observer, and Decorator.",
        "difficulty": "Expert",
        "topic": "Design Patterns",
        "modules": 8
    },
    20: {
        "title": "The Architect's War Room",
        "description": "Step into the shoes of a lead architect. Design real-world systems, identify entities, manage relationships, and build for extensibility.",
        "difficulty": "Expert",
        "topic": "System Design",
        "modules": 8
    }
}

NEW_LEVELS = {
    17: {
        1: [
            {"type": "story", "content": "You are called to rescue Project Chimera, a massive monolithic codebase that breaks every time a new feature is added. The lead developer is pulling their hair out."},
            {"type": "problem", "content": "Why does changing one part of the system cause unrelated parts to fail?"},
            {"type": "concept", "content": "When code is tightly coupled, modules rely heavily on the internal workings of other modules. A lack of cohesion means a single module tries to do too many unrelated things."},
            {"type": "visual", "visual_type": "text", "content": "[UI Module] <---> [Database Module] <---> [Business Logic] : Everything is connected like a spiderweb."},
            {"type": "reflection", "question": "Have you ever modified a class and accidentally broken something completely different? What caused it?"}
        ],
        2: [
            {"type": "story", "content": "First, we look at the 'ReportGenerator' class. It fetches data, formats it into HTML, and emails it to the boss. It changes every week."},
            {"type": "concept", "content": "The Single Responsibility Principle (SRP) states that a class should have one, and only one, reason to change."},
            {"type": "code_experiment", "starter_code": "class ReportGenerator {\npublic:\n  void fetch_data() { /* DB query */ }\n  void format_html() { /* HTML tags */ }\n  void send_email() { /* SMTP */ }\n};", "expected_output": "Refactor to three classes: DataFetcher, ReportFormatter, EmailSender."},
            {"type": "debugger", "scenario": "A new requirement asks for CSV format instead of HTML.", "options": ["Add format_csv() to ReportGenerator", "Create a new ReportFormatter interface and CSVFormatter class"], "answer": 1, "explanation": "Adding it to ReportGenerator violates SRP and OCP. Creating a separate formatter keeps responsibilities distinct."}
        ],
        3: [
            {"type": "concept", "content": "The Open/Closed Principle (OCP): Software entities should be open for extension, but closed for modification."},
            {"type": "worked_example", "content": "Instead of a massive switch statement for different payment types in a PaymentProcessor, use an IPaymentMethod interface. You can add new payment methods without touching the core processor."},
            {"type": "micro_challenge", "question": "How do interfaces/abstract classes help achieve OCP in C++?", "answer": "By defining a contract that new classes can implement without altering existing consumer code."}
        ],
        4: [
            {"type": "story", "content": "You notice a 'Bird' base class with a 'fly()' method. Someone added an 'Ostrich' class that inherits from 'Bird' but throws an exception in 'fly()'."},
            {"type": "concept", "content": "Liskov Substitution Principle (LSP): Objects of a superclass should be replaceable with objects of its subclasses without breaking the application."},
            {"type": "reflection", "question": "If a Square inherits from Rectangle, and you set width=5 and height=10 on the Square, what happens? Does this violate LSP?"}
        ],
        5: [
            {"type": "concept", "content": "Interface Segregation Principle (ISP): No client should be forced to depend on methods it does not use."},
            {"type": "visual", "visual_type": "text", "content": "Fat Interface: IMachine { print(), fax(), scan() }\nSegregated: IPrinter { print() }, IFax { fax() }, IScanner { scan() }"}
        ],
        6: [
            {"type": "concept", "content": "Dependency Inversion Principle (DIP): High-level modules should not depend on low-level modules. Both should depend on abstractions."},
            {"type": "code_experiment", "starter_code": "class Database {};\nclass App { Database db; }; // Tightly coupled", "expected_output": "class IDatabase {};\nclass Database : public IDatabase {};\nclass App { IDatabase& db; App(IDatabase& d) : db(d) {} }; // Decoupled via Dependency Injection"}
        ],
        7: [
            {"type": "story", "content": "Armed with SOLID, you begin tearing down the monolith piece by piece, injecting dependencies and carving out interfaces."},
            {"type": "problem", "content": "How do you instantiate all these objects now that they depend on interfaces?"},
            {"type": "concept", "content": "Dependency Injection (DI) containers or factory classes act as the 'wiring' layer, constructing objects and their dependencies near the entry point of the application."}
        ],
        8: [
            {"type": "story", "content": "Project Chimera is stable. New features are added by creating new classes, not modifying old ones. The codebase can finally evolve."},
            {"type": "micro_challenge", "question": "Which principle emphasizes that abstractions should not depend on details?", "answer": "Dependency Inversion Principle"}
        ]
    },
    18: {
        1: [
            {"type": "story", "content": "You join a game studio. They have a massive class hierarchy: Object -> MobileObject -> Character -> Player -> Wizard. It's a nightmare to navigate."},
            {"type": "concept", "content": "Deep inheritance trees lead to the 'Fragile Base Class' problem. A small change at the top breaks everything below."}
        ],
        2: [
            {"type": "problem", "content": "A designer wants an 'EnemyWizard' that has Wizard spells but Enemy AI. In a strict hierarchy, you can't easily inherit from both without the diamond problem."},
            {"type": "concept", "content": "Inheritance defines 'is-a' relationships. But what if something is composed of multiple behaviors?"}
        ],
        3: [
            {"type": "concept", "content": "Composition over Inheritance: Build complex objects by assembling smaller, single-purpose components rather than inheriting from a massive base class."},
            {"type": "visual", "visual_type": "text", "content": "Inheritance: class Wizard : public Player { ... }\nComposition: class Entity { HealthComponent hc; MagicComponent mc; }"}
        ],
        4: [
            {"type": "story", "content": "You refactor the Entity class to hold a list of Components. Now, adding magic to an enemy is as easy as attaching a MagicComponent."},
            {"type": "code_experiment", "starter_code": "class Entity { public: void update() {} }; // Base class", "expected_output": "class Entity { vector<Component*> comps; public: void update() { for(auto c: comps) c->update(); } };"}
        ],
        5: [
            {"type": "concept", "content": "Delegation: Forwarding a method call to a component. It allows an object to act like a subclass without being one."},
            {"type": "worked_example", "content": "A Window class doesn't need to inherit from Rectangle to have area. It can own a Rectangle object and delegate getArea() to it."}
        ],
        6: [
            {"type": "reflection", "question": "Why is multiple inheritance in C++ often discouraged, and how does composition solve the same problem more cleanly?"}
        ],
        7: [
            {"type": "concept", "content": "Traits and Interfaces (Pure Abstract Classes in C++). Use inheritance for defining interfaces (contracts), but use composition for sharing implementation."}
        ],
        8: [
            {"type": "story", "content": "The game studio's codebase is flat, flexible, and data-driven. The designers love you."},
            {"type": "micro_challenge", "question": "What principle says to build classes by combining behaviors rather than extending them?", "answer": "Composition over inheritance"}
        ]
    },
    19: {
        1: [
            {"type": "story", "content": "You discover an ancient tome in the software library: 'Design Patterns: Elements of Reusable Object-Oriented Software'."},
            {"type": "concept", "content": "Design patterns are proven templates for solving common software architecture problems. They provide a shared vocabulary for developers."}
        ],
        2: [
            {"type": "concept", "content": "Creational: The Factory Pattern. It encapsulates the instantiation logic of objects, hiding the complex 'new' calls from the client."},
            {"type": "code_experiment", "starter_code": "Enemy* e = new Goblin(); // Hardcoded", "expected_output": "Enemy* e = EnemyFactory::create(\"Goblin\"); // Decoupled"}
        ],
        3: [
            {"type": "concept", "content": "Creational: Abstract Factory. Provides an interface for creating families of related or dependent objects without specifying their concrete classes."}
        ],
        4: [
            {"type": "concept", "content": "Behavioral: The Strategy Pattern. Defines a family of algorithms, encapsulates each one, and makes them interchangeable at runtime."},
            {"type": "debugger", "scenario": "Sorting an array using different algorithms depending on data size.", "options": ["Write a giant switch statement inside sort()", "Pass an ISortStrategy object to the sorter context"], "answer": 1, "explanation": "The Strategy pattern lets you swap algorithms without modifying the context class."}
        ],
        5: [
            {"type": "concept", "content": "Behavioral: The Observer Pattern. Defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically. Crucial for Event Systems and UI."}
        ],
        6: [
            {"type": "concept", "content": "Structural: The Decorator Pattern. Attaches additional responsibilities to an object dynamically. It provides a flexible alternative to subclassing for extending functionality."},
            {"type": "visual", "visual_type": "text", "content": "Coffee -> MilkDecorator(Coffee) -> SugarDecorator(MilkDecorator) : Wraps the object to add behavior."}
        ],
        7: [
            {"type": "concept", "content": "Behavioral: The Command Pattern. Encapsulates a request as an object, thereby letting you parameterize clients with different requests, queue or log requests, and support undoable operations."}
        ],
        8: [
            {"type": "story", "content": "You've mastered the foundational patterns. You now see the matrix: everywhere you look in the codebase, you spot Factories, Observers, and Strategies."},
            {"type": "reflection", "question": "Why is it dangerous to overuse Design Patterns (Patternitis)?"}
        ]
    },
    20: {
        1: [
            {"type": "story", "content": "You've been promoted to Chief Architect. Your first task: Design a scalable ride-sharing backend system from scratch."},
            {"type": "concept", "content": "System design bridges the gap between individual classes and the entire application architecture."}
        ],
        2: [
            {"type": "problem", "content": "Where do you even begin?"},
            {"type": "concept", "content": "Start by identifying the Core Entities (Nouns). In a ride-sharing app: Rider, Driver, Ride, Location, Payment."}
        ],
        3: [
            {"type": "concept", "content": "Define the Relationships and Interactions (Verbs). A Rider 'requests' a Ride. A Driver 'accepts' a Ride."},
            {"type": "visual", "visual_type": "text", "content": "[Rider] 1 -- * [Ride] * -- 1 [Driver]"}
        ],
        4: [
            {"type": "concept", "content": "Designing for Extensibility. How will the system handle a new ride type (e.g., Carpool, Luxury) without breaking existing code? Apply OCP and Factory patterns."}
        ],
        5: [
            {"type": "concept", "content": "Managing State. A Ride goes through states: Requested, Accepted, InProgress, Completed. Use the State Pattern to encapsulate state-specific behavior."}
        ],
        6: [
            {"type": "concept", "content": "Error Handling Architecture. How do you handle network failures when connecting Rider to Driver? Design resilient retry mechanisms and define clear boundaries for exception propagation."}
        ],
        7: [
            {"type": "concept", "content": "The Data Layer. How are entities persisted? Apply the Repository Pattern to abstract away database specifics (SQL vs NoSQL)."}
        ],
        8: [
            {"type": "story", "content": "The war room whiteboard is covered in diagrams. The system is decoupled, extensible, and robust. You are a true C++ Architect."},
            {"type": "micro_challenge", "question": "What pattern is best for abstracting database queries from business logic?", "answer": "Repository Pattern"}
        ]
    }
}
