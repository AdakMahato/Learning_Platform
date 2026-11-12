# Master Catalog for DSA Story Lab (Complete A-Z LeetCode, Coding Ninjas & Theory Roadmap)

STORIES = [
    {
        "id": 0,
        "title": "The Exponential Meltdown: Complexity & Recursion Trees",
        "icon": "⏱️",
        "genre": "Performance Forensics",
        "difficulty": "Beginner",
        "hook": "A production trading router slowed from 4ms to 19 minutes after user volume merely doubled. Dissect Asymptotics, Amortized Analysis, Master Theorem, and O(log N) Binary Exponentiation.",
        "primary": "Complexity & Asymptotics",
        "topics": ["Big-O/Theta/Omega", "Master Theorem", "Amortized Analysis", "Cache Locality", "Binary Exponentiation", "LC-50"]
    },
    {
        "id": 1,
        "title": "Cipher Vault: Number Theory & Prime Sieves",
        "icon": "🔢",
        "genre": "Cryptographic Forensics",
        "difficulty": "Beginner",
        "hook": "Audit a legacy RSA key generator stalling on prime enumeration. Prove Euclid's GCD invariant, derive the O(N log log N) Sieve of Eratosthenes bound, and guard 32-bit overflow.",
        "primary": "Math & Number Theory",
        "topics": ["Euclidean GCD", "Sieve of Eratosthenes", "Modular Arithmetic", "Overflow Guards", "LC-204", "LC-7"]
    },
    {
        "id": 2,
        "title": "Telemetry Surge: Contiguous Arrays, Prefix Sums & Kadane",
        "icon": "📈",
        "genre": "Systems Telemetry",
        "difficulty": "Beginner → Intermediate",
        "hook": "Scan 10 million sensor deltas for peak burst anomalies in a single linear pass. Master Prefix Sums, Boyer-Moore Majority Vote, Dutch National Flag, and Kadane's Subarray invariant.",
        "primary": "Arrays & Prefix Sums",
        "topics": ["Kadane Algorithm", "Prefix Sum + HashMap", "Dutch National Flag", "Boyer-Moore", "LC-53", "LC-560"]
    },
    {
        "id": 3,
        "title": "The Contracting Corridor: Two Pointers & Sliding Window",
        "icon": "🪟",
        "genre": "Stream Processing",
        "difficulty": "Intermediate",
        "hook": "Eliminate nested O(N^2) packet inspection loops by exploiting monotonic pointer movement and shrinking windows across sequences and unique-character streams.",
        "primary": "Two Pointers & Sliding Window",
        "topics": ["Two Pointers", "Variable Window", "Monotonic Bounds", "Invariants", "LC-11", "LC-3"]
    },
    {
        "id": 4,
        "title": "Collision Storm: Hash Tables, Load Factors & O(1) Lookup",
        "icon": "🔑",
        "genre": "Database Internals",
        "difficulty": "Intermediate",
        "hook": "Investigate hash DoS latency spikes inside an in-memory cache. Contrast chaining vs probing, prove expected O(1) lookup, and solve Two Sum and Longest Consecutive Sequence in linear time.",
        "primary": "Hashing & Sets",
        "topics": ["Open Addressing", "Chaining", "Load Factor", "Two Sum Pattern", "Hash Sets", "LC-1", "LC-128"]
    },
    {
        "id": 5,
        "title": "The Unstable Ledger: Sorting Theory & Divide and Conquer",
        "icon": "⚖️",
        "genre": "Algorithmic Theory",
        "difficulty": "Intermediate",
        "hook": "Prove the Omega(N log N) decision-tree lower bound, preserve stability across multi-key financial records, merge overlapping SLA windows, and count array inversions via Merge Sort.",
        "primary": "Sorting & Intervals",
        "topics": ["Decision Tree Bound", "Stability", "Quicksort Pivot", "Merge Intervals", "Inversion Count", "LC-56"]
    },
    {
        "id": 6,
        "title": "The Monotonic Oracle: Binary Search & Answer Space",
        "icon": "🎯",
        "genre": "Search Optimization",
        "difficulty": "Intermediate",
        "hook": "Stop thinking Binary Search only works on sorted arrays. Locate targets in rotated logs and apply Binary Search on Answer over monotonic feasibility predicates.",
        "primary": "Binary Search Mastery",
        "topics": ["Loop Invariants", "Rotated Array", "Lower/Upper Bound", "BS on Answer", "LC-33", "LC-875"]
    },
    {
        "id": 7,
        "title": "Text Engine: String Pooling, Palindromes & KMP",
        "icon": "🧵",
        "genre": "Compiler & NLP",
        "difficulty": "Intermediate",
        "hook": "Eliminate quadratic string-building bugs, analyze Rabin-Karp rolling hash collisions, derive KMP failure links (LPS array), and group anagram signatures efficiently.",
        "primary": "Strings & Pattern Matching",
        "topics": ["Expand Around Center", "Rabin-Karp", "KMP LPS Array", "Signature Hashing", "LC-49", "LC-5"]
    },
    {
        "id": 8,
        "title": "Pointer Surgery: Linked Lists & Floyd's Cycle Proof",
        "icon": "🔗",
        "genre": "Memory & Pointers",
        "difficulty": "Intermediate",
        "hook": "Untangle corrupted heap node chains without sentinel crashes. Prove why Tortoise & Hare always meet inside cycles, reverse lists in-place, and merge sorted pointer chains.",
        "primary": "Linked Lists",
        "topics": ["Dummy Head", "In-Place Reversal", "Floyd Cycle Proof", "Fast-Slow Pointers", "LC-206", "LC-21"]
    },
    {
        "id": 9,
        "title": "The Decision Mirror: Recursion & Backtracking Trees",
        "icon": "🌿",
        "genre": "Combinatorial Search",
        "difficulty": "Intermediate → Advanced",
        "hook": "Visualize call-stack frames, prune redundant branches early, distinguish subsets vs combinations vs permutations, and conquer duplicate-skipping invariants.",
        "primary": "Recursion & Backtracking",
        "topics": ["Recursion Tree", "Choose/Unchoose", "Pruning", "Power Set", "Combination Sum", "LC-78", "LC-39"]
    },
    {
        "id": 10,
        "title": "The Monotonic Skyline: Stacks, Queues & Next Greater",
        "icon": "📚",
        "genre": "Compiler Parsing",
        "difficulty": "Intermediate",
        "hook": "Amortize every element to at most one push and one pop. Parse nested bracket grammars with stacks and compute next-warmer-day spans in O(N) using monotonic stacks.",
        "primary": "Stacks & Queues",
        "topics": ["Amortized Stack", "Delimiter Matching", "Monotonic Stack", "Ring Buffer", "LC-20", "LC-739"]
    },
    {
        "id": 11,
        "title": "Priority Dispatcher: Binary Heaps & Top-K Streams",
        "icon": "⛰️",
        "genre": "Real-Time Scheduling",
        "difficulty": "Intermediate",
        "hook": "Prove why Floyd's bottom-up heapify runs in O(N) rather than O(N log N). Maintain sliding Top-K heavy hitters and compute Kth largest elements in streaming telemetry.",
        "primary": "Heaps & Priority Queues",
        "topics": ["Binary Heap Math", "O(N) Heapify Proof", "Min-Heap Top-K", "Quickselect vs Heap", "LC-215", "LC-347"]
    },
    {
        "id": 12,
        "title": "The Myopic Trap: Greedy Choice & Exchange Proofs",
        "icon": "⚡",
        "genre": "Optimization Theory",
        "difficulty": "Intermediate → Advanced",
        "hook": "Learn when local greed succeeds—and prove with counterexamples when it fails catastrophically. Master reachability invariants and interval scheduling by earliest end time.",
        "primary": "Greedy Algorithms",
        "topics": ["Exchange Argument", "Greedy Counterexamples", "Jump Reachability", "Interval Scheduling", "LC-55", "LC-435"]
    },
    {
        "id": 13,
        "title": "Hierarchy Protocol: Binary Trees, DFS & BFS",
        "icon": "🌳",
        "genre": "Tree Architecture",
        "difficulty": "Intermediate → Advanced",
        "hook": "Master post-order height propagation, single-pass O(N) Diameter computation, BFS level grouping, and Lowest Common Ancestor (LCA) structural recursion.",
        "primary": "Binary Trees",
        "topics": ["Pre/In/Post DFS", "Level Order BFS", "Single-Pass Diameter", "LCA", "LC-102", "LC-543"]
    },
    {
        "id": 14,
        "title": "Balanced Order: Binary Search Trees & Rotation Invariants",
        "icon": "🧭",
        "genre": "Indexing Structures",
        "difficulty": "Intermediate → Advanced",
        "hook": "Catch subtle BST range violations that local child checks miss, traverse inorder for Kth smallest rank, and understand why AVL and Red-Black rotations prevent O(N) skew.",
        "primary": "BST & Balanced Trees",
        "topics": ["Range Bounds Invariant", "Inorder Sorted Property", "AVL Rotations", "Red-Black Rules", "LC-98", "LC-230"]
    },
    {
        "id": 15,
        "title": "Dependency Mesh: Graphs I, BFS/DFS & Topological Sort",
        "icon": "🕸️",
        "genre": "Distributed Orchestration",
        "difficulty": "Intermediate → Advanced",
        "hook": "Detect dependency deadlocks across microservice DAGs. Contrast undirected parent-checks with directed 3-color cycle detection, grid flood-fill, and Kahn's in-degree topological sort.",
        "primary": "Graphs & Topological Sort",
        "topics": ["Adjacency List", "Grid DFS/BFS", "3-Color Cycle Check", "Kahn TopoSort", "LC-200", "LC-207"]
    },
    {
        "id": 16,
        "title": "Shortest Conduit: Dijkstra, Bellman-Ford & Union-Find",
        "icon": "🗺️",
        "genre": "Network Routing",
        "difficulty": "Advanced",
        "hook": "Route packets at minimum latency across weighted topologies, uncover why negative weights break greedy Dijkstra, and fuse components in O(alpha(N)) via Disjoint Set Union.",
        "primary": "Shortest Paths & DSU",
        "topics": ["Dijkstra Greedy Invariant", "Bellman-Ford V-1", "Path Compression DSU", "Kruskal MST", "LC-743", "LC-684"]
    },
    {
        "id": 17,
        "title": "Subproblem Vault: Dynamic Programming 1D, Knapsack & 2D",
        "icon": "💎",
        "genre": "Optimization Engines",
        "difficulty": "Advanced",
        "hook": "Transform exponential recursion trees into polynomial DP state tables. Master state transition equations, memoization vs tabulation, 0/1 & Unbounded Knapsack, Coin Change, and LCS.",
        "primary": "Dynamic Programming",
        "topics": ["State Transition", "Memo vs Tabulation", "House Robber", "Unbounded Knapsack", "2D LCS", "LC-322", "LC-1143"]
    },
    {
        "id": 18,
        "title": "Prefix & Parity: Tries and Bit Manipulation Mastery",
        "icon": "🧬",
        "genre": "Autocomplete & Bitwise",
        "difficulty": "Intermediate → Advanced",
        "hook": "Engineer O(L) prefix autocomplete engines with Tries and eliminate memory overhead using bitwise XOR parity, Kernighan bit-counting, and bitmask subset enumeration.",
        "primary": "Tries & Bit Manipulation",
        "topics": ["Prefix Trie Node", "XOR Algebraic Laws", "Brian Kernighan Trick", "Bitmasking", "LC-208", "LC-338"]
    }
]
