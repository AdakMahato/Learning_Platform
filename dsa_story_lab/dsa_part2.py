# DSA Cases 04 to 07: Hashing, Sorting/Intervals/Inversions, Binary Search, Strings/KMP

CASES_PART2 = {
    "4": {
        "title": "Case 04: Collision Storm — Hash Tables, Load Factors & O(1) Lookup",
        "episodes": [
            {
                "title": "Module 1: Hash Collisions, Open Addressing & Load Factor Bounds",
                "blocks": [
                    {
                        "type": "story",
                        "title": "Hash DoS on the API Cache",
                        "content": "An attacker flooded the cache with carefully crafted keys colliding into bucket #0, turning expected $O(1)$ lookups into a catastrophic $O(N)$ linked-list scan.\n\n> [!WARNING]\n> Every hash table trades worst-case guarantees for $O(1)$ **expected** lookup under Uniform Hashing — unless protected by randomized hashing (like Python SipHash) or custom 64-bit mixing (`splitmix64`) in C++!"
                    },
                    {
                        "type": "objective",
                        "content": "Derive hash table performance as a function of load factor $\\alpha = N/M$, contrast Separate Chaining vs Open Addressing (Linear/Quadratic/Double Hashing), solve tombstone deletion traps, and master HashMap/HashSet streak patterns."
                    },
                    {
                        "type": "concept",
                        "title": "Load Factor α, Chaining & Probing Mechanics",
                        "content": "Given $N$ stored entries and $M$ buckets, the **Load Factor** is $\\alpha = \\frac{N}{M}$:\n\n1. **Separate Chaining:** Each bucket holds a linked list (or dynamic vector / Java 8+ converts chains $>8$ into Red-Black Trees for $O(\\log N)$ worst-case!). Expected unsuccessful probe cost is $1 + \\alpha$, so rehashing triggers around $\\alpha \\ge 1.0$.\n2. **Open Addressing (Linear Probing `h(k, i) = (h(k) + i) % M`):** All keys sit contiguously in a single array (great CPU cache locality!). However, **primary clustering** forms long occupied runs as $\\alpha \\to 0.7$, requiring aggressive resizing around $\\alpha \\ge 0.5\\text{–}0.75$ and special **Tombstone (`DELETED`) markers** so deleting a middle key doesn't break the probe chain for downstream keys!",
                        "technical_explanation": "**C++ `unordered_map` Trap:** Standard C++ `std::hash<long long>` is often the identity function, and bucket counts in older GCC/libstdc++ implementations use primes like `107897` or powers of 2. Competitive tests deliberately insert multiples of that prime to force $O(N^2)$ TLE! Using a custom functor with `splitmix64` and `chrono::steady_clock` random salt prevents hash DoS."
                    },
                    {
                        "type": "comparison_table",
                        "title": "std::unordered_map vs std::map (Hash vs Ordered RB-Tree)",
                        "headers": ["Property", "Hash Map (unordered_map / dict)", "Ordered Tree Map (std::map / TreeMap)"],
                        "rows": [
                            ["Average Lookup/Insert", "O(1) Expected", "O(log N) Guaranteed"],
                            ["Worst-Case Single Op", "O(N) on total collision", "O(log N) Strict Worst-Case"],
                            ["Sorted Iteration / Range Query", "Unsupported", "In-order traversal, lower_bound / upper_bound in O(log N)"],
                            ["Key Requirement", "Hashable + Equality (==)", "Strict Weak Ordering (<)"],
                            ["Cache & Memory Overhead", "Contiguous bucket array (open addressing very fast)", "3 pointers + color bit per heap node (~32B overhead/node)"]
                        ]
                    },
                    {
                        "type": "interactive",
                        "title": "Tombstone Necessity in Open Addressing",
                        "question": "In a Linear Probing hash table, why can't deleting a key simply set its slot back to EMPTY?",
                        "options": [
                            "It violates C++ memory alignment",
                            "Setting it to EMPTY breaks the probe sequence, causing lookups for keys that collided through that slot earlier to stop early and falsely report 'not found'",
                            "EMPTY slots double the load factor",
                            "Hash functions throw an exception on EMPTY slots"
                        ],
                        "answer": 1,
                        "explanation": "Suppose `k1` and `k2` both hashed to index 4, so `k2` landed at index 5. If `k1` at index 4 were marked EMPTY instead of TOMBSTONE (`DELETED`), searching for `k2` would probe index 4, see EMPTY, and wrongly conclude `k2` does not exist!"
                    }
                ]
            },
            {
                "title": "Module 2: Proof of O(N) Streak Starts & Duplicate-Key Traps",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "Why Longest Consecutive Sequence (LC-128) Is O(N), Not O(N^2)",
                        "content": "Checking a `while (x + 1 in num_set)` inside a `for x in num_set:` loop looks quadratic ($O(N^2)$) at first glance!\n\n**Proof of Strict O(N) Amortized Bound:**\nAdd a single guard: **`if (x - 1) not in num_set:`**.\n- Only minimal **sequence heads** (numbers lacking a predecessor) enter the `while` loop.\n- Every number in `num_set` belongs to **at most one** maximal consecutive chain `[start, ..., start + L - 1]`.\n- Therefore each unique element is visited **at most twice** (once by the outer loop checking `x - 1`, and once by the `while` walk of its sequence start) -> **$O(N)$** total steps!",
                        "technical_explanation": "**Important Optimization Detail:** Always iterate over the deduplicated `set` (`unordered_set<int> s(nums.begin(), nums.end())`), NEVER over `nums` directly! If `[1, 1, 1, ..., 2, 3, ..., 1000]` has 50,000 copies of `1`, iterating over `nums` runs the `while` streak 50,000 times -> **TLE**!"
                    },
                    {
                        "type": "debugger",
                        "title": "Pre-Populated Map Bug in Two Sum",
                        "scenario": "A student pre-inserts all `{nums[i]: i}` into a map in Pass 1, then checks `target - nums[i] in mp` in Pass 2 without checking indices.\nOn `nums = [3, 3], target = 6`, Pass 1 overwrites `mp[3] = 1`. When Pass 2 reaches `i = 0`, it finds `mp[6 - 3] == 1` (`[0, 1]`), which happens to work... Wait: what fails on `nums = [3, 2, 4], target = 6`?",
                        "options": [
                            "It works fine on all inputs",
                            "At i = 0 (nums[0] = 3), 6 - 3 = 3 finds ITSELF at index 0 and falsely returns [0, 0] unless i != mp[comp] is checked!",
                            "Target 6 cannot be formed from [3, 2, 4]",
                            "Map lookup fails on even numbers"
                        ],
                        "answer": 1,
                        "explanation": "Single-pass insertion solves this cleanly AND prevents self-pairing automatically: check if `target - nums[i]` is already in `seen` **before** inserting `seen[nums[i]] = i`!"
                    },
                    {
                        "type": "calculation_challenge",
                        "title": "Rehash Threshold Calculation",
                        "formula": "An open-addressing hash table currently has $M = 64$ slots and policy requires $\\alpha = N / M \\le 0.75$ before resizing.",
                        "problem": "What is the maximum number of elements $N$ that can be stored before triggering a rehash?",
                        "answer": "48",
                        "alternatives": ["48"],
                        "step_by_step": "$0.75 \\times 64 = \\frac{3}{4} \\times 64 = 48$."
                    }
                ]
            },
            {
                "title": "Module 3: Coding Lab I — Two Sum (LC-1)",
                "blocks": [
                    {
                        "type": "dsa_problem",
                        "title": "Two Sum",
                        "platform_style": "LeetCode 1 • Coding Ninjas Most-Asked Starter",
                        "difficulty": "Easy",
                        "pattern": "Complement HashMap (Single Pass)",
                        "target_time": "O(N)",
                        "target_space": "O(N)",
                        "statement": "Given an array of integers `nums` and an integer `target`, return **indices of the two numbers** such that they add up to `target`.\n\nYou may assume each input has **at least one valid pair**, you may **not** use the same element twice, and you may return the answer in any order.",
                        "examples": [
                            {"input": "nums = [2, 7, 11, 15], target = 9", "output": "[0, 1]", "explanation": "Because nums[0] + nums[1] == 9."},
                            {"input": "nums = [3, 3], target = 6", "output": "[0, 1]", "explanation": "Same value at distinct indices 0 and 1 sums to 6."}
                        ],
                        "constraints": [
                            "$2 \\le \\text{nums.length} \\le 10^4$",
                            "$-10^9 \\le \\text{nums}[i], \\text{target} \\le 10^9$"
                        ],
                        "approach_ladder": {
                            "brute": "Double nested loop checking every `i < j`: $O(N^2)$ time, $O(1)$ space.",
                            "optimal": "Single-pass map `seen[val] = idx`. Before inserting `nums[i]`, check if `target - nums[i]` is in `seen`. If so, return `[seen[comp], i]`. **$O(N)$ expected time, $O(N)$ space**."
                        },
                        "dry_run": "`[3, 2, 4], target = 6`: `i=0(3)` need `3` (miss, `seen={3:0}`) -> `i=1(2)` need `4` (miss, `seen={3:0,2:1}`) -> `i=2(4)` need `2` (**HIT `seen[2]=1`** -> return `[1, 2]`).",
                        "edge_cases": [
                            {"title": "Self-Reuse on target == 2 * x", "desc": "`[3, 2, 4], target = 6` must NOT return `[0, 0]`; querying before inserting solves this naturally!"},
                            {"title": "Duplicates Pair", "desc": "`[3, 3], target = 6` returns `[0, 1]` before second `3` overwrites first."}
                        ],
                        "follow_ups": "**LC-167 Two Sum II (Sorted Input):** Use Two Pointers in **$O(1)$ auxiliary space**!",
                        "hint": "Store `{value: index}` in a hash table; look up `target - x` BEFORE storing `x`.",
                        "starter_py": "class Solution:\n    def twoSum(self, nums: List[int], target: int) -> List[int]:\n        # TODO: Return [idx1, idx2] in O(N)\n        return []\n",
                        "solution_py": "class Solution:\n    def twoSum(self, nums: List[int], target: int) -> List[int]:\n        seen = {}\n        for i, x in enumerate(nums):\n            comp = target - x\n            if comp in seen:\n                return [seen[comp], i]\n            seen[x] = i\n        return []\n",
                        "harness_py": "_dsa_run_tests([\n    ('Sample 1: Sorted Pair', '[2,7,11,15], target=9', lambda: sorted(Solution().twoSum([2,7,11,15], 9)), [0, 1]),\n    ('Sample 2: Duplicates', '[3,3], target=6', lambda: sorted(Solution().twoSum([3,3], 6)), [0, 1]),\n    ('Edge: Self-Trap 2*x=target', '[3,2,4], target=6', lambda: sorted(Solution().twoSum([3,2,4], 6)), [1, 2]),\n    ('Edge: Negative Numbers', '[-3,4,3,90], target=0', lambda: sorted(Solution().twoSum([-3,4,3,90], 0)), [0, 2]),\n    ('Edge: Large Negatives', '[-10,-2,-5,15], target=10', lambda: sorted(Solution().twoSum([-10,-2,-5,15], 10)), [2, 3]),\n], sample_only=__DSA_SAMPLE_ONLY__, n_samples=2)",
                        "starter_cpp": "class Solution {\npublic:\n    vector<int> twoSum(vector<int>& nums, int target) {\n        // TODO: O(N) hash complement lookup\n        return {};\n    }\n};\n",
                        "solution_cpp": "class Solution {\npublic:\n    vector<int> twoSum(vector<int>& nums, int target) {\n        unordered_map<long long, int> seen;\n        for (int i = 0; i < (int)nums.size(); ++i) {\n            long long comp = (long long)target - nums[i];\n            auto it = seen.find(comp);\n            if (it != seen.end()) return {it->second, i};\n            seen[nums[i]] = i;\n        }\n        return {};\n    }\n};\n",
                        "harness_cpp": "int main() {\n    ostringstream _dbg; streambuf* _old = cout.rdbuf(_dbg.rdbuf());\n    vector<_DSACaseOut> _res;\n    struct T { string name, inp; vector<int> arr; int target; vector<int> exp; };\n    vector<T> tests = {\n        {\"Sample 1: Sorted Pair\", \"[2,7,11,15], target=9\", {2,7,11,15}, 9, {0, 1}},\n        {\"Sample 2: Duplicates\", \"[3,3], target=6\", {3,3}, 6, {0, 1}},\n        {\"Edge: Self-Trap 2*x=target\", \"[3,2,4], target=6\", {3,2,4}, 6, {1, 2}},\n        {\"Edge: Negative Numbers\", \"[-3,4,3,90], target=0\", {-3,4,3,90}, 0, {0, 2}},\n        {\"Edge: Large Negatives\", \"[-10,-2,-5,15], target=10\", {-10,-2,-5,15}, 10, {2, 3}}\n    };\n    int lim = DSA_SAMPLE_ONLY ? 2 : (int)tests.size();\n    Solution sol;\n    for (int i = 0; i < lim; ++i) {\n        auto v = tests[i].arr;\n        auto t0 = chrono::steady_clock::now();\n        auto act = sol.twoSum(v, tests[i].target);\n        double ms = chrono::duration<double, milli>(chrono::steady_clock::now() - t0).count();\n        sort(act.begin(), act.end());\n        _res.push_back({tests[i].name, tests[i].inp, _dsa_fmt(tests[i].exp), _dsa_fmt(act), \"\", act == tests[i].exp, ms});\n    }\n    cout.rdbuf(_old);\n    _dsa_emit_json(_res, _dbg.str());\n    return 0;\n}"
                    }
                ]
            },
            {
                "title": "Module 4: Coding Lab II — Longest Consecutive Sequence (LC-128)",
                "blocks": [
                    {
                        "type": "dsa_problem",
                        "title": "Longest Consecutive Sequence",
                        "platform_style": "LeetCode 128 • Coding Ninjas Hashing Hard-Medium",
                        "difficulty": "Medium",
                        "pattern": "HashSet Minimal-Head Detection",
                        "target_time": "O(N)",
                        "target_space": "O(N)",
                        "statement": "Given an unsorted array of integers `nums`, return the **length of the longest consecutive elements sequence** (order in `nums` does not matter).\n\nYou must write an algorithm that runs in **$O(N)$ expected time** (sorting in $O(N \\log N)$ violates the optimal target!).",
                        "examples": [
                            {"input": "nums = [100, 4, 200, 1, 3, 2]", "output": "4", "explanation": "Longest consecutive sequence is [1, 2, 3, 4], length = 4."},
                            {"input": "nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]", "output": "9", "explanation": "Sequence [0..8] spans length 9 despite duplicate 0."}
                        ],
                        "constraints": [
                            "$0 \\le \\text{nums.length} \\le 10^5$",
                            "$-10^9 \\le \\text{nums}[i] \\le 10^9$"
                        ],
                        "approach_ladder": {
                            "brute": "For each `x`, linearly scan array looking for `x+1, x+2, ...`: $O(N^3)$ naive or $O(N^2)$ with set.",
                            "better": "Sort `nums` and track consecutive streak skipping duplicates: $O(N \\log N)$ time.",
                            "optimal": "Put all items into `num_set`. Iterate over **`num_set`** (deduplicated!). Only when `x - 1` is NOT in `num_set`, expand `cur = x + 1` while `cur in num_set`. Track max streak length: **$O(N)$ time, $O(N)$ space**."
                        },
                        "dry_run": "`{100, 4, 200, 1, 3, 2}` -> only `100` (`len=1`), `200` (`len=1`), and `1` (`len=4: 1->2->3->4`) lack `x-1` -> max = **4**.",
                        "edge_cases": [
                            {"title": "Empty Input []", "desc": "Return `0` cleanly when `nums` is empty."},
                            {"title": "Iterate Over Set, Not Raw Array", "desc": "Iterating over raw `nums` when duplicates exist turns $O(N)$ into $O(N^2)$ and triggers TLE on adversarial duplicate tests!"}
                        ],
                        "follow_ups": "**Union-Find Alternative:** Map `val -> node_id`, union adjacent `x` with `x+1`, and return max component size!",
                        "hint": "Deduplicate into a hash set and start counting streaks ONLY from numbers where `num - 1` is absent.",
                        "starter_py": "class Solution:\n    def longestConsecutive(self, nums: List[int]) -> int:\n        # TODO: Must run in O(N) time!\n        return 0\n",
                        "solution_py": "class Solution:\n    def longestConsecutive(self, nums: List[int]) -> int:\n        s = set(nums)\n        best = 0\n        for x in s:\n            if x - 1 not in s:\n                cur = x + 1\n                while cur in s:\n                    cur += 1\n                best = max(best, cur - x)\n        return best\n",
                        "harness_py": "_dsa_run_tests([\n    ('Sample 1: Unsorted Mix', '[100,4,200,1,3,2]', lambda: Solution().longestConsecutive([100,4,200,1,3,2]), 4),\n    ('Sample 2: Duplicates Included', '[0,3,7,2,5,8,4,6,0,1]', lambda: Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]), 9),\n    ('Edge: Empty Array', '[]', lambda: Solution().longestConsecutive([]), 0),\n    ('Edge: Negatives Chain', '[-2,-1,0,1,10]', lambda: Solution().longestConsecutive([-2,-1,0,1,10]), 4),\n    ('Stress: 5000 Same Value + Streak', '[1]*5000 + [2,3,4]', lambda: Solution().longestConsecutive([1]*5000 + [2,3,4]), 4),\n], sample_only=__DSA_SAMPLE_ONLY__, n_samples=2)",
                        "starter_cpp": "class Solution {\npublic:\n    int longestConsecutive(vector<int>& nums) {\n        // TODO: O(N) unordered_set minimal-head walk\n        return 0;\n    }\n};\n",
                        "solution_cpp": "class Solution {\npublic:\n    int longestConsecutive(vector<int>& nums) {\n        unordered_set<int> s(nums.begin(), nums.end());\n        int best = 0;\n        for (int x : s) {\n            if (!s.count(x - 1)) {\n                int cur = x + 1;\n                while (s.count(cur)) ++cur;\n                best = max(best, cur - x);\n            }\n        }\n        return best;\n    }\n};\n",
                        "harness_cpp": "int main() {\n    ostringstream _dbg; streambuf* _old = cout.rdbuf(_dbg.rdbuf());\n    vector<_DSACaseOut> _res;\n    struct T { string name, inp; vector<int> arr; int exp; };\n    vector<int> stress(5000, 1);\n    stress.push_back(2); stress.push_back(3); stress.push_back(4);\n    vector<T> tests = {\n        {\"Sample 1: Unsorted Mix\", \"[100,4,200,1,3,2]\", {100,4,200,1,3,2}, 4},\n        {\"Sample 2: Duplicates Included\", \"[0,3,7,2,5,8,4,6,0,1]\", {0,3,7,2,5,8,4,6,0,1}, 9},\n        {\"Edge: Empty Array\", \"[]\", {}, 0},\n        {\"Edge: Negatives Chain\", \"[-2,-1,0,1,10]\", {-2,-1,0,1,10}, 4},\n        {\"Stress: 5000 Same Value\", \"5000 ones + [2,3,4]\", stress, 4}\n    };\n    int lim = DSA_SAMPLE_ONLY ? 2 : (int)tests.size();\n    Solution sol;\n    for (int i = 0; i < lim; ++i) {\n        auto v = tests[i].arr;\n        auto t0 = chrono::steady_clock::now();\n        int act = sol.longestConsecutive(v);\n        double ms = chrono::duration<double, milli>(chrono::steady_clock::now() - t0).count();\n        _res.push_back({tests[i].name, tests[i].inp, _dsa_fmt(tests[i].exp), _dsa_fmt(act), \"\", act == tests[i].exp, ms});\n    }\n    cout.rdbuf(_old);\n    _dsa_emit_json(_res, _dbg.str());\n    return 0;\n}"
                    }
                ]
            }
        ]
    },
    "5": {
        "title": "Case 05: The Unstable Ledger — Sorting Theory & Divide and Conquer",
        "episodes": [
            {
                "title": "Module 1: Ω(N log N) Lower Bound Proof, Stability & Sort Taxonomy",
                "blocks": [
                    {
                        "type": "story",
                        "title": "Why Multi-Key Sorting Scrambled Dates",
                        "content": "Accountants sorted transactions by `timestamp`, then sorted by `category`. Switching from Python's Timsort to an unstable in-place `Quicksort` scrambled timestamp ties within every category!\n\n> [!NOTE]\n> Understanding **Stability**, **In-Place Space**, and the **Comparison Decision Tree Lower Bound** separates memorizers from real engineers."
                    },
                    {
                        "type": "concept",
                        "title": "Decision Tree Lower Bound & Sorting Algorithm Taxonomy",
                        "content": "**Proof that EVERY comparison-based sort needs $\\Omega(N \\log N)$ comparisons:**\nA sorting algorithm must distinguish among all **$N!$** possible input permutations via binary (`<=` vs `>`) comparisons.\nAny binary decision tree with $L \\ge N!$ leaves has height $h$ satisfying:\n$$2^h \\ge N! \\implies h \\ge \\log_2(N!) \\ge \\log_2\\!\\left((N/2)^{N/2}\\right) = \\frac{N}{2} \\log_2(N/2) = \\Omega(N \\log N)$$\n\n- **How can Counting Sort / Radix Sort beat $\\Omega(N \\log N)$?** They do **NOT** compare elements pairwise — they index directly by integer value/digits in $O(N + K)$!\n- **Stability Definition:** Equal keys preserve their original relative order. Crucial for sorting multi-column tables (`Timsort` & `Merge Sort` are stable; standard `Quicksort` & `Heapsort` are unstable!).",
                        "technical_explanation": "**Introsort (`std::sort`) vs Timsort (`list.sort`):** C++ `std::sort` uses **Introsort** (Quicksort + switches to Heapsort if recursion depth exceeds $2\\log_2 N$ to guarantee $O(N \\log N)$ worst-case + Insertion Sort below 16 elements). Use `std::stable_sort` when order ties matter!"
                    },
                    {
                        "type": "comparison_table",
                        "title": "Sorting Algorithms Master Matrix",
                        "headers": ["Algorithm", "Best", "Average", "Worst", "Extra Space", "Stable?"],
                        "rows": [
                            ["Insertion Sort", "O(N)", "O(N^2)", "O(N^2)", "O(1)", "Yes"],
                            ["Merge Sort", "O(N log N)", "O(N log N)", "O(N log N)", "O(N)", "Yes (if <= used)"],
                            ["Quick Sort (Randomized)", "O(N log N)", "O(N log N)", "O(N^2)", "O(log N) stack", "No"],
                            ["Heap Sort", "O(N log N)", "O(N log N)", "O(N log N)", "O(1)", "No"],
                            ["Timsort (Python)", "O(N)", "O(N log N)", "O(N log N)", "O(N)", "Yes"],
                            ["Counting / Radix Sort", "O(N + K)", "O(d(N + B))", "O(d(N + B))", "O(N + B)", "Yes"]
                        ]
                    },
                    {
                        "type": "interactive",
                        "title": "Inversion Count Complexity Check",
                        "question": "Why must Merge Sort check `left[i] <= right[j]` (with `<=`, not strict `<`) when splitting elements AND when counting cross-inversions?",
                        "options": [
                            "Strict < divides by zero",
                            "Strict < skips equality and treats equal elements left[i] == right[j] as an inversion (violating i < j AND a[i] > a[j]) AND breaks sort stability!",
                            "Merge sort cannot sort negative integers otherwise",
                            "Both give identical results on all inputs"
                        ],
                        "answer": 1,
                        "explanation": "An inversion requires STRICT inequality `a[i] > a[j]`. Using `<=` takes `left[i]` first on ties, both preserving stability and refusing to count equal elements as inversions."
                    }
                ]
            },
            {
                "title": "Module 2: Merge Sort Inversion Math & Interval Sweep",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "Divide & Conquer Cross-Inversion Formula",
                        "content": "To count pairs `(i < j)` with `a[i] > a[j]` without testing all $\\binom{N}{2}$ pairs:\nSplit `arr` at `mid` -> recursively count `left_invs` + `right_invs`.\nDuring the **Merge** step, both halves `a[l..mid]` and `a[mid+1..r]` are already sorted!\nWhen **`a[i] > a[j]`** (`i` in left, `j` in right), EVERY remaining element from `i` through `mid` (`a[i], a[i+1], ..., a[mid]`) is ALSO strictly greater than `a[j]`, adding **`(mid - i + 1)`** inversions in $O(1)$ time!",
                        "technical_explanation": "Total inversions in a reverse-sorted array of size $N = 10^5$ can reach $\\frac{10^5 \\times 99999}{2} \\approx 5 \\times 10^9$, which overflows 32-bit signed `int` (`2.14e9`). Always accumulate inversion counts in 64-bit `long long` in C++!"
                    },
                    {
                        "type": "visual",
                        "title": "Cross-Inversion Leap During Merge",
                        "code": "flowchart LR\n  L[\"Sorted Left: [3, 6, 8] (i points at 6)\"] --> CHK{\"6 > right[j] = 4?\"}\n  CHK -->|Yes| ADD[\"+ (mid - i + 1) = +2 inversions: (6,4) & (8,4)\"]\n  R[\"Sorted Right: [1, 4, 9] (j points at 4)\"] --> CHK"
                    },
                    {
                        "type": "calculation_challenge",
                        "title": "Decision Tree Leaves Check",
                        "formula": "Maximum inversions in an $N$-element array equals $\\frac{N(N-1)}{2}$ (strictly decreasing order).",
                        "problem": "How many total inversions are in `[9, 7, 5, 3, 1]` ($N = 5$)?",
                        "answer": "10",
                        "alternatives": ["10"],
                        "step_by_step": "Strictly decreasing array of length 5 has $\\frac{5 \\times 4}{2} = 10$ inversions."
                    }
                ]
            },
            {
                "title": "Module 3: Coding Lab I — Merge Intervals (LC-56)",
                "blocks": [
                    {
                        "type": "dsa_problem",
                        "title": "Merge Overlapping Intervals",
                        "platform_style": "LeetCode 56 • Coding Ninjas Interval Sweep",
                        "difficulty": "Medium",
                        "pattern": "Sorting + Greedy Endpoint Merge",
                        "target_time": "O(N log N)",
                        "target_space": "O(N)",
                        "statement": "Given an array of `intervals` where `intervals[i] = [start_i, end_i]`, merge all overlapping intervals, and return an array of the **non-overlapping intervals** covering all intervals in the input (sorted by start).",
                        "examples": [
                            {"input": "intervals = [[1,3],[2,6],[8,10],[15,18]]", "output": "[[1,6],[8,10],[15,18]]", "explanation": "[1,3] and [2,6] overlap and merge into [1,6]."},
                            {"input": "intervals = [[1,4],[4,5]]", "output": "[[1,5]]", "explanation": "Touching endpoints (4 == 4) ARE considered overlapping."}
                        ],
                        "constraints": [
                            "$1 \\le \\text{intervals.length} \\le 10^4$",
                            "$0 \\le \\text{start}_i \\le \\text{end}_i \\le 10^4$"
                        ],
                        "approach_ladder": {
                            "brute": "Repeatedly scan pairs checking `s1 <= e2 and s2 <= e1` until fixed point: $O(N^2)$.",
                            "optimal": "Sort intervals by `start` ascending. Maintain `merged`. For each `[s, e]`, if `merged` is empty or `s > merged[-1][1]`, append `[s, e]`; otherwise **update `merged[-1][1] = max(merged[-1][1], e)`**! **$O(N \\log N)$ time**."
                        },
                        "dry_run": "`[[1,4], [2,3]]`: sorted -> push `[1,4]`; next `[2,3]` has `2 <= 4`, update `max(4, 3) = 4` -> result `[[1,4]]`.",
                        "edge_cases": [
                            {"title": "Completely Enclosed Interval", "desc": "`[[1,4], [2,3]]` MUST use `max(merged[-1][1], e)`, NEVER blindly assign `merged[-1][1] = e`!"},
                            {"title": "Unsorted Input Order", "desc": "`[[4,5], [1,4]]` must be sorted by start time first."}
                        ],
                        "follow_ups": "**LC-57 Insert Interval:** Insert one interval into already-sorted disjoint intervals in strictly $O(N)$ without sorting!",
                        "hint": "Sort by start coordinate first; only compare against the last merged interval's end using `max()`.",
                        "starter_py": "class Solution:\n    def merge(self, intervals: List[List[int]]) -> List[List[int]]:\n        # TODO: Sort by start and merge overlaps\n        return []\n",
                        "solution_py": "class Solution:\n    def merge(self, intervals: List[List[int]]) -> List[List[int]]:\n        intervals.sort(key=lambda iv: iv[0])\n        merged = []\n        for s, e in intervals:\n            if not merged or s > merged[-1][1]:\n                merged.append([s, e])\n            else:\n                merged[-1][1] = max(merged[-1][1], e)\n        return merged\n",
                        "harness_py": "_dsa_run_tests([\n    ('Sample 1: Multi Merge', '[[1,3],[2,6],[8,10],[15,18]]', lambda: Solution().merge([[1,3],[2,6],[8,10],[15,18]]), [[1,6],[8,10],[15,18]]),\n    ('Sample 2: Touching Edges', '[[1,4],[4,5]]', lambda: Solution().merge([[1,4],[4,5]]), [[1,5]]),\n    ('Edge: Enclosed Interval', '[[1,4],[2,3]]', lambda: Solution().merge([[1,4],[2,3]]), [[1,4]]),\n    ('Edge: Unsorted Single Chain', '[[4,5],[1,2],[2,4]]', lambda: Solution().merge([[4,5],[1,2],[2,4]]), [[1,5]]),\n    ('Edge: Single Interval', '[[5,9]]', lambda: Solution().merge([[5,9]]), [[5,9]]),\n], sample_only=__DSA_SAMPLE_ONLY__, n_samples=2)",
                        "starter_cpp": "class Solution {\npublic:\n    vector<vector<int>> merge(vector<vector<int>>& intervals) {\n        // TODO: O(N log N) interval merge\n        return {};\n    }\n};\n",
                        "solution_cpp": "class Solution {\npublic:\n    vector<vector<int>> merge(vector<vector<int>>& intervals) {\n        sort(intervals.begin(), intervals.end());\n        vector<vector<int>> merged;\n        for (const auto& iv : intervals) {\n            if (merged.empty() || iv[0] > merged.back()[1]) {\n                merged.push_back(iv);\n            } else {\n                merged.back()[1] = max(merged.back()[1], iv[1]);\n            }\n        }\n        return merged;\n    }\n};\n",
                        "harness_cpp": "int main() {\n    ostringstream _dbg; streambuf* _old = cout.rdbuf(_dbg.rdbuf());\n    vector<_DSACaseOut> _res;\n    struct T { string name, inp; vector<vector<int>> iv, exp; };\n    vector<T> tests = {\n        {\"Sample 1: Multi Merge\", \"[[1,3],[2,6],[8,10],[15,18]]\", {{1,3},{2,6},{8,10},{15,18}}, {{1,6},{8,10},{15,18}}},\n        {\"Sample 2: Touching Edges\", \"[[1,4],[4,5]]\", {{1,4},{4,5}}, {{1,5}}},\n        {\"Edge: Enclosed Interval\", \"[[1,4],[2,3]]\", {{1,4},{2,3}}, {{1,4}}},\n        {\"Edge: Unsorted Chain\", \"[[4,5],[1,2],[2,4]]\", {{4,5},{1,2},{2,4}}, {{1,5}}},\n        {\"Edge: Single Interval\", \"[[5,9]]\", {{5,9}}, {{5,9}}}\n    };\n    int lim = DSA_SAMPLE_ONLY ? 2 : (int)tests.size();\n    Solution sol;\n    for (int i = 0; i < lim; ++i) {\n        auto v = tests[i].iv;\n        auto t0 = chrono::steady_clock::now();\n        auto act = sol.merge(v);\n        double ms = chrono::duration<double, milli>(chrono::steady_clock::now() - t0).count();\n        _res.push_back({tests[i].name, tests[i].inp, _dsa_fmt(tests[i].exp), _dsa_fmt(act), \"\", act == tests[i].exp, ms});\n    }\n    cout.rdbuf(_old);\n    _dsa_emit_json(_res, _dbg.str());\n    return 0;\n}"
                    }
                ]
            },
            {
                "title": "Module 4: Coding Lab II — Count Inversions (Coding Ninjas / Striver Classic)",
                "blocks": [
                    {
                        "type": "dsa_problem",
                        "title": "Count Inversions in an Array",
                        "platform_style": "Coding Ninjas Code360 • Striver A2Z Divide & Conquer",
                        "difficulty": "Hard",
                        "pattern": "Modified Merge Sort",
                        "target_time": "O(N log N)",
                        "target_space": "O(N)",
                        "statement": "Given an integer array `nums` of length `n`, return the **total number of inversions** in the array.\n\nTwo elements form an inversion if `i < j` and `nums[i] > nums[j]` (strictly greater!). Notice answers for large reverse-sorted arrays can exceed 32-bit ints, so return 64-bit `long long` in C++.",
                        "examples": [
                            {"input": "nums = [2, 4, 1, 3, 5]", "output": "3", "explanation": "Inversions are (2,1), (4,1), (4,3)."},
                            {"input": "nums = [5, 4, 3, 2, 1]", "output": "10", "explanation": "Strictly descending order creates every C(5,2) = 10 pairs."}
                        ],
                        "constraints": [
                            "$1 \\le \\text{nums.length} \\le 10^5$",
                            "$-10^9 \\le \\text{nums}[i] \\le 10^9$"
                        ],
                        "approach_ladder": {
                            "brute": "Nested loop `i < j` counting `nums[i] > nums[j]`: $O(N^2)$ time -> TLE.",
                            "optimal": "Divide `[l..r]` at `mid`. Recursively accumulate left & right inversions, then merge sorted halves. Whenever `tmp_left <= nums[j]`, advance `i`; whenever `nums[i] > nums[j]`, add **`mid - i + 1`** inversions and advance `j`! **$O(N \\log N)$ time, $O(N)$ space**."
                        },
                        "dry_run": "`[2, 4, 1, 3, 5]`: left `[2, 4]` (0 inv), right `[1, 3, 5]` (0 inv). Merge: `1 < 2` (+2: `(2,1),(4,1)`), `2 <= 3` (+0), `3 < 4` (+1: `(4,3)`), `4 <= 5`, `5`. Total = **3**.",
                        "edge_cases": [
                            {"title": "Duplicates Must NOT Count", "desc": "`[2, 2, 2]` has **0** inversions -> condition is `left <= right`, not `<`!"},
                            {"title": "64-bit Accumulator in C++", "desc": "Use `long long` for return type and internal counts."}
                        ],
                        "follow_ups": "**LC-493 Reverse Pairs (`nums[i] > 2 * nums[j]`):** Count cross-pairs in a separate linear two-pointer sweep BEFORE performing the normal merge step!",
                        "hint": "During merge sort, whenever `arr[i] > arr[j]` from sorted left and right halves, ALL `mid - i + 1` elements from `i..mid` are > `arr[j]`.",
                        "starter_py": "class Solution:\n    def countInversions(self, nums: List[int]) -> int:\n        # TODO: Return total (i < j, nums[i] > nums[j]) in O(N log N)\n        return 0\n",
                        "solution_py": "class Solution:\n    def countInversions(self, nums: List[int]) -> int:\n        arr = list(nums)\n        tmp = [0] * len(arr)\n        def sort_count(l: int, r: int) -> int:\n            if l >= r:\n                return 0\n            mid = (l + r) // 2\n            inv = sort_count(l, mid) + sort_count(mid + 1, r)\n            i, j, k = l, mid + 1, l\n            while i <= mid and j <= r:\n                if arr[i] <= arr[j]:\n                    tmp[k] = arr[i]; i += 1\n                else:\n                    inv += (mid - i + 1)\n                    tmp[k] = arr[j]; j += 1\n                k += 1\n            while i <= mid:\n                tmp[k] = arr[i]; i += 1; k += 1\n            while j <= r:\n                tmp[k] = arr[j]; j += 1; k += 1\n            arr[l:r+1] = tmp[l:r+1]\n            return inv\n        return sort_count(0, len(arr) - 1)\n",
                        "harness_py": "_dsa_run_tests([\n    ('Sample 1: Standard Mix', '[2,4,1,3,5]', lambda: Solution().countInversions([2,4,1,3,5]), 3),\n    ('Sample 2: Reverse Sorted', '[5,4,3,2,1]', lambda: Solution().countInversions([5,4,3,2,1]), 10),\n    ('Edge: Already Sorted', '[1,2,3,4,5]', lambda: Solution().countInversions([1,2,3,4,5]), 0),\n    ('Edge: Equal Elements', '[2,2,2,2]', lambda: Solution().countInversions([2,2,2,2]), 0),\n    ('Edge: Single Element', '[9]', lambda: Solution().countInversions([9]), 0),\n], sample_only=__DSA_SAMPLE_ONLY__, n_samples=2)",
                        "starter_cpp": "class Solution {\npublic:\n    long long countInversions(vector<int>& nums) {\n        // TODO: Modified merge sort returning long long\n        return 0;\n    }\n};\n",
                        "solution_cpp": "class Solution {\n    long long mergeCount(vector<int>& a, vector<int>& tmp, int l, int mid, int r) {\n        int i = l, j = mid + 1, k = l;\n        long long inv = 0;\n        while (i <= mid && j <= r) {\n            if (a[i] <= a[j]) tmp[k++] = a[i++];\n            else { inv += (mid - i + 1); tmp[k++] = a[j++]; }\n        }\n        while (i <= mid) tmp[k++] = a[i++];\n        while (j <= r) tmp[k++] = a[j++];\n        for (int p = l; p <= r; ++p) a[p] = tmp[p];\n        return inv;\n    }\n    long long sortCount(vector<int>& a, vector<int>& tmp, int l, int r) {\n        if (l >= r) return 0;\n        int mid = l + (r - l) / 2;\n        long long inv = sortCount(a, tmp, l, mid) + sortCount(a, tmp, mid + 1, r);\n        return inv + mergeCount(a, tmp, l, mid, r);\n    }\npublic:\n    long long countInversions(vector<int>& nums) {\n        vector<int> a = nums, tmp(nums.size());\n        return sortCount(a, tmp, 0, (int)a.size() - 1);\n    }\n};\n",
                        "harness_cpp": "int main() {\n    ostringstream _dbg; streambuf* _old = cout.rdbuf(_dbg.rdbuf());\n    vector<_DSACaseOut> _res;\n    struct T { string name, inp; vector<int> arr; long long exp; };\n    vector<T> tests = {\n        {\"Sample 1: Standard Mix\", \"[2,4,1,3,5]\", {2,4,1,3,5}, 3},\n        {\"Sample 2: Reverse Sorted\", \"[5,4,3,2,1]\", {5,4,3,2,1}, 10},\n        {\"Edge: Already Sorted\", \"[1,2,3,4,5]\", {1,2,3,4,5}, 0},\n        {\"Edge: Equal Elements\", \"[2,2,2,2]\", {2,2,2,2}, 0},\n        {\"Edge: Single Element\", \"[9]\", {9}, 0}\n    };\n    int lim = DSA_SAMPLE_ONLY ? 2 : (int)tests.size();\n    Solution sol;\n    for (int i = 0; i < lim; ++i) {\n        auto v = tests[i].arr;\n        auto t0 = chrono::steady_clock::now();\n        long long act = sol.countInversions(v);\n        double ms = chrono::duration<double, milli>(chrono::steady_clock::now() - t0).count();\n        _res.push_back({tests[i].name, tests[i].inp, _dsa_fmt(tests[i].exp), _dsa_fmt(act), \"\", act == tests[i].exp, ms});\n    }\n    cout.rdbuf(_old);\n    _dsa_emit_json(_res, _dbg.str());\n    return 0;\n}"
                    }
                ]
            }
        ]
    },
    "6": {
        "title": "Case 06: The Monotonic Oracle — Binary Search & Answer Space",
        "episodes": [
            {
                "title": "Module 1: Loop Invariants, Bounds & Binary Search on Answer",
                "blocks": [
                    {
                        "type": "story",
                        "title": "Infinite Loops at `lo == hi`",
                        "content": "Even Jon Bentley noted that 90% of professional programmers wrote buggy binary searches when tested cold—usually off-by-one infinite loops at `lo = mid` or overflow at `(lo + hi) / 2`.\n\n> [!IMPORTANT]\n> Binary Search applies to **ANY monotonic predicate $P(x)$** of form `F, F, ..., F, T, T, ..., T` — not just sorted index arrays!"
                    },
                    {
                        "type": "concept",
                        "title": "Exact Bounds & Search-Space Template",
                        "content": "1. **Lower Bound (`first x >= target`):** Maintain `lo = 0, hi = n - 1, ans = n`:\n   - If `nums[mid] >= target`: record `ans = mid`, search left `hi = mid - 1`.\n   - Else: `lo = mid + 1`.\n2. **Overflow-Free Midpoint:** Compute **`mid = lo + (hi - lo) // 2`** because when `lo = 1.5e9, hi = 2e9`, `lo + hi = 3.5e9` overflows 32-bit signed `int`!\n3. **Binary Search on Answer (`Minimize Max` / `Maximize Min`):** If `canFinish(speed)` is True for speed `k`, it is guaranteed True for all `k' > k`! Define search range `[1, max(piles)]`, test `feasible(mid)`, and binary search the leftmost `True` boundary in $O(N \\log(\\text{Range}))$!",
                        "technical_explanation": "**Rotated Sorted Array Key Insight:** Whenever a strictly distinct sorted array is rotated at an unknown pivot, cutting at `mid` **guarantees at least ONE half** (`[lo..mid]` OR `[mid..hi]`) is completely sorted! Compare `nums[lo] <= nums[mid]` (`<=` is vital when `lo == mid` on a 2-element slice!) to identify which half is sorted, then check if `target` lies inside that sorted bracket."
                    },
                    {
                        "type": "visual",
                        "title": "Monotonic Feasibility Boundary (BS on Answer)",
                        "code": "graph LR\n  A[\"k=1: False\"] --> B[\"k=2: False\"] --> C[\"k=3: False\"] --> D[\"k=4: TRUE (Optimal Min!)\"] --> E[\"k=5: True\"]\n  style D fill:#065f46,stroke:#10b981,stroke-width:2px"
                    },
                    {
                        "type": "interactive",
                        "title": "Binary Search Template Trap",
                        "question": "Suppose `lo = 2, hi = 3`, `mid = (lo + hi) // 2 = 2`. Under condition `while lo < hi`, which branch causes an INFINITE LOOP?",
                        "options": [
                            "lo = mid + 1; hi = mid;",
                            "hi = mid - 1; lo = mid;",
                            "lo = mid + 1; hi = mid - 1;",
                            "lo += 1; hi -= 1;"
                        ],
                        "answer": 1,
                        "explanation": "With floor midpoint `mid = (lo + hi) // 2`, when `lo + 1 == hi` (`2, 3`), `mid == lo == 2`! Setting `lo = mid` leaves `lo = 2, hi = 3` **unchanged forever**! Always pair floor `mid` with `lo = mid + 1, hi = mid`, OR use ceiling `(lo + hi + 1) // 2` when updating `lo = mid`."
                    }
                ]
            },
            {
                "title": "Module 2: Overflow Traps & Search Space Bounds",
                "blocks": [
                    {
                        "type": "wrong_approach",
                        "title": "32-bit Sum Overflow in Feasible Check",
                        "language": "cpp",
                        "code": "int hours = 0;\nfor (int p : piles) hours += (p + k - 1) / k; // OVERFLOWS if total hours > 2.14e9!\nreturn hours <= h;",
                        "explanation": "If `10^4` piles each have size `10^9` and `k = 1`, `hours` reaches `10^13`—overflowing `int` into negative numbers and falsely passing `hours <= h`! Always accumulate `long long hours`."
                    },
                    {
                        "type": "correct_approach",
                        "title": "Safe 64-bit Ceiling Division with Early Break",
                        "language": "cpp",
                        "code": "long long hours = 0;\nfor (int p : piles) {\n    hours += (p + k - 1LL) / k;\n    if (hours > h) return false;\n}\nreturn true;",
                        "explanation": "Integer ceiling division `(p + k - 1) / k` avoids floating-point inaccuracy, uses 64-bit arithmetic, and short-circuits immediately once `hours > h`."
                    },
                    {
                        "type": "calculation_challenge",
                        "title": "Aggressive Cows / Answer Space Steps",
                        "formula": "Maximum search space value is $10^9$ and each feasibility check scans $N = 10^5$ elements.",
                        "problem": "At most how many times is `feasible(mid)` called by Binary Search on $[1, 10^9]$?",
                        "answer": "30",
                        "alternatives": ["30", "31"],
                        "step_by_step": "$\\lceil \\log_2(10^9) \\rceil = 30$ iterations, costing $30 \\times 10^5 = 3 \\times 10^6$ fast scalar operations total!"
                    }
                ]
            },
            {
                "title": "Module 3: Coding Lab I — Search in Rotated Sorted Array (LC-33)",
                "blocks": [
                    {
                        "type": "dsa_problem",
                        "title": "Search in Rotated Sorted Array",
                        "platform_style": "LeetCode 33 • Coding Ninjas Binary Search Classic",
                        "difficulty": "Medium",
                        "pattern": "Modified Binary Search (Sorted-Half Identification)",
                        "target_time": "O(log N)",
                        "target_space": "O(1)",
                        "statement": "An integer array `nums` sorted in ascending order with **distinct** values was rotated at an unknown pivot before being passed to you.\n\nGiven `nums` and an integer `target`, return the index of `target` if it is in `nums`, or `-1` if it is not in `nums` in **$O(\\log N)$ runtime**.",
                        "examples": [
                            {"input": "nums = [4,5,6,7,0,1,2], target = 0", "output": "4", "explanation": "7 -> 0 pivot rotated left; 0 sits at index 4."},
                            {"input": "nums = [4,5,6,7,0,1,2], target = 3", "output": "-1", "explanation": "3 is absent."}
                        ],
                        "constraints": [
                            "$1 \\le \\text{nums.length} \\le 5000$",
                            "$-10^4 \\le \\text{nums}[i], \\text{target} \\le 10^4$",
                            "All values in `nums` are unique."
                        ],
                        "approach_ladder": {
                            "brute": "Linear scan in $O(N)$ fails the strict $O(\\log N)$ requirement.",
                            "better": "1) Binary search pivot index, 2) Binary search chosen half (2 binary searches).",
                            "optimal": "Single Binary Search (`lo <= hi`): if `nums[mid] == target`, return `mid`. If **`nums[lo] <= nums[mid]`** (left half sorted): check `nums[lo] <= target < nums[mid]` to set `hi = mid - 1` else `lo = mid + 1`. Otherwise right half is sorted: check `nums[mid] < target <= nums[hi]`! **$O(\\log N)$ time, $O(1)$ space**."
                        },
                        "dry_run": "`[3, 1], target = 1`: `lo=0(3), hi=1(1), mid=0(3)`. Since `nums[lo] <= nums[mid]` (`3 <= 3` — notice `<=`!), left `[3]` is sorted; `1` is not in `[3, 3)`, so `lo = 1`. Next `mid = 1`, `nums[1] == 1` -> return **1**.",
                        "edge_cases": [
                            {"title": "Two Elements [3, 1] (`nums[lo] == nums[mid]`)", "desc": "MUST write `nums[lo] <= nums[mid]` (NOT strict `<`!) so `lo == mid` classifies left as sorted and moves `lo = mid + 1`!"}
                        ],
                        "follow_ups": "**LC-81 (With Duplicates):** When `nums[lo] == nums[mid] == nums[hi]`, shrink `lo += 1; hi -= 1;` before continuing (worst-case degrades to $O(N)$ on `[1,1,1,2,1]`).",
                        "hint": "Use `nums[lo] <= nums[mid]` to identify the guaranteed-sorted half, then check whether `target` sits within its endpoints.",
                        "starter_py": "class Solution:\n    def search(self, nums: List[int], target: int) -> int:\n        # TODO: Single-pass O(log N) rotated binary search\n        return -1\n",
                        "solution_py": "class Solution:\n    def search(self, nums: List[int], target: int) -> int:\n        lo, hi = 0, len(nums) - 1\n        while lo <= hi:\n            mid = lo + (hi - lo) // 2\n            if nums[mid] == target:\n                return mid\n            if nums[lo] <= nums[mid]:\n                if nums[lo] <= target < nums[mid]:\n                    hi = mid - 1\n                else:\n                    lo = mid + 1\n            else:\n                if nums[mid] < target <= nums[hi]:\n                    lo = mid + 1\n                else:\n                    hi = mid - 1\n        return -1\n",
                        "harness_py": "_dsa_run_tests([\n    ('Sample 1: Found at 4', '[4,5,6,7,0,1,2], t=0', lambda: Solution().search([4,5,6,7,0,1,2], 0), 4),\n    ('Sample 2: Missing', '[4,5,6,7,0,1,2], t=3', lambda: Solution().search([4,5,6,7,0,1,2], 3), -1),\n    ('Edge: Two Elements Lo==Mid', '[3,1], t=1', lambda: Solution().search([3,1], 1), 1),\n    ('Edge: Single Element', '[1], t=0', lambda: Solution().search([1], 0), -1),\n    ('Edge: Unrotated Target First', '[1,3,5,7,9], t=1', lambda: Solution().search([1,3,5,7,9], 1), 0),\n], sample_only=__DSA_SAMPLE_ONLY__, n_samples=2)",
                        "starter_cpp": "class Solution {\npublic:\n    int search(vector<int>& nums, int target) {\n        // TODO: O(log N) rotated binary search\n        return -1;\n    }\n};\n",
                        "solution_cpp": "class Solution {\npublic:\n    int search(vector<int>& nums, int target) {\n        int lo = 0, hi = (int)nums.size() - 1;\n        while (lo <= hi) {\n            int mid = lo + (hi - lo) / 2;\n            if (nums[mid] == target) return mid;\n            if (nums[lo] <= nums[mid]) {\n                if (nums[lo] <= target && target < nums[mid]) hi = mid - 1;\n                else lo = mid + 1;\n            } else {\n                if (nums[mid] < target && target <= nums[hi]) lo = mid + 1;\n                else hi = mid - 1;\n            }\n        }\n        return -1;\n    }\n};\n",
                        "harness_cpp": "int main() {\n    ostringstream _dbg; streambuf* _old = cout.rdbuf(_dbg.rdbuf());\n    vector<_DSACaseOut> _res;\n    struct T { string name, inp; vector<int> arr; int target, exp; };\n    vector<T> tests = {\n        {\"Sample 1: Found at 4\", \"[4,5,6,7,0,1,2], t=0\", {4,5,6,7,0,1,2}, 0, 4},\n        {\"Sample 2: Missing\", \"[4,5,6,7,0,1,2], t=3\", {4,5,6,7,0,1,2}, 3, -1},\n        {\"Edge: Two Elements Lo==Mid\", \"[3,1], t=1\", {3,1}, 1, 1},\n        {\"Edge: Single Element\", \"[1], t=0\", {1}, 0, -1},\n        {\"Edge: Unrotated\", \"[1,3,5,7,9], t=1\", {1,3,5,7,9}, 1, 0}\n    };\n    int lim = DSA_SAMPLE_ONLY ? 2 : (int)tests.size();\n    Solution sol;\n    for (int i = 0; i < lim; ++i) {\n        auto v = tests[i].arr;\n        auto t0 = chrono::steady_clock::now();\n        int act = sol.search(v, tests[i].target);\n        double ms = chrono::duration<double, milli>(chrono::steady_clock::now() - t0).count();\n        _res.push_back({tests[i].name, tests[i].inp, _dsa_fmt(tests[i].exp), _dsa_fmt(act), \"\", act == tests[i].exp, ms});\n    }\n    cout.rdbuf(_old);\n    _dsa_emit_json(_res, _dbg.str());\n    return 0;\n}"
                    }
                ]
            },
            {
                "title": "Module 4: Coding Lab II — Koko Eating Bananas / BS on Answer (LC-875)",
                "blocks": [
                    {
                        "type": "dsa_problem",
                        "title": "Koko Eating Bananas (Binary Search on Answer)",
                        "platform_style": "LeetCode 875 • Coding Ninjas Answer-Space Template",
                        "difficulty": "Medium",
                        "pattern": "Binary Search on Monotonic Feasibility Answer",
                        "target_time": "O(N log max(piles))",
                        "target_space": "O(1)",
                        "statement": "Koko loves to eat bananas. There are `n` piles of bananas, the $i$-th pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.\n\nKoko can decide her bananas-per-hour eating speed `k`. Each hour, she chooses one pile and eats `k` bananas from it (if the pile has fewer than `k`, she eats all of them and waits for the next hour). Return the **minimum integer `k`** such that she can eat all bananas within `h` hours.",
                        "examples": [
                            {"input": "piles = [3, 6, 7, 11], h = 8", "output": "4", "explanation": "At k=4: ceil(3/4)+ceil(6/4)+ceil(7/4)+ceil(11/4) = 1+2+2+3 = 8 <= 8. At k=3, total = 10 > 8."},
                            {"input": "piles = [30, 11, 23, 4, 20], h = 5", "output": "30", "explanation": "With h == len(piles), she must finish max(piles) per hour."}
                        ],
                        "constraints": [
                            "$1 \\le \\text{piles.length} \\le 10^4$",
                            "$\\text{piles.length} \\le h \\le 10^9$",
                            "$1 \\le \\text{piles}[i] \\le 10^9$"
                        ],
                        "approach_ladder": {
                            "brute": "Try `k = 1, 2, 3, ...` linearly until hours <= `h`. For `piles = [10^9], h = 2`, takes $5 \\times 10^8$ steps -> **TLE**.",
                            "optimal": "Binary search `k` over `[lo = 1, hi = max(piles)]`. Define `canEatAll(k)` returning `sum((p + k - 1) // k) <= h`. If `canEatAll(mid)` is True, record `ans = mid` and try smaller `hi = mid - 1`; else `lo = mid + 1`. **$O(N \\log(\\max p))$ time, $O(1)$ space**."
                        },
                        "dry_run": "`[3, 6, 7, 11], h = 8`: `lo=1, hi=11 -> mid=6` (hours=6<=8 -> `hi=5`) -> `mid=3` (hours=10>8 -> `lo=4`) -> `mid=4` (hours=8<=8 -> `hi=3`) -> stop, return `lo = 4`.",
                        "edge_cases": [
                            {"title": "Large Pile Values ($10^9$) in C++", "desc": "`sum((p + k - 1LL) / k)` exceeds 32-bit `int`! Use `long long` for hour sum and `(p + k - 1LL)`!"}
                        ],
                        "follow_ups": "Same exact Answer-Space template solves **LC-1011 Capacity To Ship Packages Within D Days**, **LC-410 Split Array Largest Sum**, and **Coding Ninjas Allocate Minimum Pages / Aggressive Cows**!",
                        "hint": "Search speed `k` between `1` and `max(piles)`. Use integer ceil `(p + k - 1) // k` with `long long` in C++.",
                        "starter_py": "class Solution:\n    def minEatingSpeed(self, piles: List[int], h: int) -> int:\n        # TODO: Binary search k in [1, max(piles)]\n        return 0\n",
                        "solution_py": "class Solution:\n    def minEatingSpeed(self, piles: List[int], h: int) -> int:\n        lo, hi = 1, max(piles)\n        while lo < hi:\n            mid = lo + (hi - lo) // 2\n            hours = sum((p + mid - 1) // mid for p in piles)\n            if hours <= h:\n                hi = mid\n            else:\n                lo = mid + 1\n        return lo\n",
                        "harness_py": "_dsa_run_tests([\n    ('Sample 1: h=8', '[3,6,7,11], h=8', lambda: Solution().minEatingSpeed([3,6,7,11], 8), 4),\n    ('Sample 2: h==N Strict', '[30,11,23,4,20], h=5', lambda: Solution().minEatingSpeed([30,11,23,4,20], 5), 30),\n    ('Edge: Loose h=6', '[30,11,23,4,20], h=6', lambda: Solution().minEatingSpeed([30,11,23,4,20], 6), 23),\n    ('Edge: Large Piles Overflow Check', '[805306368,805306368,805306368], h=1000000000', lambda: Solution().minEatingSpeed([805306368,805306368,805306368], 1000000000), 3),\n    ('Edge: Single Pile Exact Split', '[100], h=7', lambda: Solution().minEatingSpeed([100], 7), 15),\n], sample_only=__DSA_SAMPLE_ONLY__, n_samples=2)",
                        "starter_cpp": "class Solution {\npublic:\n    int minEatingSpeed(vector<int>& piles, int h) {\n        // TODO: Use long long for hour sum!\n        return 0;\n    }\n};\n",
                        "solution_cpp": "class Solution {\npublic:\n    int minEatingSpeed(vector<int>& piles, int h) {\n        int lo = 1, hi = *max_element(piles.begin(), piles.end());\n        while (lo < hi) {\n            int mid = lo + (hi - lo) / 2;\n            long long hours = 0;\n            for (int p : piles) hours += (p + (long long)mid - 1) / mid;\n            if (hours <= h) hi = mid;\n            else lo = mid + 1;\n        }\n        return lo;\n    }\n};\n",
                        "harness_cpp": "int main() {\n    ostringstream _dbg; streambuf* _old = cout.rdbuf(_dbg.rdbuf());\n    vector<_DSACaseOut> _res;\n    struct T { string name, inp; vector<int> arr; int h, exp; };\n    vector<T> tests = {\n        {\"Sample 1: h=8\", \"[3,6,7,11], h=8\", {3,6,7,11}, 8, 4},\n        {\"Sample 2: h==N Strict\", \"[30,11,23,4,20], h=5\", {30,11,23,4,20}, 5, 30},\n        {\"Edge: Loose h=6\", \"[30,11,23,4,20], h=6\", {30,11,23,4,20}, 6, 23},\n        {\"Edge: Large Piles Overflow\", \"[805306368x3], h=1e9\", {805306368,805306368,805306368}, 1000000000, 3},\n        {\"Edge: Single Pile\", \"[100], h=7\", {100}, 7, 15}\n    };\n    int lim = DSA_SAMPLE_ONLY ? 2 : (int)tests.size();\n    Solution sol;\n    for (int i = 0; i < lim; ++i) {\n        auto v = tests[i].arr;\n        auto t0 = chrono::steady_clock::now();\n        int act = sol.minEatingSpeed(v, tests[i].h);\n        double ms = chrono::duration<double, milli>(chrono::steady_clock::now() - t0).count();\n        _res.push_back({tests[i].name, tests[i].inp, _dsa_fmt(tests[i].exp), _dsa_fmt(act), \"\", act == tests[i].exp, ms});\n    }\n    cout.rdbuf(_old);\n    _dsa_emit_json(_res, _dbg.str());\n    return 0;\n}"
                    }
                ]
            }
        ]
    },
    "7": {
        "title": "Case 07: Text Engine — String Pooling, Palindromes & KMP",
        "episodes": [
            {
                "title": "Module 1: String Immutability, Rolling Hash & KMP Failure Function",
                "blocks": [
                    {
                        "type": "story",
                        "title": "The Quadratic Log Scrubber",
                        "content": "A regex replacement filter copied immutable strings repeatedly in a loop (`res = res + ch`), turning 100 KB logs into gigabytes of heap garbage. Meanwhile, naive `str.find` suffered $O(N \\cdot M)$ worst-case backtracking on repetitive payloads (`\"aaaaaaab\"`).\n\n> [!TIP]\n> Build strings with mutable buffers (`list.append` + `\"\".join` or C++ `string::push_back`) and search patterns in guaranteed linear $O(N + M)$ using **KMP's LPS failure table**!"
                    },
                    {
                        "type": "concept",
                        "title": "KMP Prefix Function (LPS) & Expand-Around-Center Symmetry",
                        "content": "1. **KMP LPS Array (`lps[i]`):** Length of the longest *proper prefix* of `pat[0..i]` that is also a *suffix* of `pat[0..i]`. On a mismatch at `pat[j]`, instead of resetting `i` backward in `text`, set **`j = lps[j - 1]`**!\n   - **Amortized $O(N + M)$ Proof:** `j` increases by `+1` at most $N$ times total, and each fallback `j = lps[j - 1]` strictly decreases `j >= 0`, bounding total fallbacks by $N$!\n2. **Rabin-Karp Rolling Hash:** Hash window $H(s[i..i+M-1])$ as a base-$B$ polynomial modulo prime $P$ ($10^9+7$). Slide window right in $O(1)$ by subtracting top digit and adding new trailing digit. Verify actual substring equality on hash match to handle rare collisions.\n3. **Palindromes (Expand Around Center):** Any palindrome of length $L$ has a center at 1 character (`N` odd centers) OR between 2 adjacent characters (`N-1` even centers), solving Longest Palindromic Substring cleanly in **$O(N^2)$ time, $O(1)$ space**!",
                        "technical_explanation": "**Group Anagrams Key Speedup:** Sorting each word of length $K$ costs $O(K \\log K)$, making grouping $N$ strings take $O(N K \\log K)$. Mapping each word to a 26-int frequency tuple `(c0, c1, ..., c25)` runs in optimal **$O(N \\cdot K)$**!"
                    },
                    {
                        "type": "visual",
                        "title": "KMP LPS Failure Jump Avoids Text Backtracking",
                        "code": "flowchart LR\n  M[\"Mismatch: text[i] != pat[j]\"] --> J{\"j > 0?\"}\n  J -->|Yes| FALL[\"Jump j = lps[j - 1] (Keep i stationary!)\"]\n  J -->|No| ADV[\"No prefix overlap: advance i += 1\"]"
                    },
                    {
                        "type": "calculation_challenge",
                        "title": "Compute KMP LPS Array Final Entry",
                        "formula": "For `pat = \"ababa\"` (indices `0..4`), `lps[i]` is the length of the longest proper prefix matching a suffix of `pat[0..i]` (`lps = [0, 0, 1, 2, ?]`).",
                        "problem": "What is `lps[4]` for `\"ababa\"`?",
                        "answer": "3",
                        "alternatives": ["3"],
                        "step_by_step": "Proper prefixes of `\"ababa\"`: `\"a\"`, `\"ab\"`, **`\"aba\"`** (`len=3`), `\"abab\"`. Suffixes: `\"a\"`, `\"ba\"`, **`\"aba\"`**, `\"baba\"`. Longest match is `\"aba\"` of length **3**."
                    }
                ]
            },
            {
                "title": "Module 2: Palindrome Centers & String Concatenation Pitfalls",
                "blocks": [
                    {
                        "type": "comparison_table",
                        "title": "Substring Pattern Matching Algorithms",
                        "headers": ["Algorithm", "Preprocessing", "Query Time", "Worst-Case Guarantee", "Extra Space"],
                        "rows": [
                            ["Naive Sliding Check", "O(1)", "O(N * M)", "O(N * M) on 'aaa...b'", "O(1)"],
                            ["KMP (Knuth-Morris-Pratt)", "O(M)", "O(N + M)", "Strict O(N + M)", "O(M)"],
                            ["Rabin-Karp (Rolling Hash)", "O(M)", "O(N + M) Expected", "O(N * M) on collisions", "O(1) (great for multi-pattern!)"],
                            ["Z-Algorithm", "O(N + M)", "O(N + M)", "Strict O(N + M)", "O(N + M)"]
                        ]
                    },
                    {
                        "type": "interactive",
                        "title": "Palindrome Centers Count Check",
                        "question": "A string `s` has length `n = 100`. How many total palindrome centers (odd + even) must Expand-Around-Center test?",
                        "options": [
                            "100 centers",
                            "199 centers (100 odd centers + 99 between-character even centers)",
                            "200 centers",
                            "10,000 centers"
                        ],
                        "answer": 1,
                        "explanation": "Odd palindromes center on each of the `n` characters; even palindromes center between each of the `n - 1` adjacent pairs -> `2n - 1 = 199` centers."
                    }
                ]
            },
            {
                "title": "Module 3: Coding Lab I — Group Anagrams (LC-49)",
                "blocks": [
                    {
                        "type": "dsa_problem",
                        "title": "Group Anagrams",
                        "platform_style": "LeetCode 49 • Coding Ninjas Hashing & Strings",
                        "difficulty": "Medium",
                        "pattern": "Canonical Signature Hashing (26-Freq / Sorted Key)",
                        "target_time": "O(N * K)",
                        "target_space": "O(N * K)",
                        "statement": "Given an array of strings `strs`, group the **anagrams** together. You can return the answer in **any order** (groups and elements inside each group may appear in any order).",
                        "examples": [
                            {"input": "strs = [\"eat\",\"tea\",\"tan\",\"ate\",\"nat\",\"bat\"]", "output": "[[\"bat\"],[\"nat\",\"tan\"],[\"ate\",\"eat\",\"tea\"]]", "explanation": "'eat', 'tea', 'ate' share character multiset {a:1, e:1, t:1}."},
                            {"input": "strs = [\"\"]", "output": "[[\"\"]]", "explanation": "Single empty string forms one group."}
                        ],
                        "constraints": [
                            "$1 \\le \\text{strs.length} \\le 10^4$",
                            "$0 \\le \\text{strs}[i].\\text{length} \\le 100$",
                            "`strs[i]` consists of lowercase English letters."
                        ],
                        "approach_ladder": {
                            "brute": "Compare every string pair via character counts: $O(N^2 \\cdot K)$.",
                            "better": "Sort characters of each string `sorted(s)` as dictionary key: $O(N \\cdot K \\log K)$.",
                            "optimal": "Build a 26-element count tuple (Python) or delimited count key (or fast `sorted(s)` since $K \\le 100$!) as dictionary key, appending original string to `groups[key]`. **$O(N \\cdot K)$**."
                        },
                        "dry_run": "`\"eat\" -> (1,0,0,0,1,...,1,...)`, `\"tea\"` maps to the exact same key -> appended to the same bucket!",
                        "edge_cases": [
                            {"title": "Empty Strings & Duplicate Inputs", "desc": "`[\"\", \"\"]` must remain ONE group containing TWO empty strings `[\"\", \"\"]`."}
                        ],
                        "follow_ups": "**Delimiter Trap in C++:** Never encode counts `[1, 12]` as `\"112\"` without a `#` separator — `\"1#12\"` prevents colliding `[1, 12]` with `[11, 2]`!",
                        "hint": "Use character-count tuple (or sorted copy) as the hash key, NOT a concatenated count without delimiters.",
                        "starter_py": "class Solution:\n    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:\n        # TODO: Return grouped anagram lists\n        return []\n",
                        "solution_py": "class Solution:\n    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:\n        groups = defaultdict(list)\n        for s in strs:\n            cnt = [0] * 26\n            for ch in s:\n                cnt[ord(ch) - 97] += 1\n            groups[tuple(cnt)].append(s)\n        return list(groups.values())\n",
                        "harness_py": "_norm = lambda g: sorted([sorted(x) for x in g])\n_dsa_run_tests([\n    ('Sample 1: Multi Groups', '[\"eat\",\"tea\",\"tan\",\"ate\",\"nat\",\"bat\"]', lambda: _norm(Solution().groupAnagrams(['eat','tea','tan','ate','nat','bat'])), _norm([['bat'],['nat','tan'],['ate','eat','tea']])),\n    ('Sample 2: Empty String', '[\"\"]', lambda: _norm(Solution().groupAnagrams([''])), [['']]),\n    ('Edge: Duplicate Empty', '[\"\",\"\"]', lambda: _norm(Solution().groupAnagrams(['',''])), [['','']]),\n    ('Edge: Collision Guard bbbbbbbbbbb vs b_1_11', '[\"bdddddddddd\",\"bbbbbbbbbbc\"]', lambda: _norm(Solution().groupAnagrams(['bdddddddddd','bbbbbbbbbbc'])), _norm([['bdddddddddd'],['bbbbbbbbbbc']])),\n], sample_only=__DSA_SAMPLE_ONLY__, n_samples=2)",
                        "starter_cpp": "class Solution {\npublic:\n    vector<vector<string>> groupAnagrams(vector<string>& strs) {\n        // TODO: Group anagrams cleanly\n        return {};\n    }\n};\n",
                        "solution_cpp": "class Solution {\npublic:\n    vector<vector<string>> groupAnagrams(vector<string>& strs) {\n        unordered_map<string, vector<string>> groups;\n        for (const string& s : strs) {\n            int cnt[26] = {0};\n            for (char c : s) ++cnt[c - 'a'];\n            string key;\n            key.reserve(60);\n            for (int i = 0; i < 26; ++i) { key += '#'; key += to_string(cnt[i]); }\n            groups[key].push_back(s);\n        }\n        vector<vector<string>> res;\n        for (auto& kv : groups) res.push_back(move(kv.second));\n        return res;\n    }\n};\n",
                        "harness_cpp": "static vector<vector<string>> _norm(vector<vector<string>> g) {\n    for (auto& row : g) sort(row.begin(), row.end());\n    sort(g.begin(), g.end());\n    return g;\n}\nint main() {\n    ostringstream _dbg; streambuf* _old = cout.rdbuf(_dbg.rdbuf());\n    vector<_DSACaseOut> _res;\n    struct T { string name, inp; vector<string> s; vector<vector<string>> exp; };\n    vector<T> tests = {\n        {\"Sample 1: Multi Groups\", \"[eat,tea,tan,ate,nat,bat]\", {\"eat\",\"tea\",\"tan\",\"ate\",\"nat\",\"bat\"}, {{\"bat\"},{\"nat\",\"tan\"},{\"ate\",\"eat\",\"tea\"}}},\n        {\"Sample 2: Empty String\", \"[\\\"\\\"]\", {\"\"}, {{\"\"} }},\n        {\"Edge: Duplicate Empty\", \"[\\\"\\\",\\\"\\\"]\", {\"\",\"\"}, {{\"\",\"\"}}},\n        {\"Edge: Delimiter Collision\", \"[bdddddddddd,bbbbbbbbbbc]\", {\"bdddddddddd\",\"bbbbbbbbbbc\"}, {{\"bdddddddddd\"},{\"bbbbbbbbbbc\"}}}\n    };\n    int lim = DSA_SAMPLE_ONLY ? 2 : (int)tests.size();\n    Solution sol;\n    for (int i = 0; i < lim; ++i) {\n        auto v = tests[i].s;\n        auto t0 = chrono::steady_clock::now();\n        auto act = _norm(sol.groupAnagrams(v));\n        auto exp = _norm(tests[i].exp);\n        double ms = chrono::duration<double, milli>(chrono::steady_clock::now() - t0).count();\n        _res.push_back({tests[i].name, tests[i].inp, _dsa_fmt(exp), _dsa_fmt(act), \"\", act == exp, ms});\n    }\n    cout.rdbuf(_old);\n    _dsa_emit_json(_res, _dbg.str());\n    return 0;\n}"
                    }
                ]
            },
            {
                "title": "Module 4: Coding Lab II — Longest Palindromic Substring (LC-5)",
                "blocks": [
                    {
                        "type": "dsa_problem",
                        "title": "Longest Palindromic Substring",
                        "platform_style": "LeetCode 5 • Coding Ninjas Strings Favorite",
                        "difficulty": "Medium",
                        "pattern": "Expand Around Center (Odd + Even)",
                        "target_time": "O(N^2)",
                        "target_space": "O(1)",
                        "statement": "Given a string `s`, return the **longest palindromic contiguous substring** in `s`. If multiple answers share the maximum length (e.g., `\"bab\"` or `\"aba\"` in `\"babad\"`), returning any valid longest palindrome is accepted.",
                        "examples": [
                            {"input": "s = \"babad\"", "output": "\"bab\"", "explanation": "\"aba\" is also a valid longest palindrome of length 3."},
                            {"input": "s = \"cbbd\"", "output": "\"bb\"", "explanation": "Even-length palindrome centered between index 1 and 2."}
                        ],
                        "constraints": [
                            "$1 \\le s.\\text{length} \\le 1000$",
                            "`s` consists of only digits and English letters."
                        ],
                        "approach_ladder": {
                            "brute": "Test every substring `[i..j]` for palindrome: $O(N^3)$ -> TLE.",
                            "better": "2D Interval DP `dp[i][j] = (s[i]==s[j] and dp[i+1][j-1])`: $O(N^2)$ time and $O(N^2)$ table space.",
                            "optimal": "Expand outward `(l, r)` around every center `(i, i)` (odd) and `(i, i+1)` (even), tracking only `[best_start, best_len]`! **$O(N^2)$ time and $O(1)$ extra space** (Manacher's reaches $O(N)$, rarely required outside competitive IOI)."
                        },
                        "dry_run": "`\"cbbd\"`: center `(1, 1)` gives `\"b\"` (len 1); center `(1, 2)` expands `'b' == 'b'` -> `'c' != 'd'` -> records `start=1, len=2` (`\"bb\"`).",
                        "edge_cases": [
                            {"title": "Single Char & No Repeats", "desc": "`\"abc\"` has no multi-char palindrome -> must return a 1-character substring like `\"a\"`, never `\"\"`!"}
                        ],
                        "follow_ups": "**LC-647 Palindromic Substrings:** Count total iterations across all `2N - 1` center expansions to count every palindromic substring in $O(N^2)$ time, $O(1)$ space.",
                        "hint": "Write a helper `expand(l, r)` returning length `(r - 1) - (l + 1) + 1 = r - l - 1`, and run it at `(i, i)` and `(i, i+1)`.",
                        "starter_py": "class Solution:\n    def longestPalindrome(self, s: str) -> str:\n        # TODO: Expand Around Center in O(N^2) time, O(1) space\n        return \"\"\n",
                        "solution_py": "class Solution:\n    def longestPalindrome(self, s: str) -> str:\n        if not s:\n            return \"\"\n        start, best_len = 0, 1\n        def expand(l: int, r: int):\n            nonlocal start, best_len\n            while l >= 0 and r < len(s) and s[l] == s[r]:\n                if r - l + 1 > best_len:\n                    start = l\n                    best_len = r - l + 1\n                l -= 1; r += 1\n        for i in range(len(s)):\n            expand(i, i)\n            expand(i, i + 1)\n        return s[start : start + best_len]\n",
                        "harness_py": "_ok_pal = lambda src, got, exp_len: isinstance(got, str) and len(got) == exp_len and got in src and got == got[::-1]\n_dsa_run_tests([\n    ('Sample 1: babad', 's=\"babad\"', lambda: Solution().longestPalindrome('babad'), 'bab', lambda a, e: _ok_pal('babad', a, 3)),\n    ('Sample 2: Even Palindrome', 's=\"cbbd\"', lambda: Solution().longestPalindrome('cbbd'), 'bb', lambda a, e: _ok_pal('cbbd', a, 2)),\n    ('Edge: Single Char', 's=\"a\"', lambda: Solution().longestPalindrome('a'), 'a', lambda a, e: _ok_pal('a', a, 1)),\n    ('Edge: All Distinct', 's=\"abcd\"', lambda: Solution().longestPalindrome('abcd'), 'a', lambda a, e: _ok_pal('abcd', a, 1)),\n    ('Edge: Full String Pal', 's=\"racecar\"', lambda: Solution().longestPalindrome('racecar'), 'racecar', lambda a, e: _ok_pal('racecar', a, 7)),\n], sample_only=__DSA_SAMPLE_ONLY__, n_samples=2)",
                        "starter_cpp": "class Solution {\npublic:\n    string longestPalindrome(string s) {\n        // TODO: O(N^2) time, O(1) extra space\n        return \"\";\n    }\n};\n",
                        "solution_cpp": "class Solution {\npublic:\n    string longestPalindrome(string s) {\n        int n = (int)s.size();\n        if (n == 0) return \"\";\n        int start = 0, best_len = 1;\n        auto expand = [&](int l, int r) {\n            while (l >= 0 && r < n && s[l] == s[r]) {\n                if (r - l + 1 > best_len) { start = l; best_len = r - l + 1; }\n                --l; ++r;\n            }\n        };\n        for (int i = 0; i < n; ++i) {\n            expand(i, i);\n            expand(i, i + 1);\n        }\n        return s.substr(start, best_len);\n    }\n};\n",
                        "harness_cpp": "static bool _is_ok_pal(const string& src, const string& got, int exp_len) {\n    if ((int)got.size() != exp_len) return false;\n    if (src.find(got) == string::npos) return false;\n    string rev = got; reverse(rev.begin(), rev.end());\n    return rev == got;\n}\nint main() {\n    ostringstream _dbg; streambuf* _old = cout.rdbuf(_dbg.rdbuf());\n    vector<_DSACaseOut> _res;\n    struct T { string name, inp, s, rep; int exp_len; };\n    vector<T> tests = {\n        {\"Sample 1: babad\", \"s=babad\", \"babad\", \"bab (len 3)\", 3},\n        {\"Sample 2: Even Palindrome\", \"s=cbbd\", \"cbbd\", \"bb (len 2)\", 2},\n        {\"Edge: Single Char\", \"s=a\", \"a\", \"a (len 1)\", 1},\n        {\"Edge: All Distinct\", \"s=abcd\", \"abcd\", \"any 1 char\", 1},\n        {\"Edge: Full String Pal\", \"s=racecar\", \"racecar\", \"racecar\", 7}\n    };\n    int lim = DSA_SAMPLE_ONLY ? 2 : (int)tests.size();\n    Solution sol;\n    for (int i = 0; i < lim; ++i) {\n        auto t0 = chrono::steady_clock::now();\n        string act = sol.longestPalindrome(tests[i].s);\n        double ms = chrono::duration<double, milli>(chrono::steady_clock::now() - t0).count();\n        bool ok = _is_ok_pal(tests[i].s, act, tests[i].exp_len);\n        _res.push_back({tests[i].name, tests[i].inp, _dsa_fmt(tests[i].rep), _dsa_fmt(act), \"\", ok, ms});\n    }\n    cout.rdbuf(_old);\n    _dsa_emit_json(_res, _dbg.str());\n    return 0;\n}"
                    }
                ]
            }
        ]
    }
}
