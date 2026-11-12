# DSA Cases 12 to 15: Greedy, Binary Trees, BST & Balancing, Graphs I (BFS/DFS/TopoSort)

CASES_PART4 = {
    "12": {
        "title": "Case 12: The Myopic Trap — Greedy Choice & Exchange Proofs",
        "episodes": [
            {
                "title": "Module 1: Greedy Choice Property, Exchange Arguments & Counterexamples",
                "blocks": [
                    {
                        "type": "story",
                        "title": "When 'Pick the Biggest Coin' Gives the Wrong Change",
                        "content": "A greedy change-maker worked flawlessly for US coins `[25, 10, 5, 1]`. When deployed in a region with denominations `[1, 3, 4]` for `amount = 6`, picking the locally greedy largest coin `4` produced `[4, 1, 1]` (**3 coins**) instead of the optimal `[3, 3]` (**2 coins**)!\n\n> [!WARNING]\n> **Never trust greedy intuition without a proof or counterexample search.** Greedy works ONLY when **Greedy Choice Property** and **Optimal Substructure** both hold—most often proven via an **Exchange Argument**."
                    },
                    {
                        "type": "objective",
                        "content": "Master the Exchange Argument proof technique for greedy interval scheduling, construct fast counterexamples to separate Greedy from Dynamic Programming, and prove linear reachability invariants."
                    },
                    {
                        "type": "concept",
                        "title": "The Exchange Argument Proof (Earliest Finish Time Wins)",
                        "content": "To schedule the maximum number of non-overlapping intervals:\n1. Sorting by **Start Time** fails (`[0, 100], [1, 2], [3, 4]`).\n2. Sorting by **Shortest Duration** fails (`[1, 5], [4, 7], [6, 10]`, where picking `[4, 7]` destroys BOTH `[1, 5]` and `[6, 10]`).\n3. **Sort by Earliest End Time (`end` ascending) — Exchange Proof:** Let $g_1$ be the interval finishing earliest overall, and let $O = \\{o_1, o_2, \\dots, o_k\\}$ be ANY optimal schedule ordered by finish time. Since $g_1.\\text{end} \\le o_1.\\text{end}$, swapping $o_1 \\to g_1$ creates zero new conflict with $o_2, \\dots, o_k$ while preserving optimal size $k$! Inductively, greedy matches optimal.",
                        "technical_explanation": "**Relation to Non-Overlapping Intervals (`LC-435`):** Removing the *minimum* number of overlapping intervals is strictly dual to keeping the *maximum* number of compatible intervals (`removals = N - max_kept`)!"
                    },
                    {
                        "type": "comparison_table",
                        "title": "Greedy Interval Sorting Heuristic Test",
                        "headers": ["Sort Criterion", "Counterexample Intervals", "Optimal Kept", "Heuristic Kept", "Valid?"],
                        "rows": [
                            ["Start Time Asc", "[[0,10], [1,2], [3,4]]", "2", "1 ([0,10])", "No"],
                            ["Shortest Duration Asc", "[[1,5], [4,7], [6,10]]", "2", "1 ([4,7])", "No"],
                            ["Fewest Overlaps", "Symmetric 4-chain trap", "4", "3", "No"],
                            ["Earliest End Time Asc", "Proven valid via Exchange Argument", "All k", "All k", "Yes!"]
                        ]
                    },
                    {
                        "type": "interactive",
                        "title": "Greedy vs DP Counterexample Check",
                        "question": "For which coin system does the Greedy 'always take the largest coin <= remaining' strategy FAIL to find the minimum coin count?",
                        "options": [
                            "[1, 5, 10, 25] for target = 30",
                            "[1, 3, 4] for target = 6",
                            "[1, 2, 4, 8] for target = 11",
                            "[1, 10, 100] for target = 111"
                        ],
                        "answer": 1,
                        "explanation": "On `[1, 3, 4]` with `target = 6`, greedy picks `4 + 1 + 1` (3 coins), whereas optimal DP picks `3 + 3` (2 coins)!"
                    }
                ]
            },
            {
                "title": "Module 2: Jump Reachability Invariant & Interval Removals",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "Single-Pass Reachability Horizon (`farthest = max(farthest, i + nums[i])`)",
                        "content": "In Jump Game (`LC-55`), recursion/DP asks from each index `i` whether *any* jump $1 \\dots \\text{nums}[i]$ reaches the end ($O(N^2)$). Instead, maintain only the **farthest reachable index** `max_reach = 0`:\n- Iterate `i` from `0` to `n - 1`:\n  - If **`i > max_reach`**, index `i` is an unreachable chasm -> return `False` immediately!\n  - Otherwise `max_reach = max(max_reach, i + nums[i])`.\n  - If `max_reach >= n - 1`, return `True` early!\nBecause every index `<= max_reach` is guaranteed reachable, no DP array or backtracking is ever needed ($O(N)$ time, $O(1)$ space).",
                        "technical_explanation": "**Jump Game II (`LC-45` Minimum Jumps):** Track current BFS jump level boundary `cur_end` and next horizon `farthest`; increment `jumps += 1` and advance `cur_end = farthest` only when `i == cur_end`!"
                    },
                    {
                        "type": "calculation_challenge",
                        "title": "Interval Removals Count",
                        "formula": "Maximum non-overlapping kept intervals + minimum removed intervals = Total intervals $N$.",
                        "problem": "Given `[[1,2], [2,3], [3,4], [1,3]]`, how many minimum intervals must be removed so the rest are non-overlapping?",
                        "answer": "1",
                        "alternatives": ["1"],
                        "step_by_step": "Sort by end: `[1,2], [2,3], [1,3], [3,4]`. Keep `[1,2]` (`end=2`), keep `[2,3]` (`2 >= 2, end=3`), drop `[1,3]` (`1 < 3`), keep `[3,4]` (`3 >= 3, end=4`). Removed = **1**."
                    }
                ]
            },
            {
                "title": "Module 3: Coding Lab I — Jump Game (LC-55)",
                "blocks": [
                    {
                        "type": "dsa_problem",
                        "title": "Jump Game (Reachability Horizon)",
                        "platform_style": "LeetCode 55 • Coding Ninjas Greedy Classic",
                        "difficulty": "Medium",
                        "pattern": "Greedy Reachability Invariant",
                        "target_time": "O(N)",
                        "target_space": "O(1)",
                        "statement": "You are given an integer array `nums`. You are initially positioned at the array's **first index**, and each element `nums[i]` represents your **maximum jump length** at that position.\n\nReturn `true` if you can reach the **last index**, or `false` otherwise.",
                        "examples": [
                            {"input": "nums = [2, 3, 1, 1, 4]", "output": "true", "explanation": "Jump 1 step from 0 to 1, then 3 steps to index 4."},
                            {"input": "nums = [3, 2, 1, 0, 4]", "output": "false", "explanation": "You always arrive at index 3 (max jump = 0), never crossing to index 4."}
                        ],
                        "constraints": [
                            "$1 \\le \\text{nums.length} \\le 10^4$",
                            "$0 \\le \\text{nums}[i] \\le 10^5$"
                        ],
                        "approach_ladder": {
                            "brute": "Backtracking / 1D DP testing all jump lengths $1 \\dots \\text{nums}[i]$: $O(N^2)$ worst-case.",
                            "optimal": "Track scalar `max_reach = 0`. At each index `i`: if `i > max_reach`, return `False`. Update `max_reach = max(max_reach, i + nums[i])`. **$O(N)$ time, $O(1)$ space**."
                        },
                        "dry_run": "`[3, 2, 1, 0, 4]`: `i=0->reach=3`, `i=1->reach=3`, `i=2->reach=3`, `i=3->reach=3`, `i=4 > 3` -> **False**!",
                        "edge_cases": [
                            {"title": "Single Element [0]", "desc": "Already standing at last index (`0 >= len - 1 == 0`) -> **True**, even though `nums[0] == 0`!"}
                        ],
                        "follow_ups": "**LC-45 Jump Game II:** Count the minimum jumps using implicit BFS level horizon `(cur_end, farthest)` in $O(N)$ time, $O(1)$ space!",
                        "hint": "Track `max_reach`; if index `i` ever exceeds `max_reach`, you hit a dead zone and can return `False` immediately.",
                        "starter_py": "class Solution:\n    def canJump(self, nums: List[int]) -> bool:\n        # TODO: O(N) greedy reachability check\n        return False\n",
                        "solution_py": "class Solution:\n    def canJump(self, nums: List[int]) -> bool:\n        reach = 0\n        for i, jump in enumerate(nums):\n            if i > reach:\n                return False\n            if i + jump > reach:\n                reach = i + jump\n            if reach >= len(nums) - 1:\n                return True\n        return True\n",
                        "harness_py": "_dsa_run_tests([\n    ('Sample 1: Reachable', '[2,3,1,1,4]', lambda: Solution().canJump([2,3,1,1,4]), True),\n    ('Sample 2: Zero Trap', '[3,2,1,0,4]', lambda: Solution().canJump([3,2,1,0,4]), False),\n    ('Edge: Single Zero', '[0]', lambda: Solution().canJump([0]), True),\n    ('Edge: Leap Over Zeros', '[2,0,0]', lambda: Solution().canJump([2,0,0]), True),\n    ('Edge: Blocked Start', '[0,2,3]', lambda: Solution().canJump([0,2,3]), False),\n], sample_only=__DSA_SAMPLE_ONLY__, n_samples=2)",
                        "starter_cpp": "class Solution {\npublic:\n    bool canJump(vector<int>& nums) {\n        // TODO: O(N) time, O(1) space\n        return false;\n    }\n};\n",
                        "solution_cpp": "class Solution {\npublic:\n    bool canJump(vector<int>& nums) {\n        int reach = 0, n = (int)nums.size();\n        for (int i = 0; i < n; ++i) {\n            if (i > reach) return false;\n            reach = max(reach, i + nums[i]);\n            if (reach >= n - 1) return true;\n        }\n        return true;\n    }\n};\n",
                        "harness_cpp": "int main() {\n    ostringstream _dbg; streambuf* _old = cout.rdbuf(_dbg.rdbuf());\n    vector<_DSACaseOut> _res;\n    struct T { string name, inp; vector<int> arr; bool exp; };\n    vector<T> tests = {\n        {\"Sample 1: Reachable\", \"[2,3,1,1,4]\", {2,3,1,1,4}, true},\n        {\"Sample 2: Zero Trap\", \"[3,2,1,0,4]\", {3,2,1,0,4}, false},\n        {\"Edge: Single Zero\", \"[0]\", {0}, true},\n        {\"Edge: Leap Over Zeros\", \"[2,0,0]\", {2,0,0}, true},\n        {\"Edge: Blocked Start\", \"[0,2,3]\", {0,2,3}, false}\n    };\n    int lim = DSA_SAMPLE_ONLY ? 2 : (int)tests.size();\n    Solution sol;\n    for (int i = 0; i < lim; ++i) {\n        auto v = tests[i].arr;\n        auto t0 = chrono::steady_clock::now();\n        bool act = sol.canJump(v);\n        double ms = chrono::duration<double, milli>(chrono::steady_clock::now() - t0).count();\n        _res.push_back({tests[i].name, tests[i].inp, _dsa_fmt(tests[i].exp), _dsa_fmt(act), \"\", act == tests[i].exp, ms});\n    }\n    cout.rdbuf(_old);\n    _dsa_emit_json(_res, _dbg.str());\n    return 0;\n}"
                    }
                ]
            },
            {
                "title": "Module 4: Coding Lab II — Non-Overlapping Intervals (LC-435)",
                "blocks": [
                    {
                        "type": "dsa_problem",
                        "title": "Non-overlapping Intervals (Earliest End Scheduling)",
                        "platform_style": "LeetCode 435 • Coding Ninjas Activity Selection Track",
                        "difficulty": "Medium",
                        "pattern": "Greedy Interval Scheduling (Sort by End Time)",
                        "target_time": "O(N log N)",
                        "target_space": "O(1)",
                        "statement": "Given an array of `intervals` where `intervals[i] = [start_i, end_i]`, return the **minimum number of intervals you need to remove** to make the rest of the intervals non-overlapping.\n\n**Note:** Intervals that only **touch** at a boundary (e.g. `[1, 2]` and `[2, 3]`) are **non-overlapping**.",
                        "examples": [
                            {"input": "intervals = [[1,2],[2,3],[3,4],[1,3]]", "output": "1", "explanation": "Removing [1,3] leaves [1,2], [2,3], [3,4] disjoint."},
                            {"input": "intervals = [[1,2],[1,2],[1,2]]", "output": "2", "explanation": "Must remove 2 duplicates leaving 1."}
                        ],
                        "constraints": [
                            "$1 \\le \\text{intervals.length} \\le 10^5$",
                            "$-5 \\times 10^4 \\le \\text{start}_i < \\text{end}_i \\le 5 \\times 10^4$"
                        ],
                        "approach_ladder": {
                            "brute": "Backtracking / LIS DP picking max independent set in $O(N^2)$.",
                            "optimal": "Sort intervals strictly by **`end` ascending**! Keep `prev_end = intervals[0][1]`, `removals = 0`. For each subsequent `[s, e]`: if **`s < prev_end`**, they overlap -> increment `removals += 1` (discard the later-ending one, i.e., keep `prev_end` unchanged!); else `prev_end = e`. **$O(N \\log N)$ time, $O(1)$ space**."
                        },
                        "dry_run": "`[[1,100], [2,3], [3,4]]`: sorted by end -> `[2,3], [3,4], [1,100]`. Keep `[2,3]` (`prev=3`), keep `[3,4]` (`3>=3, prev=4`), overlap `[1,100]` (`1 < 4 -> removals=1`) -> **1** (if sorted by start instead, you'd wrongly keep `[1,100]` and drop TWO intervals!).",
                        "edge_cases": [
                            {"title": "Negative Interval Coordinates", "desc": "Do NOT initialize `prev_end = 0`! Initialize from `-inf` / `intervals[0][1]` directly so `[-100, -10]` works accurately."}
                        ],
                        "follow_ups": "**LC-452 Minimum Number of Arrows to Burst Balloons:** Identical sort-by-end logic, except touching endpoints `[1,2]` & `[2,3]` CAN share one arrow (`s <= prev_end`).",
                        "hint": "Sort by END time ascending, initialize `prev_end` from the first interval's end, and increment `removed` whenever `start < prev_end`.",
                        "starter_py": "class Solution:\n    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:\n        # TODO: Sort by end time and count minimal removals\n        return 0\n",
                        "solution_py": "class Solution:\n    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:\n        intervals.sort(key=lambda iv: iv[1])\n        prev_end = intervals[0][1]\n        removed = 0\n        for s, e in intervals[1:]:\n            if s < prev_end:\n                removed += 1\n            else:\n                prev_end = e\n        return removed\n",
                        "harness_py": "_dsa_run_tests([\n    ('Sample 1: Drop Spanning [1,3]', '[[1,2],[2,3],[3,4],[1,3]]', lambda: Solution().eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]), 1),\n    ('Sample 2: Exact Duplicates', '[[1,2],[1,2],[1,2]]', lambda: Solution().eraseOverlapIntervals([[1,2],[1,2],[1,2]]), 2),\n    ('Edge: Earliest-Start Trap', '[[1,100],[2,3],[3,4]]', lambda: Solution().eraseOverlapIntervals([[1,100],[2,3],[3,4]]), 1),\n    ('Edge: Negatives Disjoint', '[[-50,-20],[-10,0],[0,5]]', lambda: Solution().eraseOverlapIntervals([[-50,-20],[-10,0],[0,5]]), 0),\n], sample_only=__DSA_SAMPLE_ONLY__, n_samples=2)",
                        "starter_cpp": "class Solution {\npublic:\n    int eraseOverlapIntervals(vector<vector<int>>& intervals) {\n        // TODO: Earliest finish time greedy sort\n        return 0;\n    }\n};\n",
                        "solution_cpp": "class Solution {\npublic:\n    int eraseOverlapIntervals(vector<vector<int>>& intervals) {\n        sort(intervals.begin(), intervals.end(), [](const auto& a, const auto& b) {\n            return a[1] < b[1];\n        });\n        int prev_end = intervals[0][1], removed = 0;\n        for (size_t i = 1; i < intervals.size(); ++i) {\n            if (intervals[i][0] < prev_end) ++removed;\n            else prev_end = intervals[i][1];\n        }\n        return removed;\n    }\n};\n",
                        "harness_cpp": "int main() {\n    ostringstream _dbg; streambuf* _old = cout.rdbuf(_dbg.rdbuf());\n    vector<_DSACaseOut> _res;\n    struct T { string name, inp; vector<vector<int>> iv; int exp; };\n    vector<T> tests = {\n        {\"Sample 1: Drop Spanning\", \"[[1,2],[2,3],[3,4],[1,3]]\", {{1,2},{2,3},{3,4},{1,3}}, 1},\n        {\"Sample 2: Duplicates\", \"[[1,2],[1,2],[1,2]]\", {{1,2},{1,2},{1,2}}, 2},\n        {\"Edge: Earliest-Start Trap\", \"[[1,100],[2,3],[3,4]]\", {{1,100},{2,3},{3,4}}, 1},\n        {\"Edge: Negative Coords\", \"[[-50,-20],[-10,0],[0,5]]\", {{-50,-20},{-10,0},{0,5}}, 0}\n    };\n    int lim = DSA_SAMPLE_ONLY ? 2 : (int)tests.size();\n    Solution sol;\n    for (int i = 0; i < lim; ++i) {\n        auto v = tests[i].iv;\n        auto t0 = chrono::steady_clock::now();\n        int act = sol.eraseOverlapIntervals(v);\n        double ms = chrono::duration<double, milli>(chrono::steady_clock::now() - t0).count();\n        _res.push_back({tests[i].name, tests[i].inp, _dsa_fmt(tests[i].exp), _dsa_fmt(act), \"\", act == tests[i].exp, ms});\n    }\n    cout.rdbuf(_old);\n    _dsa_emit_json(_res, _dbg.str());\n    return 0;\n}"
                    }
                ]
            }
        ]
    },
    "13": {
        "title": "Case 13: Hierarchy Protocol — Binary Trees, DFS & BFS",
        "episodes": [
            {
                "title": "Module 1: Structural DFS vs Level-Order BFS & Single-Pass Post-Order",
                "blocks": [
                    {
                        "type": "story",
                        "title": "Eliminating Repeated O(N^2) Tree Height Scans",
                        "content": "Computing balanced height or tree diameter by calling `height(root.left) + height(root.right)` recursively at every node re-visits deep subtrees linearly per ancestor—degrading skewed trees to $O(N^2)$.\n\n> [!TIP]\n> Returning child **height** bottom-up from a single Post-Order DFS while updating a global/reference `diameter` inside each callback solves **Diameter (`LC-543`)**, **Balanced Check (`LC-110`)**, and **Max Path Sum (`LC-124`)** in a single **$O(N)$** pass!"
                    },
                    {
                        "type": "concept",
                        "title": "Traversal Taxonomy & Lowest Common Ancestor (LCA) Logic",
                        "content": "1. **DFS Traversals ($O(N)$ time, $O(H)$ stack space):**\n   - **Pre-order (Root -> L -> R):** Cloning/serializing trees, top-down path prefix accumulation.\n   - **In-order (L -> Root -> R):** Yields sorted order in BSTs!\n   - **Post-order (L -> R -> Root):** Safe tree deletion (`free`), subtree height / diameter / bottom-up aggregation.\n2. **BFS Level Order (`LC-102`):** Snapshot `sz = len(q)` at the start of every outer loop iteration to isolate nodes strictly belonging to one horizontal depth.\n3. **Lowest Common Ancestor (`LC-236`):** Return `root` if `root in (None, p, q)`. Recurse `left = lca(root.left)` and `right = lca(root.right)`. If **both** return non-null -> current `root` is the exact split ancestor! Otherwise return `left or right`.",
                        "technical_explanation": "**Morris Traversal ($O(N)$ time, strict $O(1)$ space):** Temporarily links each node's inorder predecessor's `right` pointer back to the current root node, restoring pointers upon second visit—achieving stackless $O(1)$ space tree traversal!"
                    },
                    {
                        "type": "visual",
                        "title": "Diameter Passing Through Deep Interior Subtree (Not Root!)",
                        "code": "graph TD\n  R[\"1 (LeftH=0, RightH=4 => 4)\"] --> R1[\"2\"]\n  R1 --> L2[\"3 -> 5 -> 7\"]\n  R1 --> R2[\"4 -> 6 -> 8\"]\n  NOTE[\"Longest path goes L3-L2-node2-R2-R3 = 4+ edges WITHOUT touching root!\"]\n  style R1 fill:#065f46,stroke:#10b981"
                    },
                    {
                        "type": "interactive",
                        "title": "Skewed Binary Tree Recursion Space Complexity",
                        "question": "If a Binary Tree has $N = 10^5$ nodes and is completely left-skewed (forming a chain), what is the worst-case auxiliary call-stack space of recursive DFS vs BFS Queue max size?",
                        "options": [
                            "DFS: O(log N) | BFS: O(N)",
                            "DFS: O(N) stack depth | BFS: O(1) queue width (1 node per level!)",
                            "Both O(log N)",
                            "Both O(1)"
                        ],
                        "answer": 1,
                        "explanation": "On a skewed chain, DFS recurses $N$ frames deep ($O(N)$—risking Stack Overflow in Python's default limit!), whereas BFS holds at most `1` node per level ($O(1)$ space)! On a complete balanced tree, DFS takes $O(\\log N)$ while BFS bottom level holds $N/2 = O(N)$!"
                    }
                ]
            },
            {
                "title": "Module 2: Edge vs Node Conventions & Post-Order Dry Run",
                "blocks": [
                    {
                        "type": "debugger",
                        "title": "Nodes vs Edges Off-by-One in Diameter",
                        "scenario": "Diameter of a Binary Tree (`LC-543`) is defined as the **length in EDGES** of the longest path between any two nodes. A developer counts nodes (`left_h + right_h + 1`) cleanly at each node.",
                        "options": [
                            "Correct: node count equals edge count",
                            "Off by +1! If `height(leaf) = 1` (nodes), `left_h + right_h` already counts edges cleanly (`height` left edges + `height` right edges), whereas `+ 1` counts nodes!",
                            "Diameter cannot exceed height",
                            "Must multiply by 2"
                        ],
                        "answer": 1,
                        "explanation": "Take `height(None) = 0` and at any node `h = 1 + max(L, R)`. Then the two downward subpaths have `L` edges left + `R` edges right -> exact edge count is **`L + R`**!"
                    },
                    {
                        "type": "calculation_challenge",
                        "title": "Complete Tree Width vs Nodes Math",
                        "formula": "In a full complete binary tree of height $h$ levels (root at level 0), level $k$ holds $2^k$ nodes.",
                        "problem": "How many nodes sit on the bottom level ($k = 4$) inside a BFS queue for a full binary tree of 31 nodes?",
                        "answer": "16",
                        "alternatives": ["16"],
                        "step_by_step": "Levels `0..4` hold $1 + 2 + 4 + 8 + 16 = 31$ nodes; the final level width is $2^4 = 16$."
                    }
                ]
            },
            {
                "title": "Module 3: Coding Lab I — Diameter of Binary Tree (LC-543)",
                "blocks": [
                    {
                        "type": "dsa_problem",
                        "title": "Diameter of Binary Tree",
                        "platform_style": "LeetCode 543 • Coding Ninjas Tree DFS Classic",
                        "difficulty": "Easy",
                        "pattern": "Bottom-Up Post-Order Height Propagation",
                        "target_time": "O(N)",
                        "target_space": "O(H)",
                        "statement": "Given the `root` of a binary tree (`TreeNode`), return the **length of the diameter** of the tree.\n\nThe diameter is the length (**number of edges**) of the **longest path between any two nodes** in the tree. This path may or may not pass through `root`!",
                        "examples": [
                            {"input": "root = [1, 2, 3, 4, 5]", "output": "3", "explanation": "Longest path [4 -> 2 -> 1 -> 3] or [5 -> 2 -> 1 -> 3] has length 3 edges."},
                            {"input": "root = [1, 2]", "output": "1", "explanation": "Single edge between 1 and 2."}
                        ],
                        "constraints": [
                            "$1 \\le \\text{number of nodes} \\le 10^4$",
                            "$-100 \\le \\text{Node.val} \\le 100$"
                        ],
                        "approach_ladder": {
                            "brute": "Recompute `height(left) + height(right)` independently at every node: $O(N^2)$ on skewed trees.",
                            "optimal": "Single Post-Order `height(node)`: return `0` on null; compute `L = height(node.left)`, `R = height(node.right)`, update `best = max(best, L + R)`, and return `1 + max(L, R)`! **$O(N)$ time, $O(H)$ stack space**."
                        },
                        "dry_run": "At leaf `4`: `L=0, R=0 -> best=0, returns 1`. At `2`: `L=1 (from 4), R=1 (from 5) -> best=2, returns 2`. At `1`: `L=2, R=1 -> best=3, returns 3`.",
                        "edge_cases": [
                            {"title": "Diameter Entirely Inside One Subtree", "desc": "Tree `[1, 2, null, 3, 4, 5, null, null, 6]` has diameter completely below node `2`, never touching `1`!"}
                        ],
                        "follow_ups": "**LC-124 Binary Tree Maximum Path Sum:** Identical post-order trick—clamp negative child branches via `max(0, gain)` before summing `val + L + R`!",
                        "hint": "Have DFS return subtree node-height (`1 + max(L, R)`) while updating `diameter = max(diameter, L + R)` internally.",
                        "preamble_cpp": "#define DSA_USE_TREENODE 1\n",
                        "starter_py": "class Solution:\n    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:\n        # TODO: Single-pass O(N) post-order DFS returning edge count\n        return 0\n",
                        "solution_py": "class Solution:\n    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:\n        best = 0\n        def height(node: Optional[TreeNode]) -> int:\n            nonlocal best\n            if not node:\n                return 0\n            L = height(node.left)\n            R = height(node.right)\n            if L + R > best:\n                best = L + R\n            return 1 + (L if L > R else R)\n        height(root)\n        return best\n",
                        "harness_py": "_dsa_run_tests([\n    ('Sample 1: [1,2,3,4,5]', '[1,2,3,4,5]', lambda: Solution().diameterOfBinaryTree(_dsa_build_tree([1,2,3,4,5])), 3),\n    ('Sample 2: [1,2]', '[1,2]', lambda: Solution().diameterOfBinaryTree(_dsa_build_tree([1,2])), 1),\n    ('Edge: Single Node', '[42]', lambda: Solution().diameterOfBinaryTree(_dsa_build_tree([42])), 0),\n    ('Edge: Non-Root Diameter Subtree', '[1,2,None,3,4,5,None,None,6]', lambda: Solution().diameterOfBinaryTree(_dsa_build_tree([1,2,None,3,4,5,None,None,6])), 4),\n], sample_only=__DSA_SAMPLE_ONLY__, n_samples=2)",
                        "starter_cpp": "class Solution {\npublic:\n    int diameterOfBinaryTree(TreeNode* root) {\n        // TODO: Single-pass O(N) post-order DFS\n        return 0;\n    }\n};\n",
                        "solution_cpp": "class Solution {\n    int height(TreeNode* node, int& best) {\n        if (!node) return 0;\n        int L = height(node->left, best);\n        int R = height(node->right, best);\n        best = max(best, L + R);\n        return 1 + max(L, R);\n    }\npublic:\n    int diameterOfBinaryTree(TreeNode* root) {\n        int best = 0;\n        height(root, best);\n        return best;\n    }\n};\n",
                        "harness_cpp": "int main() {\n    ostringstream _dbg; streambuf* _old = cout.rdbuf(_dbg.rdbuf());\n    vector<_DSACaseOut> _res;\n    const int NV = INT_MIN;\n    struct T { string name, inp; vector<int> arr; int exp; };\n    vector<T> tests = {\n        {\"Sample 1: [1,2,3,4,5]\", \"[1,2,3,4,5]\", {1,2,3,4,5}, 3},\n        {\"Sample 2: [1,2]\", \"[1,2]\", {1,2}, 1},\n        {\"Edge: Single Node\", \"[42]\", {42}, 0},\n        {\"Edge: Non-Root Subtree\", \"[1,2,null,3,4,5,null,null,6]\", {1,2,NV,3,4,5,NV,NV,6}, 4}\n    };\n    int lim = DSA_SAMPLE_ONLY ? 2 : (int)tests.size();\n    Solution sol;\n    for (int i = 0; i < lim; ++i) {\n        TreeNode* root = _dsa_build_tree(tests[i].arr, NV);\n        auto t0 = chrono::steady_clock::now();\n        int act = sol.diameterOfBinaryTree(root);\n        double ms = chrono::duration<double, milli>(chrono::steady_clock::now() - t0).count();\n        _res.push_back({tests[i].name, tests[i].inp, _dsa_fmt(tests[i].exp), _dsa_fmt(act), \"\", act == tests[i].exp, ms});\n    }\n    cout.rdbuf(_old);\n    _dsa_emit_json(_res, _dbg.str());\n    return 0;\n}"
                    }
                ]
            },
            {
                "title": "Module 4: Coding Lab II — Binary Tree Level Order Traversal (LC-102)",
                "blocks": [
                    {
                        "type": "dsa_problem",
                        "title": "Binary Tree Level Order Traversal",
                        "platform_style": "LeetCode 102 • Coding Ninjas BFS Tree Traversal",
                        "difficulty": "Medium",
                        "pattern": "BFS Queue Level-Snapshot Grouping",
                        "target_time": "O(N)",
                        "target_space": "O(N)",
                        "statement": "Given the `root` of a binary tree, return the **level order traversal** of its nodes' values (i.e., from left to right, level by level as a 2D list).",
                        "examples": [
                            {"input": "root = [3, 9, 20, null, null, 15, 7]", "output": "[[3], [9, 20], [15, 7]]", "explanation": "Depth 0: [3]; Depth 1: [9, 20]; Depth 2: [15, 7]."},
                            {"input": "root = []", "output": "[]", "explanation": "Null tree produces empty outer vector."}
                        ],
                        "constraints": [
                            "$0 \\le \\text{number of nodes} \\le 2000$",
                            "$-1000 \\le \\text{Node.val} \\le 1000$"
                        ],
                        "approach_ladder": {
                            "better": "DFS carrying `(node, depth)` appending `res[depth].append(node.val)`.",
                            "optimal": "Queue seeded with `root` (if non-null). In each `while q` iteration, snapshot `sz = len(q)` and pop **exactly `sz` nodes** into `level`, enqueueing non-null left/right children! **$O(N)$ time, $O(N)$ queue space**."
                        },
                        "dry_run": "`q=[3]`, `sz=1`: pop `3` -> push `9, 20`, record `[3]`. Next `q=[9,20]`, `sz=2`: pop `9`, pop `20` -> push `15, 7`, record `[9,20]`.",
                        "edge_cases": [
                            {"title": "Empty Tree Guard", "desc": "`if not root: return []` before pushing `root` onto queue (otherwise pushing `None` iterates once and crashes!)."}
                        ],
                        "follow_ups": "**LC-103 Zigzag Level Order / LC-199 Right Side View:** Same exact `sz = len(q)` BFS skeleton—reverse odd levels or append `level[-1]`!",
                        "hint": "Capture `level_size = len(queue)` before iterating inside each BFS round so levels never mix.",
                        "preamble_cpp": "#define DSA_USE_TREENODE 1\n",
                        "starter_py": "class Solution:\n    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:\n        # TODO: BFS queue grouped per depth level\n        return []\n",
                        "solution_py": "class Solution:\n    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:\n        if not root:\n            return []\n        res = []\n        q = deque([root])\n        while q:\n            sz = len(q)\n            lvl = []\n            for _ in range(sz):\n                cur = q.popleft()\n                lvl.append(cur.val)\n                if cur.left: q.append(cur.left)\n                if cur.right: q.append(cur.right)\n            res.append(lvl)\n        return res\n",
                        "harness_py": "_dsa_run_tests([\n    ('Sample 1: Asymmetric Tree', '[3,9,20,None,None,15,7]', lambda: Solution().levelOrder(_dsa_build_tree([3,9,20,None,None,15,7])), [[3],[9,20],[15,7]]),\n    ('Sample 2: Empty Tree', '[]', lambda: Solution().levelOrder(_dsa_build_tree([])), []),\n    ('Edge: Single Node', '[1]', lambda: Solution().levelOrder(_dsa_build_tree([1])), [[1]]),\n    ('Edge: Left-Skewed Chain', '[1,2,None,3,None,4]', lambda: Solution().levelOrder(_dsa_build_tree([1,2,None,3,None,4])), [[1],[2],[3],[4]]),\n], sample_only=__DSA_SAMPLE_ONLY__, n_samples=2)",
                        "starter_cpp": "class Solution {\npublic:\n    vector<vector<int>> levelOrder(TreeNode* root) {\n        // TODO: O(N) BFS level-snapshot loop\n        return {};\n    }\n};\n",
                        "solution_cpp": "class Solution {\npublic:\n    vector<vector<int>> levelOrder(TreeNode* root) {\n        vector<vector<int>> res;\n        if (!root) return res;\n        queue<TreeNode*> q;\n        q.push(root);\n        while (!q.empty()) {\n            int sz = (int)q.size();\n            vector<int> lvl;\n            lvl.reserve(sz);\n            for (int i = 0; i < sz; ++i) {\n                TreeNode* cur = q.front(); q.pop();\n                lvl.push_back(cur->val);\n                if (cur->left) q.push(cur->left);\n                if (cur->right) q.push(cur->right);\n            }\n            res.push_back(move(lvl));\n        }\n        return res;\n    }\n};\n",
                        "harness_cpp": "int main() {\n    ostringstream _dbg; streambuf* _old = cout.rdbuf(_dbg.rdbuf());\n    vector<_DSACaseOut> _res;\n    const int NV = INT_MIN;\n    struct T { string name, inp; vector<int> arr; vector<vector<int>> exp; };\n    vector<T> tests = {\n        {\"Sample 1: Asymmetric Tree\", \"[3,9,20,null,null,15,7]\", {3,9,20,NV,NV,15,7}, {{3},{9,20},{15,7}}},\n        {\"Sample 2: Empty Tree\", \"[]\", {}, {}},\n        {\"Edge: Single Node\", \"[1]\", {1}, {{1}}},\n        {\"Edge: Left-Skewed Chain\", \"[1,2,null,3,null,4]\", {1,2,NV,3,NV,4}, {{1},{2},{3},{4}}}\n    };\n    int lim = DSA_SAMPLE_ONLY ? 2 : (int)tests.size();\n    Solution sol;\n    for (int i = 0; i < lim; ++i) {\n        TreeNode* root = _dsa_build_tree(tests[i].arr, NV);\n        auto t0 = chrono::steady_clock::now();\n        auto act = sol.levelOrder(root);\n        double ms = chrono::duration<double, milli>(chrono::steady_clock::now() - t0).count();\n        _res.push_back({tests[i].name, tests[i].inp, _dsa_fmt(tests[i].exp), _dsa_fmt(act), \"\", act == tests[i].exp, ms});\n    }\n    cout.rdbuf(_old);\n    _dsa_emit_json(_res, _dbg.str());\n    return 0;\n}"
                    }
                ]
            }
        ]
    },
    "14": {
        "title": "Case 14: Balanced Order — Binary Search Trees & Rotation Invariants",
        "episodes": [
            {
                "title": "Module 1: Global BST Range Invariants, AVL & Red-Black Theory",
                "blocks": [
                    {
                        "type": "story",
                        "title": "The Broken Local BST Validator",
                        "content": "A validation routine checked `left.val < root.val < right.val` locally at every node—and approved a corrupted index `[5, 4, 6, null, null, 3, 7]`! Notice node `3` sits in the **right subtree** of `5` (`3 < 6` locally, yet `3 < 5` violates the global BST root bound!).\n\n> [!IMPORTANT]\n> **BST Global Invariant:** Every node in `root`'s left subtree must lie strictly inside `(low_bound, root.val)`, and every node in `root`'s right subtree strictly inside `(root.val, high_bound)`."
                    },
                    {
                        "type": "concept",
                        "title": "Self-Balancing Theory: AVL Rotations vs Red-Black Trees",
                        "content": "Unbalanced BSTs degenerate into sorted linked lists (`O(N)` lookup) on ascending inserts. Balanced BSTs keep height **$O(\\log N)$**:\n\n1. **AVL Trees (Adelson-Velsky & Landis):** Enforce `|height(L) - height(R)| <= 1` at every node via 4 local $O(1)$ pointer rotations (`LL`, `RR`, `LR`, `RL`). Strictly shorter height ($\\le 1.44 \\log_2 N$), slightly faster lookups.\n2. **Red-Black Trees (powers `std::map` / `std::set` / Java `TreeMap`):** Enforce 5 color invariants ensuring longest root-to-leaf path is **$\\le 2\\times$ shortest path** ($\\le 2 \\log_2(N+1)$). At most 2 rotations on insert and 3 on delete -> much faster under heavy mutations!\n3. **Inorder Property:** Traversing a BST **Left -> Node -> Right** ALWAYS visits keys in **strictly ascending order**, letting iterative Inorder find the Kth Smallest key in **$O(H + K)$** without inspecting the entire tree!",
                        "technical_explanation": "**32-Bit Bounds Bug in C++ LC-98:** If a single-node BST holds `INT_MIN` (`-2147483648`) or `INT_MAX` (`2147483647`), initializing `int low = INT_MIN, high = INT_MAX` fails strict inequality `low < node->val`! Pass **`long long`** (`LLONG_MIN`, `LLONG_MAX`) or nullable ancestor `TreeNode* minNode, *maxNode` pointers!"
                    },
                    {
                        "type": "comparison_table",
                        "title": "AVL vs Red-Black vs Unbalanced BST",
                        "headers": ["Property", "Unbalanced BST", "AVL Tree", "Red-Black Tree"],
                        "rows": [
                            ["Max Height", "O(N) skewed", "<= 1.44 log2(N)", "<= 2 log2(N+1)"],
                            ["Worst-Case Lookup", "O(N)", "O(log N) fastest reads", "O(log N)"],
                            ["Max Rotations on Delete", "0", "O(log N) cascading", "O(1) <= 3 rotations!"],
                            ["Standard Library Use", "None", "Read-heavy DB indexes", "C++ std::map, Linux CFS scheduler"]
                        ]
                    },
                    {
                        "type": "interactive",
                        "title": "BST Deletion 2-Child Replacement",
                        "question": "When deleting a BST node `Z` that has BOTH non-null left and right children (`LC-450`), which replacement preserves the global BST invariant?",
                        "options": [
                            "Always promote Z.left blindly",
                            "Replace Z with its Inorder Successor (minimum node in Z.right) or Inorder Predecessor (maximum node in Z.left), then recursively delete that replacement!",
                            "Swap Z with root",
                            "Delete both subtrees"
                        ],
                        "answer": 1,
                        "explanation": "The minimum node in `Z.right` is guaranteed `> all of Z.left` and `< remaining nodes in Z.right`, AND has at most 1 child (right child only), reducing deletion to the trivial 0/1-child case!"
                    }
                ]
            },
            {
                "title": "Module 2: Boundary Traps & Inorder Stack Mechanics",
                "blocks": [
                    {
                        "type": "wrong_approach",
                        "title": "Checking Only Immediate Children in Validate BST",
                        "language": "python",
                        "code": "def isValidBST(root):\n    if not root: return True\n    if root.left and root.left.val >= root.val: return False\n    if root.right and root.right.val <= root.val: return False\n    return isValidBST(root.left) and isValidBST(root.right) # FAILS `[5,4,6,None,None,3,7]`!",
                        "explanation": "Even though `3 < 6`, `3` sits in `5`'s right subtree where every value MUST exceed `5`. Always pass `(low, high)` bounds down the recursion."
                    },
                    {
                        "type": "calculation_challenge",
                        "title": "Minimum Height of Valid AVL Tree",
                        "formula": "Maximum nodes in a binary tree of height $h$ edges (root height $0$) is $2^{h+1} - 1$.",
                        "problem": "What is the minimum possible edge-height $h$ (counting edges from root to deepest leaf) needed to store $15$ nodes in a binary search tree?",
                        "answer": "3",
                        "alternatives": ["3"],
                        "step_by_step": "$2^{3+1} - 1 = 15$ nodes fit cleanly across levels `0..3`, giving edge-height `3`."
                    }
                ]
            },
            {
                "title": "Module 3: Coding Lab I — Validate Binary Search Tree (LC-98)",
                "blocks": [
                    {
                        "type": "dsa_problem",
                        "title": "Validate Binary Search Tree",
                        "platform_style": "LeetCode 98 • Coding Ninjas BST Invariant Classic",
                        "difficulty": "Medium",
                        "pattern": "Recursive Global (low, high) Bounds",
                        "target_time": "O(N)",
                        "target_space": "O(H)",
                        "statement": "Given the `root` of a binary tree, determine if it is a **valid Binary Search Tree (BST)**.\n\n- Left subtree contains **only** nodes with keys **strictly less** than the node's key.\n- Right subtree contains **only** nodes with keys **strictly greater** than the node's key.\n- Both subtrees must also be valid BSTs.",
                        "examples": [
                            {"input": "root = [2, 1, 3]", "output": "true", "explanation": "1 < 2 < 3 satisfies strict global bounds."},
                            {"input": "root = [5, 4, 6, null, null, 3, 7]", "output": "false", "explanation": "Node 3 in right subtree of 5 violates 3 > 5!"}
                        ],
                        "constraints": [
                            "$1 \\le \\text{number of nodes} \\le 10^4$",
                            "$-2^{31} \\le \\text{Node.val} \\le 2^{31} - 1$"
                        ],
                        "approach_ladder": {
                            "brute": "Collect full inorder traversal in an array and verify strictly ascending (`arr[i-1] < arr[i]`): $O(N)$ time & $O(N)$ space.",
                            "optimal": "DFS `valid(node, low, high)`: return `True` if null; if `not (low < node.val < high)` return `False`; return `valid(left, low, node.val) and valid(right, node.val, high)`. Pass `long long` (`LLONG_MIN`, `LLONG_MAX`) in C++! **$O(N)$ time, $O(H)$ stack space**."
                        },
                        "dry_run": "At `5`: `(-inf, +inf) -> ok`. Right child `6`: `(5, +inf) -> ok`. Left child of `6` (`3`): `(5, 6)` -> `5 < 3` **FALSE**!",
                        "edge_cases": [
                            {"title": "INT_MIN and INT_MAX Node Values", "desc": "`[2147483647]` and `[-2147483648, null, 2147483647]` MUST pass cleanly -> use `long long` (`LLONG_MIN`/`LLONG_MAX`) or `TreeNode*` bounds in C++!"},
                            {"title": "Duplicate Equal Keys", "desc": "`[2, 2, 2]` is invalid because BST requires **strict** `<` inequality."}
                        ],
                        "follow_ups": "**LC-99 Recover BST:** Find two swapped nodes in an almost-valid BST during a single inorder sweep comparing `prev_node.val >= cur.val`!",
                        "hint": "Track `(low, high)` ancestor range constraints using 64-bit bounds in C++ so `INT_MIN`/`INT_MAX` nodes validate accurately.",
                        "preamble_cpp": "#define DSA_USE_TREENODE 1\n",
                        "starter_py": "class Solution:\n    def isValidBST(self, root: Optional[TreeNode]) -> bool:\n        # TODO: Validate global (low, high) range bounds\n        return False\n",
                        "solution_py": "class Solution:\n    def isValidBST(self, root: Optional[TreeNode]) -> bool:\n        def dfs(node: Optional[TreeNode], lo: float, hi: float) -> bool:\n            if not node:\n                return True\n            if not (lo < node.val < hi):\n                return False\n            return dfs(node.left, lo, node.val) and dfs(node.right, node.val, hi)\n        return dfs(root, float('-inf'), float('inf'))\n",
                        "harness_py": "_dsa_run_tests([\n    ('Sample 1: Valid [2,1,3]', '[2,1,3]', lambda: Solution().isValidBST(_dsa_build_tree([2,1,3])), True),\n    ('Sample 2: Global Subtree Trap', '[5,4,6,None,None,3,7]', lambda: Solution().isValidBST(_dsa_build_tree([5,4,6,None,None,3,7])), False),\n    ('Edge: Equal Key Trap', '[2,2,2]', lambda: Solution().isValidBST(_dsa_build_tree([2,2,2])), False),\n    ('Edge: Single INT_MAX', '[2147483647]', lambda: Solution().isValidBST(_dsa_build_tree([2147483647])), True),\n    ('Edge: INT_MIN -> INT_MAX', '[-2147483648,None,2147483647]', lambda: Solution().isValidBST(_dsa_build_tree([-2147483648,None,2147483647])), True),\n], sample_only=__DSA_SAMPLE_ONLY__, n_samples=2)",
                        "starter_cpp": "class Solution {\npublic:\n    bool isValidBST(TreeNode* root) {\n        // TODO: Guard with long long LLONG_MIN / LLONG_MAX!\n        return false;\n    }\n};\n",
                        "solution_cpp": "class Solution {\n    bool dfs(TreeNode* node, long long lo, long long hi) {\n        if (!node) return true;\n        if (node->val <= lo || node->val >= hi) return false;\n        return dfs(node->left, lo, node->val) && dfs(node->right, node->val, hi);\n    }\npublic:\n    bool isValidBST(TreeNode* root) {\n        return dfs(root, LLONG_MIN, LLONG_MAX);\n    }\n};\n",
                        "harness_cpp": "int main() {\n    ostringstream _dbg; streambuf* _old = cout.rdbuf(_dbg.rdbuf());\n    vector<_DSACaseOut> _res;\n    const int NV = INT_MIN;\n    vector<tuple<string, string, TreeNode*, bool>> tests = {\n        {\"Sample 1: Valid [2,1,3]\", \"[2,1,3]\", _dsa_build_tree({2,1,3}, NV), true},\n        {\"Sample 2: Global Subtree Trap\", \"[5,4,6,null,null,3,7]\", _dsa_build_tree({5,4,6,NV,NV,3,7}, NV), false},\n        {\"Edge: Equal Key Trap\", \"[2,2,2]\", _dsa_build_tree({2,2,2}, NV), false},\n        {\"Edge: Single INT_MAX\", \"[2147483647]\", new TreeNode(INT_MAX), true},\n        {\"Edge: INT_MIN -> INT_MAX\", \"[-2147483648,null,2147483647]\", new TreeNode(INT_MIN, nullptr, new TreeNode(INT_MAX)), true}\n    };\n    int lim = DSA_SAMPLE_ONLY ? 2 : (int)tests.size();\n    Solution sol;\n    for (int i = 0; i < lim; ++i) {\n        auto& [nm, inp, root, exp] = tests[i];\n        auto t0 = chrono::steady_clock::now();\n        bool act = sol.isValidBST(root);\n        double ms = chrono::duration<double, milli>(chrono::steady_clock::now() - t0).count();\n        _res.push_back({nm, inp, _dsa_fmt(exp), _dsa_fmt(act), \"\", act == exp, ms});\n    }\n    cout.rdbuf(_old);\n    _dsa_emit_json(_res, _dbg.str());\n    return 0;\n}"
                    }
                ]
            },
            {
                "title": "Module 4: Coding Lab II — Kth Smallest Element in a BST (LC-230)",
                "blocks": [
                    {
                        "type": "dsa_problem",
                        "title": "Kth Smallest Element in a BST",
                        "platform_style": "LeetCode 230 • Coding Ninjas Iterative Inorder Track",
                        "difficulty": "Medium",
                        "pattern": "Iterative Early-Stop Inorder Stack",
                        "target_time": "O(H + K)",
                        "target_space": "O(H)",
                        "statement": "Given the `root` of a Binary Search Tree and an integer `k`, return the **$k$-th smallest value** (**1-indexed**) of all values in the tree.",
                        "examples": [
                            {"input": "root = [3, 1, 4, null, 2], k = 1", "output": "1", "explanation": "Inorder values [1, 2, 3, 4] -> 1st smallest is 1."},
                            {"input": "root = [5, 3, 6, 2, 4, null, null, 1], k = 3", "output": "3", "explanation": "Inorder [1, 2, 3, ...] -> 3rd smallest is 3."}
                        ],
                        "constraints": [
                            "$1 \\le k \\le N \\le 10^4$",
                            "$0 \\le \\text{Node.val} \\le 10^4$"
                        ],
                        "approach_ladder": {
                            "brute": "Collect ALL $N$ inorder elements into an array and index `arr[k - 1]`: $O(N)$ time & $O(N)$ space even if $k = 1$!",
                            "optimal": "Iterative Inorder Stack stopping **immediately** on the $k$-th pop: push left spine, pop top `cur`, decrement `k` (if `k == 0`: return `cur.val`), then pivot `cur = cur.right`! **$O(H + K)$ time, $O(H)$ stack space**."
                        },
                        "dry_run": "`[3,1,4,None,2], k=2`: push spine `3, 1`; pop `1` (`k=1`), move right -> `2`; push `2`; pop `2` (`k=0`) -> stop early and return **2**!",
                        "edge_cases": [
                            {"title": "k == 1 at Deep Left Leaf vs k == N", "desc": "Ensure loop terminates as soon as `k == 0` cleanly."}
                        ],
                        "follow_ups": "**Order-Statistic Tree (Frequent Updates + Kth Queries):** Augment every `TreeNode` with `subtree_size` so ANY `kthSmallest(k)` runs in strict $O(H) = O(\\log N)$ without scanning $k$ elements!",
                        "hint": "Simulate inorder traversal with an explicit stack so you can return cleanly as soon as the `k`-th node is popped.",
                        "preamble_cpp": "#define DSA_USE_TREENODE 1\n",
                        "starter_py": "class Solution:\n    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:\n        # TODO: Iterative inorder stack with early exit\n        return 0\n",
                        "solution_py": "class Solution:\n    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:\n        st = []\n        cur = root\n        while cur or st:\n            while cur:\n                st.append(cur)\n                cur = cur.left\n            cur = st.pop()\n            k -= 1\n            if k == 0:\n                return cur.val\n            cur = cur.right\n        return -1\n",
                        "harness_py": "_dsa_run_tests([\n    ('Sample 1: k=1', '[3,1,4,None,2], k=1', lambda: Solution().kthSmallest(_dsa_build_tree([3,1,4,None,2]), 1), 1),\n    ('Sample 2: k=3', '[5,3,6,2,4,None,None,1], k=3', lambda: Solution().kthSmallest(_dsa_build_tree([5,3,6,2,4,None,None,1]), 3), 3),\n    ('Edge: k=2 Right Child of Min', '[3,1,4,None,2], k=2', lambda: Solution().kthSmallest(_dsa_build_tree([3,1,4,None,2]), 2), 2),\n    ('Edge: Single Node', '[9], k=1', lambda: Solution().kthSmallest(_dsa_build_tree([9]), 1), 9),\n    ('Edge: Right-Skewed Last', '[1,None,2,None,3,None,4], k=4', lambda: Solution().kthSmallest(_dsa_build_tree([1,None,2,None,3,None,4]), 4), 4),\n], sample_only=__DSA_SAMPLE_ONLY__, n_samples=2)",
                        "starter_cpp": "class Solution {\npublic:\n    int kthSmallest(TreeNode* root, int k) {\n        // TODO: O(H + k) iterative inorder stack\n        return 0;\n    }\n};\n",
                        "solution_cpp": "class Solution {\npublic:\n    int kthSmallest(TreeNode* root, int k) {\n        stack<TreeNode*> st;\n        TreeNode* cur = root;\n        while (cur || !st.empty()) {\n            while (cur) { st.push(cur); cur = cur->left; }\n            cur = st.top(); st.pop();\n            if (--k == 0) return cur->val;\n            cur = cur->right;\n        }\n        return -1;\n    }\n};\n",
                        "harness_cpp": "int main() {\n    ostringstream _dbg; streambuf* _old = cout.rdbuf(_dbg.rdbuf());\n    vector<_DSACaseOut> _res;\n    const int NV = INT_MIN;\n    struct T { string name, inp; vector<int> arr; int k, exp; };\n    vector<T> tests = {\n        {\"Sample 1: k=1\", \"[3,1,4,null,2], k=1\", {3,1,4,NV,2}, 1, 1},\n        {\"Sample 2: k=3\", \"[5,3,6,2,4,null,null,1], k=3\", {5,3,6,2,4,NV,NV,1}, 3, 3},\n        {\"Edge: Right Child of Min\", \"[3,1,4,null,2], k=2\", {3,1,4,NV,2}, 2, 2},\n        {\"Edge: Single Node\", \"[9], k=1\", {9}, 1, 9},\n        {\"Edge: Right-Skewed\", \"[1,null,2,null,3,null,4], k=4\", {1,NV,2,NV,3,NV,4}, 4, 4}\n    };\n    int lim = DSA_SAMPLE_ONLY ? 2 : (int)tests.size();\n    Solution sol;\n    for (int i = 0; i < lim; ++i) {\n        TreeNode* root = _dsa_build_tree(tests[i].arr, NV);\n        auto t0 = chrono::steady_clock::now();\n        int act = sol.kthSmallest(root, tests[i].k);\n        double ms = chrono::duration<double, milli>(chrono::steady_clock::now() - t0).count();\n        _res.push_back({tests[i].name, tests[i].inp, _dsa_fmt(tests[i].exp), _dsa_fmt(act), \"\", act == tests[i].exp, ms});\n    }\n    cout.rdbuf(_old);\n    _dsa_emit_json(_res, _dbg.str());\n    return 0;\n}"
                    }
                ]
            }
        ]
    },
    "15": {
        "title": "Case 15: Dependency Mesh — Graphs I, BFS/DFS & Topological Sort",
        "episodes": [
            {
                "title": "Module 1: Graph Storage, Directed 3-Color Cycles & Kahn's TopoSort",
                "blocks": [
                    {
                        "type": "story",
                        "title": "The False Cycle Alarm in a Diamond DAG",
                        "content": "A naive build-pipeline validator ran simple `visited` DFS to detect dependency cycles (`A -> B`, `A -> C`, `B -> D`, `C -> D`). When reaching already-visited `D` via branch `C`, it falsely flagged a circular dependency!\n\n> [!WARNING]\n> Undirected graphs only need a `visited` set (`neighbor != parent`) for cycle detection. **Directed** graphs require tracking **active recursion path (`state = 1`) vs permanently finished (`state = 2`)**—or **Kahn's BFS Indegree Algorithm**!"
                    },
                    {
                        "type": "objective",
                        "content": "Choose between Adjacency List $O(V + E)$ vs Adjacency Matrix $O(V^2)$, prove directed vs undirected cycle conditions, implement flood-fill BFS/DFS without queue explosion, and construct topological orderings via Kahn's algorithm."
                    },
                    {
                        "type": "concept",
                        "title": "Kahn's Topological Sort & BFS Visited Timing Rule",
                        "content": "1. **Directed Cycle Detection — Kahn's BFS:**\n   - Compute `indegree[u]` for every vertex $0 \\dots V-1$.\n   - Push ALL zero-indegree sources (`indegree[v] == 0`) into a queue.\n   - Pop `u`, increment `processed += 1`, decrement `indegree[nbr] -= 1`; push `nbr` as soon as `indegree[nbr] == 0`.\n   - **Theorem:** The graph is a cycle-free **DAG** iff **`processed == V`** (if a cycle exists, nodes in/downstream of the cycle NEVER reach `indegree == 0`)!\n2. **BFS Duplicate Queue Explosion Bug:**\n   - Mark `grid[nr][nc] = '0'` / `visited[nbr] = True` **AT ENQUEUE TIME (before `push`)**, NEVER when popping from the queue! Waiting until pop causes exponential duplicate pushes of the same grid corner!",
                        "technical_explanation": "**Multi-Source BFS (Rotting Oranges / 01 Matrix):** Seed ALL initially active sources simultaneously into the queue at distance `0` before starting the BFS loop—computing minimum shortest distance from ANY source in a single $O(R \\cdot C)$ sweep!"
                    },
                    {
                        "type": "visual",
                        "title": "3-Color DFS States on Directed Diamond DAG (Safe Revisit!)",
                        "code": "flowchart TD\n  A[\"A (state=1: on stack)\"] --> B[\"B -> D (marks D state=2: finished)\"]\n  A --> C[\"C -> sees D is state=2 (NOT state=1!) => SAFE, NO CYCLE!\"]"
                    },
                    {
                        "type": "interactive",
                        "title": "Why Mark Visited BEFORE Enqueuing in BFS",
                        "question": "In Grid BFS (`Number of Islands` / `Shortest Path in Grid`), why MUST you mark `grid[nr][nc] = '0'` immediately upon pushing `(nr, nc)` instead of after popping?",
                        "options": [
                            "Python deque crashes otherwise",
                            "Marking upon pop lets two neighbors simultaneously enqueue the SAME shared corner cell, cascading into O(2^(R+C)) duplicate queue entries and Memory/Time Limit Exceeded!",
                            "Queue pops in LIFO order otherwise",
                            "Both behave identically in grids"
                        ],
                        "answer": 1,
                        "explanation": "A square cell `(r, c)` has up to 2 or 4 already-queued neighbors that can discover it in the *same* BFS frontier wave. Marking visited immediately upon enqueue guarantees every cell enters the queue **at most once**!"
                    }
                ]
            },
            {
                "title": "Module 2: Edge Orientation in Prerequisites & Adjacency Bounds",
                "blocks": [
                    {
                        "type": "wrong_approach",
                        "title": "Checking Only 2-State `visited` for Directed Cycles",
                        "language": "python",
                        "code": "# Input: A->B, A->C, B->D, C->D (Diamond DAG - VALID, NO CYCLE!)\ndef has_cycle(u):\n    visited.add(u)\n    for v in adj[u]:\n        if v in visited: return True # FALSE POSITIVE on D when arrived from C!\n    return False",
                        "explanation": "Node `D` finished cleanly along `A->B->D` and was popped off the active call stack! Visiting an already-finished (`state=2`) cross/forward edge in a directed graph is completely acyclic; only hitting a currently-active ancestor (`state=1`) proves a back-edge cycle."
                    },
                    {
                        "type": "calculation_challenge",
                        "title": "Adjacency Storage Scaling",
                        "formula": "A sparse graph has $V = 10^5$ vertices and $E = 2 \\times 10^5$ directed edges.",
                        "problem": "How many gigabytes would a naive dense `int[V][V]` ($4$-byte integers) Adjacency Matrix allocate for $V = 10^5$ vertices? (Compute $4 \\times (10^5)^2 / 10^9$ GB cleanly)",
                        "answer": "40",
                        "alternatives": ["40", "40 GB"],
                        "step_by_step": "$(10^5)^2 = 10^{10}$ cells $\\times 4$ bytes $= 4 \\times 10^{10}$ bytes $= 40$ GB (instant Out-Of-Memory!). An Adjacency List stores only $V + E = 3 \\times 10^5$ entries (~5 MB)."
                    }
                ]
            },
            {
                "title": "Module 3: Coding Lab I — Number of Islands (LC-200)",
                "blocks": [
                    {
                        "type": "dsa_problem",
                        "title": "Number of Islands",
                        "platform_style": "LeetCode 200 • Coding Ninjas Grid Graph Classic",
                        "difficulty": "Medium",
                        "pattern": "4-Directional Grid Connected Components (DFS/BFS)",
                        "target_time": "O(R * C)",
                        "target_space": "O(R * C)",
                        "statement": "Given an `m x n` 2D grid of `'1'`s (land) and `'0'`s (water), return the **number of islands**.\n\nAn island is surrounded by water and formed by connecting adjacent lands **horizontally or vertically** (diagonal `'1'`s do NOT connect!).",
                        "examples": [
                            {"input": "grid = [[\"1\",\"1\",\"0\"],[\"1\",\"1\",\"0\"],[\"0\",\"0\",\"1\"]]", "output": "2", "explanation": "Top-left 4 cells form 1 island; bottom-right single '1' forms a 2nd island."},
                            {"input": "grid = [[\"0\",\"0\"],[\"0\",\"0\"]]", "output": "0", "explanation": "No land cells present."}
                        ],
                        "constraints": [
                            "$1 \\le m, n \\le 300$",
                            "`grid[i][j]` is `'0'` or `'1'`."
                        ],
                        "approach_ladder": {
                            "optimal": "Scan every cell `(r, c)`. When `grid[r][c] == '1'`, increment `islands += 1` and run iterative BFS (or DFS) marking every 4-directionally connected `'1'` as `'0'` immediately upon enqueue! **$O(R \\cdot C)$ time** (using iterative queue/stack avoids Python recursion limit crashes on $300 \\times 300$ snakes!)."
                        },
                        "dry_run": "Cell `(0,0) == '1'` increments count -> flood-fills `(0,0),(0,1),(1,0),(1,1)` to `'0'`. Next unvisited `'1'` is `(2,2)` -> increments count to **2**.",
                        "edge_cases": [
                            {"title": "Iterative BFS/Stack vs Python Recursion Limit", "desc": "Python's default recursion depth is `1000`, whereas a snake island in a $300 \\times 300$ grid has path length `45,000`! Iterative BFS queue (`deque`) never overflows the call stack."},
                            {"title": "Diagonal Neighbors Do NOT Merge", "desc": "Only check 4 offsets `[(1,0), (-1,0), (0,1), (0,-1)]`."}
                        ],
                        "follow_ups": "**LC-695 Max Area of Island / LC-994 Rotting Oranges:** Track cell count popped inside each flood-fill to compute island area!",
                        "hint": "Use an iterative `deque` / `queue` marking neighbors `'0'` BEFORE pushing onto the queue so no cell is enqueued twice.",
                        "starter_py": "class Solution:\n    def numIslands(self, grid: List[List[str]]) -> int:\n        # TODO: 4-directional grid BFS/DFS\n        return 0\n",
                        "solution_py": "class Solution:\n    def numIslands(self, grid: List[List[str]]) -> int:\n        if not grid:\n            return 0\n        rows, cols = len(grid), len(grid[0])\n        islands = 0\n        for r in range(rows):\n            for c in range(cols):\n                if grid[r][c] == '1':\n                    islands += 1\n                    grid[r][c] = '0'\n                    q = deque([(r, c)])\n                    while q:\n                        cr, cc = q.popleft()\n                        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):\n                            nr, nc = cr + dr, cc + dc\n                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':\n                                grid[nr][nc] = '0'\n                                q.append((nr, nc))\n        return islands\n",
                        "harness_py": "_dsa_run_tests([\n    ('Sample 1: Two Islands', '3x3 grid', lambda: Solution().numIslands([['1','1','0'],['1','1','0'],['0','0','1']]), 2),\n    ('Sample 2: All Water', '2x2 zeros', lambda: Solution().numIslands([['0','0'],['0','0']]), 0),\n    ('Edge: Diagonal Separate', '[[\"1\",\"0\"],[\"0\",\"1\"]]', lambda: Solution().numIslands([['1','0'],['0','1']]), 2),\n    ('Edge: Single All-Land Grid', '[[\"1\",\"1\"],[\"1\",\"1\"]]', lambda: Solution().numIslands([['1','1'],['1','1']]), 1),\n], sample_only=__DSA_SAMPLE_ONLY__, n_samples=2)",
                        "starter_cpp": "class Solution {\npublic:\n    int numIslands(vector<vector<char>>& grid) {\n        // TODO: O(R*C) BFS flood-fill\n        return 0;\n    }\n};\n",
                        "solution_cpp": "class Solution {\npublic:\n    int numIslands(vector<vector<char>>& grid) {\n        int R = (int)grid.size(), C = R ? (int)grid[0].size() : 0;\n        int islands = 0;\n        const int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};\n        for (int r = 0; r < R; ++r) {\n            for (int c = 0; c < C; ++c) {\n                if (grid[r][c] == '1') {\n                    ++islands;\n                    grid[r][c] = '0';\n                    queue<pair<int,int>> q;\n                    q.push({r, c});\n                    while (!q.empty()) {\n                        auto [cr, cc] = q.front(); q.pop();\n                        for (auto& d : dirs) {\n                            int nr = cr + d[0], nc = cc + d[1];\n                            if (nr >= 0 && nr < R && nc >= 0 && nc < C && grid[nr][nc] == '1') {\n                                grid[nr][nc] = '0';\n                                q.push({nr, nc});\n                            }\n                        }\n                    }\n                }\n            }\n        }\n        return islands;\n    }\n};\n",
                        "harness_cpp": "int main() {\n    ostringstream _dbg; streambuf* _old = cout.rdbuf(_dbg.rdbuf());\n    vector<_DSACaseOut> _res;\n    struct T { string name, inp; vector<vector<char>> g; int exp; };\n    vector<T> tests = {\n        {\"Sample 1: Two Islands\", \"3x3 grid\", {{'1','1','0'},{'1','1','0'},{'0','0','1'}}, 2},\n        {\"Sample 2: All Water\", \"2x2 zeros\", {{'0','0'},{'0','0'}}, 0},\n        {\"Edge: Diagonal Separate\", \"2x2 diag\", {{'1','0'},{'0','1'}}, 2},\n        {\"Edge: All Land\", \"2x2 ones\", {{'1','1'},{'1','1'}}, 1}\n    };\n    int lim = DSA_SAMPLE_ONLY ? 2 : (int)tests.size();\n    Solution sol;\n    for (int i = 0; i < lim; ++i) {\n        auto g = tests[i].g;\n        auto t0 = chrono::steady_clock::now();\n        int act = sol.numIslands(g);\n        double ms = chrono::duration<double, milli>(chrono::steady_clock::now() - t0).count();\n        _res.push_back({tests[i].name, tests[i].inp, _dsa_fmt(tests[i].exp), _dsa_fmt(act), \"\", act == tests[i].exp, ms});\n    }\n    cout.rdbuf(_old);\n    _dsa_emit_json(_res, _dbg.str());\n    return 0;\n}"
                    }
                ]
            },
            {
                "title": "Module 4: Coding Lab II — Course Schedule / Kahn's TopoSort (LC-207)",
                "blocks": [
                    {
                        "type": "dsa_problem",
                        "title": "Course Schedule (Directed Cycle Detection via Kahn's BFS)",
                        "platform_style": "LeetCode 207 • Coding Ninjas Topological Sort Classic",
                        "difficulty": "Medium",
                        "pattern": "Kahn's Indegree Topological Sort (DAG Check)",
                        "target_time": "O(V + E)",
                        "target_space": "O(V + E)",
                        "statement": "There are a total of `numCourses` courses labeled `0` to `numCourses - 1`.\n\nYou are given an array `prerequisites` where `prerequisites[i] = [a_i, b_i]` indicates that you **must take course `b_i` first** if you want to take course `a_i` (`b_i -> a_i`). Return `true` if you can finish all courses (i.e., the directed dependency graph has NO cycle).",
                        "examples": [
                            {"input": "numCourses = 2, prerequisites = [[1, 0]]", "output": "true", "explanation": "Take course 0, then course 1."},
                            {"input": "numCourses = 2, prerequisites = [[1, 0], [0, 1]]", "output": "false", "explanation": "Circular dependency 0 <-> 1 is impossible."}
                        ],
                        "constraints": [
                            "$1 \\le \\text{numCourses} \\le 2000$",
                            "$0 \\le \\text{prerequisites.length} \\le 5000$"
                        ],
                        "approach_ladder": {
                            "better": "3-color DFS detecting any active recursion-stack back-edge (`state[nbr] == 1`).",
                            "optimal": "**Kahn's BFS Topological Sort:** Build `adj[b].append(a)` and increment `indeg[a] += 1`. Enqueue all courses with `indeg[i] == 0`. Pop each `u`, increment `taken += 1`, decrement `indeg[v]` -> push `v` when `indeg[v] == 0`. Return **`taken == numCourses`**! **$O(V + E)$**."
                        },
                        "dry_run": "Diamond DAG `numCourses = 4, prereq = [[1,0],[2,0],[3,1],[3,2]]`: `indeg = [0,1,1,2]`. Queue `[0]` -> drops `1, 2` to `0` (`taken=3`) -> `1, 2` drop `3` from `2->1->0` (`taken=4 == 4`) -> **True**!",
                        "edge_cases": [
                            {"title": "Diamond DAG False-Positive Check", "desc": "Undirected cycle checks or 2-state DFS falsely return `False` on `[[1,0],[2,0],[3,1],[3,2]]`!"},
                            {"title": "Self-Loop Dependency `[0, 0]`", "desc": "Course `0` has `indeg[0] = 1` initially -> queue starts empty -> `taken = 0 != 1` -> **False**."}
                        ],
                        "follow_ups": "**LC-210 Course Schedule II:** Append `u` to `order` inside the BFS pop loop; return `order` if `len(order) == numCourses` else `[]`!",
                        "hint": "Build edges `prereq -> course`, compute `indegree[course]`, and peel off 0-indegree nodes iteratively via a BFS queue.",
                        "starter_py": "class Solution:\n    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:\n        # TODO: Kahn's BFS topological cycle detection in O(V+E)\n        return False\n",
                        "solution_py": "class Solution:\n    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:\n        adj = [[] for _ in range(numCourses)]\n        indeg = [0] * numCourses\n        for a, b in prerequisites:\n            adj[b].append(a)\n            indeg[a] += 1\n        q = deque([i for i in range(numCourses) if indeg[i] == 0])\n        taken = 0\n        while q:\n            u = q.popleft()\n            taken += 1\n            for v in adj[u]:\n                indeg[v] -= 1\n                if indeg[v] == 0:\n                    q.append(v)\n        return taken == numCourses\n",
                        "harness_py": "_dsa_run_tests([\n    ('Sample 1: Valid Chain', 'n=2, [[1,0]]', lambda: Solution().canFinish(2, [[1,0]]), True),\n    ('Sample 2: 2-Cycle', 'n=2, [[1,0],[0,1]]', lambda: Solution().canFinish(2, [[1,0],[0,1]]), False),\n    ('Edge: Diamond DAG (Not Cycle!)', 'n=4, [[1,0],[2,0],[3,1],[3,2]]', lambda: Solution().canFinish(4, [[1,0],[2,0],[3,1],[3,2]]), True),\n    ('Edge: Self Loop', 'n=1, [[0,0]]', lambda: Solution().canFinish(1, [[0,0]]), False),\n    ('Edge: Disconnected No Prereqs', 'n=5, []', lambda: Solution().canFinish(5, []), True),\n], sample_only=__DSA_SAMPLE_ONLY__, n_samples=2)",
                        "starter_cpp": "class Solution {\npublic:\n    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {\n        // TODO: Kahn's BFS Indegree Topological Sort\n        return false;\n    }\n};\n",
                        "solution_cpp": "class Solution {\npublic:\n    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {\n        vector<vector<int>> adj(numCourses);\n        vector<int> indeg(numCourses, 0);\n        for (const auto& e : prerequisites) {\n            adj[e[1]].push_back(e[0]);\n            ++indeg[e[0]];\n        }\n        queue<int> q;\n        for (int i = 0; i < numCourses; ++i) if (indeg[i] == 0) q.push(i);\n        int taken = 0;\n        while (!q.empty()) {\n            int u = q.front(); q.pop();\n            ++taken;\n            for (int v : adj[u]) {\n                if (--indeg[v] == 0) q.push(v);\n            }\n        }\n        return taken == numCourses;\n    }\n};\n",
                        "harness_cpp": "int main() {\n    ostringstream _dbg; streambuf* _old = cout.rdbuf(_dbg.rdbuf());\n    vector<_DSACaseOut> _res;\n    struct T { string name, inp; int n; vector<vector<int>> pre; bool exp; };\n    vector<T> tests = {\n        {\"Sample 1: Valid Chain\", \"n=2, [[1,0]]\", 2, {{1,0}}, true},\n        {\"Sample 2: 2-Cycle\", \"n=2, [[1,0],[0,1]]\", 2, {{1,0},{0,1}}, false},\n        {\"Edge: Diamond DAG\", \"n=4, [[1,0],[2,0],[3,1],[3,2]]\", 4, {{1,0},{2,0},{3,1},{3,2}}, true},\n        {\"Edge: Self Loop\", \"n=1, [[0,0]]\", 1, {{0,0}}, false},\n        {\"Edge: No Prereqs\", \"n=5, []\", 5, {}, true}\n    };\n    int lim = DSA_SAMPLE_ONLY ? 2 : (int)tests.size();\n    Solution sol;\n    for (int i = 0; i < lim; ++i) {\n        auto p = tests[i].pre;\n        auto t0 = chrono::steady_clock::now();\n        bool act = sol.canFinish(tests[i].n, p);\n        double ms = chrono::duration<double, milli>(chrono::steady_clock::now() - t0).count();\n        _res.push_back({tests[i].name, tests[i].inp, _dsa_fmt(tests[i].exp), _dsa_fmt(act), \"\", act == tests[i].exp, ms});\n    }\n    cout.rdbuf(_old);\n    _dsa_emit_json(_res, _dbg.str());\n    return 0;\n}"
                    }
                ]
            }
        ]
    }
}
