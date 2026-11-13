# Curriculum Data for Storylines 21, 22, and 23

NEW_STORIES = {
    21: {
        "title": "The C++ Under The OOP",
        "description": "Object Memory layout, vtable/vptr concept, Padding, Alignment, Object Slicing",
        "prerequisites": [20],
        "estimated_time": 240,
    },
    22: {
        "title": "The Debugger's Nightmare",
        "description": "Finding root causes for complex bugs: memory leaks, double frees, slicing, missing virtual destructors",
        "prerequisites": [21],
        "estimated_time": 240,
    },
    23: {
        "title": "The Final System",
        "description": "Capstone: The Nexus Platform - massive architecture combining everything, payment providers, logging, smart pointers",
        "prerequisites": [22],
        "estimated_time": 300,
    }
}

NEW_LEVELS = {
    21: [
        {
            "module_id": "21_01",
            "title": "The Illusion of Structure",
            "blocks": [
                {"type": "story", "content": "Your mentor points at a screen filled with hex codes. 'You think of objects as neat, isolated islands of data. The CPU just sees bytes.'"},
                {"type": "concept", "content": "Memory layout is the physical arrangement of an object's members in RAM. C++ guarantees that members of the same access control are allocated in the order they're declared."},
                {"type": "visual", "visual_type": "text", "content": "struct Simple { int a; int b; };\nLayout: [ a (4 bytes) ][ b (4 bytes) ]"},
                {"type": "micro_challenge", "content": "If an int is 4 bytes, what is the total size of struct Simple?"}
            ]
        },
        {
            "module_id": "21_02",
            "title": "The Gaps in Memory (Padding)",
            "blocks": [
                {"type": "story", "content": "You calculate the size of a struct with a char and an int to be 5 bytes. The compiler laughs at you and says 8."},
                {"type": "concept", "content": "Processors read memory in chunks (words). To optimize access, compilers insert 'padding' between members so they align perfectly on word boundaries."},
                {"type": "visual", "visual_type": "text", "content": "struct Padded { char c; int i; };\nLayout: [c (1 byte)][pad (3 bytes)][i (4 bytes)]"},
                {"type": "code_experiment", "starter_code": "#include <iostream>\nstruct Padded { char c; int i; };\nint main() { std::cout << sizeof(Padded); }", "expected_output": "8"}
            ]
        },
        {
            "module_id": "21_03",
            "title": "Minimizing the Waste",
            "blocks": [
                {"type": "story", "content": "A high-frequency trading application at Nexus is running out of cache memory. Your task: compact their data structures."},
                {"type": "concept", "content": "You can minimize padding by ordering struct members from largest to smallest. This groups smaller variables together, reducing the need for alignment gaps."},
                {"type": "worked_example", "content": "Before: char, double, int (size 24). After: double, int, char (size 16)."},
                {"type": "reflection", "content": "Why doesn't the compiler reorder members for you automatically?"}
            ]
        },
        {
            "module_id": "21_04",
            "title": "The Cost of Polymorphism (vptr)",
            "blocks": [
                {"type": "story", "content": "You add a single 'virtual' keyword to a class method, and suddenly the object size jumps by 8 bytes. Where did they come from?"},
                {"type": "concept", "content": "When a class has virtual functions, the compiler silently adds a hidden pointer (vptr) to the object. This pointer points to the vtable."},
                {"type": "visual", "visual_type": "text", "content": "class Base { virtual void foo(); int data; };\nLayout: [vptr (8 bytes)][data (4 bytes)][pad (4 bytes)]"},
                {"type": "debugger", "scenario": "You have a class with no data members, but one virtual function. What is sizeof(this class) on a 64-bit system?", "options": ["0", "1", "4", "8"], "answer": "8", "explanation": "The class contains a hidden vptr (8 bytes on 64-bit)."}
            ]
        },
        {
            "module_id": "21_05",
            "title": "The Map to the Code (vtable)",
            "blocks": [
                {"type": "story", "content": "'How does it know which function to call at runtime?' you ask. The mentor draws a map: the vtable."},
                {"type": "concept", "content": "The vtable (virtual table) is a static array of function pointers created for each polymorphic class. The object's vptr points to its class's vtable."},
                {"type": "micro_challenge", "content": "Does every object have its own vtable, or do all objects of the same class share one vtable?"}
            ]
        },
        {
            "module_id": "21_06",
            "title": "Dynamic Dispatch in Action",
            "blocks": [
                {"type": "story", "content": "It's time to trace the exact steps the CPU takes when executing 'ptr->virtualFunc()'."},
                {"type": "concept", "content": "Dynamic dispatch: 1. Follow pointer to object. 2. Read vptr. 3. Follow vptr to vtable. 4. Look up function pointer at specific offset. 5. Call function."},
                {"type": "worked_example", "content": "Showing the assembly-level logic conceptually of dynamic dispatch compared to a static function call."}
            ]
        },
        {
            "module_id": "21_07",
            "title": "The Tragedy of Object Slicing",
            "blocks": [
                {"type": "story", "content": "A derived object was passed into a function, but it lost all its special abilities and data. It was sliced."},
                {"type": "concept", "content": "Object slicing occurs when a derived object is assigned to a base class variable by value. The compiler only copies the base part, discarding the derived members and resetting the vptr to the Base class."},
                {"type": "visual", "visual_type": "text", "content": "Derived d; Base b = d;\n[Base Part | Derived Part] -> [Base Part]"}
            ]
        },
        {
            "module_id": "21_08",
            "title": "Preventing the Slice",
            "blocks": [
                {"type": "story", "content": "You must fix the logging system where detailed errors are being sliced into generic ones."},
                {"type": "concept", "content": "To preserve polymorphism and prevent slicing, always pass objects by reference or pointer."},
                {"type": "code_experiment", "starter_code": "void logError(Base b);", "expected_output": "Fix by using: void logError(const Base& b);"}
            ]
        }
    ],
    22: [
        {
            "module_id": "22_01",
            "title": "The Silent Bleed (Memory Leaks)",
            "blocks": [
                {"type": "story", "content": "The Nexus servers crash exactly every 4 days. RAM usage climbs linearly. You have a leak."},
                {"type": "concept", "content": "A memory leak happens when memory is allocated on the heap (using new) but never freed (using delete). The pointer is lost, but the memory remains reserved."},
                {"type": "debugger", "scenario": "void f() { int* p = new int[100]; }", "options": ["Memory Leak", "Double Free", "Dangling Pointer"], "answer": "Memory Leak", "explanation": "p goes out of scope, but the memory it points to was never deleted."}
            ]
        },
        {
            "module_id": "22_02",
            "title": "The Fatal Omission (Virtual Destructors)",
            "blocks": [
                {"type": "story", "content": "You thought you deleted the object. But the logs show the derived class destructor never ran. Files remain open, locks remain held."},
                {"type": "concept", "content": "When you delete a derived object through a base class pointer, if the base class destructor isn't virtual, it performs static binding. Only the base destructor runs."},
                {"type": "problem", "content": "Identify the missing virtual keyword in the Base destructor."}
            ]
        },
        {
            "module_id": "22_03",
            "title": "Double Trouble (Double Free)",
            "blocks": [
                {"type": "story", "content": "The program immediately aborts with a terrifying 'glibc detected: double free or corruption' error. Two pointers, one soul."},
                {"type": "concept", "content": "A double free occurs when you attempt to delete the same memory address twice. This corrupts the heap allocator's internal structures."},
                {"type": "visual", "visual_type": "text", "content": "A* p1 = new A(); A* p2 = p1; delete p1; delete p2; // CRASH"}
            ]
        },
        {
            "module_id": "22_04",
            "title": "The Ghost in the Machine (Dangling Pointers)",
            "blocks": [
                {"type": "story", "content": "Data is mysteriously changing. Variables you haven't touched suddenly contain garbage. A ghost is writing to your memory."},
                {"type": "concept", "content": "A dangling pointer is a pointer that points to memory that has already been freed. If you write to it, you overwrite memory that might now belong to another object."},
                {"type": "micro_challenge", "content": "How can you prevent a dangling pointer immediately after calling delete?"}
            ]
        },
        {
            "module_id": "22_05",
            "title": "The Rule of Three Reborn",
            "blocks": [
                {"type": "story", "content": "An object is copied, and suddenly everything breaks when they go out of scope. The shallow copy strikes again."},
                {"type": "concept", "content": "If your class manages a resource (like raw pointers), you must implement the Rule of Three: Destructor, Copy Constructor, and Copy Assignment Operator, to ensure deep copies."},
                {"type": "worked_example", "content": "Implementing a deep copy constructor for a String class that holds a char*."}
            ]
        },
        {
            "module_id": "22_06",
            "title": "Slicing Bugs in Containers",
            "blocks": [
                {"type": "story", "content": "You stored polymorphic objects in a std::vector. Now they all behave like the base class. The polymorphic magic is gone."},
                {"type": "concept", "content": "std::vector<Base> stores values. Inserting a Derived object slices it. To store polymorphic objects, you must use std::vector<Base*> or std::vector<std::unique_ptr<Base>>."},
                {"type": "code_experiment", "starter_code": "std::vector<Base> v; v.push_back(Derived());", "expected_output": "Fix using unique_ptr"}
            ]
        },
        {
            "module_id": "22_07",
            "title": "Valgrind: The Oracle",
            "blocks": [
                {"type": "story", "content": "You are armed with a new tool. Valgrind. It sees all, knows all allocations."},
                {"type": "concept", "content": "Valgrind's memcheck tool tracks every memory allocation and deallocation. It can pinpoint the exact line where memory was leaked or double-freed."},
                {"type": "reflection", "content": "Why is it important to test with tools like Valgrind before releasing to production?"}
            ]
        },
        {
            "module_id": "22_08",
            "title": "The Debugging Ritual",
            "blocks": [
                {"type": "story", "content": "The ultimate test: a program with a leak, a double free, and a slicing bug. You must fix them all."},
                {"type": "problem", "content": "Analyze the flawed codebase and apply fixes for resource management, virtual destructors, and pointer handling."}
            ]
        }
    ],
    23: [
        {
            "module_id": "23_01",
            "title": "The Nexus Platform Initiative",
            "blocks": [
                {"type": "story", "content": "The CEO addresses the engineering team. 'The Nexus Platform will unify our services. Payment, Logging, and Data processing. It must be modular, scalable, and crash-proof.'"},
                {"type": "concept", "content": "Building a large system requires combining interfaces, dependency injection, and smart resource management."},
                {"type": "reflection", "content": "What architectural principles are most important when building a system that will grow over years?"}
            ]
        },
        {
            "module_id": "23_02",
            "title": "Designing the Interfaces",
            "blocks": [
                {"type": "story", "content": "We need to process payments through Stripe and PayPal. We must define the contract before we write the logic."},
                {"type": "concept", "content": "Interfaces (pure abstract classes) define what a component can do, decoupling the user of the interface from its implementation."},
                {"type": "visual", "visual_type": "text", "content": "class IPaymentProvider { virtual bool processPayment(float amount) = 0; virtual ~IPaymentProvider() = default; };"}
            ]
        },
        {
            "module_id": "23_03",
            "title": "Implementing the Payment Engines",
            "blocks": [
                {"type": "story", "content": "With the interface locked in, you set out to build the concrete implementations."},
                {"type": "concept", "content": "Concrete classes inherit from the interface and use the 'override' keyword to implement the pure virtual functions."},
                {"type": "code_experiment", "starter_code": "class StripeProvider : public IPaymentProvider { ... };", "expected_output": "StripeProvider implemented successfully"}
            ]
        },
        {
            "module_id": "23_04",
            "title": "The Logging Infrastructure",
            "blocks": [
                {"type": "story", "content": "Every transaction must be audited. We need a FileLogger and a ConsoleLogger."},
                {"type": "concept", "content": "Applying the same interface pattern to ILogger. This allows the system to easily switch logging destinations."},
                {"type": "problem", "content": "Create the ILogger interface and the FileLogger implementation."}
            ]
        },
        {
            "module_id": "23_05",
            "title": "Dependency Injection",
            "blocks": [
                {"type": "story", "content": "How does the TransactionManager know which logger or payment provider to use? It doesn't. We give it to them."},
                {"type": "concept", "content": "Dependency Injection passes the required interface implementations into a class (usually via the constructor) rather than the class creating them itself. This makes testing incredibly easy."},
                {"type": "visual", "visual_type": "text", "content": "TransactionManager(IPaymentProvider* provider, ILogger* logger);"}
            ]
        },
        {
            "module_id": "23_06",
            "title": "Modernizing with Smart Pointers",
            "blocks": [
                {"type": "story", "content": "The Lead Architect reviews your raw pointers. 'It is the 21st century. We do not manually manage memory here.'"},
                {"type": "concept", "content": "std::unique_ptr ensures exclusive ownership and automatic deletion. std::shared_ptr allows multiple owners. Use them to manage your interfaces."},
                {"type": "micro_challenge", "content": "Which smart pointer should a TransactionManager use to hold a Logger that might be shared across multiple managers?"}
            ]
        },
        {
            "module_id": "23_07",
            "title": "Putting the Pieces Together",
            "blocks": [
                {"type": "story", "content": "The modules are built. It's time to wire the Nexus Platform together in main()."},
                {"type": "concept", "content": "Using std::make_unique and std::make_shared to instantiate providers, injecting them into the TransactionManager, and processing a transaction."},
                {"type": "worked_example", "content": "Wiring up the full application and tracing the polymorphic calls."}
            ]
        },
        {
            "module_id": "23_08",
            "title": "The Final Release",
            "blocks": [
                {"type": "story", "content": "The system boots. Transactions flow seamlessly. Memory remains stable. The architecture holds. You are no longer just a coder; you are a C++ Architect."},
                {"type": "concept", "content": "Review of the entire OOP paradigm: Encapsulation hides state, Inheritance builds hierarchy, Polymorphism allows flexible behavior, and RAII/Smart Pointers ensure safety."},
                {"type": "reflection", "content": "What was the most challenging paradigm shift in learning OOP in C++?"}
            ]
        }
    ]
}
