# DSA Cases 00 to 03: Complexity/Math, Number Theory, Arrays/Kadane/PrefixSum, Two Pointers/Sliding Window

CASES_PART1 = {
    "0": {
        "title": "Case 00: Complexity Analysis, Asymptotics & Recursion Trees",
        "episodes": [
            {
                "title": "Module 1: Asymptotic Bounds, RAM Model & Master Theorem",
                "blocks": [
                    {
                        "type": "story",
                        "title": "The Latency Cliff at 2x Load",
                        "content": "At 10,000 daily orders, the order-matching engine answered in 4 ms. When Black Friday traffic tripled to 30,000 orders, P99 latency exploded to **14 seconds** and crashed downstream gateways.\n\n> [!WARNING]\n> Hardware scaling (faster CPUs) buys constant factors $c$, never asymptotic survival when your inner loop runs $\\Theta(N^2)$ or $\\Theta(2^N)$."
                    },
                    {
                        "type": "objective",
                        "content": "Master formal asymptotic notation ($O, \\Omega, \\Theta$), count primitive operations in the RAM model, distinguish worst/average/amortized bounds, and solve divide-and-conquer recurrences using the **Master Theorem** and **Recursion Trees**."
                    },
                    {
                        "type": "concept",
                        "title": "Formal Asymptotic Notation & Loop Summation",
                        "content": "Under the Random Access Machine (**RAM**) model, basic arithmetic, memory indexing, and comparisons cost $O(1)$:\n\n- **Upper Bound ($f(n) = O(g(n))$):** $\\exists c > 0, n_0$ such that $0 \\le f(n) \\le c \\cdot g(n)$ for all $n \\ge n_0$.\n- **Lower Bound ($f(n) = \\Omega(g(n))$):** $\\exists c > 0, n_0$ such that $0 \\le c \\cdot g(n) \\le f(n)$ for all $n \\ge n_0$.\n- **Tight Bound ($f(n) = \\Theta(g(n))$):** Both $O(g(n))$ and $\\Omega(g(n))$ hold simultaneously.\n\nNotice **Master Theorem** for $T(n) = aT(n/b) + f(n)$ where $a \\ge 1, b > 1$:\n1. If $f(n) = O(n^{\\log_b a - \\epsilon})$ (leaves dominate) $\\implies T(n) = \\Theta(n^{\\log_b a})$.\n2. If $f(n) = \\Theta(n^{\\log_b a} \\log^k n)$ (all levels equal) $\\implies T(n) = \\Theta(n^{\\log_b a} \\log^{k+1} n)$.\n3. If $f(n) = \\Omega(n^{\\log_b a + \\epsilon})$ and $a f(n/b) \\le c f(n)$ (root dominates) $\\implies T(n) = \\Theta(f(n))$." ,
                        "technical_explanation": "Common hidden trap: `for (int i = n; i > 0; i /= 2) for (int j = 0; j < i; j++)` looks nested like $O(N \\log N)$, yet sums strictly as a geometric series: $N + N/2 + N/4 + \\dots = 2N = \\Theta(N)$! Conversely, Python string concatenation inside a loop allocates a new string every iteration, turning linear code into $\\Theta(N^2)$."
                    },
                    {
                        "type": "visual",
                        "title": "Divide & Conquer Recursion Tree: T(n) = 2T(n/2) + n",
                        "code": "graph TD\n  R[\"Level 0: n work (1 node)\"] --> L1[\"Level 1: n/2 work\"]\n  R --> R1[\"Level 1: n/2 work\"]\n  L1 --> L2A[\"Level 2: n/4\"]\n  L1 --> L2B[\"Level 2: n/4\"]\n  R1 --> R2A[\"Level 2: n/4\"]\n  R1 --> R2B[\"Level 2: n/4\"]\n  SUM[\"All log2(n) levels sum to n each => Total Theta(n log n)\"]\n  L2A -.-> SUM\n  R2B -.-> SUM"
                    },
                    {
                        "type": "interactive",
                        "title": "Complexity Analysis Checkpoint",
                        "question": "Consider the recurrence $T(n) = 4T(n/2) + n^2$ (using the Master Theorem with $a=4, b=2, f(n)=n^2$). What is the tight asymptotic time complexity $\\Theta$?",
                        "options": [
                            "Theta(n^2)",
                            "Theta(n^2 log n)",
                            "Theta(n^3)",
                            "Theta(n log n)"
                        ],
                        "answer": 1,
                        "explanation": "Here $\\log_b a = \\log_2 4 = 2$, so the leaf cost baseline is $n^{\\log_2 4} = n^2$. Since $f(n) = n^2 = \\Theta(n^2 \\log^0 n)$, Case 2 of the Master Theorem applies: $T(n) = \\Theta(n^2 \\log n)$."
                    }
                ]
            },
            {
                "title": "Module 2: Amortized Analysis, Cache Locality & Pitfalls",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "Why std::vector::push_back / list.append Is O(1) Amortized",
                        "content": "When a dynamic array reaches capacity $C$ and doubles to $2C$, that single resize copies $C$ elements in $\\Theta(C)$ worst-case time. Yet across $N$ consecutive appends:\n\n- **Aggregate Cost:** $N + (1 + 2 + 4 + \\dots + 2^{\\lfloor \\log_2 N \\rfloor}) < N + 2N = 3N$\n- **Amortized Cost per Operation:** $\\frac{3N}{N} = 3 = O(1)$.\n\n**Accounting Method:** Charge each push **3 credits** ($1$ pays the insert, $2$ are saved on the new element to prepay both its own future copy and one older uncredited element during doubling).\n\n> [!TIP]\n> If you grow capacity by a **constant** $+100$ instead of multiplying by $2$, resizes occur $\\Theta(N/100)$ times totaling $\\Theta(N^2/200) \\implies O(N)$ amortized per push! Doubling ($\\times 2$) is mandatory for $O(1)$ amortized growth.",
                        "technical_explanation": "**CPU Cache Lines (64 bytes):** Sequential array iteration prefetches 16 integers per L1 cache line fetch (~1 ns), whereas pointer-chasing a heap Linked List hits main RAM (~80 ns per cache miss). In real benchmarks, $O(N \\log N)$ `std::sort` on contiguous memory beats theoretically linear pointer-heavy structures up to surprisingly large $N$."
                    },
                    {
                        "type": "comparison_table",
                        "title": "Maximum Constraint Size Guide (1-Second C++ / Python Rule)",
                        "headers": ["Input Size Constraint (N)", "Required Target Complexity", "Algorithmic Family Typically Needed"],
                        "rows": [
                            ["N <= 10 - 12", "O(N!) or O(2^N * N)", "Backtracking, Permutations, Bitmask TSP"],
                            ["N <= 20 - 25", "O(2^N * N)", "Bitmask DP, Meet-in-the-Middle (~2^12 each side)"],
                            ["N <= 400 - 1,000", "O(N^2) or O(N^3)", "2D DP, Floyd-Warshall, All-Pairs Comparison"],
                            ["N <= 10^5", "O(N log N) or O(N)", "Sorting, Binary Search, Heaps, Trees, Segment Tree"],
                            ["N <= 10^7", "O(N) or O(N log log N)", "Two Pointers, Kadane, Linear Sieve, Prefix Sums"],
                            ["N >= 10^9", "O(log N) or O(1)", "Binary Search, Binary Exponentiation, Closed-Form Math"]
                        ]
                    },
                    {
                        "type": "calculation_challenge",
                        "title": "Operations Budget Estimator",
                        "formula": "Maximum safe operations per second in C++ is roughly $10^8$. For a binary search algorithm of cost $\\lceil \\log_2 N \\rceil$ comparisons on $N = 10^9$ (take $\\log_2(10^3) \\approx 10$).",
                        "problem": "Approximately how many loop iterations does Binary Search execute in the worst case on $N = 1,000,000,000$ ($10^9$) elements? (Enter integer ceiling using $2^{10} \\approx 10^3$)",
                        "answer": "30",
                        "alternatives": ["30", "31"],
                        "step_by_step": "Because $10^9 = (10^3)^3 \\approx (2^{10})^3 = 2^{30}$ (precisely $2^{29} < 10^9 < 2^{30}$), $\\lceil \\log_2(10^9) \\rceil = 30$ comparisons cuts $10^9$ candidates down to $1$."
                    },
                    {
                        "type": "debugger",
                        "title": "Spot the Quadratic Bug in Harmonic Loops",
                        "scenario": "Analyze the code below:\n```cpp\nlong long total = 0;\nfor (int i = 1; i <= n; i *= 2) {\n    for (int j = 0; j < n; j++) {\n        total += j;\n    }\n}\n```\nAn engineer claims this takes $O(N)$ time because `i` doubles geometrically. What is the TRUE tight time complexity?",
                        "options": [
                            "O(N) because doubling makes the outer loop constant",
                            "O(N log N) because the inner loop executes full N work in each of the log2(N) outer iterations",
                            "O(N^2) because there are two nested loops",
                            "O(log^2 N)"
                        ],
                        "answer": 1,
                        "explanation": "Compare `j < i` (which sums $1+2+4+\\dots+N = \\Theta(N)$) versus `j < n` (which executes a FULL $N$ steps $\\log_2 N$ separate times, yielding $\\Theta(N \\log N)$!). Always check whether the inner bound depends on the outer loop variable."
                    }
                ]
            },
            {
                "title": "Module 3: Coding Lab I — Single-Pass Stock Profit (LC-121)",
                "blocks": [
                    {
                        "type": "dsa_problem",
                        "title": "Best Time to Buy and Sell Stock",
                        "platform_style": "LeetCode 121 • Coding Ninjas Beginner Favorite",
                        "difficulty": "Easy",
                        "pattern": "Prefix Minimum / Greedy Invariant",
                        "target_time": "O(N)",
                        "target_space": "O(1)",
                        "statement": "You are given an integer array `prices` where `prices[i]` is the price of a stock on day `i`.\n\nChoose **a single day** to buy one stock and a **different day in the future** to sell that stock. Return the **maximum profit** you can achieve from this transaction. If no profit is possible, return `0`.",
                        "examples": [
                            {"input": "prices = [7, 1, 5, 3, 6, 4]", "output": "5", "explanation": "Buy on day 1 (price = 1) and sell on day 4 (price = 6), profit = 6 - 1 = 5."},
                            {"input": "prices = [7, 6, 4, 3, 1]", "output": "0", "explanation": "Prices strictly decrease; no profitable future sell day exists."}
                        ],
                        "constraints": [
                            "$1 \\le \\text{prices.length} \\le 10^5$",
                            "$0 \\le \\text{prices}[i] \\le 10^4$"
                        ],
                        "approach_ladder": {
                            "brute": "Check every pair $(i, j)$ with $i < j$ and compute $\\max(\\text{prices}[j] - \\text{prices}[i])$. Takes $O(N^2)$ time — causes **Time Limit Exceeded** when $N = 10^5$ ($5 \\times 10^9$ operations).",
                            "better": "Precompute a `suffix_max[i]` array in $O(N)$ extra space from right to left, then take $\\max_i(\\text{suffix\\_max}[i] - \\text{prices}[i])$. Runs in $O(N)$ time and $O(N)$ space.",
                            "optimal": "Maintain two scalar variables while scanning left-to-right: `min_price = +inf` (best historical buy so far) and `max_profit = 0`. At each day `p`, candidate sell profit is `p - min_price`; update `max_profit` and `min_price = min(min_price, p)`. Achieves **$O(N)$ time, $O(1)$ space**."
                        },
                        "dry_run": "| Day | Price | `min_price` before | `p - min_price` | `max_profit` |\n|---|---|---|---|---|\n| 0 | 7 | +inf | - | 0 |\n| 1 | 1 | 7 | -6 | 0 |\n| 2 | 5 | 1 | **4** | **4** |\n| 3 | 3 | 1 | 2 | 4 |\n| 4 | 6 | 1 | **5** | **5** |\n| 5 | 4 | 1 | 3 | 5 |",
                        "edge_cases": [
                            {"title": "Single Element Array", "desc": "`[5]` cannot buy and sell on different days -> must return `0` (not negative infinity!)."},
                            {"title": "Strictly Decreasing Prices", "desc": "Initializing `max_profit = 0` ensures we return `0` rather than a negative loss."}
                        ],
                        "follow_ups": "**LC-122 Variation:** What if you can hold at most 1 share and buy/sell *unlimited* times? Sum every positive upward delta `max(0, prices[i] - prices[i-1])`!",
                        "hint": "If you decide to sell today, which single past day MUST you have bought on to maximize today's profit?",
                        "starter_py": "class Solution:\n    def maxProfit(self, prices: List[int]) -> int:\n        # TODO: Return max single-transaction profit in O(N) time, O(1) space\n        return 0\n",
                        "solution_py": "class Solution:\n    def maxProfit(self, prices: List[int]) -> int:\n        min_price = float('inf')\n        best = 0\n        for p in prices:\n            if p < min_price:\n                min_price = p\n            elif p - min_price > best:\n                best = p - min_price\n        return best\n",
                        "harness_py": "_dsa_run_tests([\n    ('Sample 1: Valley & Peak', '[7,1,5,3,6,4]', lambda: Solution().maxProfit([7,1,5,3,6,4]), 5),\n    ('Sample 2: Monotonic Drop', '[7,6,4,3,1]', lambda: Solution().maxProfit([7,6,4,3,1]), 0),\n    ('Edge: Single Day', '[42]', lambda: Solution().maxProfit([42]), 0),\n    ('Edge: Double Dip Recovery', '[7,2,8,1,9]', lambda: Solution().maxProfit([7,2,8,1,9]), 8),\n    ('Edge: Flat Prices', '[5,5,5,5]', lambda: Solution().maxProfit([5,5,5,5]), 0),\n    ('Stress: 10^4 Ramp', 'range(10000, 0, -1) + [10001]', lambda: Solution().maxProfit(list(range(10000, 0, -1)) + [10001]), 10000),\n], sample_only=__DSA_SAMPLE_ONLY__, n_samples=2)",
                        "starter_cpp": "class Solution {\npublic:\n    int maxProfit(vector<int>& prices) {\n        // TODO: O(N) time, O(1) space\n        return 0;\n    }\n};\n",
                        "solution_cpp": "class Solution {\npublic:\n    int maxProfit(vector<int>& prices) {\n        int min_price = INT_MAX;\n        int best = 0;\n        for (int p : prices) {\n            min_price = min(min_price, p);\n            best = max(best, p - min_price);\n        }\n        return best;\n    }\n};\n",
                        "harness_cpp": "int main() {\n    ostringstream _dbg; streambuf* _old = cout.rdbuf(_dbg.rdbuf());\n    vector<_DSACaseOut> _res;\n    struct T { string name, inp; vector<int> arr; int exp; };\n    vector<int> stress;\n    for (int i = 10000; i >= 1; --i) stress.push_back(i);\n    stress.push_back(10001);\n    vector<T> tests = {\n        {\"Sample 1: Valley & Peak\", \"[7,1,5,3,6,4]\", {7,1,5,3,6,4}, 5},\n        {\"Sample 2: Monotonic Drop\", \"[7,6,4,3,1]\", {7,6,4,3,1}, 0},\n        {\"Edge: Single Day\", \"[42]\", {42}, 0},\n        {\"Edge: Double Dip Recovery\", \"[7,2,8,1,9]\", {7,2,8,1,9}, 8},\n        {\"Edge: Flat Prices\", \"[5,5,5,5]\", {5,5,5,5}, 0},\n        {\"Stress: 10^4 Ramp\", \"10000..1 then 10001\", stress, 10000}\n    };\n    int lim = DSA_SAMPLE_ONLY ? 2 : (int)tests.size();\n    Solution sol;\n    for (int i = 0; i < lim; ++i) {\n        auto v = tests[i].arr;\n        auto t0 = chrono::steady_clock::now();\n        int act = sol.maxProfit(v);\n        double ms = chrono::duration<double, milli>(chrono::steady_clock::now() - t0).count();\n        _res.push_back({tests[i].name, tests[i].inp, _dsa_fmt(tests[i].exp), _dsa_fmt(act), \"\", act == tests[i].exp, ms});\n    }\n    cout.rdbuf(_old);\n    _dsa_emit_json(_res, _dbg.str());\n    return 0;\n}"
                    }
                ]
            },
            {
                "title": "Module 4: Coding Lab II — Binary Exponentiation Pow(x, n) (LC-50)",
                "blocks": [
                    {
                        "type": "dsa_problem",
                        "title": "Pow(x, n) — Fast Binary Exponentiation",
                        "platform_style": "LeetCode 50 • Coding Ninjas Exponentiation Track",
                        "difficulty": "Medium",
                        "pattern": "Binary Exponentiation / Divide & Conquer",
                        "target_time": "O(log |n|)",
                        "target_space": "O(1)",
                        "statement": "Implement `myPow(x, n)`, which calculates $x$ raised to the integer power $n$ ($x^n$).\n\nNotice `n` can be negative (e.g., $2^{-2} = 0.25$) and as extreme as $-2^{31} = -2147483648$!",
                        "examples": [
                            {"input": "x = 2.0, n = 10", "output": "1024.0", "explanation": "Split $2^{10} = (2^5)^2 = (2 \\cdot (2^2)^2)^2 = 1024.0$ in only 4 multiplications."},
                            {"input": "x = 2.0, n = -2", "output": "0.25", "explanation": "$2^{-2} = (1/2)^2 = 0.25$."}
                        ],
                        "constraints": [
                            "$-100.0 < x < 100.0$",
                            "$-2^{31} \\le n \\le 2^{31} - 1$",
                            "Either $x \\ne 0$ or $n \\ge 0$."
                        ],
                        "approach_ladder": {
                            "brute": "Loop `n` times multiplying by `x`. When $n = 2^{31}-1$, this executes $2.14 \\times 10^9$ steps and **Times Out (TLE)** immediately.",
                            "better": "Recursive Divide & Conquer: `half = pow(x, exp // 2); return half * half * (x if exp % 2 else 1)`. Runs in $O(\\log n)$ time and $O(\\log n)$ call stack.",
                            "optimal": "Iterative Binary Exponentiation scanning bits of `long exp = n`: if `exp < 0`, set `x = 1.0 / x` and `exp = -exp`. While `exp > 0`: if `exp & 1`, `ans *= x`; then `x *= x; exp >>= 1`. Achieves **$O(\\log |n|)$ time and $O(1)$ space**."
                        },
                        "dry_run": "Trace `x = 2, n = 10` (`10` in binary = `1010_2`):\n- `exp=10` (even): `x = 4, exp = 5, ans = 1`\n- `exp=5` (odd): `ans *= 4 => 4`, `x = 16, exp = 2`\n- `exp=2` (even): `x = 256, exp = 1, ans = 4`\n- `exp=1` (odd): `ans *= 256 => 1024`, `exp = 0` -> return `1024.0`.",
                        "edge_cases": [
                            {"title": "C++ Signed INT_MIN Overflow Trap!", "desc": "In C++, `-n` when `n == -2147483648` triggers signed integer overflow (**Undefined Behavior**) because $+2147483648 > \\text{INT\\_MAX}$ (`2147483647`). Cast `long long exp = n;` **before** negating `-exp`!"},
                            {"title": "Exponent Zero & Negative Exponents", "desc": "$x^0 = 1.0$ even when $x = -3.5$."}
                        ],
                        "follow_ups": "**Modular Exponentiation:** Compute $(a^b) \\bmod 10^9+7$ in cryptography & competitive programming using the exact same loop with `% MOD` after every multiplication.",
                        "hint": "Promote `n` to 64-bit `long long` in C++ before computing `-n`, and repeatedly square `x` while halving `exp`.",
                        "starter_py": "class Solution:\n    def myPow(self, x: float, n: int) -> float:\n        # TODO: Binary exponentiation in O(log |n|) time\n        return 0.0\n",
                        "solution_py": "class Solution:\n    def myPow(self, x: float, n: int) -> float:\n        exp = n\n        if exp < 0:\n            x = 1.0 / x\n            exp = -exp\n        ans = 1.0\n        while exp > 0:\n            if exp & 1:\n                ans *= x\n            x *= x\n            exp >>= 1\n        return ans\n",
                        "harness_py": "_dsa_run_tests([\n    ('Sample 1: Positive Even', 'x=2.0, n=10', lambda: Solution().myPow(2.0, 10), 1024.0, lambda a,e: abs(a-e)<1e-6),\n    ('Sample 2: Negative Exp', 'x=2.0, n=-2', lambda: Solution().myPow(2.0, -2), 0.25, lambda a,e: abs(a-e)<1e-6),\n    ('Edge: Zero Power', 'x=3.5, n=0', lambda: Solution().myPow(3.5, 0), 1.0, lambda a,e: abs(a-e)<1e-6),\n    ('Edge: Negative Base Odd', 'x=-2.0, n=3', lambda: Solution().myPow(-2.0, 3), -8.0, lambda a,e: abs(a-e)<1e-6),\n    ('Edge: INT_MIN Limit', 'x=1.0, n=-2147483648', lambda: Solution().myPow(1.0, -2147483648), 1.0, lambda a,e: abs(a-e)<1e-6),\n    ('Edge: Tiny Fraction Decay', 'x=2.0, n=-2147483648', lambda: Solution().myPow(2.0, -2147483648), 0.0, lambda a,e: abs(a-e)<1e-9),\n], sample_only=__DSA_SAMPLE_ONLY__, n_samples=2)",
                        "starter_cpp": "class Solution {\npublic:\n    double myPow(double x, int n) {\n        // TODO: Guard against INT_MIN (-2147483648) before negating!\n        return 0.0;\n    }\n};\n",
                        "solution_cpp": "class Solution {\npublic:\n    double myPow(double x, int n) {\n        long long exp = n;\n        if (exp < 0) {\n            x = 1.0 / x;\n            exp = -exp;\n        }\n        double ans = 1.0;\n        while (exp > 0) {\n            if (exp & 1LL) ans *= x;\n            x *= x;\n            exp >>= 1;\n        }\n        return ans;\n    }\n};\n",
                        "harness_cpp": "int main() {\n    ostringstream _dbg; streambuf* _old = cout.rdbuf(_dbg.rdbuf());\n    vector<_DSACaseOut> _res;\n    struct T { string name, inp; double x; int n; double exp; };\n    vector<T> tests = {\n        {\"Sample 1: Positive Even\", \"x=2.0, n=10\", 2.0, 10, 1024.0},\n        {\"Sample 2: Negative Exp\", \"x=2.0, n=-2\", 2.0, -2, 0.25},\n        {\"Edge: Zero Power\", \"x=3.5, n=0\", 3.5, 0, 1.0},\n        {\"Edge: Negative Base Odd\", \"x=-2.0, n=3\", -2.0, 3, -8.0},\n        {\"Edge: INT_MIN Unity\", \"x=1.0, n=-2147483648\", 1.0, INT_MIN, 1.0},\n        {\"Edge: INT_MIN Decay\", \"x=2.0, n=-2147483648\", 2.0, INT_MIN, 0.0}\n    };\n    int lim = DSA_SAMPLE_ONLY ? 2 : (int)tests.size();\n    Solution sol;\n    for (int i = 0; i < lim; ++i) {\n        auto t0 = chrono::steady_clock::now();\n        double act = sol.myPow(tests[i].x, tests[i].n);\n        double ms = chrono::duration<double, milli>(chrono::steady_clock::now() - t0).count();\n        bool ok = fabs(act - tests[i].exp) < 1e-6;\n        _res.push_back({tests[i].name, tests[i].inp, _dsa_fmt(tests[i].exp), _dsa_fmt(act), \"\", ok, ms});\n    }\n    cout.rdbuf(_old);\n    _dsa_emit_json(_res, _dbg.str());\n    return 0;\n}"
                    }
                ]
            }
        ]
    },
    "1": {
        "title": "Case 01: Cipher Vault — Number Theory & Prime Sieves",
        "episodes": [
            {
                "title": "Module 1: Euclidean GCD, Primes & Sieve of Eratosthenes Proof",
                "blocks": [
                    {
                        "type": "story",
                        "title": "The Stalled Key Generator",
                        "content": "Generating public-key parameters requires enumerating all primes up to $N = 10^6$. A naive loop calls `isPrime(k)` up to $\\sqrt{k}$ on each candidate, saturating CPU cores for minutes.\n\n> [!NOTE]\n> Sieving crosses out multiples rather than factorizing each number individually — trading $O(N)$ auxiliary bits for a dramatic speed collapse."
                    },
                    {
                        "type": "concept",
                        "title": "Harmonic Series & The O(N log log N) Sieve Derivation",
                        "content": "1. **Trial Division:** Checking $d \\in [2, \\lfloor\\sqrt{x}\\rfloor]$ works in $O(\\sqrt{x})$ because if $x = a \\cdot b$ is composite, $\\min(a, b) \\le \\sqrt{x}$. Running it for all $1 \\dots N$ takes $\\Theta(N\\sqrt{N})$.\n2. **Sieve of Eratosthenes:** Initialize `is_prime[2..n-1] = True`. For each prime $p \\le \\sqrt{n}$, mark multiples starting at **$p^2$** (`p*p, p*p+p, ...`) because any smaller multiple $k \\cdot p$ with $k < p$ was already crossed off by a prime divisor of $k$!\n3. **Time Complexity Proof (Mertens' Theorem):** Total inner steps across all primes $p \\le N$:\n$$\\sum_{p \\le N \\text{ prime}} \\frac{N}{p} = N \\sum_{p \\le N} \\frac{1}{p} = O(N \\log \\log N)$$\nSince $\\log_2(\\log_2(10^9)) \\approx 4.9$, the Sieve performs nearly linear $O(N)$ work!\n\n4. **Euclidean Algorithm Proof:** For $b > 0$, $\\gcd(a, b) = \\gcd(b, a \\bmod b)$ because $a = q b + r \\implies$ any common divisor of $(a, b)$ divides $a - qb = r$, and conversely. Since $a \\bmod b < b$ and drops by $> 50\\%$ every 2 steps (Lamé's Theorem / Fibonacci worst-case), runtime is strictly $O(\\log(\\min(a, b)))$.",
                        "technical_explanation": "**Integer Overflow Invariant:** Computing `lcm(a, b)` as `(a * b) / gcd(a, b)` overflows 32-bit or even 64-bit integers before dividing! Always write `(a / gcd(a, b)) * b`."
                    },
                    {
                        "type": "visual",
                        "title": "Sieve Marking Flow starting at p*p",
                        "code": "graph LR\n  P[\"Prime p <= sqrt(n)\"] --> C{\"is_prime[p] == true?\"}\n  C -->|No| SKIP[\"Already composite, skip!\"]\n  C -->|Yes| S[\"Start inner loop at m = p * p\"]\n  S --> M[\"Mark is_prime[m] = false; m += p\"]"
                    },
                    {
                        "type": "interactive",
                        "title": "Number Theory Proof Check",
                        "question": "In the Sieve of Eratosthenes, why can the inner loop for prime $p$ safely start at $p^2$ instead of $2p$?",
                        "options": [
                            "Even numbers are impossible to factor",
                            "Any multiple k * p with k < p already has a prime factor <= k < p, so it was already crossed out earlier",
                            "p^2 is always the largest multiple below N",
                            "Starting at 2p fails to mark composite squares"
                        ],
                        "answer": 1,
                        "explanation": "Every composite number $k \\cdot p$ with $2 \\le k < p$ has a prime factor $q \\le k < p$, so prime $q$'s sweep already marked $k \\cdot p$ composite."
                    }
                ]
            },
            {
                "title": "Module 2: Modular Arithmetic & Overflow Guards",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "Signed Overflow & Negative Modulo Differences (C++ vs Python)",
                        "content": "**Modular Rules:**\n- $(a + b) \\bmod m = ((a \\bmod m) + (b \\bmod m)) \\bmod m$\n- $(a - b) \\bmod m = ((a \\bmod m) - (b \\bmod m) + m) \\bmod m$\n- $(a \\cdot b) \\bmod m = ((a \\bmod m) \\cdot (b \\bmod m)) \\bmod m$\n\n**Critical C++ vs Python Pitfall:** In Python, `-123 % 10 == 7` (mathematical floor division, `div` rounds toward $-\\infty$). In C++/Java, `-123 % 10 == -3` (truncation toward zero!) — AND dividing `-123 / 10` gives `-12` rather than Python's `-13` (`-123 // 10 == -13`). Mixing negative modulo semantics causes notorious subtle bugs!",
                        "technical_explanation": "To reverse digits cleanly in **both** positive and negative directions without overflow: check `res > INT_MAX / 10 || (res == INT_MAX / 10 && pop > 7)` and `res < INT_MIN / 10 || (res == INT_MIN / 10 && pop < -8)` *before* executing `res * 10 + pop`, never resorting to a `long long` workaround when constrained strictly to 32-bit registers."
                    },
                    {
                        "type": "comparison_table",
                        "title": "Prime Counting & Factorization Cost Comparison",
                        "headers": ["Technique", "Time Complexity", "Space", "Best Use Case"],
                        "rows": [
                            ["Single Trial Division", "O(sqrt(N))", "O(1)", "Checking 1 large number up to 10^14"],
                            ["Sieve of Eratosthenes", "O(N log log N)", "O(N)", "All primes <= 10^7 at once"],
                            ["Segmented Sieve", "O((R-L) log log R)", "O(sqrt(R))", "Primes in range [L, R] where R <= 10^12"],
                            ["Smallest Prime Factor (SPF) Sieve", "O(N log log N) prep, O(log N) query", "O(N)", "Factorizing 10^5 queries under 10^7 cleanly"]
                        ]
                    },
                    {
                        "type": "calculation_challenge",
                        "title": "GCD Trace Counter",
                        "formula": "Apply Euclidean recursion $\\gcd(a, b) = \\gcd(b, a \\bmod b)$ starting from `(48, 18)`.",
                        "problem": "What is $\\gcd(48, 18)$?",
                        "answer": "6",
                        "alternatives": ["6"],
                        "step_by_step": "`gcd(48, 18) -> gcd(18, 48 % 18 = 12) -> gcd(12, 18 % 12 = 6) -> gcd(6, 12 % 6 = 0) -> return 6`."
                    },
                    {
                        "type": "fill_in_the_blank",
                        "title": "Modulo Negative Fix",
                        "question": "In C++, to guarantee `(a - b) % M` always falls in `[0, M - 1]` assuming `a, b` are already reduced mod `M`, evaluate `((a - b) % M + _____) % M`.\n\nAnswer: _____",
                        "answer": "M",
                        "alternatives": ["M", "m"],
                        "explanation": "Adding `M` lifts any negative remainder in `[-(M-1), -1]` cleanly into `[1, M-1]` before the final `% M`."
                    }
                ]
            },
            {
                "title": "Module 3: Coding Lab I — Count Primes (LC-204)",
                "blocks": [
                    {
                        "type": "dsa_problem",
                        "title": "Count Primes Strictly Less Than N",
                        "platform_style": "LeetCode 204 • Coding Ninjas Number Theory",
                        "difficulty": "Medium",
                        "pattern": "Sieve of Eratosthenes",
                        "target_time": "O(N log log N)",
                        "target_space": "O(N)",
                        "statement": "Given an integer `n`, return the number of prime numbers that are **strictly less than** `n`.",
                        "examples": [
                            {"input": "n = 10", "output": "4", "explanation": "Primes strictly less than 10 are 2, 3, 5, and 7 (count = 4)."},
                            {"input": "n = 2", "output": "0", "explanation": "Note: strictly less than 2 means 2 itself is NOT counted."}
                        ],
                        "constraints": [
                            "$0 \\le n \\le 5 \\times 10^6$"
                        ],
                        "approach_ladder": {
                            "brute": "Test `isPrime(k)` in $O(\\sqrt{k})$ for each $k \\in [2, n-1]$. Costs $\\Theta(n\\sqrt{n})$ and **TLEs** above $n = 10^5$.",
                            "better": "Cross out multiples starting from `2 * p` using a boolean array.",
                            "optimal": "Iterate `p` from `2` while `p * p < n`. If `is_prime[p]`, mark `p*p, p*p + p, ... < n` as `False`. Sum remaining `True` entries in `[2, n)` for **$O(N \\log \\log N)$** runtime."
                        },
                        "dry_run": "For `n = 10` (`indices 0..9`): initially `[F, F, T, T, T, T, T, T, T, T]`.\n- `p = 2` ($2^2=4 < 10$): mark `4, 6, 8 -> F`.\n- `p = 3` ($3^2=9 < 10$): mark `9 -> F`.\n- Next $p = 4$ has $4^2 = 16 \\ge 10$ -> stop loop! Surviving `True`: `2, 3, 5, 7` = **4**.",
                        "edge_cases": [
                            {"title": "Boundary n <= 2", "desc": "`n = 0`, `n = 1`, and `n = 2` all have 0 primes strictly less than `n`."}
                        ],
                        "follow_ups": "**Odd-Only Sieve Optimization:** Skip even integers entirely to halve memory usage and improve CPU L1/L2 cache hit ratio.",
                        "hint": "Stop the outer loop at `p * p < n` and start the inner crossing loop at `p * p`.",
                        "starter_py": "class Solution:\n    def countPrimes(self, n: int) -> int:\n        # TODO: Sieve of Eratosthenes strictly < n\n        return 0\n",
                        "solution_py": "class Solution:\n    def countPrimes(self, n: int) -> int:\n        if n <= 2:\n            return 0\n        is_prime = [True] * n\n        is_prime[0] = is_prime[1] = False\n        p = 2\n        while p * p < n:\n            if is_prime[p]:\n                is_prime[p * p : n : p] = [False] * ((n - 1 - p * p) // p + 1)\n            p += 1\n        return sum(is_prime)\n",
                        "harness_py": "_dsa_run_tests([\n    ('Sample 1: n=10', 'n=10', lambda: Solution().countPrimes(10), 4),\n    ('Sample 2: n=2 (strict <)', 'n=2', lambda: Solution().countPrimes(2), 0),\n    ('Edge: n=0', 'n=0', lambda: Solution().countPrimes(0), 0),\n    ('Edge: n=3', 'n=3', lambda: Solution().countPrimes(3), 1),\n    ('Edge: n=100', 'n=100', lambda: Solution().countPrimes(100), 25),\n    ('Large: n=10000', 'n=10000', lambda: Solution().countPrimes(10000), 1229),\n], sample_only=__DSA_SAMPLE_ONLY__, n_samples=2)",
                        "starter_cpp": "class Solution {\npublic:\n    int countPrimes(int n) {\n        // TODO: O(N log log N) Sieve strictly < n\n        return 0;\n    }\n};\n",
                        "solution_cpp": "class Solution {\npublic:\n    int countPrimes(int n) {\n        if (n <= 2) return 0;\n        vector<char> is_prime(n, 1);\n        is_prime[0] = is_prime[1] = 0;\n        for (int p = 2; (long long)p * p < n; ++p) {\n            if (is_prime[p]) {\n                for (int m = p * p; m < n; m += p) {\n                    is_prime[m] = 0;\n                }\n            }\n        }\n        int cnt = 0;\n        for (char v : is_prime) cnt += v;\n        return cnt;\n    }\n};\n",
                        "harness_cpp": "int main() {\n    ostringstream _dbg; streambuf* _old = cout.rdbuf(_dbg.rdbuf());\n    vector<_DSACaseOut> _res;\n    struct T { string name, inp; int n, exp; };\n    vector<T> tests = {\n        {\"Sample 1: n=10\", \"n=10\", 10, 4},\n        {\"Sample 2: n=2 (strict <)\", \"n=2\", 2, 0},\n        {\"Edge: n=0\", \"n=0\", 0, 0},\n        {\"Edge: n=3\", \"n=3\", 3, 1},\n        {\"Edge: n=100\", \"n=100\", 100, 25},\n        {\"Large: n=10000\", \"n=10000\", 10000, 1229}\n    };\n    int lim = DSA_SAMPLE_ONLY ? 2 : (int)tests.size();\n    Solution sol;\n    for (int i = 0; i < lim; ++i) {\n        auto t0 = chrono::steady_clock::now();\n        int act = sol.countPrimes(tests[i].n);\n        double ms = chrono::duration<double, milli>(chrono::steady_clock::now() - t0).count();\n        _res.push_back({tests[i].name, tests[i].inp, _dsa_fmt(tests[i].exp), _dsa_fmt(act), \"\", act == tests[i].exp, ms});\n    }\n    cout.rdbuf(_old);\n    _dsa_emit_json(_res, _dbg.str());\n    return 0;\n}"
                    }
                ]
            },
            {
                "title": "Module 4: Coding Lab II — Overflow-Safe Reverse Integer (LC-7)",
                "blocks": [
                    {
                        "type": "dsa_problem",
                        "title": "Reverse Integer with Strict 32-bit Overflow Guard",
                        "platform_style": "LeetCode 7 • Coding Ninjas Digit Extraction",
                        "difficulty": "Medium",
                        "pattern": "Modulo Digit Extraction / Overflow Invariant",
                        "target_time": "O(log10 |x|)",
                        "target_space": "O(1)",
                        "statement": "Given a signed 32-bit integer `x`, return `x` with its digits reversed.\n\nIf reversing `x` causes the value to go outside the signed 32-bit integer range **$[-2^{31}, 2^{31} - 1]$**, then **return `0`**. Avoid overflowing 32-bit signed limits.",
                        "examples": [
                            {"input": "x = -123", "output": "-321", "explanation": "Sign is preserved while reversing digits 1, 2, 3."},
                            {"input": "x = 1534236469", "output": "0", "explanation": "Reversed value 9646324351 exceeds 2^31 - 1 (2147483647), so return 0."}
                        ],
                        "constraints": [
                            "$-2^{31} \\le x \\le 2^{31} - 1$"
                        ],
                        "approach_ladder": {
                            "brute": "Convert integer to string, reverse string, parse integer and catch overflow. Allocates extra $O(\\log |x|)$ heap string space.",
                            "optimal": "Pop digits via `digit = x % 10` (`sign * (abs(x) % 10)` in Python cleanly avoids `-123 % 10 == 7`!) and build `rev`. Check `rev > INT_MAX // 10` (or `== INT_MAX // 10 and digit > 7`) **before** multiplying by 10. **$O(\\log_{10} |x|)$ time, $O(1)$ space**."
                        },
                        "dry_run": "`INT_MAX = 2147483647` (last digit `7`), `INT_MIN = -2147483648` (last digit `8`). Checking before `rev * 10 + pop` guarantees no signed 32-bit overflow occurs at any step.",
                        "edge_cases": [
                            {"title": "Python Arbitrary Precision vs 32-bit Spec", "desc": "Python integers do not overflow automatically, so you MUST explicitly check bounds `[-2**31, 2**31 - 1]` and return `0`!"},
                            {"title": "Trailing Zeros", "desc": "`120 -> 21` automatically drops leading zero during base-10 accumulation."}
                        ],
                        "follow_ups": "**LC-9 Palindrome Number:** Reversing only half the digits until `x <= reversedHalf` avoids overflow checks entirely!",
                        "hint": "In Python, work with `sign = -1 if x < 0 else 1` and `x = abs(x)` so `% 10` and `// 10` behave consistently with unsigned digits, then clamp to `[-2**31, 2**31 - 1]`.",
                        "starter_py": "class Solution:\n    def reverse(self, x: int) -> int:\n        # TODO: Reverse digits; return 0 if outside [-2**31, 2**31 - 1]\n        return 0\n",
                        "solution_py": "class Solution:\n    def reverse(self, x: int) -> int:\n        INT_MAX, INT_MIN = (1 << 31) - 1, -(1 << 31)\n        sign = -1 if x < 0 else 1\n        n = abs(x)\n        rev = 0\n        while n:\n            pop = n % 10\n            n //= 10\n            val = sign * (rev * 10 + pop)\n            if val > INT_MAX or val < INT_MIN:\n                return 0\n            rev = rev * 10 + pop\n        return sign * rev\n",
                        "harness_py": "_dsa_run_tests([\n    ('Sample 1: Negative', 'x=-123', lambda: Solution().reverse(-123), -321),\n    ('Sample 2: Positive Overflow', 'x=1534236469', lambda: Solution().reverse(1534236469), 0),\n    ('Edge: Trailing Zero', 'x=120', lambda: Solution().reverse(120), 21),\n    ('Edge: Zero', 'x=0', lambda: Solution().reverse(0), 0),\n    ('Edge: INT_MIN Overflow', 'x=-2147483648', lambda: Solution().reverse(-2147483648), 0),\n    ('Edge: Max Safe Reversible', 'x=1463847412', lambda: Solution().reverse(1463847412), 2147483641),\n], sample_only=__DSA_SAMPLE_ONLY__, n_samples=2)",
                        "starter_cpp": "class Solution {\npublic:\n    int reverse(int x) {\n        // TODO: Reverse digits safely without signed 32-bit overflow\n        return 0;\n    }\n};\n",
                        "solution_cpp": "class Solution {\npublic:\n    int reverse(int x) {\n        int rev = 0;\n        while (x != 0) {\n            int pop = x % 10;\n            x /= 10;\n            if (rev > INT_MAX / 10 || (rev == INT_MAX / 10 && pop > 7)) return 0;\n            if (rev < INT_MIN / 10 || (rev == INT_MIN / 10 && pop < -8)) return 0;\n            rev = rev * 10 + pop;\n        }\n        return rev;\n    }\n};\n",
                        "harness_cpp": "int main() {\n    ostringstream _dbg; streambuf* _old = cout.rdbuf(_dbg.rdbuf());\n    vector<_DSACaseOut> _res;\n    struct T { string name, inp; int x, exp; };\n    vector<T> tests = {\n        {\"Sample 1: Negative\", \"x=-123\", -123, -321},\n        {\"Sample 2: Positive Overflow\", \"x=1534236469\", 1534236469, 0},\n        {\"Edge: Trailing Zero\", \"x=120\", 120, 21},\n        {\"Edge: Zero\", \"x=0\", 0, 0},\n        {\"Edge: INT_MIN Overflow\", \"x=-2147483648\", INT_MIN, 0},\n        {\"Edge: Max Safe Reversible\", \"x=1463847412\", 1463847412, 2147483641}\n    };\n    int lim = DSA_SAMPLE_ONLY ? 2 : (int)tests.size();\n    Solution sol;\n    for (int i = 0; i < lim; ++i) {\n        auto t0 = chrono::steady_clock::now();\n        int act = sol.reverse(tests[i].x);\n        double ms = chrono::duration<double, milli>(chrono::steady_clock::now() - t0).count();\n        _res.push_back({tests[i].name, tests[i].inp, _dsa_fmt(tests[i].exp), _dsa_fmt(act), \"\", act == tests[i].exp, ms});\n    }\n    cout.rdbuf(_old);\n    _dsa_emit_json(_res, _dbg.str());\n    return 0;\n}"
                    }
                ]
            }
        ]
    },
    "2": {
        "title": "Case 02: Telemetry Surge — Arrays, Prefix Sums & Kadane's Invariant",
        "episodes": [
            {
                "title": "Module 1: Prefix Sums, Difference Arrays & Kadane's DP Proof",
                "blocks": [
                    {
                        "type": "story",
                        "title": "Anomaly in the Trading Feed",
                        "content": "You have $10^7$ tick deltas (positive and negative). A naive query loop scans subarrays $[L, R]$ repeatedly, and peak-burst detection scans every start/end pair.\n\n> [!TIP]\n> Three core array theorems eliminate quadratic scans forever: **Prefix Sums** (for static range sums & exact-K subarray counts), **Kadane's Local Reset** (for max sum), and **Boyer-Moore Voting** (for $>N/2$ majority in $O(1)$ space)."
                    },
                    {
                        "type": "concept",
                        "title": "Prefix Sum Algebra & Kadane's Optimal Substructure",
                        "content": "Let `pref[0] = 0` and `pref[i+1] = pref[i] + arr[i]`. Then ANY contiguous range sum equals a single subtraction:\n$$\\sum_{t=L}^{R} \\text{arr}[t] = \\text{pref}[R+1] - \\text{pref}[L]$$\n\n**Prefix Sum + HashMap Duality (`Subarray Sum == k`):**\nA subarray ending at index $R$ sums to $k$ iff there exists $L \\le R$ such that:\n$$\\text{pref}[R+1] - \\text{pref}[L] = k \\iff \\text{pref}[L] = \\text{pref}[R+1] - k$$\nBy storing frequencies in `count_map` (seeded with `{0: 1}` for empty prefix!), even arrays containing **negatives and zeros** are solved in $O(N)$ (note: pure Sliding Window **FAILS** when negatives exist!).\n\n**Kadane's Loop Invariant (`cur = max(x, cur + x)`):**\nLet $dp[i]$ be the maximum subarray sum *strictly ending* at index $i$. Either extend $dp[i-1] + a[i]$ or start fresh at $a[i]$ whenever $dp[i-1] < 0$ (since carrying a negative prefix only drags the sum down).",
                        "technical_explanation": "**Dutch National Flag (3-Way Partition):** Maintain three pointers `low = 0, mid = 0, high = n - 1` so invariant holds at every iteration: `[0..low-1]` are `0`, `[low..mid-1]` are `1`, `[mid..high]` unknown, `[high+1..n-1]` are `2`. Critically, when swapping `a[mid]` with `a[high]` (`a[mid] == 2`), do **NOT** increment `mid`, because the swapped-in element from `high` is uninspected!"
                    },
                    {
                        "type": "visual",
                        "title": "Subarray Sum Strategy Selection",
                        "code": "flowchart TD\n  Q{\"Array has negative numbers?\"}\n  Q -->|\"No (All >= 0)\"| SW[\"Use Two Pointers / Sliding Window: O(N) time, O(1) space\"]\n  Q -->|\"Yes (Mixed +/-)\"| PM[\"Use Prefix Sum + HashMap: O(N) time, O(N) space\"]\n  PM --> SEED[\"Seed freq[0] = 1 for prefix starting at index 0\"]"
                    },
                    {
                        "type": "interactive",
                        "title": "Why Sliding Window Breaks on Negatives",
                        "question": "Why can't a positive-shrinking Sliding Window solve 'Count Subarrays with Sum == K' when the array contains negative integers?",
                        "options": [
                            "Hash tables cannot hash negative keys",
                            "Shrinking the left pointer breaks monotonicity: removing a negative element INCREASES the window sum instead of decreasing it",
                            "Negative integers overflow Python ints",
                            "Prefix sums do not work on negative arrays"
                        ],
                        "answer": 1,
                        "explanation": "Sliding window correctness relies on a monotonic sum function as you shrink/expand. Negative entries violate monotonicity because adding an element can decrease the sum and removing one can increase it."
                    }
                ]
            },
            {
                "title": "Module 2: Boyer-Moore Voting & Difference Array Updates",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "Boyer-Moore Majority Vote ($O(N)$ Time, $O(1)$ Space)",
                        "content": "Given an element appearing **strictly more than** $\\lfloor N/2 \\rfloor$ times:\nIf you conceptually cancel out every pair of *distinct* elements, the true majority element still has at least one surviving uncancelled copy!\n\n- Maintain `cand = 0, votes = 0`.\n- When `votes == 0`, adopt `cand = x`.\n- If `x == cand`, `votes += 1`; else `votes -= 1`.\n\n**Note:** If a majority element is NOT guaranteed to exist, you **must** perform a second linear verification pass counting `cand` occurrences.",
                        "technical_explanation": "**Difference Array Trick (Range Batch Updates):** To add `+v` to range `[L, R]` across $Q$ queries in $O(1)$ per query: execute `diff[L] += v` and `diff[R+1] -= v`, then take a single prefix sum over `diff` at the end in $O(N)$ total instead of $O(Q \\cdot N)$!"
                    },
                    {
                        "type": "debugger",
                        "title": "All-Negative Kadane Bug",
                        "scenario": "A junior developer writes Kadane's algorithm like this:\n```cpp\nint cur = 0, best = 0;\nfor (int x : nums) {\n    cur = max(0, cur + x);\n    best = max(best, cur);\n}\nreturn best;\n```\nWhat happens on `nums = [-5, -2, -9]` when non-empty subarrays are required?",
                        "options": [
                            "It correctly returns -2",
                            "It returns 0 (the empty subarray) instead of -2, failing the non-empty requirement",
                            "It crashes with vector bounds error",
                            "It loops infinitely"
                        ],
                        "answer": 1,
                        "explanation": "Initializing `best = INT_MIN` and `cur = 0` with `cur += x; best = max(best, cur); if (cur < 0) cur = 0;` (or `cur = max(x, cur + x); best = max(best, cur);`) handles all-negative arrays accurately, returning `-2`."
                    },
                    {
                        "type": "calculation_challenge",
                        "title": "Prefix Sum Zero-Collision Math",
                        "formula": "In an array of $z$ consecutive zeros `[0, 0, ..., 0]`, there are $z+1$ positions with identical prefix sum $0$ (`pref[0]..pref[z]`). Every pair of positions forms a valid zero-sum subarray.",
                        "problem": "How many non-empty subarrays sum to `0` in `[0, 0, 0, 0]` (length 4)?",
                        "answer": "10",
                        "alternatives": ["10"],
                        "step_by_step": "Length 4 has $4 \\times 5 / 2 = 10$ pairs (or prefix counts matching `0` at steps `1 + 2 + 3 + 4 = 10`)."
                    }
                ]
            },
            {
                "title": "Module 3: Coding Lab I — Maximum Subarray / Kadane (LC-53)",
                "blocks": [
                    {
                        "type": "dsa_problem",
                        "title": "Maximum Subarray (Kadane's Algorithm)",
                        "platform_style": "LeetCode 53 • Coding Ninjas Arrays Track",
                        "difficulty": "Medium",
                        "pattern": "Kadane's Algorithm / 1D Dynamic Programming",
                        "target_time": "O(N)",
                        "target_space": "O(1)",
                        "statement": "Given an integer array `nums`, find the **contiguous non-empty subarray** (containing at least one number) which has the **largest sum**, and return its sum.",
                        "examples": [
                            {"input": "nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]", "output": "6", "explanation": "Subarray [4, -1, 2, 1] has the largest sum 6."},
                            {"input": "nums = [5, 4, -1, 7, 8]", "output": "23", "explanation": "The entire array sums to 23."}
                        ],
                        "constraints": [
                            "$1 \\le \\text{nums.length} \\le 10^5$",
                            "$-10^4 \\le \\text{nums}[i] \\le 10^4$"
                        ],
                        "approach_ladder": {
                            "brute": "Two nested loops computing prefix or running subarray sums across all $(i, j)$ pairs: $O(N^2)$ time -> **TLE**.",
                            "optimal": "Track `cur_sum = nums[0]` and `best = nums[0]`. For each `x` in `nums[1:]`: `cur_sum = max(x, cur_sum + x)` and `best = max(best, cur_sum)`. Runs in **$O(N)$ time, $O(1)$ space**."
                        },
                        "dry_run": "Trace `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`:\n- `4`: `cur = max(4, -2+4) = 4`, `best = 4`\n- `-1`: `cur = max(-1, 3) = 3`, `best = 4`\n- `2`: `cur = 5`, `best = 5`\n- `1`: `cur = 6`, `best = 6`.",
                        "edge_cases": [
                            {"title": "All Negative Elements", "desc": "`[-8, -3, -6, -2, -5, -4]` must return `-2`, NEVER `0`!"}
                        ],
                        "follow_ups": "**Print Subarray Indices:** Track `temp_start`, updating `ans_start = temp_start, ans_end = i` whenever `best` improves, and resetting `temp_start = i + 1` whenever `cur < 0`.",
                        "hint": "Initialize `cur = nums[0]` and `best = nums[0]` rather than `0` so all-negative inputs return the least negative single element.",
                        "starter_py": "class Solution:\n    def maxSubArray(self, nums: List[int]) -> int:\n        # TODO: Kadane's algorithm handling all-negative arrays\n        return 0\n",
                        "solution_py": "class Solution:\n    def maxSubArray(self, nums: List[int]) -> int:\n        cur = best = nums[0]\n        for x in nums[1:]:\n            cur = max(x, cur + x)\n            if cur > best:\n                best = cur\n        return best\n",
                        "harness_py": "_dsa_run_tests([\n    ('Sample 1: Mixed Signals', '[-2,1,-3,4,-1,2,1,-5,4]', lambda: Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]), 6),\n    ('Sample 2: Mostly Positive', '[5,4,-1,7,8]', lambda: Solution().maxSubArray([5,4,-1,7,8]), 23),\n    ('Edge: Single Element Negative', '[-7]', lambda: Solution().maxSubArray([-7]), -7),\n    ('Edge: All Negatives', '[-8,-3,-6,-2,-5,-4]', lambda: Solution().maxSubArray([-8,-3,-6,-2,-5,-4]), -2),\n    ('Edge: Zeros & Negatives', '[0,-3,0,-1]', lambda: Solution().maxSubArray([0,-3,0,-1]), 0),\n], sample_only=__DSA_SAMPLE_ONLY__, n_samples=2)",
                        "starter_cpp": "class Solution {\npublic:\n    int maxSubArray(vector<int>& nums) {\n        // TODO: O(N) time, O(1) space\n        return 0;\n    }\n};\n",
                        "solution_cpp": "class Solution {\npublic:\n    int maxSubArray(vector<int>& nums) {\n        int cur = nums[0], best = nums[0];\n        for (size_t i = 1; i < nums.size(); ++i) {\n            cur = max(nums[i], cur + nums[i]);\n            best = max(best, cur);\n        }\n        return best;\n    }\n};\n",
                        "harness_cpp": "int main() {\n    ostringstream _dbg; streambuf* _old = cout.rdbuf(_dbg.rdbuf());\n    vector<_DSACaseOut> _res;\n    struct T { string name, inp; vector<int> arr; int exp; };\n    vector<T> tests = {\n        {\"Sample 1: Mixed Signals\", \"[-2,1,-3,4,-1,2,1,-5,4]\", {-2,1,-3,4,-1,2,1,-5,4}, 6},\n        {\"Sample 2: Mostly Positive\", \"[5,4,-1,7,8]\", {5,4,-1,7,8}, 23},\n        {\"Edge: Single Negative\", \"[-7]\", {-7}, -7},\n        {\"Edge: All Negatives\", \"[-8,-3,-6,-2,-5,-4]\", {-8,-3,-6,-2,-5,-4}, -2},\n        {\"Edge: Zeros & Negatives\", \"[0,-3,0,-1]\", {0,-3,0,-1}, 0}\n    };\n    int lim = DSA_SAMPLE_ONLY ? 2 : (int)tests.size();\n    Solution sol;\n    for (int i = 0; i < lim; ++i) {\n        auto v = tests[i].arr;\n        auto t0 = chrono::steady_clock::now();\n        int act = sol.maxSubArray(v);\n        double ms = chrono::duration<double, milli>(chrono::steady_clock::now() - t0).count();\n        _res.push_back({tests[i].name, tests[i].inp, _dsa_fmt(tests[i].exp), _dsa_fmt(act), \"\", act == tests[i].exp, ms});\n    }\n    cout.rdbuf(_old);\n    _dsa_emit_json(_res, _dbg.str());\n    return 0;\n}"
                    }
                ]
            },
            {
                "title": "Module 4: Coding Lab II — Subarray Sum Equals K (LC-560)",
                "blocks": [
                    {
                        "type": "dsa_problem",
                        "title": "Subarray Sum Equals K",
                        "platform_style": "LeetCode 560 • Striver A2Z / Coding Ninjas Essential",
                        "difficulty": "Medium",
                        "pattern": "Prefix Sum + HashMap Frequency",
                        "target_time": "O(N)",
                        "target_space": "O(N)",
                        "statement": "Given an integer array `nums` (which **may contain negatives and zeros**) and an integer `k`, return the **total number of subarrays** whose sum equals `k`.",
                        "examples": [
                            {"input": "nums = [1, 1, 1], k = 2", "output": "2", "explanation": "Subarrays [0..1] and [1..2] both sum to 2."},
                            {"input": "nums = [1, -1, 0], k = 0", "output": "3", "explanation": "Valid subarrays: [1, -1], [0], and [1, -1, 0]."}
                        ],
                        "constraints": [
                            "$1 \\le \\text{nums.length} \\le 2 \\times 10^4$",
                            "$-1000 \\le \\text{nums}[i] \\le 1000$",
                            "$-10^7 \\le k \\le 10^7$"
                        ],
                        "approach_ladder": {
                            "brute": "Test every start-end pair $(i, j)$ in $O(N^2)$ with running sum.",
                            "optimal": "Maintain `prefix = 0` and frequency map `freq = {0: 1}`. At each `x`, set `prefix += x`, add `freq.get(prefix - k, 0)` to `ans`, then increment `freq[prefix] += 1`. Runs in **$O(N)$ expected time and $O(N)$ space**."
                        },
                        "dry_run": "Trace `nums = [1, -1, 0], k = 0` with `freq = {0: 1}`:\n- `x=1`: `pref=1`, lookup `1-0=1` (+0), `freq={0:1, 1:1}`\n- `x=-1`: `pref=0`, lookup `0-0=0` (**+1**), `freq={0:2, 1:1}`\n- `x=0`: `pref=0`, lookup `0-0=0` (**+2**), `freq={0:3, 1:1}` -> total = **3**.",
                        "edge_cases": [
                            {"title": "Lookup BEFORE Insert when k == 0", "desc": "Always add `freq[pref - k]` BEFORE calling `freq[pref] += 1`, otherwise when `k = 0` an empty prefix matches itself!"},
                            {"title": "Initial Seed `{0: 1}`", "desc": "Without seeding empty-prefix sum `0` once, any subarray starting at index `0` is missed."}
                        ],
                        "follow_ups": "**LC-523 / LC-974:** Replace `prefix - k` with `prefix % k` (adjusted to non-negative in C++ via `((s % k) + k) % k`) to count subarrays divisible by `k`!",
                        "hint": "Store `{prefix_sum: frequency}` seeded with `{0: 1}`. Query `freq[prefix - k]` BEFORE incrementing `freq[prefix]`.",
                        "starter_py": "class Solution:\n    def subarraySum(self, nums: List[int], k: int) -> int:\n        # TODO: Prefix Sum + HashMap\n        return 0\n",
                        "solution_py": "class Solution:\n    def subarraySum(self, nums: List[int], k: int) -> int:\n        freq = {0: 1}\n        pref = 0\n        ans = 0\n        for x in nums:\n            pref += x\n            ans += freq.get(pref - k, 0)\n            freq[pref] = freq.get(pref, 0) + 1\n        return ans\n",
                        "harness_py": "_dsa_run_tests([\n    ('Sample 1: All Ones', '[1,1,1], k=2', lambda: Solution().subarraySum([1,1,1], 2), 2),\n    ('Sample 2: Negatives & Zero', '[1,-1,0], k=0', lambda: Solution().subarraySum([1,-1,0], 0), 3),\n    ('Edge: Multiple Zero Prefixes', '[0,0,0], k=0', lambda: Solution().subarraySum([0,0,0], 0), 6),\n    ('Edge: Single Miss', '[1], k=0', lambda: Solution().subarraySum([1], 0), 0),\n    ('Edge: Negatives Cancel', '[-1,-1,1], k=0', lambda: Solution().subarraySum([-1,-1,1], 0), 1),\n], sample_only=__DSA_SAMPLE_ONLY__, n_samples=2)",
                        "starter_cpp": "class Solution {\npublic:\n    int subarraySum(vector<int>& nums, int k) {\n        // TODO: unordered_map prefix counts\n        return 0;\n    }\n};\n",
                        "solution_cpp": "class Solution {\npublic:\n    int subarraySum(vector<int>& nums, int k) {\n        unordered_map<int, int> freq;\n        freq[0] = 1;\n        int pref = 0, ans = 0;\n        for (int x : nums) {\n            pref += x;\n            auto it = freq.find(pref - k);\n            if (it != freq.end()) ans += it->second;\n            ++freq[pref];\n        }\n        return ans;\n    }\n};\n",
                        "harness_cpp": "int main() {\n    ostringstream _dbg; streambuf* _old = cout.rdbuf(_dbg.rdbuf());\n    vector<_DSACaseOut> _res;\n    struct T { string name, inp; vector<int> arr; int k, exp; };\n    vector<T> tests = {\n        {\"Sample 1: All Ones\", \"[1,1,1], k=2\", {1,1,1}, 2, 2},\n        {\"Sample 2: Negatives & Zero\", \"[1,-1,0], k=0\", {1,-1,0}, 0, 3},\n        {\"Edge: Multiple Zeros\", \"[0,0,0], k=0\", {0,0,0}, 0, 6},\n        {\"Edge: Single Miss\", \"[1], k=0\", {1}, 0, 0},\n        {\"Edge: Negatives Cancel\", \"[-1,-1,1], k=0\", {-1,-1,1}, 0, 1}\n    };\n    int lim = DSA_SAMPLE_ONLY ? 2 : (int)tests.size();\n    Solution sol;\n    for (int i = 0; i < lim; ++i) {\n        auto v = tests[i].arr;\n        auto t0 = chrono::steady_clock::now();\n        int act = sol.subarraySum(v, tests[i].k);\n        double ms = chrono::duration<double, milli>(chrono::steady_clock::now() - t0).count();\n        _res.push_back({tests[i].name, tests[i].inp, _dsa_fmt(tests[i].exp), _dsa_fmt(act), \"\", act == tests[i].exp, ms});\n    }\n    cout.rdbuf(_old);\n    _dsa_emit_json(_res, _dbg.str());\n    return 0;\n}"
                    }
                ]
            }
        ]
    },
    "3": {
        "title": "Case 03: The Contracting Corridor — Two Pointers & Sliding Window",
        "episodes": [
            {
                "title": "Module 1: Monotonic Two-Pointer & Window Shrinking Proofs",
                "blocks": [
                    {
                        "type": "story",
                        "title": "Eliminating Nested Loops Forever",
                        "content": "How can scanning a string with **two** indices (`left` and `right`) still run strictly in $O(N)$ instead of $O(N^2)$?\n\n> [!IMPORTANT]\n> Amortized linear runtime holds whenever BOTH pointers only move forward: `right` steps $N$ times total, and `left` can NEVER walk backward (`left <= right`), capping total steps at $2N$!"
                    },
                    {
                        "type": "concept",
                        "title": "The Two Families of Sliding Window + Shrinking Pointers",
                        "content": "1. **Opposite-End Two Pointers (`l = 0, r = n-1`):** Exploits monotonicity (sorted arrays, maximizing width $\\times$ bottleneck height). Every step proves **all other pairs** involving the discarded endpoint are provably suboptimal and eliminates an entire row/column of the $N \\times N$ search matrix in $O(1)$!\n2. **Same-Direction Variable Sliding Window (`l = 0, r = 0..n-1`):** Expand `r` to include element `x`, updating window state. While the window **violates** the constraint (e.g., duplicate character, sum $> K$, distinct count $> K$), increment `l` and undo `arr[l]` from window state until valid again. Update answer cleanly once valid.",
                        "technical_explanation": "**Two Common Coding Ninjas Pitfalls:**\n- Storing last-seen indices (`last_idx[c]`) instead of `while` shrinking: if you set `left = last_idx[c] + 1` unconditionally on seeing `'a'` in `\"abba\"`, `left` would jump **backward** to `1`! Always write `left = max(left, last_idx[c] + 1)`.\n- Forgetting to shrink with `while` vs `if` when looking for exact/minimum window lengths!"
                    },
                    {
                        "type": "visual_stepper",
                        "title": "Interactive Dry Run: Longest Unique Substring on 'abba'",
                        "steps": [
                            {
                                "explanation": "`r=0` ('a'): Window `['a']`, `last['a']=0`, `l=0`, `max_len=1`.",
                                "mermaid_code": "graph LR\n  A[\"a (l=0,r=0)\"] --> B[\"b\"] --> C[\"b\"] --> D[\"a\"]\n  style A fill:#065f46,stroke:#10b981"
                            },
                            {
                                "explanation": "`r=1` ('b'): Window `['a','b']`, `last['b']=1`, `l=0`, `max_len=2`.",
                                "mermaid_code": "graph LR\n  A[\"a (l=0)\"] --> B[\"b (r=1)\"] --> C[\"b\"] --> D[\"a\"]\n  style A fill:#065f46,stroke:#10b981\n  style B fill:#065f46,stroke:#10b981"
                            },
                            {
                                "explanation": "`r=2` ('b'): Duplicate! Jump `l = max(0, last['b']+1) = 2`. Update `last['b']=2`. Window `['b']`, `max_len=2`.",
                                "mermaid_code": "graph LR\n  A[\"a\"] --> B[\"b\"] --> C[\"b (l=2,r=2)\"] --> D[\"a\"]\n  style C fill:#065f46,stroke:#10b981"
                            },
                            {
                                "explanation": "`r=3` ('a'): `last['a']=0 < l=2`! Using `max(l, 0+1)` keeps `l=2` safely (no backward jump!). Window `['b','a']`, `max_len=2`.",
                                "mermaid_code": "graph LR\n  A[\"a (stale 0)\"] --> B[\"b\"] --> C[\"b (l=2)\"] --> D[\"a (r=3)\"]\n  style C fill:#065f46,stroke:#10b981\n  style D fill:#065f46,stroke:#10b981"
                            }
                        ]
                    }
                ]
            },
            {
                "title": "Module 2: Proof of Opposite-End Elimination & Window Edge Cases",
                "blocks": [
                    {
                        "type": "wrong_approach",
                        "title": "Unsafe Last-Seen Jump Without max()",
                        "language": "cpp",
                        "code": "// BUG on input \"abba\" when r = 3 ('a'):\nif (last.count(s[r])) {\n    left = last[s[r]] + 1; // jumps BACKWARDS from 2 to 1!\n}",
                        "explanation": "At `r=3`, `s[3] = 'a'` was seen at index `0`, outside the active window `[2, 2]`. Moving `left` backward to `1` silently re-admits the duplicate `'b'` at index `1`!"
                    },
                    {
                        "type": "correct_approach",
                        "title": "Monotonic Left Clamp Invariant",
                        "language": "cpp",
                        "code": "if (last.count(s[r])) {\n    left = max(left, last[s[r]] + 1);\n}\nlast[s[r]] = r;",
                        "explanation": "Clamping with `max(left, ...)` guarantees `left` is monotonically non-decreasing, proving strict $O(N)$ runtime and zero stale-window corruption."
                    },
                    {
                        "type": "interactive",
                        "title": "Greedy Elimination Invariant (LC-11)",
                        "question": "In Container With Most Water (`l = 0, r = n - 1`), why do we advance the SHORTER wall inward instead of the taller wall?",
                        "options": [
                            "The shorter wall always sits at the left end",
                            "Area is `min(h[l], h[r]) * (r - l)`. Keeping the shorter wall while narrowing `(r - l)` can NEVER achieve a larger area with any interior partner",
                            "Advancing the taller wall runs in O(N^2)",
                            "To keep the array sorted"
                        ],
                        "answer": 1,
                        "explanation": "Suppose `h[l] <= h[r]`. For every interior `k` (`l < k < r`), width `(k - l) < (r - l)` and height `min(h[l], h[k]) <= h[l]`. Thus `(l, r)` dominates ALL pairs `(l, k)`, safely eliminating index `l` forever!"
                    }
                ]
            },
            {
                "title": "Module 3: Coding Lab I — Container With Most Water (LC-11)",
                "blocks": [
                    {
                        "type": "dsa_problem",
                        "title": "Container With Most Water",
                        "platform_style": "LeetCode 11 • Coding Ninjas Two Pointers",
                        "difficulty": "Medium",
                        "pattern": "Opposite-End Two Pointers",
                        "target_time": "O(N)",
                        "target_space": "O(1)",
                        "statement": "You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the $i$-th line are `(i, 0)` and `(i, height[i])`.\n\nFind two lines that together with the x-axis form a container holding the **most water**. Return the **maximum amount of water** a container can store.",
                        "examples": [
                            {"input": "height = [1, 8, 6, 2, 5, 4, 8, 3, 7]", "output": "49", "explanation": "Lines at index 1 (height 8) and index 8 (height 7): area = min(8, 7) * (8 - 1) = 49."},
                            {"input": "height = [4, 3, 2, 1, 4]", "output": "16", "explanation": "Outer walls at indices 0 and 4: 4 * 4 = 16."}
                        ],
                        "constraints": [
                            "$2 \\le n \\le 10^5$",
                            "$0 \\le \\text{height}[i] \\le 10^4$"
                        ],
                        "approach_ladder": {
                            "brute": "Evaluate all $\\binom{n}{2}$ pairs `min(h[i], h[j]) * (j - i)` in $O(N^2)$ time -> TLE.",
                            "optimal": "Initialize `l = 0, r = n - 1, best = 0`. While `l < r`: compute `area = min(h[l], h[r]) * (r - l)`, update `best`, and advance whichever pointer has the smaller height (`l += 1` if `h[l] < h[r]` else `r -= 1`). **$O(N)$ time, $O(1)$ space**."
                        },
                        "dry_run": "`[1, 8, 6, 2, 5, 4, 8, 3, 7]`: start `(0, 8)` -> `min(1,7)*8 = 8`. Advance `l` (`1 < 7`). Now `(1, 8)` -> `min(8,7)*7 = 49`. Advance `r` (`7 < 8`)...",
                        "edge_cases": [
                            {"title": "Equal Wall Heights", "desc": "When `h[l] == h[r]`, advancing *either* pointer (or even both simultaneously if interior bars matter less!) preserves optimality, though incrementing one safely captures asymmetric walls."}
                        ],
                        "follow_ups": "**LC-42 Trapping Rain Water:** Whereas LC-11 looks for the single largest independent container, Trapping Rain Water sums pooled water above *every* bar using `leftMax` & `rightMax` two pointers!",
                        "hint": "Start as wide as possible (`l=0, r=n-1`) and step inward strictly on the shorter boundary wall.",
                        "starter_py": "class Solution:\n    def maxArea(self, height: List[int]) -> int:\n        # TODO: O(N) Two Pointers\n        return 0\n",
                        "solution_py": "class Solution:\n    def maxArea(self, height: List[int]) -> int:\n        l, r = 0, len(height) - 1\n        best = 0\n        while l < r:\n            h = height[l] if height[l] < height[r] else height[r]\n            area = h * (r - l)\n            if area > best:\n                best = area\n            if height[l] < height[r]:\n                l += 1\n            else:\n                r -= 1\n        return best\n",
                        "harness_py": "_dsa_run_tests([\n    ('Sample 1: Standard Mix', '[1,8,6,2,5,4,8,3,7]', lambda: Solution().maxArea([1,8,6,2,5,4,8,3,7]), 49),\n    ('Sample 2: Symmetric Outer', '[4,3,2,1,4]', lambda: Solution().maxArea([4,3,2,1,4]), 16),\n    ('Edge: Two Zeros', '[0,0]', lambda: Solution().maxArea([0,0]), 0),\n    ('Edge: Tall Center', '[1,2,1]', lambda: Solution().maxArea([1,2,1]), 2),\n    ('Edge: Narrow High Peak', '[1,100,100,1]', lambda: Solution().maxArea([1,100,100,1]), 100),\n], sample_only=__DSA_SAMPLE_ONLY__, n_samples=2)",
                        "starter_cpp": "class Solution {\npublic:\n    int maxArea(vector<int>& height) {\n        // TODO: O(N) time, O(1) space\n        return 0;\n    }\n};\n",
                        "solution_cpp": "class Solution {\npublic:\n    int maxArea(vector<int>& height) {\n        int l = 0, r = (int)height.size() - 1, best = 0;\n        while (l < r) {\n            int h = min(height[l], height[r]);\n            best = max(best, h * (r - l));\n            if (height[l] < height[r]) ++l;\n            else --r;\n        }\n        return best;\n    }\n};\n",
                        "harness_cpp": "int main() {\n    ostringstream _dbg; streambuf* _old = cout.rdbuf(_dbg.rdbuf());\n    vector<_DSACaseOut> _res;\n    struct T { string name, inp; vector<int> arr; int exp; };\n    vector<T> tests = {\n        {\"Sample 1: Standard Mix\", \"[1,8,6,2,5,4,8,3,7]\", {1,8,6,2,5,4,8,3,7}, 49},\n        {\"Sample 2: Symmetric Outer\", \"[4,3,2,1,4]\", {4,3,2,1,4}, 16},\n        {\"Edge: Two Zeros\", \"[0,0]\", {0,0}, 0},\n        {\"Edge: Tall Center\", \"[1,2,1]\", {1,2,1}, 2},\n        {\"Edge: Narrow High Peak\", \"[1,100,100,1]\", {1,100,100,1}, 100}\n    };\n    int lim = DSA_SAMPLE_ONLY ? 2 : (int)tests.size();\n    Solution sol;\n    for (int i = 0; i < lim; ++i) {\n        auto v = tests[i].arr;\n        auto t0 = chrono::steady_clock::now();\n        int act = sol.maxArea(v);\n        double ms = chrono::duration<double, milli>(chrono::steady_clock::now() - t0).count();\n        _res.push_back({tests[i].name, tests[i].inp, _dsa_fmt(tests[i].exp), _dsa_fmt(act), \"\", act == tests[i].exp, ms});\n    }\n    cout.rdbuf(_old);\n    _dsa_emit_json(_res, _dbg.str());\n    return 0;\n}"
                    }
                ]
            },
            {
                "title": "Module 4: Coding Lab II — Longest Substring Without Repeating Characters (LC-3)",
                "blocks": [
                    {
                        "type": "dsa_problem",
                        "title": "Longest Substring Without Repeating Characters",
                        "platform_style": "LeetCode 3 • Coding Ninjas Sliding Window Classics",
                        "difficulty": "Medium",
                        "pattern": "Variable Sliding Window + Last-Seen Map",
                        "target_time": "O(N)",
                        "target_space": "O(min(N, |Sigma|))",
                        "statement": "Given a string `s`, find the length of the **longest contiguous substring** without repeating characters.",
                        "examples": [
                            {"input": "s = \"abcabcbb\"", "output": "3", "explanation": "Longest substring is \"abc\" with length 3."},
                            {"input": "s = \"pwwkew\"", "output": "3", "explanation": "Longest substring is \"wke\" (note \"pwke\" is a subsequence, NOT contiguous!)."}
                        ],
                        "constraints": [
                            "$0 \\le s.\\text{length} \\le 5 \\times 10^4$",
                            "`s` consists of English letters, digits, symbols and spaces."
                        ],
                        "approach_ladder": {
                            "brute": "Check all $O(N^2)$ substrings for uniqueness ($O(N^3)$ naive or $O(N^2)$ with bitmask/set).",
                            "better": "Sliding window with `set`: when `s[r]` already exists in set, shrink `l += 1` inside a `while` loop deleting `s[l]` until valid ($2N$ steps).",
                            "optimal": "Store `last_seen[ch]` (or ASCII array `vector<int>(256, -1)` in C++!). Jump `l = max(l, last_seen[ch] + 1)`, record `last_seen[ch] = r`, update `best = max(best, r - l + 1)` in exactly $N$ single-pass steps!"
                        },
                        "dry_run": "`\"pwwkew\"`: `r=0('p')->1`, `r=1('w')->2`, `r=2('w')` duplicate `l=2` len=1, `r=3('k')` len=2, `r=4('e')` len=3, `r=5('w')` jump `l=max(2, 2+1)=3` (`\"kew\"` len=3) -> **3**.",
                        "edge_cases": [
                            {"title": "Empty String & Spaces", "desc": "`\"\"` -> `0`; `\" \"` (single space) -> `1`! Avoid fixed `26`-letter assumptions since punctuation and spaces appear."},
                            {"title": "Backward Left Jump (`\"abba\"`)", "desc": "Always guard with `max(l, last_seen[ch] + 1)`."}
                        ],
                        "follow_ups": "**LC-340 / LC-904:** Extend to Longest Substring with At Most $K$ Distinct Characters by tracking a frequency map `len(freq) > K` shrink loop.",
                        "hint": "Use a 256-entry ASCII array in C++ or dictionary in Python, and clamp `left = max(left, last[ch] + 1)`.",
                        "starter_py": "class Solution:\n    def lengthOfLongestSubstring(self, s: str) -> int:\n        # TODO: Sliding window in O(N) time\n        return 0\n",
                        "solution_py": "class Solution:\n    def lengthOfLongestSubstring(self, s: str) -> int:\n        last = {}\n        left = 0\n        best = 0\n        for right, ch in enumerate(s):\n            if ch in last and last[ch] >= left:\n                left = last[ch] + 1\n            last[ch] = right\n            best = max(best, right - left + 1)\n        return best\n",
                        "harness_py": "_dsa_run_tests([\n    ('Sample 1: abcabcbb', 's=\"abcabcbb\"', lambda: Solution().lengthOfLongestSubstring('abcabcbb'), 3),\n    ('Sample 2: pwwkew', 's=\"pwwkew\"', lambda: Solution().lengthOfLongestSubstring('pwwkew'), 3),\n    ('Edge: Empty String', 's=\"\"', lambda: Solution().lengthOfLongestSubstring(''), 0),\n    ('Edge: Space Char', 's=\" \"', lambda: Solution().lengthOfLongestSubstring(' '), 1),\n    ('Trap: abba Jump', 's=\"abba\"', lambda: Solution().lengthOfLongestSubstring('abba'), 2),\n    ('Edge: All Identical', 's=\"bbbb\"', lambda: Solution().lengthOfLongestSubstring('bbbb'), 1),\n], sample_only=__DSA_SAMPLE_ONLY__, n_samples=2)",
                        "starter_cpp": "class Solution {\npublic:\n    int lengthOfLongestSubstring(string s) {\n        // TODO: O(N) ASCII sliding window\n        return 0;\n    }\n};\n",
                        "solution_cpp": "class Solution {\npublic:\n    int lengthOfLongestSubstring(string s) {\n        vector<int> last(256, -1);\n        int left = 0, best = 0;\n        for (int r = 0; r < (int)s.size(); ++r) {\n            unsigned char c = static_cast<unsigned char>(s[r]);\n            if (last[c] >= left) left = last[c] + 1;\n            last[c] = r;\n            best = max(best, r - left + 1);\n        }\n        return best;\n    }\n};\n",
                        "harness_cpp": "int main() {\n    ostringstream _dbg; streambuf* _old = cout.rdbuf(_dbg.rdbuf());\n    vector<_DSACaseOut> _res;\n    struct T { string name, inp, s; int exp; };\n    vector<T> tests = {\n        {\"Sample 1: abcabcbb\", \"s=abcabcbb\", \"abcabcbb\", 3},\n        {\"Sample 2: pwwkew\", \"s=pwwkew\", \"pwwkew\", 3},\n        {\"Edge: Empty String\", \"s=\\\"\\\"\", \"\", 0},\n        {\"Edge: Space Char\", \"s=\\\" \\\"\", \" \", 1},\n        {\"Trap: abba Jump\", \"s=abba\", \"abba\", 2},\n        {\"Edge: All Identical\", \"s=bbbb\", \"bbbb\", 1}\n    };\n    int lim = DSA_SAMPLE_ONLY ? 2 : (int)tests.size();\n    Solution sol;\n    for (int i = 0; i < lim; ++i) {\n        auto t0 = chrono::steady_clock::now();\n        int act = sol.lengthOfLongestSubstring(tests[i].s);\n        double ms = chrono::duration<double, milli>(chrono::steady_clock::now() - t0).count();\n        _res.push_back({tests[i].name, tests[i].inp, _dsa_fmt(tests[i].exp), _dsa_fmt(act), \"\", act == tests[i].exp, ms});\n    }\n    cout.rdbuf(_old);\n    _dsa_emit_json(_res, _dbg.str());\n    return 0;\n}"
                    }
                ]
            }
        ]
    }
}
