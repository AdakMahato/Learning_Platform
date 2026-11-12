# DSA Cases 08 to 11: Linked Lists, Recursion & Backtracking, Stacks/Monotonic, Heaps/Top-K

CASES_PART3 = {
    "8": {
        "title": "Case 08: Pointer Surgery — Linked Lists & Floyd's Cycle Proof",
        "episodes": [
            {
                "title": "Module 1: Sentinel Dummy Heads & Mathematical Proof of Floyd's Cycle",
                "blocks": [
                    {
                        "type": "story",
                        "title": "Segmentation Fault on Empty Head Pointer",
                        "content": "Manipulating linked lists without a dummy sentinel head turns every `head == None` deletion or `k == 1` insertion into fragile branching. Worse, corrupt cyclic next pointers sent traversal loops spinning infinitely in production.\n\n> [!IMPORTANT]\n> **Floyd's Tortoise & Hare Algorithm** detects cycles AND locates the exact cycle entry node using strictly **$O(1)$ auxiliary pointers**—no hash set required!"
                    },
                    {
                        "type": "objective",
                        "content": "Prove Floyd's Tortoise-and-Hare cycle entry distance identity ($a = c + kL$), eliminate special-case head bugs with sentinel Dummy nodes, and execute in-place 3-pointer node reversal cleanly."
                    },
                    {
                        "type": "concept",
                        "title": "Proof of Floyd's Cycle Detection & Entry Point (LC-141 / 142)",
                        "content": "Let `a` be the distance from `head` to the cycle entry node `E`, `b` the distance along the cycle from `E` to the first meeting point `M`, `c` the remainder of the cycle back to `E`, and $L = b + c$ the cycle length.\n\nWhen `slow` (speed 1) meets `fast` (speed 2):\n- Distance of `slow`: $D_s = a + b$\n- Distance of `fast`: $D_f = a + b + kL$ (for some integer $k \\ge 1$ loops)\nSince $D_f = 2 D_s$:\n$$2(a + b) = a + b + kL \\implies a + b = kL \\implies a = (k - 1)L + (L - b) = (k - 1)L + c$$\nTherefore, resetting one pointer to `head` and stepping BOTH pointers by `1` guarantees they collide at **exact cycle entry `E`** after `a` steps!",
                        "technical_explanation": "**Cache Performance vs Arrays:** While Linked Lists provide $O(1)$ splice/delete *given a pointer to the previous node*, traversing element $k$ is $O(N)$ AND scatters nodes across heap memory, defeating CPU cache prefetching. Use `std::list` / linked lists mainly for LRU Cache $O(1)$ iterator stability or intrusive kernel queues."
                    },
                    {
                        "type": "visual",
                        "title": "Three-Pointer In-Place List Reversal Step",
                        "code": "flowchart LR\n  N1[\"nxt = curr.next\"] --> N2[\"curr.next = prev\"]\n  N2 --> N3[\"prev = curr\"]\n  N3 --> N4[\"curr = nxt\"]"
                    },
                    {
                        "type": "interactive",
                        "title": "Floyd Tortoise & Hare Collision Proof",
                        "question": "If a linked list has a cycle of length $L$, and `fast` advances 2 nodes per step while `slow` advances 1 node per step inside the cycle, why can `fast` NEVER jump right past `slow` without ever landing on the same node?",
                        "options": [
                            "Hash sets prevent skipping",
                            "Inside the cycle, their relative gap narrows by exactly `2 - 1 = 1` node per step—closing gap G to G-1, ..., 1, 0 without ever jumping over 0!",
                            "Cycles only have even lengths",
                            "fast resets to head on overflow"
                        ],
                        "answer": 1,
                        "explanation": "Relative velocity is `2 - 1 = +1` step/turn, so the distance from `fast` to `slow` shrinks by `1` every turn (`G -> G-1 -> ... -> 0`). Had `fast` stepped by `3`, relative speed `2` could jump from distance `1` to `-1` over small odd-length cycles!"
                    }
                ]
            },
            {
                "title": "Module 2: Null-Dereference Traps & Sentinel Patterns",
                "blocks": [
                    {
                        "type": "wrong_approach",
                        "title": "Losing Remainder of List & Null-Dereference Loop Condition",
                        "language": "cpp",
                        "code": "// BUG 1: Checking fast->next != nullptr BEFORE checking fast != nullptr!\nwhile (fast->next != nullptr && fast != nullptr) { ... }\n// BUG 2: Checking if (!list1->next) skips empty single-node merge!\n// Wait -> forgetting next_ptr save during reversal breaks chain forever!",
                        "explanation": "Short-circuit boolean checks MUST always test `fast != nullptr` **before** `fast->next != nullptr`! Even a single dereference on `nullptr` triggers immediate `SIGSEGV` Segmentation Fault in C++."
                    },
                    {
                        "type": "correct_approach",
                        "title": "Dummy Sentinel Merge Guard",
                        "language": "cpp",
                        "code": "ListNode dummy(0);\nListNode* tail = &dummy;\nwhile (l1 && l2) {\n    if (l1->val <= l2->val) { tail->next = l1; l1 = l1->next; }\n    else { tail->next = l2; l2 = l2->next; }\n    tail = tail->next;\n}\ntail->next = l1 ? l1 : l2;\nreturn dummy.next;",
                        "explanation": "Stack-allocating `ListNode dummy(0)` avoids dynamic `new` leaks, eliminates `if (!head)` special cases, and cleanly splices any remaining sorted suffix in $O(1)$."
                    },
                    {
                        "type": "calculation_challenge",
                        "title": "Floyd Meeting Distance Calculation",
                        "formula": "Tail before cycle has length $a = 5$ nodes, cycle has length $L = 6$ nodes. Suppose `slow` and `fast` start at `head` (`idx 0`).",
                        "problem": "How many total edges (steps) does `slow` take before `slow == fast` for the first time?",
                        "answer": "6",
                        "alternatives": ["6"],
                        "step_by_step": "After $t = 5$ steps `slow` reaches cycle entry (pos `0 mod 6`) while `fast` is at step `10`, i.e., `10 - 5 = 5 mod 6` inside the cycle. Gap from `fast` behind `slow` is `6 - 5 = 1`, so after `t = 5 + 1 = 6` total steps both meet at `b = 1`!"
                    }
                ]
            },
            {
                "title": "Module 3: Coding Lab I — Reverse Linked List (LC-206)",
                "blocks": [
                    {
                        "type": "dsa_problem",
                        "title": "Reverse Linked List",
                        "platform_style": "LeetCode 206 • Coding Ninjas Pointer Manipulation",
                        "difficulty": "Easy",
                        "pattern": "Three-Pointer Iterative Reversal",
                        "target_time": "O(N)",
                        "target_space": "O(1)",
                        "statement": "Given the `head` of a singly linked list (`ListNode` with `.val` and `.next`), reverse the list in-place, and return the **reversed list's new head**.",
                        "examples": [
                            {"input": "head = [1, 2, 3, 4, 5]", "output": "[5, 4, 3, 2, 1]", "explanation": "All next pointers flip direction without allocating new nodes."},
                            {"input": "head = []", "output": "[]", "explanation": "Empty list returns null / None."}
                        ],
                        "constraints": [
                            "$0 \\le \\text{number of nodes} \\le 5000$",
                            "$-5000 \\le \\text{Node.val} \\le 5000$"
                        ],
                        "approach_ladder": {
                            "brute": "Push node values to an array, reverse array, write back or allocate fresh nodes: $O(N)$ extra space.",
                            "better": "Recursive call `new_head = reverseList(head.next); head.next.next = head; head.next = None;`. Uses $O(N)$ recursion call-stack space.",
                            "optimal": "Track `prev = None, curr = head`. Save `nxt = curr.next`, point `curr.next = prev`, advance `prev = curr, curr = nxt`, finally return `prev`. **$O(N)$ time, strict $O(1)$ space**."
                        },
                        "dry_run": "`1 -> 2 -> None`: step 1 `1->None`, `prev=1, curr=2`; step 2 `2->1->None`, `prev=2, curr=None` -> return `prev` (`2`).",
                        "edge_cases": [
                            {"title": "Empty & 1-Node List", "desc": "`prev = None` automatically handles `head == None` (`return None`) cleanly with zero extra `if` checks."}
                        ],
                        "follow_ups": "**LC-92 Reverse Linked List II / LC-25 Reverse Nodes in k-Group:** Reuse exact 3-pointer reversal over bounded sub-segments `[left..right]`!",
                        "hint": "Always save `nxt = curr.next` BEFORE flipping `curr.next = prev`!",
                        "preamble_cpp": "#define DSA_USE_LISTNODE 1\n",
                        "starter_py": "class Solution:\n    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:\n        # TODO: Iterative O(N) time, O(1) space pointer reversal\n        return None\n",
                        "solution_py": "class Solution:\n    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:\n        prev, curr = None, head\n        while curr:\n            nxt = curr.next\n            curr.next = prev\n            prev = curr\n            curr = nxt\n        return prev\n",
                        "harness_py": "_dsa_run_tests([\n    ('Sample 1: 5 Nodes', '[1,2,3,4,5]', lambda: _dsa_dump_list(Solution().reverseList(_dsa_build_list([1,2,3,4,5]))), [5,4,3,2,1]),\n    ('Sample 2: Empty List', '[]', lambda: _dsa_dump_list(Solution().reverseList(_dsa_build_list([]))), []),\n    ('Edge: Two Nodes', '[1,2]', lambda: _dsa_dump_list(Solution().reverseList(_dsa_build_list([1,2]))), [2,1]),\n    ('Edge: Single Node', '[99]', lambda: _dsa_dump_list(Solution().reverseList(_dsa_build_list([99]))), [99]),\n    ('Edge: Negatives', '[-5,0,5]', lambda: _dsa_dump_list(Solution().reverseList(_dsa_build_list([-5,0,5]))), [5,0,-5]),\n], sample_only=__DSA_SAMPLE_ONLY__, n_samples=2)",
                        "starter_cpp": "class Solution {\npublic:\n    ListNode* reverseList(ListNode* head) {\n        // TODO: Reverse pointers in O(1) space\n        return nullptr;\n    }\n};\n",
                        "solution_cpp": "class Solution {\npublic:\n    ListNode* reverseList(ListNode* head) {\n        ListNode *prev = nullptr, *curr = head;\n        while (curr) {\n            ListNode* nxt = curr->next;\n            curr->next = prev;\n            prev = curr;\n            curr = nxt;\n        }\n        return prev;\n    }\n};\n",
                        "harness_cpp": "int main() {\n    ostringstream _dbg; streambuf* _old = cout.rdbuf(_dbg.rdbuf());\n    vector<_DSACaseOut> _res;\n    struct T { string name, inp; vector<int> arr, exp; };\n    vector<T> tests = {\n        {\"Sample 1: 5 Nodes\", \"[1,2,3,4,5]\", {1,2,3,4,5}, {5,4,3,2,1}},\n        {\"Sample 2: Empty List\", \"[]\", {}, {}},\n        {\"Edge: Two Nodes\", \"[1,2]\", {1,2}, {2,1}},\n        {\"Edge: Single Node\", \"[99]\", {99}, {99}},\n        {\"Edge: Negatives\", \"[-5,0,5]\", {-5,0,5}, {5,0,-5}}\n    };\n    int lim = DSA_SAMPLE_ONLY ? 2 : (int)tests.size();\n    Solution sol;\n    for (int i = 0; i < lim; ++i) {\n        ListNode* h = _dsa_build_list(tests[i].arr);\n        auto t0 = chrono::steady_clock::now();\n        ListNode* out_h = sol.reverseList(h);\n        double ms = chrono::duration<double, milli>(chrono::steady_clock::now() - t0).count();\n        auto act = _dsa_dump_list(out_h);\n        _res.push_back({tests[i].name, tests[i].inp, _dsa_fmt(tests[i].exp), _dsa_fmt(act), \"\", act == tests[i].exp, ms});\n    }\n    cout.rdbuf(_old);\n    _dsa_emit_json(_res, _dbg.str());\n    return 0;\n}"
                    }
                ]
            },
            {
                "title": "Module 4: Coding Lab II — Merge Two Sorted Lists (LC-21)",
                "blocks": [
                    {
                        "type": "dsa_problem",
                        "title": "Merge Two Sorted Linked Lists",
                        "platform_style": "LeetCode 21 • Coding Ninjas Sentinel Dummy Pattern",
                        "difficulty": "Easy",
                        "pattern": "Dummy Head + Two-Way Splice",
                        "target_time": "O(N + M)",
                        "target_space": "O(1)",
                        "statement": "You are given the heads of two sorted linked lists `list1` and `list2`.\n\nMerge the two lists into one **sorted** list by splicing together the nodes of the first two lists, and return the **head of the merged linked list**.",
                        "examples": [
                            {"input": "list1 = [1, 2, 4], list2 = [1, 3, 4]", "output": "[1, 1, 2, 3, 4, 4]", "explanation": "Equal values stay contiguous in ascending order."},
                            {"input": "list1 = [], list2 = [0]", "output": "[0]", "explanation": "One list empty splices the remainder immediately."}
                        ],
                        "constraints": [
                            "$0 \\le \\text{list lengths} \\le 50$",
                            "$-100 \\le \\text{Node.val} \\le 100$"
                        ],
                        "approach_ladder": {
                            "brute": "Collect all values into an array, sort $O((N+M)\\log(N+M))$, allocate brand-new nodes.",
                            "optimal": "Create `dummy = ListNode(0)` and `tail = dummy`. Loop while both `list1` and `list2` are non-null, attaching the smaller node to `tail.next`. After the loop ends, attach **`tail.next = list1 or list2`** in $O(1)$! Return `dummy.next`. **$O(N + M)$ time, $O(1)$ extra space**."
                        },
                        "dry_run": "`[1,4]` + `[2,3]`: splice `1` (`tail->1`), splice `2` (`tail->2`), splice `3` (`tail->3`); `list2` exhausted -> `tail.next = [4]` -> `[1,2,3,4]`.",
                        "edge_cases": [
                            {"title": "Both Empty", "desc": "`dummy.next` defaults to `None` / `nullptr` cleanly."}
                        ],
                        "follow_ups": "**LC-23 Merge k Sorted Lists:** Place the head node of each non-empty list into a Min-Heap of size $k$ to achieve **$O(N \\log k)$** total time!",
                        "hint": "Use a local `dummy` node (`ListNode dummy(0);` in C++) so appending the first node needs zero special branches.",
                        "preamble_cpp": "#define DSA_USE_LISTNODE 1\n",
                        "starter_py": "class Solution:\n    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:\n        # TODO: Splice sorted lists using Dummy Head in O(1) space\n        return None\n",
                        "solution_py": "class Solution:\n    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:\n        dummy = ListNode(0)\n        tail = dummy\n        while list1 and list2:\n            if list1.val <= list2.val:\n                tail.next = list1; list1 = list1.next\n            else:\n                tail.next = list2; list2 = list2.next\n            tail = tail.next\n        tail.next = list1 if list1 else list2\n        return dummy.next\n",
                        "harness_py": "_dsa_run_tests([\n    ('Sample 1: Interleaved', 'l1=[1,2,4], l2=[1,3,4]', lambda: _dsa_dump_list(Solution().mergeTwoLists(_dsa_build_list([1,2,4]), _dsa_build_list([1,3,4]))), [1,1,2,3,4,4]),\n    ('Sample 2: One Empty', 'l1=[], l2=[0]', lambda: _dsa_dump_list(Solution().mergeTwoLists(_dsa_build_list([]), _dsa_build_list([0]))), [0]),\n    ('Edge: Both Empty', 'l1=[], l2=[]', lambda: _dsa_dump_list(Solution().mergeTwoLists(_dsa_build_list([]), _dsa_build_list([]))), []),\n    ('Edge: Disjoint Negatives', 'l1=[-10,-5], l2=[1,2,3]', lambda: _dsa_dump_list(Solution().mergeTwoLists(_dsa_build_list([-10,-5]), _dsa_build_list([1,2,3]))), [-10,-5,1,2,3]),\n    ('Edge: Reversed Tail Longer', 'l1=[5], l2=[1,2,3,4]', lambda: _dsa_dump_list(Solution().mergeTwoLists(_dsa_build_list([5]), _dsa_build_list([1,2,3,4]))), [1,2,3,4,5]),\n], sample_only=__DSA_SAMPLE_ONLY__, n_samples=2)",
                        "starter_cpp": "class Solution {\npublic:\n    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {\n        // TODO: Sentinel dummy splice in O(1) extra space\n        return nullptr;\n    }\n};\n",
                        "solution_cpp": "class Solution {\npublic:\n    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {\n        ListNode dummy(0);\n        ListNode* tail = &dummy;\n        while (list1 && list2) {\n            if (list1->val <= list2->val) { tail->next = list1; list1 = list1->next; }\n            else { tail->next = list2; list2 = list2->next; }\n            tail = tail->next;\n        }\n        tail->next = list1 ? list1 : list2;\n        return dummy.next;\n    }\n};\n",
                        "harness_cpp": "int main() {\n    ostringstream _dbg; streambuf* _old = cout.rdbuf(_dbg.rdbuf());\n    vector<_DSACaseOut> _res;\n    struct T { string name, inp; vector<int> a, b, exp; };\n    vector<T> tests = {\n        {\"Sample 1: Interleaved\", \"[1,2,4] + [1,3,4]\", {1,2,4}, {1,3,4}, {1,1,2,3,4,4}},\n        {\"Sample 2: One Empty\", \"[] + [0]\", {}, {0}, {0}},\n        {\"Edge: Both Empty\", \"[] + []\", {}, {}, {}},\n        {\"Edge: Negatives & Pos\", \"[-10,-5] + [1,2,3]\", {-10,-5}, {1,2,3}, {-10,-5,1,2,3}},\n        {\"Edge: Asymmetric Lengths\", \"[5] + [1,2,3,4]\", {5}, {1,2,3,4}, {1,2,3,4,5}}\n    };\n    int lim = DSA_SAMPLE_ONLY ? 2 : (int)tests.size();\n    Solution sol;\n    for (int i = 0; i < lim; ++i) {\n        ListNode* l1 = _dsa_build_list(tests[i].a);\n        ListNode* l2 = _dsa_build_list(tests[i].b);\n        auto t0 = chrono::steady_clock::now();\n        ListNode* out_h = sol.mergeTwoLists(l1, l2);\n        double ms = chrono::duration<double, milli>(chrono::steady_clock::now() - t0).count();\n        auto act = _dsa_dump_list(out_h);\n        _res.push_back({tests[i].name, tests[i].inp, _dsa_fmt(tests[i].exp), _dsa_fmt(act), \"\", act == tests[i].exp, ms});\n    }\n    cout.rdbuf(_old);\n    _dsa_emit_json(_res, _dbg.str());\n    return 0;\n}"
                    }
                ]
            }
        ]
    },
    "9": {
        "title": "Case 09: The Decision Mirror — Recursion & Backtracking Trees",
        "episodes": [
            {
                "title": "Module 1: Pick/Skip Trees, State Rollback & Complexity Analysis",
                "blocks": [
                    {
                        "type": "story",
                        "title": "Mutating State Across Sibling Branches",
                        "content": "A backtracking solver found one valid branch, then corrupted every subsequent candidate because `path` was modified in-place and never rolled back when popping off the recursion stack!\n\n> [!IMPORTANT]\n> Every backtracking algorithm obeys the 3-step **Choose -> Explore -> Unchoose (`pop_back()`)** symmetry—and remember to **copy** `path` (`list(path)`) when recording a base-case solution!"
                    },
                    {
                        "type": "concept",
                        "title": "Two Canonical Backtracking Templates & Complexity Math",
                        "content": "1. **Pick / Skip Binary Decision Tree (Depth $N$, $2^N$ leaves):** At index `i`, branch left (include `nums[i]`) and right (exclude `nums[i]`). Copying leaves costs $O(N \\cdot 2^N)$.\n2. **Loop-Over-Choices (`for j in range(start, n)`):** Used for **Combinations / Partitioning / Duplicate-Skipping**. Passing `j` (not `j + 1`) allows unlimited reuse of `candidates[j]` (Combination Sum); passing `j + 1` enforces single-use.\n3. **Skipping Duplicates (`LC-90 / LC-40`):** Sort first, then skip same-depth siblings via:\n   `if j > start and nums[j] == nums[j - 1]: continue`\n   (Notice `j > start` skips *horizontal duplicate choices at this recursion depth*, while allowing the same value vertically across child calls!).",
                        "technical_explanation": "**Reference Aliasing Bug:** In Python, `res.append(path)` stores a reference to the mutable list `path`! When backtracking later calls `path.pop()`, every previously saved copy inside `res` shrinks to `[]`! Always append a shallow copy: `res.append(path[:])` or `res.append(list(path))`."
                    },
                    {
                        "type": "visual",
                        "title": "Subset Decision Tree for [1, 2]",
                        "code": "graph TD\n  R[\"start=0, path=[] -> record []\"] --> A[\"pick 1: path=[1] -> record [1]\"]\n  R --> B[\"pick 2: path=[2] -> record [2]\"]\n  A --> C[\"pick 2: path=[1,2] -> record [1,2]\"]"
                    },
                    {
                        "type": "interactive",
                        "title": "Duplicate Skipping Condition Check",
                        "question": "In sorted Subsets II / Combination Sum II, why is the condition `if (i > start && nums[i] == nums[i-1]) continue;` written with `i > start` instead of `i > 0`?",
                        "options": [
                            "i > 0 crashes at index 0",
                            "`i > 0` would forbid picking a duplicate element vertically on the next recursion depth (`[1, 1]`), whereas `i > start` only skips redundant sibling branches at the SAME level!",
                            "Sorting places duplicates at the end",
                            "Both behave identically"
                        ],
                        "answer": 1,
                        "explanation": "On input `[1, 1]`: `path=[1]` recurses with `start=1`. At `i = 1 == start`, we WANT to pick the second `1` to form `[1, 1]`. Skipping happens only when `i > start` (`i=1` at depth 0 where `start=0`), preventing a duplicate `[1]` branch."
                    }
                ]
            },
            {
                "title": "Module 2: Branch Pruning & Call-Stack Bounds",
                "blocks": [
                    {
                        "type": "wrong_approach",
                        "title": "Mutable Reference Bug in Backtracking Collect",
                        "language": "python",
                        "code": "def dfs(i):\n    if i == len(nums):\n        ans.append(path) # BUG: saves reference to same mutable list!\n        return\n    path.append(nums[i]); dfs(i+1); path.pop()\n    dfs(i+1)",
                        "explanation": "At completion every element in `ans` points to the exact same emptied `path` object, producing `[[], [], ..., []]`!"
                    },
                    {
                        "type": "calculation_challenge",
                        "title": "Power Set Cardinality Calculation",
                        "formula": "A set of $N$ distinct elements produces $2^N$ subsets (including the empty subset `[]` and the full set).",
                        "problem": "For `nums = [1, 2, 3, 4, 5, 6]` ($N = 6$), how many subsets are in the power set?",
                        "answer": "64",
                        "alternatives": ["64"],
                        "step_by_step": "$2^6 = 64$ subsets."
                    }
                ]
            },
            {
                "title": "Module 3: Coding Lab I — Subsets / Power Set (LC-78)",
                "blocks": [
                    {
                        "type": "dsa_problem",
                        "title": "Subsets (Power Set via Backtracking)",
                        "platform_style": "LeetCode 78 • Coding Ninjas Recursion Classics",
                        "difficulty": "Medium",
                        "pattern": "Backtracking Pick / Explore / Unchoose",
                        "target_time": "O(N * 2^N)",
                        "target_space": "O(N) recursion + O(N * 2^N) output",
                        "statement": "Given an integer array `nums` of **unique elements**, return **all possible subsets** (the power set).\n\nThe solution set **must not** contain duplicate subsets. Return the subsets in **any order**.",
                        "examples": [
                            {"input": "nums = [1, 2, 3]", "output": "[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]", "explanation": "All 2^3 = 8 subsets of distinct integers."},
                            {"input": "nums = [0]", "output": "[[],[0]]", "explanation": "Power set of 1 element has empty set + singleton."}
                        ],
                        "constraints": [
                            "$1 \\le \\text{nums.length} \\le 10$",
                            "$-10 \\le \\text{nums}[i] \\le 10$",
                            "All integers in `nums` are unique."
                        ],
                        "approach_ladder": {
                            "brute": "Iterative cascading: start `res = [[]]`, for each `x`, append `[curr + [x] for curr in res]`.",
                            "optimal": "Backtracking `dfs(start, path)`: immediately append `list(path)` at EVERY call, then loop `i` from `start..n-1`: `path.append(nums[i]); dfs(i + 1, path); path.pop()`! **$O(N \\cdot 2^N)$**."
                        },
                        "dry_run": "`[1, 2]` -> enter `(0, [])` record `[]` -> `i=0`: push `1`, enter `(1, [1])` record `[1]` -> `i=1`: push `2`, enter `(2, [1,2])` record `[1,2]`, pop `2` -> pop `1` -> `i=1`: push `2`, enter `(2, [2])` record `[2]`.",
                        "edge_cases": [
                            {"title": "Copy Snapshot of Mutable Path", "desc": "Use `path[:]` / `list(path)` in Python when appending to `res`."}
                        ],
                        "follow_ups": "**Bitmask Alternative:** Loop `mask` from `0` to `(1 << n) - 1` and include `nums[i]` whenever `(mask >> i) & 1` is non-zero!",
                        "hint": "Record a copy of `path` on entry to `dfs(start)`, then iterate `i` from `start` to `n - 1` choosing and unchoosing `nums[i]`.",
                        "starter_py": "class Solution:\n    def subsets(self, nums: List[int]) -> List[List[int]]:\n        # TODO: Backtrack all 2^N subsets\n        return []\n",
                        "solution_py": "class Solution:\n    def subsets(self, nums: List[int]) -> List[List[int]]:\n        res, path = [], []\n        def dfs(start: int):\n            res.append(path[:])\n            for i in range(start, len(nums)):\n                path.append(nums[i])\n                dfs(i + 1)\n                path.pop()\n        dfs(0)\n        return res\n",
                        "harness_py": "_norm = lambda x: sorted([sorted(s) for s in x])\n_dsa_run_tests([\n    ('Sample 1: [1,2,3]', '[1,2,3]', lambda: _norm(Solution().subsets([1,2,3])), _norm([[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]])),\n    ('Sample 2: [0]', '[0]', lambda: _norm(Solution().subsets([0])), _norm([[],[0]])),\n    ('Edge: Negatives Pair', '[-2,5]', lambda: _norm(Solution().subsets([-2,5])), _norm([[],[ -2],[5],[-2,5]])),\n    ('Edge: Size 4 Count', '[1,2,3,4]', lambda: len({tuple(sorted(s)) for s in Solution().subsets([1,2,3,4])}), 16),\n], sample_only=__DSA_SAMPLE_ONLY__, n_samples=2)",
                        "starter_cpp": "class Solution {\npublic:\n    vector<vector<int>> subsets(vector<int>& nums) {\n        // TODO: Backtracking DFS with push_back/pop_back\n        return {};\n    }\n};\n",
                        "solution_cpp": "class Solution {\n    void dfs(int start, const vector<int>& nums, vector<int>& path, vector<vector<int>>& res) {\n        res.push_back(path);\n        for (int i = start; i < (int)nums.size(); ++i) {\n            path.push_back(nums[i]);\n            dfs(i + 1, nums, path, res);\n            path.pop_back();\n        }\n    }\npublic:\n    vector<vector<int>> subsets(vector<int>& nums) {\n        vector<vector<int>> res;\n        vector<int> path;\n        dfs(0, nums, path, res);\n        return res;\n    }\n};\n",
                        "harness_cpp": "static vector<vector<int>> _norm(vector<vector<int>> g) {\n    for (auto& r : g) sort(r.begin(), r.end());\n    sort(g.begin(), g.end());\n    return g;\n}\nint main() {\n    ostringstream _dbg; streambuf* _old = cout.rdbuf(_dbg.rdbuf());\n    vector<_DSACaseOut> _res;\n    struct T { string name, inp; vector<int> arr; vector<vector<int>> exp; };\n    vector<T> tests = {\n        {\"Sample 1: [1,2,3]\", \"[1,2,3]\", {1,2,3}, {{},{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}}},\n        {\"Sample 2: [0]\", \"[0]\", {0}, {{},{0}}},\n        {\"Edge: Negatives Pair\", \"[-2,5]\", {-2,5}, {{},{-2},{5},{-2,5}}}\n    };\n    int lim = DSA_SAMPLE_ONLY ? 2 : (int)tests.size();\n    Solution sol;\n    for (int i = 0; i < lim; ++i) {\n        auto v = tests[i].arr;\n        auto t0 = chrono::steady_clock::now();\n        auto act = _norm(sol.subsets(v));\n        auto exp = _norm(tests[i].exp);\n        double ms = chrono::duration<double, milli>(chrono::steady_clock::now() - t0).count();\n        _res.push_back({tests[i].name, tests[i].inp, _dsa_fmt(exp), _dsa_fmt(act), \"\", act == exp, ms});\n    }\n    cout.rdbuf(_old);\n    _dsa_emit_json(_res, _dbg.str());\n    return 0;\n}"
                    }
                ]
            },
            {
                "title": "Module 4: Coding Lab II — Combination Sum (LC-39)",
                "blocks": [
                    {
                        "type": "dsa_problem",
                        "title": "Combination Sum (Unbounded Reuse with Pruning)",
                        "platform_style": "LeetCode 39 • Coding Ninjas Backtracking Track",
                        "difficulty": "Medium",
                        "pattern": "Backtracking Reuse Index + Sorted Pruning",
                        "target_time": "O(N^(T/M + 1))",
                        "target_space": "O(T / M)",
                        "statement": "Given an array of **distinct positive integers** `candidates` and a target integer `target`, return a list of all **unique combinations** of `candidates` where the chosen numbers sum to `target` (you may return combinations in any order).\n\nThe **same number** may be chosen from `candidates` an **unlimited number of times**!",
                        "examples": [
                            {"input": "candidates = [2,3,6,7], target = 7", "output": "[[2,2,3],[7]]", "explanation": "2+2+3 = 7 and 7 = 7; permutations like [3,2,2] count as duplicates so index only moves >= start."},
                            {"input": "candidates = [2], target = 1", "output": "[]", "explanation": "No combination equals 1."}
                        ],
                        "constraints": [
                            "$1 \\le \\text{candidates.length} \\le 30$",
                            "$2 \\le \\text{candidates}[i] \\le 40$, all distinct",
                            "$1 \\le \\text{target} \\le 40$"
                        ],
                        "approach_ladder": {
                            "brute": "Explore unconstrained permutations ignoring order -> produces duplicates `[2,2,3]`, `[2,3,2]`, `[3,2,2]`!",
                            "optimal": "Sort `candidates`. In `dfs(start, rem, path)`: if `rem == 0`, snapshot `path`; else iterate `i` from `start` to `n-1`. If `candidates[i] > rem`, **`break` immediately** (pruning!). Recurse passing **`i`** (NOT `i + 1`, allowing reuse while blocking smaller prior indices!)."
                        },
                        "dry_run": "`[2,3,6,7], target=7`: pick `2 (rem=5)` -> `2 (rem=3)` -> `2 (rem=1, loop 2>1 breaks)` -> pop `2` -> `3 (rem=0 -> record [2,2,3])`.",
                        "edge_cases": [
                            {"title": "Order-Agnostic Dedup via Non-Decreasing Index", "desc": "Passing `i` rather than `0` in loops guarantees elements stay in non-decreasing index order `[2,2,3]`, NEVER generating `[3,2,2]`!"}
                        ],
                        "follow_ups": "**LC-40 Combination Sum II:** Sort + skip `i > start and c[i] == c[i-1]` + recurse with `i + 1` (each element used at most once).",
                        "hint": "Sort `candidates` first to prune `if cand > rem: break`, and recurse from index `i` (allowing unlimited reuse without permutation duplicates).",
                        "starter_py": "class Solution:\n    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:\n        # TODO: Unbounded combination backtracking\n        return []\n",
                        "solution_py": "class Solution:\n    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:\n        candidates.sort()\n        res, path = [], []\n        def dfs(start: int, rem: int):\n            if rem == 0:\n                res.append(path[:])\n                return\n            for i in range(start, len(candidates)):\n                c = candidates[i]\n                if c > rem:\n                    break\n                path.append(c)\n                dfs(i, rem - c)\n                path.pop()\n        dfs(0, target)\n        return res\n",
                        "harness_py": "_norm = lambda g: sorted([sorted(r) for r in g])\n_dsa_run_tests([\n    ('Sample 1: target=7', '[2,3,6,7], t=7', lambda: _norm(Solution().combinationSum([2,3,6,7], 7)), _norm([[2,2,3],[7]])),\n    ('Sample 2: Impossible', '[2], t=1', lambda: _norm(Solution().combinationSum([2], 1)), []),\n    ('Edge: Multiple Ways t=8', '[2,3,5], t=8', lambda: _norm(Solution().combinationSum([2,3,5], 8)), _norm([[2,2,2,2],[2,3,3],[3,5]])),\n    ('Edge: Unsorted Input', '[7,3,2], t=7', lambda: _norm(Solution().combinationSum([7,3,2], 7)), _norm([[2,2,3],[7]])),\n], sample_only=__DSA_SAMPLE_ONLY__, n_samples=2)",
                        "starter_cpp": "class Solution {\npublic:\n    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {\n        // TODO: Sorted pruning + non-decreasing index DFS\n        return {};\n    }\n};\n",
                        "solution_cpp": "class Solution {\n    void dfs(int start, int rem, const vector<int>& c, vector<int>& path, vector<vector<int>>& res) {\n        if (rem == 0) { res.push_back(path); return; }\n        for (int i = start; i < (int)c.size(); ++i) {\n            if (c[i] > rem) break;\n            path.push_back(c[i]);\n            dfs(i, rem - c[i], c, path, res);\n            path.pop_back();\n        }\n    }\npublic:\n    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {\n        sort(candidates.begin(), candidates.end());\n        vector<vector<int>> res;\n        vector<int> path;\n        dfs(0, target, candidates, path, res);\n        return res;\n    }\n};\n",
                        "harness_cpp": "static vector<vector<int>> _norm(vector<vector<int>> g) {\n    for (auto& r : g) sort(r.begin(), r.end());\n    sort(g.begin(), g.end());\n    return g;\n}\nint main() {\n    ostringstream _dbg; streambuf* _old = cout.rdbuf(_dbg.rdbuf());\n    vector<_DSACaseOut> _res;\n    struct T { string name, inp; vector<int> arr; int t; vector<vector<int>> exp; };\n    vector<T> tests = {\n        {\"Sample 1: target=7\", \"[2,3,6,7], t=7\", {2,3,6,7}, 7, {{2,2,3},{7}}},\n        {\"Sample 2: Impossible\", \"[2], t=1\", {2}, 1, {}},\n        {\"Edge: Multi Ways t=8\", \"[2,3,5], t=8\", {2,3,5}, 8, {{2,2,2,2},{2,3,3},{3,5}}},\n        {\"Edge: Unsorted Input\", \"[7,3,2], t=7\", {7,3,2}, 7, {{2,2,3},{7}}}\n    };\n    int lim = DSA_SAMPLE_ONLY ? 2 : (int)tests.size();\n    Solution sol;\n    for (int i = 0; i < lim; ++i) {\n        auto v = tests[i].arr;\n        auto t0 = chrono::steady_clock::now();\n        auto act = _norm(sol.combinationSum(v, tests[i].t));\n        auto exp = _norm(tests[i].exp);\n        double ms = chrono::duration<double, milli>(chrono::steady_clock::now() - t0).count();\n        _res.push_back({tests[i].name, tests[i].inp, _dsa_fmt(exp), _dsa_fmt(act), \"\", act == exp, ms});\n    }\n    cout.rdbuf(_old);\n    _dsa_emit_json(_res, _dbg.str());\n    return 0;\n}"
                    }
                ]
            }
        ]
    },
    "10": {
        "title": "Case 10: The Monotonic Skyline — Stacks, Queues & Next Greater",
        "episodes": [
            {
                "title": "Module 1: Amortized O(N) Monotonic Stacks & Ring Buffers",
                "blocks": [
                    {
                        "type": "story",
                        "title": "Finding Next Warmer Peaks in Linear Time",
                        "content": "Given 100,000 daily latency readings, engineers need to know for EVERY day: *how many days until a strictly higher spike arrives?* Nested loops scan forward in $O(N^2)$.\n\n> [!TIP]\n> A **Monotonic Decreasing Stack** resolves ALL future waiting indices the exact moment a larger value arrives—every element is pushed **once** and popped **at most once**, proving strict $O(N)$ runtime!"
                    },
                    {
                        "type": "concept",
                        "title": "When & How Monotonic Stack Works",
                        "content": "Maintain a stack of **unresolved indices** whose values strictly descend from bottom to top (`nums[st[0]] >= nums[st[1]] >= ...`).\n\nWhen new element `x = nums[i]` arrives:\n- While stack non-empty AND **`x > nums[st[-1]]`** (strictly warmer / next greater!):\n  Pop index `prev_idx = st.pop()`. Since `x` is the **first** strictly greater value to `prev_idx`'s right, set `ans[prev_idx] = i - prev_idx` (distance) or `x` (next greater value)!\n- Push `i` onto `st`.\n\n**Stack vs Queue Ring Buffer Note:** Circular arrays store bounded FIFO queues without shifting elements via `(tail + 1) % cap` and distinguish full vs empty via a stored `size` counter (or reserving 1 empty slot).",
                        "technical_explanation": "**Next Smaller vs Next Greater & Histogram Area (LC-84):** Storing a monotonic *increasing* stack pops whenever a shorter bar arrives at right boundary `i`; the popped height `H` extends left all the way to the *new stack top + 1*, solving Largest Rectangle in Histogram in a single $O(N)$ pass!"
                    },
                    {
                        "type": "visual",
                        "title": "Monotonic Stack Resolution on New Peak",
                        "code": "flowchart LR\n  IN[\"Incoming T[i] = 75\"] --> CHK{\"Stack top T[idx] < 75?\"}\n  CHK -->|Yes| POP[\"Pop idx, record ans[idx] = i - idx, repeat!\"]\n  CHK -->|No| PUSH[\"Push i onto stack\"]"
                    },
                    {
                        "type": "interactive",
                        "title": "Why Nested Stack While-Loop Is O(N), Not O(N^2)",
                        "question": "A `while` loop runs inside a `for i in range(N):` loop in Monotonic Stack algorithms. Why is total time complexity $\\Theta(N)$ instead of $\\Theta(N^2)$?",
                        "options": [
                            "The stack size never exceeds 10",
                            "Even though one iteration can pop many elements, each of the N indices can be pushed onto the stack ONCE and popped AT MOST ONCE across the entire algorithm (<= 2N total ops)",
                            "While loops run in parallel",
                            "Because inputs are pre-sorted"
                        ],
                        "answer": 1,
                        "explanation": "Aggregate amortized analysis: total pops across ALL $N$ iterations cannot exceed total pushes ($N$), so `for + while` runs at most $2N = O(N)$ iterations overall."
                    }
                ]
            },
            {
                "title": "Module 2: Delimiter Nesting & Stack Underflow Edge Cases",
                "blocks": [
                    {
                        "type": "debugger",
                        "title": "Closing Bracket Before Opening Crash",
                        "scenario": "Analyze this bracket checker on input `s = \"]\"`:\n```python\nfor ch in s:\n    if ch in '([{': stack.append(ch)\n    elif match[ch] != stack.pop(): return False\nreturn True\n```\nWhich TWO bugs break this implementation?",
                        "options": [
                            "None — it returns False properly",
                            "(1) Calling `stack.pop()` when `stack` is empty throws IndexError on `\"]\"`, and (2) `return True` misses leftover unclosed `'('` (`not stack` required!)",
                            "Only bug (2)",
                            "Strings cannot use `in`"
                        ],
                        "answer": 1,
                        "explanation": "1) Check `if not stack or stack.pop() != match[ch]: return False` to handle stray closing brackets; 2) finish with `return len(stack) == 0` so unclosed `\"((\"` returns `False`!"
                    },
                    {
                        "type": "calculation_challenge",
                        "title": "Monotonic Stack Pop Count Trace",
                        "formula": "Process array `[73, 74, 75, 71, 69, 72, 76, 73]` left to right using a monotonic decreasing stack (push index after popping strictly smaller values).",
                        "problem": "How many elements are **popped** when `76` arrives at index `6`? (Stack currently holds `[75, 71, 69]` -> wait: check what arrived before `76`! Trace `72` popped `69` and `71`, leaving `[75, 72]`!)",
                        "answer": "2",
                        "alternatives": ["2"],
                        "step_by_step": "Before `76`: `73` pushed, `74` popped `73`, `75` popped `74`, `71` pushed, `69` pushed, `72` popped `69 & 71` leaving `[75, 72]`. When `76` arrives, it pops **`72` and `75`** = **2** elements!"
                    }
                ]
            },
            {
                "title": "Module 3: Coding Lab I — Valid Parentheses (LC-20)",
                "blocks": [
                    {
                        "type": "dsa_problem",
                        "title": "Valid Parentheses",
                        "platform_style": "LeetCode 20 • Coding Ninjas Stack Essentials",
                        "difficulty": "Easy",
                        "pattern": "LIFO Delimiter Matching Stack",
                        "target_time": "O(N)",
                        "target_space": "O(N)",
                        "statement": "Given a string `s` containing only characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is **valid**.\n\nBrackets must close in the **correct LIFO order** and every open bracket must be closed by the matching type.",
                        "examples": [
                            {"input": "s = \"()[]{}\"", "output": "true", "explanation": "Each pair opens and immediately closes in matching type."},
                            {"input": "s = \"([)]\"", "output": "false", "explanation": "Counters alone fail here! LIFO order requires closing '[' before ')'."}
                        ],
                        "constraints": [
                            "$1 \\le s.\\text{length} \\le 10^4$"
                        ],
                        "approach_ladder": {
                            "brute": "Repeatedly strip `\"()\"`, `\"[]\"`, `\"{}\"` substrings until unchanged: $O(N^2)$ time.",
                            "optimal": "Push opening brackets (or push their *expected closing bracket*!) onto a stack. On a closing char, verify non-empty stack AND matching top. End with `return len(st) == 0`! **$O(N)$ time, $O(N)$ space**."
                        },
                        "dry_run": "`\"([{}])\"` pushes `'('`, `'['`, `'{'`, pops `'}'`, `']'`, `')'` -> stack empty -> **True**.",
                        "edge_cases": [
                            {"title": "Stray Closer `\"]\"` & Odd Length", "desc": "Always guard `not stack` before reading `stack[-1]` / `st.top()`."},
                            {"title": "Unclosed Tail `\"(((\"`", "desc": "Never `return True` blindly at loop end; must check `len(stack) == 0`."}
                        ],
                        "follow_ups": "**LC-32 Longest Valid Parentheses:** Push indices (seeded with `-1` sentinel) onto a stack instead of characters!",
                        "hint": "Map each closing bracket to its expected opener (or push expected closer on open), and guard empty stack before popping.",
                        "starter_py": "class Solution:\n    def isValid(self, s: str) -> bool:\n        # TODO: LIFO stack delimiter validation\n        return False\n",
                        "solution_py": "class Solution:\n    def isValid(self, s: str) -> bool:\n        pair = {')': '(', ']': '[', '}': '{'}\n        st = []\n        for ch in s:\n            if ch in pair:\n                if not st or st[-1] != pair[ch]:\n                    return False\n                st.pop()\n            else:\n                st.append(ch)\n        return not st\n",
                        "harness_py": "_dsa_run_tests([\n    ('Sample 1: Multi Pairs', 's=\"()[]{}\"', lambda: Solution().isValid('()[]{}'), True),\n    ('Sample 2: Crossed Nest', 's=\"([)]\"', lambda: Solution().isValid('([)]'), False),\n    ('Edge: Stray Closer', 's=\"]\"', lambda: Solution().isValid(']'), False),\n    ('Edge: Unclosed Open', 's=\"(((\"', lambda: Solution().isValid('((('), False),\n    ('Edge: Deep Valid Nest', 's=\"{[()]}\"', lambda: Solution().isValid('{[()]}'), True),\n], sample_only=__DSA_SAMPLE_ONLY__, n_samples=2)",
                        "starter_cpp": "class Solution {\npublic:\n    bool isValid(string s) {\n        // TODO: O(N) LIFO stack validation\n        return false;\n    }\n};\n",
                        "solution_cpp": "class Solution {\npublic:\n    bool isValid(string s) {\n        stack<char> st;\n        for (char c : s) {\n            if (c == '(') st.push(')');\n            else if (c == '[') st.push(']');\n            else if (c == '{') st.push('}');\n            else {\n                if (st.empty() || st.top() != c) return false;\n                st.pop();\n            }\n        }\n        return st.empty();\n    }\n};\n",
                        "harness_cpp": "int main() {\n    ostringstream _dbg; streambuf* _old = cout.rdbuf(_dbg.rdbuf());\n    vector<_DSACaseOut> _res;\n    struct T { string name, inp, s; bool exp; };\n    vector<T> tests = {\n        {\"Sample 1: Multi Pairs\", \"()[]{}\", \"()[]{}\", true},\n        {\"Sample 2: Crossed Nest\", \"([)]\", \"([)]\", false},\n        {\"Edge: Stray Closer\", \"]\", \"]\", false},\n        {\"Edge: Unclosed Open\", \"(((\", \"(((\", false},\n        {\"Edge: Deep Valid Nest\", \"{[()]}\", \"{[()]}\", true}\n    };\n    int lim = DSA_SAMPLE_ONLY ? 2 : (int)tests.size();\n    Solution sol;\n    for (int i = 0; i < lim; ++i) {\n        auto t0 = chrono::steady_clock::now();\n        bool act = sol.isValid(tests[i].s);\n        double ms = chrono::duration<double, milli>(chrono::steady_clock::now() - t0).count();\n        _res.push_back({tests[i].name, tests[i].inp, _dsa_fmt(tests[i].exp), _dsa_fmt(act), \"\", act == tests[i].exp, ms});\n    }\n    cout.rdbuf(_old);\n    _dsa_emit_json(_res, _dbg.str());\n    return 0;\n}"
                    }
                ]
            },
            {
                "title": "Module 4: Coding Lab II — Daily Temperatures / Monotonic Stack (LC-739)",
                "blocks": [
                    {
                        "type": "dsa_problem",
                        "title": "Daily Temperatures (Next Greater Element Distance)",
                        "platform_style": "LeetCode 739 • Coding Ninjas Monotonic Stack Classic",
                        "difficulty": "Medium",
                        "pattern": "Monotonic Decreasing Index Stack",
                        "target_time": "O(N)",
                        "target_space": "O(N)",
                        "statement": "Given an array of integers `temperatures`, return an array `answer` such that `answer[i]` is the **number of days you have to wait** after the $i$-th day to get a **strictly warmer** temperature.\n\nIf there is no future day with a warmer temperature, set `answer[i] = 0`.",
                        "examples": [
                            {"input": "temperatures = [73,74,75,71,69,72,76,73]", "output": "[1,1,4,2,1,1,0,0]", "explanation": "After 75 (idx 2), wait 4 days for 76 (idx 6)."},
                            {"input": "temperatures = [30,40,50,60]", "output": "[1,1,1,0]", "explanation": "Strictly increasing temps wait 1 day except the last."}
                        ],
                        "constraints": [
                            "$1 \\le \\text{temperatures.length} \\le 10^5$",
                            "$30 \\le \\text{temperatures}[i] \\le 100$"
                        ],
                        "approach_ladder": {
                            "brute": "For each `i`, scan `j = i+1..n-1` until `t[j] > t[i]`: $O(N^2)$ -> TLE on strictly descending `temperatures`!",
                            "optimal": "Initialize `ans = [0] * n` and stack `st = []` holding indices. For `i, temp in enumerate(temperatures)`: while `st` and `temp > temperatures[st[-1]]`, `prev = st.pop(); ans[prev] = i - prev`. Append `i`. **$O(N)$ amortized time, $O(N)$ space**."
                        },
                        "dry_run": "Duplicate values `[70, 70, 71]`: second `70` is NOT strictly `> 70`, so `[0, 1]` stay stacked until `71` arrives at `2`, popping BOTH (`ans[1] = 1, ans[0] = 2`)!",
                        "edge_cases": [
                            {"title": "Strictly Decreasing & Equal Temperatures", "desc": "Equal temperatures do NOT pop earlier ones—must use strict `>` comparison! Unresolved indices naturally remain `0`."}
                        ],
                        "follow_ups": "**LC-496 / LC-503:** Next Greater Element I & Circular Next Greater Element II (loop index `i % n` from `0` to `2n - 1`!).",
                        "hint": "Store array **indices** (not raw temperatures!) in a stack ordered monotonically decreasing by temperature.",
                        "starter_py": "class Solution:\n    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:\n        # TODO: Monotonic decreasing index stack in O(N)\n        return []\n",
                        "solution_py": "class Solution:\n    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:\n        n = len(temperatures)\n        ans = [0] * n\n        st = []\n        for i, t in enumerate(temperatures):\n            while st and t > temperatures[st[-1]]:\n                prev = st.pop()\n                ans[prev] = i - prev\n            st.append(i)\n        return ans\n",
                        "harness_py": "_dsa_run_tests([\n    ('Sample 1: Standard Profile', '[73,74,75,71,69,72,76,73]', lambda: Solution().dailyTemperatures([73,74,75,71,69,72,76,73]), [1,1,4,2,1,1,0,0]),\n    ('Sample 2: Ascending', '[30,40,50,60]', lambda: Solution().dailyTemperatures([30,40,50,60]), [1,1,1,0]),\n    ('Edge: Equal Temperatures', '[70,70,71]', lambda: Solution().dailyTemperatures([70,70,71]), [2,1,0]),\n    ('Edge: Strictly Decreasing', '[90,80,70,60]', lambda: Solution().dailyTemperatures([90,80,70,60]), [0,0,0,0]),\n    ('Edge: Single Day', '[55]', lambda: Solution().dailyTemperatures([55]), [0]),\n], sample_only=__DSA_SAMPLE_ONLY__, n_samples=2)",
                        "starter_cpp": "class Solution {\npublic:\n    vector<int> dailyTemperatures(vector<int>& temperatures) {\n        // TODO: O(N) Monotonic Stack\n        return {};\n    }\n};\n",
                        "solution_cpp": "class Solution {\npublic:\n    vector<int> dailyTemperatures(vector<int>& temperatures) {\n        int n = (int)temperatures.size();\n        vector<int> ans(n, 0);\n        stack<int> st;\n        for (int i = 0; i < n; ++i) {\n            while (!st.empty() && temperatures[i] > temperatures[st.top()]) {\n                int prev = st.top(); st.pop();\n                ans[prev] = i - prev;\n            }\n            st.push(i);\n        }\n        return ans;\n    }\n};\n",
                        "harness_cpp": "int main() {\n    ostringstream _dbg; streambuf* _old = cout.rdbuf(_dbg.rdbuf());\n    vector<_DSACaseOut> _res;\n    struct T { string name, inp; vector<int> arr, exp; };\n    vector<T> tests = {\n        {\"Sample 1: Standard Profile\", \"[73,74,75,71,69,72,76,73]\", {73,74,75,71,69,72,76,73}, {1,1,4,2,1,1,0,0}},\n        {\"Sample 2: Ascending\", \"[30,40,50,60]\", {30,40,50,60}, {1,1,1,0}},\n        {\"Edge: Equal Temps\", \"[70,70,71]\", {70,70,71}, {2,1,0}},\n        {\"Edge: Descending\", \"[90,80,70,60]\", {90,80,70,60}, {0,0,0,0}},\n        {\"Edge: Single Day\", \"[55]\", {55}, {0}}\n    };\n    int lim = DSA_SAMPLE_ONLY ? 2 : (int)tests.size();\n    Solution sol;\n    for (int i = 0; i < lim; ++i) {\n        auto v = tests[i].arr;\n        auto t0 = chrono::steady_clock::now();\n        auto act = sol.dailyTemperatures(v);\n        double ms = chrono::duration<double, milli>(chrono::steady_clock::now() - t0).count();\n        _res.push_back({tests[i].name, tests[i].inp, _dsa_fmt(tests[i].exp), _dsa_fmt(act), \"\", act == tests[i].exp, ms});\n    }\n    cout.rdbuf(_old);\n    _dsa_emit_json(_res, _dbg.str());\n    return 0;\n}"
                    }
                ]
            }
        ]
    },
    "11": {
        "title": "Case 11: Priority Dispatcher — Binary Heaps & Top-K Streams",
        "episodes": [
            {
                "title": "Module 1: Binary Heap Layout, O(N) Heapify Proof & Top-K Pattern",
                "blocks": [
                    {
                        "type": "story",
                        "title": "Top-100 Heavy Hitters in a Billion Events",
                        "content": "Sorting $N = 10^8$ telemetry records takes $O(N \\log N)$ time and holds all records in memory just to read the top $K = 100$. Using a **Min-Heap of fixed size $K$** inspects every item in one stream pass in $O(N \\log K)$ time and $O(K)$ RAM!\n\n> [!NOTE]\n> Counter-intuitive interview rule: To find the **K Largest**, always maintain a **MIN-Heap** of size $K$ (evicting the weakest element whenever size exceeds $K$); to find the **K Smallest**, maintain a **MAX-Heap** of size $K$!"
                    },
                    {
                        "type": "concept",
                        "title": "Array Indexing & Proof that Floyd's Build-Heap Is O(N)",
                        "content": "A Binary Heap is a **Complete Binary Tree** packed contiguously in a 0-indexed array:\n- Left Child of `i`: `2*i + 1` | Right Child: `2*i + 2` | Parent: `(i - 1) // 2`\n- All leaf nodes occupy `[N//2 .. N-1]`.\n\n**Why Floyd's Bottom-Up `heapify()` (`for i in range(N//2 - 1, -1, -1)`) runs in $\\Theta(N)$ (NOT $O(N \\log N)$):**\nHalf the nodes are leaves (height `0`, `0` swaps). At height $h$, at most $\\lceil N / 2^{h+1} \\rceil$ nodes sift down by at most $h$ levels:\n$$T(N) \\le \\sum_{h=0}^{\\lfloor \\log_2 N \\rfloor} \\frac{N}{2^{h+1}} \\cdot h = \\frac{N}{2} \\sum_{h=0}^{\\infty} \\frac{h}{2^h} = \\frac{N}{2} \\cdot 2 = O(N)$$",
                        "technical_explanation": "**C++ vs Python Priority Queue Defaults:** C++ `priority_queue<int>` is a **MAX-heap** by default (`greater<int>` converts to MIN-heap: `priority_queue<int, vector<int>, greater<int>>`). Python `heapq` is strictly a **MIN-heap** by default (negate numbers `-x` or use `(freq, key)` tuples carefully!)."
                    },
                    {
                        "type": "comparison_table",
                        "title": "Finding Kth Largest Element Trade-offs",
                        "headers": ["Approach", "Time Complexity", "Extra Space", "Streaming Support?"],
                        "rows": [
                            ["Full Sort", "O(N log N)", "O(1) - O(N)", "No (needs full array)"],
                            ["Max-Heap + K Pops", "O(N + K log N)", "O(N)", "No (stores all N)"],
                            ["Min-Heap of Size K", "O(N log K)", "O(K)", "Yes (single stream pass!)"],
                            ["Bucket Sort (Top K Frequent)", "O(N)", "O(N)", "Offline frequency map"],
                            ["Quickselect (Hoare Randomized)", "O(N) avg / O(N^2) worst", "O(1) iterative", "No (mutates array)"]
                        ]
                    },
                    {
                        "type": "interactive",
                        "title": "Min-Heap vs Max-Heap for Kth Largest",
                        "question": "Why does maintaining a Min-Heap of capacity $K$ yield the Kth **largest** element faster than a Max-Heap of all $N$ elements when $K \\ll N$?",
                        "options": [
                            "Min-Heaps ignore duplicate values",
                            "A Min-Heap of size K immediately peeks and evicts the smallest among top-K candidates in O(log K) per item and stores only O(K) RAM instead of O(N)",
                            "Max-Heaps take O(N^2) to build",
                            "Min-Heaps support binary search directly"
                        ],
                        "answer": 1,
                        "explanation": "Holding only `K` items keeps every push/pop at $O(\\log K)$ and memory at $O(K)$. After scanning all `N` elements, the root `heap[0]` is strictly the smallest of the top `K` elements—i.e., the exact Kth largest!"
                    }
                ]
            },
            {
                "title": "Module 2: Heap Array Index & Bucket Sort Optimization",
                "blocks": [
                    {
                        "type": "calculation_challenge",
                        "title": "0-Indexed Complete Binary Tree Parent/Child Math",
                        "formula": "In a 0-indexed binary heap stored in array `H`, node `i` has children `2i+1` and `2i+2`, and parent `(i-1)//2`.",
                        "problem": "In a heap of 15 elements (`indices 0..14`), what is the index of the **parent** of node `i = 12`?",
                        "answer": "5",
                        "alternatives": ["5"],
                        "step_by_step": "`(12 - 1) // 2 = 11 // 2 = 5` (indeed, node `5`'s children are `2*5+1 = 11` and `2*5+2 = 12`!)."
                    },
                    {
                        "type": "wrong_approach",
                        "title": "Non-Comparable Payload Tuple Crash in heapq",
                        "language": "python",
                        "code": "heapq.heappush(hq, (priority, custom_node_obj))\n# TypeError: '<' not supported between instances of 'Node' and 'Node'!",
                        "explanation": "When two elements share equal `priority`, Python's `heapq` breaks ties by comparing the **next tuple item** (`custom_node_obj < custom_node_obj`). Always insert a unique tie-breaker sequence `(priority, seq_id, obj)`!"
                    }
                ]
            },
            {
                "title": "Module 3: Coding Lab I — Kth Largest Element (LC-215)",
                "blocks": [
                    {
                        "type": "dsa_problem",
                        "title": "Kth Largest Element in an Array",
                        "platform_style": "LeetCode 215 • Coding Ninjas Priority Queue Classic",
                        "difficulty": "Medium",
                        "pattern": "Fixed Size-K Min-Heap Streaming",
                        "target_time": "O(N log K)",
                        "target_space": "O(K)",
                        "statement": "Given an integer array `nums` and an integer `k`, return the **$k$-th largest** element in the array.\n\nNotice it is the $k$-th largest element in sorted order (duplicates ARE counted individually, e.g., in `[3,2,3,1,2,4,5,5,6]`, the 4th largest is `4`, NOT the 4th distinct value!).",
                        "examples": [
                            {"input": "nums = [3, 2, 1, 5, 6, 4], k = 2", "output": "5", "explanation": "Sorted descending: [6, 5, 4, 3, 2, 1] -> 2nd element is 5."},
                            {"input": "nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4", "output": "4", "explanation": "Sorted descending: [6, 5, 5, 4, ...] -> 4th element is 4."}
                        ],
                        "constraints": [
                            "$1 \\le k \\le \\text{nums.length} \\le 10^5$",
                            "$-10^4 \\le \\text{nums}[i] \\le 10^4$"
                        ],
                        "approach_ladder": {
                            "brute": "Sort descending and index `nums[k - 1]`: $O(N \\log N)$ time.",
                            "optimal": "Maintain a **Min-Heap** of size at most `k`: push each element, and whenever `len(heap) > k`, pop the minimum! Return `heap[0]` (`pq.top()`). Runs in **$O(N \\log K)$ time, $O(K)$ space** (Note: C++ `nth_element` or Randomized 3-way Quickselect runs in $O(N)$ average, while Min-Heap avoids worst-case $O(N^2)$ duplicates trap on `[1,1,1,...,1]`!)."
                        },
                        "dry_run": "`[3, 2, 1, 5, 6, 4], k=2`: push `3, 2` -> `heap=[2,3]`; push `1` & pop min (`[2,3]`); push `5` & pop `2` (`[3,5]`); push `6` & pop `3` (`[5,6]`); push `4` & pop `4` (`[5,6]`) -> `heap[0] = 5`.",
                        "edge_cases": [
                            {"title": "All Duplicates Quickselect Trap", "desc": "Naive 2-way Lomuto Quickselect degrades to $O(N^2)$ when all $10^5$ elements are identical! Size-K Min-Heap guarantees $O(N \\log K)$ even on all-equal inputs."}
                        ],
                        "follow_ups": "**LC-295 Find Median from Data Stream:** Pair a **Max-Heap** (lower half) + **Min-Heap** (upper half) balanced within `1` element to query live median in $O(1)$!",
                        "hint": "Keep a Min-Heap capped at size `k`; its root is always the smallest of the top `k` largest numbers.",
                        "starter_py": "class Solution:\n    def findKthLargest(self, nums: List[int], k: int) -> int:\n        # TODO: Size-k Min-Heap in O(N log k) time\n        return 0\n",
                        "solution_py": "class Solution:\n    def findKthLargest(self, nums: List[int], k: int) -> int:\n        hq = []\n        for x in nums:\n            if len(hq) < k:\n                heapq.heappush(hq, x)\n            elif x > hq[0]:\n                heapq.heapreplace(hq, x)\n        return hq[0]\n",
                        "harness_py": "_dsa_run_tests([\n    ('Sample 1: Distinct K=2', '[3,2,1,5,6,4], k=2', lambda: Solution().findKthLargest([3,2,1,5,6,4], 2), 5),\n    ('Sample 2: Duplicates K=4', '[3,2,3,1,2,4,5,5,6], k=4', lambda: Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4), 4),\n    ('Edge: k==1 (Max)', '[-1,2,0], k=1', lambda: Solution().findKthLargest([-1,2,0], 1), 2),\n    ('Edge: k==N (Min)', '[7,3,9], k=3', lambda: Solution().findKthLargest([7,3,9], 3), 3),\n    ('Stress: All Duplicates', '[5]*5000 + [8], k=2', lambda: Solution().findKthLargest([5]*5000 + [8], 2), 5),\n], sample_only=__DSA_SAMPLE_ONLY__, n_samples=2)",
                        "starter_cpp": "class Solution {\npublic:\n    int findKthLargest(vector<int>& nums, int k) {\n        // TODO: priority_queue min-heap of size k\n        return 0;\n    }\n};\n",
                        "solution_cpp": "class Solution {\npublic:\n    int findKthLargest(vector<int>& nums, int k) {\n        priority_queue<int, vector<int>, greater<int>> pq;\n        for (int x : nums) {\n            pq.push(x);\n            if ((int)pq.size() > k) pq.pop();\n        }\n        return pq.top();\n    }\n};\n",
                        "harness_cpp": "int main() {\n    ostringstream _dbg; streambuf* _old = cout.rdbuf(_dbg.rdbuf());\n    vector<_DSACaseOut> _res;\n    struct T { string name, inp; vector<int> arr; int k, exp; };\n    vector<int> all_eq(5000, 5); all_eq.push_back(8);\n    vector<T> tests = {\n        {\"Sample 1: Distinct K=2\", \"[3,2,1,5,6,4], k=2\", {3,2,1,5,6,4}, 2, 5},\n        {\"Sample 2: Duplicates K=4\", \"[3,2,3,1,2,4,5,5,6], k=4\", {3,2,3,1,2,4,5,5,6}, 4, 4},\n        {\"Edge: k==1\", \"[-1,2,0], k=1\", {-1,2,0}, 1, 2},\n        {\"Edge: k==N\", \"[7,3,9], k=3\", {7,3,9}, 3, 3},\n        {\"Stress: All Duplicates\", \"5000 fives + 8, k=2\", all_eq, 2, 5}\n    };\n    int lim = DSA_SAMPLE_ONLY ? 2 : (int)tests.size();\n    Solution sol;\n    for (int i = 0; i < lim; ++i) {\n        auto v = tests[i].arr;\n        auto t0 = chrono::steady_clock::now();\n        int act = sol.findKthLargest(v, tests[i].k);\n        double ms = chrono::duration<double, milli>(chrono::steady_clock::now() - t0).count();\n        _res.push_back({tests[i].name, tests[i].inp, _dsa_fmt(tests[i].exp), _dsa_fmt(act), \"\", act == tests[i].exp, ms});\n    }\n    cout.rdbuf(_old);\n    _dsa_emit_json(_res, _dbg.str());\n    return 0;\n}"
                    }
                ]
            },
            {
                "title": "Module 4: Coding Lab II — Top K Frequent Elements (LC-347)",
                "blocks": [
                    {
                        "type": "dsa_problem",
                        "title": "Top K Frequent Elements",
                        "platform_style": "LeetCode 347 • Coding Ninjas Hash + Bucket/Heap Classic",
                        "difficulty": "Medium",
                        "pattern": "Frequency Map + Bucket Sort O(N) / Min-Heap",
                        "target_time": "O(N)",
                        "target_space": "O(N)",
                        "statement": "Given an integer array `nums` and an integer `k`, return the **$k$ most frequent elements** (you may return the answer in **any order**).",
                        "examples": [
                            {"input": "nums = [1,1,1,2,2,3], k = 2", "output": "[1, 2]", "explanation": "1 occurs 3 times and 2 occurs 2 times."},
                            {"input": "nums = [1], k = 1", "output": "[1]", "explanation": "Single element."}
                        ],
                        "constraints": [
                            "$1 \\le \\text{nums.length} \\le 10^5$",
                            "$k$ is in the range $[1, \\text{number of unique elements}]$.",
                            "Answer is guaranteed unique."
                        ],
                        "approach_ladder": {
                            "brute": "Sort unique `(val, freq)` pairs by frequency descending in $O(N \\log N)$.",
                            "better": "Size-$K$ Min-Heap over `(freq, val)` pairs from `freq_map`: **$O(N \\log K)$**.",
                            "optimal": "**Linear Bucket Sort ($O(N)$ time, $O(N)$ space):** Since frequencies fall strictly within `[1..N]`, create `buckets = [[] for _ in range(n + 1)]`, append each `num` into `buckets[count]`, and sweep `buckets` from `n` down to `1` collecting the first `k` values!"
                        },
                        "dry_run": "`[1,1,1,2,2,3]`, `freq={1:3, 2:2, 3:1}`. `buckets[3]=[1]`, `buckets[2]=[2]`, `buckets[1]=[3]`. Walk backwards from `6`: pick `1`, pick `2` -> stop (`len == 2`)!",
                        "edge_cases": [
                            {"title": "Negative Keys with Bucket Sort", "desc": "Bucket array is indexed by **frequency** (`0..N`), NEVER by element value! Negative values like `-1` work cleanly without offset math."}
                        ],
                        "follow_ups": "**LC-692 Top K Frequent Words:** Lexicographical tie-breaking on equal frequencies requires a custom comparator rather than blind bucket append.",
                        "hint": "Frequency counts are always positive integers $\\le N$, so bucket-sorting by frequency achieves true linear $O(N)$ runtime!",
                        "starter_py": "class Solution:\n    def topKFrequent(self, nums: List[int], k: int) -> List[int]:\n        # TODO: O(N) Bucket Sort or O(N log k) Min-Heap\n        return []\n",
                        "solution_py": "class Solution:\n    def topKFrequent(self, nums: List[int], k: int) -> List[int]:\n        freq = Counter(nums)\n        buckets = [[] for _ in range(len(nums) + 1)]\n        for val, cnt in freq.items():\n            buckets[cnt].append(val)\n        res = []\n        for cnt in range(len(nums), 0, -1):\n            for val in buckets[cnt]:\n                res.append(val)\n                if len(res) == k:\n                    return res\n        return res\n",
                        "harness_py": "_dsa_run_tests([\n    ('Sample 1: Top 2', '[1,1,1,2,2,3], k=2', lambda: sorted(Solution().topKFrequent([1,1,1,2,2,3], 2)), [1, 2]),\n    ('Sample 2: Single', '[1], k=1', lambda: sorted(Solution().topKFrequent([1], 1)), [1]),\n    ('Edge: Negatives', '[-1,-1,5,5,5,2], k=2', lambda: sorted(Solution().topKFrequent([-1,-1,5,5,5,2], 2)), [-1, 5]),\n    ('Edge: k Equals Distinct Count', '[4,1,-1,2,-1,2,3], k=5', lambda: sorted(Solution().topKFrequent([4,1,-1,2,-1,2,3], 5)), [-1, 1, 2, 3, 4]),\n], sample_only=__DSA_SAMPLE_ONLY__, n_samples=2)",
                        "starter_cpp": "class Solution {\npublic:\n    vector<int> topKFrequent(vector<int>& nums, int k) {\n        // TODO: O(N) frequency bucket sort\n        return {};\n    }\n};\n",
                        "solution_cpp": "class Solution {\npublic:\n    vector<int> topKFrequent(vector<int>& nums, int k) {\n        unordered_map<int, int> freq;\n        for (int x : nums) ++freq[x];\n        vector<vector<int>> buckets(nums.size() + 1);\n        for (auto& kv : freq) buckets[kv.second].push_back(kv.first);\n        vector<int> res;\n        for (int c = (int)nums.size(); c >= 1 && (int)res.size() < k; --c) {\n            for (int v : buckets[c]) {\n                res.push_back(v);\n                if ((int)res.size() == k) break;\n            }\n        }\n        return res;\n    }\n};\n",
                        "harness_cpp": "int main() {\n    ostringstream _dbg; streambuf* _old = cout.rdbuf(_dbg.rdbuf());\n    vector<_DSACaseOut> _res;\n    struct T { string name, inp; vector<int> arr; int k; vector<int> exp; };\n    vector<T> tests = {\n        {\"Sample 1: Top 2\", \"[1,1,1,2,2,3], k=2\", {1,1,1,2,2,3}, 2, {1, 2}},\n        {\"Sample 2: Single\", \"[1], k=1\", {1}, 1, {1}},\n        {\"Edge: Negatives\", \"[-1,-1,5,5,5,2], k=2\", {-1,-1,5,5,5,2}, 2, {-1, 5}},\n        {\"Edge: Full Distinct\", \"[4,1,-1,2,-1,2,3], k=5\", {4,1,-1,2,-1,2,3}, 5, {-1, 1, 2, 3, 4}}\n    };\n    int lim = DSA_SAMPLE_ONLY ? 2 : (int)tests.size();\n    Solution sol;\n    for (int i = 0; i < lim; ++i) {\n        auto v = tests[i].arr;\n        auto t0 = chrono::steady_clock::now();\n        auto act = sol.topKFrequent(v, tests[i].k);\n        double ms = chrono::duration<double, milli>(chrono::steady_clock::now() - t0).count();\n        sort(act.begin(), act.end());\n        _res.push_back({tests[i].name, tests[i].inp, _dsa_fmt(tests[i].exp), _dsa_fmt(act), \"\", act == tests[i].exp, ms});\n    }\n    cout.rdbuf(_old);\n    _dsa_emit_json(_res, _dbg.str());\n    return 0;\n}"
                    }
                ]
            }
        ]
    }
}
