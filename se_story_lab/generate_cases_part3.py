import json
import os

PART3_CASES = {}

# CASE 10: The Architecture Decision (Software Architecture)
PART3_CASES["10"] = {
    "title": "Case 10: The Architecture Decision",
    "episodes": [
        {
            "title": "Module 1: The Scope of Software Architecture",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Martin Fowler quotes Ralph Johnson: *'Architecture is about the important stuff. Whatever that is.'* More formally, software architecture comprises the foundational design choices that are **costly and difficult to change once implemented**. It shapes the system's non-functional quality attributes: latency, scalability, security, and team deployment velocity."
                },
                {
                    "type": "objective",
                    "title": "Module Objective",
                    "content": "Master architectural paradigms: Monolithic, Microservices, Event-Driven, and Hexagonal (Ports & Adapters) architectures, evaluating their trade-offs under Conway's Law."
                },
                {
                    "type": "concept",
                    "title": "Architectural Drivers & Conway's Law",
                    "content": "### Key Concepts:\n- **Architectural Drivers:** High-priority Quality Attribute Requirements (QARs) that dictate structure. For example, a trading platform prioritizes sub-millisecond latency; a global e-commerce portal prioritizes 99.999% availability and independent team releases.\n- **Conway's Law (Melvin Conway, 1967):** *'Organizations which design systems are constrained to produce designs which are copies of the communication structures of these organizations.'* A company with 4 siloed teams will inevitably produce a 4-tier software architecture."
                },
                {
                    "type": "visual",
                    "title": "Monolith vs. Microservices Architectural Topology",
                    "code": """graph TD
  subgraph Monolithic ["Monolithic Architecture"]
    M_UI["Presentation Layer"] --> M_BIZ["Single Process: Order, Inventory, Auth, Billing"]
    M_BIZ --> M_DB[("Single Unified Relational DB")]
  end
  subgraph Microservices ["Microservices Architecture"]
    API_GW["API Gateway"]
    API_GW --> S_AUTH["Auth Service"]
    API_GW --> S_ORD["Order Service"]
    API_GW --> S_INV["Inventory Service"]
    S_AUTH --> DB_AUTH[("Auth DB")]
    S_ORD --> DB_ORD[("Order DB")]
    S_INV --> DB_INV[("Inv DB")]
    S_ORD -.->|"Kafka Event Bus"| S_INV
  end
  style Monolithic fill:#1e1b4b,stroke:#6366f1
  style Microservices fill:#064e3b,stroke:#10b981"""
                },
                {
                    "type": "interactive",
                    "title": "Architectural Trade-off Challenge",
                    "question": "A 5-person seed startup with 200 users chooses a microservices architecture with 15 separate Kubernetes services and distributed databases. What is the most likely consequence?",
                    "options": [
                        "The startup will immediately achieve higher profit margins and faster feature delivery.",
                        "The crushing operational overhead of distributed tracing, network latency, distributed transactions (sagas), and deployment complexity will cripple the small team.",
                        "The system will automatically scale to 100 million users without code changes.",
                        "Conway's Law will be permanently nullified."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nMicroservices trade operational simplicity for team scaling independence. For a small 5-person team, microservices introduce massive distributed systems complexity (network failures, eventual consistency, distributed tracing) without any of the organizational benefits, an antipattern known as the 'Distributed Monolith'."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Sociological Law Challenge",
                    "question": "The foundational software observation that system architectures mirror the communication structures of the organizations that design them is _____ Law.\n\nAnswer: _____",
                    "answer": "Conway's",
                    "alternatives": ["Conway's", "Conway", "conway", "Conways Law"],
                    "explanation": "**Why Conway's Law is Correct:**\n**Conway's Law** explains why architectural reorganizations must go hand-in-hand with organizational team restructurings (the 'Inverse Conway Maneuver')."
                }
            ]
        },
        {
            "title": "Module 2: Event-Driven Architecture (EDA)",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Synchronous REST calls (`HTTP GET/POST`) create temporal and spatial coupling: if Service B is slow or down, Service A blocks and cascades failure. **Event-Driven Architecture (EDA)** decouples producers and consumers using immutable event streams."
                },
                {
                    "type": "concept",
                    "title": "Core EDA Concepts & Messaging Topologies",
                    "content": "- **Event:** A notification of something that has already happened in the past (e.g., `OrderPlaced`, `PaymentReceived`). Events are immutable facts.\n- **Message Broker:** High-throughput streaming platforms (Apache Kafka, RabbitMQ, AWS SNS/SQS) that buffer and route events.\n- **Choreography vs. Orchestration:**\n  - *Choreography:* Microservices react to domain events autonomously without a central coordinator.\n  - *Orchestration:* A central workflow coordinator (e.g., Temporal, AWS Step Functions) explicitly directs each service what to do next.\n- **Eventual Consistency:** In distributed systems, data converges to consistency over time rather than guaranteeing immediate ACID transactional locking."
                },
                {
                    "type": "visual",
                    "title": "Choreographed Event-Driven Pipeline",
                    "code": """graph LR
  subgraph Producer ["Event Producer"]
    CHECKOUT["Checkout Service"]
  end
  subgraph EventStream ["Distributed Event Log (Kafka)"]
    TOPIC["Topic: 'order-events' (Partitioned)"]
  end
  subgraph Consumers ["Autonomous Reactive Consumers"]
    EMAIL["Notification Service (Send Email)"]
    FRAUD["Fraud Detection Service (Analyze Risk)"]
    INVENTORY["Inventory Service (Reserve Stock)"]
  end
  CHECKOUT -->|"Emit: OrderPlacedEvent"| TOPIC
  TOPIC --> EMAIL & FRAUD & INVENTORY
  style Producer fill:#0f172a,stroke:#3b82f6
  style EventStream fill:#3f1a1a,stroke:#ef4444
  style Consumers fill:#064e3b,stroke:#10b981"""
                },
                {
                    "type": "interactive",
                    "title": "Temporal Decoupling Challenge",
                    "question": "In an Event-Driven Architecture, what happens if the Email Notification Service goes offline for 30 minutes while customers are placing orders?",
                    "options": [
                        "Customers receive HTTP 500 errors and cannot checkout.",
                        "Orders are placed successfully; the events accumulate safely in the broker, and the Notification Service processes the backlog as soon as it recovers.",
                        "All checkout transactions are automatically rolled back in the database.",
                        "The Kafka event broker crashes due to buffer overflow."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nEDA provides **temporal decoupling**. The producer (Checkout Service) only needs to successfully write the event to the resilient broker. If a consumer is temporarily offline, events are buffered in the log and processed in order upon recovery without impacting upstream users."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Distributed Consistency Challenge",
                    "question": "The data consistency model in distributed microservices where all replicas eventually become consistent without continuous synchronous ACID locking is _____ consistency.\n\nAnswer: _____",
                    "answer": "Eventual",
                    "alternatives": ["Eventual", "eventual", "Eventual Consistency"],
                    "explanation": "**Why Eventual is Correct:**\nUnder the CAP theorem, distributed systems trading immediate consistency for high availability rely on **Eventual Consistency**."
                }
            ]
        },
        {
            "title": "Module 3: Hexagonal Architecture (Ports and Adapters)",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Alistair Cockburn created **Hexagonal Architecture** (also known as Ports and Adapters, closely related to Uncle Bob's Clean Architecture and Onion Architecture). Its fundamental rule: **Business logic must not depend on external frameworks, databases, or UI protocols**."
                },
                {
                    "type": "concept",
                    "title": "Ports and Adapters Mechanics",
                    "content": "- **Inside the Hexagon (Domain Core):** Pure business entities, domain rules, and use cases. Has ZERO dependencies on libraries like Django, SQLAlchemy, Flask, or Postgres.\n- **Ports (Interfaces):**\n  - *Driving / Primary Ports:* Interfaces that describe how external callers interact with the domain (e.g. `OrderUseCasePort`).\n  - *Driven / Secondary Ports:* Interfaces that describe what the domain needs from external systems (e.g. `OrderRepositoryPort`, `PaymentGatewayPort`).\n- **Adapters (Implementation):** Concrete implementations that plug into ports.\n  - *Driving Adapters:* REST Controllers, GraphQL Resolvers, CLI tools, RabbitMQ listeners.\n  - *Driven Adapters:* PostgreSQL repository, Stripe client, in-memory mock repository for tests."
                },
                {
                    "type": "visual",
                    "title": "Hexagonal Architecture Isolation",
                    "code": """graph TD
  subgraph OutsideWorld ["External World (Frameworks & Drivers)"]
    REST["REST Controller (FastAPI)"]
    CLI["CLI Management Command"]
    PG_ADAPTER["PostgreSQL Adapter"]
    MOCK_DB["In-Memory Mock Adapter"]
  end
  subgraph PortsLayer ["Boundary Ports (Interfaces)"]
    PRIMARY_PORT["OrderUseCase (Driving Port)"]
    SECONDARY_PORT["OrderRepository (Driven Port)"]
  end
  subgraph DomainCore ["Pure Hexagon Domain (Zero External Dependencies)"]
    ORDER_ENTITY["Order Entity & Business Rules"]
    USE_CASE["ProcessOrderUseCase Interactor"]
  end
  REST & CLI --> PRIMARY_PORT --> USE_CASE --> ORDER_ENTITY
  USE_CASE --> SECONDARY_PORT
  PG_ADAPTER & MOCK_DB -.->|"Implements"| SECONDARY_PORT
  style OutsideWorld fill:#0f172a,stroke:#3b82f6
  style PortsLayer fill:#1e1b4b,stroke:#6366f1
  style DomainCore fill:#064e3b,stroke:#10b981"""
                },
                {
                    "type": "interactive",
                    "title": "Hexagonal Dependency Rule Challenge",
                    "question": "In Hexagonal Architecture, which direction do source code dependencies point?",
                    "options": [
                        "Domain entities must import database models directly to ensure data integrity.",
                        "Dependencies point strictly inward toward the domain; the domain core knows nothing about databases, web frameworks, or third-party APIs.",
                        "Controllers depend on databases, which depend on domain logic.",
                        "All layers have bidirectional circular dependencies."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nThe **Dependency Inversion Principle** governs Hexagonal Architecture: all source code dependencies point strictly inward toward high-level business policies. External details (databases, web frameworks) depend on domain abstractions (ports)."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Architecture Synonym Challenge",
                    "question": "Hexagonal Architecture is formally and descriptively known as the Ports and _____ architecture.\n\nAnswer: _____",
                    "answer": "Adapters",
                    "alternatives": ["Adapters", "adapters", "Ports and Adapters"],
                    "explanation": "**Why Adapters is Correct:**\n**Ports and Adapters** highlights how adapters translate between external protocol data formats and internal domain contracts."
                }
            ]
        },
        {
            "title": "Module 4: Hexagonal Order Engine Implementation Lab",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Let's implement a complete Hexagonal slice: a pure Domain Use Case decoupled from concrete database storage using an abstract Driven Port, allowing instant swap to an in-memory repository for unit testing."
                },
                {
                    "type": "code_lab",
                    "title": "Hexagonal Domain Decoupling Lab",
                    "instructions": "Implement `OrderRepositoryPort` (abstract interface), `InMemoryOrderRepository` (driven adapter), and `OrderService` (domain use case). Verify that `OrderService` operates correctly using the abstract port.",
                    "starter_code": """from abc import ABC, abstractmethod

class OrderRepositoryPort(ABC):
    @abstractmethod
    def save(self, order: dict) -> bool:
        pass
        
    @abstractmethod
    def find_by_id(self, order_id: str) -> dict:
        pass

class InMemoryOrderRepository(OrderRepositoryPort):
    \"\"\"Driven Adapter: stores orders in a dictionary.\"\"\"
    def __init__(self):
        self._storage = {}
        
    def save(self, order: dict) -> bool:
        # TODO: Store order
        pass
        
    def find_by_id(self, order_id: str) -> dict:
        # TODO: Retrieve order
        pass

class OrderService:
    \"\"\"Pure Domain Interactor: interacts only through OrderRepositoryPort.\"\"\"
    def __init__(self, repo: OrderRepositoryPort):
        self.repo = repo
        
    def create_order(self, order_id: str, total_amount: float) -> dict:
        # TODO: Validate and save order
        pass
""",
                    "solution_code": """from abc import ABC, abstractmethod

class OrderRepositoryPort(ABC):
    @abstractmethod
    def save(self, order: dict) -> bool:
        pass
        
    @abstractmethod
    def find_by_id(self, order_id: str) -> dict:
        pass

class InMemoryOrderRepository(OrderRepositoryPort):
    def __init__(self):
        self._storage = {}
        
    def save(self, order: dict) -> bool:
        self._storage[order['id']] = order
        return True
        
    def find_by_id(self, order_id: str) -> dict:
        return self._storage.get(order_id)

class OrderService:
    def __init__(self, repo: OrderRepositoryPort):
        self.repo = repo
        
    def create_order(self, order_id: str, total_amount: float) -> dict:
        if total_amount <= 0:
            raise ValueError("Order total must be positive")
        order = {
            'id': order_id,
            'total': float(total_amount),
            'status': 'CONFIRMED'
        }
        self.repo.save(order)
        return order
""",
                    "test_code": """repo = InMemoryOrderRepository()
service = OrderService(repo)

order = service.create_order("ORD-101", 149.99)
assert order['status'] == 'CONFIRMED'
assert repo.find_by_id("ORD-101")['total'] == 149.99

try:
    service.create_order("ORD-102", -50.0)
    assert False, "Should have raised ValueError"
except ValueError:
    pass

print("Hexagonal Decoupling tests passed successfully!")
""",
                    "why_works": "**Why This Solution Works:**\n`OrderService` depends exclusively on `OrderRepositoryPort` (an abstraction). It does not import or know about SQL, tables, or database drivers. We can test 100% of the domain business logic in memory in 2 milliseconds without starting a Docker database.",
                    "alternatives": "**Alternative Approaches & Trade-offs:**\n- **Active Record Pattern (Django ORM / Rails):** Models inherit directly from database base classes (`class Order(models.Model)`). Faster to scaffold, but couples domain logic tightly to database schema.\n- **Data Mapper Pattern:** ORM pattern (SQLAlchemy) separating the in-memory representation from the database schema.",
                    "edge_cases": "**Edge Cases & Failure Modes:**\n- Non-existent order lookup: Returns `None` cleanly without throwing exceptions.\n- Zero or negative amount: Intercepted by domain validation before hitting the repository."
                }
            ]
        }
    ]
}

# CASE 11: The Tangled Web (Cohesion & Coupling)
PART3_CASES["11"] = {
    "title": "Case 11: The Tangled Web",
    "episodes": [
        {
            "title": "Module 1: Constantine's Law: High Cohesion & Low Coupling",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "In 1974, Larry Constantine and Edward Yourdon introduced the two foundational metrics that govern modular software architecture: **Cohesion** and **Coupling**. The golden law of software engineering states: **Maximize Cohesion within modules, and Minimize Coupling between modules**."
                },
                {
                    "type": "objective",
                    "title": "Module Objective",
                    "content": "Classify the 7 levels of Cohesion and 5 levels of Coupling, apply the Law of Demeter, and calculate the Instability (I) metric."
                },
                {
                    "type": "concept",
                    "title": "Definitions of Cohesion and Coupling",
                    "content": "- **Cohesion:** A measure of how strongly related and focused the responsibilities inside a single module or class are. A highly cohesive module does one thing and does it completely.\n- **Coupling:** A measure of the degree of interdependence between two modules. Tightly coupled modules cannot be modified, tested, or reused independently without breaking each other."
                },
                {
                    "type": "visual",
                    "title": "Cohesion vs. Coupling Grid",
                    "code": """graph TD
  subgraph IdealArchitecture ["IDEAL: High Cohesion, Low Coupling (Modular)"]
    M1["Module A (Single Clear Focus)"]
    M2["Module B (Single Clear Focus)"]
    M1 -.->|"Narrow Interface Contract"| M2
  end
  subgraph ToxicArchitecture ["TOXIC: Low Cohesion, High Coupling (Spaghetti)"]
    G1["God Class A (50 unrelated functions)"]
    G2["God Class B (Directly alters A's internals)"]
    G1 <-->|"Deep Internal Dependency"| G2
  end
  style IdealArchitecture fill:#064e3b,stroke:#10b981
  style ToxicArchitecture fill:#3f1a1a,stroke:#ef4444"""
                },
                {
                    "type": "interactive",
                    "title": "Architecture Evaluation Challenge",
                    "question": "A developer bundles `calculateTax()`, `printInvoice()`, `hashPassword()`, and `sendSlackAlert()` into a single class named `GeneralUtils`. What describes this class?",
                    "options": [
                        "High functional cohesion.",
                        "Low coincidental cohesion (an antipattern with unrelated responsibilities thrown together).",
                        "High loose coupling.",
                        "Strict adherence to SOLID principles."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nThis class exhibits **Coincidental Cohesion** (the worst level of cohesion). Its methods have no conceptual relationship other than happening to exist in the same utility file. This makes the class unmaintainable and prone to merge conflicts."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Modularity Goal Challenge",
                    "question": "The foundational engineering goal for software modules is high cohesion and _____ coupling.\n\nAnswer: _____",
                    "answer": "Low",
                    "alternatives": ["Low", "low", "Loose", "loose"],
                    "explanation": "**Why Low is Correct:**\n**Low (loose) coupling** ensures that changing the internal implementation of one module causes zero ripple effects in other modules."
                }
            ]
        },
        {
            "title": "Module 2: The 7 Levels of Cohesion (Worst to Best)",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Constantine and Yourdon established a strict hierarchy of 7 cohesion levels, ranging from toxic to ideal."
                },
                {
                    "type": "concept",
                    "title": "Cohesion Hierarchy Spectrum",
                    "content": "1. **Coincidental (Worst):** Elements are grouped arbitrarily (e.g. `MiscUtils.py`).\n2. **Logical:** Elements do similar logical tasks but differ radically in practice (e.g., an `InputHandler` that processes mouse clicks, keyboard strokes, and network packets with giant switch statements).\n3. **Temporal:** Elements are executed at the same time during startup or shutdown (e.g. `initializeSystem()` that sets up databases, seeds random seeds, and loads fonts).\n4. **Procedural:** Elements are grouped because they must execute in a specific order (e.g. `readConfigThenStartServer()`).\n5. **Communicational:** Elements operate on the same input dataset (e.g. a module that takes `EmployeeRecord` and calculates pay, calculates vacation days, and prints their badge).\n6. **Sequential:** The output of one element is the direct input to the next, like an assembly line.\n7. **Functional (Best):** Every element in the module contributes to executing exactly one well-defined single mathematical or domain task (e.g. `SHA256Hasher`, `TrigonometricCalculator`)."
                },
                {
                    "type": "interactive",
                    "title": "Cohesion Classification Challenge",
                    "question": "A module contains functions: `validateCardChecksum()`, `checkCardExpiration()`, and `encryptCVV()`, all operating strictly to verify payment card authenticity. What level of cohesion does this demonstrate?",
                    "options": [
                        "Coincidental Cohesion.",
                        "Temporal Cohesion.",
                        "Functional Cohesion (all elements contribute to a single, well-defined domain task).",
                        "Procedural Cohesion."
                    ],
                    "answer": 2,
                    "explanation": "**Why this is Correct:**\nAll operations in the module are unified around performing one specific business capability: payment card validation. This represents **Functional Cohesion**, the highest and most desirable form of cohesion."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Cohesion Ranking Challenge",
                    "question": "The highest, most desirable level of cohesion in software engineering is _____ cohesion.\n\nAnswer: _____",
                    "answer": "Functional",
                    "alternatives": ["Functional", "functional"],
                    "explanation": "**Why Functional is Correct:**\n**Functional Cohesion** means every part of the module contributes to executing a single, well-defined function or capability."
                }
            ]
        },
        {
            "title": "Module 3: The 5 Levels of Coupling & The Law of Demeter",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Just as cohesion has levels, coupling ranges from destructive to minimal. Furthermore, the **Law of Demeter (LoD)** (the Principle of Least Knowledge) provides a concrete coding rule to prevent train-wreck coupling."
                },
                {
                    "type": "concept",
                    "title": "Coupling Hierarchy (Worst to Best)",
                    "content": "1. **Content Coupling (Worst):** One module directly modifies the private internal memory or variables of another module.\n2. **Common Coupling:** Modules share and mutate global variables or a shared database table without encapsulation.\n3. **Control Coupling:** One module passes a control flag (`doFancyCalculation = True`) that dictates the internal control flow of another module.\n4. **Stamp (Data-Structured) Coupling:** Modules share a complex composite data structure (e.g. passing a 50-field `CustomerRecord` when the function only needs `zip_code`).\n5. **Data Coupling (Best):** Modules communicate strictly by passing minimal primitive atomic parameters (e.g. `computeSalesTax(amount, zip_code)`)."
                },
                {
                    "type": "concept",
                    "title": "The Law of Demeter (LoD)",
                    "content": "A method `m` of class `C` should only invoke methods of:\n- `C` itself\n- Objects passed as parameters to `m`\n- Objects instantiated within `m`\n- Direct instance variables of `C`\n\n**The Antipattern (Train Wreck):** `order.getCustomer().getProfile().getAddress().getZipCode()` violates Demeter; `order` should expose `order.getCustomerZipCode()` directly."
                },
                {
                    "type": "interactive",
                    "title": "Law of Demeter Violation Challenge",
                    "question": "Why is the method call chain `user.getAccount().getBillingDetails().getCard().charge(50)` an architectural antipattern?",
                    "options": [
                        "It executes slower in Python than in C++.",
                        "It tightly couples the caller to 4 levels of internal structural implementation details; if BillingDetails is refactored, the caller breaks.",
                        "It uses too many parenthesis symbols.",
                        "Method chaining is forbidden by the Python compiler."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nThis 'train wreck' violates the **Law of Demeter**. The caller knows far too much about the internal structural hierarchy of `User`. Any restructuring of intermediate classes breaks all callers throughout the entire system."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Coupling Ranking Challenge",
                    "question": "The worst, most dangerous form of coupling, where one module directly modifies the internal private memory of another, is _____ coupling.\n\nAnswer: _____",
                    "answer": "Content",
                    "alternatives": ["Content", "content", "Pathological", "pathological"],
                    "explanation": "**Why Content is Correct:**\n**Content coupling** (also called pathological coupling) completely violates encapsulation, making it impossible to change one module without breaking the other."
                }
            ]
        },
        {
            "title": "Module 4: Robert C. Martin's Package Metrics Lab",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "In *Clean Architecture*, Robert C. Martin formulated mathematical metrics to calculate package modularity: **Afferent Coupling ($C_a$)**, **Efferent Coupling ($C_e$)**, and **Instability ($I$)**."
                },
                {
                    "type": "concept",
                    "title": "The Instability Metric Formula",
                    "content": "$$I = \\frac{C_e}{C_a + C_e}$$\n\nWhere:\n- $C_a$ (Afferent / Incoming Coupling): Number of external classes that depend on this package (who needs me?).\n- $C_e$ (Efferent / Outgoing Coupling): Number of external classes this package depends on (who do I need?).\n- $I = 0.0$ indicates a **Maximally Stable** package (hard to change because many depend on it, like a standard library core).\n- $I = 1.0$ indicates a **Maximally Instable** package (easy to change because nobody depends on it, like a top-level UI controller)."
                },
                {
                    "type": "code_lab",
                    "title": "Package Instability Metric Calculator",
                    "instructions": "Implement `calculate_package_instability(ca, ce)` that computes the Instability metric $I$ and determines whether the package is stable, balanced, or volatile.",
                    "starter_code": """def calculate_package_instability(ca: int, ce: int) -> dict:
    \"\"\"
    Calculate Robert C. Martin's Instability Metric I = Ce / (Ca + Ce).
    
    Returns dict:
      - 'afferent_ca': int
      - 'efferent_ce': int
      - 'instability': float (rounded to 2 decimals)
      - 'stability_category': 'Maximally Stable' (I <= 0.2), 'Balanced' (0.2 < I < 0.8), 'Maximally Instable' (I >= 0.8)
    \"\"\"
    # TODO: Implement instability calculation
    pass
""",
                    "solution_code": """def calculate_package_instability(ca: int, ce: int) -> dict:
    total = ca + ce
    if total == 0:
        return {
            'afferent_ca': 0,
            'efferent_ce': 0,
            'instability': 0.0,
            'stability_category': 'Maximally Stable'
        }
        
    instability = round(ce / total, 2)
    
    if instability <= 0.2:
        cat = 'Maximally Stable'
    elif instability >= 0.8:
        cat = 'Maximally Instable'
    else:
        cat = 'Balanced'
        
    return {
        'afferent_ca': ca,
        'efferent_ce': ce,
        'instability': instability,
        'stability_category': cat
    }
""",
                    "test_code": """# Core domain package: 10 incoming dependencies, 0 outgoing dependencies
res = calculate_package_instability(ca=10, ce=0)
assert res['instability'] == 0.0
assert res['stability_category'] == 'Maximally Stable'

# UI View controller: 0 incoming dependencies, 8 outgoing dependencies
res2 = calculate_package_instability(ca=0, ce=8)
assert res2['instability'] == 1.0
assert res2['stability_category'] == 'Maximally Instable'

# Service layer: 5 incoming, 5 outgoing
res3 = calculate_package_instability(ca=5, ce=5)
assert res3['instability'] == 0.5
assert res3['stability_category'] == 'Balanced'
print("Package Instability Metric tests passed successfully!")
""",
                    "why_works": "**Why This Solution Works:**\nUncle Bob's Stable Dependencies Principle states that dependencies must point in the direction of stability: volatile packages ($I=1.0$) should depend on stable packages ($I=0.0$), never vice versa. This prevents ripple effects from destabilizing foundational core modules.",
                    "alternatives": "**Alternative Approaches & Trade-offs:**\n- **Abstractness Metric ($A$):** Computes the ratio of interfaces/abstract classes to total classes in the package.\n- **Distance from Main Sequence ($D$):** Measures $|A + I - 1|$; values close to 0 represent a healthy balance between abstractness and stability.",
                    "edge_cases": "**Edge Cases & Failure Modes:**\n- `ca = 0, ce = 0`: Package is completely isolated; returns 0.0 without division by zero.\n- Large numbers: Handled with full precision arithmetic."
                }
            ]
        }
    ]
}

# CASE 12: The SOLID Foundations (SOLID Principles)
PART3_CASES["12"] = {
    "title": "Case 12: The SOLID Foundations",
    "episodes": [
        {
            "title": "Module 1: SRP & OCP: The Core Pillars",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Coined by Robert C. Martin ('Uncle Bob') in the early 2000s, the **SOLID** principles are the five foundational commandments of Object-Oriented software design."
                },
                {
                    "type": "objective",
                    "title": "Module Objective",
                    "content": "Master the Single Responsibility Principle (SRP) and Open/Closed Principle (OCP), and refactor brittle monolithic classes into extensible designs."
                },
                {
                    "type": "concept",
                    "title": "SRP and OCP Detailed",
                    "content": "### 1. Single Responsibility Principle (SRP)\n- *'A class should have one, and only one, reason to change.'*\n- A reason to change corresponds to an **actor / stakeholder**. If a class contains business logic for the CFO (payroll calculation), the CTO (database persistence), and the COO (report printing), changes requested by the CFO risk breaking the report printing."
                },
                {
                    "type": "concept",
                    "title": "2. Open/Closed Principle (OCP)",
                    "content": "- *'Software entities should be open for extension, but closed for modification.'*\n- You should be able to introduce a new payment method (e.g. Bitcoin) without modifying existing, tested `CheckoutService` code. This is achieved using polymorphism and strategy interfaces."
                },
                {
                    "type": "visual",
                    "title": "OCP Extensibility via Strategy Interface",
                    "code": """graph TD
  subgraph Client ["Client Business Logic (Closed for Modification)"]
    CHECKOUT["PaymentProcessor.process(PaymentMethod)"]
  end
  subgraph Abstraction ["Abstract Strategy (Open for Extension)"]
    INTERFACE["PaymentMethod Interface: pay(amount)"]
  end
  subgraph ConcreteExtensions ["New Plug-in Adapters (Zero Client Changes!)"]
    CREDIT["CreditCardPayment"]
    PAYPAL["PayPalPayment"]
    CRYPTO["CryptoPayment (Added in v2.0)"]
  end
  CHECKOUT --> INTERFACE
  CREDIT -.->|"Implements"| INTERFACE
  PAYPAL -.->|"Implements"| INTERFACE
  CRYPTO -.->|"Implements"| INTERFACE
  style Client fill:#0f172a,stroke:#3b82f6
  style Abstraction fill:#1e1b4b,stroke:#6366f1
  style ConcreteExtensions fill:#064e3b,stroke:#10b981"""
                },
                {
                    "type": "interactive",
                    "title": "SRP Identification Challenge",
                    "question": "A class `User` has methods: `authenticate()`, `calculateSalary()`, `exportToPDF()`, and `saveToMySQL()`. How many distinct actors/responsibilities does this violate?",
                    "options": [
                        "It violates SRP because it mixes authentication (Security actor), payroll (HR actor), rendering (UI actor), and persistence (DBA actor).",
                        "Zero, because all functions relate to a User.",
                        "It only violates the Open/Closed Principle.",
                        "It adheres to high cohesion."
                    ],
                    "answer": 0,
                    "explanation": "**Why this is Correct:**\n`User` has at least 4 distinct reasons to change: security policies, payroll rules, report formats, and database schema migrations. A change in the MySQL driver should never risk breaking salary calculations."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "SOLID Principle Challenge",
                    "question": "The principle stating that software entities should be open for extension but closed for modification is the _____/Closed Principle.\n\nAnswer: _____",
                    "answer": "Open",
                    "alternatives": ["Open", "open", "Open Closed", "OCP"],
                    "explanation": "**Why Open is Correct:**\nThe **Open/Closed Principle (OCP)** prevents code regressions by enabling new features to be added via new subclasses or strategy plugins rather than editing tested legacy code."
                }
            ]
        },
        {
            "title": "Module 2: Liskov Substitution Principle (LSP)",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Formulated by Turing Award laureate Barbara Liskov in 1987, the **Liskov Substitution Principle (LSP)** governs inheritance subtyping: *'Subtypes must be substitutable for their base types without altering the correctness of the program.'*"
                },
                {
                    "type": "concept",
                    "title": "LSP Rules & The Classic Square-Rectangle Flaw",
                    "content": "### The Square-Rectangle Violation:\nIn mathematics, a Square IS-A Rectangle. But in software:\n```python\nclass Rectangle:\n    def set_width(self, w): self.w = w\n    def set_height(self, h): self.h = h\n    def area(self): return self.w * self.h\n\nclass Square(Rectangle):\n    def set_width(self, w): self.w = self.h = w\n    def set_height(self, h): self.w = self.h = h\n```\nIf a client function assumes `r.set_width(5); r.set_height(4); assert r.area() == 20`, passing a `Square` instance **breaks the assertion** (`area()` returns 16). The subtype altered the behavioral contract of the base class!"
                },
                {
                    "type": "interactive",
                    "title": "LSP Violation Identification Challenge",
                    "question": "A base class `Bird` defines `fly()`. A subclass `Penguin` inherits from `Bird` and overrides `def fly(self): raise NotImplementedError('Penguins cannot fly!')`. Why does this violate LSP?",
                    "options": [
                        "Penguins are birds in biological taxonomy.",
                        "Any client function expecting a Bird will crash with an unexpected exception when passed a Penguin, violating behavioral substitutability.",
                        "Subclasses in Python cannot raise exceptions.",
                        "The fly method should return None instead."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nIf a client accepts `Bird` and calls `b.fly()`, substituting a `Penguin` throws an unexpected exception and crashes the program. The subtype cannot honor the behavioral contract of the supertype. The solution is to model `FlyingBird` vs `FlightlessBird`."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Turing Laureate Challenge",
                    "question": "The computer scientist who formulated the Liskov Substitution Principle is Barbara _____.\n\nAnswer: _____",
                    "answer": "Liskov",
                    "alternatives": ["Liskov", "liskov", "Barbara Liskov"],
                    "explanation": "**Why Barbara Liskov is Correct:**\n**Barbara Liskov** received the ACM Turing Award in 2008 for foundational contributions to programming languages, abstract data types, and distributed computing."
                }
            ]
        },
        {
            "title": "Module 3: ISP & DIP: Interfaces and Inversion",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "The final two principles of SOLID — **Interface Segregation (ISP)** and **Dependency Inversion (DIP)** — govern the architecture of large systems."
                },
                {
                    "type": "concept",
                    "title": "ISP and DIP Detailed",
                    "content": "### 4. Interface Segregation Principle (ISP)\n- *'Clients should not be forced to depend on methods they do not use.'*\n- Avoid fat, bloated interfaces (e.g. `MultiFunctionPrinter` with `print()`, `scan()`, `fax()`, `staple()`). Split into role-specific interfaces (`Printer`, `Scanner`, `Fax`). A basic desk printer only implements `Printer`.\n\n### 5. Dependency Inversion Principle (DIP)\n- *'High-level modules should not depend on low-level modules. Both should depend on abstractions.'*\n- *'Abstractions should not depend on details. Details should depend on abstractions.'*"
                },
                {
                    "type": "visual",
                    "title": "DIP Inverting the Architectural Arrow",
                    "code": """graph TD
  subgraph WithoutDIP ["Direct Tight Coupling (Violates DIP)"]
    HL1["OrderProcessor (High-Level Business Logic)"] -->|"Direct Import"| LL1["MySQLDatabase (Low-Level Driver)"]
  end
  subgraph WithDIP ["Inverted Coupling via Abstraction (Satisfies DIP)"]
    HL2["OrderProcessor (High-Level Logic)"] -->|"Depends On"| INT["DatabaseInterface (Abstract Contract)"]
    LL2["MySQLDatabase (Low-Level Driver)"] -.->|"Implements"| INT
  end
  style WithoutDIP fill:#3f1a1a,stroke:#ef4444
  style WithDIP fill:#064e3b,stroke:#10b981"""
                },
                {
                    "type": "interactive",
                    "title": "Interface Segregation Challenge",
                    "question": "A developer creates an interface `Worker` with methods `code()`, `test()`, `manage()`, and `design()`. A junior programmer implements this class and leaves `manage()` and `design()` throwing `NotImplementedError`. Which principle is violated?",
                    "options": [
                        "Open/Closed Principle.",
                        "Interface Segregation Principle (clients are forced to depend on methods they don't need).",
                        "Single Responsibility Principle.",
                        "None; this is clean design."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nISP mandates thin, role-based interfaces. Forcing a class to implement dummy or throwing methods because the interface is bloated with unrelated capabilities violates the **Interface Segregation Principle**."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "SOLID Acronym Challenge",
                    "question": "In the SOLID acronym, the letter 'D' represents Dependency _____.\n\nAnswer: _____",
                    "answer": "Inversion",
                    "alternatives": ["Inversion", "inversion", "Dependency Inversion"],
                    "explanation": "**Why Inversion is Correct:**\n**Dependency Inversion** 'inverts' traditional procedural dependencies so that concrete implementation details depend on high-level business abstractions."
                }
            ]
        },
        {
            "title": "Module 4: SOLID Refactoring Lab",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Let's refactor a messy violation of OCP and DIP into clean, polymorphic Python code adhering to SOLID principles."
                },
                {
                    "type": "code_lab",
                    "title": "SOLID Notification Dispatcher Lab",
                    "instructions": "Implement `NotificationChannel` (interface) and concrete channels `EmailChannel` and `SMSChannel`. Build `NotificationService` that dispatches alerts to any injected channel list without hardcoding channel types.",
                    "starter_code": """from abc import ABC, abstractmethod

class NotificationChannel(ABC):
    @abstractmethod
    def send(self, recipient: str, message: str) -> bool:
        pass

class EmailChannel(NotificationChannel):
    def send(self, recipient: str, message: str) -> bool:
        # TODO: Implement email sending (return True if '@' in recipient)
        pass

class SMSChannel(NotificationChannel):
    def send(self, recipient: str, message: str) -> bool:
        # TODO: Implement SMS sending (return True if recipient starts with '+')
        pass

class NotificationService:
    \"\"\"Adheres to OCP & DIP: accepts any list of NotificationChannel.\"\"\"
    def __init__(self, channels: list):
        self.channels = channels
        
    def broadcast(self, recipient: str, message: str) -> dict:
        \"\"\"
        Send message across all configured channels.
        Returns dict:
          - 'total_channels': int
          - 'successful_dispatches': int
        \"\"\"
        # TODO: Broadcast message
        pass
""",
                    "solution_code": """from abc import ABC, abstractmethod

class NotificationChannel(ABC):
    @abstractmethod
    def send(self, recipient: str, message: str) -> bool:
        pass

class EmailChannel(NotificationChannel):
    def send(self, recipient: str, message: str) -> bool:
        return '@' in recipient and len(message.strip()) > 0

class SMSChannel(NotificationChannel):
    def send(self, recipient: str, message: str) -> bool:
        return recipient.startswith('+') and len(message.strip()) > 0

class NotificationService:
    def __init__(self, channels: list):
        self.channels = channels
        
    def broadcast(self, recipient: str, message: str) -> dict:
        success = 0
        for channel in self.channels:
            if channel.send(recipient, message):
                success += 1
                
        return {
            'total_channels': len(self.channels),
            'successful_dispatches': success
        }
""",
                    "test_code": """email = EmailChannel()
sms = SMSChannel()

service = NotificationService([email, sms])

# Recipient with both valid email and phone format
res = service.broadcast("user@corp.com", "Server down!")
assert res['total_channels'] == 2
assert res['successful_dispatches'] == 1 # only email passes

res2 = service.broadcast("+123456789", "Server down!")
assert res2['successful_dispatches'] == 1 # only sms passes

print("SOLID Notification tests passed successfully!")
""",
                    "why_works": "**Why This Solution Works:**\n`NotificationService` is open for extension: if we want to add Slack, Discord, or Webhook channels in the future, we write a new `NotificationChannel` subclass and pass it in. We never modify a single line of `NotificationService` code (satisfying OCP and DIP).",
                    "alternatives": "**Alternative Approaches & Trade-offs:**\n- **Chain of Responsibility Pattern:** If notifications should fall back to secondary channels only when the primary channel fails (e.g., try SMS, if fail then email).\n- **Asynchronous Task Queue (Celery):** In high-throughput systems, dispatch channels asynchronously across worker pools.",
                    "edge_cases": "**Edge Cases & Failure Modes:**\n- Empty message: Channels reject empty strings, yielding 0 successful dispatches.\n- Zero channels registered: Returns 0 total and 0 success without errors."
                }
            ]
        }
    ]
}

# CASE 13: The Object Foundry (Creational Design Patterns)
PART3_CASES["13"] = {
    "title": "Case 13: The Object Foundry",
    "episodes": [
        {
            "title": "Module 1: The Gang of Four & Creational Patterns",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "In 1994, Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides published *Design Patterns: Elements of Reusable Object-Oriented Software*. Known as the **Gang of Four (GoF)**, they cataloged 23 classic patterns categorized into Creational, Structural, and Behavioral groups."
                },
                {
                    "type": "objective",
                    "title": "Module Objective",
                    "content": "Master Creational Design Patterns: Factory Method, Abstract Factory, Builder, and thread-safe Singleton, learning when to encapsulate object instantiation."
                },
                {
                    "type": "concept",
                    "title": "Why Encapsulate Creation?",
                    "content": "Directly calling concrete constructors (`car = ElectricCar()`) across client code couples the client to a specific implementation. Creational patterns decouple object creation from object representation, allowing systems to vary what gets created, who creates it, and how it is assembled at runtime."
                },
                {
                    "type": "visual",
                    "title": "Factory Method Architecture",
                    "code": """classDiagram
  class Dialog {
    <<abstract>>
    +render()
    +createButton()* Button
  }
  class WindowsDialog {
    +createButton() Button
  }
  class WebDialog {
    +createButton() Button
  }
  class Button {
    <<interface>>
    +onClick()
  }
  class WindowsButton {
    +onClick()
  }
  class HTMLButton {
    +onClick()
  }

  Dialog <|-- WindowsDialog
  Dialog <|-- WebDialog
  Button <|-- WindowsButton
  Button <|-- HTMLButton
  WindowsDialog ..> WindowsButton : Instantiates
  WebDialog ..> HTMLButton : Instantiates"""
                },
                {
                    "type": "interactive",
                    "title": "Factory Method Intent Challenge",
                    "question": "What is the primary intent of the Factory Method design pattern?",
                    "options": [
                        "To guarantee that a class has only one instance in memory.",
                        "To define an interface for creating an object, but let subclasses decide which class to instantiate.",
                        "To convert the interface of a class into another interface clients expect.",
                        "To execute database SQL queries in parallel."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nThe GoF definition of **Factory Method** is: *'Define an interface for creating an object, but let subclasses decide which class to instantiate. Factory Method lets a class defer instantiation to subclasses.'*"
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "GoF Book Authors Challenge",
                    "question": "The four authors who published the 1994 Design Patterns catalog are collectively known as the Gang of _____.\n\nAnswer: _____",
                    "answer": "Four",
                    "alternatives": ["Four", "four", "GoF", "4"],
                    "explanation": "**Why Four is Correct:**\nThe **Gang of Four (GoF)** cataloged the 23 foundational patterns that shaped modern object-oriented software engineering."
                }
            ]
        },
        {
            "title": "Module 2: Abstract Factory vs. Builder Pattern",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "When dealing with complex object construction, two patterns dominate: **Abstract Factory** (creating families of related products) and **Builder** (step-by-step construction of complex objects)."
                },
                {
                    "type": "concept",
                    "title": "Abstract Factory vs. Builder Comparison",
                    "content": "### Abstract Factory\n- **Intent:** Provide an interface for creating **families of related or dependent objects** without specifying their concrete classes.\n- *Example:* `GUIFactory` creates matching `Button`, `Scrollbar`, and `Window` for DarkMode or LightMode.\n\n### Builder Pattern\n- **Intent:** Separate the construction of a complex object from its representation so that the same construction process can create different representations.\n- *Example:* Constructing an `HttpRequest` with fluent chaining: `.set_method('POST').set_header('Auth', token).set_body(payload).build()`."
                },
                {
                    "type": "interactive",
                    "title": "Pattern Selection Challenge",
                    "question": "You are building a game that must render consistent medieval vs sci-fi assets (if medieval: sword, shield, horse; if sci-fi: laser, energy barrier, hovercraft). Which pattern best guarantees stylistic consistency?",
                    "options": [
                        "Singleton.",
                        "Abstract Factory (ensures products from the same family are always instantiated together).",
                        "Decorator.",
                        "Observer."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\n**Abstract Factory** specializes in enforcing consistency across families of related objects. A `SciFiAssetFactory` will create matching laser weapons, energy shields, and hovercraft, preventing accidental cross-mixing of medieval swords with sci-fi spaceships."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Builder Terminal Method Challenge",
                    "question": "In the Builder design pattern, the final method that validates the assembled parameters and returns the instantiated object is conventionally named _____().\n\nAnswer: _____",
                    "answer": "build",
                    "alternatives": ["build", "Build", "get_result"],
                    "explanation": "**Why build is Correct:**\nThe **build()** method terminates fluent method chaining, executes validation rules, and returns the constructed product."
                }
            ]
        },
        {
            "title": "Module 3: The Singleton Pattern: Antipattern or Tool?",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "The **Singleton Pattern** ensures a class has only one instance and provides a global access point to it. While widely used for hardware drivers and loggers, it is often criticized as an antipattern when misused as a hidden global variable."
                },
                {
                    "type": "concept",
                    "title": "Thread-Safe Singleton Mechanics",
                    "content": "In multi-threaded environments, naive lazy initialization suffers from race conditions: two threads simultaneously check `if instance is None` and instantiate two distinct objects. Production Singletons require **thread locks**."
                },
                {
                    "type": "code_lab",
                    "title": "Thread-Safe Singleton Logger Lab",
                    "instructions": "Implement a thread-safe Singleton `AppLogger` using a class-level threading lock so that all calls to `AppLogger()` return the exact same memory instance.",
                    "starter_code": """import threading

class AppLogger:
    \"\"\"Thread-safe Singleton implementation.\"\"\"
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls, *args, **kwargs):
        # TODO: Implement thread-safe double-checked locking singleton
        pass
        
    def log(self, message: str):
        if not hasattr(self, 'logs'):
            self.logs = []
        self.logs.append(message)
""",
                    "solution_code": """import threading

class AppLogger:
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(AppLogger, cls).__new__(cls)
                    cls._instance.logs = []
        return cls._instance
        
    def log(self, message: str):
        self.logs.append(message)
""",
                    "test_code": """log1 = AppLogger()
log2 = AppLogger()

assert log1 is log2, "Instances must have identical memory identity"
log1.log("System startup initiated")
log2.log("Database connected")

assert len(log1.logs) == 2
assert log1.logs[1] == "Database connected"
print("Thread-Safe Singleton tests passed successfully!")
""",
                    "why_works": "**Why This Solution Works:**\nDouble-Checked Locking checks `_instance is None` before acquiring the lock (avoiding lock contention overhead on every call once initialized), and checks again *inside* the lock to prevent the second thread in a race condition from creating a duplicate instance.",
                    "alternatives": "**Alternative Approaches & Trade-offs:**\n- **Python Module-Level Singleton:** In Python, modules are imported only once per process, making a module-level variable a natural built-in singleton without complex class locking.\n- **Dependency Injection Framework:** Passing a single instance via DI container is much easier to mock in unit tests than a hardcoded Singleton.",
                    "edge_cases": "**Edge Cases & Failure Modes:**\n- Concurrent access during startup: Protected by the threading lock.\n- Unit test isolation: Hard to reset singleton state between unit tests (the primary reason it is criticized as an antipattern)."
                }
            ]
        },
        {
            "title": "Module 4: Fluent Builder Pattern Lab",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Let's build a practical **Fluent Builder** for constructing HTTP requests with validation and immutable results."
                },
                {
                    "type": "code_lab",
                    "title": "Fluent HTTP Request Builder",
                    "instructions": "Implement `HttpRequestBuilder` with methods `set_method()`, `set_url()`, `add_header()`, and `build()`. Raise `ValueError` in `build()` if URL or method are missing.",
                    "starter_code": """class HttpRequest:
    def __init__(self, method: str, url: str, headers: dict):
        self.method = method
        self.url = url
        self.headers = headers

class HttpRequestBuilder:
    def __init__(self):
        self.method = None
        self.url = None
        self.headers = {}
        
    def set_method(self, method: str):
        # TODO: return self for chaining
        pass
        
    def set_url(self, url: str):
        # TODO: return self for chaining
        pass
        
    def add_header(self, key: str, value: str):
        # TODO: return self for chaining
        pass
        
    def build(self) -> HttpRequest:
        # TODO: Validate and return HttpRequest
        pass
""",
                    "solution_code": """class HttpRequest:
    def __init__(self, method: str, url: str, headers: dict):
        self.method = method
        self.url = url
        self.headers = headers

class HttpRequestBuilder:
    def __init__(self):
        self.method = None
        self.url = None
        self.headers = {}
        
    def set_method(self, method: str):
        self.method = method.upper()
        return self
        
    def set_url(self, url: str):
        self.url = url.strip()
        return self
        
    def add_header(self, key: str, value: str):
        self.headers[key] = value
        return self
        
    def build(self) -> HttpRequest:
        if not self.method:
            raise ValueError("HTTP method is required")
        if not self.url or not self.url.startswith("http"):
            raise ValueError("Valid HTTP URL is required")
        return HttpRequest(self.method, self.url, dict(self.headers))
""",
                    "test_code": """builder = HttpRequestBuilder()
req = (builder
       .set_method("post")
       .set_url("https://api.github.com/repos")
       .add_header("Authorization", "Bearer token123")
       .add_header("Accept", "application/json")
       .build())

assert req.method == "POST"
assert req.url == "https://api.github.com/repos"
assert req.headers["Authorization"] == "Bearer token123"

try:
    HttpRequestBuilder().set_method("GET").build()
    assert False, "Should raise ValueError for missing URL"
except ValueError:
    pass

print("Fluent Builder tests passed successfully!")
""",
                    "why_works": "**Why This Solution Works:**\nReturning `self` from every setter enables fluent chaining syntax. Centralizing validation inside `build()` ensures that partially constructed or invalid objects cannot be created.",
                    "alternatives": "**Alternative Approaches & Trade-offs:**\n- **Named Keyword Arguments (`kwargs`):** Feasible in Python, but doesn't provide step-by-step assembly or distinct representations.\n- **Director Class:** GoF includes a `Director` that orchestrates builders to construct standard product configurations (e.g., `Director.create_json_post_request(url)`).",
                    "edge_cases": "**Edge Cases & Failure Modes:**\n- Invalid protocol (e.g. `ftp://`): Fails URL validation.\n- Missing method: Handled with informative `ValueError`."
                }
            ]
        }
    ]
}

# CASE 14: The Structural Bridge (Structural Design Patterns)
PART3_CASES["14"] = {
    "title": "Case 14: The Structural Bridge",
    "episodes": [
        {
            "title": "Module 1: Adapter & Facade Patterns",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Structural design patterns concern how classes and objects are composed to form larger structures. The two most common workhorses for managing interfaces are **Adapter** (translating between incompatible interfaces) and **Facade** (providing a simplified unified interface to a complex subsystem)."
                },
                {
                    "type": "objective",
                    "title": "Module Objective",
                    "content": "Master Structural Design Patterns: Adapter, Facade, Decorator, Composite, and Proxy, applying them to decouple third-party libraries and subsystem boundaries."
                },
                {
                    "type": "concept",
                    "title": "Adapter vs. Facade Comparison",
                    "content": "- **Adapter Pattern (Wrapper):**\n  - *Intent:* Convert the interface of a legacy or third-party class into another interface clients expect. Adapter lets classes work together that couldn't otherwise because of incompatible interfaces.\n  - *Example:* Wrapping a legacy XML payment gateway to satisfy a modern `JSONPaymentGateway` interface.\n- **Facade Pattern:**\n  - *Intent:* Provide a unified, high-level interface to a set of interfaces in a complex subsystem. Facade makes a subsystem easier to use by hiding internal complexity.\n  - *Example:* A `VideoConverterFacade.convert(file, 'mp4')` that internally configures audio codecs, video bitrates, color spaces, and disk buffers."
                },
                {
                    "type": "visual",
                    "title": "Adapter Pattern Architecture",
                    "code": """classDiagram
  class TargetClientInterface {
    <<interface>>
    +request()
  }
  class ConcreteAdapter {
    -adaptee : LegacyService
    +request()
  }
  class LegacyService {
    +specificRequestIncompatible()
  }

  TargetClientInterface <|.. ConcreteAdapter : Implements
  ConcreteAdapter o--> LegacyService : Wraps & Delegates"""
                },
                {
                    "type": "interactive",
                    "title": "Structural Pattern Distinction Challenge",
                    "question": "A library contains 40 complex classes for audio compression, filter synthesis, and buffer streaming. You write a single class `AudioPlayer` with one method `play(file_path)` that coordinates them. What pattern did you implement?",
                    "options": [
                        "Adapter Pattern.",
                        "Facade Pattern (provides a simple unified interface to a complex subsystem).",
                        "Singleton Pattern.",
                        "Abstract Factory."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\n**Facade** does not adapt an incompatible interface to match an existing contract; rather, it invents a **new, simplified high-level interface** to hide the daunting complexity of a multi-class subsystem."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Pattern Synonym Challenge",
                    "question": "The Adapter design pattern is also colloquially and descriptively known as a _____.\n\nAnswer: _____",
                    "answer": "Wrapper",
                    "alternatives": ["Wrapper", "wrapper"],
                    "explanation": "**Why Wrapper is Correct:**\nAn **Adapter (Wrapper)** wraps an existing object and translates calls to its internal methods."
                }
            ]
        },
        {
            "title": "Module 2: The Decorator Pattern",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Inheritance is static: once you subclass `EncryptedCompressedFileWriter`, you are locked in at compile time. What if you want to dynamically wrap an object with compression, encryption, and logging in any arbitrary order at runtime? Enter the **Decorator Pattern**."
                },
                {
                    "type": "concept",
                    "title": "Decorator Mechanics",
                    "content": "- **Intent:** Attach additional responsibilities to an object **dynamically**. Decorators provide a flexible alternative to subclassing for extending functionality.\n- **Key Architectural Rule:** The Decorator implements the SAME interface as the component it wraps, and maintains a reference to a component instance.\n- *Example:* Java's classic `new BufferedReader(new InputStreamReader(new FileInputStream('data.txt')))`."
                },
                {
                    "type": "visual",
                    "title": "Decorator Onion Wrapping",
                    "code": """graph LR
  subgraph Pipeline ["Dynamic Wrapping Pipeline"]
    CALLER["Client Calls: write(data)"] --> DEC_LOG["LoggingDecorator"]
    DEC_LOG --> DEC_ENC["EncryptionDecorator"]
    DEC_ENC --> DEC_COMP["CompressionDecorator"]
    DEC_COMP --> BASE["BaseFileWriter (Writes to Disk)"]
  end
  style Pipeline fill:#1e1b4b,stroke:#6366f1
  style BASE fill:#064e3b,stroke:#10b981"""
                },
                {
                    "type": "interactive",
                    "title": "Decorator vs. Subclassing Challenge",
                    "question": "Why is the Decorator pattern preferred over creating a deep class inheritance hierarchy when features can be combined in many permutations?",
                    "options": [
                        "Subclassing leads to an exponential class explosion (e.g. 10 features would require hundreds of subclasses for every combination), while Decorator composes them dynamically at runtime.",
                        "Subclassing is not supported in modern programming languages.",
                        "Decorators eliminate all object instantiation.",
                        "Decorators make the code run faster by bypassing CPU registers."
                    ],
                    "answer": 0,
                    "explanation": "**Why this is Correct:**\nCombining $N$ independent features via inheritance requires $2^N$ combinatorial subclasses (`EncryptedLoggedStream`, `CompressedLoggedStream`, etc.). With Decorators, you need only $N$ small decorator classes that can be nested in any combination at runtime."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "OO Principle Challenge",
                    "question": "The foundational object-oriented design maxim underlying the Decorator pattern is: Favor Object Composition over Class _____.\n\nAnswer: _____",
                    "answer": "Inheritance",
                    "alternatives": ["Inheritance", "inheritance"],
                    "explanation": "**Why Inheritance is Correct:**\n**Favoring composition over inheritance** provides runtime flexibility, loose coupling, and eliminates rigid compile-time inheritance hierarchies."
                }
            ]
        },
        {
            "title": "Module 3: Composite and Proxy Patterns",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "To complete the structural toolbox, we examine **Composite** (treating individual objects and compositions of objects uniformly) and **Proxy** (controlling access to another object)."
                },
                {
                    "type": "concept",
                    "title": "Composite and Proxy Detailed",
                    "content": "### Composite Pattern\n- **Intent:** Compose objects into tree structures to represent part-whole hierarchies. Composite lets clients treat individual objects and compositions of objects uniformly.\n- *Example:* In a file system, both a `File` (leaf) and a `Directory` (composite) implement `FileSystemNode.get_size()`.\n\n### Proxy Pattern\n- **Intent:** Provide a surrogate or placeholder for another object to control access to it.\n- *Types of Proxies:*\n  1. **Virtual Proxy:** Lazy-loads heavy resources (e.g. loading a 50MB image only when scrolled into view).\n  2. **Protection Proxy:** Enforces role-based permissions before delegating.\n  3. **Remote Proxy:** Marshals RPC/gRPC calls over the network."
                },
                {
                    "type": "interactive",
                    "title": "Proxy Pattern Use Case Challenge",
                    "question": "An image gallery displays 1,000 photos. Instead of downloading all gigabytes of high-res image files immediately, you display lightweight placeholder objects that fetch the actual high-res data only when requested. What pattern is this?",
                    "options": [
                        "Virtual Proxy.",
                        "Flyweight.",
                        "Adapter.",
                        "State."
                    ],
                    "answer": 0,
                    "explanation": "**Why this is Correct:**\nA **Virtual Proxy** delays the instantiation and network/memory loading of an expensive, heavy resource until the exact moment it is accessed."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Composite Structure Challenge",
                    "question": "The Composite pattern organizes objects into a recursive _____ data structure so clients can treat leaves and containers identically.\n\nAnswer: _____",
                    "answer": "Tree",
                    "alternatives": ["Tree", "tree", "Hierarchy"],
                    "explanation": "**Why Tree is Correct:**\n**Tree** structures allow composite nodes to contain both leaf elements and other composite subtrees."
                }
            ]
        },
        {
            "title": "Module 4: Practical Decorator Pipeline Lab",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Let's build a practical text processing pipeline using the **Decorator Pattern** to apply formatting, encryption, and HTML wrapping dynamically."
                },
                {
                    "type": "code_lab",
                    "title": "Dynamic Text Decorator Pipeline",
                    "instructions": "Implement `TextComponent` (base interface with `render()`), `PlainText`, and decorators `UpperCaseDecorator` and `HTMLEmphasisDecorator`. Demonstrate nesting multiple decorators.",
                    "starter_code": """from abc import ABC, abstractmethod

class TextComponent(ABC):
    @abstractmethod
    def render(self) -> str:
        pass

class PlainText(TextComponent):
    def __init__(self, text: str):
        self.text = text
        
    def render(self) -> str:
        return self.text

class UpperCaseDecorator(TextComponent):
    def __init__(self, wrapped: TextComponent):
        self.wrapped = wrapped
        
    def render(self) -> str:
        # TODO: Transform wrapped render to UPPERCASE
        pass

class HTMLEmphasisDecorator(TextComponent):
    def __init__(self, wrapped: TextComponent):
        self.wrapped = wrapped
        
    def render(self) -> str:
        # TODO: Wrap wrapped render in <em>...</em> tags
        pass
""",
                    "solution_code": """from abc import ABC, abstractmethod

class TextComponent(ABC):
    @abstractmethod
    def render(self) -> str:
        pass

class PlainText(TextComponent):
    def __init__(self, text: str):
        self.text = text
        
    def render(self) -> str:
        return self.text

class UpperCaseDecorator(TextComponent):
    def __init__(self, wrapped: TextComponent):
        self.wrapped = wrapped
        
    def render(self) -> str:
        return self.wrapped.render().upper()

class HTMLEmphasisDecorator(TextComponent):
    def __init__(self, wrapped: TextComponent):
        self.wrapped = wrapped
        
    def render(self) -> str:
        return f"<em>{self.wrapped.render()}</em>"
""",
                    "test_code": """raw = PlainText("software engineering")
assert raw.render() == "software engineering"

upper = UpperCaseDecorator(raw)
assert upper.render() == "SOFTWARE ENGINEERING"

# Nesting: first uppercase, then wrap in HTML emphasis
nested = HTMLEmphasisDecorator(upper)
assert nested.render() == "<em>SOFTWARE ENGINEERING</em>"

# Reverse nesting order: first HTML emphasis, then uppercase
reverse_nested = UpperCaseDecorator(HTMLEmphasisDecorator(raw))
assert reverse_nested.render() == "<EM>SOFTWARE ENGINEERING</EM>"

print("Decorator Pipeline tests passed successfully!")
""",
                    "why_works": "**Why This Solution Works:**\nBecause `UpperCaseDecorator` and `HTMLEmphasisDecorator` both implement `TextComponent`, they can wrap any other component or decorator seamlessly. The order of execution depends strictly on the wrapping nesting order, providing infinite runtime permutations.",
                    "alternatives": "**Alternative Approaches & Trade-offs:**\n- **Python `@decorator` Functions:** Idiomatic for decorating function calls, but classic GoF object decorators allow dynamic state mutation and swapping of wrapped components at runtime.\n- **Pipeline / Middleware Pattern:** Used in web frameworks (FastAPI/Express) to process requests in a linear array.",
                    "edge_cases": "**Edge Cases & Failure Modes:**\n- Empty string: Properly processed through transformations without exceptions.\n- Deep nesting: Python handles recursion and delegation smoothly."
                }
            ]
        }
    ]
}

print(f"Loaded {len(PART3_CASES)} cases for Part 3 (Cases 10-14).")

with open('/Users/aadarshamahato/Downloads/LEARNING_PLATFORM/se_story_lab/cases_part3.json', 'w', encoding='utf-8') as f:
    json.dump(PART3_CASES, f, indent=4)
