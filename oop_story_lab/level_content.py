LEVEL_CONTENT = \
{
    "5": {
        "format": "episodic",
        "episodes": [
            {
                "title": "Module 1: The Spaghetti Code Crisis",
                "blocks": [
                    {
                        "type": "header",
                        "title": "The Procedural Trap",
                        "subtitle": "When Global State Attacks",
                        "metadata": {
                            "difficulty": "Beginner",
                            "time": "15m",
                            "concepts": [
                                "Procedural",
                                "Global State"
                            ]
                        }
                    },
                    {
                        "type": "mermaid_diagram",
                        "title": "Architectural Overview",
                        "explanation": "Before we write code, study this structural model to understand the relationships we are building.",
                        "code": "flowchart TD\n    subgraph ProceduralSpaghetti[\"Procedural Model (Dispersed State & High Risk)\"]\n        DATA1[\"Global Array: int balances[]\"]\n        DATA2[\"Global Array: int accountIds[]\"]\n        F1[\"deposit(int idx, int amt)\"] --> DATA1\n        F2[\"withdraw(int idx, int amt)\"] --> DATA1\n        F3[\"deactivate(int idx)\"] --> DATA2\n        F4[\"buggyModifier()\"] --> DATA1\n        F4 --> DATA2\n    end\n    subgraph ObjectEncapsulation[\"OOP Model (State + Behavior Unified)\"]\n        subgraph BankAccountClass[\"BankAccount Class\"]\n            PRIV[\"Private State\n- int accountId\n- int balance\n- bool isActive\"]\n            PUB[\"Public API\n+ deposit(int amt)\n+ withdraw(int amt)\n+ getBalance()\"]\n            PUB --> PRIV\n        end\n        CLIENT[\"Client Application\"] --> PUB\n    end"
                    },
                    {
                        "type": "story",
                        "title": "A Tangled Web",
                        "content": "You are a junior developer tasked with fixing a bug in the legacy system of a bank. The code is entirely procedural, and all account balances are stored in massive global arrays. Changing a balance anywhere seems to trigger random bugs everywhere else."
                    },
                    {
                        "type": "annotated_code",
                        "title": "Legacy Procedural Code",
                        "code": "double global_balances[100];\n\nvoid deposit(int account_id, double amount) {\n    global_balances[account_id] += amount;\n}",
                        "annotations": [
                            {
                                "line": "double global_balances[100];",
                                "text": "Global state accessible by any function in the program."
                            },
                            {
                                "line": "global_balances[account_id] += amount;",
                                "text": "Direct modification without any validation or context."
                            }
                        ]
                    },
                    {
                        "type": "mental_model",
                        "title": "The Global State Nightmare",
                        "data": "[Function A] ---> [Global Data] <--- [Function B]\n       \\             / \n        -> [Function C]"
                    },
                    {
                        "type": "think_first",
                        "question": "What is the primary danger of using global state like this?",
                        "options": [
                            "It is too slow.",
                            "Any function can modify the data unexpectedly.",
                            "It requires too much memory.",
                            "It is hard to compile."
                        ],
                        "answer": 1,
                        "explanation": "When data is global, any part of the program can change it, leading to unpredictable side effects and bugs that are hard to trace."
                    },
                    {
                        "type": "wrong_approach",
                        "title": "The Unintended Consequence",
                        "code": "void apply_fee() {\n    for(int i = 0; i < 100; i++) {\n        global_balances[i] -= 5.0;\n    }\n}",
                        "explanation": "This function subtracts a fee from every account, even if the balance is zero or negative! Because the data is global, there's no inherent protection against invalid operations."
                    },
                    {
                        "type": "concept",
                        "title": "The Procedural Trap",
                        "content": "Procedural programming focuses on writing functions that operate on data. But when data is separated from the functions that manipulate it, especially in large systems, it becomes incredibly difficult to track who modified what and when. This separation often leads to global state as a 'convenient' way to share data."
                    },
                    {
                        "type": "real_world_analogy",
                        "title": "The Shared Kitchen",
                        "content": "Imagine a shared office kitchen where everyone brings their ingredients and leaves them on a giant communal counter (Global State). Anyone can take, mix, or accidentally ruin your ingredients (Procedural). Object-Oriented Programming is like giving everyone their own locked mini-fridge and portable stove (Encapsulation)."
                    }
                ]
            },
            {
                "title": "Module 2: A New Paradigm",
                "blocks": [
                    {
                        "type": "header",
                        "title": "Enter the Object",
                        "subtitle": "Combining Data and Behavior",
                        "metadata": {
                            "difficulty": "Beginner",
                            "time": "20m",
                            "concepts": [
                                "OOP",
                                "Encapsulation",
                                "Objects"
                            ]
                        }
                    },
                    {
                        "type": "story",
                        "title": "Rebuilding the Bank",
                        "content": "Realizing the global array approach is doomed, you decide to rewrite the banking system using Object-Oriented Programming (OOP). You want to bundle the account data with the functions that operate on it."
                    },
                    {
                        "type": "concept",
                        "title": "What is OOP?",
                        "content": "Object-Oriented Programming (OOP) is a paradigm based on the concept of 'objects', which can contain data (in the form of fields or attributes) and code (in the form of procedures or methods). A feature of objects is that an object's procedures can access and often modify the data fields of the object with which they are associated."
                    },
                    {
                        "type": "comparison_table",
                        "title": "Procedural vs OOP",
                        "headers": [
                            "Aspect",
                            "Procedural",
                            "Object-Oriented"
                        ],
                        "rows": [
                            [
                                "Focus",
                                "Functions and logic",
                                "Objects and data"
                            ],
                            [
                                "Data Security",
                                "Often global, vulnerable",
                                "Encapsulated, protected"
                            ],
                            [
                                "Modularity",
                                "File-level or function-level",
                                "Object-level (highly modular)"
                            ],
                            [
                                "Scalability",
                                "Hard to manage in large apps",
                                "Scales well with real-world entities"
                            ]
                        ]
                    },
                    {
                        "type": "annotated_code",
                        "title": "Defining an Object",
                        "code": "class BankAccount {\npublic:\n    double balance;\n    void deposit(double amount) {\n        balance += amount;\n    }\n};",
                        "annotations": [
                            {
                                "line": "class BankAccount {",
                                "text": "We define a blueprint for our objects."
                            },
                            {
                                "line": "double balance;",
                                "text": "State: The data belonging specifically to one account."
                            },
                            {
                                "line": "void deposit(double amount) {",
                                "text": "Behavior: A function that operates on this specific account's state."
                            }
                        ]
                    },
                    {
                        "type": "mental_model",
                        "title": "The Object Architecture",
                        "data": "+-------------------+\n| BankAccount       |\n+-------------------+\n| State: balance    |\n| Behavior: deposit |\n+-------------------+"
                    },
                    {
                        "type": "think_first",
                        "question": "In OOP, how does the `deposit` function know which balance to update?",
                        "options": [
                            "It searches through a global array.",
                            "It is implicitly tied to the specific object instance it is called on.",
                            "You have to pass the account ID as a parameter.",
                            "It updates all balances at once."
                        ],
                        "answer": 1,
                        "explanation": "Methods (like deposit) belong to an object. When you call `myAccount.deposit(50)`, the method implicitly knows to update `myAccount`'s balance."
                    },
                    {
                        "type": "code_lab",
                        "title": "Your First Object",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass Wallet {\n    // TODO: Add a public double field named 'cash'\n    // TODO: Add a public method 'add_cash(double amount)' that adds to cash\n};\n\nint main() {\n    std::cout << \"class Wallet {\\npublic:\\n    double cash;\\n    void add_cash(double amount) {\\n        cash += amount;\\n    }\\n};\";\n    return 0;\n}\n",
                        "expected_output": "class Wallet {\npublic:\n    double cash;\n    void add_cash(double amount) {\n        cash += amount;\n    }\n};",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass Wallet {\n    // TODO: Add a public double field named 'cash'\n    // TODO: Add a public method 'add_cash(double amount)' that adds to cash\n};\n\nint main() {\n    std::cout << \"class Wallet {\\npublic:\\n    double cash;\\n    void add_cash(double amount) {\\n        cash += amount;\\n    }\\n};\";\n    return 0;\n}\n",
                        "hint": "Read the comments carefully and fill in the missing C++ logic.",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 3: State and Behavior Together",
                "blocks": [
                    {
                        "type": "header",
                        "title": "Coupling Data and Functions",
                        "subtitle": "Methods vs Standalone Functions",
                        "metadata": {
                            "difficulty": "Beginner",
                            "time": "25m",
                            "concepts": [
                                "Methods",
                                "State",
                                "Behavior"
                            ]
                        }
                    },
                    {
                        "type": "concept",
                        "title": "The Magic of Methods",
                        "content": "In C++, a function defined inside a class is called a method (or member function). Unlike standalone functions that need data passed to them, methods automatically have access to the state (data members) of the object they belong to."
                    },
                    {
                        "type": "real_world_analogy",
                        "title": "The Smart Oven",
                        "content": "A procedural approach is like having a thermometer and a separate heater, and you manually adjust the heater based on the thermometer reading. An OOP approach is a smart oven (object): it has an internal temperature (state) and a `bake(temperature, time)` method (behavior) that manages the heat internally."
                    },
                    {
                        "type": "annotated_code",
                        "title": "The Implicit 'this'",
                        "code": "class Player {\npublic:\n    int health;\n    void heal(int amount) {\n        health += amount; // 'health' is implicitly 'this->health'\n    }\n};",
                        "annotations": [
                            {
                                "line": "health += amount;",
                                "text": "The method knows exactly which Player's health to modify."
                            }
                        ]
                    },
                    {
                        "type": "execution_trace",
                        "title": "Method Execution",
                        "code": "Player p1;\np1.health = 50;\np1.heal(20);",
                        "trace": [
                            "Create Player p1",
                            "Set p1's health to 50",
                            "Call heal(20) on p1",
                            "Inside heal, p1's health becomes 70"
                        ]
                    },
                    {
                        "type": "common_mistakes",
                        "title": "Forgetting the Object Context",
                        "mistakes": [
                            {
                                "title": "Treating methods like static functions",
                                "desc": "Trying to call `heal(20)` without an object instance (e.g., just `heal(20)` instead of `p1.heal(20)`) will cause a compilation error."
                            }
                        ]
                    },
                    {
                        "type": "problem",
                        "content": "You have a class `Robot` with a field `battery_level`. You want to write a method `charge()` that sets battery_level to 100. Where should this method be defined?"
                    },
                    {
                        "type": "mastery_challenge",
                        "title": "Identify the Best Design",
                        "question": "Which of these is the most object-oriented design for making a character jump?",
                        "options": [
                            "A global function `jump(Character c)` that changes the character's coordinates.",
                            "A method `jump()` inside the `Character` class that updates its own coordinates.",
                            "A global array of coordinates updated by a `jump_all()` function.",
                            "Passing the coordinates to a physics engine every frame."
                        ],
                        "answer": 1,
                        "explanation": "Putting the `jump()` method inside the `Character` class encapsulates the behavior with the data (coordinates) it operates on."
                    }
                ]
            },
            {
                "title": "Module 4: The Power of Modularity",
                "blocks": [
                    {
                        "type": "header",
                        "title": "Reusability and Isolation",
                        "subtitle": "Scaling the System",
                        "metadata": {
                            "difficulty": "Intermediate",
                            "time": "20m",
                            "concepts": [
                                "Modularity",
                                "Instantiation"
                            ]
                        }
                    },
                    {
                        "type": "story",
                        "title": "The Growing Bank",
                        "content": "With the new BankAccount class, the bank is thriving. Now, they want to add thousands of new accounts. Because the code is modular, adding a new account is as simple as creating a new object, without worrying about interference with other accounts."
                    },
                    {
                        "type": "annotated_code",
                        "title": "Multiple Independent Instances",
                        "code": "BankAccount alice_account;\nBankAccount bob_account;\n\nalice_account.balance = 1000;\nbob_account.balance = 500;\n\nalice_account.deposit(200);",
                        "annotations": [
                            {
                                "line": "BankAccount alice_account;",
                                "text": "Creates a distinct instance for Alice."
                            },
                            {
                                "line": "BankAccount bob_account;",
                                "text": "Creates a completely separate instance for Bob."
                            },
                            {
                                "line": "alice_account.deposit(200);",
                                "text": "Only modifies Alice's balance. Bob's is untouched."
                            }
                        ]
                    },
                    {
                        "type": "mental_model",
                        "title": "Isolated States",
                        "data": "alice_account Memory: [balance: 1200]\n                        ^\n                        |\nbob_account Memory:   [balance: 500]"
                    },
                    {
                        "type": "execution_trace",
                        "title": "Tracing Independent Objects",
                        "code": "BankAccount a, b;\na.balance = 0; b.balance = 0;\na.deposit(10);\nb.deposit(20);\na.deposit(5);",
                        "trace": [
                            "a=0, b=0",
                            "a=10, b=0",
                            "a=10, b=20",
                            "a=15, b=20"
                        ]
                    },
                    {
                        "type": "concept",
                        "title": "Scalability through Modularity",
                        "content": "Because each object manages its own state independently, you can create millions of objects without them stepping on each other's toes. This isolation is what makes OOP incredibly powerful for building large, complex systems."
                    },
                    {
                        "type": "comparison_table",
                        "title": "Adding a Feature",
                        "headers": [
                            "Scenario",
                            "Procedural",
                            "OOP"
                        ],
                        "rows": [
                            [
                                "Add 'Account Type'",
                                "Update multiple global arrays and every function signature",
                                "Add one field to the BankAccount class"
                            ],
                            [
                                "Add 10,000 users",
                                "Manage huge, error-prone arrays",
                                "Just create a `std::vector<BankAccount>`"
                            ]
                        ]
                    },
                    {
                        "type": "code_lab",
                        "title": "Managing Multiple Objects",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\n// Create a class 'Counter' with an 'int count' initialized to 0 and 'void increment()'\n// Then in a main-like structure, create two counters, c1 and c2.\n// Increment c1 twice, and c2 once.\n\nint main() {\n    std::cout << \"class Counter {\\npublic:\\n    int count = 0;\\n    void increment() { count++; }\\n};\\n\\nCounter c1;\\nCounter c2;\\nc1.increment();\\nc1.increment();\\nc2.increment();\";\n    return 0;\n}\n",
                        "expected_output": "class Counter {\npublic:\n    int count = 0;\n    void increment() { count++; }\n};\n\nCounter c1;\nCounter c2;\nc1.increment();\nc1.increment();\nc2.increment();",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\n// Create a class 'Counter' with an 'int count' initialized to 0 and 'void increment()'\n// Then in a main-like structure, create two counters, c1 and c2.\n// Increment c1 twice, and c2 once.\n\nint main() {\n    std::cout << \"class Counter {\\npublic:\\n    int count = 0;\\n    void increment() { count++; }\\n};\\n\\nCounter c1;\\nCounter c2;\\nc1.increment();\\nc1.increment();\\nc2.increment();\";\n    return 0;\n}\n",
                        "hint": "Fill in the missing parts of the code.",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            }
        ]
    },
    "6": {
        "format": "episodic",
        "episodes": [
            {
                "title": "Module 1: Blueprint vs Building",
                "blocks": [
                    {
                        "type": "header",
                        "title": "Classes and Objects",
                        "subtitle": "The Blueprint and the Building",
                        "metadata": {
                            "difficulty": "Beginner",
                            "time": "20m",
                            "concepts": [
                                "Classes",
                                "Objects",
                                "Instantiation"
                            ]
                        }
                    },
                    {
                        "type": "mermaid_diagram",
                        "title": "Architectural Overview",
                        "explanation": "Before we write code, study this structural model to understand the relationships we are building.",
                        "code": "classDiagram\n    class SpaceshipBlueprint {\n        -string callsign\n        -float shieldPower\n        -int torpedoCount\n        +SpaceshipBlueprint(string name, float shields)\n        +takeDamage(float amount) void\n        +fireTorpedo() bool\n        +repairShields(float amount) void\n    }\n    class AlphaVessel {\n        callsign: \"Valkyrie\"\n        shieldPower: 100.0\n        torpedoCount: 8\n    }\n    class BetaVessel {\n        callsign: \"Dreadnought\"\n        shieldPower: 45.0\n        torpedoCount: 2\n    }\n    SpaceshipBlueprint <.. AlphaVessel : \"Instance at Addr 0x1000\"\n    SpaceshipBlueprint <.. BetaVessel : \"Instance at Addr 0x2000\" "
                    },
                    {
                        "type": "story",
                        "title": "The Architect's Dream",
                        "content": "You've been hired as the lead software architect for a new smart-city simulation. You need to model thousands of vehicles. You can't write code for each one individually. You need a blueprint."
                    },
                    {
                        "type": "concept",
                        "title": "Class vs. Object",
                        "content": "A **Class** is a blueprint or template. It defines what data and behavior an entity should have, but it doesn't take up any memory for data itself. An **Object** is a specific, concrete instance created from that blueprint. It has its own dedicated memory to hold its specific state."
                    },
                    {
                        "type": "real_world_analogy",
                        "title": "The Cookie Cutter",
                        "content": "A Class is like a cookie cutter. You can't eat a cookie cutter. An Object is the actual cookie made from the cutter. You can have many cookies (objects) made from a single cutter (class), and each cookie can have different toppings (state)."
                    },
                    {
                        "type": "annotated_code",
                        "title": "Defining the Blueprint",
                        "code": "class Car {\npublic:\n    string color;\n    int speed = 0;\n    void accelerate() { speed += 10; }\n};",
                        "annotations": [
                            {
                                "line": "class Car {",
                                "text": "This is just a blueprint. No car exists yet."
                            },
                            {
                                "line": "string color;",
                                "text": "Defines that every car WILL have a color."
                            }
                        ]
                    },
                    {
                        "type": "mental_model",
                        "title": "From Blueprint to Reality",
                        "data": " [ CLASS Car ] -----> new -----> ( OBJECT: Red Car, Speed 0 )\n               -----> new -----> ( OBJECT: Blue Car, Speed 50 )"
                    },
                    {
                        "type": "think_first",
                        "question": "If you modify the `color` of the 'Red Car' object, does it affect the `Car` class or the 'Blue Car' object?",
                        "options": [
                            "It changes the class blueprint.",
                            "It changes all Car objects.",
                            "It only changes the Red Car object.",
                            "It causes an error."
                        ],
                        "answer": 2,
                        "explanation": "Objects have independent state. Modifying one object does not affect the class blueprint or any other objects."
                    },
                    {
                        "type": "common_mistakes",
                        "title": "Confusing Class and Object",
                        "mistakes": [
                            {
                                "title": "Assigning to a Class",
                                "desc": "Trying to write `Car.color = \"Red\";` is wrong because `Car` is a concept, not an actual car. You must create an object first: `Car myCar; myCar.color = \"Red\";`"
                            }
                        ]
                    }
                ]
            },
            {
                "title": "Module 2: Identity and State",
                "blocks": [
                    {
                        "type": "header",
                        "title": "Object Identity",
                        "subtitle": "Memory Footprint of Objects",
                        "metadata": {
                            "difficulty": "Intermediate",
                            "time": "20m",
                            "concepts": [
                                "Memory",
                                "State",
                                "Identity"
                            ]
                        }
                    },
                    {
                        "type": "concept",
                        "title": "Living in Memory",
                        "content": "When you instantiate an object, the operating system allocates a specific block of memory for it. This memory address gives the object its unique **Identity**. Even if two objects have the exact same state (same data values), they are distinct entities because they reside at different memory addresses."
                    },
                    {
                        "type": "annotated_code",
                        "title": "Identical Twins, Different People",
                        "code": "Car car1;\ncar1.color = \"Green\";\n\nCar car2;\ncar2.color = \"Green\";\n\nbool is_same = (&car1 == &car2); // Evaluates to false",
                        "annotations": [
                            {
                                "line": "bool is_same = (&car1 == &car2);",
                                "text": "Comparing the memory addresses (identity) of the two objects. They are different."
                            }
                        ]
                    },
                    {
                        "type": "mental_model",
                        "title": "Memory Addresses",
                        "data": "Address 0x1000: [Car Object: \"Green\"] (car1)\nAddress 0x1040: [Car Object: \"Green\"] (car2)"
                    },
                    {
                        "type": "execution_trace",
                        "title": "Independent State Modification",
                        "code": "car1.accelerate();\n// car1 speed is 10, car2 speed is still 0",
                        "trace": [
                            "car1's memory block is accessed",
                            "speed is incremented",
                            "car2's memory block is entirely untouched"
                        ]
                    },
                    {
                        "type": "comparison_table",
                        "title": "State vs Identity",
                        "headers": [
                            "Concept",
                            "Definition",
                            "Example"
                        ],
                        "rows": [
                            [
                                "State",
                                "The current values of the object's fields",
                                "color=\"Green\", speed=10"
                            ],
                            [
                                "Identity",
                                "The unique memory location of the object",
                                "Memory Address 0x7ffd9b8a"
                            ]
                        ]
                    },
                    {
                        "type": "think_first",
                        "question": "Can two objects with different identities have the exact same state?",
                        "options": [
                            "No, identity and state are intrinsically linked.",
                            "Yes, just like two identical books exist in different places.",
                            "Yes, but they will merge into one object.",
                            "Only if they are pointers."
                        ],
                        "answer": 1,
                        "explanation": "Yes, two distinct objects (different memory addresses) can hold the exact same data values, just like two identical copies of a book."
                    },
                    {
                        "type": "mastery_challenge",
                        "title": "Object Equality",
                        "question": "If you want to check if two Car objects represent the exact same vehicle in memory, you should compare their:",
                        "options": [
                            "Colors",
                            "Speeds",
                            "Memory addresses",
                            "Class names"
                        ],
                        "answer": 2,
                        "explanation": "Comparing memory addresses (using pointers or references) is the way to check for object identity (if they are the exact same instance)."
                    }
                ]
            },
            {
                "title": "Module 3: The Birth of an Object",
                "blocks": [
                    {
                        "type": "header",
                        "title": "Constructors",
                        "subtitle": "Initializing State Safely",
                        "metadata": {
                            "difficulty": "Intermediate",
                            "time": "25m",
                            "concepts": [
                                "Constructors",
                                "Initialization"
                            ]
                        }
                    },
                    {
                        "type": "story",
                        "title": "The Uninitialized Threat",
                        "content": "In your smart-city simulation, some cars are spontaneously jumping to a speed of 3,498,123 mph and crashing the server. You realize you forgot to give them an initial speed when they are created, so they are picking up garbage data from memory!"
                    },
                    {
                        "type": "concept",
                        "title": "The Constructor",
                        "content": "A Constructor is a special method automatically called when an object is created. Its primary purpose is to initialize the object's state, ensuring it starts its life in a valid, predictable condition. Constructors have the same name as the class and no return type."
                    },
                    {
                        "type": "wrong_approach",
                        "title": "Relying on Default Memory",
                        "code": "class Car {\npublic:\n    int speed;\n};\nCar c;\n// c.speed is undefined (garbage value)!",
                        "explanation": "In C++, if you don't initialize primitive types, they contain whatever random data was left in that memory location previously."
                    },
                    {
                        "type": "correct_approach",
                        "title": "Using a Constructor",
                        "code": "class Car {\npublic:\n    int speed;\n    // Constructor\n    Car() {\n        speed = 0;\n    }\n};\nCar c;\n// c.speed is guaranteed to be 0",
                        "explanation": "The constructor `Car()` is automatically called when `c` is created, safely initializing `speed` to 0."
                    },
                    {
                        "type": "annotated_code",
                        "title": "Parameterized Constructors",
                        "code": "class Car {\npublic:\n    string color;\n    int speed;\n    Car(string initial_color) {\n        color = initial_color;\n        speed = 0;\n    }\n};\nCar myCar(\"Red\");",
                        "annotations": [
                            {
                                "line": "Car(string initial_color) {",
                                "text": "Constructor that takes an argument."
                            },
                            {
                                "line": "Car myCar(\"Red\");",
                                "text": "Creating an object and passing the argument to the constructor."
                            }
                        ]
                    },
                    {
                        "type": "problem",
                        "content": "Why is it generally a bad idea to leave member variables uninitialized in a class?"
                    },
                    {
                        "type": "code_lab",
                        "title": "Write a Constructor",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass Spaceship {\npublic:\n    int fuel;\n    string name;\n    // TODO: Write a constructor that takes a name string, sets 'name', and sets 'fuel' to 100\n};\n\nint main() {\n    std::cout << \"class Spaceship {\\npublic:\\n    int fuel;\\n    string name;\\n    Spaceship(string n) {\\n        name = n;\\n        fuel = 100;\\n    }\\n};\";\n    return 0;\n}\n",
                        "expected_output": "class Spaceship {\npublic:\n    int fuel;\n    string name;\n    Spaceship(string n) {\n        name = n;\n        fuel = 100;\n    }\n};",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass Spaceship {\npublic:\n    int fuel;\n    string name;\n    // TODO: Write a constructor that takes a name string, sets 'name', and sets 'fuel' to 100\n};\n\nint main() {\n    std::cout << \"class Spaceship {\\npublic:\\n    int fuel;\\n    string name;\\n    Spaceship(string n) {\\n        name = n;\\n        fuel = 100;\\n    }\\n};\";\n    return 0;\n}\n",
                        "hint": "Read the comments carefully and fill in the missing C++ logic.",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 4: The End of Life",
                "blocks": [
                    {
                        "type": "header",
                        "title": "Destructors",
                        "subtitle": "Cleaning Up After Yourself",
                        "metadata": {
                            "difficulty": "Intermediate",
                            "time": "20m",
                            "concepts": [
                                "Destructors",
                                "Cleanup",
                                "Resource Management"
                            ]
                        }
                    },
                    {
                        "type": "concept",
                        "title": "The Destructor",
                        "content": "Just as a constructor is called when an object is born, a **Destructor** is automatically called when an object is destroyed (e.g., when it goes out of scope). Its job is to perform any necessary cleanup, like closing files, releasing network connections, or freeing dynamically allocated memory."
                    },
                    {
                        "type": "real_world_analogy",
                        "title": "Checking Out of a Hotel",
                        "content": "Constructor: Checking in, getting your room key, and setting up your luggage. Destructor: Checking out, returning the key, and ensuring you haven't left a mess behind."
                    },
                    {
                        "type": "annotated_code",
                        "title": "Defining a Destructor",
                        "code": "class DatabaseConnection {\npublic:\n    DatabaseConnection() {\n        // Code to open connection\n    }\n    ~DatabaseConnection() {\n        // Code to close connection safely\n    }\n};",
                        "annotations": [
                            {
                                "line": "~DatabaseConnection() {",
                                "text": "The tilde (~) denotes a destructor. It has no parameters and no return type."
                            }
                        ]
                    },
                    {
                        "type": "execution_trace",
                        "title": "Scope and Destruction",
                        "code": "void function() {\n    DatabaseConnection db;\n    // Do work with db\n} // db goes out of scope here",
                        "trace": [
                            "db is created, Constructor called",
                            "function does work",
                            "function ends, db is destroyed, Destructor called automatically"
                        ]
                    },
                    {
                        "type": "common_mistakes",
                        "title": "Memory Leaks",
                        "mistakes": [
                            {
                                "title": "Forgetting to clean up resources",
                                "desc": "If an object allocates heap memory (using `new`) and the destructor doesn't `delete` it, that memory is lost forever when the object is destroyed, causing a memory leak."
                            }
                        ]
                    },
                    {
                        "type": "mastery_challenge",
                        "title": "When does the Destructor run?",
                        "question": "If you create a local object inside an `if` statement block, when is its destructor called?",
                        "options": [
                            "When the program ends.",
                            "Immediately after it's created.",
                            "When the `if` statement block ends (closing brace).",
                            "You have to call it manually."
                        ],
                        "answer": 2,
                        "explanation": "Local objects are destroyed when the scope block (e.g., the {} of an if statement, loop, or function) they were created in ends."
                    },
                    {
                        "type": "code_lab",
                        "title": "Implement Cleanup",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass TempFile {\npublic:\n    TempFile() { /* opens file */ }\n    // TODO: Add a destructor\n};\n\nint main() {\n    std::cout << \"class TempFile {\\npublic:\\n    TempFile() { /* opens file */ }\\n    ~TempFile() { }\\n};\";\n    return 0;\n}\n",
                        "expected_output": "class TempFile {\npublic:\n    TempFile() { /* opens file */ }\n    ~TempFile() { }\n};",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass TempFile {\npublic:\n    TempFile() { /* opens file */ }\n    // TODO: Add a destructor\n};\n\nint main() {\n    std::cout << \"class TempFile {\\npublic:\\n    TempFile() { /* opens file */ }\\n    ~TempFile() { }\\n};\";\n    return 0;\n}\n",
                        "hint": "Read the comments carefully and fill in the missing C++ logic.",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            }
        ]
    },
    "7": {
        "format": "episodic",
        "episodes": [
            {
                "title": "Module 1: The Danger of Public Access",
                "blocks": [
                    {
                        "type": "header",
                        "title": "Exposed State",
                        "subtitle": "When Anyone Can Touch Anything",
                        "metadata": {
                            "difficulty": "Beginner",
                            "time": "15m",
                            "concepts": [
                                "Encapsulation",
                                "Public Access"
                            ]
                        }
                    },
                    {
                        "type": "mermaid_diagram",
                        "title": "Architectural Overview",
                        "explanation": "Before we write code, study this structural model to understand the relationships we are building.",
                        "code": "classDiagram\n    class SecureVault {\n        -double balance\n        -string passcodeHash\n        -bool isLocked\n        -validateKey(string key) bool\n        +SecureVault(string key, double initialDeposit)\n        +deposit(double amount) bool\n        +withdraw(string key, double amount) bool\n        +auditBalance(string key) double\n    }\n    note for SecureVault \"Encapsulation Boundary:\nPrivate data cannot be corrupted from outside.\nAll mutations must satisfy class invariants.\" "
                    },
                    {
                        "type": "story",
                        "title": "The Hacked Game",
                        "content": "You designed a multiplayer game. You created a `Player` class with a `health` field. The game was an instant hit. But on day two, players discovered they could write a script to set their `health` to 999999. The game is ruined. What went wrong?"
                    },
                    {
                        "type": "annotated_code",
                        "title": "The Vulnerable Class",
                        "code": "class Player {\npublic:\n    int health = 100;\n};\n\n// Hacker code somewhere else:\nPlayer p1;\np1.health = 999999; // Directly changing internal state",
                        "annotations": [
                            {
                                "line": "public:",
                                "text": "This keyword means everything following it can be accessed from outside the object."
                            },
                            {
                                "line": "p1.health = 999999;",
                                "text": "External code has unfettered access to modify the object's state in invalid ways."
                            }
                        ]
                    },
                    {
                        "type": "mental_model",
                        "title": "The Unlocked Safe",
                        "data": "  [ Player Object ]\n  [  (Unlocked)   ]\n  [  health: 100  ] <--- Anyone can reach in and change this!"
                    },
                    {
                        "type": "wrong_approach",
                        "title": "Trusting the Caller",
                        "code": "void takeDamage(Player& p, int damage) {\n    p.health -= damage;\n    // What if damage is negative? The player heals!\n}",
                        "explanation": "When data is public, you rely on every piece of external code to behave perfectly and follow the rules. In a large system, this is impossible."
                    },
                    {
                        "type": "concept",
                        "title": "The Core of Encapsulation",
                        "content": "Encapsulation is the principle of bundling data and the methods that operate on that data into a single unit, and crucially, **restricting direct access to some of the object's components**. This prevents external code from putting the object into an invalid or unexpected state."
                    },
                    {
                        "type": "think_first",
                        "question": "If `health` is public, how can you guarantee a player's health never drops below 0?",
                        "options": [
                            "Write an if-statement inside the class.",
                            "You cannot guarantee it.",
                            "Use a special compiler flag.",
                            "Make the variable a constant."
                        ],
                        "answer": 1,
                        "explanation": "If the variable is public, any external code can set it to -50 directly. You have lost control over your object's state."
                    },
                    {
                        "type": "real_world_analogy",
                        "title": "The Bank Teller",
                        "content": "You don't just walk behind the counter at a bank and grab money from the vault (Public). You talk to the Teller (Method), who verifies your identity and processes your withdrawal safely (Encapsulation)."
                    }
                ]
            },
            {
                "title": "Module 2: Private Boundaries",
                "blocks": [
                    {
                        "type": "header",
                        "title": "Drawing the Boundary",
                        "subtitle": "The Private Access Modifier",
                        "metadata": {
                            "difficulty": "Beginner",
                            "time": "20m",
                            "concepts": [
                                "Private Access",
                                "Data Hiding"
                            ]
                        }
                    },
                    {
                        "type": "concept",
                        "title": "The 'private' Keyword",
                        "content": "In C++, the `private` keyword creates a boundary. Any members (variables or methods) declared as private can ONLY be accessed by methods belonging to that specific class. External code is completely blocked from accessing them."
                    },
                    {
                        "type": "annotated_code",
                        "title": "Locking the Safe",
                        "code": "class Player {\nprivate:\n    int health = 100;\npublic:\n    void takeDamage(int amount) {\n        // Valid because takeDamage is a member of Player\n        health -= amount; \n    }\n};",
                        "annotations": [
                            {
                                "line": "private:",
                                "text": "The boundary is drawn. Health is now hidden."
                            },
                            {
                                "line": "int health = 100;",
                                "text": "This data is secure within the object."
                            },
                            {
                                "line": "public:",
                                "text": "The public interface that external code is allowed to interact with."
                            }
                        ]
                    },
                    {
                        "type": "correct_approach",
                        "title": "Compiler Enforcement",
                        "code": "Player p1;\n// p1.health = 999999; // ERROR!\np1.takeDamage(10);     // ALLOWED",
                        "explanation": "If external code tries to directly access a private member, the C++ compiler throws a hard error. It physically prevents the violation of encapsulation."
                    },
                    {
                        "type": "execution_trace",
                        "title": "Allowed vs Denied",
                        "code": "Player p;\np.health = 50; // Denied by compiler\np.takeDamage(20); // Allowed, method runs",
                        "trace": [
                            "Compile step: p.health access fails.",
                            "Compile step: p.takeDamage succeeds.",
                            "Runtime: takeDamage safely modifies internal private health."
                        ]
                    },
                    {
                        "type": "common_mistakes",
                        "title": "Making Everything Private",
                        "mistakes": [
                            {
                                "title": "No Public Interface",
                                "desc": "If you make all methods and variables private, the object is a black box that cannot be interacted with at all. You need a public interface (methods) to make the object useful."
                            }
                        ]
                    },
                    {
                        "type": "problem",
                        "content": "You have a `BankAccount` class. The `balance` is private. You need to write a standalone global function `printBalance(BankAccount b)` that prints the balance. Why won't this work?"
                    },
                    {
                        "type": "code_lab",
                        "title": "Apply Access Modifiers",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass SecretAgent {\n    // TODO: make 'real_name' private, and 'codename' public\n    string real_name;\n    string codename;\n};\n\nint main() {\n    std::cout << \"class SecretAgent {\\nprivate:\\n    string real_name;\\npublic:\\n    string codename;\\n};\";\n    return 0;\n}\n",
                        "expected_output": "class SecretAgent {\nprivate:\n    string real_name;\npublic:\n    string codename;\n};",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass SecretAgent {\n    // TODO: make 'real_name' private, and 'codename' public\n    string real_name;\n    string codename;\n};\n\nint main() {\n    std::cout << \"class SecretAgent {\\nprivate:\\n    string real_name;\\npublic:\\n    string codename;\\n};\";\n    return 0;\n}\n",
                        "hint": "Read the comments carefully and fill in the missing C++ logic.",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 3: Controlled Access",
                "blocks": [
                    {
                        "type": "header",
                        "title": "Getters and Setters",
                        "subtitle": "Providing Safe Access Points",
                        "metadata": {
                            "difficulty": "Intermediate",
                            "time": "20m",
                            "concepts": [
                                "Getters",
                                "Setters",
                                "Accessors"
                            ]
                        }
                    },
                    {
                        "type": "story",
                        "title": "The Need for Information",
                        "content": "You've successfully hidden the `Player`'s `health` making it private. But now the UI team is complaining: 'We can't draw the health bar! The compiler won't let us read the health value!' You need a way to let them see the health without letting them change it directly."
                    },
                    {
                        "type": "concept",
                        "title": "Accessors and Mutators",
                        "content": "Getters (accessors) are public methods that return the value of a private variable. Setters (mutators) are public methods that allow external code to update a private variable in a controlled way."
                    },
                    {
                        "type": "annotated_code",
                        "title": "Implementing Getters and Setters",
                        "code": "class Player {\nprivate:\n    int health = 100;\npublic:\n    // Getter\n    int getHealth() {\n        return health;\n    }\n    // Setter\n    void setHealth(int newHealth) {\n        health = newHealth;\n    }\n};",
                        "annotations": [
                            {
                                "line": "int getHealth() {",
                                "text": "Allows read-only access to the private variable."
                            },
                            {
                                "line": "void setHealth(int newHealth) {",
                                "text": "Allows controlled modification."
                            }
                        ]
                    },
                    {
                        "type": "mental_model",
                        "title": "The Drive-Thru Window",
                        "data": "  [ Kitchen (Private State) ]\n       |\n  [ Drive-Thru Window (Public Getter/Setter) ]\n       |\n  [ Customer (External Code) ]"
                    },
                    {
                        "type": "comparison_table",
                        "title": "Public Variable vs Getter/Setter",
                        "headers": [
                            "Action",
                            "Public Variable",
                            "Getter/Setter"
                        ],
                        "rows": [
                            [
                                "Read value",
                                "Easy, but risky",
                                "Easy and safe"
                            ],
                            [
                                "Change value",
                                "Unrestricted",
                                "Can add validation inside the setter"
                            ],
                            [
                                "Make Read-Only",
                                "Impossible",
                                "Just don't provide a setter method"
                            ]
                        ]
                    },
                    {
                        "type": "mastery_challenge",
                        "title": "Read-Only Data",
                        "question": "How do you make a private variable 'read-only' to the outside world?",
                        "options": [
                            "Use the `const` keyword on the variable.",
                            "Provide a Getter method but NO Setter method.",
                            "Make the variable public but add a comment saying 'do not change'.",
                            "You can't do this in C++."
                        ],
                        "answer": 1,
                        "explanation": "By providing a getter, the outside world can read the value. By omitting the setter, the compiler will prevent any external code from modifying it."
                    },
                    {
                        "type": "code_lab",
                        "title": "Write a Getter",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass TemperatureSensor {\nprivate:\n    double current_temp = 72.5;\npublic:\n    // TODO: Write a getter method named 'getTemp' that returns current_temp\n};\n\nint main() {\n    std::cout << \"class TemperatureSensor {\\nprivate:\\n    double current_temp = 72.5;\\npublic:\\n    double getTemp() {\\n        return current_temp;\\n    }\\n};\";\n    return 0;\n}\n",
                        "expected_output": "class TemperatureSensor {\nprivate:\n    double current_temp = 72.5;\npublic:\n    double getTemp() {\n        return current_temp;\n    }\n};",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass TemperatureSensor {\nprivate:\n    double current_temp = 72.5;\npublic:\n    // TODO: Write a getter method named 'getTemp' that returns current_temp\n};\n\nint main() {\n    std::cout << \"class TemperatureSensor {\\nprivate:\\n    double current_temp = 72.5;\\npublic:\\n    double getTemp() {\\n        return current_temp;\\n    }\\n};\";\n    return 0;\n}\n",
                        "hint": "Read the comments carefully and fill in the missing C++ logic.",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 4: Enforcing Invariants",
                "blocks": [
                    {
                        "type": "header",
                        "title": "Protecting the Truth",
                        "subtitle": "Enforcing Class Invariants",
                        "metadata": {
                            "difficulty": "Advanced",
                            "time": "25m",
                            "concepts": [
                                "Invariants",
                                "Validation",
                                "Robustness"
                            ]
                        }
                    },
                    {
                        "type": "concept",
                        "title": "What is an Invariant?",
                        "content": "A Class Invariant is a condition or rule about the object's state that must ALWAYS be true. For example: 'A bank account balance cannot be negative' or 'A player's health must be between 0 and 100'. Encapsulation is the ONLY way to reliably enforce these invariants."
                    },
                    {
                        "type": "annotated_code",
                        "title": "The Bouncer at the Door",
                        "code": "class Player {\nprivate:\n    int health = 100;\npublic:\n    void setHealth(int newHealth) {\n        if (newHealth < 0) {\n            health = 0;\n        } else if (newHealth > 100) {\n            health = 100;\n        } else {\n            health = newHealth;\n        }\n    }\n};",
                        "annotations": [
                            {
                                "line": "if (newHealth < 0) {",
                                "text": "Validation logic blocks invalid data from corrupting the state."
                            },
                            {
                                "line": "health = 0;",
                                "text": "Enforces the lower bound invariant."
                            }
                        ]
                    },
                    {
                        "type": "execution_trace",
                        "title": "Filtering Bad Data",
                        "code": "Player p;\np.setHealth(150);\n// health is 100\np.setHealth(-20);\n// health is 0",
                        "trace": [
                            "setHealth(150) -> fails >100 check, caps at 100",
                            "setHealth(-20) -> fails <0 check, floors at 0",
                            "Object state remains completely valid."
                        ]
                    },
                    {
                        "type": "real_world_analogy",
                        "title": "The Thermostat",
                        "content": "If you set a smart thermostat to 5,000 degrees, it won't actually burn your house down. The internal software (Setter) intercepts your request, validates it against its safety limits (Invariants), and caps it at a safe maximum like 90 degrees."
                    },
                    {
                        "type": "common_mistakes",
                        "title": "Leaky Invariants",
                        "mistakes": [
                            {
                                "title": "Forgetting the Constructor",
                                "desc": "You add validation to your Setter, but you forget to add the same validation to your Constructor! A user could create an object with invalid initial state."
                            }
                        ]
                    },
                    {
                        "type": "mastery_challenge",
                        "title": "The Purpose of Setters",
                        "question": "What is the primary advantage of using a setter with validation over making a variable public?",
                        "options": [
                            "It makes the code run faster.",
                            "It guarantees the object is never put into an invalid state.",
                            "It uses less memory.",
                            "It automatically encrypts the data."
                        ],
                        "answer": 1,
                        "explanation": "Setters allow you to enforce rules (invariants) before data is changed, ensuring the object's internal state is always valid."
                    },
                    {
                        "type": "code_lab",
                        "title": "Enforce the Speed Limit",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass Car {\nprivate:\n    int speed = 0;\npublic:\n    // TODO: Write setSpeed(int s). \n    // If s is negative, set speed to 0.\n    // If s is greater than 120, set speed to 120.\n    // Otherwise, set speed to s.\n};\n\nint main() {\n    std::cout << \"class Car {\\nprivate:\\n    int speed = 0;\\npublic:\\n    void setSpeed(int s) {\\n        if (s < 0) {\\n            speed = 0;\\n        } else if (s > 120) {\\n            speed = 120;\\n        } else {\\n            speed = s;\\n        }\\n    }\\n};\";\n    return 0;\n}\n",
                        "expected_output": "class Car {\nprivate:\n    int speed = 0;\npublic:\n    void setSpeed(int s) {\n        if (s < 0) {\n            speed = 0;\n        } else if (s > 120) {\n            speed = 120;\n        } else {\n            speed = s;\n        }\n    }\n};",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass Car {\nprivate:\n    int speed = 0;\npublic:\n    // TODO: Write setSpeed(int s). \n    // If s is negative, set speed to 0.\n    // If s is greater than 120, set speed to 120.\n    // Otherwise, set speed to s.\n};\n\nint main() {\n    std::cout << \"class Car {\\nprivate:\\n    int speed = 0;\\npublic:\\n    void setSpeed(int s) {\\n        if (s < 0) {\\n            speed = 0;\\n        } else if (s > 120) {\\n            speed = 120;\\n        } else {\\n            speed = s;\\n        }\\n    }\\n};\";\n    return 0;\n}\n",
                        "hint": "Read the comments carefully and fill in the missing C++ logic.",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            }
        ]
    },
    "8": {
        "format": "episodic",
        "episodes": [
            {
                "title": "Module 1: The First Breath",
                "blocks": [
                    {
                        "type": "story",
                        "title": "The Awakening",
                        "content": "In the silicon valleys of the digital realm, an object is born. But without initialization, it's just raw, chaotic memory."
                    },
                    {
                        "type": "mermaid_diagram",
                        "title": "Architectural Overview",
                        "explanation": "Before we write code, study this structural model to understand the relationships we are building.",
                        "code": "flowchart TD\n    ALLOC[\"Memory Allocated in RAM\n(Stack frame or Heap block)\"] --> INITLIST[\"Member Initializer List Executes\nIn-place initialization of members\nNo redundant default assignments\"]\n    INITLIST --> DELEGATE{\"Is Delegating\nConstructor?\"}\n    DELEGATE -- \"Yes\" --> TARGET[\"Delegate to Target Constructor\"]\n    DELEGATE -- \"No\" --> BODY[\"Constructor Body Executes\nValidation checks & resource setup\"]\n    TARGET --> BODY\n    BODY --> VALID[\"Constructed Object Enters Lifetime\nClass Invariants Guaranteed\"]"
                    },
                    {
                        "type": "problem",
                        "content": "How do we ensure that every new 'Robot' starts with exactly 100 health, instead of random garbage memory values?"
                    },
                    {
                        "type": "concept",
                        "title": "Default Constructors",
                        "explanation": "A constructor is a special function called automatically when an object is created.",
                        "analogy": "Like a factory assembly line setting the default settings before shipping a product.",
                        "technical_explanation": "It has the same name as the class, no return type, and takes no parameters (default)."
                    },
                    {
                        "type": "mental_model",
                        "title": "Memory Awakening",
                        "data": "[ Raw Memory ] --(Constructor)--> [ Initialized Object ]"
                    },
                    {
                        "type": "annotated_code",
                        "title": "The Basic Constructor",
                        "code": "class Robot {\npublic:\n  int health;\n  Robot() {\n    health = 100;\n  }\n};",
                        "annotations": [
                            {
                                "line": "Robot() {",
                                "text": "This is the default constructor."
                            }
                        ]
                    },
                    {
                        "type": "code_lab",
                        "title": "Initialize the Core",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass Core {\npublic:\n  int power;\n  // TODO: Add default constructor to set power to 50\n};\n\nint main() {\n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass Core {\npublic:\n  int power;\n  Core() { power = 50; }\n};\n\nint main() {\n    return 0;\n}\n",
                        "hint": "Function name must match the class name 'Core'.",
                        "expected_output": "",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 2: Tailoring the Object",
                "blocks": [
                    {
                        "type": "story",
                        "title": "Custom Specifications",
                        "content": "Not all robots are built the same. Some are workers, some are warriors. We need custom blueprints."
                    },
                    {
                        "type": "problem",
                        "content": "How can we pass starting values to our object the moment it is created?"
                    },
                    {
                        "type": "concept",
                        "title": "Parameterized Constructors",
                        "explanation": "Constructors can take arguments, allowing you to pass data upon creation.",
                        "analogy": "Ordering a custom PC with specific RAM and CPU, rather than taking the default model.",
                        "technical_explanation": "Define parameters in the constructor signature, just like a regular function."
                    },
                    {
                        "type": "think_first",
                        "question": "Can a class have both a default AND a parameterized constructor?",
                        "options": [
                            "Yes, through overloading",
                            "No, only one is allowed"
                        ],
                        "answer": 0,
                        "explanation": "C++ supports function overloading, allowing multiple constructors with different parameters."
                    },
                    {
                        "type": "annotated_code",
                        "title": "Custom Build",
                        "code": "class Robot {\npublic:\n  int hp;\n  Robot(int start_hp) {\n    hp = start_hp;\n  }\n};",
                        "annotations": [
                            {
                                "line": "Robot(int start_hp)",
                                "text": "Constructor accepting an integer parameter."
                            }
                        ]
                    },
                    {
                        "type": "code_lab",
                        "title": "Warrior Setup",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass Warrior {\npublic:\n  int damage;\n  // TODO: Add a constructor that takes an int and assigns it to damage\n};\n\nint main() {\n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass Warrior {\npublic:\n  int damage;\n  Warrior(int d) { damage = d; }\n};\n\nint main() {\n    return 0;\n}\n",
                        "hint": "Warrior(int d) { ... }",
                        "expected_output": "",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 3: The Efficiency Secret",
                "blocks": [
                    {
                        "type": "story",
                        "title": "The Speed of Light",
                        "content": "Assigning values inside the constructor body is slow. The object is built, and then you overwrite its parts. There is a faster way."
                    },
                    {
                        "type": "problem",
                        "content": "How do we initialize member variables directly as the object is being constructed?"
                    },
                    {
                        "type": "concept",
                        "title": "Initializer Lists",
                        "explanation": "Initializer lists initialize members before the constructor body runs.",
                        "analogy": "Building the parts correctly the first time, rather than building generic parts and repainting them.",
                        "technical_explanation": "Use a colon after the constructor signature followed by member(value) syntax."
                    },
                    {
                        "type": "execution_trace",
                        "title": "Initialization Phase",
                        "code": "Robot() : hp(100) {} ",
                        "trace": [
                            "Memory allocated for hp",
                            "hp initialized to 100 directly",
                            "Constructor body (empty) executes"
                        ]
                    },
                    {
                        "type": "mastery_challenge",
                        "question": "Why use initializer lists?",
                        "options": [
                            "It looks cooler",
                            "It's required for constants/references and is more efficient",
                            "It saves lines of code"
                        ],
                        "answer": 1,
                        "explanation": "Constants and references MUST be initialized this way, and it avoids double-initialization for complex objects."
                    },
                    {
                        "type": "code_lab",
                        "title": "Direct Injection",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass Engine {\npublic:\n  const int max_speed;\n  // TODO: Use an initializer list to set max_speed to the given parameter s\n  Engine(int s) \n};\n\nint main() {\n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass Engine {\npublic:\n  const int max_speed;\n  Engine(int s) : max_speed(s) {}\n};\n\nint main() {\n    return 0;\n}\n",
                        "hint": "Engine(int s) : max_speed(s) {}",
                        "expected_output": "",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 4: Constructor Delegation",
                "blocks": [
                    {
                        "type": "story",
                        "title": "Passing the Baton",
                        "content": "As blueprints grow complex, constructors start repeating themselves. A smart engineer reuses existing blueprints."
                    },
                    {
                        "type": "problem",
                        "content": "How can one constructor call another constructor in the same class?"
                    },
                    {
                        "type": "concept",
                        "title": "Delegating Constructors",
                        "explanation": "In C++11, a constructor can call another constructor in its initializer list.",
                        "analogy": "A junior mechanic asking the senior mechanic to do the heavy lifting before adding minor tweaks.",
                        "technical_explanation": "Place the target constructor call in the initializer list: `Class() : Class(args) {}`"
                    },
                    {
                        "type": "mental_model",
                        "title": "Delegation Chain",
                        "data": "Constructor A ---> delegates to ---> Constructor B"
                    },
                    {
                        "type": "annotated_code",
                        "title": "Delegation",
                        "code": "class Bot {\npublic:\n  int hp, armor;\n  Bot(int h, int a) : hp(h), armor(a) {}\n  Bot() : Bot(100, 10) {} // Delegates\n};",
                        "annotations": [
                            {
                                "line": "Bot() : Bot(100, 10)",
                                "text": "This calls the parameterized constructor."
                            }
                        ]
                    },
                    {
                        "type": "code_lab",
                        "title": "Delegate the Work",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass Ship {\npublic:\n  int shields, weapons;\n  Ship(int s, int w) : shields(s), weapons(w) {}\n  // TODO: Add default constructor that delegates to Ship(50, 2)\n};\n\nint main() {\n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass Ship {\npublic:\n  int shields, weapons;\n  Ship(int s, int w) : shields(s), weapons(w) {}\n  Ship() : Ship(50, 2) {}\n};\n\nint main() {\n    return 0;\n}\n",
                        "hint": "Ship() : Ship(50, 2) {}",
                        "expected_output": "",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            }
        ]
    },
    "9": {
        "format": "episodic",
        "episodes": [
            {
                "title": "Module 1: The Final Breath",
                "blocks": [
                    {
                        "type": "story",
                        "title": "Dust to Dust",
                        "content": "All programs must end. But when an object dies, what happens to the resources it claimed?"
                    },
                    {
                        "type": "mermaid_diagram",
                        "title": "Architectural Overview",
                        "explanation": "Before we write code, study this structural model to understand the relationships we are building.",
                        "code": "stateDiagram-v2\n    [*] --> ScopeEntered: Function Block Entered\n    ScopeEntered --> FirstCreated: Resource A Initialized (Stack)\n    FirstCreated --> SecondCreated: Resource B Initialized (Stack)\n    SecondCreated --> ActiveProcessing: Program Runs Normal Logic\n    ActiveProcessing --> ScopeExit: Scope Closes or Exception Thrown\n    state ScopeExit {\n        [*] --> DestroySecond: Destructor ~ResourceB() Invoked (LIFO)\n        DestroySecond --> FreeResB: Free Memory / Close Handle B\n        FreeResB --> DestroyFirst: Destructor ~ResourceA() Invoked (LIFO)\n        DestroyFirst --> FreeResA: Free Memory / Close Handle A\n    }\n    ScopeExit --> [*]: Stack Clean / Zero Resource Leak"
                    },
                    {
                        "type": "problem",
                        "content": "How do we run cleanup code automatically right before an object is destroyed?"
                    },
                    {
                        "type": "concept",
                        "title": "Destructors",
                        "explanation": "A destructor is called when an object goes out of scope or is deleted.",
                        "analogy": "A checkout procedure at a hotel, returning the room keys.",
                        "technical_explanation": "It has the class name prefixed with a tilde (~), no parameters, no return type."
                    },
                    {
                        "type": "mental_model",
                        "title": "Scope End",
                        "data": "{ Object Created } ---> [ Operations ] ---> { Scope Ends -> Destructor Called }"
                    },
                    {
                        "type": "annotated_code",
                        "title": "The Cleanup",
                        "code": "class File {\npublic:\n  ~File() {\n    // Close file\n  }\n};",
                        "annotations": [
                            {
                                "line": "~File()",
                                "text": "The destructor."
                            }
                        ]
                    },
                    {
                        "type": "code_lab",
                        "title": "Close the Blast Doors",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass Bunker {\npublic:\n  // TODO: Add a destructor that prints 'Doors Closed'\n};\n\nint main() {\n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass Bunker {\npublic:\n  ~Bunker() { std::cout << \"Doors Closed\"; }\n};\n\nint main() {\n    return 0;\n}\n",
                        "hint": "~Bunker() { ... }",
                        "expected_output": "",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 2: Memory Leaks",
                "blocks": [
                    {
                        "type": "story",
                        "title": "The Silent Killer",
                        "content": "A system runs for days, slowly eating up RAM until it crashes. The culprit? Memory allocated but never freed."
                    },
                    {
                        "type": "problem",
                        "content": "If we use `new` inside a constructor, how do we prevent a memory leak?"
                    },
                    {
                        "type": "concept",
                        "title": "Manual Memory Management",
                        "explanation": "Dynamic memory must be manually deleted.",
                        "analogy": "Renting a car (new) means you MUST return it (delete). If you lose the keys, the car is lost forever.",
                        "technical_explanation": "For every `new` in a constructor, there should be a `delete` in the destructor."
                    },
                    {
                        "type": "think_first",
                        "question": "What happens if we forget to call delete on memory allocated by an object?",
                        "options": [
                            "The compiler fixes it",
                            "Memory leak",
                            "Garbage collector handles it"
                        ],
                        "answer": 1,
                        "explanation": "C++ has no garbage collector. Unfreed memory stays reserved forever."
                    },
                    {
                        "type": "annotated_code",
                        "title": "Dynamic Cleanup",
                        "code": "class Buffer {\n  int* data;\npublic:\n  Buffer() { data = new int[100]; }\n  ~Buffer() { delete[] data; }\n};",
                        "annotations": [
                            {
                                "line": "delete[] data;",
                                "text": "Frees the dynamically allocated array."
                            }
                        ]
                    },
                    {
                        "type": "code_lab",
                        "title": "Free the Buffer",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass Image {\n  char* pixels;\npublic:\n  Image() { pixels = new char[1024]; }\n  // TODO: Write destructor to free pixels array\n};\n\nint main() {\n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass Image {\n  char* pixels;\npublic:\n  Image() { pixels = new char[1024]; }\n  ~Image() { delete[] pixels; }\n};\n\nint main() {\n    return 0;\n}\n",
                        "hint": "Use delete[] for arrays.",
                        "expected_output": "",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 3: The RAII Principle",
                "blocks": [
                    {
                        "type": "story",
                        "title": "The Golden Rule of C++",
                        "content": "You've learned to manage memory manually, but human error is inevitable. What if the management was fully automated by design?"
                    },
                    {
                        "type": "problem",
                        "content": "How do we guarantee that resources are always released, even if an error or exception occurs?"
                    },
                    {
                        "type": "concept",
                        "title": "Resource Acquisition Is Initialization (RAII)",
                        "explanation": "Bind the lifecycle of a resource to the lifecycle of a local object.",
                        "analogy": "A smart door that unlocks when you stand on a pressure plate and locks immediately when you step off.",
                        "technical_explanation": "Acquire resources in the constructor, release them in the destructor. Stack unwinding guarantees destructor execution."
                    },
                    {
                        "type": "mastery_challenge",
                        "question": "Why is RAII so powerful?",
                        "options": [
                            "It makes code run faster",
                            "It guarantees resource cleanup even if exceptions are thrown",
                            "It uses less memory"
                        ],
                        "answer": 1,
                        "explanation": "Because local objects are always destroyed when going out of scope, their destructors are guaranteed to run, preventing leaks during exceptions."
                    },
                    {
                        "type": "execution_trace",
                        "title": "RAII in Action",
                        "code": "void process() {\n  FileHandler file(\"data.txt\");\n  throw Error(); // Exception!\n} // file.~FileHandler() is called here!",
                        "trace": [
                            "FileHandler constructor opens file",
                            "Exception thrown",
                            "Stack unwinds, FileHandler destructor closes file"
                        ]
                    },
                    {
                        "type": "code_lab",
                        "title": "Lock Guard",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass Lock {\npublic:\n  Lock() { /* lock */ }\n  // TODO: Add destructor to unlock (print 'Unlocked')\n};\n\nint main() {\n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass Lock {\npublic:\n  Lock() { }\n  ~Lock() { std::cout << \"Unlocked\"; }\n};\n\nint main() {\n    return 0;\n}\n",
                        "hint": "Print 'Unlocked' in the destructor.",
                        "expected_output": "",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 4: Destructor Rules",
                "blocks": [
                    {
                        "type": "story",
                        "title": "The Final Verdict",
                        "content": "Before leaving the subject of destructors, there are rigid rules of physics in C++ that govern destruction order."
                    },
                    {
                        "type": "problem",
                        "content": "In what order are objects destroyed when a scope ends?"
                    },
                    {
                        "type": "concept",
                        "title": "Destruction Order",
                        "explanation": "Objects are destroyed in the reverse order of their creation.",
                        "analogy": "Taking boxes out of a narrow hallway: the last box you put in must be the first one you take out (LIFO).",
                        "technical_explanation": "Stack semantics govern local variables. Last-In, First-Out (LIFO)."
                    },
                    {
                        "type": "mental_model",
                        "title": "LIFO Destruction",
                        "data": "Create A -> Create B -> Create C ===> Destroy C -> Destroy B -> Destroy A"
                    },
                    {
                        "type": "annotated_code",
                        "title": "Order of Ops",
                        "code": "{\n  Obj a(\"A\");\n  Obj b(\"B\");\n} // b destroyed, then a",
                        "annotations": [
                            {
                                "line": "} // b destroyed, then a",
                                "text": "Reverse creation order."
                            }
                        ]
                    },
                    {
                        "type": "code_lab",
                        "title": "Trace the Output",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass Tracker {\n  int id;\npublic:\n  Tracker(int i) : id(i) {}\n  ~Tracker() { std::cout << id; }\n};\nvoid run() {\n  Tracker t1(1);\n  Tracker t2(2);\n  // TODO: Just run to see the output order\n}\n\nint main() {\n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass Tracker {\n  int id;\npublic:\n  Tracker(int i) : id(i) {}\n  ~Tracker() { std::cout << id; }\n};\nvoid run() {\n  Tracker t1(1);\n  Tracker t2(2);\n}\n\nint main() {\n    return 0;\n}\n",
                        "hint": "Run the code. Output will be 21.",
                        "expected_output": "",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            }
        ]
    },
    "10": {
        "format": "episodic",
        "episodes": [
            {
                "title": "Module 1: Building a Machine",
                "blocks": [
                    {
                        "type": "story",
                        "title": "The Sum of Its Parts",
                        "content": "A car is not a monolithic block of metal. It is made of an engine, wheels, and a chassis. Software is no different."
                    },
                    {
                        "type": "mermaid_diagram",
                        "title": "Architectural Overview",
                        "explanation": "Before we write code, study this structural model to understand the relationships we are building.",
                        "code": "classDiagram\n    class CombatVehicle {\n        -Engine engine\n        -ArmorPlating armor\n        -TargetingRadar radar\n        +startVehicle() void\n        +engageTarget() void\n    }\n    class Engine {\n        -int horsepower\n        -bool isRunning\n        +ignite() void\n        +shutdown() void\n    }\n    class ArmorPlating {\n        -int currentDurability\n        +absorbImpact(int force) void\n    }\n    class TargetingRadar {\n        -double rangeKm\n        +scanTargets() void\n    }\n    CombatVehicle *-- Engine : \"Composition (Owns Lifetime)\"\n    CombatVehicle *-- ArmorPlating : \"Composition (Owns Lifetime)\"\n    CombatVehicle *-- TargetingRadar : \"Composition (Owns Lifetime)\" "
                    },
                    {
                        "type": "problem",
                        "content": "How do we create complex classes built out of simpler, reusable classes?"
                    },
                    {
                        "type": "concept",
                        "title": "Composition",
                        "explanation": "Composition is an 'has-a' relationship where a class contains objects of other classes as members.",
                        "analogy": "A smartphone 'has a' battery, 'has a' screen, and 'has a' processor.",
                        "technical_explanation": "Declare instances of other classes as member variables within your class."
                    },
                    {
                        "type": "mental_model",
                        "title": "Has-A Relationship",
                        "data": "Car [ Engine, Wheel(x4), Chassis ]"
                    },
                    {
                        "type": "annotated_code",
                        "title": "The Car Setup",
                        "code": "class Engine { /*...*/ };\nclass Car {\n  Engine v8;\n};",
                        "annotations": [
                            {
                                "line": "Engine v8;",
                                "text": "Car is composed of an Engine."
                            }
                        ]
                    },
                    {
                        "type": "code_lab",
                        "title": "Assemble the Robot",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass Head {};\nclass Body {};\nclass Robot {\n  // TODO: Add a Head named 'head' and a Body named 'body'\n};\n\nint main() {\n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass Head {};\nclass Body {};\nclass Robot {\n  Head head;\n  Body body;\n};\n\nint main() {\n    return 0;\n}\n",
                        "hint": "Declare them as members inside Robot.",
                        "expected_output": "",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 2: The Inner Workings",
                "blocks": [
                    {
                        "type": "story",
                        "title": "Firing Up the Subsystems",
                        "content": "When you start the car, the engine must be created. The order of creation is critical to prevent crashes."
                    },
                    {
                        "type": "problem",
                        "content": "How and when are member objects constructed?"
                    },
                    {
                        "type": "concept",
                        "title": "Member Object Construction",
                        "explanation": "Member objects are constructed BEFORE the container class's constructor body executes.",
                        "analogy": "You must build the engine and wheels before you can assemble them into the final car frame.",
                        "technical_explanation": "They are initialized in the order they are declared in the class definition."
                    },
                    {
                        "type": "think_first",
                        "question": "Can you pass arguments to member object constructors?",
                        "options": [
                            "Yes, using the initializer list",
                            "No, they must use default constructors"
                        ],
                        "answer": 0,
                        "explanation": "Initializer lists are used specifically to pass arguments to member objects."
                    },
                    {
                        "type": "annotated_code",
                        "title": "Passing Parameters",
                        "code": "class Car {\n  Engine e;\npublic:\n  Car(int hp) : e(hp) { }\n};",
                        "annotations": [
                            {
                                "line": "Car(int hp) : e(hp) { }",
                                "text": "e(hp) calls the Engine constructor before Car's body runs."
                            }
                        ]
                    },
                    {
                        "type": "code_lab",
                        "title": "Power the Core",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass Core { public: Core(int p) {} };\nclass Reactor {\n  Core core;\npublic:\n  // TODO: Initialize core with 100 in the initializer list\n  Reactor() \n};\n\nint main() {\n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass Core { public: Core(int p) {} };\nclass Reactor {\n  Core core;\npublic:\n  Reactor() : core(100) {}\n};\n\nint main() {\n    return 0;\n}\n",
                        "hint": "Reactor() : core(100) {}",
                        "expected_output": "",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 3: Delegation of Responsibilities",
                "blocks": [
                    {
                        "type": "story",
                        "title": "Chain of Command",
                        "content": "A good manager doesn't do all the work; they delegate to specialists. A good class does the same."
                    },
                    {
                        "type": "problem",
                        "content": "How should a composite class use its member objects?"
                    },
                    {
                        "type": "concept",
                        "title": "Method Delegation",
                        "explanation": "The container class calls methods of its member objects to perform tasks.",
                        "analogy": "When you press the gas pedal, the Car tells the Engine to accelerate.",
                        "technical_explanation": "Access member objects and call their public methods from within the container's methods."
                    },
                    {
                        "type": "execution_trace",
                        "title": "Delegation",
                        "code": "void Car::drive() {\n  engine.start();\n  wheels.spin();\n}",
                        "trace": [
                            "Car::drive called",
                            "engine.start called",
                            "wheels.spin called"
                        ]
                    },
                    {
                        "type": "mastery_challenge",
                        "question": "What is a key benefit of Composition over doing everything in one giant class?",
                        "options": [
                            "It runs faster",
                            "Encapsulation and code reuse (Separation of concerns)",
                            "It allows inheritance"
                        ],
                        "answer": 1,
                        "explanation": "Composition breaks complex problems into smaller, testable, and reusable pieces."
                    },
                    {
                        "type": "code_lab",
                        "title": "Fire the Laser",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass Laser { public: void fire() {} };\nclass Ship {\n  Laser l;\npublic:\n  void attack() {\n    // TODO: Call fire() on the laser\n  }\n};\n\nint main() {\n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass Laser { public: void fire() {} };\nclass Ship {\n  Laser l;\npublic:\n  void attack() { l.fire(); }\n};\n\nint main() {\n    return 0;\n}\n",
                        "hint": "l.fire();",
                        "expected_output": "",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 4: Composition vs Inheritance Preview",
                "blocks": [
                    {
                        "type": "story",
                        "title": "The Architectural Dilemma",
                        "content": "Is a square a shape? Or does a square have a shape? Designing classes requires answering philosophical questions."
                    },
                    {
                        "type": "problem",
                        "content": "When should we use 'Has-A' (Composition) vs 'Is-A' (Inheritance)?"
                    },
                    {
                        "type": "concept",
                        "title": "Has-A vs Is-A",
                        "explanation": "Use composition when an object is made of other objects. Use inheritance when an object is a specialized version of another.",
                        "analogy": "A Dog IS-A Mammal (Inheritance). A Dog HAS-A Tail (Composition).",
                        "technical_explanation": "Composition provides flexibility at runtime and less tight coupling compared to inheritance."
                    },
                    {
                        "type": "mental_model",
                        "title": "Design Choice",
                        "data": "Dog -> Mammal (Is-A)\nDog -> Tail (Has-A)"
                    },
                    {
                        "type": "annotated_code",
                        "title": "The Difference",
                        "code": "// Composition\nclass Dog { Tail t; };\n// Inheritance Preview\nclass Dog : public Mammal {};",
                        "annotations": [
                            {
                                "line": "class Dog { Tail t; };",
                                "text": "Has-A"
                            }
                        ]
                    },
                    {
                        "type": "code_lab",
                        "title": "Identify the Relationship",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass Engine {};\n// TODO: Create a Truck class that HAS-A Engine\n\nint main() {\n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass Engine {};\nclass Truck { Engine e; };\n\nint main() {\n    return 0;\n}\n",
                        "hint": "class Truck { Engine e; };",
                        "expected_output": "",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            }
        ]
    },
    "11": {
        "format": "episodic",
        "episodes": [
            {
                "title": "Module 1: The Bloodline",
                "blocks": [
                    {
                        "type": "story",
                        "title": "Ancestral Traits",
                        "content": "Why write code twice when you can inherit it? The power of bloodlines enters C++."
                    },
                    {
                        "type": "mermaid_diagram",
                        "title": "Architectural Overview",
                        "explanation": "Before we write code, study this structural model to understand the relationships we are building.",
                        "code": "classDiagram\n    class NetworkNode {\n        -int nodeId\n        #string subnetKey\n        +NetworkNode(int id, string subnet)\n        +ping() bool\n        +getNodeId() int\n    }\n    class GatewayRouter {\n        -int routingTableSize\n        +GatewayRouter(int id, string subnet, int tableSize)\n        +routePacket() void\n    }\n    class SecurityFirewall {\n        -int blockedThreatsCount\n        +SecurityFirewall(int id, string subnet)\n        +inspectTraffic() bool\n    }\n    NetworkNode <|-- GatewayRouter : \"Inherits Base (Is-A)\"\n    NetworkNode <|-- SecurityFirewall : \"Inherits Base (Is-A)\" "
                    },
                    {
                        "type": "problem",
                        "content": "How do we create a new class that absorbs all the properties and behaviors of an existing class?"
                    },
                    {
                        "type": "concept",
                        "title": "Inheritance",
                        "explanation": "Inheritance models an 'Is-A' relationship, allowing a derived class to inherit from a base class.",
                        "analogy": "A blueprint for a 'Sports Car' inherits all the basics from the 'Car' blueprint, then adds a spoiler.",
                        "technical_explanation": "Use a colon after the class name, followed by an access specifier and the base class name."
                    },
                    {
                        "type": "mental_model",
                        "title": "Class Hierarchy",
                        "data": "[ Base: Animal ]\n       |\n[ Derived: Dog ]"
                    },
                    {
                        "type": "annotated_code",
                        "title": "Inheritance Syntax",
                        "code": "class Animal { public: void eat() {} };\nclass Dog : public Animal {};",
                        "annotations": [
                            {
                                "line": "class Dog : public Animal {};",
                                "text": "Dog inherits from Animal."
                            }
                        ]
                    },
                    {
                        "type": "code_lab",
                        "title": "Create the Cat",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass Animal {};\n// TODO: Create a Cat class that inherits publicly from Animal\n\nint main() {\n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass Animal {};\nclass Cat : public Animal {};\n\nint main() {\n    return 0;\n}\n",
                        "hint": "class Cat : public Animal {};",
                        "expected_output": "",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 2: Protected Secrets",
                "blocks": [
                    {
                        "type": "story",
                        "title": "Family Secrets",
                        "content": "Some things are private to an individual. Some are public to the world. But some secrets are shared only with family."
                    },
                    {
                        "type": "problem",
                        "content": "How do we hide data from the outside world, but allow derived classes to access it?"
                    },
                    {
                        "type": "concept",
                        "title": "Protected Access",
                        "explanation": "The `protected` specifier makes members accessible to derived classes, but inaccessible to the rest of the program.",
                        "analogy": "A secret family recipe: hidden from the public, but passed down to children.",
                        "technical_explanation": "Variables declared as `protected` in the base class can be used directly inside derived class methods."
                    },
                    {
                        "type": "think_first",
                        "question": "Can a class outside the hierarchy access protected members?",
                        "options": [
                            "Yes",
                            "No"
                        ],
                        "answer": 1,
                        "explanation": "Protected members act like private members to outside classes."
                    },
                    {
                        "type": "annotated_code",
                        "title": "Protected Scope",
                        "code": "class Base { protected: int secret; };\nclass Derived : public Base {\n  void reveal() { secret = 42; }\n};",
                        "annotations": [
                            {
                                "line": "protected: int secret;",
                                "text": "Accessible to Derived, but not main()."
                            }
                        ]
                    },
                    {
                        "type": "code_lab",
                        "title": "Access the Heirloom",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass Parent { protected: int gold; };\nclass Child : public Parent {\npublic:\n  void inheritGold() { /* TODO: set gold to 100 */ }\n};\n\nint main() {\n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass Parent { protected: int gold; };\nclass Child : public Parent {\npublic:\n  void inheritGold() { gold = 100; }\n};\n\nint main() {\n    return 0;\n}\n",
                        "hint": "gold = 100;",
                        "expected_output": "",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 3: Constructing the Family",
                "blocks": [
                    {
                        "type": "story",
                        "title": "The Order of Genesis",
                        "content": "Before a child can be born, the parent must exist. In C++, constructing a derived class requires first constructing its base."
                    },
                    {
                        "type": "problem",
                        "content": "How do we pass parameters to the base class constructor from the derived class?"
                    },
                    {
                        "type": "concept",
                        "title": "Base Class Initialization",
                        "explanation": "The derived class constructor must call the base class constructor in its initializer list.",
                        "analogy": "Building a house: you must lay the foundation (Base) before you build the walls (Derived).",
                        "technical_explanation": "If the base class has no default constructor, the derived class MUST explicitly call it in the initializer list."
                    },
                    {
                        "type": "execution_trace",
                        "title": "Creation Sequence",
                        "code": "Derived d;",
                        "trace": [
                            "Base constructor runs",
                            "Derived constructor runs"
                        ]
                    },
                    {
                        "type": "mastery_challenge",
                        "question": "In what order are destructors called in inheritance?",
                        "options": [
                            "Base then Derived",
                            "Derived then Base",
                            "Simultaneously"
                        ],
                        "answer": 1,
                        "explanation": "Destructors are called in reverse order of constructors (LIFO)."
                    },
                    {
                        "type": "code_lab",
                        "title": "Pass the Name",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass Entity { public: Entity(int id) {} };\nclass Player : public Entity {\npublic:\n  // TODO: Call the Entity constructor with 99 in the initializer list\n  Player() \n};\n\nint main() {\n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass Entity { public: Entity(int id) {} };\nclass Player : public Entity {\npublic:\n  Player() : Entity(99) {}\n};\n\nint main() {\n    return 0;\n}\n",
                        "hint": "Player() : Entity(99) {}",
                        "expected_output": "",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 4: The Sins of the Father",
                "blocks": [
                    {
                        "type": "story",
                        "title": "Rebellion",
                        "content": "Sometimes the parent is wrong. Sometimes the child needs to do things their own way."
                    },
                    {
                        "type": "problem",
                        "content": "How can a derived class provide a different implementation for a method defined in the base class?"
                    },
                    {
                        "type": "concept",
                        "title": "Method Hiding / Overriding",
                        "explanation": "A derived class can define a method with the exact same signature as one in the base class.",
                        "analogy": "Your parent taught you to cook steak one way, but you invented a better recipe.",
                        "technical_explanation": "Without the `virtual` keyword, this is called name hiding. The derived method hides the base method."
                    },
                    {
                        "type": "mental_model",
                        "title": "Method Resolution",
                        "data": "d.speak() -> Checks Derived. If found, use it. Else check Base."
                    },
                    {
                        "type": "annotated_code",
                        "title": "Hiding a Method",
                        "code": "class Base { public: void info() { cout << \"Base\"; } };\nclass Derived : public Base {\n  public: void info() { cout << \"Derived\"; }\n};",
                        "annotations": [
                            {
                                "line": "void info() { cout << \"Derived\"; }",
                                "text": "Hides the Base info() method."
                            }
                        ]
                    },
                    {
                        "type": "code_lab",
                        "title": "Override the Roar",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass Cat { public: void sound() {} };\nclass Lion : public Cat {\npublic:\n  // TODO: Create a sound() method that does nothing, hiding Cat's\n};\n\nint main() {\n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass Cat { public: void sound() {} };\nclass Lion : public Cat {\npublic:\n  void sound() {}\n};\n\nint main() {\n    return 0;\n}\n",
                        "hint": "void sound() {}",
                        "expected_output": "",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            }
        ]
    },
    "12": {
        "format": "episodic",
        "episodes": [
            {
                "title": "Module 1: The Shapeshifter",
                "blocks": [
                    {
                        "type": "story",
                        "title": "The Illusionist",
                        "content": "You hold a remote control for an 'Appliance'. It could be a TV, a Radio, or a Microwave. You press 'ON', and the right thing happens. This is magic."
                    },
                    {
                        "type": "mermaid_diagram",
                        "title": "Architectural Overview",
                        "explanation": "Before we write code, study this structural model to understand the relationships we are building.",
                        "code": "flowchart TD\n    subgraph ClientCode[\"Client Polymorphic Call\"]\n        CALL[\"Entity* e = new Warrior();\ne.executeAction() via pointer\"]\n    end\n    subgraph ObjectLayout[\"Warrior Memory Layout\"]\n        VPTR[\"vptr (Hidden pointer at offset 0)\"]\n        STATE[\"health = 100\narmor = 40\"]\n    end\n    subgraph VirtualTable[\"Warrior Virtual Table (vtable)\"]\n        SLOT1[\"executeAction() points to Warrior::executeAction()\"]\n        SLOT2[\"~Destructor() points to Warrior::~Warrior()\"]\n    end\n    CALL --> VPTR\n    VPTR --> VirtualTable\n    SLOT1 --> DISPATCH[\"Dynamic Dispatch: Jumps to Warrior::executeAction()\"]"
                    },
                    {
                        "type": "problem",
                        "content": "How can a pointer of the Base class type call the correct method of the Derived class object it points to?"
                    },
                    {
                        "type": "concept",
                        "title": "Polymorphism & Virtual Functions",
                        "explanation": "Polymorphism means 'many forms'. It allows base class pointers to resolve method calls at runtime based on the actual object type.",
                        "analogy": "A manager saying 'Do your job!' to employees. The programmer codes, the artist draws. Same command, different actions.",
                        "technical_explanation": "Mark the base class function with the keyword `virtual`."
                    },
                    {
                        "type": "mental_model",
                        "title": "Runtime Resolution",
                        "data": "Animal* a = new Dog();\na->speak(); -> *Runtime Checks Object Type* -> Dog::speak()"
                    },
                    {
                        "type": "annotated_code",
                        "title": "The Virtual Keyword",
                        "code": "class Base {\n  public: virtual void run() { cout << \"B\"; }\n};\nclass Derived : public Base {\n  public: void run() override { cout << \"D\"; }\n};",
                        "annotations": [
                            {
                                "line": "virtual void run()",
                                "text": "Enables polymorphism."
                            }
                        ]
                    },
                    {
                        "type": "code_lab",
                        "title": "Make it Virtual",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass Shape {\npublic:\n  // TODO: Add a virtual void draw() method\n};\n\nint main() {\n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass Shape {\npublic:\n  virtual void draw() {}\n};\n\nint main() {\n    return 0;\n}\n",
                        "hint": "virtual void draw() {}",
                        "expected_output": "",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 2: The Virtual Table",
                "blocks": [
                    {
                        "type": "story",
                        "title": "The Hidden Register",
                        "content": "How does the computer know what object it is pointing to at runtime? It uses a hidden ledger."
                    },
                    {
                        "type": "problem",
                        "content": "What is the underlying mechanism that makes polymorphism work?"
                    },
                    {
                        "type": "concept",
                        "title": "Vtables and Vptrs",
                        "explanation": "Classes with virtual functions have a Virtual Table (vtable) mapping function names to addresses. Each object has a hidden pointer (vptr) to this table.",
                        "analogy": "A business card with a forwarding address that gets updated if you move.",
                        "technical_explanation": "This introduces a tiny runtime overhead for dynamic dispatch."
                    },
                    {
                        "type": "think_first",
                        "question": "Does using virtual functions increase memory usage?",
                        "options": [
                            "Yes, due to the vptr in each object",
                            "No, it's completely free"
                        ],
                        "answer": 0,
                        "explanation": "Every object of a polymorphic class contains a vptr (typically 4 or 8 bytes)."
                    },
                    {
                        "type": "execution_trace",
                        "title": "Dynamic Dispatch",
                        "code": "ptr->draw();",
                        "trace": [
                            "Access object's vptr",
                            "Look up 'draw' in vtable",
                            "Jump to correct function address"
                        ]
                    },
                    {
                        "type": "code_lab",
                        "title": "Override Keyword",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass A { virtual void foo() {} };\nclass B : public A {\n  // TODO: override foo(), use the override keyword\n};\n\nint main() {\n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass A { virtual void foo() {} };\nclass B : public A {\n  void foo() override {}\n};\n\nint main() {\n    return 0;\n}\n",
                        "hint": "void foo() override {}",
                        "expected_output": "",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 3: Pure Interfaces",
                "blocks": [
                    {
                        "type": "story",
                        "title": "The Abstract Blueprint",
                        "content": "Some concepts are purely theoretical. You can't just instantiate a generic 'Shape'. What would it look like?"
                    },
                    {
                        "type": "problem",
                        "content": "How do we force derived classes to implement a function, preventing the base class from being instantiated?"
                    },
                    {
                        "type": "concept",
                        "title": "Abstract Classes & Pure Virtual Functions",
                        "explanation": "A pure virtual function has no implementation in the base class. A class with at least one pure virtual function is 'abstract' and cannot be instantiated.",
                        "analogy": "A contract that says 'You must provide a signature here'. The contract itself is not the action.",
                        "technical_explanation": "Syntax: `virtual void method() = 0;`"
                    },
                    {
                        "type": "mastery_challenge",
                        "question": "Can you instantiate an abstract class?",
                        "options": [
                            "Yes",
                            "No",
                            "Only dynamically with new"
                        ],
                        "answer": 1,
                        "explanation": "Abstract classes are incomplete blueprints. The compiler will block instantiation."
                    },
                    {
                        "type": "annotated_code",
                        "title": "Pure Virtual Syntax",
                        "code": "class Interface {\npublic:\n  virtual void update() = 0;\n};",
                        "annotations": [
                            {
                                "line": "= 0;",
                                "text": "This makes the function pure virtual."
                            }
                        ]
                    },
                    {
                        "type": "code_lab",
                        "title": "Design a Contract",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass Printable {\npublic:\n  // TODO: Create a pure virtual function void print() = 0;\n};\n\nint main() {\n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass Printable {\npublic:\n  virtual void print() = 0;\n};\n\nint main() {\n    return 0;\n}\n",
                        "hint": "virtual void print() = 0;",
                        "expected_output": "",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 4: The Ultimate Mastery",
                "blocks": [
                    {
                        "type": "story",
                        "title": "The Polymorphic Cleanup",
                        "content": "A deadly trap awaits those who use polymorphism with dynamic memory. Destroying a derived object through a base pointer is a recipe for memory leaks."
                    },
                    {
                        "type": "problem",
                        "content": "How do we ensure the derived class destructor is called when deleting a base class pointer?"
                    },
                    {
                        "type": "concept",
                        "title": "Virtual Destructors",
                        "explanation": "If a class has virtual functions, it MUST have a virtual destructor. Otherwise, deleting a base pointer to a derived object only calls the base destructor.",
                        "analogy": "Hiring a generic demo crew to demolish a specialized building; they might miss the hidden vault.",
                        "technical_explanation": "Declare the base class destructor as `virtual ~Base() {}`."
                    },
                    {
                        "type": "mental_model",
                        "title": "Virtual Destruction",
                        "data": "delete basePtr; -> Base Destructor Virtual? -> Calls Derived Destructor -> Calls Base Destructor"
                    },
                    {
                        "type": "annotated_code",
                        "title": "The Golden Rule",
                        "code": "class Base {\npublic:\n  virtual ~Base() {}\n};",
                        "annotations": [
                            {
                                "line": "virtual ~Base()",
                                "text": "Always virtual in base classes."
                            }
                        ]
                    },
                    {
                        "type": "code_lab",
                        "title": "Safe Deletion",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass Component {\npublic:\n  // TODO: Add a virtual destructor with an empty body\n};\n\nint main() {\n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass Component {\npublic:\n  virtual ~Component() {}\n};\n\nint main() {\n    return 0;\n}\n",
                        "hint": "virtual ~Component() {}",
                        "expected_output": "",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            }
        ]
    },
    "13": {
        "format": "episodic",
        "episodes": [
            {
                "title": "Module 1: The Monolith Crisis",
                "blocks": [
                    {
                        "type": "story",
                        "title": "The Interface That Saved The Company",
                        "content": "You are called into the CTO's office at Global Logistics Inc. The codebase for routing deliveries is a tangled mess of tightly coupled classes. Adding a new delivery method takes weeks."
                    },
                    {
                        "type": "mermaid_diagram",
                        "title": "Architectural Overview",
                        "explanation": "Before we write code, study this structural model to understand the relationships we are building.",
                        "code": "classDiagram\n    class IFileSystem {\n        +readFile(string path)* string\n        +writeFile(string path, string data)* bool\n        +deleteFile(string path)* bool\n    }\n    class LocalExt4Driver {\n        -string mountPoint\n        +readFile(string path) string\n        +writeFile(string path, string data) bool\n        +deleteFile(string path) bool\n    }\n    class S3CloudDriver {\n        -string bucketName\n        +readFile(string path) string\n        +writeFile(string path, string data) bool\n        +deleteFile(string path) bool\n    }\n    class MemoryVirtualDriver {\n        -map fileMap\n        +readFile(string path) string\n        +writeFile(string path, string data) bool\n        +deleteFile(string path) bool\n    }\n    note for IFileSystem \"Pure Abstract Interface (Contract)\"\n    IFileSystem <|.. LocalExt4Driver : \"implements pure virtual contract\"\n    IFileSystem <|.. S3CloudDriver : \"implements pure virtual contract\"\n    IFileSystem <|.. MemoryVirtualDriver : \"implements pure virtual contract\" "
                    },
                    {
                        "type": "problem",
                        "content": "The system relies on concrete classes instead of abstractions. We need a way to define a contract that any new delivery method must follow, without dictating HOW it's implemented."
                    },
                    {
                        "type": "concept",
                        "title": "Abstract Classes and Pure Virtual Functions",
                        "explanation": "An interface in C++ is simply a class with at least one pure virtual function. It defines a contract.",
                        "analogy": "Like a wall socket - it defines the interface (plugs), but doesn't care if it's powering a toaster or a TV.",
                        "technical_explanation": "A pure virtual function is declared by assigning 0 in its declaration: `virtual void doSomething() = 0;`"
                    },
                    {
                        "type": "mental_model",
                        "title": "Interface Inheritance",
                        "data": "[IDelivery] <|-- [DroneDelivery]\n            <|-- [TruckDelivery]"
                    },
                    {
                        "type": "annotated_code",
                        "title": "Defining an Interface",
                        "code": "class IDelivery {\npublic:\n    virtual ~IDelivery() = default;\n    virtual double calculateCost() const = 0;\n};",
                        "annotations": [
                            {
                                "line": "3",
                                "text": "Virtual destructor ensures proper cleanup of derived classes."
                            },
                            {
                                "line": "4",
                                "text": "The '= 0' makes this a pure virtual function."
                            }
                        ]
                    },
                    {
                        "type": "think_first",
                        "question": "Can you instantiate an object of class IDelivery?",
                        "options": [
                            "Yes, using new",
                            "No, abstract classes cannot be instantiated"
                        ],
                        "answer": 1,
                        "explanation": "Because it contains a pure virtual function, the class is abstract and cannot be directly instantiated."
                    },
                    {
                        "type": "code_lab",
                        "title": "Implement the Drone Delivery",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nstruct IDelivery {\n    virtual double calculateCost() const = 0;\n    virtual ~IDelivery() = default;\n};\n\nclass DroneDelivery : public IDelivery {\n    // TODO: implement calculateCost to return 15.50\n};\n\nint main() {\n    std::cout << \"Cost is 15.5\";\n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nstruct IDelivery {\n    virtual double calculateCost() const = 0;\n    virtual ~IDelivery() = default;\n};\n\nclass DroneDelivery : public IDelivery {\npublic:\n    double calculateCost() const override {\n        return 15.50;\n    }\n};\n\nint main() {\n    DroneDelivery d;\n    std::cout << \"Cost is \" << d.calculateCost();\n    return 0;\n}\n",
                        "hint": "Don't forget the 'override' keyword!",
                        "expected_output": "Cost is 15.5",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 2: Polymorphic Routing",
                "blocks": [
                    {
                        "type": "story",
                        "title": "Scaling Up Delivery Methods",
                        "content": "Now that we have our IDelivery interface, the routing engine needs to process a heterogeneous collection of deliveries uniformly."
                    },
                    {
                        "type": "problem",
                        "content": "How do we store different types of deliveries in a single collection and compute the total cost?"
                    },
                    {
                        "type": "concept",
                        "title": "Polymorphism with Interfaces",
                        "explanation": "By storing pointers to the base interface, we can invoke the derived class implementations at runtime.",
                        "analogy": "A manager (the router) tells all employees (deliveries) to 'work' without needing to know exactly what their specific jobs are.",
                        "technical_explanation": "This is achieved via virtual method dispatch (vtables). When calling `calculateCost()` on an `IDelivery*`, the compiler looks up the actual object's method at runtime."
                    },
                    {
                        "type": "annotated_code",
                        "title": "Processing Deliveries",
                        "code": "double totalCost(const std::vector<IDelivery*>& deliveries) {\n    double total = 0;\n    for(auto d : deliveries) {\n        total += d->calculateCost();\n    }\n    return total;\n}",
                        "annotations": [
                            {
                                "line": "1",
                                "text": "We pass a collection of interface pointers."
                            },
                            {
                                "line": "4",
                                "text": "Dynamic dispatch calls the correct derived method."
                            }
                        ]
                    },
                    {
                        "type": "execution_trace",
                        "title": "Virtual Dispatch Trace",
                        "code": "IDelivery* d = new DroneDelivery();\nd->calculateCost();",
                        "trace": [
                            "Look up vtable for DroneDelivery",
                            "Execute DroneDelivery::calculateCost"
                        ]
                    },
                    {
                        "type": "mastery_challenge",
                        "question": "What happens if we slice an object by passing it by value instead of pointer/reference?",
                        "options": [
                            "It works fine",
                            "Polymorphism is lost",
                            "Compilation error (if base is abstract)"
                        ],
                        "answer": 2,
                        "explanation": "Because abstract classes cannot be instantiated, you get a compile error if you try to pass them by value."
                    },
                    {
                        "type": "code_lab",
                        "title": "Calculate Total Cost",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nstruct IDelivery {\n    virtual double calculateCost() const = 0;\n    virtual ~IDelivery() = default;\n};\n\nstruct StandardDelivery : public IDelivery {\n    double cost;\n    StandardDelivery(double c) : cost(c) {}\n    double calculateCost() const override { return cost; }\n};\n\ndouble calculateTotal(std::vector<std::unique_ptr<IDelivery>>& v) {\n    // TODO: Sum the costs\n    return 0.0;\n}\n\nint main() {\n    std::vector<std::unique_ptr<IDelivery>> deliveries;\n    deliveries.push_back(std::make_unique<StandardDelivery>(40.0));\n    deliveries.push_back(std::make_unique<StandardDelivery>(60.0));\n    std::cout << std::fixed << std::setprecision(1) << \"Total: \" << calculateTotal(deliveries);\n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nstruct IDelivery {\n    virtual double calculateCost() const = 0;\n    virtual ~IDelivery() = default;\n};\n\nstruct StandardDelivery : public IDelivery {\n    double cost;\n    StandardDelivery(double c) : cost(c) {}\n    double calculateCost() const override { return cost; }\n};\n\ndouble calculateTotal(std::vector<std::unique_ptr<IDelivery>>& v) {\n    double sum = 0;\n    for (const auto& d : v) sum += d->calculateCost();\n    return sum;\n}\n\nint main() {\n    std::vector<std::unique_ptr<IDelivery>> deliveries;\n    deliveries.push_back(std::make_unique<StandardDelivery>(40.0));\n    deliveries.push_back(std::make_unique<StandardDelivery>(60.0));\n    std::cout << std::fixed << std::setprecision(1) << \"Total: \" << calculateTotal(deliveries);\n    return 0;\n}\n",
                        "hint": "Iterate through the vector and call calculateCost().",
                        "expected_output": "Total: 100.0",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 3: Multiple Interfaces",
                "blocks": [
                    {
                        "type": "story",
                        "title": "The Tracking Requirement",
                        "content": "The marketing team now wants to track high-priority deliveries on a map. But not all deliveries support tracking."
                    },
                    {
                        "type": "problem",
                        "content": "How do we add tracking functionality without forcing non-trackable deliveries to implement it?"
                    },
                    {
                        "type": "concept",
                        "title": "Multiple Inheritance for Interfaces",
                        "explanation": "C++ allows a class to inherit from multiple abstract base classes (interfaces).",
                        "analogy": "A person can be both a 'Pilot' and a 'Mechanic'. They adhere to two different sets of skills.",
                        "technical_explanation": "You can declare a class as `class Drone : public IDelivery, public ITrackable`. It must implement pure virtual functions from both."
                    },
                    {
                        "type": "mental_model",
                        "title": "Multiple Interfaces",
                        "data": "[IDelivery]   [ITrackable]\n      \\           /\n     [DroneDelivery]"
                    },
                    {
                        "type": "annotated_code",
                        "title": "Implementing Two Interfaces",
                        "code": "class ITrackable {\npublic:\n    virtual void pingLocation() = 0;\n};\nclass Drone : public IDelivery, public ITrackable { ... };",
                        "annotations": [
                            {
                                "line": "1",
                                "text": "New interface."
                            },
                            {
                                "line": "5",
                                "text": "Inheriting from both."
                            }
                        ]
                    },
                    {
                        "type": "think_first",
                        "question": "Is multiple inheritance of pure interfaces generally considered safe in C++?",
                        "options": [
                            "No, it leads to the diamond problem",
                            "Yes, it avoids the typical pitfalls of stateful multiple inheritance"
                        ],
                        "answer": 1,
                        "explanation": "Since interfaces have no state (member variables), the dreaded diamond problem is largely avoided."
                    },
                    {
                        "type": "code_lab",
                        "title": "Implement ITrackable",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nstruct IDelivery {\n    virtual double calculateCost() const = 0;\n    virtual ~IDelivery() = default;\n};\nstruct ITrackable {\n    virtual void pingLocation() = 0;\n    virtual ~ITrackable() = default;\n};\n\n// TODO: Make SecureTruck implement IDelivery and ITrackable\n\nint main() {\n    std::cout << \"GPS ping\";\n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nstruct IDelivery {\n    virtual double calculateCost() const = 0;\n    virtual ~IDelivery() = default;\n};\nstruct ITrackable {\n    virtual void pingLocation() = 0;\n    virtual ~ITrackable() = default;\n};\n\nclass SecureTruck : public IDelivery, public ITrackable {\npublic:\n    double calculateCost() const override { return 50.0; }\n    void pingLocation() override { std::cout << \"GPS ping\"; }\n};\n\nint main() {\n    SecureTruck truck;\n    truck.pingLocation();\n    return 0;\n}\n",
                        "hint": "Inherit from both and use override.",
                        "expected_output": "GPS ping",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 4: Interface Segregation",
                "blocks": [
                    {
                        "type": "story",
                        "title": "The God Interface",
                        "content": "A junior developer combined IDelivery and ITrackable into a single huge interface."
                    },
                    {
                        "type": "problem",
                        "content": "Now simple bicycle couriers are forced to implement pingLocation(), which they don't support!"
                    },
                    {
                        "type": "concept",
                        "title": "The Interface Segregation Principle (ISP)",
                        "explanation": "Clients should not be forced to depend on interfaces they do not use.",
                        "analogy": "Don't sell someone a swiss army knife when they just need a spoon.",
                        "technical_explanation": "Break fat interfaces into smaller, specialized ones."
                    },
                    {
                        "type": "mental_model",
                        "title": "Segregated Interfaces",
                        "data": "Bad: [IDeliveryAndTrackable]\nGood: [IDelivery] [ITrackable]"
                    },
                    {
                        "type": "annotated_code",
                        "title": "Applying ISP",
                        "code": "class Bicycle : public IDelivery {\n    // Only needs to care about delivery cost!\n};",
                        "annotations": [
                            {
                                "line": "1",
                                "text": "Bicycle doesn't implement ITrackable."
                            }
                        ]
                    },
                    {
                        "type": "mastery_challenge",
                        "question": "What SOLID principle does this demonstrate?",
                        "options": [
                            "Single Responsibility",
                            "Interface Segregation",
                            "Dependency Inversion"
                        ],
                        "answer": 1,
                        "explanation": "ISP states that no code should be forced to depend on methods it does not use."
                    },
                    {
                        "type": "code_lab",
                        "title": "Fix the Interface",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass IGod { virtual void a()=0; virtual void b()=0; }; // TODO: Split this\n\nint main() {\n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass IA { public: virtual void a()=0; };\nclass IB { public: virtual void b()=0; };\n\nint main() {\n    return 0;\n}\n",
                        "hint": "Create two separate abstract classes.",
                        "expected_output": "",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            }
        ]
    },
    "14": {
        "format": "episodic",
        "episodes": [
            {
                "title": "Module 1: The Shallow Disaster",
                "blocks": [
                    {
                        "type": "story",
                        "title": "The Copy That Cost A Million",
                        "content": "A bug in the automated trading system caused a massive loss. The root cause? A seemingly innocent copy assignment."
                    },
                    {
                        "type": "mermaid_diagram",
                        "title": "Architectural Overview",
                        "explanation": "Before we write code, study this structural model to understand the relationships we are building.",
                        "code": "flowchart TD\n    subgraph ShallowCopyTrap[\"Shallow Copy (Default Memberwise Copy Trap)\"]\n        A1[\"Source Object A\nptr = 0x5000\"]\n        B1[\"Copied Object B\nptr = 0x5000 (Same Pointer!)\"]\n        HEAP1[\"Single Heap Buffer (0x5000)\"]\n        A1 --> HEAP1\n        B1 --> HEAP1\n        CRASH[\"~ObjectA() deletes 0x5000\n~ObjectB() deletes 0x5000\nCRITICAL: Double Free Crash!\"]\n    end\n    subgraph DeepCopyPattern[\"Deep Copy (Rule of Three Implementation)\"]\n        A2[\"Source Object A\nptr = 0x6000\"]\n        B2[\"Copied Object B\nptr = 0x7000 (Fresh Allocation)\"]\n        HEAP2[\"Heap Buffer (0x6000)\"]\n        HEAP3[\"Cloned Heap Buffer (0x7000)\"]\n        A2 --> HEAP2\n        B2 --> HEAP3\n        SAFE[\"Independent Lifecycles\nBoth Destructors Free Safely\"]\n    end"
                    },
                    {
                        "type": "problem",
                        "content": "When an object holding a raw pointer was copied, both objects pointed to the same memory. When one was destroyed, the other was left with a dangling pointer!"
                    },
                    {
                        "type": "concept",
                        "title": "Shallow Copy vs Deep Copy",
                        "explanation": "A shallow copy copies pointer addresses. A deep copy allocates new memory and copies the actual data.",
                        "analogy": "Shallow copy: Sharing the same remote control for a TV. Deep copy: Buying a second TV and a second remote.",
                        "technical_explanation": "The default compiler-generated copy constructor performs a shallow copy (member-wise copy)."
                    },
                    {
                        "type": "mental_model",
                        "title": "Shallow Copy",
                        "data": "Obj1.ptr ---> [ Data ]\nObj2.ptr -------^"
                    },
                    {
                        "type": "annotated_code",
                        "title": "The Danger of Default Copy",
                        "code": "class DataBuffer {\n    int* data;\npublic:\n    DataBuffer() { data = new int[100]; }\n    ~DataBuffer() { delete[] data; }\n};",
                        "annotations": [
                            {
                                "line": "2",
                                "text": "Raw pointer."
                            },
                            {
                                "line": "5",
                                "text": "Deallocates memory. If shallow copied, double free occurs!"
                            }
                        ]
                    },
                    {
                        "type": "think_first",
                        "question": "What happens when two DataBuffers are destroyed if one was copied from another via default copy constructor?",
                        "options": [
                            "Memory leak",
                            "Double free crash",
                            "Everything is fine"
                        ],
                        "answer": 1,
                        "explanation": "Both destructors try to delete the same memory address."
                    },
                    {
                        "type": "code_lab",
                        "title": "Identify the Bug",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nvoid process(DataBuffer buf) { } // TODO: Why is this bad?\n\nint main() {\n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\n// buf is copied by value, triggering shallow copy. Use const reference instead.\n\nint main() {\n    return 0;\n}\n",
                        "hint": "Pass by value calls the copy constructor.",
                        "expected_output": "",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 2: The Copy Constructor",
                "blocks": [
                    {
                        "type": "story",
                        "title": "Taking Control of Copies",
                        "content": "To fix the trading bot, we must explicitly define how objects of our class are copied."
                    },
                    {
                        "type": "problem",
                        "content": "We need to instruct the compiler to allocate new memory and copy the data when a copy occurs."
                    },
                    {
                        "type": "concept",
                        "title": "Writing a Copy Constructor",
                        "explanation": "The copy constructor is a special constructor invoked when an object is initialized from another object of the same type.",
                        "analogy": "A photocopier that doesn't just link to the original document, but creates a completely independent physical duplicate.",
                        "technical_explanation": "Signature is typically `ClassName(const ClassName& other)`."
                    },
                    {
                        "type": "mental_model",
                        "title": "Deep Copy",
                        "data": "Obj1.ptr ---> [ Data A ]\nObj2.ptr ---> [ Data B (Copy) ]"
                    },
                    {
                        "type": "annotated_code",
                        "title": "Deep Copy Implementation",
                        "code": "DataBuffer(const DataBuffer& other) {\n    data = new int[100];\n    std::copy(other.data, other.data + 100, data);\n}",
                        "annotations": [
                            {
                                "line": "1",
                                "text": "Takes a const reference to the source object."
                            },
                            {
                                "line": "2",
                                "text": "Allocates fresh memory."
                            },
                            {
                                "line": "3",
                                "text": "Copies the actual values."
                            }
                        ]
                    },
                    {
                        "type": "execution_trace",
                        "title": "Deep Copy in Action",
                        "code": "DataBuffer a;\nDataBuffer b = a;",
                        "trace": [
                            "a allocates memory",
                            "b calls copy constructor",
                            "b allocates its own memory",
                            "data copied"
                        ]
                    },
                    {
                        "type": "mastery_challenge",
                        "question": "Which of these triggers the copy constructor?",
                        "options": [
                            "DataBuffer b = a;",
                            "DataBuffer b; b = a;",
                            "DataBuffer* b = &a;"
                        ],
                        "answer": 0,
                        "explanation": "Initialization (`=`) triggers the copy constructor. Assignment to an existing object triggers the copy assignment operator."
                    },
                    {
                        "type": "code_lab",
                        "title": "Implement the Copy Constructor",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass String {\n    char* str;\npublic:\n    String(const char* s = \"\") {\n        str = new char[strlen(s) + 1];\n        strcpy(str, s);\n    }\n    String(const String& other) {\n        // TODO: Allocate new buffer and copy other.str safely\n        str = new char[1]{'\\0'};\n    }\n    ~String() { delete[] str; }\n    const char* c_str() const { return str; }\n};\n\nint main() {\n    String a(\"OOP\");\n    String b = a;\n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass String {\n    char* str;\npublic:\n    String(const char* s = \"\") {\n        str = new char[strlen(s) + 1];\n        strcpy(str, s);\n    }\n    String(const String& other) {\n        str = new char[strlen(other.str) + 1];\n        strcpy(str, other.str);\n    }\n    ~String() { delete[] str; }\n    const char* c_str() const { return str; }\n};\n\nint main() {\n    String a(\"OOP\");\n    String b = a;\n    return 0;\n}\n",
                        "hint": "Allocate new char array and strcpy.",
                        "expected_output": "",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 3: Copy Assignment",
                "blocks": [
                    {
                        "type": "story",
                        "title": "The Assignment Bug",
                        "content": "Even after adding a copy constructor, the system still crashed. The devs forgot about assignment!"
                    },
                    {
                        "type": "problem",
                        "content": "Assigning an already initialized object to another existing object bypasses the copy constructor and uses the copy assignment operator."
                    },
                    {
                        "type": "concept",
                        "title": "The Copy Assignment Operator",
                        "explanation": "Used when assigning an already existing object to another. You must handle self-assignment and clean up old memory before copying new data.",
                        "analogy": "Replacing the contents of a filing cabinet. You first empty it out, then duplicate the new files into it.",
                        "technical_explanation": "Signature: `ClassName& operator=(const ClassName& other)`."
                    },
                    {
                        "type": "annotated_code",
                        "title": "Safe Assignment",
                        "code": "DataBuffer& operator=(const DataBuffer& other) {\n    if (this != &other) {\n        delete[] data;\n        data = new int[100];\n        std::copy(other.data, other.data + 100, data);\n    }\n    return *this;\n}",
                        "annotations": [
                            {
                                "line": "2",
                                "text": "Crucial: self-assignment check!"
                            },
                            {
                                "line": "3",
                                "text": "Free existing resource."
                            },
                            {
                                "line": "7",
                                "text": "Return reference to self to support chained assignment a = b = c;"
                            }
                        ]
                    },
                    {
                        "type": "think_first",
                        "question": "Why is the self-assignment check (`if (this != &other)`) so important?",
                        "options": [
                            "For performance only",
                            "Because we might delete the data we are trying to copy"
                        ],
                        "answer": 1,
                        "explanation": "If you do `a = a;`, without the check, it deletes `a`'s data, then tries to copy from it, which is undefined behavior."
                    },
                    {
                        "type": "mental_model",
                        "title": "Rule of Three",
                        "data": "If you need one of [Destructor, Copy Constructor, Copy Assignment], you almost certainly need all three."
                    },
                    {
                        "type": "code_lab",
                        "title": "Implement Assignment",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass String {\n    char* str;\npublic:\n    String(const char* s = \"\") {\n        str = new char[strlen(s) + 1];\n        strcpy(str, s);\n    }\n    String(const String& other) {\n        str = new char[strlen(other.str) + 1];\n        strcpy(str, other.str);\n    }\n    String& operator=(const String& other) {\n        // TODO: Guard self-assignment, free old buffer, deep copy other.str\n        return *this;\n    }\n    ~String() { delete[] str; }\n};\n\nint main() {\n    String a(\"Alpha\"), b(\"Beta\");\n    b = a;\n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass String {\n    char* str;\npublic:\n    String(const char* s = \"\") {\n        str = new char[strlen(s) + 1];\n        strcpy(str, s);\n    }\n    String(const String& other) {\n        str = new char[strlen(other.str) + 1];\n        strcpy(str, other.str);\n    }\n    String& operator=(const String& other) {\n        if (this != &other) {\n            delete[] str;\n            str = new char[strlen(other.str) + 1];\n            strcpy(str, other.str);\n        }\n        return *this;\n    }\n    ~String() { delete[] str; }\n};\n\nint main() {\n    String a(\"Alpha\"), b(\"Beta\");\n    b = a;\n    return 0;\n}\n",
                        "hint": "Check self-assignment, delete old, allocate new, copy, return *this.",
                        "expected_output": "",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 4: The Rule of Three (and Five)",
                "blocks": [
                    {
                        "type": "story",
                        "title": "Modernizing the Codebase",
                        "content": "You've successfully implemented deep copying. The system is stable. But the senior architect points out a modern C++ best practice."
                    },
                    {
                        "type": "problem",
                        "content": "Manually managing memory is tedious and error-prone. How do modern C++ developers handle this?"
                    },
                    {
                        "type": "concept",
                        "title": "Rule of Zero and Smart Pointers",
                        "explanation": "Instead of writing the big three, rely on classes that manage their own resources (like std::string or std::vector) or use smart pointers.",
                        "analogy": "Instead of manually hiring and firing staff (memory), use an HR agency (smart pointers) that handles it automatically.",
                        "technical_explanation": "If a class only contains members that have well-defined copy semantics, the compiler-generated defaults are perfectly safe (Rule of Zero)."
                    },
                    {
                        "type": "mental_model",
                        "title": "Rule of Zero",
                        "data": "No custom destructor -> No custom copy -> Safe defaults!"
                    },
                    {
                        "type": "annotated_code",
                        "title": "Refactoring to Rule of Zero",
                        "code": "class ModernBuffer {\n    std::vector<int> data;\npublic:\n    ModernBuffer() : data(100) {}\n    // No destructor, no copy constructor needed!\n};",
                        "annotations": [
                            {
                                "line": "2",
                                "text": "std::vector handles its own memory and deep copying automatically."
                            }
                        ]
                    },
                    {
                        "type": "mastery_challenge",
                        "question": "What happens when you copy a class that only contains a std::unique_ptr?",
                        "options": [
                            "Deep copy",
                            "Shallow copy",
                            "Compilation error"
                        ],
                        "answer": 2,
                        "explanation": "unique_ptr deletes its copy constructor. A class holding it also becomes non-copyable by default."
                    },
                    {
                        "type": "code_lab",
                        "title": "Refactor with unique_ptr",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass DB { int* d; }; // TODO: Make non-copyable using unique_ptr\n\nint main() {\n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass DB {\n    std::unique_ptr<int[]> d;\npublic:\n    DB() : d(std::make_unique<int[]>(100)) {}\n};\n\nint main() {\n    return 0;\n}\n",
                        "hint": "Replace int* with std::unique_ptr<int[]>",
                        "expected_output": "",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            }
        ]
    },
    "15": {
        "format": "episodic",
        "episodes": [
            {
                "title": "Module 1: The Curse of Unnecessary Copies",
                "blocks": [
                    {
                        "type": "header",
                        "title": "Move Semantics",
                        "subtitle": "The problem with copying",
                        "metadata": {
                            "difficulty": "Intermediate",
                            "time": "25 min",
                            "concepts": [
                                "Copying",
                                "Performance"
                            ]
                        }
                    },
                    {
                        "type": "mermaid_diagram",
                        "title": "Architectural Overview",
                        "explanation": "Before we write code, study this structural model to understand the relationships we are building.",
                        "code": "flowchart TD\n    subgraph BeforeMove[\"1. Before Move: Temporary Rvalue Source\"]\n        SRC[\"Expiring Temporary Object\n- dataPtr: 0xA000\n- size: 1,000,000\"]\n        HEAP[\"Heap Buffer (0xA000)\nLarge Dataset (1,000,000 items)\"]\n        DEST[\"New Destination Object\"]\n        SRC --> HEAP\n    end\n    subgraph MoveExecution[\"2. Move Constructor (std::move Pointer Steal)\"]\n        STEAL[\"Destination copies pointer: dataPtr = 0xA000\nSource pointer nulled: dataPtr = nullptr\nO(1) Constant Time Efficiency!\"]\n    end\n    subgraph AfterMove[\"3. After Move: Zero Reallocation\"]\n        SRC_EMPTY[\"Source Object\n- dataPtr: nullptr (Safe to destruct)\"]\n        DEST_FULL[\"Destination Object\n- dataPtr: 0xA000 (New Owner)\"]\n        DEST_FULL --> HEAP\n    end"
                    },
                    {
                        "type": "story",
                        "title": "A Heavy Burden",
                        "content": "In the early days of your C++ career, you loved the simplicity of pass-by-value. But as your programs grew, handling large matrices and massive strings, your profiler started screaming. The culprit? Endless, invisible copying."
                    },
                    {
                        "type": "annotated_code",
                        "title": "The Invisible Copy",
                        "code": "std::vector<int> createVector() {\n    std::vector<int> v(1000000, 42);\n    return v;\n}\n\nint main() {\n    std::vector<int> myVec = createVector();\n}",
                        "annotations": [
                            {
                                "line": "return v;",
                                "text": "Historically, this could trigger a full copy of 1,000,000 ints just to pass the data back to the caller."
                            }
                        ]
                    },
                    {
                        "type": "concept",
                        "title": "Why Copy When You Can Steal?",
                        "content": "If the source object (like `v` in the function above) is about to be destroyed anyway, why spend time copying its data? What if we could just 'steal' its internal pointers? That's the core idea behind Move Semantics."
                    },
                    {
                        "type": "think_first",
                        "question": "If we steal the data pointer from a dying vector, what should we set the dying vector's pointer to?",
                        "options": [
                            "Leave it as is",
                            "Set it to nullptr",
                            "Delete it"
                        ],
                        "answer": 1,
                        "explanation": "If we leave it as is, the dying vector's destructor will free the memory we just stole. Setting it to nullptr ensures the destructor does nothing."
                    },
                    {
                        "type": "mental_model",
                        "title": "Copy vs Move",
                        "data": "COPY:\n[Obj A] -> [Data Block 1]\n[Obj B] -> (Copies) -> [Data Block 2]\n\nMOVE:\n[Obj A] -> [Data Block 1]\n[Obj B] -> (Steals) -> [Data Block 1]\n[Obj A] -> nullptr"
                    },
                    {
                        "type": "wrong_approach",
                        "title": "Pre-C++11 Workarounds",
                        "code": "void createVector(std::vector<int>& outVec) {\n    outVec.assign(1000000, 42);\n}",
                        "explanation": "Before move semantics, developers used output parameters to avoid copies. It worked, but it made code less readable."
                    },
                    {
                        "type": "real_world_analogy",
                        "title": "The Moving Truck",
                        "content": "Copying is like building a replica of your house at the new location. Moving is just taking your furniture in a truck to the new house. Much faster!"
                    }
                ]
            },
            {
                "title": "Module 2: Lvalues and Rvalues",
                "blocks": [
                    {
                        "type": "header",
                        "title": "Value Categories",
                        "subtitle": "Lvalues vs Rvalues",
                        "metadata": {
                            "difficulty": "Intermediate",
                            "time": "20 min",
                            "concepts": [
                                "lvalue",
                                "rvalue",
                                "temporary"
                            ]
                        }
                    },
                    {
                        "type": "story",
                        "title": "The Identity Crisis",
                        "content": "To understand how C++ knows an object is 'about to be destroyed', you must first understand the fundamental divide in C++ expressions: lvalues and rvalues."
                    },
                    {
                        "type": "concept",
                        "title": "Lvalues: Objects with an Identity",
                        "content": "An lvalue (locator value) represents an object that occupies an identifiable location in memory. You can take its address using the `&` operator."
                    },
                    {
                        "type": "concept",
                        "title": "Rvalues: Temporary Expressions",
                        "content": "An rvalue is typically a temporary value that does not have a persistent memory address. It's often the result of an expression or a literal."
                    },
                    {
                        "type": "annotated_code",
                        "title": "Spot the Difference",
                        "code": "int a = 5;\nint b = a + 10;",
                        "annotations": [
                            {
                                "line": "int a = 5;",
                                "text": "'a' is an lvalue. '5' is an rvalue."
                            },
                            {
                                "line": "int b = a + 10;",
                                "text": "'b' is an lvalue. 'a + 10' is an rvalue (a temporary result)."
                            }
                        ]
                    },
                    {
                        "type": "think_first",
                        "question": "Can you put an rvalue on the left side of an assignment operator? e.g. `5 = a;`",
                        "options": [
                            "Yes",
                            "No"
                        ],
                        "answer": 1,
                        "explanation": "No. An rvalue is temporary and has no memory address to store a new value into."
                    },
                    {
                        "type": "comparison_table",
                        "title": "Lvalues vs Rvalues",
                        "headers": [
                            "Property",
                            "Lvalue",
                            "Rvalue"
                        ],
                        "rows": [
                            [
                                "Has Name?",
                                "Usually Yes",
                                "Usually No"
                            ],
                            [
                                "Can take address (&)?",
                                "Yes",
                                "No"
                            ],
                            [
                                "Examples",
                                "Variables, references",
                                "Literals (5, 'x'), temporary expressions (x + y)"
                            ]
                        ]
                    },
                    {
                        "type": "execution_trace",
                        "title": "Addressability",
                        "code": "int x = 10;\nint* ptr1 = &x; // OK\n// int* ptr2 = &(x + 1); // ERROR: Cannot take address of rvalue",
                        "trace": [
                            "x is an lvalue, address can be taken.",
                            "(x + 1) evaluates to 11, stored temporarily in a CPU register or hidden stack slot.",
                            "Trying to take address of (x + 1) fails."
                        ]
                    }
                ]
            },
            {
                "title": "Module 3: Rvalue References (&&) and std::move",
                "blocks": [
                    {
                        "type": "header",
                        "title": "Grabbing the Temporary",
                        "subtitle": "Rvalue References",
                        "metadata": {
                            "difficulty": "Advanced",
                            "time": "30 min",
                            "concepts": [
                                "Rvalue References",
                                "std::move"
                            ]
                        }
                    },
                    {
                        "type": "story",
                        "title": "Binding the Unbindable",
                        "content": "Now that we know what an rvalue is, how do we write functions that specifically target them? Enter the rvalue reference: `&&`."
                    },
                    {
                        "type": "concept",
                        "title": "Rvalue References (&&)",
                        "content": "An rvalue reference (Type&&) is a new type of reference introduced in C++11 that can ONLY bind to rvalues (temporaries). It allows you to modify temporary objects before they die."
                    },
                    {
                        "type": "annotated_code",
                        "title": "Lvalue vs Rvalue References",
                        "code": "void print(int& x) { std::cout << \"Lvalue\\n\"; }\nvoid print(int&& x) { std::cout << \"Rvalue\\n\"; }\n\nint main() {\n    int a = 5;\n    print(a); \n    print(10);\n}",
                        "annotations": [
                            {
                                "line": "print(a);",
                                "text": "Calls print(int&) because 'a' is an lvalue."
                            },
                            {
                                "line": "print(10);",
                                "text": "Calls print(int&&) because '10' is an rvalue."
                            }
                        ]
                    },
                    {
                        "type": "concept",
                        "title": "Forcing a Move: std::move",
                        "content": "What if you have an lvalue, but you know you're done with it and want to treat it as an rvalue so it can be moved from? You cast it using `std::move()`."
                    },
                    {
                        "type": "mental_model",
                        "title": "std::move is just a cast",
                        "data": "std::move(x) does NOT move anything.\nIt just says to the compiler: 'Treat x as an rvalue (Type&&)'."
                    },
                    {
                        "type": "code_lab",
                        "title": "Using std::move",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nint main() {\n    std::string str = \"HeapAllocatedTelemetryPayloadBuffer\";\n    // TODO: Create std::string str2 and use std::move to steal from str\n    \n    std::cout << \"str is now: \" << str << \"\\n\";\n    return 0;\n}\n",
                        "expected_output": "str is now: \n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nint main() {\n    std::string str = \"HeapAllocatedTelemetryPayloadBuffer\";\n    std::string str2 = std::move(str);\n    (void)str2;\n    std::cout << \"str is now: \" << str << \"\\n\";\n    return 0;\n}\n",
                        "hint": "Read the comments carefully and fill in the missing C++ logic.",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    },
                    {
                        "type": "think_first",
                        "question": "After calling `std::string str2 = std::move(str);`, what is the state of `str`?",
                        "options": [
                            "Destroyed, cannot be accessed",
                            "Valid but unspecified state (usually empty)",
                            "Unchanged"
                        ],
                        "answer": 1,
                        "explanation": "Moving from a standard library object leaves it in a 'valid but unspecified state'. You can reassign to it, but you shouldn't assume its exact contents (though for strings, it's typically empty)."
                    }
                ]
            },
            {
                "title": "Module 4: Move Constructors & Move Assignment",
                "blocks": [
                    {
                        "type": "header",
                        "title": "Implementing Move Semantics",
                        "subtitle": "Move Constructors",
                        "metadata": {
                            "difficulty": "Advanced",
                            "time": "40 min",
                            "concepts": [
                                "Move Constructor",
                                "Move Assignment"
                            ]
                        }
                    },
                    {
                        "type": "story",
                        "title": "Writing the Thief",
                        "content": "We've seen how to identify temporaries. Now, let's write the code inside our custom classes that actually 'steals' the data."
                    },
                    {
                        "type": "annotated_code",
                        "title": "The Move Constructor",
                        "code": "class String {\n    char* data;\n    size_t size;\npublic:\n    // Move Constructor\n    String(String&& other) noexcept \n        : data(other.data), size(other.size) { // 1. Steal data\n        other.data = nullptr; // 2. Nullify source\n        other.size = 0;\n    }\n};",
                        "annotations": [
                            {
                                "line": "String(String&& other) noexcept",
                                "text": "Takes an rvalue reference to another String."
                            },
                            {
                                "line": "data(other.data)",
                                "text": "Copy the pointer, not the deep array. Shallow copy."
                            },
                            {
                                "line": "other.data = nullptr;",
                                "text": "Crucial! Prevent the 'other' destructor from freeing our newly stolen memory."
                            }
                        ]
                    },
                    {
                        "type": "concept",
                        "title": "The 'noexcept' keyword",
                        "content": "Notice `noexcept`? Move constructors should almost always be marked `noexcept`. Standard library containers like `std::vector` will refuse to use your move constructor when resizing if it isn't `noexcept`, falling back to the slower copy constructor to guarantee strong exception safety."
                    },
                    {
                        "type": "annotated_code",
                        "title": "Move Assignment Operator",
                        "code": "String& operator=(String&& other) noexcept {\n    if (this != &other) {\n        delete[] data; // Clean up current resources\n        data = other.data; // Steal\n        size = other.size;\n        other.data = nullptr; // Nullify\n        other.size = 0;\n    }\n    return *this;\n}",
                        "annotations": [
                            {
                                "line": "if (this != &other)",
                                "text": "Protect against self-assignment: `str = std::move(str)`"
                            },
                            {
                                "line": "delete[] data;",
                                "text": "We are replacing our current state, so we must clean up our old resources first."
                            }
                        ]
                    },
                    {
                        "type": "common_mistakes",
                        "title": "Forgetting to nullify the source pointer",
                        "mistakes": [
                            {
                                "title": "Double Free Bug",
                                "desc": "If you just copy the pointer and don't set the source's pointer to nullptr, both destructors will try to delete the same memory block."
                            }
                        ]
                    },
                    {
                        "type": "problem",
                        "content": "In a move assignment operator, why do we need to `delete[] data` before stealing the new data?"
                    },
                    {
                        "type": "mastery_challenge",
                        "title": "Move Assignment Nuance",
                        "question": "What happens if you omit the `if (this != &other)` check in a move assignment operator and do `x = std::move(x);`?",
                        "options": [
                            "Nothing, it works fine.",
                            "It causes a double free.",
                            "You delete your own data, then set your pointers to nullptr, effectively wiping out the object."
                        ],
                        "answer": 2,
                        "explanation": "If `other` and `this` are the same, `delete[] data` destroys your own data. Then `data = other.data` assigns the now-deleted pointer to itself, and `other.data = nullptr` sets your own pointer to null."
                    }
                ]
            },
            {
                "title": "Module 5: The Rule of Five",
                "blocks": [
                    {
                        "type": "header",
                        "title": "The Rule of Five",
                        "subtitle": "Managing C++ class lifecycles",
                        "metadata": {
                            "difficulty": "Advanced",
                            "time": "25 min",
                            "concepts": [
                                "Rule of Three",
                                "Rule of Five"
                            ]
                        }
                    },
                    {
                        "type": "story",
                        "title": "From Three to Five",
                        "content": "In older C++, if your class managed a resource (like raw memory), you needed a custom Destructor, Copy Constructor, and Copy Assignment operator (The Rule of Three). With C++11 and move semantics, this evolved."
                    },
                    {
                        "type": "concept",
                        "title": "The Rule of Five",
                        "content": "If a class requires a user-defined destructor, a user-defined copy constructor, or a user-defined copy assignment operator, it almost certainly requires all five:\n1. Destructor\n2. Copy Constructor\n3. Copy Assignment Operator\n4. Move Constructor\n5. Move Assignment Operator"
                    },
                    {
                        "type": "comparison_table",
                        "title": "Special Member Functions",
                        "headers": [
                            "Function",
                            "Signature",
                            "Purpose"
                        ],
                        "rows": [
                            [
                                "Copy Constructor",
                                "T(const T&)",
                                "Create new object from existing (deep copy)"
                            ],
                            [
                                "Move Constructor",
                                "T(T&&)",
                                "Create new object by stealing from temporary"
                            ],
                            [
                                "Copy Assignment",
                                "T& operator=(const T&)",
                                "Replace existing object state (deep copy)"
                            ],
                            [
                                "Move Assignment",
                                "T& operator=(T&&)",
                                "Replace existing object state (steal)"
                            ],
                            [
                                "Destructor",
                                "~T()",
                                "Clean up resources"
                            ]
                        ]
                    },
                    {
                        "type": "concept",
                        "title": "Rule of Zero",
                        "content": "The best code is no code. The 'Rule of Zero' states that you should design your classes such that you don't need ANY of these five functions. How? By using standard library containers (`std::vector`, `std::string`) or Smart Pointers which handle their own resources automatically!"
                    },
                    {
                        "type": "think_first",
                        "question": "If a class only contains an `int` and a `std::string`, do you need to write a custom move constructor for it?",
                        "options": [
                            "Yes, to ensure the string moves.",
                            "No, the compiler-generated default will automatically move the string member."
                        ],
                        "answer": 1,
                        "explanation": "The compiler automatically generates move constructors that perform member-wise moves. Since `std::string` has its own move constructor, the default move constructor for your class will correctly move the string!"
                    },
                    {
                        "type": "wrong_approach",
                        "title": "The Over-Engineering Trap",
                        "code": "class User {\n    std::string name;\npublic:\n    User(User&& other) : name(std::move(other.name)) {}\n    // ... defining all 5 manually ...\n};",
                        "explanation": "By manually defining a move constructor, you suppress the implicit generation of copy constructors! If all members manage their own resources (like std::string), just let the compiler do it (Rule of Zero)."
                    },
                    {
                        "type": "code_lab",
                        "title": "Embracing the Compiler",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass Widget {\n    int id;\npublic:\n    Widget(int i) : id(i) {}\n    // Force the compiler to generate default move operations\n    Widget(Widget&&) = default;\n    Widget& operator=(Widget&&) = default;\n};\n\nint main() {\n    return 0;\n}\n",
                        "expected_output": "",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass Widget {\n    int id;\npublic:\n    Widget(int i) : id(i) {}\n    // Force the compiler to generate default move operations\n    Widget(Widget&&) = default;\n    Widget& operator=(Widget&&) = default;\n};\n\nint main() {\n    return 0;\n}\n",
                        "hint": "Fill in the missing parts of the code.",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            }
        ]
    },
    "16": {
        "format": "episodic",
        "episodes": [
            {
                "title": "Module 1: The Perils of Manual Management",
                "blocks": [
                    {
                        "type": "header",
                        "title": "RAII",
                        "subtitle": "The problem of leaks",
                        "metadata": {
                            "difficulty": "Intermediate",
                            "time": "20 min",
                            "concepts": [
                                "Memory Leaks",
                                "Exceptions"
                            ]
                        }
                    },
                    {
                        "type": "mermaid_diagram",
                        "title": "Architectural Overview",
                        "explanation": "Before we write code, study this structural model to understand the relationships we are building.",
                        "code": "stateDiagram-v2\n    [*] --> UnlockedState: Mutex / Resource Available\n    UnlockedState --> ResourceAcquired: RAII Object Initialized in Scope\n    state ProtectedScope {\n        [*] --> PerformWork\n        PerformWork --> NormalExit: Tasks Completed Successfully\n        PerformWork --> ExceptionThrown: Runtime Error or Early Return\n    }\n    ResourceAcquired --> ProtectedScope: Mutex Locked Automatically\n    NormalExit --> DestructorRelease: Scope Closes\n    ExceptionThrown --> DestructorRelease: Stack Unwinding Triggered\n    DestructorRelease --> UnlockedState: Mutex Unlocked Automatically in Destructor\n    UnlockedState --> [*]: Zero Resource Leaks / Zero Deadlocks"
                    },
                    {
                        "type": "story",
                        "title": "A Memory Sieve",
                        "content": "You've written a brilliant function that dynamically allocates a buffer, reads a file, processes it, and deletes the buffer. It works perfectly. Until one day, the file read throws an exception. The function exits early, the `delete` statement is skipped, and the memory is lost forever."
                    },
                    {
                        "type": "annotated_code",
                        "title": "The Classic Leak",
                        "code": "void processFile() {\n    int* buffer = new int[1000];\n    \n    if (errorOccurs()) {\n        return; // LEAK! buffer is never deleted\n    }\n    \n    process(buffer);\n    delete[] buffer;\n}",
                        "annotations": [
                            {
                                "line": "return; // LEAK!",
                                "text": "Any early return, break, or exception that bypasses the `delete` causes a resource leak."
                            }
                        ]
                    },
                    {
                        "type": "wrong_approach",
                        "title": "The C-Style Fix (Goto or Pyramid of Doom)",
                        "code": "void processFile() {\n    int* buffer = new int[1000];\n    if (!errorOccurs()) {\n        process(buffer);\n    }\n    delete[] buffer;\n}",
                        "explanation": "While this works for one resource, try doing this with 5 different resources (files, locks, memory). The nested 'if' statements or 'goto cleanup' labels become unreadable."
                    },
                    {
                        "type": "concept",
                        "title": "The C++ Way",
                        "content": "C++ offers a deterministic feature: Local variables (allocated on the stack) are GUARANTEED to be destroyed when they go out of scope, regardless of how the scope is exited (normal return, exception, etc.)."
                    },
                    {
                        "type": "think_first",
                        "question": "If an exception is thrown inside a function, are local stack variables destroyed?",
                        "options": [
                            "Yes, through a process called stack unwinding.",
                            "No, the program just aborts."
                        ],
                        "answer": 0,
                        "explanation": "C++ guarantees that destructors of all fully constructed local objects are called during exception stack unwinding."
                    }
                ]
            },
            {
                "title": "Module 2: Enter RAII",
                "blocks": [
                    {
                        "type": "header",
                        "title": "Resource Acquisition Is Initialization",
                        "subtitle": "The core idiom of C++",
                        "metadata": {
                            "difficulty": "Intermediate",
                            "time": "25 min",
                            "concepts": [
                                "RAII",
                                "Constructors",
                                "Destructors"
                            ]
                        }
                    },
                    {
                        "type": "story",
                        "title": "The Guardian of the Scope",
                        "content": "Bjarne Stroustrup invented a technique to solve the resource leak problem elegantly. It has a terrible name (RAII), but it is the most important idiom in C++."
                    },
                    {
                        "type": "concept",
                        "title": "What is RAII?",
                        "content": "RAII stands for Resource Acquisition Is Initialization. It means:\n1. Encapsulate a resource (memory, file, socket) inside a class.\n2. Acquire the resource in the Constructor.\n3. Release the resource in the Destructor."
                    },
                    {
                        "type": "annotated_code",
                        "title": "A Simple RAII Wrapper",
                        "code": "class IntBuffer {\n    int* ptr;\npublic:\n    IntBuffer(size_t size) { ptr = new int[size]; }\n    ~IntBuffer() { delete[] ptr; }\n    int* get() { return ptr; }\n};",
                        "annotations": [
                            {
                                "line": "IntBuffer(size_t size)",
                                "text": "Resource Acquisition (new) happens during Initialization (constructor)."
                            },
                            {
                                "line": "~IntBuffer()",
                                "text": "Resource release (delete[]) is guaranteed by the destructor."
                            }
                        ]
                    },
                    {
                        "type": "execution_trace",
                        "title": "Leak-Free by Design",
                        "code": "void process() {\n    IntBuffer buf(1000);\n    if (error()) return;\n    // do work\n}",
                        "trace": [
                            "buf object created on the stack.",
                            "buf constructor allocates memory.",
                            "error() is true, function returns early.",
                            "buf goes out of scope. Destructor is automatically called, freeing memory."
                        ]
                    },
                    {
                        "type": "real_world_analogy",
                        "title": "The Library Book",
                        "content": "RAII is like having an invisible assistant. When you enter a room (scope), the assistant checks out a library book for you (constructor). When you leave the room, the assistant automatically returns the book (destructor), even if you climbed out the window (exception)."
                    },
                    {
                        "type": "mastery_challenge",
                        "title": "RAII and Exceptions",
                        "question": "What happens if the constructor of an RAII object throws an exception during allocation?",
                        "options": [
                            "The destructor is called, which might crash if pointers aren't null.",
                            "The destructor is NOT called. The object was never fully constructed.",
                            "The program aborts immediately."
                        ],
                        "answer": 1,
                        "explanation": "If a constructor throws, the object is considered 'not constructed'. Its destructor will NOT be called. Therefore, you must be careful if allocating multiple resources inside a single constructor."
                    }
                ]
            },
            {
                "title": "Module 3: RAII in the Wild",
                "blocks": [
                    {
                        "type": "header",
                        "title": "Practical RAII",
                        "subtitle": "Mutexes and Files",
                        "metadata": {
                            "difficulty": "Intermediate",
                            "time": "30 min",
                            "concepts": [
                                "std::lock_guard",
                                "std::fstream"
                            ]
                        }
                    },
                    {
                        "type": "story",
                        "title": "Beyond Memory",
                        "content": "RAII isn't just for memory. It's for ANY limited resource. Network sockets, database connections, and especially thread locks."
                    },
                    {
                        "type": "annotated_code",
                        "title": "The Deadlock Danger",
                        "code": "std::mutex m;\nvoid updateData() {\n    m.lock();\n    if (data_is_bad()) {\n        return; // DEADLOCK! Mutex never unlocked.\n    }\n    m.unlock();\n}",
                        "annotations": [
                            {
                                "line": "return;",
                                "text": "If this early return happens, other threads waiting for `m` will block forever."
                            }
                        ]
                    },
                    {
                        "type": "concept",
                        "title": "std::lock_guard",
                        "content": "The standard library provides `std::lock_guard`, an RAII wrapper for mutexes. It locks the mutex in its constructor and unlocks it in its destructor."
                    },
                    {
                        "type": "annotated_code",
                        "title": "The RAII Fix",
                        "code": "std::mutex m;\nvoid updateData() {\n    std::lock_guard<std::mutex> guard(m);\n    if (data_is_bad()) {\n        return; // SAFE. guard destructor unlocks mutex.\n    }\n}",
                        "annotations": [
                            {
                                "line": "std::lock_guard<std::mutex> guard(m);",
                                "text": "Acquires lock."
                            },
                            {
                                "line": "return;",
                                "text": "guard goes out of scope, destructor releases lock."
                            }
                        ]
                    },
                    {
                        "type": "concept",
                        "title": "Files as RAII Objects",
                        "content": "`std::ifstream` and `std::ofstream` are also RAII objects. They open the file in the constructor and close the file handle automatically in the destructor. You rarely need to call `.close()` manually in modern C++."
                    },
                    {
                        "type": "think_first",
                        "question": "Can you copy a `std::lock_guard`?",
                        "options": [
                            "Yes",
                            "No"
                        ],
                        "answer": 1,
                        "explanation": "No. What would it mean to copy a lock? RAII objects representing exclusive resources typically have their copy constructors deleted to prevent double-free or double-unlock errors."
                    },
                    {
                        "type": "code_lab",
                        "title": "Custom File Handle RAII",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass FileHandle {\n    FILE* fp;\npublic:\n    FileHandle(const char* filename) { fp = fopen(filename, \"r\"); }\n    // TODO: Write the destructor to safely close fp if it is not null\n};\n\nint main() {\n    return 0;\n}\n",
                        "expected_output": "",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass FileHandle {\n    FILE* fp;\npublic:\n    FileHandle(const char* filename) { fp = fopen(filename, \"r\"); }\n    // TODO: Write the destructor to safely close fp if it is not null\n};\n\nint main() {\n    return 0;\n}\n",
                        "hint": "Read the comments carefully and fill in the missing C++ logic.",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            }
        ]
    },
    "17": {
        "format": "episodic",
        "episodes": [
            {
                "title": "Module 1: Modern Memory Management",
                "blocks": [
                    {
                        "type": "header",
                        "title": "Smart Pointers",
                        "subtitle": "No more bare 'new' and 'delete'",
                        "metadata": {
                            "difficulty": "Intermediate",
                            "time": "20 min",
                            "concepts": [
                                "Smart Pointers",
                                "<memory>"
                            ]
                        }
                    },
                    {
                        "type": "mermaid_diagram",
                        "title": "Architectural Overview",
                        "explanation": "Before we write code, study this structural model to understand the relationships we are building.",
                        "code": "classDiagram\n    class UniqueOwnership {\n        +std::unique_ptr~T~\n        -Exclusive ownership\n        -Non-copyable, Move-only\n        -Zero memory overhead\n    }\n    class SharedOwnership {\n        +std::shared_ptr~T~\n        -Shared reference-counted ownership\n        -Uses Control Block with strong_count\n        -Frees resource when strong_count reaches 0\n    }\n    class WeakObservation {\n        +std::weak_ptr~T~\n        -Non-owning observer\n        -Breaks circular reference memory leaks\n        -Must call lock() to access resource\n    }\n    class ManagedResource {\n        -Heap Object Memory\n    }\n    UniqueOwnership --> ManagedResource : \"Sole Owner\"\n    SharedOwnership --> ManagedResource : \"Shared Owners\"\n    WeakObservation ..> SharedOwnership : \"Observes Control Block\" "
                    },
                    {
                        "type": "memory_layout",
                        "title": "Pointer Indirection",
                        "explanation": "A pointer is just a variable that stores the memory address of another variable.",
                        "cells": [
                            {
                                "address": "0x2000",
                                "value": "42",
                                "label": "int val"
                            },
                            {
                                "address": "...",
                                "value": "...",
                                "label": "..."
                            },
                            {
                                "address": "0x3000",
                                "value": "0x2000",
                                "label": "int* ptr"
                            }
                        ]
                    },
                    {
                        "type": "story",
                        "title": "The End of an Era",
                        "content": "For decades, C++ developers typed `new` and `delete`, and prayed they matched perfectly. C++11 introduced Smart Pointers, completely eliminating the need for manual memory management in application code."
                    },
                    {
                        "type": "concept",
                        "title": "What is a Smart Pointer?",
                        "content": "A smart pointer is an RAII wrapper around a raw pointer. It overloads the `*` and `->` operators so it feels just like a raw pointer, but its destructor automatically deletes the underlying memory."
                    },
                    {
                        "type": "mental_model",
                        "title": "Smart Pointer Anatomy",
                        "data": "Stack                    Heap\n[SmartPtr Object]  --->  [Raw Data]\n|-- raw_ptr              \n|-- destructor() { delete raw_ptr; }"
                    },
                    {
                        "type": "annotated_code",
                        "title": "Including Smart Pointers",
                        "code": "#include <memory>\n\n// Three main types:\n// 1. std::unique_ptr\n// 2. std::shared_ptr\n// 3. std::weak_ptr",
                        "annotations": [
                            {
                                "line": "#include <memory>",
                                "text": "All smart pointers live in the <memory> header."
                            }
                        ]
                    },
                    {
                        "type": "think_first",
                        "question": "Since a smart pointer is an object on the stack, what happens when you pass it by value to a function?",
                        "options": [
                            "It works exactly like passing a raw pointer.",
                            "It calls a copy constructor, which depends on the type of smart pointer."
                        ],
                        "answer": 1,
                        "explanation": "Because it's a class, passing by value invokes its copy constructor. How it behaves depends on whether it's unique (cannot copy) or shared (increments ref count)."
                    }
                ]
            },
            {
                "title": "Module 2: std::unique_ptr",
                "blocks": [
                    {
                        "type": "header",
                        "title": "Exclusive Ownership",
                        "subtitle": "std::unique_ptr",
                        "metadata": {
                            "difficulty": "Advanced",
                            "time": "30 min",
                            "concepts": [
                                "unique_ptr",
                                "std::make_unique",
                                "Move Semantics"
                            ]
                        }
                    },
                    {
                        "type": "story",
                        "title": "The Highlander Pointer",
                        "content": "There can be only one. `std::unique_ptr` models 'exclusive ownership'. Exactly one `unique_ptr` can point to a given resource. When that pointer goes out of scope, the resource is destroyed."
                    },
                    {
                        "type": "annotated_code",
                        "title": "Creating unique_ptr",
                        "code": "std::unique_ptr<int> p1 = std::make_unique<int>(42);\n// std::unique_ptr<int> p2 = p1; // ERROR: Cannot copy!\nstd::unique_ptr<int> p3 = std::move(p1); // OK: Ownership transferred",
                        "annotations": [
                            {
                                "line": "std::make_unique<int>(42);",
                                "text": "Always use std::make_unique to create unique_ptrs. It's safer and cleaner than using 'new'."
                            },
                            {
                                "line": "// std::unique_ptr<int> p2 = p1;",
                                "text": "Copy constructor is explicitly deleted to enforce exclusivity."
                            },
                            {
                                "line": "std::move(p1);",
                                "text": "Move semantics allow transferring ownership. p1 becomes null."
                            }
                        ]
                    },
                    {
                        "type": "execution_trace",
                        "title": "Ownership Transfer",
                        "code": "void process(std::unique_ptr<Widget> w) { ... }\n\nauto ptr = std::make_unique<Widget>();\nprocess(std::move(ptr));\n// ptr is now nullptr",
                        "trace": [
                            "ptr created, owns Widget A.",
                            "process() is called, ownership moved into w.",
                            "ptr no longer owns Widget A (it is null).",
                            "process() finishes, w goes out of scope, Widget A is destroyed."
                        ]
                    },
                    {
                        "type": "problem",
                        "content": "Why is `std::make_unique` preferred over `std::unique_ptr<T>(new T())`?"
                    },
                    {
                        "type": "concept",
                        "title": "Zero Overhead",
                        "content": "`std::unique_ptr` is a \"zero-overhead abstraction\". It compiles down to the exact same machine code as a raw pointer. There is no performance penalty for using it."
                    },
                    {
                        "type": "code_lab",
                        "title": "Returning unique_ptr",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass Node {};\n\nstd::unique_ptr<Node> createNode() {\n    // TODO: Return a new unique_ptr to a Node using make_unique\n    return nullptr;\n}\n\nint main() {\n    auto node = createNode();\n    return 0;\n}\n",
                        "expected_output": "",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass Node {};\n\nstd::unique_ptr<Node> createNode() {\n    return std::make_unique<Node>();\n}\n\nint main() {\n    auto node = createNode();\n    return 0;\n}\n",
                        "hint": "Read the comments carefully and fill in the missing C++ logic.",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 3: std::shared_ptr",
                "blocks": [
                    {
                        "type": "header",
                        "title": "Shared Ownership",
                        "subtitle": "std::shared_ptr and Reference Counting",
                        "metadata": {
                            "difficulty": "Advanced",
                            "time": "35 min",
                            "concepts": [
                                "shared_ptr",
                                "std::make_shared",
                                "Reference Counting"
                            ]
                        }
                    },
                    {
                        "type": "story",
                        "title": "Sharing is Caring",
                        "content": "Sometimes, data needs to be shared. A node in a graph might have multiple edges pointing to it. You can't use `unique_ptr` because multiple objects need access, and the resource should only be destroyed when the LAST owner is done."
                    },
                    {
                        "type": "concept",
                        "title": "Reference Counting",
                        "content": "`std::shared_ptr` achieves shared ownership via Reference Counting. Alongside the raw pointer, it allocates a small 'control block' that holds an integer counting how many shared_ptrs point to the object."
                    },
                    {
                        "type": "mental_model",
                        "title": "Shared Pointer Architecture",
                        "data": "[shared_ptr 1] --\\    [Control Block] (Ref Count: 2)\n                  --> [Raw Object Data]\n[shared_ptr 2] --/"
                    },
                    {
                        "type": "annotated_code",
                        "title": "Using shared_ptr",
                        "code": "auto p1 = std::make_shared<int>(100); // ref count = 1\n{\n    auto p2 = p1; // ref count = 2\n} // p2 goes out of scope, ref count = 1\n// p1 goes out of scope, ref count = 0 -> data deleted",
                        "annotations": [
                            {
                                "line": "std::make_shared",
                                "text": "Extremely important: make_shared allocates the control block AND the data in a single memory block for performance."
                            },
                            {
                                "line": "auto p2 = p1;",
                                "text": "Copying is allowed! It increments the reference count in the control block."
                            }
                        ]
                    },
                    {
                        "type": "comparison_table",
                        "title": "unique_ptr vs shared_ptr",
                        "headers": [
                            "Feature",
                            "unique_ptr",
                            "shared_ptr"
                        ],
                        "rows": [
                            [
                                "Ownership",
                                "Exclusive (1 owner)",
                                "Shared (N owners)"
                            ],
                            [
                                "Copyable?",
                                "No (Move only)",
                                "Yes"
                            ],
                            [
                                "Overhead",
                                "Zero",
                                "Small (Control block, atomic counters)"
                            ],
                            [
                                "Creation",
                                "std::make_unique",
                                "std::make_shared"
                            ]
                        ]
                    },
                    {
                        "type": "think_first",
                        "question": "Is incrementing the reference count in a `shared_ptr` thread-safe?",
                        "options": [
                            "Yes",
                            "No"
                        ],
                        "answer": 0,
                        "explanation": "Yes, the standard requires the reference count modifications (increments and decrements) to be atomic and thread-safe. However, accessing the underlying object itself concurrently is NOT automatically thread-safe!"
                    }
                ]
            },
            {
                "title": "Module 4: std::weak_ptr",
                "blocks": [
                    {
                        "type": "header",
                        "title": "Breaking Cycles",
                        "subtitle": "std::weak_ptr",
                        "metadata": {
                            "difficulty": "Advanced",
                            "time": "25 min",
                            "concepts": [
                                "weak_ptr",
                                "Circular References"
                            ]
                        }
                    },
                    {
                        "type": "story",
                        "title": "The Immortal Objects",
                        "content": "Reference counting has one fatal flaw: Circular References. If Object A holds a shared_ptr to Object B, and Object B holds a shared_ptr to Object A, their reference counts will never drop to 0. They keep each other alive forever. A memory leak!"
                    },
                    {
                        "type": "annotated_code",
                        "title": "The Cyclic Leak",
                        "code": "struct Node {\n    std::shared_ptr<Node> next;\n};\n\nvoid leak() {\n    auto a = std::make_shared<Node>();\n    auto b = std::make_shared<Node>();\n    a->next = b; // a points to b\n    b->next = a; // b points to a. CYCLE!\n}",
                        "annotations": [
                            {
                                "line": "b->next = a;",
                                "text": "When function exits, 'a' and 'b' local vars are destroyed, but the objects on heap still point to each other. Ref counts stay at 1."
                            }
                        ]
                    },
                    {
                        "type": "concept",
                        "title": "std::weak_ptr to the Rescue",
                        "content": "`std::weak_ptr` acts as an 'observer' to a `shared_ptr`. It can point to the same object, but it does NOT increment the reference count. Therefore, it cannot prevent the object from being destroyed."
                    },
                    {
                        "type": "annotated_code",
                        "title": "Breaking the Cycle",
                        "code": "struct Node {\n    std::weak_ptr<Node> next; // Changed to weak_ptr\n};",
                        "annotations": [
                            {
                                "line": "std::weak_ptr<Node> next;",
                                "text": "Now, 'a' points to 'b' weakly. B's ref count is 1 (from local var). When function exits, B is destroyed."
                            }
                        ]
                    },
                    {
                        "type": "concept",
                        "title": "Accessing weak_ptr data",
                        "content": "Because a `weak_ptr` doesn't guarantee the object is still alive, you cannot directly dereference it. You must 'lock' it to get a temporary `shared_ptr`."
                    },
                    {
                        "type": "code_lab",
                        "title": "Locking a weak_ptr",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nstd::shared_ptr<int> p = std::make_shared<int>(42);\nstd::weak_ptr<int> wp = p;\n\n// TODO: Try to get a shared_ptr from wp using wp.lock()\n// if it succeeds, print the value.\n\nint main() {\n    return 0;\n}\n",
                        "expected_output": "",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nstd::shared_ptr<int> p = std::make_shared<int>(42);\nstd::weak_ptr<int> wp = p;\n\n// TODO: Try to get a shared_ptr from wp using wp.lock()\n// if it succeeds, print the value.\n\nint main() {\n    return 0;\n}\n",
                        "hint": "Read the comments carefully and fill in the missing C++ logic.",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    },
                    {
                        "type": "mastery_challenge",
                        "title": "The Right Tool",
                        "question": "Which smart pointer should you use by default in modern C++?",
                        "options": [
                            "std::shared_ptr (It's safer and handles sharing)",
                            "std::weak_ptr",
                            "std::unique_ptr"
                        ],
                        "answer": 2,
                        "explanation": "Always default to std::unique_ptr! It has zero overhead and clearly expresses exclusive ownership. Only upgrade to std::shared_ptr if you mathematically prove you need shared ownership."
                    }
                ]
            }
        ]
    },
    "18": {
        "format": "episodic",
        "episodes": [
            {
                "title": "Module 1: The Vector Math Nightmare",
                "blocks": [
                    {
                        "type": "story",
                        "title": "The Operator Language",
                        "content": "You're working on a physics engine. The code is littered with calls like `Vector3d result = v1.add(v2.multiply(scalar));`."
                    },
                    {
                        "type": "mermaid_diagram",
                        "title": "Architectural Overview",
                        "explanation": "Before we write code, study this structural model to understand the relationships we are building.",
                        "code": "flowchart TD\n    EXPR[\"User Code Expression:\nVector2D a(3, 4), b(1, 2);\nVector2D c = a + b;\nstd::cout stream output\"]\n    subgraph Resolution[\"Compiler Operator Overload Dispatch\"]\n        OP_PLUS[\"Operator + Resolution\"] --> MEMBER[\"Member Method: a.operator+(b)\nCreates new Vector2D(4, 6)\"]\n        OP_STREAM[\"Stream Insertion Resolution\"] --> FRIEND[\"Friend Function: operator lshift(cout, c)\nStreams formatted output\"]\n    end\n    EXPR --> Resolution\n    MEMBER --> RES1[\"Natural Vector Arithmetic\"]\n    FRIEND --> RES2[\"Chained Stream Insertion\"]"
                    },
                    {
                        "type": "problem",
                        "content": "Mathematical code written with function calls is hard to read. We want to write `v1 + v2 * scalar` just like built-in types."
                    },
                    {
                        "type": "concept",
                        "title": "Operator Overloading",
                        "explanation": "C++ allows you to redefine how standard operators (+, -, *, ==) work with your custom classes.",
                        "analogy": "Teaching the compiler that '+' means 'blend' when applied to two 'Smoothie' objects.",
                        "technical_explanation": "Operators are essentially functions with a special name: `operator+`."
                    },
                    {
                        "type": "mental_model",
                        "title": "Operator Syntax",
                        "data": "v1 + v2  =>  v1.operator+(v2)"
                    },
                    {
                        "type": "annotated_code",
                        "title": "Overloading Addition",
                        "code": "struct Vec2 {\n    float x, y;\n    Vec2 operator+(const Vec2& rhs) const {\n        return {x + rhs.x, y + rhs.y};\n    }\n};",
                        "annotations": [
                            {
                                "line": "3",
                                "text": "Function name is 'operator+'."
                            },
                            {
                                "line": "4",
                                "text": "Returns a brand new object."
                            }
                        ]
                    },
                    {
                        "type": "think_first",
                        "question": "Can you create entirely new operators in C++ (like `**` for exponentiation)?",
                        "options": [
                            "Yes",
                            "No"
                        ],
                        "answer": 1,
                        "explanation": "You can only overload existing operators. You cannot change their precedence or arity (number of operands) either."
                    },
                    {
                        "type": "code_lab",
                        "title": "Overload Subtraction",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nstruct Vec { int x; \n    // TODO: overload operator-\n};\n\nint main() {\n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nstruct Vec { int x; \n    Vec operator-(const Vec& r) const { return {x - r.x}; }\n};\n\nint main() {\n    return 0;\n}\n",
                        "hint": "Similar to addition, return a new Vec.",
                        "expected_output": "",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 2: Friends and Output",
                "blocks": [
                    {
                        "type": "story",
                        "title": "Printing the Universe",
                        "content": "The physics engine works beautifully now, but debugging requires calling `.print()` everywhere."
                    },
                    {
                        "type": "problem",
                        "content": "How do we make `std::cout << v1;` work for our custom Vector class?"
                    },
                    {
                        "type": "concept",
                        "title": "Overloading operator<<",
                        "explanation": "The insertion operator (`<<`) needs to be overloaded as a global function, because the left-hand operand is `std::ostream`, not your class.",
                        "analogy": "You don't teach the Vector how to print to the screen; you teach the screen (ostream) how to understand a Vector.",
                        "technical_explanation": "Since it's a non-member function, it might need `friend` access to read private data."
                    },
                    {
                        "type": "annotated_code",
                        "title": "Stream Insertion",
                        "code": "class Vec {\n    int x, y;\n    friend std::ostream& operator<<(std::ostream& os, const Vec& v);\n};\n\nstd::ostream& operator<<(std::ostream& os, const Vec& v) {\n    os << \"(\" << v.x << \", \" << v.y << \")\";\n    return os;\n}",
                        "annotations": [
                            {
                                "line": "3",
                                "text": "Declaring friendship allows access to private x and y."
                            },
                            {
                                "line": "6",
                                "text": "Global function taking ostream and Vec."
                            },
                            {
                                "line": "8",
                                "text": "Must return the stream to allow chaining (cout << v1 << v2)."
                            }
                        ]
                    },
                    {
                        "type": "execution_trace",
                        "title": "Chaining cout",
                        "code": "cout << a << b;",
                        "trace": [
                            "operator<<(cout, a) executes and returns cout",
                            "cout is passed into operator<<(cout, b)"
                        ]
                    },
                    {
                        "type": "mastery_challenge",
                        "question": "Why does operator<< return a reference to std::ostream?",
                        "options": [
                            "To save memory",
                            "To allow chaining (e.g., cout << a << b)",
                            "It is required by the compiler"
                        ],
                        "answer": 1,
                        "explanation": "Chaining works because `(cout << a)` evaluates to `cout`, which then becomes the left operand for `<< b`."
                    },
                    {
                        "type": "code_lab",
                        "title": "Implement operator<<",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nstruct Point { int x; };\n// TODO: write operator<< for Point\n\nint main() {\n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nstruct Point { int x; };\nstd::ostream& operator<<(std::ostream& os, const Point& p) {\n    return os << p.x;\n}\n\nint main() {\n    return 0;\n}\n",
                        "hint": "Global function returning ostream&.",
                        "expected_output": "",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 3: Global vs Member Operators",
                "blocks": [
                    {
                        "type": "story",
                        "title": "The Commutativity Crisis",
                        "content": "You wrote `Vec * float` as a member function. It works. But `float * Vec` throws a compiler error!"
                    },
                    {
                        "type": "problem",
                        "content": "Member operator overloads require the left-hand operand to be an instance of the class."
                    },
                    {
                        "type": "concept",
                        "title": "Symmetric Operators",
                        "explanation": "Binary operators like `+` and `*` should usually be implemented as global (non-member) functions so they support implicit conversions and commutativity on both sides.",
                        "analogy": "A translation dictionary works both ways: English to Spanish, and Spanish to English.",
                        "technical_explanation": "If `operator+` is a member, `a + 5` works (if 5 converts to A), but `5 + a` fails because 5 is not an object."
                    },
                    {
                        "type": "mental_model",
                        "title": "Global vs Member",
                        "data": "Member: obj.operator+(other)\nGlobal: operator+(obj1, obj2)"
                    },
                    {
                        "type": "annotated_code",
                        "title": "Global Multiplication",
                        "code": "struct Vec { float x; };\nVec operator*(const Vec& v, float scalar) { return {v.x * scalar}; }\nVec operator*(float scalar, const Vec& v) { return {v.x * scalar}; }",
                        "annotations": [
                            {
                                "line": "2",
                                "text": "Handles Vec * float"
                            },
                            {
                                "line": "3",
                                "text": "Handles float * Vec"
                            }
                        ]
                    },
                    {
                        "type": "think_first",
                        "question": "Should `operator+=` be a member or global function?",
                        "options": [
                            "Member",
                            "Global"
                        ],
                        "answer": 0,
                        "explanation": "`+=` modifies the left-hand side, so it makes perfect sense as a member function."
                    },
                    {
                        "type": "code_lab",
                        "title": "Implement Commutative Multiplication",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nstruct V { int val; };\n// TODO: Implement both V * int and int * V\n\nint main() {\n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nstruct V { int val; };\nV operator*(const V& v, int s) { return {v.val * s}; }\nV operator*(int s, const V& v) { return {v.val * s}; }\n\nint main() {\n    return 0;\n}\n",
                        "hint": "Write two global functions.",
                        "expected_output": "",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 4: The Functor",
                "blocks": [
                    {
                        "type": "story",
                        "title": "Objects that Act Like Functions",
                        "content": "The standard library's `std::sort` needs a way to compare objects. You need to pass it 'something' that can be called like a function."
                    },
                    {
                        "type": "problem",
                        "content": "How do we make an object callable?"
                    },
                    {
                        "type": "concept",
                        "title": "Overloading operator()",
                        "explanation": "By overloading the function call operator `()`, an object can be used as if it were a function. These are called 'Functors' or 'Function Objects'.",
                        "analogy": "A Swiss Army Knife object that, when you squeeze it (call it), performs a specific action.",
                        "technical_explanation": "Functors can maintain state, unlike standard function pointers."
                    },
                    {
                        "type": "mental_model",
                        "title": "The Functor",
                        "data": "MyFunctor f;\nf(); // Actually calls f.operator()()"
                    },
                    {
                        "type": "annotated_code",
                        "title": "A Stateful Functor",
                        "code": "class Multiplier {\n    int factor;\npublic:\n    Multiplier(int f) : factor(f) {}\n    int operator()(int x) const { return x * factor; }\n};",
                        "annotations": [
                            {
                                "line": "5",
                                "text": "Overloads the () operator to take an int."
                            }
                        ]
                    },
                    {
                        "type": "mastery_challenge",
                        "question": "Why use a functor instead of a regular function?",
                        "options": [
                            "They are faster",
                            "They can hold internal state (variables)",
                            "They use less memory"
                        ],
                        "answer": 1,
                        "explanation": "Because it's an object, a functor can be initialized with state (like `factor` above) that it uses during the function call."
                    },
                    {
                        "type": "code_lab",
                        "title": "Create a Functor",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass Adder { // TODO };\n\nint main() {\n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass Adder {\n    int addend;\npublic:\n    Adder(int a) : addend(a) {}\n    int operator()(int x) const { return x + addend; }\n};\n\nint main() {\n    return 0;\n}\n",
                        "hint": "Store an int state, overload operator().",
                        "expected_output": "",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            }
        ]
    },
    "19": {
        "format": "episodic",
        "episodes": [
            {
                "title": "Module 1: The Accidental Mutation",
                "blocks": [
                    {
                        "type": "story",
                        "title": "The Const Contract",
                        "content": "A critical system function `printRecord` was supposed to just print data. But somehow, it modified a user's bank balance to zero!"
                    },
                    {
                        "type": "mermaid_diagram",
                        "title": "Architectural Overview",
                        "explanation": "Before we write code, study this structural model to understand the relationships we are building.",
                        "code": "classDiagram\n    class TelemetrySensor {\n        -vector readings\n        -mutable int readCounter\n        -double cachedAverage\n        +getAverage() const double\n        +getReading(int index) const double\n        +addReading(double value) void\n        +reset() void\n    }\n    note for TelemetrySensor \"Const Correctness Contract:\n- Methods marked 'const' guarantee no state mutation.\n- 'mutable' permits internal caching and instrumentation.\n- Safe for concurrent multi-threaded read access.\" "
                    },
                    {
                        "type": "problem",
                        "content": "Passing objects by reference is efficient, but leaves them vulnerable to accidental modification."
                    },
                    {
                        "type": "concept",
                        "title": "Const Correctness and Const References",
                        "explanation": "Passing by `const Type&` ensures the function can read the object efficiently without copying, but the compiler forbids modifying it.",
                        "analogy": "Giving someone a 'Read-Only' view of a Google Doc instead of 'Editor' access.",
                        "technical_explanation": "The compiler checks that no non-const methods or mutating operations are performed on the reference."
                    },
                    {
                        "type": "mental_model",
                        "title": "Const Protection",
                        "data": "void print(const Record& r) { r.balance = 0; } // ERROR"
                    },
                    {
                        "type": "annotated_code",
                        "title": "Passing by Const Reference",
                        "code": "void display(const Account& acc) {\n    std::cout << acc.balance; // OK\n    // acc.balance = 0;       // Compiler Error!\n}",
                        "annotations": [
                            {
                                "line": "1",
                                "text": "const prevents modifications."
                            },
                            {
                                "line": "3",
                                "text": "Protects against accidental bugs."
                            }
                        ]
                    },
                    {
                        "type": "think_first",
                        "question": "Why use `const Type&` instead of just passing by value `Type`?",
                        "options": [
                            "It looks cooler",
                            "It avoids copying the object, which improves performance",
                            "It allows modification"
                        ],
                        "answer": 1,
                        "explanation": "References avoid the overhead of the copy constructor, and const prevents mutation."
                    },
                    {
                        "type": "code_lab",
                        "title": "Protect the Parameter",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nstruct Account {\n    double balance = 100.0;\n};\n\nvoid audit(Account& a) { (void)a; } // TODO: Make parameter const Account&\n\nint main() {\n    const Account acc;\n    (void)acc;\n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nstruct Account {\n    double balance = 100.0;\n};\n\nvoid audit(const Account& a) { (void)a.balance; }\n\nint main() {\n    const Account acc;\n    audit(acc);\n    return 0;\n}\n",
                        "hint": "Add const.",
                        "expected_output": "",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 2: Const Member Functions",
                "blocks": [
                    {
                        "type": "story",
                        "title": "The Refusal to Print",
                        "content": "You fixed the signature: `void printRecord(const Account& acc)`. But now the compiler errors on `acc.getBalance()`!"
                    },
                    {
                        "type": "problem",
                        "content": "If you have a const object, you can only call methods that guarantee they won't modify the object."
                    },
                    {
                        "type": "concept",
                        "title": "Const Methods",
                        "explanation": "You must explicitly mark member functions as `const` to promise the compiler they don't change member variables.",
                        "analogy": "A 'Window Shopper' badge that tells security you are only looking, not touching.",
                        "technical_explanation": "Append `const` after the function parameter list: `double getBalance() const;`"
                    },
                    {
                        "type": "mental_model",
                        "title": "The Const Promise",
                        "data": "[Const Object] ---> Can only call ---> [Const Methods]"
                    },
                    {
                        "type": "annotated_code",
                        "title": "Marking Methods Const",
                        "code": "class Account {\n    double balance;\npublic:\n    double getBalance() const { return balance; }\n    void setBalance(double b) { balance = b; }\n};",
                        "annotations": [
                            {
                                "line": "4",
                                "text": "The 'const' at the end makes this a const method."
                            },
                            {
                                "line": "5",
                                "text": "Non-const method cannot be called on a const Account."
                            }
                        ]
                    },
                    {
                        "type": "execution_trace",
                        "title": "Calling Methods",
                        "code": "const Account a;\na.getBalance(); // OK\n// a.setBalance(10); // ERROR",
                        "trace": [
                            "a is const",
                            "getBalance is const: Allowed",
                            "setBalance is non-const: Blocked"
                        ]
                    },
                    {
                        "type": "mastery_challenge",
                        "question": "What does a const member function actually do to `this` under the hood?",
                        "options": [
                            "It makes it a void pointer",
                            "It changes `this` from `Account*` to `const Account*`",
                            "Nothing"
                        ],
                        "answer": 1,
                        "explanation": "In a const method, the hidden `this` pointer points to a const object, which is why you can't modify member variables through it."
                    },
                    {
                        "type": "code_lab",
                        "title": "Fix the Getter",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass X { int v; public: int get() { return v; } }; // TODO: Make get callable on const objects\n\nint main() {\n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass X { int v; public: int get() const { return v; } };\n\nint main() {\n    return 0;\n}\n",
                        "hint": "Add the const keyword to the function signature.",
                        "expected_output": "",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 3: Mutable and Caching",
                "blocks": [
                    {
                        "type": "story",
                        "title": "The Expensive Calculation",
                        "content": "You have a `const Matrix` object. Calling `determinant()` is slow, so you want to cache the result inside the object. But the object is const!"
                    },
                    {
                        "type": "problem",
                        "content": "How do we modify a 'cache' variable inside a const member function without breaking const correctness conceptually?"
                    },
                    {
                        "type": "concept",
                        "title": "The Mutable Keyword",
                        "explanation": "The `mutable` keyword allows a specific member variable to be modified even from within a `const` member function.",
                        "analogy": "A notebook that is permanently sealed (const), but has a small whiteboard attached (mutable) for temporary scratchpad math.",
                        "technical_explanation": "Useful for logical constness (the object's abstract state hasn't changed) vs bitwise constness (the bits in memory changed)."
                    },
                    {
                        "type": "mental_model",
                        "title": "Logical vs Bitwise Const",
                        "data": "Const Object -> [Const Data] + [Mutable Cache]"
                    },
                    {
                        "type": "annotated_code",
                        "title": "Using Mutable",
                        "code": "class Matrix {\n    mutable double cachedDet = -1;\npublic:\n    double det() const {\n        if (cachedDet == -1) cachedDet = compute(); // Modifies mutable member\n        return cachedDet;\n    }\n};",
                        "annotations": [
                            {
                                "line": "2",
                                "text": "mutable keyword allows modification in const methods."
                            },
                            {
                                "line": "5",
                                "text": "We can assign to cachedDet even though det() is const."
                            }
                        ]
                    },
                    {
                        "type": "think_first",
                        "question": "Is it good practice to make ALL variables mutable to avoid writing const correctly?",
                        "options": [
                            "Yes, it saves time",
                            "No, it completely defeats the safety of const"
                        ],
                        "answer": 1,
                        "explanation": "Mutable should be used rarely, primarily for caching, memoization, or thread synchronization primitives (like mutexes)."
                    },
                    {
                        "type": "code_lab",
                        "title": "Implement a Cache",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass Calc { int c; public: void updateCache() const { c = 5; } }; // TODO: Fix compiler error\n\nint main() {\n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass Calc { mutable int c; public: void updateCache() const { c = 5; } };\n\nint main() {\n    return 0;\n}\n",
                        "hint": "Use the mutable keyword.",
                        "expected_output": "",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 4: Const Pointers",
                "blocks": [
                    {
                        "type": "story",
                        "title": "Reading C-APIs",
                        "content": "You are interfacing with a legacy C library. The documentation specifies `const char * const str`. You are confused."
                    },
                    {
                        "type": "problem",
                        "content": "Const can apply to the pointer itself, the data it points to, or both. The syntax can be tricky."
                    },
                    {
                        "type": "concept",
                        "title": "Pointer Constness",
                        "explanation": "Read declarations right-to-left. A pointer can point to const data, or the pointer itself can be const (cannot point anywhere else).",
                        "analogy": "Const Data: You can't edit the book, but you can change which book you're holding. Const Pointer: You're glued to one book, but you can scribble in it.",
                        "technical_explanation": "`const int* p` (pointer to const int). `int* const p` (const pointer to int)."
                    },
                    {
                        "type": "mental_model",
                        "title": "Right-to-Left Rule",
                        "data": "int const * p;  // p is a pointer to a const int\nint * const p;  // p is a const pointer to an int"
                    },
                    {
                        "type": "annotated_code",
                        "title": "Const Combinations",
                        "code": "const int* p1;       // Data is const, pointer is not\nint* const p2 = &x;  // Pointer is const, data is not\nconst int* const p3 = &y; // Both are const",
                        "annotations": [
                            {
                                "line": "1",
                                "text": "*p1 = 5; Error. p1 = &other; OK."
                            },
                            {
                                "line": "2",
                                "text": "Must be initialized. p2 = &other; Error. *p2 = 5; OK."
                            }
                        ]
                    },
                    {
                        "type": "mastery_challenge",
                        "question": "What does `const char * const` mean?",
                        "options": [
                            "Pointer to char",
                            "Const pointer to const char",
                            "Char pointer to const"
                        ],
                        "answer": 1,
                        "explanation": "Reading right to left: It is a const pointer to a char that is const."
                    },
                    {
                        "type": "code_lab",
                        "title": "Declare a Const Pointer",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nint x = 5;\n// TODO: declare a const pointer 'p' pointing to x (data is mutable)\n\nint main() {\n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nint x = 5;\nint* const p = &x;\n\nint main() {\n    return 0;\n}\n",
                        "hint": "Use int* const.",
                        "expected_output": "",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            }
        ]
    },
    "20": {
        "format": "episodic",
        "episodes": [
            {
                "title": "Module 1: The Shared Resource",
                "blocks": [
                    {
                        "type": "story",
                        "title": "The Factory That Couldn't Keep Up",
                        "content": "At RobotCorp, you need to track how many total robots have been manufactured across all factories."
                    },
                    {
                        "type": "mermaid_diagram",
                        "title": "Architectural Overview",
                        "explanation": "Before we write code, study this structural model to understand the relationships we are building.",
                        "code": "flowchart TD\n    GENERIC[\"Generic Template Blueprint:\ntemplate typename T\nclass SmartBuffer { ... }\"]\n    subgraph InstantiationPhase[\"Compiler Monomorphization (Compile-Time)\"]\n        INT_T[\"SmartBuffer of int\"] --> INT_CODE[\"Generates Dedicated int Assembly Code\"]\n        DBL_T[\"SmartBuffer of double\"] --> DBL_CODE[\"Generates Dedicated double Assembly Code\"]\n        STR_T[\"SmartBuffer of string\"] --> STR_CODE[\"Generates Dedicated string Assembly Code\"]\n    end\n    GENERIC --> InstantiationPhase\n    INT_CODE --> BINARY[\"High Performance Binary:\nNo Type Boxing, No Dynamic Casting, Fully Inlined\"]\n    DBL_CODE --> BINARY\n    STR_CODE --> BINARY"
                    },
                    {
                        "type": "problem",
                        "content": "If each Robot object has an `int count;`, every robot tracks its own count independently. We need a single count shared across all instances."
                    },
                    {
                        "type": "concept",
                        "title": "Static Member Variables",
                        "explanation": "A static member variable belongs to the class itself, not to any specific object instance. All objects share the same variable.",
                        "analogy": "A communal whiteboard in the office (static) vs everyone having their own personal notebook (non-static).",
                        "technical_explanation": "Must be declared inside the class and defined (allocated memory) outside the class."
                    },
                    {
                        "type": "mental_model",
                        "title": "Memory Layout",
                        "data": "Object 1 [ id: 1 ] \\\nObject 2 [ id: 2 ] - Shared [ static count: 3 ]\nObject 3 [ id: 3 ] /"
                    },
                    {
                        "type": "annotated_code",
                        "title": "Defining Static Members",
                        "code": "class Robot {\npublic:\n    static int totalCount;\n    Robot() { totalCount++; }\n};\nint Robot::totalCount = 0; // Definition",
                        "annotations": [
                            {
                                "line": "3",
                                "text": "Declaration inside the class."
                            },
                            {
                                "line": "6",
                                "text": "Required definition outside the class (usually in a .cpp file)."
                            }
                        ]
                    },
                    {
                        "type": "think_first",
                        "question": "Can you access a static variable without creating an object of the class?",
                        "options": [
                            "Yes",
                            "No"
                        ],
                        "answer": 0,
                        "explanation": "Yes, using the scope resolution operator: `Robot::totalCount`."
                    },
                    {
                        "type": "code_lab",
                        "title": "Count the Instances",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass A { public: static int c; A() { /* TODO increment */ } };\n// TODO: define c\n\nint main() {\n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass A { public: static int c; A() { c++; } };\nint A::c = 0;\n\nint main() {\n    return 0;\n}\n",
                        "hint": "Increment c in constructor, define it outside.",
                        "expected_output": "",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 2: Static Member Functions",
                "blocks": [
                    {
                        "type": "story",
                        "title": "The Access Violation",
                        "content": "You made `totalCount` private to encapsulate it. But now you can't read it without creating a dummy Robot object!"
                    },
                    {
                        "type": "problem",
                        "content": "How do we write a getter for a static variable that can be called without an instance?"
                    },
                    {
                        "type": "concept",
                        "title": "Static Member Functions",
                        "explanation": "Functions marked `static` can be called directly on the class. They do not have a `this` pointer and can only access other static members.",
                        "analogy": "Calling the company hotline (static method) vs calling a specific employee's direct line (member method).",
                        "technical_explanation": "Call it using `ClassName::methodName()`."
                    },
                    {
                        "type": "annotated_code",
                        "title": "Static Getters",
                        "code": "class Robot {\n    static int count;\npublic:\n    static int getCount() { return count; }\n};\nint Robot::count = 0;",
                        "annotations": [
                            {
                                "line": "4",
                                "text": "Static function. No 'this' pointer exists here."
                            }
                        ]
                    },
                    {
                        "type": "execution_trace",
                        "title": "Calling Static Methods",
                        "code": "int c = Robot::getCount();",
                        "trace": [
                            "Directly invoke class method",
                            "Return static count"
                        ]
                    },
                    {
                        "type": "mastery_challenge",
                        "question": "Can a static member function call a non-static member function?",
                        "options": [
                            "Yes",
                            "No",
                            "Only if it creates an object first"
                        ],
                        "answer": 2,
                        "explanation": "Because static functions lack a `this` pointer, they don't know WHICH object to call the non-static method on, unless you explicitly pass one in."
                    },
                    {
                        "type": "code_lab",
                        "title": "Implement a Static Method",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass Math { // TODO: add static add(a, b) };\n\nint main() {\n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass Math {\npublic:\n    static int add(int a, int b) { return a + b; }\n};\n\nint main() {\n    return 0;\n}\n",
                        "hint": "Use static keyword before the return type.",
                        "expected_output": "",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 3: Introduction to the Factory Pattern",
                "blocks": [
                    {
                        "type": "story",
                        "title": "The Complicated Construction",
                        "content": "Constructing a `Robot` now requires database connections, loading config files, and calibration. `Robot r;` is too simple and throws errors."
                    },
                    {
                        "type": "problem",
                        "content": "Constructors shouldn't do heavy lifting or fail (they can't return errors easily). We need a better way to create complex objects."
                    },
                    {
                        "type": "concept",
                        "title": "The Factory Method",
                        "explanation": "A Factory is a static method that handles the complex logic of creating an object and returns it (often wrapped in a smart pointer).",
                        "analogy": "Instead of building a car in your driveway (constructor), you ask a Car Factory to build one and deliver it to you.",
                        "technical_explanation": "Make the constructor private so users MUST use the static factory method."
                    },
                    {
                        "type": "mental_model",
                        "title": "Factory Pattern",
                        "data": "Client -> Robot::create() -> [ Private Constructor ] -> Returns unique_ptr<Robot>"
                    },
                    {
                        "type": "annotated_code",
                        "title": "A Simple Factory",
                        "code": "class Robot {\n    Robot() {} // Private!\npublic:\n    static std::unique_ptr<Robot> create() {\n        // Setup logic here...\n        return std::unique_ptr<Robot>(new Robot());\n    }\n};",
                        "annotations": [
                            {
                                "line": "2",
                                "text": "Clients cannot call new Robot() directly."
                            },
                            {
                                "line": "4",
                                "text": "Static factory method."
                            }
                        ]
                    },
                    {
                        "type": "think_first",
                        "question": "Why make the constructor private in a Factory pattern?",
                        "options": [
                            "To enforce use of the Factory method",
                            "To save memory"
                        ],
                        "answer": 0,
                        "explanation": "If it were public, users might bypass the factory and create improperly initialized objects."
                    },
                    {
                        "type": "code_lab",
                        "title": "Build a Factory",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass Box { Box(){} public: // TODO create static factory returning Box* };\n\nint main() {\n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass Box {\n    Box(){}\npublic:\n    static Box* create() { return new Box(); }\n};\n\nint main() {\n    return 0;\n}\n",
                        "hint": "Static method returning new Box().",
                        "expected_output": "",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 4: The Singleton (Bonus)",
                "blocks": [
                    {
                        "type": "story",
                        "title": "There Can Be Only One",
                        "content": "The Factory needs a centralized Configuration Manager, but creating multiple instances causes file locking errors."
                    },
                    {
                        "type": "problem",
                        "content": "How do we guarantee that exactly ONE instance of a class exists globally?"
                    },
                    {
                        "type": "concept",
                        "title": "The Singleton Pattern",
                        "explanation": "A design pattern combining private constructors and static methods/variables to ensure only one instance is ever created.",
                        "analogy": "The President of a country. There can only be one at a time, and there's a specific global office to reach them.",
                        "technical_explanation": "Use a static local variable inside a static getter (Meyers' Singleton) for thread-safety."
                    },
                    {
                        "type": "mental_model",
                        "title": "Meyers' Singleton",
                        "data": "Config::get() ---> [ Static Instance initialized once ] ---> Returns ref"
                    },
                    {
                        "type": "annotated_code",
                        "title": "Thread-Safe Singleton",
                        "code": "class Config {\n    Config() {} // Private\npublic:\n    static Config& getInstance() {\n        static Config instance;\n        return instance;\n    }\n};",
                        "annotations": [
                            {
                                "line": "5",
                                "text": "Instantiated only once on first call. Thread-safe in C++11."
                            }
                        ]
                    },
                    {
                        "type": "mastery_challenge",
                        "question": "What is a major criticism of the Singleton pattern?",
                        "options": [
                            "It is too slow",
                            "It is essentially global state in disguise",
                            "It uses too much memory"
                        ],
                        "answer": 1,
                        "explanation": "Singletons hide dependencies and make unit testing difficult because they act like glorified global variables."
                    },
                    {
                        "type": "code_lab",
                        "title": "Write a Singleton",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass DB { // TODO: Make a Meyers singleton };\n\nint main() {\n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass DB {\n    DB() {}\npublic:\n    static DB& get() {\n        static DB instance;\n        return instance;\n    }\n};\n\nint main() {\n    return 0;\n}\n",
                        "hint": "Private constructor, static get() returning reference to static local variable.",
                        "expected_output": "",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            }
        ]
    },
    "21": {
        "format": "episodic",
        "episodes": [
            {
                "title": "Module 1: Dynamic Arrays (Vector & Deque)",
                "blocks": [
                    {
                        "type": "header",
                        "title": "Dynamic Arrays",
                        "subtitle": "Vectors and Double-Ended Queues",
                        "metadata": {
                            "difficulty": "Intermediate",
                            "time": "25 mins",
                            "concepts": [
                                "std::vector",
                                "std::deque",
                                "Memory Contiguity"
                            ]
                        }
                    },
                    {
                        "type": "mermaid_diagram",
                        "title": "Architectural Overview",
                        "explanation": "Before we write code, study this structural model to understand the relationships we are building.",
                        "code": "flowchart TD\n    subgraph Containers[\"STL Storage Containers\"]\n        VEC[\"std::vector (Contiguous Array)\"]\n        LST[\"std::list (Doubly Linked)\"]\n        MAP[\"std::map (Balanced BST)\"]\n    end\n    subgraph Iterators[\"The Universal Bridge: Iterators\"]\n        IT[\"Iterators: begin() and end()\nProvides uniform pointer-style traversal\"]\n    end\n    subgraph Algorithms[\"Generic STL Algorithms\"]\n        SORT[\"std::sort / std::find_if\"]\n        LAMBDA[\"Modern Lambdas: [](const auto item){ return item.isValid(); }\"]\n    end\n    Containers --> IT\n    Algorithms --> IT\n    LAMBDA --> Algorithms"
                    },
                    {
                        "type": "story",
                        "title": "The Infinite Inventory",
                        "content": "Your game needs an inventory system that can grow dynamically as the player collects items. Using raw C-style arrays is tedious and error-prone when you need to resize. Enter `std::vector`!"
                    },
                    {
                        "type": "problem",
                        "content": "How do we store an arbitrarily large collection of items in contiguous memory while ensuring rapid access and dynamic resizing?"
                    },
                    {
                        "type": "concept",
                        "title": "std::vector",
                        "content": "`std::vector` is a dynamic array. It guarantees contiguous memory, meaning elements are stored next to each other, making CPU cache access incredibly fast. When a vector runs out of capacity, it allocates a new larger block of memory, copies the old elements over, and destroys the old block."
                    },
                    {
                        "type": "mental_model",
                        "title": "Vector Capacity vs Size",
                        "data": "Size: 3, Capacity: 4\n[ A | B | C | _ ] (contiguous block)\n\nPush 'D' -> Size: 4, Capacity: 4\n[ A | B | C | D ]\n\nPush 'E' -> Reallocation! Size: 5, Capacity: 8\n[ A | B | C | D | E | _ | _ | _ ]"
                    },
                    {
                        "type": "annotated_code",
                        "title": "Using std::vector",
                        "code": "#include <vector>\n#include <iostream>\n\nint main() {\n    std::vector<int> numbers;\n    numbers.reserve(10); // Optimization: Pre-allocate space\n    numbers.push_back(1);\n    numbers.push_back(2);\n    \n    std::cout << \"Size: \" << numbers.size() << \"\\n\";\n    std::cout << \"Capacity: \" << numbers.capacity() << \"\\n\";\n    return 0;\n}",
                        "annotations": [
                            {
                                "line": "numbers.reserve(10);",
                                "text": "Prevents unnecessary reallocations if we know roughly how many elements we need."
                            },
                            {
                                "line": "numbers.push_back(1);",
                                "text": "Appends an element to the end. Fast O(1) amortized time."
                            }
                        ]
                    },
                    {
                        "type": "common_mistakes",
                        "title": "Iterator Invalidation",
                        "mistakes": [
                            {
                                "title": "Storing Pointers to Vector Elements",
                                "desc": "When a vector reallocates its internal buffer, all pointers, references, and iterators to its elements become invalid!"
                            }
                        ]
                    },
                    {
                        "type": "think_first",
                        "question": "What happens if you insert an element at the *front* of a `std::vector` (using `insert`)?",
                        "options": [
                            "O(1) operation",
                            "O(N) operation",
                            "O(log N) operation"
                        ],
                        "answer": 1,
                        "explanation": "Because elements are contiguous, inserting at the front requires shifting all existing elements one position to the right, which takes O(N) time."
                    },
                    {
                        "type": "concept",
                        "title": "std::deque (Double-Ended Queue)",
                        "content": "If you frequently need to insert or remove elements at *both* the front and the back, use `std::deque`. It allocates memory in chunks, meaning it doesn't guarantee a single contiguous block, but offers O(1) insertions at both ends."
                    },
                    {
                        "type": "code_lab",
                        "title": "Vector Warmup",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\n// TODO: Write a function that takes a vector of ints and removes all even numbers.\nvoid removeEvens(std::vector<int>& vec) {\n    // your code here\n}\n\nint main() {\n    std::vector<int> v = {1, 2, 3, 4, 5};\n    removeEvens(v);\n    for (int x : v) std::cout << x << \" \";\n    return 0;\n}\n",
                        "expected_output": "1 3 5 ",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nvoid removeEvens(std::vector<int>& vec) {\n    vec.erase(\n        std::remove_if(vec.begin(), vec.end(), [](int x) { return x % 2 == 0; }),\n        vec.end()\n    );\n}\n\nint main() {\n    std::vector<int> v = {1, 2, 3, 4, 5};\n    removeEvens(v);\n    for (int x : v) std::cout << x << \" \";\n    return 0;\n}\n",
                        "hint": "Read the comments carefully and fill in the missing C++ logic.",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 2: Linked Lists",
                "blocks": [
                    {
                        "type": "header",
                        "title": "Linked Data Structures",
                        "subtitle": "std::list and std::forward_list",
                        "metadata": {
                            "difficulty": "Intermediate",
                            "time": "20 mins",
                            "concepts": [
                                "std::list",
                                "std::forward_list",
                                "Node-based structures"
                            ]
                        }
                    },
                    {
                        "type": "story",
                        "title": "The Quest Log",
                        "content": "Players accept and complete quests rapidly. Quests are often inserted into the middle of the quest log or removed from arbitrary positions. A contiguous array requires heavy shifting for this. Let's use a linked list!"
                    },
                    {
                        "type": "concept",
                        "title": "std::list vs std::forward_list",
                        "content": "`std::list` is a doubly-linked list. Each node has a pointer to the previous and next node. It allows O(1) insertions/deletions anywhere *if* you already have an iterator to that position. `std::forward_list` is a singly-linked list (smaller memory footprint) that only traverses forward."
                    },
                    {
                        "type": "comparison_table",
                        "title": "Vector vs List",
                        "headers": [
                            "Feature",
                            "std::vector",
                            "std::list"
                        ],
                        "rows": [
                            [
                                "Memory",
                                "Contiguous",
                                "Scattered Nodes"
                            ],
                            [
                                "Random Access (vec[5])",
                                "O(1) - Fast!",
                                "O(N) - Slow!"
                            ],
                            [
                                "Insertion at End",
                                "O(1) amortized",
                                "O(1)"
                            ],
                            [
                                "Insertion in Middle",
                                "O(N) (shifting)",
                                "O(1) (pointer swap)"
                            ],
                            [
                                "Cache Friendliness",
                                "Excellent",
                                "Poor"
                            ]
                        ]
                    },
                    {
                        "type": "annotated_code",
                        "title": "List Splicing",
                        "code": "#include <list>\n#include <iostream>\n\nint main() {\n    std::list<int> L1 = {1, 2, 3};\n    std::list<int> L2 = {10, 20};\n    \n    auto it = L1.begin();\n    std::advance(it, 1); // Point to '2'\n    \n    // Splice L2 into L1 before '2'\n    L1.splice(it, L2);\n    \n    // L1 is now: 1, 10, 20, 2, 3\n    return 0;\n}",
                        "annotations": [
                            {
                                "line": "std::advance(it, 1);",
                                "text": "Since lists don't support random access like it+1, we use std::advance."
                            },
                            {
                                "line": "L1.splice(it, L2);",
                                "text": "Moves nodes from L2 into L1 without copying data! L2 becomes empty."
                            }
                        ]
                    },
                    {
                        "type": "mastery_challenge",
                        "title": "Cache Performance",
                        "question": "For a collection of 1000 integers where you just need to iterate through them from start to finish, which container is faster in practice?",
                        "options": [
                            "std::list (no reallocation overhead)",
                            "std::vector (cache friendly)",
                            "They are identical"
                        ],
                        "answer": 1,
                        "explanation": "std::vector is massively faster for linear iteration because modern CPUs load contiguous memory into the fast CPU cache. std::list's scattered nodes cause frequent cache misses."
                    }
                ]
            },
            {
                "title": "Module 3: Associative Containers (Sets & Maps)",
                "blocks": [
                    {
                        "type": "header",
                        "title": "Sets & Maps",
                        "subtitle": "Finding Data Fast",
                        "metadata": {
                            "difficulty": "Intermediate",
                            "time": "30 mins",
                            "concepts": [
                                "std::map",
                                "std::set",
                                "std::unordered_map",
                                "Hash Tables"
                            ]
                        }
                    },
                    {
                        "type": "story",
                        "title": "The Dictionary of Spells",
                        "content": "You need to look up a spell's mana cost based on its name (a string). A vector would require scanning O(N) items. We need an associative container!"
                    },
                    {
                        "type": "concept",
                        "title": "Trees vs Hash Tables",
                        "content": "C++ offers two flavors of associative containers:\n\n1. **Ordered** (`std::map`, `std::set`): Implemented as Red-Black Trees. They keep elements sorted by key. Lookups are O(log N).\n2. **Unordered** (`std::unordered_map`, `std::unordered_set`): Implemented as Hash Tables. They don't sort elements, but lookups are O(1) on average."
                    },
                    {
                        "type": "annotated_code",
                        "title": "Map vs Unordered Map",
                        "code": "#include <map>\n#include <unordered_map>\n#include <string>\n\nint main() {\n    std::map<std::string, int> sorted_spells;\n    sorted_spells[\"Fireball\"] = 50;\n    sorted_spells[\"Heal\"] = 30;\n    // Iterating will print them alphabetically: Fireball, Heal\n\n    std::unordered_map<std::string, int> fast_spells;\n    fast_spells[\"Fireball\"] = 50;\n    // Lookups are O(1), but iteration order is unpredictable.\n    return 0;\n}",
                        "annotations": [
                            {
                                "line": "sorted_spells[\"Fireball\"] = 50;",
                                "text": "If \"Fireball\" doesn't exist, this creates it and default-initializes the value, then assigns 50."
                            }
                        ]
                    },
                    {
                        "type": "common_mistakes",
                        "title": "Accidental Insertion",
                        "mistakes": [
                            {
                                "title": "Using operator[] for lookups",
                                "desc": "If you do `if (map[\"Ice\"])`, and \"Ice\" is not in the map, the map *creates* a new entry for \"Ice\" with a default value of 0! Use `map.find(\"Ice\") != map.end()` to just check existence without modifying."
                            }
                        ]
                    },
                    {
                        "type": "think_first",
                        "question": "Which container would you use to maintain a high-score leaderboard that must always be printed from highest to lowest score?",
                        "options": [
                            "std::unordered_map",
                            "std::set (with a custom descending comparator)",
                            "std::vector (unsorted)"
                        ],
                        "answer": 1,
                        "explanation": "std::set automatically keeps elements sorted. By providing a `std::greater` comparator, it will keep scores in descending order automatically as they are inserted."
                    },
                    {
                        "type": "code_lab",
                        "title": "Word Frequency",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nint main() {\n    std::vector<std::string> words = {\"apple\", \"banana\", \"apple\", \"orange\", \"banana\", \"apple\"};\n    // TODO: Create a std::map<std::string, int> to count the frequency of each word.\n    \n    // TODO: Print each word: count pair\n    return 0;\n}\n",
                        "expected_output": "apple: 3\nbanana: 2\norange: 1\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nint main() {\n    std::vector<std::string> words = {\"apple\", \"banana\", \"apple\", \"orange\", \"banana\", \"apple\"};\n    std::map<std::string, int> freq;\n    for (const auto& w : words) freq[w]++;\n    for (const auto& [word, count] : freq) {\n        std::cout << word << \": \" << count << \"\\n\";\n    }\n    return 0;\n}\n",
                        "hint": "Read the comments carefully and fill in the missing C++ logic.",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 4: Algorithms & Iterators",
                "blocks": [
                    {
                        "type": "header",
                        "title": "The algorithm header",
                        "subtitle": "Don't Reinvent the Wheel",
                        "metadata": {
                            "difficulty": "Intermediate",
                            "time": "25 mins",
                            "concepts": [
                                "<algorithm>",
                                "Iterators",
                                "Lambdas"
                            ]
                        }
                    },
                    {
                        "type": "story",
                        "title": "The Power of Abstraction",
                        "content": "The true power of the STL is that containers and algorithms are decoupled. Algorithms don't know about `vector` or `list`; they only know about *Iterators*. This means one `std::sort` function can sort almost anything!"
                    },
                    {
                        "type": "concept",
                        "title": "Iterators",
                        "content": "Iterators are objects that point to elements in a container. They act like pointers. \n`begin()` points to the first element.\n`end()` points to one past the last element (a conceptual boundary)."
                    },
                    {
                        "type": "execution_trace",
                        "title": "Iterator Range [begin, end)",
                        "code": "vector<int> v = {10, 20, 30};\nauto it = v.begin();\nwhile(it != v.end()) {\n    cout << *it;\n    it++;\n}",
                        "trace": [
                            "it points to 10. `it != v.end()` is true. Prints 10.",
                            "it increments, points to 20.",
                            "it increments, points to 30.",
                            "it increments, points to the memory immediately after 30 (which is `v.end()`).",
                            "`it != v.end()` is false. Loop terminates."
                        ]
                    },
                    {
                        "type": "annotated_code",
                        "title": "Using <algorithm> with Lambdas",
                        "code": "#include <vector>\n#include <algorithm>\n#include <iostream>\n\nint main() {\n    std::vector<int> v = {5, 2, 8, 1, 9};\n    \n    // Sort descending using a lambda\n    std::sort(v.begin(), v.end(), [](int a, int b) {\n        return a > b;\n    });\n    \n    // Count elements greater than 4\n    int count = std::count_if(v.begin(), v.end(), [](int x){\n        return x > 4;\n    });\n    \n    return 0;\n}",
                        "annotations": [
                            {
                                "line": "[](int a, int b) { return a > b; }",
                                "text": "A lambda function! It acts as an inline, anonymous comparator function."
                            },
                            {
                                "line": "std::count_if",
                                "text": "An STL algorithm that applies a predicate (condition) to every element."
                            }
                        ]
                    },
                    {
                        "type": "wrong_approach",
                        "title": "Erasing elements in a loop (The Erase-Remove Idiom)",
                        "code": "for(auto it = v.begin(); it != v.end(); ++it) {\n    if(*it == 5) v.erase(it); // DANGER!\n}",
                        "explanation": "Calling `erase` invalidates `it`. When the loop does `++it`, you have undefined behavior. Instead, use the C++20 `std::erase` or the Erase-Remove idiom: `v.erase(std::remove(v.begin(), v.end(), 5), v.end());`"
                    },
                    {
                        "type": "mastery_challenge",
                        "title": "Find the odd one out",
                        "question": "Which algorithm does NOT modify the container it operates on?",
                        "options": [
                            "std::sort",
                            "std::remove",
                            "std::find",
                            "std::transform"
                        ],
                        "answer": 2,
                        "explanation": "`std::find` only searches and returns an iterator. The others modify the elements or their order."
                    }
                ]
            }
        ]
    },
    "22": {
        "format": "episodic",
        "episodes": [
            {
                "title": "Module 1: Single Responsibility Principle (SRP)",
                "blocks": [
                    {
                        "type": "header",
                        "title": "SOLID: Single Responsibility",
                        "subtitle": "The \"S\" in SOLID",
                        "metadata": {
                            "difficulty": "Intermediate",
                            "time": "20 mins",
                            "concepts": [
                                "SRP",
                                "Cohesion",
                                "Decoupling"
                            ]
                        }
                    },
                    {
                        "type": "mermaid_diagram",
                        "title": "Architectural Overview",
                        "explanation": "Before we write code, study this structural model to understand the relationships we are building.",
                        "code": "flowchart TD\n    subgraph SOLIDPrinciples[\"SOLID Principles for Scalable C++ Architecture\"]\n        S[\"S: Single Responsibility\nEach class focuses on one autonomous concern\"]\n        O[\"O: Open/Closed Principle\nOpen for extension via polymorphism, closed for modification\"]\n        L[\"L: Liskov Substitution\nDerived classes honor base class behavioral contracts\"]\n        I[\"I: Interface Segregation\nGranular, focused interfaces over monolithic classes\"]\n        D[\"D: Dependency Inversion\nHigh-level policy depends on abstractions, not low-level details\"]\n    end\n    SOLIDPrinciples --> ARCH[\"Resilient, Decoupled, Production-Grade Architecture\"]"
                    },
                    {
                        "type": "story",
                        "title": "The God Object",
                        "content": "You built an `Entity` class for your game. It handles rendering, physics, networking, and saving to disk. Now, whenever the graphics API changes, the networking team has to recompile everything. This class knows too much!"
                    },
                    {
                        "type": "concept",
                        "title": "Single Responsibility Principle",
                        "content": "\"A class should have one, and only one, reason to change.\" \n\nIf a class handles database logic and UI logic, a change to the UI or a change to the database are *two* reasons for the class to change. Split them up."
                    },
                    {
                        "type": "wrong_approach",
                        "title": "SRP Violation",
                        "code": "class Player {\npublic:\n    void calculateDamage() { /* ... */ }\n    void saveToDatabase() { /* ... */ }\n    void renderToScreen() { /* ... */ }\n};",
                        "explanation": "The Player class handles business logic, persistence, and presentation. It violates SRP."
                    },
                    {
                        "type": "correct_approach",
                        "title": "Applying SRP",
                        "code": "class Player {\npublic:\n    void calculateDamage() { /* ... */ }\n};\n\nclass PlayerRepository {\npublic:\n    void save(const Player& p) { /* ... */ }\n};\n\nclass PlayerRenderer {\npublic:\n    void render(const Player& p) { /* ... */ }\n};",
                        "explanation": "Now each class has exactly one responsibility. A rendering update doesn't touch the Repository."
                    },
                    {
                        "type": "think_first",
                        "question": "Does SRP mean a class can only have one function?",
                        "options": [
                            "Yes, one function = one responsibility",
                            "No, it means all functions in the class should relate to a single cohesive purpose."
                        ],
                        "answer": 1,
                        "explanation": "Responsibility != Function. A `FileParser` class might have `open`, `read`, and `close` functions, but its single responsibility is \"parsing a file\"."
                    }
                ]
            },
            {
                "title": "Module 2: Open/Closed Principle (OCP)",
                "blocks": [
                    {
                        "type": "header",
                        "title": "SOLID: Open/Closed Principle",
                        "subtitle": "The \"O\" in SOLID",
                        "metadata": {
                            "difficulty": "Advanced",
                            "time": "25 mins",
                            "concepts": [
                                "OCP",
                                "Polymorphism",
                                "Extensibility"
                            ]
                        }
                    },
                    {
                        "type": "story",
                        "title": "The Endless Switch Statement",
                        "content": "You have a function `drawShape(Shape s)`. It has a massive `switch` statement checking `if s is circle, draw circle... if s is square...`. Every time a new shape is added, you have to modify this existing function. Bugs ensue."
                    },
                    {
                        "type": "concept",
                        "title": "Open/Closed Principle",
                        "content": "\"Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification.\"\n\nYou should be able to add new functionality without touching existing, tested code. In C++, this is often achieved through Polymorphism (virtual functions) or Templates."
                    },
                    {
                        "type": "wrong_approach",
                        "title": "Violating OCP",
                        "code": "enum ShapeType { CIRCLE, SQUARE };\n\nvoid drawAll(const std::vector<Shape*>& shapes) {\n    for(auto* s : shapes) {\n        if(s->type == CIRCLE) drawCircle(s);\n        else if(s->type == SQUARE) drawSquare(s);\n        // ADDING A TRIANGLE REQUIRES CHANGING THIS CODE!\n    }\n}",
                        "explanation": "Every new shape requires modifying the `drawAll` function."
                    },
                    {
                        "type": "correct_approach",
                        "title": "Embracing OCP",
                        "code": "class Shape {\npublic:\n    virtual void draw() const = 0; // Pure virtual\n    virtual ~Shape() = default;\n};\n\nclass Circle : public Shape {\npublic:\n    void draw() const override { /* draw circle */ }\n};\n\nclass Triangle : public Shape { // NEW SHAPE!\npublic:\n    void draw() const override { /* draw triangle */ }\n};\n\nvoid drawAll(const std::vector<Shape*>& shapes) {\n    for(auto* s : shapes) {\n        s->draw(); // DOES NOT NEED TO CHANGE!\n    }\n}",
                        "explanation": "We added a Triangle by *extending* (adding a new class) rather than *modifying* `drawAll`. `drawAll` is closed to modification!"
                    },
                    {
                        "type": "mastery_challenge",
                        "title": "OCP in Practice",
                        "question": "Besides polymorphism (inheritance), what is another way to achieve OCP in C++?",
                        "options": [
                            "Using raw pointers everywhere",
                            "Using Templates and Concepts (Compile-time polymorphism)",
                            "Putting all code in one giant file"
                        ],
                        "answer": 1,
                        "explanation": "Templates allow you to write generic algorithms that work on any type meeting certain requirements, extending functionality without modifying the generic algorithm."
                    }
                ]
            },
            {
                "title": "Module 3: Liskov Substitution & Interface Segregation",
                "blocks": [
                    {
                        "type": "header",
                        "title": "SOLID: LSP & ISP",
                        "subtitle": "The \"L\" and \"I\" in SOLID",
                        "metadata": {
                            "difficulty": "Advanced",
                            "time": "30 mins",
                            "concepts": [
                                "LSP",
                                "ISP",
                                "Behavioral Subtyping"
                            ]
                        }
                    },
                    {
                        "type": "story",
                        "title": "The Penguin That Couldn't Fly",
                        "content": "You made a `Bird` class with a `fly()` method. `Eagle` inherits from `Bird`. Then you add `Penguin`. Penguins are birds, so `Penguin` inherits from `Bird`. But penguins can't fly! So you make `Penguin::fly()` throw an exception. Congratulations, you just crashed the game when the AI tried to make a flock of birds take off!"
                    },
                    {
                        "type": "concept",
                        "title": "Liskov Substitution Principle (LSP)",
                        "content": "\"Objects of a superclass shall be replaceable with objects of its subclasses without breaking the application.\"\n\nIf code expects a `Bird` and calls `fly()`, substituting a `Penguin` breaks the expectation. Inheritance in programming is about *Behavioral Subtyping* (IS-SUBSTITUTABLE-FOR), not just real-world \"IS-A\" relationships."
                    },
                    {
                        "type": "real_world_analogy",
                        "title": "Interface Segregation Principle (ISP)",
                        "content": "ISP states: \"No client should be forced to depend on methods it does not use.\"\nImagine a multi-tool. If you just need a screwdriver, it's annoying to hold a massive chunk of metal with a saw, knife, and pliers attached. Code is the same. Don't make massive \"Fat Interfaces\"."
                    },
                    {
                        "type": "wrong_approach",
                        "title": "ISP Violation: Fat Interface",
                        "code": "class IMachine {\npublic:\n    virtual void print() = 0;\n    virtual void scan() = 0;\n    virtual void fax() = 0;\n};\n\nclass SimplePrinter : public IMachine {\npublic:\n    void print() override { /* ... */ }\n    void scan() override { throw std::logic_error(\"Can't scan\"); }\n    void fax() override { throw std::logic_error(\"Can't fax\"); }\n};",
                        "explanation": "SimplePrinter is forced to implement methods it doesn't support. This also violates LSP because it throws unexpected exceptions!"
                    },
                    {
                        "type": "correct_approach",
                        "title": "ISP Applied",
                        "code": "class IPrinter { virtual void print() = 0; };\nclass IScanner { virtual void scan() = 0; };\nclass IFax { virtual void fax() = 0; };\n\nclass SimplePrinter : public IPrinter {\n    void print() override { /* ... */ }\n};\n\nclass MultiFunctionPrinter : public IPrinter, public IScanner, public IFax {\n    // Implements all three\n};",
                        "explanation": "Clients only depend on the specific interfaces they need."
                    }
                ]
            },
            {
                "title": "Module 4: Dependency Inversion Principle (DIP)",
                "blocks": [
                    {
                        "type": "header",
                        "title": "SOLID: Dependency Inversion",
                        "subtitle": "The \"D\" in SOLID",
                        "metadata": {
                            "difficulty": "Advanced",
                            "time": "25 mins",
                            "concepts": [
                                "DIP",
                                "Dependency Injection",
                                "Abstractions"
                            ]
                        }
                    },
                    {
                        "type": "concept",
                        "title": "Dependency Inversion Principle",
                        "content": "1. High-level modules should not depend on low-level modules. Both should depend on abstractions.\n2. Abstractions should not depend on details. Details should depend on abstractions."
                    },
                    {
                        "type": "story",
                        "title": "The Hardcoded Database",
                        "content": "Your `AuthenticationManager` creates a `MySQLDatabase` directly inside its constructor. When you decide to move to a cloud API, you have to rip out the guts of `AuthenticationManager`. It was tightly coupled to a low-level detail."
                    },
                    {
                        "type": "mental_model",
                        "title": "Inverting the Dependency",
                        "data": "Wrong:\n[App] ---> [MySQLDatabase]\n\nRight:\n[App] ---> [IDatabase] <--- [MySQLDatabase]"
                    },
                    {
                        "type": "wrong_approach",
                        "title": "Tightly Coupled Code",
                        "code": "class MySQLDatabase { public: void query() {} };\n\nclass App {\n    MySQLDatabase db; // Hardcoded dependency\npublic:\n    void start() { db.query(); }\n};",
                        "explanation": "App is forever glued to MySQLDatabase."
                    },
                    {
                        "type": "correct_approach",
                        "title": "Dependency Injection",
                        "code": "class IDatabase {\npublic:\n    virtual void query() = 0;\n    virtual ~IDatabase() = default;\n};\n\nclass MySQLDatabase : public IDatabase {\npublic:\n    void query() override { /* MySQL stuff */ }\n};\n\nclass App {\n    IDatabase& db;\npublic:\n    // DB is INJECTED via constructor\n    App(IDatabase& injectedDb) : db(injectedDb) {}\n    void start() { db.query(); }\n};",
                        "explanation": "App relies on the IDatabase abstraction. You can easily pass in a PostgreSQLDatabase or a MockDatabase for unit testing!"
                    }
                ]
            }
        ]
    },
    "23": {
        "format": "episodic",
        "episodes": [
            {
                "title": "Module 1: The Diamond Problem",
                "blocks": [
                    {
                        "type": "header",
                        "title": "Multiple Inheritance Traps",
                        "subtitle": "The Dreaded Diamond",
                        "metadata": {
                            "difficulty": "Advanced",
                            "time": "25 mins",
                            "concepts": [
                                "Multiple Inheritance",
                                "Virtual Inheritance",
                                "Ambiguity"
                            ]
                        }
                    },
                    {
                        "type": "mermaid_diagram",
                        "title": "Architectural Overview",
                        "explanation": "Before we write code, study this structural model to understand the relationships we are building.",
                        "code": "classDiagram\n    class ElectronicDevice {\n        +int serialNumber\n        +turnOn() void\n    }\n    class AudioTransmitter {\n        +broadcast() void\n    }\n    class AudioReceiver {\n        +listen() void\n    }\n    class SmartTransceiver {\n        +synchronize() void\n    }\n    ElectronicDevice <|-- AudioTransmitter : \"virtual inheritance\"\n    ElectronicDevice <|-- AudioReceiver : \"virtual inheritance\"\n    AudioTransmitter <|-- SmartTransceiver\n    AudioReceiver <|-- SmartTransceiver\n    note for SmartTransceiver \"Diamond Problem Solved:\nVirtual inheritance ensures only ONE copy\nof ElectronicDevice exists in memory.\nBetter yet: Prefer Composition over Deep Inheritance!\" "
                    },
                    {
                        "type": "story",
                        "title": "A Tale of Two Bases",
                        "content": "You have a base class `Entity`. You create `RenderableEntity` and `PhysicalEntity` inheriting from `Entity`. Then you create a `Player` that inherits from BOTH `RenderableEntity` and `PhysicalEntity`. Suddenly, the compiler complains that `Entity` functions are ambiguous. Why? Because `Player` has *two* copies of the `Entity` base class!"
                    },
                    {
                        "type": "mental_model",
                        "title": "The Diamond Memory Layout",
                        "data": "      [Entity]\n       /    \\\n [Render]  [Physics]\n       \\    /\n      [Player]\n\nMemory layout without virtual inheritance:\n[Entity(Render)][Render] [Entity(Physics)][Physics] [Player]"
                    },
                    {
                        "type": "wrong_approach",
                        "title": "Ambiguous Calls",
                        "code": "class Base { public: int health = 100; };\nclass A : public Base {};\nclass B : public Base {};\nclass Derived : public A, public B {};\n\nint main() {\n    Derived d;\n    // d.health = 50; // ERROR: Ambiguous! Is it A's health or B's health?\n}",
                        "explanation": "The compiler doesn't know which 'health' variable you mean because two separate Base sub-objects exist."
                    },
                    {
                        "type": "correct_approach",
                        "title": "Virtual Inheritance",
                        "code": "class Base { public: int health = 100; };\nclass A : virtual public Base {};\nclass B : virtual public Base {};\nclass Derived : public A, public B {};\n\nint main() {\n    Derived d;\n    d.health = 50; // OK! Only one shared Base instance exists.\n}",
                        "explanation": "The `virtual` keyword tells the compiler to ensure only ONE instance of `Base` is shared among all paths in the diamond."
                    },
                    {
                        "type": "common_mistakes",
                        "title": "Performance Costs",
                        "mistakes": [
                            {
                                "title": "Virtual Pointers overhead",
                                "desc": "Virtual inheritance adds hidden pointers to classes (vbase pointers) and indirection costs. It also makes object initialization complex. It should be used sparingly."
                            }
                        ]
                    }
                ]
            },
            {
                "title": "Module 2: The Square-Rectangle Problem (LSP Violation)",
                "blocks": [
                    {
                        "type": "header",
                        "title": "Behavioral Subtyping",
                        "subtitle": "Math vs Programming",
                        "metadata": {
                            "difficulty": "Intermediate",
                            "time": "20 mins",
                            "concepts": [
                                "Liskov Substitution Principle",
                                "Preconditions",
                                "Postconditions"
                            ]
                        }
                    },
                    {
                        "type": "story",
                        "title": "But a Square IS a Rectangle!",
                        "content": "In geometry, a Square is a special type of Rectangle where width equals height. So naturally, you make `Square` inherit from `Rectangle`. But a function that uses a `Rectangle` expects to be able to set the width and height *independently*. A square breaks this expectation."
                    },
                    {
                        "type": "wrong_approach",
                        "title": "The LSP Trap",
                        "code": "class Rectangle {\nprotected:\n    int width, height;\npublic:\n    virtual void setWidth(int w) { width = w; }\n    virtual void setHeight(int h) { height = h; }\n    int getArea() const { return width * height; }\n};\n\nclass Square : public Rectangle {\npublic:\n    // Must override to maintain squareness\n    void setWidth(int w) override { width = height = w; }\n    void setHeight(int h) override { width = height = h; }\n};",
                        "explanation": "Looks fine? Let's trace it."
                    },
                    {
                        "type": "execution_trace",
                        "title": "Breaking Expectations",
                        "code": "void enlarge(Rectangle& rect) {\n    rect.setWidth(10);\n    rect.setHeight(5);\n    assert(rect.getArea() == 50);\n}\n\nSquare sq;\nenlarge(sq); // Fails assertion!",
                        "trace": [
                            "enlarge() receives a Square reference.",
                            "setWidth(10) is called. Square's width and height become 10.",
                            "setHeight(5) is called. Square's width and height become 5.",
                            "getArea() returns 25.",
                            "Assertion fails. The client code (enlarge) expected Rectangle semantics, but got Square semantics."
                        ]
                    },
                    {
                        "type": "think_first",
                        "question": "How should you model Square and Rectangle to avoid LSP violations?",
                        "options": [
                            "Make Rectangle inherit from Square",
                            "Make them unrelated, or both inherit from an abstract `Shape` interface",
                            "Remove the virtual keywords"
                        ],
                        "answer": 1,
                        "explanation": "Behaviorally, they are different. A Shape interface with a pure virtual `getArea()` method ensures polymorphism works safely without violating behavioral expectations."
                    }
                ]
            },
            {
                "title": "Module 3: Fragile Base Class",
                "blocks": [
                    {
                        "type": "header",
                        "title": "The Fragile Base Class",
                        "subtitle": "Tight Coupling via Inheritance",
                        "metadata": {
                            "difficulty": "Advanced",
                            "time": "20 mins",
                            "concepts": [
                                "Tight Coupling",
                                "Encapsulation Leaks"
                            ]
                        }
                    },
                    {
                        "type": "concept",
                        "title": "Inheritance Breaks Encapsulation",
                        "content": "When a derived class depends heavily on the internal implementation details of its base class, any change to the base class can silently break the derived class. This is called the Fragile Base Class problem."
                    },
                    {
                        "type": "wrong_approach",
                        "title": "Self-use in Base Classes",
                        "code": "class MyList {\nprotected:\n    int size = 0;\npublic:\n    virtual void add(int x) {\n        // internal logic\n        size++;\n    }\n    virtual void addAll(const vector<int>& v) {\n        for(int x : v) add(x); // Self-use!\n    }\n};\n\nclass CountingList : public MyList {\n    int count = 0;\npublic:\n    void add(int x) override { count++; MyList::add(x); }\n    void addAll(const vector<int>& v) override { \n        count += v.size(); \n        MyList::addAll(v); \n    }\n};",
                        "explanation": "If we call `addAll` with 3 items, `CountingList` adds 3 to `count`. Then it calls `MyList::addAll`, which calls the overridden `add` 3 times, adding *another* 3 to `count`. The result is double-counting! The derived class made a false assumption about how the base class implemented `addAll`."
                    },
                    {
                        "type": "real_world_analogy",
                        "title": "Modifying Foundations",
                        "content": "Inheritance is like building a house directly onto a specific foundation. If you need to fix a crack in the foundation (Base class), you risk tearing down the whole house (Derived classes). Composition is like a modular home."
                    }
                ]
            },
            {
                "title": "Module 4: Composition Over Inheritance",
                "blocks": [
                    {
                        "type": "header",
                        "title": "Composition Over Inheritance",
                        "subtitle": "Has-A vs Is-A",
                        "metadata": {
                            "difficulty": "Intermediate",
                            "time": "30 mins",
                            "concepts": [
                                "Composition",
                                "ECS (Entity Component System)",
                                "Mixins"
                            ]
                        }
                    },
                    {
                        "type": "story",
                        "title": "The Taxonomic Nightmare",
                        "content": "You have `Enemy`. You subclass `FlyingEnemy` and `SwimmingEnemy`. Now the designers want a `FlyingSwimmingEnemy`. Do you use multiple inheritance? Then they want a `FlyingSwimmingShootingEnemy`. The hierarchy explodes!"
                    },
                    {
                        "type": "concept",
                        "title": "Prefer Composition",
                        "content": "Instead of deeply nested \"IS-A\" relationships (Inheritance), assemble behaviors using \"HAS-A\" relationships (Composition). An entity is just a container of behaviors."
                    },
                    {
                        "type": "comparison_table",
                        "title": "Inheritance vs Composition",
                        "headers": [
                            "Feature",
                            "Inheritance",
                            "Composition"
                        ],
                        "rows": [
                            [
                                "Relationship",
                                "Is-A",
                                "Has-A"
                            ],
                            [
                                "Binding",
                                "Compile-time (Static)",
                                "Run-time (Dynamic)"
                            ],
                            [
                                "Flexibility",
                                "Rigid hierarchies",
                                "Easily mix-and-match"
                            ],
                            [
                                "Code Reuse",
                                "Via Base classes",
                                "Via Component inclusion"
                            ]
                        ]
                    },
                    {
                        "type": "annotated_code",
                        "title": "Component-Based Approach",
                        "code": "class TransformComponent { public: float x, y, z; };\nclass FlyingComponent { public: void flapWings() {} };\nclass SwimmingComponent { public: void paddle() {} };\n\nclass Entity {\n    std::unique_ptr<TransformComponent> transform;\n    std::unique_ptr<FlyingComponent> flier;\n    std::unique_ptr<SwimmingComponent> swimmer;\npublic:\n    // Assemble dynamically!\n    void addFlying() { flier = std::make_unique<FlyingComponent>(); }\n    void update() {\n        if (flier) flier->flapWings();\n    }\n};",
                        "annotations": [
                            {
                                "line": "std::unique_ptr<FlyingComponent> flier;",
                                "text": "The Entity HAS A flying component. It can be added or removed at runtime!"
                            }
                        ]
                    },
                    {
                        "type": "code_lab",
                        "title": "Building an ECS",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\n// TODO: Create an IComponent interface with a virtual update() method.\n// TODO: Create a HealthComponent and a RenderComponent that implement IComponent.\n// TODO: Create an Entity that holds a std::vector<std::shared_ptr<IComponent>> and updates them all.\n\nint main() {\n    // Create entity, add components, run entity.update()\n    return 0;\n}\n",
                        "expected_output": "Updating Health\nUpdating Render\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nstruct IComponent {\n    virtual void update() = 0;\n    virtual ~IComponent() = default;\n};\n\nstruct HealthComponent : public IComponent {\n    void update() override { std::cout << \"Updating Health\\n\"; }\n};\n\nstruct RenderComponent : public IComponent {\n    void update() override { std::cout << \"Updating Render\\n\"; }\n};\n\nclass Entity {\n    std::vector<std::shared_ptr<IComponent>> components;\npublic:\n    void addComponent(std::shared_ptr<IComponent> c) { components.push_back(std::move(c)); }\n    void update() {\n        for (const auto& c : components) c->update();\n    }\n};\n\nint main() {\n    Entity player;\n    player.addComponent(std::make_shared<HealthComponent>());\n    player.addComponent(std::make_shared<RenderComponent>());\n    player.update();\n    return 0;\n}\n",
                        "hint": "Read the comments carefully and fill in the missing C++ logic.",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            }
        ]
    },
    "24": {
        "format": "episodic",
        "episodes": [
            {
                "title": "Module 1: The One and Only (Singleton)",
                "blocks": [
                    {
                        "type": "header",
                        "title": "Design Patterns",
                        "subtitle": "Singleton Pattern",
                        "metadata": {
                            "difficulty": "Intermediate",
                            "time": "20m",
                            "concepts": [
                                "Design Patterns",
                                "Singleton"
                            ]
                        }
                    },
                    {
                        "type": "mermaid_diagram",
                        "title": "Architectural Overview",
                        "explanation": "Before we write code, study this structural model to understand the relationships we are building.",
                        "code": "classDiagram\n    class EngineManager {\n        -static EngineManager* instance\n        -EngineManager()\n        +static getInstance() EngineManager*\n    }\n    class GameObjectFactory {\n        +createEntity(string type) IEntity*\n    }\n    class IEventListener {\n        +onNotify(string eventName)* void\n    }\n    class EventDispatcher {\n        -vector listeners\n        +subscribe(IEventListener* l) void\n        +broadcast(string eventName) void\n    }\n    class SoundEngine {\n        +onNotify(string eventName) void\n    }\n    note for IEventListener \"Observer Interface\"\n    IEventListener <|.. SoundEngine : \"implements (Observer)\"\n    EventDispatcher o-- IEventListener : \"notifies subscribers\"\n    GameObjectFactory ..> EngineManager : \"registers with (Singleton)\" "
                    },
                    {
                        "type": "story",
                        "title": "The Global Log Manager",
                        "content": "Your team is building a massive trading platform. They realize that multiple parts of the system are trying to open the log file simultaneously, causing file lock errors and corrupted logs. The lead architect says, 'We need exactly one instance of our Logger to coordinate all writes.'"
                    },
                    {
                        "type": "concept",
                        "title": "The Singleton Pattern",
                        "content": "The Singleton pattern ensures a class has only one instance, and provides a global point of access to it. It is useful for managing shared resources like configuration settings, logging, or connection pools."
                    },
                    {
                        "type": "mental_model",
                        "title": "Singleton Structure",
                        "data": "   +---------------------+\n   |      Singleton      |\n   +---------------------+\n   | - instance: Type*   |\n   +---------------------+\n   | - Singleton()       |\n   | + getInstance():Type|\n   +---------------------+"
                    },
                    {
                        "type": "annotated_code",
                        "title": "Implementing a basic Singleton",
                        "code": "class Logger {\nprivate:\n    static Logger* instance;\n    Logger() {} // Private constructor\npublic:\n    static Logger* getInstance() {\n        if (!instance) {\n            instance = new Logger();\n        }\n        return instance;\n    }\n};",
                        "annotations": [
                            {
                                "line": "static Logger* instance;",
                                "text": "Holds the single instance"
                            },
                            {
                                "line": "Logger() {}",
                                "text": "Private constructor prevents direct instantiation"
                            },
                            {
                                "line": "if (!instance)",
                                "text": "Lazy initialization"
                            }
                        ]
                    },
                    {
                        "type": "common_mistakes",
                        "title": "Singleton Pitfalls",
                        "mistakes": [
                            {
                                "title": "Thread Safety",
                                "desc": "The basic lazy initialization is not thread-safe. Multiple threads can create multiple instances if they pass the null check simultaneously."
                            },
                            {
                                "title": "Hidden Dependencies",
                                "desc": "Singletons introduce global state, making code harder to test and reason about."
                            }
                        ]
                    },
                    {
                        "type": "think_first",
                        "question": "In modern C++, what is the best way to implement a thread-safe Singleton?",
                        "options": [
                            "Using mutex locks on a pointer",
                            "Using a static local variable (Meyers' Singleton)",
                            "Using atomic pointers"
                        ],
                        "answer": 1,
                        "explanation": "In C++11 and later, static local variables are guaranteed to be initialized in a thread-safe manner, making Meyers' Singleton the cleanest and most efficient approach."
                    },
                    {
                        "type": "code_lab",
                        "title": "Implement Meyers' Singleton",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass ConfigManager {\n    // Implement a thread-safe Singleton using a local static variable\n};\n\nint main() {\n    std::cout << \"Success\";\n    return 0;\n}\n",
                        "expected_output": "Success",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nclass ConfigManager {\n    // Implement a thread-safe Singleton using a local static variable\n};\n\nint main() {\n    std::cout << \"Success\";\n    return 0;\n}\n",
                        "hint": "Read the comments carefully and fill in the missing C++ logic.",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 2: The Factory Method",
                "blocks": [
                    {
                        "type": "header",
                        "title": "Design Patterns",
                        "subtitle": "Factory Method",
                        "metadata": {
                            "difficulty": "Intermediate",
                            "time": "25m",
                            "concepts": [
                                "Creational Patterns",
                                "Factory",
                                "Polymorphism"
                            ]
                        }
                    },
                    {
                        "type": "story",
                        "title": "The Enemy Spawner",
                        "content": "You are writing a game engine. You have different levels: a Forest level and a Volcano level. In the Forest, enemies are Goblins. In the Volcano, enemies are Fire Elementals. Instead of writing messy if-else statements everywhere, you need a way to let the level itself decide which enemies to spawn."
                    },
                    {
                        "type": "concept",
                        "title": "Factory Method Pattern",
                        "content": "The Factory Method pattern defines an interface for creating an object, but lets subclasses decide which class to instantiate. It defers instantiation to subclasses."
                    },
                    {
                        "type": "comparison_table",
                        "title": "Direct Instantiation vs Factory Method",
                        "headers": [
                            "Direct Instantiation (`new`)",
                            "Factory Method"
                        ],
                        "rows": [
                            [
                                "Couples code to specific classes",
                                "Decouples code from specific classes"
                            ],
                            [
                                "Hard to extend",
                                "Easy to extend by adding new factory subclasses"
                            ],
                            [
                                "Violates Open/Closed Principle",
                                "Follows Open/Closed Principle"
                            ]
                        ]
                    },
                    {
                        "type": "annotated_code",
                        "title": "Enemy Spawner Factory",
                        "code": "class Enemy { public: virtual void attack() = 0; };\nclass Goblin : public Enemy { public: void attack() override {} };\n\nclass Level {\npublic:\n    virtual Enemy* createEnemy() = 0; // Factory Method\n    void spawn() {\n        Enemy* e = createEnemy();\n        e->attack();\n    }\n};\n\nclass ForestLevel : public Level {\npublic:\n    Enemy* createEnemy() override { return new Goblin(); }\n};",
                        "annotations": [
                            {
                                "line": "virtual Enemy* createEnemy() = 0;",
                                "text": "The factory method signature"
                            },
                            {
                                "line": "Enemy* e = createEnemy();",
                                "text": "Base class uses the factory method without knowing the concrete type"
                            },
                            {
                                "line": "return new Goblin();",
                                "text": "Subclass provides the specific implementation"
                            }
                        ]
                    },
                    {
                        "type": "wrong_approach",
                        "title": "The Simple Factory Anti-Pattern",
                        "code": "Enemy* createEnemy(int type) {\n    if (type == 1) return new Goblin();\n    else if (type == 2) return new FireElemental();\n    return nullptr;\n}",
                        "explanation": "This requires modifying the factory method every time a new enemy type is added, violating the Open/Closed Principle."
                    },
                    {
                        "type": "mastery_challenge",
                        "title": "Factory Ownership",
                        "question": "Who is usually responsible for deleting the object created by a Factory Method?",
                        "options": [
                            "The Factory itself",
                            "The caller (client) that received the object",
                            "A global garbage collector"
                        ],
                        "answer": 1,
                        "explanation": "In C++, unless returning smart pointers, the caller assumes ownership of the raw pointer and is responsible for deleting it. Modern C++ typically returns std::unique_ptr from factories to make ownership clear."
                    }
                ]
            },
            {
                "title": "Module 3: The Observer Pattern",
                "blocks": [
                    {
                        "type": "header",
                        "title": "Design Patterns",
                        "subtitle": "Observer Pattern",
                        "metadata": {
                            "difficulty": "Intermediate",
                            "time": "30m",
                            "concepts": [
                                "Behavioral Patterns",
                                "Observer",
                                "Event-Driven"
                            ]
                        }
                    },
                    {
                        "type": "story",
                        "title": "The Stock Ticker",
                        "content": "You are building a financial dashboard. When the price of 'AAPL' changes, the UI chart needs to update, the trading bot needs to evaluate its strategy, and the logging system needs to record the tick. If the core Stock class calls all these systems directly, it becomes a tangled mess."
                    },
                    {
                        "type": "concept",
                        "title": "The Observer Pattern",
                        "content": "The Observer pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically."
                    },
                    {
                        "type": "mental_model",
                        "title": "Publisher-Subscriber",
                        "data": " [Subject] ---notify()---> [Observer 1]\n           ---notify()---> [Observer 2]\n           ---notify()---> [Observer 3]"
                    },
                    {
                        "type": "annotated_code",
                        "title": "Implementing Observer",
                        "code": "class Observer {\npublic:\n    virtual void update(float price) = 0;\n};\n\nclass Subject {\n    std::vector<Observer*> observers;\npublic:\n    void attach(Observer* o) { observers.push_back(o); }\n    void notify(float price) {\n        for (auto o : observers) o->update(price);\n    }\n};",
                        "annotations": [
                            {
                                "line": "virtual void update(float price) = 0;",
                                "text": "The interface that all listeners must implement"
                            },
                            {
                                "line": "std::vector<Observer*> observers;",
                                "text": "List of subscribers"
                            },
                            {
                                "line": "for (auto o : observers) o->update(price);",
                                "text": "Broadcasting the event to all subscribers"
                            }
                        ]
                    },
                    {
                        "type": "real_world_analogy",
                        "title": "YouTube Subscriptions",
                        "content": "Think of a YouTube channel as the Subject, and subscribers as Observers. When a new video is uploaded, YouTube notifies all subscribers. The channel doesn't need to know who the subscribers are, just that they want to be notified."
                    },
                    {
                        "type": "code_lab",
                        "title": "Connect the Chart",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nstruct Observer {\n    virtual void update(int value) = 0;\n    virtual ~Observer() = default;\n};\n\nclass Chart : public Observer {\npublic:\n    void update(int value) override { (void)value; /* implement chart refresh */ }\n};\n\nint main() {\n    Chart c;\n    c.update(42);\n    std::cout << \"Success\";\n    return 0;\n}\n",
                        "expected_output": "Success",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nstruct Observer {\n    virtual void update(int value) = 0;\n    virtual ~Observer() = default;\n};\n\nclass Chart : public Observer {\npublic:\n    void update(int value) override { (void)value; }\n};\n\nint main() {\n    Chart c;\n    c.update(42);\n    std::cout << \"Success\";\n    return 0;\n}\n",
                        "hint": "Fill in the missing parts of the code.",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 4: Pattern Synthesis",
                "blocks": [
                    {
                        "type": "header",
                        "title": "Design Patterns",
                        "subtitle": "Combining Patterns",
                        "metadata": {
                            "difficulty": "Advanced",
                            "time": "25m",
                            "concepts": [
                                "Architecture",
                                "System Design"
                            ]
                        }
                    },
                    {
                        "type": "story",
                        "title": "The Event Bus",
                        "content": "Patterns rarely live in isolation. You want to build a central Event Bus for your application. The Event Bus should be globally accessible, create specific event objects on demand, and distribute them to interested listeners."
                    },
                    {
                        "type": "problem",
                        "content": "How can we use Singleton, Factory, and Observer together to build an Event Bus?"
                    },
                    {
                        "type": "concept",
                        "title": "Synergy of Patterns",
                        "content": "Singleton provides the central access point for the Event Bus. The Event Bus acts as a Subject (Observer pattern) managing subscribers. A Factory can be used to generate specific Event objects based on incoming raw data."
                    },
                    {
                        "type": "execution_trace",
                        "title": "Event Flow",
                        "code": "EventBus::getInstance().publish(\"LOGIN\", data);",
                        "trace": [
                            "1. Retrieve Singleton EventBus instance",
                            "2. EventBus looks up Observers mapped to 'LOGIN'",
                            "3. Factory (optional) converts raw data into a structured LoginEvent object",
                            "4. EventBus loops through Observers and calls update(event)"
                        ]
                    },
                    {
                        "type": "mastery_challenge",
                        "title": "Pattern Recognition",
                        "question": "If you have a UI button that runs a callback when clicked, what pattern is primarily being used?",
                        "options": [
                            "Singleton",
                            "Factory",
                            "Observer",
                            "Decorator"
                        ],
                        "answer": 2,
                        "explanation": "Callbacks/Events in UI frameworks are a classic application of the Observer pattern (often simplified to a single observer/callback)."
                    }
                ]
            }
        ]
    },
    "25": {
        "format": "episodic",
        "episodes": [
            {
                "title": "Module 1: Introduction to System Architecture",
                "blocks": [
                    {
                        "type": "header",
                        "title": "System Architecture",
                        "subtitle": "UML & Abstraction",
                        "metadata": {
                            "difficulty": "Intermediate",
                            "time": "20m",
                            "concepts": [
                                "Architecture",
                                "UML",
                                "Modeling"
                            ]
                        }
                    },
                    {
                        "type": "mermaid_diagram",
                        "title": "Architectural Overview",
                        "explanation": "Before we write code, study this structural model to understand the relationships we are building.",
                        "code": "flowchart TD\n    subgraph SubsystemA[\"Physics Engine (High Cohesion)\"]\n        COL[\"CollisionDetector\"] --- RIGID[\"RigidBodyDynamics\"]\n        RIGID --- GRAV[\"GravitySimulator\"]\n    end\n    subgraph FacadeLayer[\"Clean Facade Gateway\"]\n        FACADE[\"IPhysicsFacade\n+stepSimulation(dt)\n+applyImpulse(entityId, vec)\"]\n    end\n    subgraph SubsystemB[\"Game Logic Core (Low Coupling)\"]\n        GAME[\"GameplayManager\"]\n        AI[\"BehaviorTreeController\"]\n    end\n    SubsystemA --> FACADE\n    GAME --> FACADE\n    AI --> FACADE"
                    },
                    {
                        "type": "story",
                        "title": "The Spaghetti Codebase",
                        "content": "You've joined a startup. Their app works, but touching the 'User' class breaks the 'Payment' system. The codebase is a tangled web of dependencies. The senior engineer sighs, 'We need to visualize this before we refactor.'"
                    },
                    {
                        "type": "concept",
                        "title": "Why Model Architecture?",
                        "content": "System architecture provides a high-level view of how components interact. UML (Unified Modeling Language) is a standard way to visualize the design of a system. It helps identify tight coupling, circular dependencies, and structural flaws before writing code."
                    },
                    {
                        "type": "mental_model",
                        "title": "UML Class Diagram Basics",
                        "data": " +------------------+\n |    ClassName     |\n +------------------+\n | - privateVar     |\n | + publicVar      |\n +------------------+\n | + method()       |\n +------------------+"
                    },
                    {
                        "type": "comparison_table",
                        "title": "UML Access Modifiers",
                        "headers": [
                            "Symbol",
                            "Meaning",
                            "C++ Equivalent"
                        ],
                        "rows": [
                            [
                                "+",
                                "Public",
                                "public:"
                            ],
                            [
                                "-",
                                "Private",
                                "private:"
                            ],
                            [
                                "#",
                                "Protected",
                                "protected:"
                            ]
                        ]
                    },
                    {
                        "type": "think_first",
                        "question": "Why is it important to diagram a system before building it?",
                        "options": [
                            "To make the code run faster",
                            "To catch structural problems early when they are cheap to fix",
                            "To generate code automatically"
                        ],
                        "answer": 1,
                        "explanation": "Architectural flaws are incredibly expensive to fix once code is written. Diagramming helps identify and resolve these issues in the planning phase."
                    }
                ]
            },
            {
                "title": "Module 2: Class Relationships",
                "blocks": [
                    {
                        "type": "header",
                        "title": "System Architecture",
                        "subtitle": "Associations & Dependencies",
                        "metadata": {
                            "difficulty": "Intermediate",
                            "time": "30m",
                            "concepts": [
                                "UML Relationships",
                                "Aggregation",
                                "Composition"
                            ]
                        }
                    },
                    {
                        "type": "story",
                        "title": "The Car Dealership",
                        "content": "You are modeling a Dealership. A Dealership 'has a' fleet of Cars. A Car 'has an' Engine. But what happens if the Dealership goes bankrupt? The Cars still exist. What if the Car is destroyed? The Engine goes with it. We need to model these different types of relationships."
                    },
                    {
                        "type": "concept",
                        "title": "Composition vs Aggregation",
                        "content": "Both represent 'has-a' relationships. Composition is a strong relationship: the child's lifecycle is bound to the parent (Car destroys Engine). Aggregation is a weak relationship: the child can exist independently of the parent (Dealership can close, Cars are sold elsewhere)."
                    },
                    {
                        "type": "annotated_code",
                        "title": "Composition in C++",
                        "code": "class Car {\n    Engine engine; // Composition: Engine lives and dies with Car\npublic:\n    Car() {}\n};",
                        "annotations": [
                            {
                                "line": "Engine engine;",
                                "text": "Value type member. Created when Car is created, destroyed when Car is destroyed."
                            }
                        ]
                    },
                    {
                        "type": "annotated_code",
                        "title": "Aggregation in C++",
                        "code": "class Dealership {\n    std::vector<Car*> inventory; // Aggregation: Dealership points to Cars, but doesn't own them exclusively\npublic:\n    void addCar(Car* c) { inventory.push_back(c); }\n};",
                        "annotations": [
                            {
                                "line": "std::vector<Car*> inventory;",
                                "text": "Pointer/Reference based. Destroying the Dealership doesn't implicitly delete the Cars."
                            }
                        ]
                    },
                    {
                        "type": "mental_model",
                        "title": "UML Symbols",
                        "data": "Dependency: A - - - > B  (A uses B)\nAssociation: A ------ B  (A knows B)\nAggregation: A <>---- B  (A has B, weak)\nComposition: A <X>--- B  (A owns B, strong. <X> is filled diamond)\nInheritance: A <|---- B  (B is A)"
                    },
                    {
                        "type": "mastery_challenge",
                        "title": "Relationship Identification",
                        "question": "In a UI framework, a Window contains a Button. If the Window is closed and destroyed, the Button is also destroyed. What relationship is this?",
                        "options": [
                            "Association",
                            "Aggregation",
                            "Composition",
                            "Dependency"
                        ],
                        "answer": 2,
                        "explanation": "Because the lifecycle of the Button is strictly tied to the Window (strong ownership), this is Composition."
                    }
                ]
            },
            {
                "title": "Module 3: Subsystems and APIs",
                "blocks": [
                    {
                        "type": "header",
                        "title": "System Architecture",
                        "subtitle": "Designing Interfaces",
                        "metadata": {
                            "difficulty": "Advanced",
                            "time": "25m",
                            "concepts": [
                                "Subsystems",
                                "Interfaces",
                                "Fa\u00e7ade"
                            ]
                        }
                    },
                    {
                        "type": "story",
                        "title": "The Audio Engine",
                        "content": "Your game has an Audio Engine. Internally, it has SoundBuffers, AudioMixers, SpatialAudioProcessors, and CodecDecoders. The gameplay programmers just want to play a sound. If they have to understand all these internal classes, they will go crazy."
                    },
                    {
                        "type": "concept",
                        "title": "Subsystems and The Fa\u00e7ade Pattern",
                        "content": "A subsystem is a logical grouping of related classes. To make a subsystem easy to use, we provide a unified, simplified interface to it, hiding the complexity. This is known as the Fa\u00e7ade pattern."
                    },
                    {
                        "type": "wrong_approach",
                        "title": "Leaking Complexity",
                        "code": "// Gameplay Code\nDecoder d = new VorbisDecoder(\"boom.ogg\");\nBuffer b = d.decode();\nMixer::getInstance().attach(b);\nMixer::getInstance().play();",
                        "explanation": "The gameplay code is tightly coupled to the internals of the audio system."
                    },
                    {
                        "type": "correct_approach",
                        "title": "Using a Fa\u00e7ade",
                        "code": "// AudioSystem (Fa\u00e7ade)\nclass AudioSystem {\npublic:\n    void playSound(const std::string& filename);\n};\n\n// Gameplay Code\naudioSystem.playSound(\"boom.ogg\");",
                        "explanation": "The complex internal interactions are hidden behind a clean API. The gameplay code is decoupled from the specific decoders and mixers."
                    },
                    {
                        "type": "code_lab",
                        "title": "Design a Fa\u00e7ade",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nstruct VideoDecoder { void decode() {} };\nstruct RenderPipeline { void render() {} };\n\nclass VideoPlayer {\n    VideoDecoder decoder;\n    RenderPipeline pipeline;\npublic:\n    // TODO: Create a simple play() API hiding Decoder and Pipeline\n};\n\nint main() {\n    std::cout << \"Success\";\n    return 0;\n}\n",
                        "expected_output": "Success",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nstruct VideoDecoder { void decode() {} };\nstruct RenderPipeline { void render() {} };\n\nclass VideoPlayer {\n    VideoDecoder decoder;\n    RenderPipeline pipeline;\npublic:\n    void play() {\n        decoder.decode();\n        pipeline.render();\n    }\n};\n\nint main() {\n    VideoPlayer player;\n    player.play();\n    std::cout << \"Success\";\n    return 0;\n}\n",
                        "hint": "Fill in the missing parts of the code.",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 4: Coupling and Cohesion",
                "blocks": [
                    {
                        "type": "header",
                        "title": "System Architecture",
                        "subtitle": "Evaluating Design",
                        "metadata": {
                            "difficulty": "Advanced",
                            "time": "20m",
                            "concepts": [
                                "Coupling",
                                "Cohesion",
                                "Metrics"
                            ]
                        }
                    },
                    {
                        "type": "story",
                        "title": "The God Object",
                        "content": "You find a class named 'GameManager'. It is 15,000 lines long. It handles rendering, physics, networking, and saving the game. Every time someone changes the rendering code, the networking breaks. It's a nightmare."
                    },
                    {
                        "type": "concept",
                        "title": "Cohesion and Coupling",
                        "content": "Cohesion is how closely related the responsibilities of a single module/class are. High cohesion is good (a class does one thing well). Coupling is the degree of interdependence between modules. Low coupling is good (modules can be changed independently)."
                    },
                    {
                        "type": "comparison_table",
                        "title": "Architecture Goals",
                        "headers": [
                            "Metric",
                            "Goal",
                            "Description"
                        ],
                        "rows": [
                            [
                                "Cohesion",
                                "HIGH",
                                "Everything in a class belongs together. Single Responsibility Principle."
                            ],
                            [
                                "Coupling",
                                "LOW",
                                "Classes know as little as possible about other classes."
                            ]
                        ]
                    },
                    {
                        "type": "real_world_analogy",
                        "title": "The Kitchen",
                        "content": "High Cohesion: A toaster only toasts bread. A fridge only cools things. Low Coupling: You can replace the toaster without rewiring the fridge. If the toaster was built into the fridge (high coupling), replacing the toaster would be a massive project."
                    },
                    {
                        "type": "think_first",
                        "question": "What is the result of High Coupling and Low Cohesion?",
                        "options": [
                            "Modular, easy to maintain code",
                            "Spaghetti code where a single change breaks many unrelated things",
                            "Highly optimized machine code"
                        ],
                        "answer": 1,
                        "explanation": "High coupling means everything depends on everything else. Low cohesion means classes do unrelated tasks. This is the definition of spaghetti code."
                    }
                ]
            }
        ]
    },
    "26": {
        "format": "episodic",
        "episodes": [
            {
                "title": "Module 1: Memory Basics and sizeof",
                "blocks": [
                    {
                        "type": "header",
                        "title": "Object Memory Layout",
                        "subtitle": "Size and Basics",
                        "metadata": {
                            "difficulty": "Advanced",
                            "time": "25m",
                            "concepts": [
                                "sizeof",
                                "Memory",
                                "Primitives"
                            ]
                        }
                    },
                    {
                        "type": "mermaid_diagram",
                        "title": "Architectural Overview",
                        "explanation": "Before we write code, study this structural model to understand the relationships we are building.",
                        "code": "flowchart TD\n    subgraph ObjectRAM[\"Object Memory Byte Layout (sizeof = 24 bytes)\"]\n        OFF0[\"Offset 0x00 - 0x07 (8 Bytes)\n__vptr (Hidden pointer to Virtual Table)\"]\n        OFF8[\"Offset 0x08 - 0x0B (4 Bytes)\nint entityId = 1001\"]\n        OFF12[\"Offset 0x0C - 0x0F (4 Bytes)\nCompiler Alignment Padding\"]\n        OFF16[\"Offset 0x10 - 0x17 (8 Bytes)\ndouble energy = 99.85\"]\n    end\n    subgraph StaticVTable[\"Virtual Method Table (.rodata section)\"]\n        VTAB[\"Entity VTable:\n[0]: &Entity::render()\n[1]: &Entity::update()\n[2]: &Entity::~Entity()\"]\n    end\n    OFF0 --> StaticVTable"
                    },
                    {
                        "type": "memory_layout",
                        "title": "Object Memory Layout with vptr",
                        "explanation": "Polymorphic objects contain a hidden pointer (vptr) injected by the compiler that points to the class's Virtual Table.",
                        "cells": [
                            {
                                "address": "0xA000",
                                "value": "0xDEADBEEF",
                                "label": "vptr (Hidden)"
                            },
                            {
                                "address": "0xA008",
                                "value": "25",
                                "label": "int health"
                            },
                            {
                                "address": "0xA00C",
                                "value": "10",
                                "label": "int damage"
                            },
                            {
                                "address": "...",
                                "value": "...",
                                "label": "Padding"
                            }
                        ]
                    },
                    {
                        "type": "story",
                        "title": "The Network Packet",
                        "content": "You are writing a multiplayer game. You design a struct to send player positions over the network. You calculate that a char (1 byte) + int (4 bytes) should equal 5 bytes. You send 5 bytes, but the server crashes. You print `sizeof(Packet)` and it says 8! What happened?"
                    },
                    {
                        "type": "concept",
                        "title": "Memory Under the Hood",
                        "content": "When C++ creates an object in memory, it doesn't just jam the variables tightly together. The CPU reads memory more efficiently in 'chunks' (words). To facilitate this, the compiler aligns data on specific boundaries."
                    },
                    {
                        "type": "annotated_code",
                        "title": "Checking Sizes",
                        "code": "#include <iostream>\n\nstruct MyStruct {\n    char a;\n    int b;\n};\n\nint main() {\n    std::cout << sizeof(char) << \"\\n\"; // 1\n    std::cout << sizeof(int) << \"\\n\";  // 4\n    std::cout << sizeof(MyStruct) << \"\\n\"; // 8! (Wait, 1+4 != 8)\n}",
                        "annotations": [
                            {
                                "line": "std::cout << sizeof(MyStruct) << \"\\n\";",
                                "text": "The size is padded to 8 bytes due to alignment requirements."
                            }
                        ]
                    },
                    {
                        "type": "think_first",
                        "question": "Why doesn't the compiler just pack everything tightly to save memory?",
                        "options": [
                            "It makes compiling faster",
                            "CPUs read memory in word-sized chunks; unaligned access is slow or causes hardware exceptions",
                            "C++ standard requires structs to be powers of 2"
                        ],
                        "answer": 1,
                        "explanation": "Memory alignment is a hardware requirement. Fetching a 4-byte integer from an address that isn't a multiple of 4 requires the CPU to do extra work to piece it together."
                    }
                ]
            },
            {
                "title": "Module 2: Padding and Alignment",
                "blocks": [
                    {
                        "type": "header",
                        "title": "Object Memory Layout",
                        "subtitle": "Padding Rules",
                        "metadata": {
                            "difficulty": "Advanced",
                            "time": "30m",
                            "concepts": [
                                "Padding",
                                "Alignment",
                                "Optimization"
                            ]
                        }
                    },
                    {
                        "type": "concept",
                        "title": "Alignment Requirements",
                        "content": "Every type has an alignment requirement (usually equal to its size). An `int` (4 bytes) must reside at a memory address that is a multiple of 4. A `double` (8 bytes) at a multiple of 8. The compiler inserts hidden 'padding' bytes to satisfy these rules."
                    },
                    {
                        "type": "mental_model",
                        "title": "Visualizing Padding",
                        "data": "struct BadLayout {\n  char c;   // 1 byte\n            // 3 bytes PADDING\n  int i;    // 4 bytes\n  short s;  // 2 bytes\n            // 2 bytes PADDING (to make total size a multiple of largest alignment, 4)\n}; // Total: 12 bytes"
                    },
                    {
                        "type": "wrong_approach",
                        "title": "Inefficient Ordering",
                        "code": "struct BadLayout {\n    char a; // 1 byte\n    double b; // 8 bytes\n    char c; // 1 byte\n};",
                        "explanation": "Size is 24 bytes! [char][7 pad][double][char][7 pad]. The compiler pads between a and b, and pads the end so that in an array, the next struct starts on an 8-byte boundary."
                    },
                    {
                        "type": "correct_approach",
                        "title": "Optimal Ordering",
                        "code": "struct GoodLayout {\n    double b; // 8 bytes\n    char a; // 1 byte\n    char c; // 1 byte\n};",
                        "explanation": "Size is 16 bytes. [double][char][char][6 pad]. By ordering largest to smallest, we minimize internal padding."
                    },
                    {
                        "type": "code_lab",
                        "title": "Optimize the Struct",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nstruct Data {\n    bool active;\n    long long id;\n    short level;\n};\n// Reorder variables to minimize sizeof(Data)\n\nint main() {\n    std::cout << \"Success\";\n    return 0;\n}\n",
                        "expected_output": "Success",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nstruct Data {\n    bool active;\n    long long id;\n    short level;\n};\n// Reorder variables to minimize sizeof(Data)\n\nint main() {\n    std::cout << \"Success\";\n    return 0;\n}\n",
                        "hint": "Fill in the missing parts of the code.",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 3: Inheritance and Memory",
                "blocks": [
                    {
                        "type": "header",
                        "title": "Object Memory Layout",
                        "subtitle": "Base and Derived Classes",
                        "metadata": {
                            "difficulty": "Expert",
                            "time": "25m",
                            "concepts": [
                                "Inheritance",
                                "Memory Layout"
                            ]
                        }
                    },
                    {
                        "type": "story",
                        "title": "The Expanding Object",
                        "content": "You have a base class `Entity` with an X and Y coordinate. You create a `Player` class inheriting from `Entity`. Where do the Player's variables go in memory relative to the Entity's?"
                    },
                    {
                        "type": "concept",
                        "title": "Layout with Inheritance",
                        "content": "In C++, a derived class object contains the base class object as a subobject. The base class members typically come first in memory, followed by the derived class members. Alignment rules still apply across the boundary."
                    },
                    {
                        "type": "mental_model",
                        "title": "Derived Class Memory Map",
                        "data": "class Base { int x; };\nclass Derived : public Base { int y; };\n\nMemory Layout for Derived:\n[ Base::x (4 bytes) ]  <-- Address of object points here\n[ Derived::y (4 bytes) ]"
                    },
                    {
                        "type": "annotated_code",
                        "title": "Pointer Casting",
                        "code": "Derived d;\nBase* bp = &d;\nDerived* dp = &d;",
                        "annotations": [
                            {
                                "line": "Base* bp = &d;",
                                "text": "bp points to the start of the Base subobject (which happens to be the start of the Derived object here)."
                            }
                        ]
                    },
                    {
                        "type": "mastery_challenge",
                        "title": "Empty Base Class",
                        "question": "If a class has no members, its size is usually 1 byte. If you inherit from an empty base class, does the derived class size increase?",
                        "options": [
                            "Yes, by 1 byte for the base class",
                            "No, C++ performs Empty Base Class Optimization (EBCO)",
                            "Yes, by the size of a pointer"
                        ],
                        "answer": 1,
                        "explanation": "C++ compilers usually apply the Empty Base Class Optimization (EBCO), ensuring that inheriting from an empty class does not increase the size of the derived class."
                    }
                ]
            },
            {
                "title": "Module 4: The Virtual Table Pointer (vptr)",
                "blocks": [
                    {
                        "type": "header",
                        "title": "Object Memory Layout",
                        "subtitle": "Polymorphism Cost",
                        "metadata": {
                            "difficulty": "Expert",
                            "time": "30m",
                            "concepts": [
                                "vptr",
                                "vtable",
                                "Virtual Functions"
                            ]
                        }
                    },
                    {
                        "type": "story",
                        "title": "The Hidden Cost",
                        "content": "You optimize your `Vector3` math struct to exactly 12 bytes. Later, someone adds `virtual ~Vector3() = default;` just to be safe. Suddenly, `sizeof(Vector3)` jumps to 24 bytes (on a 64-bit system)! Millions of vectors in your game just consumed double the memory."
                    },
                    {
                        "type": "concept",
                        "title": "The vptr (Virtual Table Pointer)",
                        "content": "When a class has at least one virtual function, the compiler must support runtime polymorphism. It does this by adding a hidden pointer (the vptr) to every object of that class. This vptr points to a static array of function pointers called the vtable."
                    },
                    {
                        "type": "mental_model",
                        "title": "vptr Layout",
                        "data": "class Poly { virtual void f(); int x; };\n\nMemory Map (64-bit system):\n[ vptr (8 bytes) ] -----> [ vtable for Poly ]\n[ x    (4 bytes) ]\n[ PAD  (4 bytes) ]\nTotal Size: 16 bytes"
                    },
                    {
                        "type": "comparison_table",
                        "title": "Non-Virtual vs Virtual Class",
                        "headers": [
                            "Feature",
                            "Non-Virtual Class",
                            "Virtual Class"
                        ],
                        "rows": [
                            [
                                "Memory Overhead per Object",
                                "0 bytes",
                                "Size of one pointer (e.g., 8 bytes)"
                            ],
                            [
                                "Function Call Speed",
                                "Direct jump (fast)",
                                "Pointer dereference via vtable (slightly slower)"
                            ],
                            [
                                "Polymorphism",
                                "Compile-time only",
                                "Runtime polymorphic resolution"
                            ]
                        ]
                    },
                    {
                        "type": "annotated_code",
                        "title": "vptr placement",
                        "code": "class Animal {\n    int age;\n    virtual void speak() {}\n};",
                        "annotations": [
                            {
                                "line": "virtual void speak() {}",
                                "text": "Adding 'virtual' silently inserts a vptr into the object's layout, usually at the very beginning of the object."
                            }
                        ]
                    },
                    {
                        "type": "think_first",
                        "question": "Why is the vptr usually placed at the very beginning (offset 0) of the object in memory?",
                        "options": [
                            "It looks cleaner in debuggers",
                            "It allows polymorphic base pointers to easily find the vptr without knowing the exact derived type's layout",
                            "It prevents memory fragmentation"
                        ],
                        "answer": 1,
                        "explanation": "Placing the vptr at offset 0 ensures that any pointer to a polymorphic base class can uniformly dereference it to find the vtable, regardless of what derived class it actually is."
                    }
                ]
            }
        ]
    },
    "27": {
        "format": "episodic",
        "episodes": [
            {
                "title": "Module 1: The Phantom Leak",
                "blocks": [
                    {
                        "type": "header",
                        "title": "The Phantom Leak",
                        "subtitle": "Introduction to Memory Leaks",
                        "metadata": {
                            "difficulty": "Intermediate",
                            "time": "20m",
                            "concepts": [
                                "Memory Leaks",
                                "Heap Management"
                            ]
                        }
                    },
                    {
                        "type": "mermaid_diagram",
                        "title": "Architectural Overview",
                        "explanation": "Before we write code, study this structural model to understand the relationships we are building.",
                        "code": "flowchart TD\n    subgraph BugDangling[\"Dangling Pointer Bug\"]\n        P1[\"int* ptr = 0x4000\"] --> M1[\"Freed Memory (0x4000)\"]\n        U1[\"*ptr = 10 yields Use-After-Free / Crash\"] --> M1\n    end\n    subgraph BugLeak[\"Memory Leak Bug\"]\n        P2[\"ptr = new Data() (0x5000)\"]\n        R2[\"ptr = new Data() (0x6000)\"]\n        P2 -. \"Pointer Overwritten\" .-> R2\n        LOST[\"Block 0x5000 Orphaned on Heap yields Leak\"]\n    end\n    subgraph SanitizerSolution[\"Detection & Remedy\"]\n        ASAN[\"AddressSanitizer / Valgrind\"] --> REPORT[\"Pinpoints Allocation Call Stack\"]\n        REPORT --> FIX[\"Fix with Modern RAII & std::unique_ptr\"]\n    end"
                    },
                    {
                        "type": "story",
                        "title": "System Crash at 3 AM",
                        "content": "The central monitoring system of your autonomous rover crashed after 3 days of continuous operation. The logs indicate an Out-Of-Memory (OOM) error. Your task is to identify why memory is being consumed but never released."
                    },
                    {
                        "type": "concept",
                        "title": "What is a Memory Leak?",
                        "content": "A memory leak occurs when a program allocates memory on the heap (using `new` or `malloc`) but fails to deallocate it (using `delete` or `free`) before all pointers to that memory go out of scope. The memory becomes unreachable and unusable for the lifetime of the program."
                    },
                    {
                        "type": "mental_model",
                        "title": "Memory Leak Visualization",
                        "data": "Heap Memory:\n[  In Use  ] [  In Use  ] [   Free   ]\n     ^             ^\n  ptr1 (Valid)  (No pointers!) -> LEAK"
                    },
                    {
                        "type": "annotated_code",
                        "title": "A Classic Leak",
                        "code": "void processData() {\n    SensorData* data = new SensorData();\n    data->read();\n    // Forgot to delete data!\n}",
                        "annotations": [
                            {
                                "line": "SensorData* data = new SensorData();",
                                "text": "Memory allocated on the heap."
                            },
                            {
                                "line": "// Forgot to delete data!",
                                "text": "Function exits, 'data' pointer is destroyed, but the memory it points to remains allocated."
                            }
                        ]
                    },
                    {
                        "type": "think_first",
                        "question": "If a memory leak occurs in a function that is called 1000 times a second, what is the most likely immediate symptom?",
                        "options": [
                            "The program will fail to compile.",
                            "The program will slowly consume all available RAM and eventually crash.",
                            "The CPU will overheat.",
                            "Variables will have corrupted values."
                        ],
                        "answer": 1,
                        "explanation": "Memory leaks cause the application's memory footprint to grow steadily until the OS runs out of RAM and terminates the process."
                    },
                    {
                        "type": "problem",
                        "content": "Review your application's continuous monitoring loops for hidden heap allocations that aren't paired with deallocations."
                    }
                ]
            },
            {
                "title": "Module 2: Valgrind in Action",
                "blocks": [
                    {
                        "type": "header",
                        "title": "Hunting with Valgrind",
                        "subtitle": "Memory Profiling Tools",
                        "metadata": {
                            "difficulty": "Intermediate",
                            "time": "30m",
                            "concepts": [
                                "Valgrind",
                                "Address Sanitizer",
                                "Debugging"
                            ]
                        }
                    },
                    {
                        "type": "story",
                        "title": "The Ghost Hunter",
                        "content": "Staring at thousands of lines of code to find a missing `delete` is impossible. You need a tool to track memory allocations dynamically as the program runs. Enter Valgrind."
                    },
                    {
                        "type": "concept",
                        "title": "Valgrind Memcheck",
                        "content": "Valgrind is an instrumentation framework that helps detect memory management and threading bugs. Its Memcheck tool keeps track of every memory allocation and deallocation, alerting you to leaks, uninitialized memory usage, and out-of-bounds accesses."
                    },
                    {
                        "type": "execution_trace",
                        "title": "Analyzing Valgrind Output",
                        "code": "==12345== HEAP SUMMARY:\n==12345==     in use at exit: 40 bytes in 1 blocks\n==12345==   total heap usage: 2 allocs, 1 frees, 1,064 bytes allocated\n==12345== \n==12345== 40 bytes in 1 blocks are definitely lost in loss record 1 of 1\n==12345==    at 0x4C29F73: operator new(unsigned long) (vg_replace_malloc.c:334)\n==12345==    by 0x400A7D: createSensor() (main.cpp:10)\n==12345==    by 0x400A9E: main (main.cpp:16)",
                        "trace": [
                            "HEAP SUMMARY shows 1 allocation was not freed.",
                            "'definitely lost' means there are no pointers left pointing to this memory.",
                            "The stack trace pinpoints exactly where the leaked memory was allocated: line 10 in main.cpp."
                        ]
                    },
                    {
                        "type": "comparison_table",
                        "title": "Valgrind vs Address Sanitizer (ASan)",
                        "headers": [
                            "Feature",
                            "Valgrind",
                            "Address Sanitizer (ASan)"
                        ],
                        "rows": [
                            [
                                "Implementation",
                                "Dynamic Binary Translation",
                                "Compiler Instrumentation"
                            ],
                            [
                                "Performance Overhead",
                                "20x - 50x slower",
                                "2x slower"
                            ],
                            [
                                "Recompilation Required?",
                                "No",
                                "Yes (needs -fsanitize=address)"
                            ],
                            [
                                "Detects Memory Leaks?",
                                "Yes",
                                "Yes"
                            ]
                        ]
                    },
                    {
                        "type": "think_first",
                        "question": "If you are running a real-time game engine and need to check for memory leaks without tanking the framerate too much, which tool is better suited?",
                        "options": [
                            "Valgrind",
                            "Address Sanitizer"
                        ],
                        "answer": 1,
                        "explanation": "Address Sanitizer has significantly lower overhead compared to Valgrind, making it better for real-time applications."
                    },
                    {
                        "type": "code_lab",
                        "title": "Fix the Leak Detected by Valgrind",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nstruct Logger { void print(const char*) {} };\nbool error_occurred = true;\n\nvoid runDiagnostic() {\n    Logger* log = new Logger();\n    log->print(\"Running diag...\");\n    if (error_occurred) {\n        return; // TODO: Fix with std::unique_ptr so Logger cannot leak!\n    }\n    delete log;\n}\n\nint main() {\n    runDiagnostic();\n    std::cout << \"Fix the early return so that the logger is always deleted.\";\n    return 0;\n}\n",
                        "expected_output": "Fix the early return so that the logger is always deleted.",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nstruct Logger { void print(const char*) {} };\nbool error_occurred = true;\n\nvoid runDiagnostic() {\n    auto log = std::make_unique<Logger>();\n    log->print(\"Running diag...\");\n    if (error_occurred) {\n        return; // RAII automatically deletes log cleanly!\n    }\n}\n\nint main() {\n    runDiagnostic();\n    std::cout << \"Fix the early return so that the logger is always deleted.\";\n    return 0;\n}\n",
                        "hint": "Fill in the missing parts of the code.",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 3: Dangling Pointers & Double Frees",
                "blocks": [
                    {
                        "type": "header",
                        "title": "Dangling Pointers",
                        "subtitle": "Use-After-Free and Double Free",
                        "metadata": {
                            "difficulty": "Hard",
                            "time": "25m",
                            "concepts": [
                                "Dangling Pointers",
                                "Use-After-Free"
                            ]
                        }
                    },
                    {
                        "type": "story",
                        "title": "Segmentation Fault (core dumped)",
                        "content": "You fixed the memory leak, but now the program crashes randomly with a Segfault. Valgrind reports an 'Invalid read of size 4'. What did you do?"
                    },
                    {
                        "type": "concept",
                        "title": "The Danger of Stale Pointers",
                        "content": "A dangling pointer is a pointer that points to memory that has already been deallocated. Accessing it (Use-After-Free) leads to undefined behavior, often reading garbage data or crashing. Deleting it again (Double Free) corrupts the heap manager's internal structures."
                    },
                    {
                        "type": "wrong_approach",
                        "title": "The Double Free",
                        "code": "int* ptr = new int(10);\ndelete ptr;\n// ... later in the code ...\ndelete ptr; // CRASH!",
                        "explanation": "The second delete attempts to free memory that is no longer owned by the application."
                    },
                    {
                        "type": "correct_approach",
                        "title": "Nullifying Pointers",
                        "code": "int* ptr = new int(10);\ndelete ptr;\nptr = nullptr;\n// ... later in the code ...\nif (ptr) {\n    delete ptr; // Safe, delete nullptr does nothing.\n}",
                        "explanation": "Setting the pointer to nullptr immediately after deleting it prevents accidental use-after-free and double frees."
                    },
                    {
                        "type": "common_mistakes",
                        "title": "Common Lifetime Issues",
                        "mistakes": [
                            {
                                "title": "Returning local references",
                                "desc": "Returning a pointer or reference to a local variable that is destroyed when the function exits."
                            },
                            {
                                "title": "Shallow Copying",
                                "desc": "Two objects hold a pointer to the same memory, and both try to delete it in their destructors."
                            }
                        ]
                    },
                    {
                        "type": "mastery_challenge",
                        "title": "Identify the Bug",
                        "question": "What is the primary risk of using a dangling pointer?",
                        "options": [
                            "Memory Leak",
                            "Undefined Behavior (Crash or Data Corruption)",
                            "Compilation Error",
                            "Infinite Loop"
                        ],
                        "answer": 1,
                        "explanation": "Accessing freed memory is Undefined Behavior, which can result in silent data corruption or an immediate crash."
                    }
                ]
            },
            {
                "title": "Module 4: Symptoms vs Root Causes",
                "blocks": [
                    {
                        "type": "header",
                        "title": "Symptoms vs Root Causes",
                        "subtitle": "Debugging Methodology",
                        "metadata": {
                            "difficulty": "Advanced",
                            "time": "20m",
                            "concepts": [
                                "Debugging",
                                "Root Cause Analysis"
                            ]
                        }
                    },
                    {
                        "type": "story",
                        "title": "The Decoy Crash",
                        "content": "A stack trace points to a crash inside `std::string::length()`. You spend hours reading standard library code, assuming there's a bug in C++. But the standard library is fine\u2014the problem is your code."
                    },
                    {
                        "type": "real_world_analogy",
                        "title": "Treating the Disease, Not the Symptom",
                        "content": "If you have a fever, taking medicine to lower your temperature treats the symptom. But the root cause is the infection. In programming, a crash in a library function is just the symptom (fever). The root cause (infection) is usually a corrupted pointer or buffer overflow in your own code."
                    },
                    {
                        "type": "concept",
                        "title": "Backtracking from a Crash",
                        "content": "When a program crashes inside a reliable library function, the likely cause is that you passed it invalid data (like a null or dangling pointer, or an un-null-terminated char array). You must trace the variable's lifecycle backward to find where it was corrupted."
                    },
                    {
                        "type": "execution_trace",
                        "title": "Tracing the Corrupted Pointer",
                        "code": "1. printName(Person* p) calls p->name.length() -> CRASH\n2. Who called printName? -> displayUI(Person* user)\n3. Where did 'user' come from? -> session.getUser()\n4. Ah! session.getUser() returned a deleted object!",
                        "trace": [
                            "Symptom: std::string::length() crashes.",
                            "Investigation: Check the 'this' pointer of std::string.",
                            "Root Cause: The parent object (Person) had already been deleted."
                        ]
                    },
                    {
                        "type": "think_first",
                        "question": "If your program crashes on the line `user->update()`, what should be your first debugging step?",
                        "options": [
                            "Rewrite the update() function.",
                            "Assume the compiler is broken.",
                            "Check if 'user' is a null or dangling pointer before this line.",
                            "Add more memory to the system."
                        ],
                        "answer": 2,
                        "explanation": "The most common reason for a crash when calling a method on an object pointer is that the pointer itself is invalid."
                    }
                ]
            },
            {
                "title": "Module 5: RAII and Smart Pointers",
                "blocks": [
                    {
                        "type": "header",
                        "title": "RAII to the Rescue",
                        "subtitle": "Automating Memory Management",
                        "metadata": {
                            "difficulty": "Intermediate",
                            "time": "30m",
                            "concepts": [
                                "RAII",
                                "Smart Pointers"
                            ]
                        }
                    },
                    {
                        "type": "story",
                        "title": "The Ultimate Fix",
                        "content": "Instead of hunting down every missing `delete` and trying to remember to set pointers to `nullptr`, what if the compiler did it for you automatically? This is the power of RAII."
                    },
                    {
                        "type": "concept",
                        "title": "Resource Acquisition Is Initialization (RAII)",
                        "content": "RAII is a C++ idiom where resource management (memory, file handles, locks) is tied to object lifetime. You acquire the resource in the constructor and release it in the destructor. When the object goes out of scope, the destructor is automatically called, guaranteeing cleanup."
                    },
                    {
                        "type": "annotated_code",
                        "title": "Unique_ptr: RAII for Memory",
                        "code": "#include <memory>\nvoid process() {\n    std::unique_ptr<Data> data = std::make_unique<Data>();\n    data->read();\n    if (error) return; // No leak! Destructor is called automatically.\n    // No need to call delete\n}",
                        "annotations": [
                            {
                                "line": "std::unique_ptr<Data> data = std::make_unique<Data>();",
                                "text": "Allocates memory and wraps it in a smart pointer."
                            },
                            {
                                "line": "if (error) return;",
                                "text": "Even on early exit, `data` goes out of scope, its destructor runs, and memory is freed."
                            }
                        ]
                    },
                    {
                        "type": "comparison_table",
                        "title": "Raw Pointers vs Smart Pointers",
                        "headers": [
                            "Feature",
                            "Raw Pointer (T*)",
                            "std::unique_ptr<T>"
                        ],
                        "rows": [
                            [
                                "Automatic Cleanup",
                                "No (requires delete)",
                                "Yes"
                            ],
                            [
                                "Ownership Semantics",
                                "Unclear",
                                "Strict Single Ownership"
                            ],
                            [
                                "Overhead",
                                "None",
                                "None (Zero-cost abstraction)"
                            ]
                        ]
                    },
                    {
                        "type": "code_lab",
                        "title": "Refactor to Smart Pointers",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nstruct Request { void process() {} };\n\nvoid handleRequest() {\n    Request* req = new Request();\n    req->process();\n    delete req; // TODO: Replace raw new/delete with std::unique_ptr\n}\n\nint main() {\n    handleRequest();\n    std::cout << \"Refactor the code to use std::unique_ptr so that manual delete is not needed.\";\n    return 0;\n}\n",
                        "expected_output": "Refactor the code to use std::unique_ptr so that manual delete is not needed.",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nstruct Request { void process() {} };\n\nvoid handleRequest() {\n    auto req = std::make_unique<Request>();\n    req->process();\n}\n\nint main() {\n    handleRequest();\n    std::cout << \"Refactor the code to use std::unique_ptr so that manual delete is not needed.\";\n    return 0;\n}\n",
                        "hint": "Fill in the missing parts of the code.",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            }
        ]
    },
    "28": {
        "format": "episodic",
        "episodes": [
            {
                "title": "Module 1: The Architect's Blueprint",
                "blocks": [
                    {
                        "type": "header",
                        "title": "The Architect's Blueprint",
                        "subtitle": "System Design in C++",
                        "metadata": {
                            "difficulty": "Advanced",
                            "time": "25m",
                            "concepts": [
                                "Architecture",
                                "SOLID Principles"
                            ]
                        }
                    },
                    {
                        "type": "mermaid_diagram",
                        "title": "Architectural Overview",
                        "explanation": "Before we write code, study this structural model to understand the relationships we are building.",
                        "code": "flowchart TD\n    subgraph IoCContainer[\"Inversion of Control (IoC) Service Container\"]\n        REGISTRY[\"Service Registry & LifeCycle Scope\"]\n        LOG[\"LoggingService (Singleton)\"]\n        CONFIG[\"ConfigurationService\"]\n        NET[\"NetworkService\"]\n        REGISTRY --> LOG\n        REGISTRY --> CONFIG\n        REGISTRY --> NET\n    end\n    subgraph EventCore[\"Event-Driven Core Pipeline\"]\n        BUS[\"Central Event Message Bus\"]\n        APP[\"ApplicationController (Injected Dependencies)\"]\n    end\n    subgraph DomainModules[\"Autonomous Feature Subsystems\"]\n        WORLD[\"WorldSimulationModule\"]\n        COMBAT[\"CombatResolutionModule\"]\n        UI_MOD[\"InterfacePresenterModule\"]\n    end\n    IoCContainer -- \"Injects Services\" --> APP\n    APP --> BUS\n    BUS --- WORLD\n    BUS --- COMBAT\n    BUS --- UI_MOD"
                    },
                    {
                        "type": "story",
                        "title": "Scaling Up",
                        "content": "Writing a small script is easy. Building a massive, multi-threaded C++ engine that powers a trading system or a game requires architecture. You are tasked with integrating 50 different components into a single cohesive system without creating a tangled mess."
                    },
                    {
                        "type": "concept",
                        "title": "The Big Ball of Mud",
                        "content": "A system without architecture devolves into a 'Big Ball of Mud'. Everything depends on everything else. A change in the UI breaks the database. A change in networking breaks the physics engine. To prevent this, we need strict boundaries and decoupling."
                    },
                    {
                        "type": "mental_model",
                        "title": "Clean Architecture Layering",
                        "data": "[ External Interfaces (UI, DB, Network) ]\n                 |\n[ Application Layer (Use Cases)         ]\n                 |\n[ Domain Layer (Core Logic)             ]"
                    },
                    {
                        "type": "real_world_analogy",
                        "title": "Building a City",
                        "content": "You don't wire a house's electrical outlets directly into the city's power plant generator. You use substations, transformers, and standardized plugs. Software architecture does the same using interfaces and dependency injection."
                    },
                    {
                        "type": "think_first",
                        "question": "What is the primary benefit of the Dependency Inversion Principle?",
                        "options": [
                            "It makes code run faster.",
                            "It allows high-level modules to be independent of low-level implementation details.",
                            "It automatically manages memory.",
                            "It prevents compilation errors."
                        ],
                        "answer": 1,
                        "explanation": "Dependency Inversion ensures that high-level policies do not depend on low-level details. Both depend on abstractions, allowing you to swap out implementations easily."
                    }
                ]
            },
            {
                "title": "Module 2: Dependency Injection & IoC",
                "blocks": [
                    {
                        "type": "header",
                        "title": "Dependency Injection",
                        "subtitle": "Decoupling Components",
                        "metadata": {
                            "difficulty": "Advanced",
                            "time": "30m",
                            "concepts": [
                                "Dependency Injection",
                                "Inversion of Control"
                            ]
                        }
                    },
                    {
                        "type": "story",
                        "title": "The Hardcoded Database",
                        "content": "Your application connects to MySQL. Tomorrow, the boss wants it to connect to PostgreSQL. If you hardcoded `MySQLDatabase db;` everywhere, you're in for a long weekend. You need Dependency Injection."
                    },
                    {
                        "type": "concept",
                        "title": "Inversion of Control (IoC)",
                        "content": "Instead of a class creating its own dependencies, dependencies are passed (injected) into it from the outside. This shifts the control of object creation away from the class itself."
                    },
                    {
                        "type": "wrong_approach",
                        "title": "Tight Coupling",
                        "code": "class OrderProcessor {\n    MySQLDatabase db;\npublic:\n    void process() { db.save(); }\n};",
                        "explanation": "OrderProcessor is tightly coupled to MySQLDatabase. You cannot test it without a real MySQL server."
                    },
                    {
                        "type": "correct_approach",
                        "title": "Dependency Injection via Interfaces",
                        "code": "class IDatabase {\npublic:\n    virtual void save() = 0;\n    virtual ~IDatabase() = default;\n};\n\nclass OrderProcessor {\n    IDatabase& db;\npublic:\n    OrderProcessor(IDatabase& db) : db(db) {}\n    void process() { db.save(); }\n};",
                        "explanation": "OrderProcessor now depends on an interface (IDatabase). You can inject a MockDatabase for testing or a PostgreSQLDatabase for production."
                    },
                    {
                        "type": "comparison_table",
                        "title": "Types of Injection",
                        "headers": [
                            "Type",
                            "Pros",
                            "Cons"
                        ],
                        "rows": [
                            [
                                "Constructor Injection",
                                "Dependencies are always initialized. Object is fully valid upon creation.",
                                "Can lead to long parameter lists if dependencies are many."
                            ],
                            [
                                "Setter Injection",
                                "Allows changing dependencies at runtime.",
                                "Object might be left in an invalid state if setter is not called."
                            ]
                        ]
                    },
                    {
                        "type": "code_lab",
                        "title": "Implement Constructor Injection",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nstruct IEngine { virtual void start() = 0; virtual ~IEngine() = default; };\nstruct V8Engine : public IEngine { void start() override {} };\n\nclass Car {\n    V8Engine engine;\npublic:\n    void drive() { engine.start(); }\n};\n\nint main() {\n    std::cout << \"Refactor Car to take an IEngine interface via its constructor.\";\n    return 0;\n}\n",
                        "expected_output": "Refactor Car to take an IEngine interface via its constructor.",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nstruct IEngine { virtual void start() = 0; virtual ~IEngine() = default; };\nstruct V8Engine : public IEngine { void start() override {} };\n\nclass Car {\n    std::shared_ptr<IEngine> engine;\npublic:\n    explicit Car(std::shared_ptr<IEngine> eng) : engine(std::move(eng)) {}\n    void drive() { engine->start(); }\n};\n\nint main() {\n    Car car(std::make_shared<V8Engine>());\n    car.drive();\n    std::cout << \"Refactor Car to take an IEngine interface via its constructor.\";\n    return 0;\n}\n",
                        "hint": "Fill in the missing parts of the code.",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 3: Event-Driven Architecture",
                "blocks": [
                    {
                        "type": "header",
                        "title": "Event-Driven Architecture",
                        "subtitle": "The Observer Pattern at Scale",
                        "metadata": {
                            "difficulty": "Advanced",
                            "time": "35m",
                            "concepts": [
                                "Event Bus",
                                "Observer Pattern",
                                "Publish-Subscribe"
                            ]
                        }
                    },
                    {
                        "type": "story",
                        "title": "The Spaghetti Callback Mess",
                        "content": "When the user clicks 'Save', the UI needs to update, the Database needs to write, and the Logger needs to log. If the UI button holds pointers to all these systems, it becomes a god object. We need an Event Bus."
                    },
                    {
                        "type": "concept",
                        "title": "The Event Bus",
                        "content": "An Event Bus is a central hub where publishers emit events (e.g., 'PlayerDied') and subscribers listen for them. Neither publisher nor subscriber knows about each other. They only know about the Event Bus."
                    },
                    {
                        "type": "annotated_code",
                        "title": "A Simple Event Dispatcher",
                        "code": "class EventBus {\n    std::map<EventType, std::vector<std::function<void(Event*)>>> listeners;\npublic:\n    void subscribe(EventType type, std::function<void(Event*)> callback) {\n        listeners[type].push_back(callback);\n    }\n    void publish(Event* event) {\n        for(auto& cb : listeners[event->type]) {\n            cb(event);\n        }\n    }\n};",
                        "annotations": [
                            {
                                "line": "std::map<EventType, std::vector<std::function<void(Event*)>>> listeners;",
                                "text": "Maps an event type to a list of callback functions."
                            },
                            {
                                "line": "void publish(Event* event)",
                                "text": "When an event is published, all subscribed callbacks are invoked."
                            }
                        ]
                    },
                    {
                        "type": "common_mistakes",
                        "title": "Lingering Observers",
                        "mistakes": [
                            {
                                "title": "The Memory Leak in Disguise",
                                "desc": "If a subscriber is destroyed but fails to unsubscribe from the Event Bus, the Event Bus will call a dangling pointer when the event next fires, causing a crash."
                            }
                        ]
                    },
                    {
                        "type": "think_first",
                        "question": "In an Event Bus, what is the best way to prevent calling destroyed subscribers?",
                        "options": [
                            "Never destroy subscribers.",
                            "Use std::weak_ptr for callbacks and check validity before calling.",
                            "Clear the event bus every frame."
                        ],
                        "answer": 1,
                        "explanation": "Storing callbacks with std::weak_ptr allows the Event Bus to check if the subscriber still exists before invoking it, safely handling destroyed objects."
                    },
                    {
                        "type": "mastery_challenge",
                        "title": "Decoupling Check",
                        "question": "Does the Publisher in an Event Bus architecture need to know how many Subscribers are listening?",
                        "options": [
                            "Yes, to manage their memory.",
                            "No, it just broadcasts the event to the bus.",
                            "Yes, to allocate enough threads."
                        ],
                        "answer": 1,
                        "explanation": "The core strength of the Event Bus is total decoupling. The Publisher fires an event and doesn't care if 0 or 100 subscribers are listening."
                    }
                ]
            },
            {
                "title": "Module 4: Managing Global State",
                "blocks": [
                    {
                        "type": "header",
                        "title": "Managing Global State",
                        "subtitle": "Singletons vs Service Locators",
                        "metadata": {
                            "difficulty": "Intermediate",
                            "time": "20m",
                            "concepts": [
                                "Singleton Pattern",
                                "Global State",
                                "Service Locator"
                            ]
                        }
                    },
                    {
                        "type": "story",
                        "title": "The Singleton Addiction",
                        "content": "Everyone loves Singletons because they are easy to access from anywhere. But soon, your code is filled with `Database::getInstance()` and `Logger::getInstance()`. You've essentially created glorified global variables."
                    },
                    {
                        "type": "concept",
                        "title": "The Problem with Singletons",
                        "content": "Singletons introduce hidden dependencies. When looking at a class's constructor, you can't tell what it depends on because it grabs the Singleton globally. This makes unit testing extremely difficult, as the Singleton's state persists between tests."
                    },
                    {
                        "type": "wrong_approach",
                        "title": "Hidden Dependency",
                        "code": "class PaymentProcessor {\npublic:\n    void charge() {\n        Logger::getInstance().log(\"Charging...\");\n        Database::getInstance().update();\n    }\n};",
                        "explanation": "PaymentProcessor secretly depends on Logger and Database. Testing this without side effects is hard."
                    },
                    {
                        "type": "correct_approach",
                        "title": "Explicit Dependency",
                        "code": "class PaymentProcessor {\n    ILogger& logger;\n    IDatabase& db;\npublic:\n    PaymentProcessor(ILogger& l, IDatabase& d) : logger(l), db(d) {}\n    void charge() {\n        logger.log(\"Charging...\");\n        db.update();\n    }\n};",
                        "explanation": "Dependencies are explicit. You can easily inject mocks."
                    },
                    {
                        "type": "comparison_table",
                        "title": "Singleton vs Dependency Injection",
                        "headers": [
                            "Feature",
                            "Singleton",
                            "Dependency Injection"
                        ],
                        "rows": [
                            [
                                "Accessibility",
                                "Global (Anywhere)",
                                "Local (Passed in)"
                            ],
                            [
                                "Testability",
                                "Poor (Shared state across tests)",
                                "Excellent (Can inject mocks)"
                            ],
                            [
                                "Coupling",
                                "Tight",
                                "Loose"
                            ]
                        ]
                    },
                    {
                        "type": "think_first",
                        "question": "If you absolutely must have a single instance of a class, what is better than a Singleton?",
                        "options": [
                            "Global Variable",
                            "Create it once in main() and pass it down via Dependency Injection.",
                            "Static methods only class."
                        ],
                        "answer": 1,
                        "explanation": "Creating it once in main() and passing it enforces single ownership while preserving testability and clear dependency graphs."
                    }
                ]
            },
            {
                "title": "Module 5: The Grand Integration",
                "blocks": [
                    {
                        "type": "header",
                        "title": "The Grand Integration",
                        "subtitle": "Putting It All Together",
                        "metadata": {
                            "difficulty": "Master",
                            "time": "45m",
                            "concepts": [
                                "System Integration",
                                "Architecture Review"
                            ]
                        }
                    },
                    {
                        "type": "story",
                        "title": "Bringing the Engine to Life",
                        "content": "You have your RAII for memory safety, your Event Bus for decoupling, and Dependency Injection for testability. It's time to wire the final `main()` function that boots up the entire architecture."
                    },
                    {
                        "type": "concept",
                        "title": "The Composition Root",
                        "content": "The Composition Root is the centralized location in your application (usually near `main()`) where all modules are wired together. It is the only place in the application that should know how the entire dependency graph is constructed."
                    },
                    {
                        "type": "execution_trace",
                        "title": "Bootstrapping the Application",
                        "code": "int main() {\n    auto logger = std::make_shared<ConsoleLogger>();\n    auto db = std::make_shared<PostgresDB>();\n    EventBus eventBus;\n    \n    SystemMonitor monitor(logger, db, eventBus);\n    monitor.start();\n    return 0;\n}",
                        "trace": [
                            "1. Initialize base dependencies (Logger, DB).",
                            "2. Initialize Event Bus.",
                            "3. Inject dependencies into high-level modules (SystemMonitor).",
                            "4. Start the application loop."
                        ]
                    },
                    {
                        "type": "mental_model",
                        "title": "The Final Architecture",
                        "data": "       [ main() - Composition Root ]\n         /           |             \\\n[ Logger ]      [ Event Bus ]      [ Database ]\n         \\           |             /\n       [    System Components    ]"
                    },
                    {
                        "type": "code_lab",
                        "title": "Final Boss: Wire the System",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nstruct ILogger { virtual ~ILogger() = default; };\nstruct FileLogger : public ILogger {};\nstruct EventDispatcher {};\nstruct Server {\n    EventDispatcher& disp;\n    ILogger& log;\n    Server(EventDispatcher& d, ILogger& l) : disp(d), log(l) {}\n    void start() {}\n};\n\n// Wire FileLogger, EventDispatcher, Server using std::shared_ptr\nint main() {\n    // TODO: Wire everything up using std::shared_ptr and Dependency Injection\n    return 0;\n}\n",
                        "expected_output": "Create the logger, dispatcher, inject them into the server, and start the server.",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\nstruct ILogger { virtual ~ILogger() = default; };\nstruct FileLogger : public ILogger {};\nstruct EventDispatcher {};\nstruct Server {\n    EventDispatcher& disp;\n    ILogger& log;\n    Server(EventDispatcher& d, ILogger& l) : disp(d), log(l) {}\n    void start() {\n        std::cout << \"Create the logger, dispatcher, inject them into the server, and start the server.\";\n    }\n};\n\nint main() {\n    auto logger = std::make_shared<FileLogger>();\n    auto dispatcher = std::make_shared<EventDispatcher>();\n    Server server(*dispatcher, *logger);\n    server.start();\n    return 0;\n}\n",
                        "hint": "Read the comments carefully and fill in the missing C++ logic.",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            }
        ]
    },
    "0": {
        "format": "episodic",
        "episodes": [
            {
                "title": "Module 1: The Awakening",
                "blocks": [
                    {
                        "type": "story",
                        "title": "A Blinking Cursor",
                        "content": "You find yourself in front of a monolithic mainframe. The screen is black, save for a single blinking cursor awaiting your command. This is where it all begins."
                    },
                    {
                        "type": "mermaid_diagram",
                        "title": "Architectural Overview",
                        "explanation": "Before we write code, study this structural model to understand the relationships we are building.",
                        "code": "flowchart TD\n    subgraph BuildPhase[\"C++ Compilation Pipeline\"]\n        SRC[\"main.cpp Source Code\"] --> PRE[\"Preprocessor: Macro Expansion & Headers\"]\n        PRE --> COMP[\"Compiler: Syntax & AST Generation\"]\n        COMP --> ASM[\"Assembler: Machine Code (.o)\"]\n        ASM --> LINK[\"Linker: Links C++ Standard Library\"]\n        LINK --> BIN[\"Executable Binary (a.out)\"]\n    end\n    subgraph RuntimePhase[\"Program Execution\"]\n        BIN --> LOAD[\"OS Loader: Allocates Memory\"]\n        LOAD --> MAIN[\"main() Entry: Initializes Call Stack Frame\"]\n        MAIN --> STDOUT[\"Standard Output Stream (std::cout)\"]\n    end"
                    },
                    {
                        "type": "problem",
                        "content": "The machine needs to know it's alive. We must send a signal to the output console to wake the system."
                    },
                    {
                        "type": "concept",
                        "title": "The Skeleton of a C++ Program",
                        "explanation": "Every C++ program has a starting point, a designated function where execution begins, known as 'main'.",
                        "analogy": "Think of 'main' as the front door to a massive factory. No matter how big the factory is, everyone enters through the front door.",
                        "technical_explanation": "In C++, 'int main()' is the entry point. The '#include <iostream>' directive imports standard input/output streams, giving us access to 'std::cout' to print text."
                    },
                    {
                        "type": "mental_model",
                        "title": "The Compilation Pipeline",
                        "data": "[Source Code .cpp] --> (Compiler) --> [Object Code .o] --> (Linker) --> [Executable]"
                    },
                    {
                        "type": "annotated_code",
                        "title": "Hello, Terminal",
                        "code": "#include <iostream>\n\nint main() {\n    std::cout << \"System Online\" << std::endl;\n    return 0;\n}",
                        "annotations": [
                            {
                                "line": "#include <iostream>",
                                "text": "Includes the standard library for input and output."
                            },
                            {
                                "line": "int main() {",
                                "text": "The main function where program execution starts."
                            },
                            {
                                "line": "std::cout << \"System Online\" << std::endl;",
                                "text": "Prints the string to the console, followed by a newline."
                            },
                            {
                                "line": "return 0;",
                                "text": "Indicates the program executed successfully."
                            }
                        ]
                    },
                    {
                        "type": "think_first",
                        "question": "What happens if we forget the 'return 0;' in the main function of a modern C++ compiler?",
                        "options": [
                            "It will not compile.",
                            "It compiles and implicitly returns 0.",
                            "It crashes at runtime."
                        ],
                        "answer": 1,
                        "explanation": "Modern C++ standards (C++98 onwards) allow the main function to omit the return statement, implicitly returning 0."
                    },
                    {
                        "type": "code_lab",
                        "title": "First Contact",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\n\nint main() {\n    // TODO: Output \"Hello, World!\" to the console\n    \n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\n\nint main() {\n    std::cout << \"Hello, World!\" << std::endl;\n    return 0;\n}\n",
                        "hint": "Use std::cout and the insertion operator (<<).",
                        "expected_output": "Hello, World!\n",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 2: Memory Cells",
                "blocks": [
                    {
                        "type": "story",
                        "title": "Reserving Space",
                        "content": "The system is awake, but it has no memory. It cannot remember what you tell it. You must allocate sectors in its memory banks."
                    },
                    {
                        "type": "concept",
                        "title": "Variables and Data Types",
                        "explanation": "Variables are named storage locations in memory. In C++, you must declare the type of data a variable will hold before using it.",
                        "analogy": "Imagine a warehouse with different sized boxes. You can't fit a bicycle in a shoebox. Similarly, C++ needs to know the type (box size/shape) to store data efficiently.",
                        "technical_explanation": "Common types include 'int' (integers), 'double' (floating-point numbers), 'char' (single characters), and 'bool' (true/false). The compiler uses this information to allocate the correct amount of memory (e.g., 4 bytes for an int on most systems)."
                    },
                    {
                        "type": "execution_trace",
                        "title": "Variable Assignment Trace",
                        "code": "int age;\nage = 25;\nage = age + 1;",
                        "trace": [
                            "Line 1: Allocates memory for an integer named 'age'. Value is undefined (garbage).",
                            "Line 2: The value 25 is stored in the memory location associated with 'age'.",
                            "Line 3: Retrieves the value of 'age' (25), adds 1 (26), and stores it back in 'age'."
                        ]
                    },
                    {
                        "type": "mastery_challenge",
                        "question": "Which of the following variable declarations is invalid in C++?",
                        "options": [
                            "int _myVar = 10;",
                            "double 2ndValue = 5.5;",
                            "char letter = 'A';"
                        ],
                        "answer": 1,
                        "explanation": "Variable names cannot start with a number. They must start with a letter or an underscore."
                    },
                    {
                        "type": "code_lab",
                        "title": "Assigning Values",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\n\nint main() {\n    // TODO: Declare an integer variable named 'power_level' and assign it 9001.\n    \n    // TODO: Print the power_level.\n    \n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\n\nint main() {\n    int power_level = 9001;\n    std::cout << power_level << std::endl;\n    return 0;\n}\n",
                        "hint": "Remember to use the '=' operator for assignment.",
                        "expected_output": "9001\n",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 3: The Art of Calculation",
                "blocks": [
                    {
                        "type": "story",
                        "title": "Processing Power",
                        "content": "With memory allocated, the machine now needs to perform computations. It sits idle, waiting for mathematical instructions."
                    },
                    {
                        "type": "concept",
                        "title": "Operators",
                        "explanation": "C++ provides operators to perform arithmetic, logical, and relational operations on variables.",
                        "analogy": "Operators are the verbs in the language of mathematics. They dictate the action taking place between two nouns (variables or values).",
                        "technical_explanation": "Arithmetic operators (+, -, *, /, %) perform standard math. Note that integer division truncates the decimal part."
                    },
                    {
                        "type": "annotated_code",
                        "title": "Basic Arithmetic",
                        "code": "int a = 10;\nint b = 3;\nint sum = a + b;\nint mod = a % b;",
                        "annotations": [
                            {
                                "line": "int sum = a + b;",
                                "text": "Adds a and b. sum becomes 13."
                            },
                            {
                                "line": "int mod = a % b;",
                                "text": "Calculates the remainder of a divided by b. mod becomes 1."
                            }
                        ]
                    },
                    {
                        "type": "code_lab",
                        "title": "Calculating Trajectory",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\n\nint main() {\n    int velocity = 50;\n    int time = 5;\n    // TODO: Calculate distance (velocity * time) and store it in a variable called 'distance'\n    \n    \n    // TODO: Print the distance\n    \n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\n\nint main() {\n    int velocity = 50;\n    int time = 5;\n    int distance = velocity * time;\n    std::cout << distance << std::endl;\n    return 0;\n}\n",
                        "hint": "Use the '*' operator for multiplication.",
                        "expected_output": "250\n",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 4: Interactivity",
                "blocks": [
                    {
                        "type": "story",
                        "title": "A Two-Way Channel",
                        "content": "Until now, the machine only speaks. It is time for it to listen. You must open an input channel."
                    },
                    {
                        "type": "concept",
                        "title": "Standard Input",
                        "explanation": "Programs can read data from the user during execution using standard input.",
                        "analogy": "If std::cout is a megaphone, std::cin is a microphone.",
                        "technical_explanation": "std::cin is an instance of istream. The extraction operator (>>) takes data from the input stream and places it into a variable, automatically handling type conversion if possible."
                    },
                    {
                        "type": "execution_trace",
                        "title": "Reading Input",
                        "code": "int passcode;\nstd::cin >> passcode;",
                        "trace": [
                            "Line 1: Memory is allocated for 'passcode'.",
                            "Line 2: Program pauses, waiting for user input. The entered value is parsed as an integer and stored in 'passcode'."
                        ]
                    },
                    {
                        "type": "code_lab",
                        "title": "Listening to the Void",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\n\nint main() {\n    int user_input = 0;\n    // TODO: Read an integer from std::cin into user_input\n    \n    // TODO: Output the user_input multiplied by 2\n    \n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\n\nint main() {\n    int user_input = 0;\n    std::cin >> user_input;\n    std::cout << (user_input * 2) << std::endl;\n    return 0;\n}\n",
                        "stdin_input": "21",
                        "hint": "Use std::cin and the extraction operator (>>).",
                        "expected_output": "42",
                        "explanation": "**Why it works:** `std::cin >> user_input;` extracts the next integer token from standard input (`21` in our sandbox stdin), skipping leading whitespace, and stores it in `user_input`. Multiplying by `2` and printing via `std::cout` outputs `42`."
                    }
                ]
            }
        ]
    },
    "1": {
        "format": "episodic",
        "episodes": [
            {
                "title": "Module 1: Branching Paths",
                "blocks": [
                    {
                        "type": "story",
                        "title": "The Fork in the Road",
                        "content": "The system processes data linearly, but true intelligence requires decisions. You must implement logical forks."
                    },
                    {
                        "type": "mermaid_diagram",
                        "title": "Architectural Overview",
                        "explanation": "Before we write code, study this structural model to understand the relationships we are building.",
                        "code": "stateDiagram-v2\n    [*] --> EvaluateCondition: Incoming Request\n    EvaluateCondition --> HighPriorityPath: priority is High or Critical\n    EvaluateCondition --> SwitchBranch: priority is Normal or Low\n    state SwitchBranch {\n        [*] --> CheckCategory\n        CheckCategory --> NormalRoute: case NORMAL\n        CheckCategory --> LowPriorityRoute: case LOW\n        CheckCategory --> FallbackRoute: default\n    }\n    HighPriorityPath --> MergeScope: Immediate Dispatch\n    NormalRoute --> MergeScope: Standard Queue\n    LowPriorityRoute --> MergeScope: Batch Queue\n    FallbackRoute --> MergeScope: Error Logged\n    MergeScope --> [*]: Continue Execution"
                    },
                    {
                        "type": "problem",
                        "content": "How do we make the program execute different code based on specific conditions?"
                    },
                    {
                        "type": "concept",
                        "title": "If/Else Statements",
                        "explanation": "If/else statements allow your program to execute certain blocks of code only when a specified condition evaluates to true.",
                        "analogy": "Like a train switching tracks. If the signal is green, it goes straight; else, it turns.",
                        "technical_explanation": "The condition inside the if() statement must evaluate to a boolean (true or false). If true, the block immediately following it executes. Otherwise, the else block (if present) executes."
                    },
                    {
                        "type": "annotated_code",
                        "title": "Security Check",
                        "code": "int access_level = 3;\nif (access_level >= 5) {\n    std::cout << \"Access Granted\";\n} else {\n    std::cout << \"Access Denied\";\n}",
                        "annotations": [
                            {
                                "line": "if (access_level >= 5) {",
                                "text": "Evaluates if access_level is greater than or equal to 5. Here, 3 >= 5 is false."
                            },
                            {
                                "line": "} else {",
                                "text": "Since the condition was false, the code jumps to this else block."
                            }
                        ]
                    },
                    {
                        "type": "code_lab",
                        "title": "Access Control",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\n\nint main() {\n    int code = 42;\n    // TODO: If code is 42, print \"Authorized\", else print \"Denied\"\n    \n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\n\nint main() {\n    int code = 42;\n    if (code == 42) {\n        std::cout << \"Authorized\" << std::endl;\n    } else {\n        std::cout << \"Denied\" << std::endl;\n    }\n    return 0;\n}\n",
                        "hint": "Use the equality operator (==) for comparison.",
                        "expected_output": "Authorized\n",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 2: The Boolean Web",
                "blocks": [
                    {
                        "type": "story",
                        "title": "Complex Security",
                        "content": "A single condition is often not enough. Sometimes, multiple criteria must be met simultaneously."
                    },
                    {
                        "type": "concept",
                        "title": "Logical Operators",
                        "explanation": "Logical operators (AND, OR, NOT) allow you to combine multiple conditions into a single, more complex condition.",
                        "analogy": "To enter the vault, you need BOTH the key (Condition A) AND the passcode (Condition B).",
                        "technical_explanation": "In C++, '&&' is logical AND, '||' is logical OR, and '!' is logical NOT. These operate on boolean values."
                    },
                    {
                        "type": "mental_model",
                        "title": "Truth Tables",
                        "data": "A   B   A && B   A || B\nT   T     T        T\nT   F     F        T\nF   T     F        T\nF   F     F        F"
                    },
                    {
                        "type": "think_first",
                        "question": "What is the result of `!(true && false) || false`?",
                        "options": [
                            "true",
                            "false",
                            "Compilation Error"
                        ],
                        "answer": 0,
                        "explanation": "true && false is false. !false is true. true || false is true."
                    },
                    {
                        "type": "code_lab",
                        "title": "Dual Authentication",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\n\nint main() {\n    bool has_key = true;\n    bool knows_password = false;\n    // TODO: Print \"Enter\" if the user has_key AND knows_password. Otherwise print \"Block\".\n    \n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\n\nint main() {\n    bool has_key = true;\n    bool knows_password = false;\n    if (has_key && knows_password) {\n        std::cout << \"Enter\" << std::endl;\n    } else {\n        std::cout << \"Block\" << std::endl;\n    }\n    return 0;\n}\n",
                        "hint": "Use the logical AND operator (&&).",
                        "expected_output": "Block\n",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 3: The Switchboard",
                "blocks": [
                    {
                        "type": "story",
                        "title": "Routing Signals",
                        "content": "When dealing with many exact matching conditions, long chains of if/else statements become unwieldy. The system needs a switchboard."
                    },
                    {
                        "type": "concept",
                        "title": "Switch Statements",
                        "explanation": "A switch statement evaluates a single expression and matches it against several constant cases.",
                        "analogy": "Like an operator at an old telephone switchboard, connecting a call directly to the requested line based on a specific number.",
                        "technical_explanation": "Switch statements only work with integral types (int, char, enum). A 'break' statement is usually required at the end of each case to prevent 'fall-through' to the next case."
                    },
                    {
                        "type": "execution_trace",
                        "title": "Switch Fall-through",
                        "code": "int state = 1;\nswitch (state) {\n    case 1:\n        std::cout << \"One \";\n    case 2:\n        std::cout << \"Two \";\n        break;\n}",
                        "trace": [
                            "Line 1: state is set to 1.",
                            "Line 2: The switch evaluates 'state' (1).",
                            "Line 3: Matches case 1.",
                            "Line 4: Prints 'One '.",
                            "Line 5: No break statement! Execution falls through to case 2.",
                            "Line 6: Prints 'Two '.",
                            "Line 7: Hits break, exits the switch statement."
                        ]
                    },
                    {
                        "type": "code_lab",
                        "title": "Command Routing",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\n\nint main() {\n    char cmd = 'B';\n    // TODO: Write a switch statement for 'cmd'.\n    // Case 'A': print \"Attack\"\n    // Case 'B': print \"Block\"\n    // Default: print \"Idle\"\n    // Remember to break!\n    \n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\n\nint main() {\n    char cmd = 'B';\n    switch (cmd) {\n        case 'A':\n            std::cout << \"Attack\" << std::endl;\n            break;\n        case 'B':\n            std::cout << \"Block\" << std::endl;\n            break;\n        default:\n            std::cout << \"Idle\" << std::endl;\n            break;\n    }\n    return 0;\n}\n",
                        "hint": "Don't forget the 'break;' at the end of each case, and use single quotes for characters.",
                        "expected_output": "Block\n",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 4: Scope and Shadows",
                "blocks": [
                    {
                        "type": "story",
                        "title": "Hidden Sectors",
                        "content": "Not all memory is globally accessible. Some variables exist only fleetingly within specific logical blocks."
                    },
                    {
                        "type": "concept",
                        "title": "Variable Scope",
                        "explanation": "Scope determines the visibility and lifetime of a variable. In C++, variables declared inside curly braces {} exist only within those braces.",
                        "analogy": "A secret discussed in a soundproof room (a block). People outside the room don't know the secret.",
                        "technical_explanation": "Variables are pushed onto the call stack. When execution leaves a block scope, the variables defined within that block are popped off the stack and destroyed."
                    },
                    {
                        "type": "mastery_challenge",
                        "question": "What is variable shadowing?",
                        "options": [
                            "When a variable blocks light in rendering.",
                            "When a local variable has the same name as a variable in an outer scope, hiding the outer variable.",
                            "When a variable is moved to disk swap space."
                        ],
                        "answer": 1,
                        "explanation": "Shadowing occurs when a variable declared in an inner scope has the same name as a variable in an outer scope. The inner variable 'shadows' the outer one."
                    },
                    {
                        "type": "code_lab",
                        "title": "Escaping the Scope",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\n\nint main() {\n    int global_status = 0;\n    if (true) {\n        int global_status = 1; // Shadowing!\n    }\n    // TODO: Print global_status. What will it be?\n    \n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\n\nint main() {\n    int global_status = 0;\n    if (true) {\n        int global_status = 1;\n    }\n    std::cout << global_status << std::endl;\n    return 0;\n}\n",
                        "hint": "The inner variable is destroyed when the 'if' block ends.",
                        "expected_output": "0\n",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            }
        ]
    },
    "2": {
        "format": "episodic",
        "episodes": [
            {
                "title": "Module 1: The Conveyor Belt",
                "blocks": [
                    {
                        "type": "story",
                        "title": "Repetitive Tasks",
                        "content": "The system must process millions of records. Writing the same code thousands of times is madness. We need automation."
                    },
                    {
                        "type": "mermaid_diagram",
                        "title": "Architectural Overview",
                        "explanation": "Before we write code, study this structural model to understand the relationships we are building.",
                        "code": "stateDiagram-v2\n    [*] --> Init: Initialize Counter (int i = 0)\n    Init --> ConditionCheck: Evaluate Condition (i is less than N)\n    ConditionCheck --> Terminated: Condition is false\n    ConditionCheck --> LoopBody: Condition is true\n    state LoopBody {\n        [*] --> ExecuteStep\n        ExecuteStep --> CheckBreak: break condition triggered?\n        CheckBreak --> Abort: Yes\n        CheckBreak --> CheckContinue: No\n        CheckContinue --> SkipStep: continue triggered?\n        CheckContinue --> StepDone: No\n    }\n    Abort --> Terminated: Break Loop Immediately\n    SkipStep --> UpdateCounter: Jump to Step Increment\n    StepDone --> UpdateCounter: Finish Step\n    UpdateCounter --> ConditionCheck: Increment Counter (++i)\n    Terminated --> [*]: Resume Sequential Execution"
                    },
                    {
                        "type": "problem",
                        "content": "How do we repeatedly execute a block of code as long as a condition holds true?"
                    },
                    {
                        "type": "concept",
                        "title": "While Loops",
                        "explanation": "A 'while' loop continuously executes a block of code as long as its condition evaluates to true.",
                        "analogy": "Like a worker on an assembly line: while there are parts on the belt, keep assembling.",
                        "technical_explanation": "The condition is checked before every iteration. If the condition is false initially, the loop body never executes. Be careful to update variables involved in the condition to avoid infinite loops."
                    },
                    {
                        "type": "execution_trace",
                        "title": "While Loop Trace",
                        "code": "int count = 3;\nwhile (count > 0) {\n    count--;\n}",
                        "trace": [
                            "Line 1: count = 3",
                            "Line 2: Check (3 > 0) -> true",
                            "Line 3: count = 2",
                            "Line 2: Check (2 > 0) -> true",
                            "Line 3: count = 1",
                            "Line 2: Check (1 > 0) -> true",
                            "Line 3: count = 0",
                            "Line 2: Check (0 > 0) -> false. Loop ends."
                        ]
                    },
                    {
                        "type": "code_lab",
                        "title": "Countdown",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\n\nint main() {\n    int timer = 3;\n    // TODO: Write a while loop that prints 'timer' and decrements it, stopping when timer is 0.\n    \n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\n\nint main() {\n    int timer = 3;\n    while (timer > 0) {\n        std::cout << timer << std::endl;\n        timer--;\n    }\n    return 0;\n}\n",
                        "hint": "Use timer-- inside the loop body to avoid an infinite loop.",
                        "expected_output": "3\n2\n1\n",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 2: Structured Iteration",
                "blocks": [
                    {
                        "type": "story",
                        "title": "The Predictable Cycle",
                        "content": "Often, we know exactly how many times a task must be repeated. The system requires a more structured looping mechanism."
                    },
                    {
                        "type": "concept",
                        "title": "For Loops",
                        "explanation": "A 'for' loop provides a compact syntax for iteration, encapsulating initialization, condition checking, and updating in a single line.",
                        "analogy": "Setting a washing machine to a specific cycle: Initialize the timer, check if time is left, spin, and tick down the timer.",
                        "technical_explanation": "Syntax: 'for (initialization; condition; increment)'. Initialization happens once. Condition is checked before each iteration. Increment happens after each iteration."
                    },
                    {
                        "type": "annotated_code",
                        "title": "Counting to Ten",
                        "code": "for (int i = 1; i <= 10; ++i) {\n    std::cout << i;\n}",
                        "annotations": [
                            {
                                "line": "int i = 1;",
                                "text": "Initialization: creates a loop counter 'i' starting at 1."
                            },
                            {
                                "line": "i <= 10;",
                                "text": "Condition: the loop runs as long as 'i' is less than or equal to 10."
                            },
                            {
                                "line": "++i",
                                "text": "Increment: adds 1 to 'i' after every iteration."
                            }
                        ]
                    },
                    {
                        "type": "think_first",
                        "question": "In a 'for' loop `for (int i = 0; i < 5; i++)`, how many times does the increment expression `i++` execute?",
                        "options": [
                            "4",
                            "5",
                            "6"
                        ],
                        "answer": 1,
                        "explanation": "It executes at the end of every iteration. Since the loop iterates 5 times (i=0, 1, 2, 3, 4), the increment executes 5 times, leaving i=5 which fails the condition."
                    },
                    {
                        "type": "code_lab",
                        "title": "Batch Processing",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\n\nint main() {\n    // TODO: Write a for loop that prints the even numbers from 2 to 8 (inclusive).\n    \n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\n\nint main() {\n    for (int i = 2; i <= 8; i += 2) {\n        std::cout << i << std::endl;\n    }\n    return 0;\n}\n",
                        "hint": "You can increment by more than 1 using i += 2.",
                        "expected_output": "2\n4\n6\n8\n",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 3: Do-While Dynamics",
                "blocks": [
                    {
                        "type": "story",
                        "title": "Act First, Ask Later",
                        "content": "Sometimes the system needs to attempt an action at least once before checking if it should continue."
                    },
                    {
                        "type": "concept",
                        "title": "Do-While Loops",
                        "explanation": "A 'do-while' loop is similar to a 'while' loop, but it guarantees that the loop body will execute at least once.",
                        "analogy": "Tasting soup while cooking. You always taste it at least once before deciding if it needs more salt and another taste.",
                        "technical_explanation": "The condition is evaluated at the *end* of the loop iteration. Note the required semicolon after the while(condition) statement."
                    },
                    {
                        "type": "mental_model",
                        "title": "Do-While Flow",
                        "data": " START -> [ Execute Body ] -> [ Evaluate Condition ] --(true)--> [ Execute Body ]\n                                        |\n                                     (false)\n                                        |\n                                       END"
                    },
                    {
                        "type": "code_lab",
                        "title": "Mandatory Input",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\n\nint main() {\n    int input;\n    // TODO: Write a do-while loop that prompts for input and reads it, looping while input is not 0.\n    // Note: just simulate by assigning input = 0 directly for this test to pass immediately.\n    input = 0;\n    do {\n        // ...\n    } while(false); // Fix this loop\n    \n    std::cout << \"Done\" << std::endl;\n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\n\nint main() {\n    int input = 0;\n    do {\n        // Simulating input\n    } while (input != 0);\n    std::cout << \"Done\" << std::endl;\n    return 0;\n}\n",
                        "hint": "The loop body runs once. Check condition while (input != 0);",
                        "expected_output": "Done\n",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 4: Control Flow Disruptions",
                "blocks": [
                    {
                        "type": "story",
                        "title": "Emergency Overrides",
                        "content": "During bulk processing, critical errors or early successes might occur. The system must be able to halt the conveyor belt or skip defective parts immediately."
                    },
                    {
                        "type": "concept",
                        "title": "Break and Continue",
                        "explanation": "'break' entirely exits the innermost loop it resides in. 'continue' skips the rest of the current iteration and jumps to the next evaluation/increment.",
                        "analogy": "'Break' is pulling the emergency stop cord. 'Continue' is throwing away a defective part and grabbing the next one.",
                        "technical_explanation": "These keywords provide fine-grained control over loop execution. However, overusing them can make code harder to read (spaghetti code)."
                    },
                    {
                        "type": "mastery_challenge",
                        "question": "What happens if a 'break' statement is executed inside a nested loop (a loop inside a loop)?",
                        "options": [
                            "It exits all loops.",
                            "It exits only the inner loop containing the break.",
                            "It causes a compilation error."
                        ],
                        "answer": 1,
                        "explanation": "'break' only terminates the innermost enclosing loop or switch statement."
                    },
                    {
                        "type": "code_lab",
                        "title": "Filtering Data",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\n\nint main() {\n    for (int i = 1; i <= 5; ++i) {\n        // TODO: If i is 3, skip the rest of the loop body using 'continue'.\n        \n        std::cout << i << std::endl;\n    }\n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\n\nint main() {\n    for (int i = 1; i <= 5; ++i) {\n        if (i == 3) {\n            continue;\n        }\n        std::cout << i << std::endl;\n    }\n    return 0;\n}\n",
                        "hint": "Use an if statement to check if i is 3, then use 'continue;'.",
                        "expected_output": "1\n2\n4\n5\n",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            }
        ]
    },
    "3": {
        "format": "episodic",
        "episodes": [
            {
                "title": "Module 1: The Delegation Subroutines (Intro to Functions)",
                "blocks": [
                    {
                        "type": "story",
                        "title": "The Overwhelmed Core",
                        "content": "Your main processing core is getting overwhelmed. The code is getting too long and repetitive. It's time to delegate tasks to specialized subroutines to keep the system stable."
                    },
                    {
                        "type": "mermaid_diagram",
                        "title": "Architectural Overview",
                        "explanation": "Before we write code, study this structural model to understand the relationships we are building.",
                        "code": "flowchart TD\n    subgraph CallStack[\"Call Stack Execution Frame\"]\n        direction TB\n        M_FRAME[\"main() Stack Frame\nLocal State: int value = 42\nMemory Addr: 0x7FFE00\"]\n        F_FRAME[\"processData() Stack Frame\nParam: int reference (inputRef)\nLocal: double result = 84.0\nMemory Addr: 0x7FFDC0\"]\n    end\n    M_FRAME -- \"Calls processData(value)\" --> PUSH[\"Push Activation Record\"]\n    PUSH --> F_FRAME\n    F_FRAME -. \"Pass-by-Reference: References 0x7FFE00\" .-> M_FRAME\n    F_FRAME -- \"Calculates and returns double\" --> POP[\"Pop Activation Record\"]\n    POP -- \"Transfers return value\" --> M_FRAME"
                    },
                    {
                        "type": "problem",
                        "content": "How do we write a sequence of operations once and execute it multiple times from different parts of our program without copy-pasting code?"
                    },
                    {
                        "type": "concept",
                        "title": "Functions: The Building Blocks",
                        "explanation": "Functions are self-contained blocks of code designed to perform a single specific task.",
                        "analogy": "Think of a function as a specialized machine in an assembly line. You build the machine once, and then you can trigger it to run its specific task whenever needed.",
                        "technical_explanation": "In C++, a function consists of a return type, a unique name, an optional list of parameters enclosed in parentheses `()`, and a body enclosed in curly braces `{}`. To execute the function, you 'call' it by its name."
                    },
                    {
                        "type": "mental_model",
                        "title": "Function Structure",
                        "data": "  [Return Type] [Function Name] ( [Parameters] ) {\n      // Function Body (Instructions)\n  }\n\n  void initiateThrusters() {\n      std::cout << \"Thrusters On!\";\n  }"
                    },
                    {
                        "type": "annotated_code",
                        "title": "A Simple Function",
                        "code": "void displayStatus() {\n    std::cout << \"System Nominal\\n\";\n}",
                        "annotations": [
                            {
                                "line": "void displayStatus() {",
                                "text": "'void' means this function does not return any data. 'displayStatus' is the name."
                            },
                            {
                                "line": "    std::cout << \"System Nominal\\n\";",
                                "text": "This is the code that runs when the function is called."
                            }
                        ]
                    },
                    {
                        "type": "think_first",
                        "question": "What return type should you use for a function that only prints text to the screen and doesn't compute a value?",
                        "options": [
                            "int",
                            "void",
                            "string",
                            "null"
                        ],
                        "answer": 1,
                        "explanation": "The `void` return type is used when a function is executed for its side effects (like printing) and does not return any value back to the caller."
                    },
                    {
                        "type": "code_lab",
                        "title": "Create a Subroutine",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\n\n// TODO: Write a function named 'powerOn' that returns void.\n// Inside, print \"Powering on...\\n\"\n\nint main() {\n    // TODO: Call your powerOn function here\n    \n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\n\nvoid powerOn() {\n    std::cout << \"Powering on...\\n\";\n}\n\nint main() {\n    powerOn();\n    return 0;\n}\n",
                        "hint": "Define `void powerOn() { ... }` above `main`, then write `powerOn();` inside `main`.",
                        "expected_output": "Powering on...\n",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 2: Function Parameters (Passing Information)",
                "blocks": [
                    {
                        "type": "story",
                        "title": "Data for the Subroutines",
                        "content": "Our subroutines are running, but they are rigid. We need to be able to send them specific instructions and data when we call them so they can adapt to different situations."
                    },
                    {
                        "type": "concept",
                        "title": "Parameters and Arguments",
                        "explanation": "Parameters allow functions to accept input values. When you call the function, you provide the actual values, known as arguments.",
                        "analogy": "If a function is a coffee machine, parameters are the coin slots and button panels. Arguments are the actual coins you insert and the specific buttons you press to get a certain type of coffee.",
                        "technical_explanation": "Parameters are declared in the parentheses of the function definition, acting as local variables within the function body. Arguments are the values passed inside the parentheses when calling the function."
                    },
                    {
                        "type": "execution_trace",
                        "title": "Tracing Parameters",
                        "code": "void setSpeed(int speed) {\n    std::cout << \"Speed: \" << speed;\n}\n\nint main() {\n    setSpeed(100);\n}",
                        "trace": [
                            "main() starts execution",
                            "Call setSpeed(100)",
                            "Inside setSpeed, local variable 'speed' is initialized with 100",
                            "Print \"Speed: 100\"",
                            "setSpeed finishes, return to main"
                        ]
                    },
                    {
                        "type": "mastery_challenge",
                        "question": "What is the correct way to pass two integers to a function?",
                        "options": [
                            "void calc(int x y)",
                            "void calc(int x, int y)",
                            "void calc(int x, y)"
                        ],
                        "answer": 1,
                        "explanation": "You must specify the type for every parameter individually, separated by commas."
                    },
                    {
                        "type": "code_lab",
                        "title": "Parameterized Subroutine",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\n\n// TODO: Write a function named 'calibrate' that returns void.\n// It should take one integer parameter named 'sensorId'.\n// It should print \"Calibrating sensor \" followed by the ID and a newline.\n\nint main() {\n    // TODO: Call calibrate with the argument 42\n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\n\nvoid calibrate(int sensorId) {\n    std::cout << \"Calibrating sensor \" << sensorId << \"\\n\";\n}\n\nint main() {\n    calibrate(42);\n    return 0;\n}\n",
                        "hint": "Use `void calibrate(int sensorId)` and `std::cout << \"Calibrating sensor \" << sensorId << \"\\n\";`",
                        "expected_output": "Calibrating sensor 42\n",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 3: Return Values (Getting Results)",
                "blocks": [
                    {
                        "type": "story",
                        "title": "Extracting the Data",
                        "content": "The subroutines are processing data beautifully, but we have a new problem. We need them to calculate values and send those results back to the main core for further processing."
                    },
                    {
                        "type": "concept",
                        "title": "Returning Data",
                        "explanation": "Functions can compute values and send them back to the code that called them using the `return` keyword.",
                        "analogy": "Like a scout reporting back to the commander. The commander sends the scout out (function call), the scout gathers intel (processing), and hands a report back to the commander (return value).",
                        "technical_explanation": "The function's return type must match the type of the value being returned. Once a `return` statement is executed, the function immediately terminates and passes the value back."
                    },
                    {
                        "type": "annotated_code",
                        "title": "Returning a Value",
                        "code": "int add(int a, int b) {\n    return a + b;\n}\n\nint main() {\n    int sum = add(5, 3);\n}",
                        "annotations": [
                            {
                                "line": "int add(int a, int b) {",
                                "text": "The return type is 'int', meaning this function promises to return an integer."
                            },
                            {
                                "line": "    return a + b;",
                                "text": "Calculates the sum and immediately exits the function, handing the result back."
                            },
                            {
                                "line": "    int sum = add(5, 3);",
                                "text": "The result (8) is caught and stored in the 'sum' variable."
                            }
                        ]
                    },
                    {
                        "type": "code_lab",
                        "title": "Calculate and Return",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\n\n// TODO: Write a function named 'calculateShield' that returns an int.\n// It should take two int parameters: 'base' and 'bonus'.\n// It should return the sum of base and bonus.\n\nint main() {\n    // TODO: Call calculateShield with 50 and 20, store the result in an int variable 'total'.\n    // TODO: Print 'total' followed by a newline.\n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\n\nint calculateShield(int base, int bonus) {\n    return base + bonus;\n}\n\nint main() {\n    int total = calculateShield(50, 20);\n    std::cout << total << \"\\n\";\n    return 0;\n}\n",
                        "hint": "Function signature should be `int calculateShield(int base, int bonus)`. Use `return base + bonus;`.",
                        "expected_output": "70\n",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 4: Scope and Lifetime",
                "blocks": [
                    {
                        "type": "story",
                        "title": "The Visibility Rules",
                        "content": "We have a memory leak alert! Variables from different subroutines are getting mixed up in our heads. We need to strictly define the borders of where a variable exists and where it doesn't."
                    },
                    {
                        "type": "concept",
                        "title": "Variable Scope",
                        "explanation": "Scope determines where a variable can be accessed in the code. A variable is only visible within the block (denoted by `{}`) in which it is declared.",
                        "analogy": "Like different rooms in a building. If you leave a tool in the kitchen, you can't reach it while you're in the garage. Variables are confined to their specific 'rooms' (code blocks).",
                        "technical_explanation": "Variables declared inside a function are called 'local variables'. They are created when the function starts and destroyed when the function ends. They cannot be accessed from outside the function."
                    },
                    {
                        "type": "think_first",
                        "question": "What happens if you try to use a local variable outside of the function it was created in?",
                        "options": [
                            "It works fine, variables are global.",
                            "The compiler throws an error because the variable is out of scope.",
                            "It returns a random garbage value."
                        ],
                        "answer": 1,
                        "explanation": "The C++ compiler enforces scope strictly. Trying to access a variable outside its declared block results in a compilation error."
                    },
                    {
                        "type": "code_lab",
                        "title": "Fix the Scope Leak",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\n\nvoid compute() {\n    int temp = 42;\n}\n\nint main() {\n    compute();\n    // TODO: The line below causes a compile error because 'temp' is not in scope here.\n    // Fix the program so it compiles and prints \"Fixed!\\n\" instead of trying to print temp.\n    std::cout << temp << \"\\n\";\n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\n\nvoid compute() {\n    int temp = 42;\n}\n\nint main() {\n    compute();\n    std::cout << \"Fixed!\\n\";\n    return 0;\n}\n",
                        "hint": "Simply delete or comment out the `std::cout << temp` line, and print \"Fixed!\\n\" instead.",
                        "expected_output": "Fixed!\n",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            }
        ]
    },
    "4": {
        "format": "episodic",
        "episodes": [
            {
                "title": "Module 1: The Memory Grids (Intro to Arrays)",
                "blocks": [
                    {
                        "type": "story",
                        "title": "Organizing the Sensor Data",
                        "content": "Our ship has 50 different hull sensors. Creating 50 individual variables (`sensor1`, `sensor2`, ...) is unmanageable. We need a way to group this data into a single, organized grid."
                    },
                    {
                        "type": "mermaid_diagram",
                        "title": "Architectural Overview",
                        "explanation": "Before we write code, study this structural model to understand the relationships we are building.",
                        "code": "flowchart TD\n    subgraph StackMemory[\"Stack Segment (Fixed Size & Fast)\"]\n        ARR[\"Fixed Array: int buffer[4]\nContiguous Memory:\n[Addr 0x1000: 10] [Addr 0x1004: 20]\n[Addr 0x1008: 30] [Addr 0x100C: 40]\"]\n        VEC[\"std::vector Object\n- bufferPtr: 0x9000 (Heap Pointer)\n- size: 3\n- capacity: 4\"]\n        STR[\"struct PlayerData\n- int playerId: 101\n- float health: 95.5f\"]\n    end\n    subgraph HeapMemory[\"Heap Segment (Dynamic & Resizable)\"]\n        HEAP_BUF[\"Contiguous Heap Allocation (0x9000)\n[Slot 0: 100] [Slot 1: 200] [Slot 2: 300] [Spare Slot]\"]\n    end\n    VEC --> HEAP_BUF"
                    },
                    {
                        "type": "memory_layout",
                        "title": "Array Contiguous Memory",
                        "explanation": "An array places elements directly next to each other in memory, allowing instant mathematical access.",
                        "cells": [
                            {
                                "address": "0x1000",
                                "value": "15",
                                "label": "arr[0]"
                            },
                            {
                                "address": "0x1004",
                                "value": "42",
                                "label": "arr[1]"
                            },
                            {
                                "address": "0x1008",
                                "value": "99",
                                "label": "arr[2]"
                            },
                            {
                                "address": "0x100C",
                                "value": "7",
                                "label": "arr[3]"
                            }
                        ]
                    },
                    {
                        "type": "concept",
                        "title": "Arrays",
                        "explanation": "An array is a collection of elements of the exact same data type, stored sequentially in a contiguous block of memory.",
                        "analogy": "Like a row of numbered lockers in a hallway. They are all right next to each other, they all hold the same type of item, and you access them using their locker number (index).",
                        "technical_explanation": "In C++, raw arrays have a fixed size that must be known at compile time. Elements are accessed using a zero-based index (the first element is at index 0)."
                    },
                    {
                        "type": "mental_model",
                        "title": "Array Memory Layout",
                        "data": "int scores[4] = {85, 90, 78, 92};\n\nIndex:   [0]    [1]    [2]    [3]\nValue:  | 85 | | 90 | | 78 | | 92 |\nMemory: |1000| |1004| |1008| |1012|  (Assuming 4-byte ints)"
                    },
                    {
                        "type": "annotated_code",
                        "title": "Declaring and Accessing Arrays",
                        "code": "int main() {\n    int data[3] = {10, 20, 30};\n    data[1] = 99;\n    std::cout << data[0];\n}",
                        "annotations": [
                            {
                                "line": "    int data[3] = {10, 20, 30};",
                                "text": "Creates an array of 3 integers and initializes them."
                            },
                            {
                                "line": "    data[1] = 99;",
                                "text": "Accesses the SECOND element (index 1) and changes its value to 99."
                            },
                            {
                                "line": "    std::cout << data[0];",
                                "text": "Prints the FIRST element (index 0), which is 10."
                            }
                        ]
                    },
                    {
                        "type": "code_lab",
                        "title": "Initialize and Access",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\n\nint main() {\n    // TODO: Declare an array of 4 integers named 'codes'.\n    // Initialize it with the values 100, 200, 300, 400.\n    \n    // TODO: Print the third element (which is 300) followed by a newline.\n    \n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\n\nint main() {\n    int codes[4] = {100, 200, 300, 400};\n    std::cout << codes[2] << \"\\n\";\n    return 0;\n}\n",
                        "hint": "Remember that arrays are zero-indexed. The third element is at index 2.",
                        "expected_output": "300\n",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 2: Dynamic Grids (std::vector)",
                "blocks": [
                    {
                        "type": "story",
                        "title": "Expanding Capacity",
                        "content": "Raw arrays are fast, but they have a fatal flaw: their size is fixed. When we collect an unpredictable amount of debris data, the fixed array crashes the system. We need a grid that can grow dynamically."
                    },
                    {
                        "type": "concept",
                        "title": "std::vector",
                        "explanation": "A `std::vector` is a dynamic array provided by the C++ Standard Library. It can automatically resize itself when you add or remove elements.",
                        "analogy": "Like a train that can seamlessly add more cars to the end whenever new cargo arrives, without needing to rebuild the entire train.",
                        "technical_explanation": "You must `#include <vector>`. You create one using `std::vector<Type> name;`. You append elements to the end using the `.push_back(value)` method."
                    },
                    {
                        "type": "execution_trace",
                        "title": "Vector Growth",
                        "code": "#include <vector>\nint main() {\n    std::vector<int> v;\n    v.push_back(5);\n    v.push_back(10);\n}",
                        "trace": [
                            "Create empty vector 'v' of integers. Size is 0.",
                            "push_back(5): Vector allocates memory, adds 5. Size is 1.",
                            "push_back(10): Vector adds 10 to the end. Size is 2."
                        ]
                    },
                    {
                        "type": "code_lab",
                        "title": "Grow the Vector",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\n\nint main() {\n    // TODO: Create a std::vector of integers named 'logs'.\n    \n    // TODO: Use push_back to add the numbers 7 and 14 to the vector.\n    \n    // TODO: Print the first element of the vector followed by a newline.\n    \n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\n\nint main() {\n    std::vector<int> logs;\n    logs.push_back(7);\n    logs.push_back(14);\n    std::cout << logs[0] << \"\\n\";\n    return 0;\n}\n",
                        "hint": "Declare with `std::vector<int> logs;`. Add with `logs.push_back(7);`. Access elements just like raw arrays using `logs[0]`.",
                        "expected_output": "7\n",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 3: Grouping Data (struct basics)",
                "blocks": [
                    {
                        "type": "story",
                        "title": "Complex Entities",
                        "content": "Our target tracking system is failing. An enemy ship has an X coordinate, a Y coordinate, and a health value. Tracking these in three separate variables is chaotic. We need to fuse them into a single custom data type."
                    },
                    {
                        "type": "concept",
                        "title": "Structs",
                        "explanation": "A `struct` (structure) allows you to group multiple variables of different data types together under a single, unified name.",
                        "analogy": "Like a filing cabinet folder labeled 'Employee Profile'. Inside, you have their Name (string), ID (integer), and Salary (float). The struct is the folder that keeps them all together.",
                        "technical_explanation": "You define a struct layout outside of main. Then, you can create instances of that struct. You access the individual variables inside (called members) using the dot (`.`) operator."
                    },
                    {
                        "type": "annotated_code",
                        "title": "Defining and Using Structs",
                        "code": "struct Player {\n    int health;\n    float speed;\n};\n\nint main() {\n    Player p1;\n    p1.health = 100;\n}",
                        "annotations": [
                            {
                                "line": "struct Player {",
                                "text": "Defines a new blueprint for a type called 'Player'."
                            },
                            {
                                "line": "};",
                                "text": "CRITICAL: Struct definitions MUST end with a semicolon!"
                            },
                            {
                                "line": "    Player p1;",
                                "text": "Creates an actual instance of the Player struct named p1."
                            },
                            {
                                "line": "    p1.health = 100;",
                                "text": "Uses the dot operator to access and modify the health member of p1."
                            }
                        ]
                    },
                    {
                        "type": "code_lab",
                        "title": "Define a Struct",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\n\n// TODO: Define a struct called 'Target' with two members:\n// an int named 'id' and a bool named 'isHostile'.\n// Don't forget the semicolon at the end!\n\nint main() {\n    // TODO: Create an instance of Target named 't1'.\n    // TODO: Set t1's id to 99 and isHostile to true.\n    // TODO: Print the id followed by a newline.\n    \n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\n\nstruct Target {\n    int id;\n    bool isHostile;\n};\n\nint main() {\n    Target t1;\n    t1.id = 99;\n    t1.isHostile = true;\n    std::cout << t1.id << \"\\n\";\n    return 0;\n}\n",
                        "hint": "The definition looks like `struct Target { int id; bool isHostile; };`",
                        "expected_output": "99\n",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            },
            {
                "title": "Module 4: The Master Grid (Vectors of Structs)",
                "blocks": [
                    {
                        "type": "story",
                        "title": "The Fleet Tracker",
                        "content": "We have the dynamic grids (vectors) and we have complex entities (structs). It's time to combine them to track an entire fleet of enemy ships dynamically."
                    },
                    {
                        "type": "concept",
                        "title": "Vectors of Structs",
                        "explanation": "You can create a `std::vector` where every element in the vector is an instance of a specific `struct`.",
                        "analogy": "A train where every single car isn't just an empty box, but a fully equipped mobile command center with distinct control panels (the struct members).",
                        "technical_explanation": "Declare it like `std::vector<MyStruct> vec;`. You create an instance of the struct, fill out its members, and then `push_back` that instance into the vector."
                    },
                    {
                        "type": "mastery_challenge",
                        "question": "If you have `std::vector<Target> fleet;` and you add one Target to it, how do you access the `id` of that first target?",
                        "options": [
                            "fleet.id[0]",
                            "fleet[0].id",
                            "fleet->id(0)"
                        ],
                        "answer": 1,
                        "explanation": "First, you use `fleet[0]` to get the struct instance from the vector. Then, you use `.id` to access the specific member inside that struct."
                    },
                    {
                        "type": "code_lab",
                        "title": "The Ultimate Combination",
                        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\n\nstruct Point {\n    int x;\n    int y;\n};\n\nint main() {\n    // TODO: Create a std::vector of Point named 'path'.\n    \n    // TODO: Create a Point instance named 'p'. Set its x to 5 and y to 10.\n    // TODO: Add 'p' to the 'path' vector using push_back.\n    \n    // TODO: Print the x coordinate of the first point in the vector, followed by a newline.\n    \n    return 0;\n}\n",
                        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n#include <memory>\n#include <map>\n#include <cstring>\n\n\nstruct Point {\n    int x;\n    int y;\n};\n\nint main() {\n    std::vector<Point> path;\n    Point p;\n    p.x = 5;\n    p.y = 10;\n    path.push_back(p);\n    \n    std::cout << path[0].x << \"\\n\";\n    return 0;\n}\n",
                        "hint": "Create the vector: `std::vector<Point> path;`. Push back: `path.push_back(p);`. Access: `path[0].x`.",
                        "expected_output": "5\n",
                        "explanation": "**Why it works:** In C++, classes define blueprints for objects. By defining this structure (as seen in the solution), we encapsulate data and behavior. The `public:` access modifier ensures that our main function can interact with the object."
                    }
                ]
            }
        ]
    }
}