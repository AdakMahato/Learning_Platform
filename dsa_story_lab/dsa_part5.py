"""
DSA Story Lab - Part 5: Cases 16 to 18
Covers:
  - Case 16: Graphs II (Dijkstra Shortest Paths, Bellman-Ford, Disjoint Set Union / Kruskal MST)
  - Case 17: Dynamic Programming (Memo vs Tabulation, Knapsack, LCS)
  - Case 18: Tries & Bit Manipulation (Prefix Trees, XOR Laws, Kernighan Bitwise Tricks)
"""

CASES_PART5 = {
    "16": {
        "title": "Graphs II: Shortest Paths & Disjoint Set Union",
        "episodes": [
            {
                "title": "Module 1: Dijkstra Greedy Invariant, Bellman-Ford & DSU Theory",
                "blocks": [
                    {
                        "type": "story",
                        "title": "The Negative-Weight Routing Collapse",
                        "content": "A cloud backbone router ran **Dijkstra's Algorithm** across microservice links—even though promotional peering credits created **negative-weight edges** (`cost = -5 ms`). Because Dijkstra permanently finalizes the minimum unvisited vertex at each pop, node `B` was locked at cost `4` BEFORE a longer path `S -> A (cost 6) -> B (cost -5)` total `1` was ever explored!\n\n> [!IMPORTANT]\n> **Dijkstra's Greedy Invariant:** Selecting the minimum tentative vertex `u` is mathematically sound **only when all edge weights are non-negative (`w >= 0`)**, ensuring no future path leaving `u` or any remaining queue vertex can ever decrease `dist[u]`."
                    },
                    {
                        "type": "concept",
                        "title": "Weighted Shortest Paths vs Dynamic Connectivity (DSU)",
                        "content": "Choose the graph engine matched to edge weights and query type:\n\n1. **BFS (`O(V + E)`):** Unweighted graphs (or all weights `== 1`).\n2. **Dijkstra with Binary Min-Heap (`O((V + E) log V)`):** Single-source shortest paths when **all `w >= 0`**. Always use **lazy deletion**: push `(new_dist, v)` when relaxing an edge, and upon popping `(d, u)`, discard immediately if `d > dist[u]`!\n3. **Bellman-Ford (`O(V * E)`):** Handles **negative edge weights** by relaxing ALL `E` edges `V - 1` times. A **$V$-th relaxation** change proves a **negative weight cycle**!\n4. **Disjoint Set Union / Union-Find (`O(alpha(N))` amortized):** Answers dynamic connectivity (`connected(u, v)`) and cycle detection in undirected graphs using **Path Compression** + **Union by Rank/Size**.",
                        "technical_explanation": "**Inverse Ackermann Bound ($\\alpha(N)$):** Tarjan proved that combining *both* **Path Compression** (`parent[x] = find(parent[x])`) and **Union by Rank/Size** bounds $M$ operations on $N$ elements to **$O(M \\cdot \\alpha(N))$**, where $\\alpha(N) \\le 4$ for every physically observable $N \\le 10^{600}$."
                    },
                    {
                        "type": "visual",
                        "title": "Dijkstra Lazy Min-Heap Relaxation Flow",
                        "code": """flowchart LR
    Pop["Pop min (d, u) from Min-Heap"] --> Stale{"d > dist[u]?"}
    Stale -- "Yes (Stale Entry)" --> Skip["Discard in O(log E)"]
    Stale -- "No (Optimal dist[u] locked)" --> Relax["For each neighbor (v, w) of u"]
    Relax --> Imp{"dist[u] + w < dist[v]?"}
    Imp -- "Yes" --> Push["Update dist[v] & push (dist[v], v)"]
    Imp -- "No" --> Skip2["Keep existing dist[v]"]"""
                    },
                    {
                        "type": "comparison_table",
                        "title": "Shortest Path Algorithms Matrix",
                        "headers": ["Algorithm", "Graph Constraint", "Time Complexity", "Detects Negative Cycle?"],
                        "rows": [
                            ["Standard BFS", "All weights == 1", "O(V + E)", "N/A"],
                            ["0-1 BFS (Deque)", "Weights in {0, 1}", "O(V + E)", "N/A"],
                            ["Dijkstra (Min-Heap)", "All weights >= 0", "O((V + E) log V)", "No (gives wrong answer)"],
                            ["Bellman-Ford", "Negative weights allowed", "O(V * E)", "Yes (on V-th pass)"],
                            ["Floyd-Warshall", "All-pairs shortest paths", "O(V^3)", "Yes (if dist[i][i] < 0)"]
                        ]
                    },
                    {
                        "type": "micro_challenge",
                        "question": "Why does standard Dijkstra with `visited[u] = True` fail if an undirected/directed graph has even a single negative edge `w < 0`?",
                        "options": [
                            "It relies on `visited[u]` marking the node permanently finalized assuming remaining paths cannot shrink—which a later negative edge violates",
                            "Priority queues in Python and C++ cannot store negative integers",
                            "Adjacency lists cannot represent edges whose weights are negative",
                            "It always enters an infinite loop even on a DAG with negative edges"
                        ],
                        "answer": "It relies on `visited[u]` marking the node permanently finalized assuming remaining paths cannot shrink—which a later negative edge violates",
                        "explanation": "On a DAG with negative edges, Dijkstra terminates cleanly—yet returns a **wrong answer** because once `u` is finalized, a later longer prefix followed by a negative edge cannot reduce `dist[u]`."
                    }
                ]
            },
            {
                "title": "Module 2: MST Cut Property, Stale-Heap Bugs & Relaxation Bounds",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "Minimum Spanning Tree (Kruskal's & Cut Property) + DSU Math",
                        "content": "**Minimum Spanning Tree (MST):** Connects all $V$ vertices using $V - 1$ edges with minimum total weight.\n\n- **Cut Property Theorem:** Partition vertices into any non-empty sets $(S, V \\setminus S)$. If an edge $e$ has strictly minimum weight among all edges crossing $(S, V \\setminus S)$, then $e$ MUST belong to every MST!\n- **Kruskal's Algorithm (`O(E log E)`):** Sort all edges ascending by weight, then scan each `(u, v, w)`: if `find(u) != find(v)`, union them and add `w` to MST cost! Otherwise `u` and `v` are already connected, so adding `(u, v)` would create a **cycle** (the exact foundation of **LC-684 Redundant Connection**!).",
                        "technical_explanation": "**Union-Find Rank vs Size:** Both yield identical asymptotic $O(\\alpha(N))$ bounds when paired with path compression. **Union by Size** is doubly helpful in interviews because `size[find(x)]` simultaneously tracks exact component population in `O(1)`!"
                    },
                    {
                        "type": "debugger",
                        "title": "Bug Hunt: O(E^2) Dijkstra Regression",
                        "code": """import heapq
def dijkstra(n, adj, src):
    dist = [float('inf')] * (n + 1)
    dist[src] = 0
    pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        # Missing guard right here!
        for v, w in adj[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                heapq.heappush(pq, (dist[v], v))
    return dist""",
                        "question": "What subtle defect causes this Dijkstra implementation to degrade exponentially or exceed TLE on dense graphs with duplicate relaxed heap entries?",
                        "options": [
                            "Missing `if d > dist[u]: continue` right after `heappop`, causing outdated heap pairs to re-relax all neighbors of `u` repeatedly",
                            "Initializing `dist` with `float('inf')` fails in Python comparisons",
                            "Priority queues require negative keys for min-heap ordering in `heapq`",
                            "You must sort `adj[u]` before looping"
                        ],
                        "answer": "Missing `if d > dist[u]: continue` right after `heappop`, causing outdated heap pairs to re-relax all neighbors of `u` repeatedly",
                        "explanation": "Since `heapq` doesn't support `decrease_key`, each improvement pushes a new pair `(new_dist, v)`. Without `if d > dist[u]: continue`, stale pops re-scan `adj[u]` (even failing `d + w < dist[v]` on every neighbor, costing `O(deg(u))` per stale entry!)."
                    },
                    {
                        "type": "calculation_challenge",
                        "title": "Bellman-Ford Maximum Simple Path Length",
                        "question": "In a graph with $V = 250$ vertices and $E = 1800$ directed edges (no negative cycles), what is the **maximum number of outer relaxation iterations** Bellman-Ford needs to guarantee shortest paths between source `S` and every reachable vertex?",
                        "answer": "249",
                        "alternatives": ["249"],
                        "step_by_step": "Any simple shortest path (without cycles) visits at most $V$ vertices and therefore uses at most **$V - 1 = 250 - 1 = 249$ edges**. Pass $k$ finalizes all shortest paths of $\\le k$ edges."
                    }
                ]
            },
            {
                "title": "Module 3: Coding Lab I — Network Delay Time (LC-743)",
                "blocks": [
                    {
                        "type": "dsa_problem",
                        "title": "Network Delay Time",
                        "platform_style": "LeetCode 743 • Coding Ninjas Dijkstra Benchmark",
                        "difficulty": "Medium",
                        "pattern": "Dijkstra Single-Source Shortest Path (Min-Heap)",
                        "target_time": "O(E log V)",
                        "target_space": "O(V + E)",
                        "statement": "You are given a network of `n` nodes labeled `1` to `n`, and a list of directed weighted edges `times[i] = [u_i, v_i, w_i]` where signal takes `w_i` milliseconds to travel from `u_i` to `v_i` (`w_i >= 0`).\n\nSend a signal from starting node `k`. Return the **minimum time** for **ALL `n` nodes** to receive the signal (i.e., `max(dist[1..n])`), or **`-1`** if at least one node is unreachable.",
                        "examples": [
                            {"input": "times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2", "output": "2", "explanation": "dist: {2:0, 1:1, 3:1, 4:2}. Max delay = 2."},
                            {"input": "times = [[1,2,1]], n = 2, k = 2", "output": "-1", "explanation": "Node 1 is unreachable from node 2."}
                        ],
                        "constraints": [
                            "$1 \\le k \\le n \\le 100$",
                            "$1 \\le \\text{times.length} \\le 6000$",
                            "$0 \\le w_i \\le 100$ (non-negative weights, 1-indexed nodes!)"
                        ],
                        "approach_ladder": {
                            "better": "Bellman-Ford relaxing `times` $n - 1$ times: $O(V \\cdot E)$ time, handles negative edges if present.",
                            "optimal": "Build 1-indexed adjacency list `adj[u] = [(v, w), ...]`. Run **Dijkstra** with min-heap initialized at `(0, k)` and `dist = [INF]*(n+1)`. Skip stale pops `if d > dist[u]: continue`. After heap empties, check `mx = max(dist[1:])`; return `-1` if `mx == INF` else `mx`. **$O(E \\log V)$**."
                        },
                        "dry_run": "`k=2`: pop `(0, 2)` -> `dist[1]=1, dist[3]=1`, push `(1,1), (1,3)`. Pop `(1,1)` (no edges). Pop `(1,3)` -> `dist[4]=2`, push `(2,4)`. All nodes `[0, 1, 1, 2]` reachable -> max = **2**.",
                        "edge_cases": [
                            {"title": "1-Indexed Vertices `1..n`", "desc": "Allocate `dist` and `adj` of size `n + 1`, and check `max(dist[1:])` so dummy index `0` (`INF`) never pollutes the maximum!"},
                            {"title": "Zero-Weight Edges & Self/Parallel Edges", "desc": "`w_i == 0` is valid (`0 <= w_i`), and parallel directed edges simply keep the shorter relaxation naturally."}
                        ],
                        "follow_ups": "**LC-787 Cheapest Flights Within K Stops:** When edge count is capped by `K`, standard single-state `dist[u]` fails—track `(stops, cost, u)` with modified Bellman-Ford (copy previous iteration array) or BFS!",
                        "hint": "Use `dist = [INF] * (n + 1)`, set `dist[k] = 0`, push `(0, k)` onto a min-heap, discard pops with `d > dist[u]`, then take `max(dist[1:])`.",
                        "starter_py": "class Solution:\n    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:\n        # TODO: Dijkstra from 1-indexed source node k\n        return -1\n",
                        "solution_py": "class Solution:\n    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:\n        adj = [[] for _ in range(n + 1)]\n        for u, v, w in times:\n            adj[u].append((v, w))\n        INF = float('inf')\n        dist = [INF] * (n + 1)\n        dist[k] = 0\n        pq = [(0, k)]\n        while pq:\n            d, u = heapq.heappop(pq)\n            if d > dist[u]:\n                continue\n            for v, w in adj[u]:\n                nd = d + w\n                if nd < dist[v]:\n                    dist[v] = nd\n                    heapq.heappush(pq, (nd, v))\n        mx = max(dist[1:])\n        return -1 if mx == INF else mx\n",
                        "harness_py": "_dsa_run_tests([\n    ('Sample 1: 4-Node DAG', '[[2,1,1],[2,3,1],[3,4,1]], n=4, k=2', lambda: Solution().networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2), 2),\n    ('Sample 2: Unreachable Node', '[[1,2,1]], n=2, k=2', lambda: Solution().networkDelayTime([[1,2,1]], 2, 2), -1),\n    ('Edge: Parallel & Longer Shortcut', '[[1,2,10],[1,3,2],[3,2,3]], n=3, k=1', lambda: Solution().networkDelayTime([[1,2,10],[1,3,2],[3,2,3]], 3, 1), 5),\n    ('Edge: Single Node n=1', '[], n=1, k=1', lambda: Solution().networkDelayTime([], 1, 1), 0),\n    ('Edge: Zero-Weight Link & Cycle', '[[1,2,0],[2,1,0],[2,3,4]], n=3, k=1', lambda: Solution().networkDelayTime([[1,2,0],[2,1,0],[2,3,4]], 3, 1), 4),\n], sample_only=__DSA_SAMPLE_ONLY__, n_samples=2)",
                        "starter_cpp": "class Solution {\npublic:\n    int networkDelayTime(vector<vector<int>>& times, int n, int k) {\n        // TODO: Dijkstra with priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>>\n        return -1;\n    }\n};\n",
                        "solution_cpp": "class Solution {\npublic:\n    int networkDelayTime(vector<vector<int>>& times, int n, int k) {\n        vector<vector<pair<int,int>>> adj(n + 1);\n        for (const auto& e : times) adj[e[0]].push_back({e[1], e[2]});\n        const int INF = 1e9;\n        vector<int> dist(n + 1, INF);\n        dist[k] = 0;\n        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;\n        pq.push({0, k});\n        while (!pq.empty()) {\n            auto [d, u] = pq.top(); pq.pop();\n            if (d > dist[u]) continue;\n            for (auto [v, w] : adj[u]) {\n                if (d + w < dist[v]) {\n                    dist[v] = d + w;\n                    pq.push({dist[v], v});\n                }\n            }\n        }\n        int ans = 0;\n        for (int i = 1; i <= n; ++i) {\n            if (dist[i] == INF) return -1;\n            ans = max(ans, dist[i]);\n        }\n        return ans;\n    }\n};\n",
                        "harness_cpp": "int main() {\n    ostringstream _dbg; streambuf* _old = cout.rdbuf(_dbg.rdbuf());\n    vector<_DSACaseOut> _res;\n    struct T { string name, inp; vector<vector<int>> times; int n, k, exp; };\n    vector<T> tests = {\n        {\"Sample 1: 4-Node DAG\", \"n=4, k=2\", {{2,1,1},{2,3,1},{3,4,1}}, 4, 2, 2},\n        {\"Sample 2: Unreachable Node\", \"[[1,2,1]], n=2, k=2\", {{1,2,1}}, 2, 2, -1},\n        {\"Edge: Shortcut Path\", \"n=3, k=1\", {{1,2,10},{1,3,2},{3,2,3}}, 3, 1, 5},\n        {\"Edge: Single Node n=1\", \"[], n=1, k=1\", {}, 1, 1, 0},\n        {\"Edge: Zero Weight & Cycle\", \"n=3, k=1\", {{1,2,0},{2,1,0},{2,3,4}}, 3, 1, 4}\n    };\n    int lim = DSA_SAMPLE_ONLY ? 2 : (int)tests.size();\n    Solution sol;\n    for (int i = 0; i < lim; ++i) {\n        auto tm = tests[i].times;\n        auto t0 = chrono::steady_clock::now();\n        int act = sol.networkDelayTime(tm, tests[i].n, tests[i].k);\n        double ms = chrono::duration<double, milli>(chrono::steady_clock::now() - t0).count();\n        _res.push_back({tests[i].name, tests[i].inp, _dsa_fmt(tests[i].exp), _dsa_fmt(act), \"\", act == tests[i].exp, ms});\n    }\n    cout.rdbuf(_old);\n    _dsa_emit_json(_res, _dbg.str());\n    return 0;\n}"
                    }
                ]
            },
            {
                "title": "Module 4: Coding Lab II — Redundant Connection via DSU (LC-684)",
                "blocks": [
                    {
                        "type": "dsa_problem",
                        "title": "Redundant Connection (Disjoint Set Union Cycle Edge)",
                        "platform_style": "LeetCode 684 • Coding Ninjas Union-Find Classic",
                        "difficulty": "Medium",
                        "pattern": "Disjoint Set Union (Path Compression + Union by Rank)",
                        "target_time": "O(N * alpha(N))",
                        "target_space": "O(N)",
                        "statement": "A connected undirected tree of `n` nodes labeled `1` to `n` had **one extra edge** added, creating a cycle.\n\nGiven `edges` of length `n`, return the **last edge in `edges`** that can be removed so the remaining graph becomes a valid tree of `n` nodes.",
                        "examples": [
                            {"input": "edges = [[1,2],[1,3],[2,3]]", "output": "[2, 3]", "explanation": "1-2 and 1-3 connect {1,2,3}; edge [2,3] closes the cycle."},
                            {"input": "edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]", "output": "[1, 4]", "explanation": "[1,4] connects already-connected vertices."}
                        ],
                        "constraints": [
                            "$3 \\le n \\le 1000$",
                            "`edges.length == n`, edges are unique `1 <= u_i < v_i <= n`."
                        ],
                        "approach_ladder": {
                            "brute": "For each edge `(u, v)` added incrementally, run BFS/DFS to check if `u` can already reach `v`: **$O(N^2)$**.",
                            "optimal": "**Disjoint Set Union:** Process edges from left to right. If `find(u) == find(v)`, both endpoints ALREADY share a connected component, so `[u, v]` MUST close the single cycle—return `[u, v]` immediately! Otherwise `union(u, v)`. **$O(N \\cdot \\alpha(N))$**!"
                        },
                        "dry_run": "`[[1,2],[1,3],[2,3]]`: union(1,2), union(1,3) -> root(2)=1, root(3)=1. Next `[2,3]`: `find(2)==find(3)` -> return **[2, 3]**.",
                        "edge_cases": [
                            {"title": "Iterative vs Recursive Path Compression", "desc": "`parent[x] = find(parent[x])` compresses paths in 3 lines cleanly for $N \\le 10^5$."},
                            {"title": "1-Indexed Allocation", "desc": "Allocate `parent = list(range(n + 1))` where `n = len(edges)`."}
                        ],
                        "follow_ups": "**LC-685 Redundant Connection II (Directed):** Must check TWO conditions—a node with indegree 2 AND a directed cycle—requiring a 2-pass DSU!",
                        "hint": "Initialize `parent = [i for i in range(len(edges) + 1)]`, implement `find(x)` and `union(a, b) -> bool`. Return the first edge where `union(u, v)` returns `False`!",
                        "starter_py": "class Solution:\n    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:\n        # TODO: DSU with path compression + union by rank/size\n        return []\n",
                        "solution_py": "class Solution:\n    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:\n        n = len(edges)\n        parent = list(range(n + 1))\n        rank = [0] * (n + 1)\n\n        def find(x: int) -> int:\n            while parent[x] != x:\n                parent[x] = parent[parent[x]]\n                x = parent[x]\n            return x\n\n        def union(a: int, b: int) -> bool:\n            ra, rb = find(a), find(b)\n            if ra == rb:\n                return False\n            if rank[ra] < rank[rb]:\n                ra, rb = rb, ra\n            parent[rb] = ra\n            if rank[ra] == rank[rb]:\n                rank[ra] += 1\n            return True\n\n        for u, v in edges:\n            if not union(u, v):\n                return [u, v]\n        return []\n",
                        "harness_py": "_dsa_run_tests([\n    ('Sample 1: Triangle Cycle', '[[1,2],[1,3],[2,3]]', lambda: Solution().findRedundantConnection([[1,2],[1,3],[2,3]]), [2, 3]),\n    ('Sample 2: 4-Cycle + Tail', '[[1,2],[2,3],[3,4],[1,4],[1,5]]', lambda: Solution().findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]), [1, 4]),\n    ('Edge: Cycle At Very End', '[[1,2],[3,4],[2,3],[4,1]]', lambda: Solution().findRedundantConnection([[1,2],[3,4],[2,3],[4,1]]), [4, 1]),\n    ('Edge: Early Cycle Before Branch', '[[1,2],[2,3],[1,3],[3,4]]', lambda: Solution().findRedundantConnection([[1,2],[2,3],[1,3],[3,4]]), [1, 3]),\n], sample_only=__DSA_SAMPLE_ONLY__, n_samples=2)",
                        "starter_cpp": "class Solution {\npublic:\n    vector<int> findRedundantConnection(vector<vector<int>>& edges) {\n        // TODO: Union-Find returning first edge forming a cycle\n        return {};\n    }\n};\n",
                        "solution_cpp": "class Solution {\npublic:\n    vector<int> findRedundantConnection(vector<vector<int>>& edges) {\n        int n = (int)edges.size();\n        vector<int> p(n + 1), rk(n + 1, 0);\n        iota(p.begin(), p.end(), 0);\n        auto find = [&](int x) {\n            while (p[x] != x) {\n                p[x] = p[p[x]];\n                x = p[x];\n            }\n            return x;\n        };\n        for (const auto& e : edges) {\n            int ra = find(e[0]), rb = find(e[1]);\n            if (ra == rb) return {e[0], e[1]};\n            if (rk[ra] < rk[rb]) swap(ra, rb);\n            p[rb] = ra;\n            if (rk[ra] == rk[rb]) ++rk[ra];\n        }\n        return {};\n    }\n};\n",
                        "harness_cpp": "int main() {\n    ostringstream _dbg; streambuf* _old = cout.rdbuf(_dbg.rdbuf());\n    vector<_DSACaseOut> _res;\n    struct T { string name, inp; vector<vector<int>> edges; vector<int> exp; };\n    vector<T> tests = {\n        {\"Sample 1: Triangle Cycle\", \"[[1,2],[1,3],[2,3]]\", {{1,2},{1,3},{2,3}}, {2,3}},\n        {\"Sample 2: 4-Cycle + Tail\", \"[[1,2],[2,3],[3,4],[1,4],[1,5]]\", {{1,2},{2,3},{3,4},{1,4},{1,5}}, {1,4}},\n        {\"Edge: Cycle At End\", \"[[1,2],[3,4],[2,3],[4,1]]\", {{1,2},{3,4},{2,3},{4,1}}, {4,1}},\n        {\"Edge: Early Cycle\", \"[[1,2],[2,3],[1,3],[3,4]]\", {{1,2},{2,3},{1,3},{3,4}}, {1,3}}\n    };\n    int lim = DSA_SAMPLE_ONLY ? 2 : (int)tests.size();\n    Solution sol;\n    for (int i = 0; i < lim; ++i) {\n        auto ed = tests[i].edges;\n        auto t0 = chrono::steady_clock::now();\n        auto act = sol.findRedundantConnection(ed);\n        double ms = chrono::duration<double, milli>(chrono::steady_clock::now() - t0).count();\n        _res.push_back({tests[i].name, tests[i].inp, _dsa_fmt(tests[i].exp), _dsa_fmt(act), \"\", act == tests[i].exp, ms});\n    }\n    cout.rdbuf(_old);\n    _dsa_emit_json(_res, _dbg.str());\n    return 0;\n}"
                    }
                ]
            }
        ]
    },
    "17": {
        "title": "Subproblem Vault: Dynamic Programming 1D, Knapsack & 2D",
        "episodes": [
            {
                "title": "Module 1: Overlapping Subproblems, Memoization vs Tabulation Theory",
                "blocks": [
                    {
                        "type": "story",
                        "title": "The 2^50 Recursion Explosion",
                        "content": "A naïve recursive billing solver recalculated `solve(25)` **317,811 times** when pricing `n = 50` tiered steps, freezing production CPUs for minutes. By caching repeated states into a Directed Acyclic Graph (DAG) of subproblems, the runtime plunged from **$O(2^N)$ exponential** to **$O(N)$ microseconds**!\n\n> [!IMPORTANT]\n> **When Does Dynamic Programming Apply?** Exactly two properties must hold:\n> 1. **Optimal Substructure:** An optimal solution for size `n` can be built from optimal solutions to smaller subproblems.\n> 2. **Overlapping Subproblems:** The same `(state)` arguments recur repeatedly across branches (unlike Merge Sort, whose subproblems are disjoint!)."
                    },
                    {
                        "type": "concept",
                        "title": "The 4-Step DP Framework & Top-Down vs Bottom-Up",
                        "content": "Never guess a DP array! Derive every DP problem using four formal steps:\n\n1. **Define State `dp[...]` in plain English:** e.g., `dp[x]` = *minimum coins needed to make amount `x`*.\n2. **Write the Recurrence Relation (Transition):** e.g., `dp[x] = 1 + min(dp[x - c] for c in coins if x >= c)`.\n3. **Establish Base Cases:** e.g., `dp[0] = 0`, invalid states = `+INF`.\n4. **Determine Evaluation Order & Space Compression:** Top-Down (DFS + `@lru_cache` / `memo[]`) explores only reachable states; Bottom-Up (iterative loops) eliminates recursion overhead and allows **rolling-array `O(W)` or `O(1)` space compression**!",
                        "technical_explanation": "**House Robber 1D Recurrence (`LC-198`):** You cannot rob two adjacent houses. State `dp[i]` = max loot from `0..i` -> `dp[i] = max(dp[i-1], nums[i] + dp[i-2])`. Notice `dp[i]` depends ONLY on `dp[i-1]` and `dp[i-2]`, shrinking space from $O(N)$ to **$O(1)$** with two variables `prev2, prev1`!"
                    },
                    {
                        "type": "visual",
                        "title": "Top-Down Memoization vs Bottom-Up Tabulation DAG",
                        "code": """flowchart TD
    Fib5["dp(5)"] --> Fib4["dp(4)"]
    Fib5 --> Fib3a["dp(3)"]
    Fib4 --> Fib3b["dp(3) [CACHED O(1)!]"]
    Fib4 --> Fib2a["dp(2)"]
    Fib3a --> Fib2b["dp(2) [CACHED O(1)!]"]"""
                    },
                    {
                        "type": "comparison_table",
                        "title": "Memoization (Top-Down) vs Tabulation (Bottom-Up)",
                        "headers": ["Dimension", "Top-Down Memoization", "Bottom-Up Tabulation"],
                        "rows": [
                            ["Control Flow", "Recursive DFS + Cache Table", "Iterative Loops over State Order"],
                            ["States Computed", "Only reachable states", "All states in topological order"],
                            ["Call Stack Overhead", "O(depth) stack frames (recursion risk)", "Zero recursion stack overhead"],
                            ["Space Optimization", "Harder (cache stays full)", "Easy (rolling 1D row / O(1) vars)"]
                        ]
                    }
                ]
            },
            {
                "title": "Module 2: 0/1 vs Unbounded Knapsack & 2D LCS Recurrences",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "Critical Loop Invariant: 0/1 Knapsack vs Unbounded Knapsack",
                        "content": "Both 1D space-compressed Knapsack algorithms look identical EXCEPT for one line—the **inner capacity loop direction**:\n\n- **0/1 Knapsack (each item used AT MOST once):** Loop capacity **BACKWARD** (`for c in range(W, w - 1, -1)`). Why? When reading `dp[c - w]`, it MUST reflect the **previous item row**—if you swept forward, you would overwrite `dp[c - w]` with the current item already included and accidentally use an item twice!\n- **Unbounded Knapsack (Coin Change `LC-322`, unlimited supply):** Loop capacity **FORWARD** (`for c in range(c_val, amount + 1)`), intentionally reusing updated `dp[c - coin]` from the current item!\n- **2D Subsequence DP (LCS `LC-1143`):**\n  - If `s1[i-1] == s2[j-1]`: `dp[i][j] = 1 + dp[i-1][j-1]`\n  - Else: `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`",
                        "technical_explanation": "**Coin Change Combinations (`LC-518`) vs Permutations (`LC-377`):** Putting `for coin in coins:` on the **OUTER** loop enforces canonical coin ordering (counts **combinations**, e.g. `1+2` once). Putting `for x in range(amount + 1):` on the **OUTER** loop allows mixing coins in any order (counts **permutations**, e.g. `1+2` and `2+1`)."
                    },
                    {
                        "type": "debugger",
                        "title": "Bug Hunt: Coin Change Greedy vs DP & Initialization Trap",
                        "code": """def coin_change_buggy(coins, amount):
    dp = [0] * (amount + 1)
    for x in range(1, amount + 1):
        for c in coins:
            if x >= c:
                dp[x] = min(dp[x], dp[x - c] + 1)
    return dp[amount] if dp[amount] > 0 else -1""",
                        "question": "Why does `coin_change_buggy([1, 2, 5], 11)` immediately return `-1` for every positive amount?",
                        "options": [
                            "`dp` was initialized to all `0`s instead of `amount + 1` (Infinity), so `min(0, dp[x-c] + 1)` ALWAYS stays `0`!",
                            "Iterating `amount` in the outer loop breaks minimum coin calculation",
                            "Sorting `coins` descending is mandatory before Unbounded Knapsack DP",
                            "`x >= c` should be strict `x > c`"
                        ],
                        "answer": "`dp` was initialized to all `0`s instead of `amount + 1` (Infinity), so `min(0, dp[x-c] + 1)` ALWAYS stays `0`!",
                        "explanation": "Because `min` seeks smaller values, unreachable or uncomputed states must start at `INF = amount + 1` (or `1e9`), with ONLY `dp[0] = 0`."
                    },
                    {
                        "type": "calculation_challenge",
                        "title": "Why Greedy Fails Coin Change",
                        "question": "Given `coins = [1, 3, 4]` and target `amount = 6`, greedy largest-coin-first picks `[4, 1, 1]` (3 coins). What is the true **minimum number of coins** found by Dynamic Programming?",
                        "answer": "2",
                        "alternatives": ["2"],
                        "step_by_step": "DP evaluates `dp[6] = min(1 + dp[5], 1 + dp[3], 1 + dp[2]) = min(1+2, 1+1, 1+2) = 2` (using `[3, 3]`)."
                    }
                ]
            },
            {
                "title": "Module 3: Coding Lab I — Coin Change (LC-322)",
                "blocks": [
                    {
                        "type": "dsa_problem",
                        "title": "Coin Change",
                        "platform_style": "LeetCode 322 • Coding Ninjas Unbounded Knapsack Essential",
                        "difficulty": "Medium",
                        "pattern": "1D Bottom-Up Unbounded Knapsack DP",
                        "target_time": "O(amount * len(coins))",
                        "target_space": "O(amount)",
                        "statement": "You are given an integer array `coins` representing coin denominations and an integer `amount` representing a total amount of money.\n\nReturn the **fewest number of coins** needed to make up that `amount` (infinite supply of each denomination). If no combination can form `amount`, return **`-1`**.",
                        "examples": [
                            {"input": "coins = [1, 2, 5], amount = 11", "output": "3", "explanation": "5 + 5 + 1 = 11 (3 coins)."},
                            {"input": "coins = [2], amount = 3", "output": "-1", "explanation": "Only coin 2 cannot sum to odd amount 3."}
                        ],
                        "constraints": [
                            "$1 \\le \\text{coins.length} \\le 12$",
                            "$1 \\le \\text{coins}[i] \\le 2^{31} - 1$",
                            "$0 \\le \\text{amount} \\le 10^4$"
                        ],
                        "approach_ladder": {
                            "brute": "Try choosing each coin recursively at step `rem`: **$O(|coins|^{\\text{amount}})$ TLE**.",
                            "optimal": "Initialize `dp = [amount + 1] * (amount + 1)` with `dp[0] = 0`. For each `coin` in `coins`, sweep `x` **forward** from `coin` to `amount`: `dp[x] = min(dp[x], dp[x - coin] + 1)`. Return `-1` if `dp[amount] > amount` else `dp[amount]`. **$O(\\text{amount} \\cdot |coins|)$**!"
                        },
                        "dry_run": "`coins=[1,3,4], amount=6`: initially `[0, 7,7,7,7,7,7]`. Coin `1` -> `[0,1,2,3,4,5,6]`. Coin `3` -> `dp[3]=1, dp[4]=2, dp[6]=1+dp[3]=2`! Coin `4` -> `dp[4]=1`, `dp[6]` remains `2` -> returns **2**.",
                        "edge_cases": [
                            {"title": "`amount == 0` Base Case", "desc": "0 coins needed to make amount `0` -> returns **0**!"},
                            {"title": "Coin Value Larger Than `amount` (`coin > amount`)", "desc": "With `range(c, amount + 1)`, oversized coins cleanly skip without overflow or out-of-bounds indexing (important since `coins[i]` can reach $2^{31}-1$ in C++: loop only when `c <= amount`)."}
                        ],
                        "follow_ups": "**LC-518 Coin Change II:** Count distinct combinations by replacing `min(..., 1 + dp[x-c])` with `dp[x] += dp[x - c]` and `dp[0] = 1`!",
                        "hint": "Initialize `dp = [amount + 1] * (amount + 1)`, set `dp[0] = 0`, iterate `for c in coins:` and forward `for x in range(c, amount + 1): dp[x] = min(dp[x], dp[x - c] + 1)`.",
                        "starter_py": "class Solution:\n    def coinChange(self, coins: List[int], amount: int) -> int:\n        # TODO: Bottom-Up Unbounded Knapsack Min-Coins DP\n        return -1\n",
                        "solution_py": "class Solution:\n    def coinChange(self, coins: List[int], amount: int) -> int:\n        INF = amount + 1\n        dp = [INF] * (amount + 1)\n        dp[0] = 0\n        for c in coins:\n            for x in range(c, amount + 1):\n                if dp[x - c] + 1 < dp[x]:\n                    dp[x] = dp[x - c] + 1\n        return -1 if dp[amount] > amount else dp[amount]\n",
                        "harness_py": "_dsa_run_tests([\n    ('Sample 1: [1,2,5], amt=11', 'coins=[1,2,5], amount=11', lambda: Solution().coinChange([1, 2, 5], 11), 3),\n    ('Sample 2: [2], amt=3 (Impossible)', 'coins=[2], amount=3', lambda: Solution().coinChange([2], 3), -1),\n    ('Edge: Greedy Trap [1,3,4], amt=6', 'coins=[1,3,4], amount=6', lambda: Solution().coinChange([1, 3, 4], 6), 2),\n    ('Edge: Zero Amount', 'coins=[1], amount=0', lambda: Solution().coinChange([1], 0), 0),\n    ('Edge: Oversized Coin > amount', 'coins=[2147483647], amount=2', lambda: Solution().coinChange([2147483647], 2), -1),\n], sample_only=__DSA_SAMPLE_ONLY__, n_samples=2)",
                        "starter_cpp": "class Solution {\npublic:\n    int coinChange(vector<int>& coins, int amount) {\n        // TODO: O(amount * len(coins)) bottom-up DP\n        return -1;\n    }\n};\n",
                        "solution_cpp": "class Solution {\npublic:\n    int coinChange(vector<int>& coins, int amount) {\n        int INF = amount + 1;\n        vector<int> dp(amount + 1, INF);\n        dp[0] = 0;\n        for (int c : coins) {\n            if (c > amount) continue;\n            for (int x = c; x <= amount; ++x) {\n                dp[x] = min(dp[x], dp[x - c] + 1);\n            }\n        }\n        return dp[amount] > amount ? -1 : dp[amount];\n    }\n};\n",
                        "harness_cpp": "int main() {\n    ostringstream _dbg; streambuf* _old = cout.rdbuf(_dbg.rdbuf());\n    vector<_DSACaseOut> _res;\n    struct T { string name, inp; vector<int> coins; int amt, exp; };\n    vector<T> tests = {\n        {\"Sample 1: [1,2,5], amt=11\", \"[1,2,5], 11\", {1,2,5}, 11, 3},\n        {\"Sample 2: [2], amt=3\", \"[2], 3\", {2}, 3, -1},\n        {\"Edge: Greedy Trap [1,3,4], amt=6\", \"[1,3,4], 6\", {1,3,4}, 6, 2},\n        {\"Edge: Zero Amount\", \"[1], 0\", {1}, 0, 0},\n        {\"Edge: INT_MAX Coin\", \"[INT_MAX], 2\", {INT_MAX}, 2, -1}\n    };\n    int lim = DSA_SAMPLE_ONLY ? 2 : (int)tests.size();\n    Solution sol;\n    for (int i = 0; i < lim; ++i) {\n        auto c = tests[i].coins;\n        auto t0 = chrono::steady_clock::now();\n        int act = sol.coinChange(c, tests[i].amt);\n        double ms = chrono::duration<double, milli>(chrono::steady_clock::now() - t0).count();\n        _res.push_back({tests[i].name, tests[i].inp, _dsa_fmt(tests[i].exp), _dsa_fmt(act), \"\", act == tests[i].exp, ms});\n    }\n    cout.rdbuf(_old);\n    _dsa_emit_json(_res, _dbg.str());\n    return 0;\n}"
                    }
                ]
            },
            {
                "title": "Module 4: Coding Lab II — Longest Common Subsequence (LC-1143)",
                "blocks": [
                    {
                        "type": "dsa_problem",
                        "title": "Longest Common Subsequence (2D String DP)",
                        "platform_style": "LeetCode 1143 • Coding Ninjas 2D DP Foundation",
                        "difficulty": "Medium",
                        "pattern": "2D Grid DP (Space-Optimized to O(min(M, N)))",
                        "target_time": "O(M * N)",
                        "target_space": "O(min(M, N))",
                        "statement": "Given two strings `text1` and `text2`, return the **length of their longest common subsequence** (characters appear in the same relative order, not necessarily contiguous). Return `0` if there is no common subsequence.",
                        "examples": [
                            {"input": "text1 = \"abcde\", text2 = \"ace\"", "output": "3", "explanation": "Longest common subsequence is \"ace\" of length 3."},
                            {"input": "text1 = \"abc\", text2 = \"def\"", "output": "0", "explanation": "No shared characters."}
                        ],
                        "constraints": [
                            "$1 \\le \\text{text1.length}, \\text{text2.length} \\le 1000$",
                            "Both strings consist only of lowercase English letters."
                        ],
                        "approach_ladder": {
                            "better": "2D DP table `(M+1) x (N+1)`: `$O(M \\cdot N)$` time and `$O(M \\cdot N)$` space.",
                            "optimal": "Maintain a 1D rolling row `dp[0..N]` saving `prev_diag` (`dp[i-1][j-1]`) before updating `dp[j]`: **$O(M \\cdot N)$ time and $O(\\min(M, N))$ space**!"
                        },
                        "dry_run": "`text1=\"abcde\", text2=\"ace\"`: `'a'` matches `'a'` (`dp=1`), skips `'b'`, `'c'` matches `'c'` (`dp=2`), skips `'d'`, `'e'` matches `'e'` (`dp=3`).",
                        "edge_cases": [
                            {"title": "Identical Strings", "desc": "Returns `len(text1)` cleanly."},
                            {"title": "Interleaved Repeats (`\"aab\"`, `\"azb\"`)", "desc": "Diagonal transition ensures a character isn't reused twice in the same step!"}
                        ],
                        "follow_ups": "**LC-72 Edit Distance & LC-516 Longest Palindromic Subsequence (LPS):** Notice `LPS(s) == LCS(s, reverse(s))`!",
                        "hint": "Use `dp[i][j] = 1 + dp[i-1][j-1]` when `text1[i-1] == text2[j-1]`, else `max(dp[i-1][j], dp[i][j-1])` (or compress to 1D with `prev_diag`).",
                        "starter_py": "class Solution:\n    def longestCommonSubsequence(self, text1: str, text2: str) -> int:\n        # TODO: 2D / space-optimized 1D LCS DP in O(M*N)\n        return 0\n",
                        "solution_py": "class Solution:\n    def longestCommonSubsequence(self, text1: str, text2: str) -> int:\n        if len(text1) < len(text2):\n            text1, text2 = text2, text1\n        n = len(text2)\n        dp = [0] * (n + 1)\n        for ch1 in text1:\n            prev_diag = 0\n            for j, ch2 in enumerate(text2, 1):\n                tmp = dp[j]\n                if ch1 == ch2:\n                    dp[j] = prev_diag + 1\n                else:\n                    if dp[j - 1] > dp[j]:\n                        dp[j] = dp[j - 1]\n                prev_diag = tmp\n        return dp[n]\n",
                        "harness_py": "_dsa_run_tests([\n    ('Sample 1: \"abcde\" & \"ace\"', 'text1=\"abcde\", text2=\"ace\"', lambda: Solution().longestCommonSubsequence('abcde', 'ace'), 3),\n    ('Sample 2: Disjoint Strings', 'text1=\"abc\", text2=\"def\"', lambda: Solution().longestCommonSubsequence('abc', 'def'), 0),\n    ('Edge: Identical Strings', 'text1=\"abc\", text2=\"abc\"', lambda: Solution().longestCommonSubsequence('abc', 'abc'), 3),\n    ('Edge: Repeated Interleaved', 'text1=\"bl\", text2=\"yby\"', lambda: Solution().longestCommonSubsequence('bl', 'yby'), 1),\n    ('Edge: Classic Pair \"oxcpqrsvwf\" & \"shmtulqrypy\"', '10 chars vs 11 chars', lambda: Solution().longestCommonSubsequence('oxcpqrsvwf', 'shmtulqrypy'), 2),\n], sample_only=__DSA_SAMPLE_ONLY__, n_samples=2)",
                        "starter_cpp": "class Solution {\npublic:\n    int longestCommonSubsequence(string text1, string text2) {\n        // TODO: O(M*N) time, O(min(M,N)) space LCS\n        return 0;\n    }\n};\n",
                        "solution_cpp": "class Solution {\npublic:\n    int longestCommonSubsequence(string text1, string text2) {\n        if (text1.size() < text2.size()) swap(text1, text2);\n        int n = (int)text2.size();\n        vector<int> dp(n + 1, 0);\n        for (char c1 : text1) {\n            int prev_diag = 0;\n            for (int j = 1; j <= n; ++j) {\n                int tmp = dp[j];\n                if (c1 == text2[j - 1]) dp[j] = prev_diag + 1;\n                else dp[j] = max(dp[j], dp[j - 1]);\n                prev_diag = tmp;\n            }\n        }\n        return dp[n];\n    }\n};\n",
                        "harness_cpp": "int main() {\n    ostringstream _dbg; streambuf* _old = cout.rdbuf(_dbg.rdbuf());\n    vector<_DSACaseOut> _res;\n    struct T { string name, inp, a, b; int exp; };\n    vector<T> tests = {\n        {\"Sample 1: abcde & ace\", \"abcde, ace\", \"abcde\", \"ace\", 3},\n        {\"Sample 2: Disjoint\", \"abc, def\", \"abc\", \"def\", 0},\n        {\"Edge: Identical\", \"abc, abc\", \"abc\", \"abc\", 3},\n        {\"Edge: Repeated Char\", \"bl, yby\", \"bl\", \"yby\", 1},\n        {\"Edge: Sparse Match\", \"oxcpqrsvwf, shmtulqrypy\", \"oxcpqrsvwf\", \"shmtulqrypy\", 2}\n    };\n    int lim = DSA_SAMPLE_ONLY ? 2 : (int)tests.size();\n    Solution sol;\n    for (int i = 0; i < lim; ++i) {\n        auto t0 = chrono::steady_clock::now();\n        int act = sol.longestCommonSubsequence(tests[i].a, tests[i].b);\n        double ms = chrono::duration<double, milli>(chrono::steady_clock::now() - t0).count();\n        _res.push_back({tests[i].name, tests[i].inp, _dsa_fmt(tests[i].exp), _dsa_fmt(act), \"\", act == tests[i].exp, ms});\n    }\n    cout.rdbuf(_old);\n    _dsa_emit_json(_res, _dbg.str());\n    return 0;\n}"
                    }
                ]
            }
        ]
    },
    "18": {
        "title": "Prefix & Parity: Tries and Bit Manipulation Mastery",
        "episodes": [
            {
                "title": "Module 1: Prefix Trie Architecture & XOR Group Theory",
                "blocks": [
                    {
                        "type": "story",
                        "title": "The Millisecond Autocomplete Dictionary",
                        "content": "Searching whether *any* word among 10 million English & brand queries starts with `\"anti\"` takes `O(N)` (`10,000,000` string scans) in a hash table, because hash tables compute full-word hashes and **cannot query prefixes**! Replacing it with a **Prefix Trie (Digital Tree)** searches ANY prefix in exact **$O(L)$** time (4 character hops)—completely independent of whether the dictionary has 10 words or 100 million!\n\n> [!IMPORTANT]\n> **Trie Invariant:** Every edge represents a single character; shared prefixes collapse into a single ancestor path, and a boolean `is_end` marks complete stored keys."
                    },
                    {
                        "type": "concept",
                        "title": "Prefix Tries vs Binary Search / Hashing & XOR Algebraic Laws",
                        "content": "### 1. Prefix Trie Node Design\n- Each `TrieNode` holds up to $\\Sigma = 26$ child pointers (`children = {}` dict or `TrieNode* child[26] = {}`) plus `isEnd = False`.\n- **Time Complexity:** `insert`, `search`, and `startsWith` each cost **$O(L)$** (`L = len(word)`).\n- **Space:** $O(\\text{Total Characters} \\times \\Sigma)$ worst-case, dramatically smaller when keys share prefixes.\n\n### 2. XOR (`^`) Algebraic Laws\n- **Self-Inverse:** $x \\oplus x = 0$\n- **Identity:** $x \\oplus 0 = x$\n- **Commutative & Associative:** `(a ^ b) ^ c == a ^ (b ^ c)` -> pairing every duplicate leaves only the unique single number in **$O(N)$ time, $O(1)$ space** (`LC-136 Single Number`)!",
                        "technical_explanation": "**Binary Trie (Maximum XOR of Two Numbers `LC-421`):** Store integers bit-by-bit from MSB (bit `30`) down to LSB (bit `0`) in a 2-branch Trie `{0, 1}`. At query time, greedily step into the **opposite bit** `(1 - bit)` whenever present to maximize XOR in $O(31)$ per number!"
                    },
                    {
                        "type": "visual",
                        "title": "Prefix Trie Structure Sharing 'app'",
                        "code": """flowchart TD
    Root["(root)"] -->|a| A["a"]
    A -->|p| P1["p"]
    P1 -->|p| P2["p (isEnd: false)"]
    P2 -->|l| L["l"]
    L -->|e| E["e (isEnd: TRUE -> 'apple')"]
    L -->|y| Y["y (isEnd: TRUE -> 'apply')"]"""
                    },
                    {
                        "type": "comparison_table",
                        "title": "Dictionary Lookup Data Structures",
                        "headers": ["Data Structure", "Exact Search", "Prefix Query (`startsWith`)", "Ordered Traversal"],
                        "rows": [
                            ["Hash Set (`unordered_set`)", "O(L) avg", "O(N * L) — fails prefix!", "No"],
                            ["Sorted Array + Binary Search", "O(L log N)", "O(L log N) via lower_bound", "Yes"],
                            ["Prefix Trie", "O(L) worst-case", "O(L) worst-case!", "Yes (DFS lexicographic)"]
                        ]
                    }
                ]
            },
            {
                "title": "Module 2: Brian Kernighan `n & (n-1)`, Operator Precedence & Bitmasks",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "Essential Bitwise Identities Every Systems Engineer Memorizes",
                        "content": "- **`n & (n - 1)`:** Clears the **lowest set `1`-bit** of `n`! Running this in a `while n:` loop executes only `popcount(n)` times (**Brian Kernighan's Algorithm**), and `n > 0 and (n & (n - 1)) == 0` checks if `n` is a **power of 2** in $O(1)$!\n- **`n & (-n)`:** Isolates ONLY the **lowest set `1`-bit** (via Two's Complement `-n = ~n + 1`), powering Fenwick Trees (`BIT`)!\n- **Bitwise DP Recurrence (`LC-338 Counting Bits`):**\n  `dp[i] = dp[i >> 1] + (i & 1)` (removing LSB divides by 2 + adds the popped LSB) OR `dp[i] = dp[i & (i - 1)] + 1` -> **$O(N)$ total for `0..N`**!",
                        "technical_explanation": "**Subset Enumeration via Bitmask:** Iterating `for mask in range(1 << n):` maps every integer $0 \\le \\text{mask} < 2^n$ bijectively to one subset of an $n$-element set (`mask & (1 << j)` tests membership of item `j`)."
                    },
                    {
                        "type": "debugger",
                        "title": "Bug Hunt: The Silent Operator Precedence Trap",
                        "code": """bool isEven(int x) {
    return (x & 1 == 0);
}""",
                        "question": "Why does `isEven(4)` shockingly return `false` (`0`) in BOTH C++ and Python (`x & 1 == 0`)?!",
                        "options": [
                            "`==` has HIGHER operator precedence than `&`, so `x & (1 == 0)` evaluates `x & 0 == 0`!",
                            "1 cannot be bitwise ANDed with an even integer",
                            "Right-associativity evaluates `bool == int` backward",
                            "C++ forbids bitwise operations inside boolean functions"
                        ],
                        "answer": "`==` has HIGHER operator precedence than `&`, so `x & (1 == 0)` evaluates `x & 0 == 0`!",
                        "explanation": "Due to historic B-language ancestry, C/C++, Java, JS, AND Python all bind `==` tighter than `&`, `^`, and `|`! Always parenthesize: **`(x & 1) == 0`**."
                    },
                    {
                        "type": "calculation_challenge",
                        "title": "Trace Brian Kernighan Loop Iterations",
                        "question": "Starting with `x = 0b1011000` (decimal `88`), how many iterations does `while x: x &= (x - 1); count += 1` execute before `x == 0`?",
                        "answer": "3",
                        "alternatives": ["3"],
                        "step_by_step": "`x = 0b1011000` has exactly three `1`-bits. Iteration 1 clears bit 3 (`0b1010000`), Iteration 2 clears bit 4 (`0b1000000`), Iteration 3 clears bit 6 (`0b0`) -> **3 iterations**."
                    }
                ]
            },
            {
                "title": "Module 3: Coding Lab I — Implement Trie (Prefix Tree) (LC-208)",
                "blocks": [
                    {
                        "type": "dsa_problem",
                        "title": "Implement Trie (Prefix Tree)",
                        "platform_style": "LeetCode 208 • Coding Ninjas Trie Design Classic",
                        "difficulty": "Medium",
                        "pattern": "Trie Node Tree (26-Way / Dict Children + isEnd Flag)",
                        "target_time": "O(L) per operation",
                        "target_space": "O(Total Chars Inserted)",
                        "statement": "Implement the `Trie` class with three methods:\n\n1. `Trie()` — Initializes the empty trie object.\n2. `insert(word)` — Inserts string `word` into the trie.\n3. `search(word)` — Returns `true` ONLY if `word` was inserted as a **complete word** (`isEnd == true`).\n4. `startsWith(prefix)` — Returns `true` if there is ANY previously inserted word starting with `prefix`.",
                        "examples": [
                            {"input": "insert(\"apple\"), search(\"apple\"), search(\"app\"), startsWith(\"app\"), insert(\"app\"), search(\"app\")", "output": "[true, false, true, true]", "explanation": "Before insert(\"app\"), \"app\" exists as a prefix (startsWith=true) but NOT as a complete word (search=false)!"},
                            {"input": "search(\"\"), insert(\"a\"), startsWith(\"a\"), startsWith(\"ab\")", "output": "[false, true, false]", "explanation": "Prefix \"ab\" misses after node 'a'."}
                        ],
                        "constraints": [
                            "$1 \\le \\text{word.length}, \\text{prefix.length} \\le 2000$",
                            "Consists only of lowercase English letters `'a'..'z'`.",
                            "Up to $3 \\times 10^4$ total calls across methods."
                        ],
                        "approach_ladder": {
                            "optimal": "Represent each node with a child lookup (`dict` in Python, `TrieNode* child[26] = {}` or flat vector pool in C++) and `bool isEnd = false`. Write a shared private `_find(s)` helper returning the final node or `None`/`nullptr`: `search(w)` checks `node is not None and node.isEnd`, while `startsWith(p)` simply checks `node is not None`! **$O(L)$ per op**."
                        },
                        "dry_run": "`insert('apple')` builds chain `a->p->p->l->e` with `e.isEnd=True`. `search('app')` reaches second `p` (`p.isEnd=False`) -> **False**. `startsWith('app')` reaches `p` -> **True**.",
                        "edge_cases": [
                            {"title": "Duplicate Word Re-Insert", "desc": "Inserting `'app'` after `'apple'` MUST NOT overwrite child pointers (`l -> e`); only traverse existing child and flip `node.isEnd = True`!"},
                            {"title": "Empty Prefix or Missing Branch", "desc": "Uninserted queries return `False` without crashing on missing keys/nullptrs."}
                        ],
                        "follow_ups": "**LC-211 Design Add & Search Words (`.` wildcard):** Run DFS branching over all present children whenever pattern matches `'.'`!",
                        "hint": "Have `search` and `startsWith` share one traversal helper returning the last matched node (or `None`/`nullptr`). Only `search` checks `node.is_end`.",
                        "starter_py": "class Trie:\n    def __init__(self):\n        # TODO: Initialize root Trie node\n        pass\n\n    def insert(self, word: str) -> None:\n        pass\n\n    def search(self, word: str) -> bool:\n        return False\n\n    def startsWith(self, prefix: str) -> bool:\n        return False\n",
                        "solution_py": "class _TrieNode:\n    __slots__ = ('children', 'is_end')\n    def __init__(self):\n        self.children = {}\n        self.is_end = False\n\nclass Trie:\n    def __init__(self):\n        self.root = _TrieNode()\n\n    def insert(self, word: str) -> None:\n        cur = self.root\n        for ch in word:\n            if ch not in cur.children:\n                cur.children[ch] = _TrieNode()\n            cur = cur.children[ch]\n        cur.is_end = True\n\n    def _walk(self, s: str):\n        cur = self.root\n        for ch in s:\n            if ch not in cur.children:\n                return None\n            cur = cur.children[ch]\n        return cur\n\n    def search(self, word: str) -> bool:\n        node = self._walk(word)\n        return node is not None and node.is_end\n\n    def startsWith(self, prefix: str) -> bool:\n        return self._walk(prefix) is not None\n",
                        "harness_py": "def _run_trie_seq(ops):\n    t = Trie()\n    out = []\n    for op, arg in ops:\n        if op == 'insert': t.insert(arg)\n        elif op == 'search': out.append(t.search(arg))\n        elif op == 'starts': out.append(t.startsWith(arg))\n    return out\n\n_dsa_run_tests([\n    ('Sample 1: apple then app', 'insert(apple), search(apple/app), starts(app), insert(app), search(app)', lambda: _run_trie_seq([('insert','apple'),('search','apple'),('search','app'),('starts','app'),('insert','app'),('search','app')]), [True, False, True, True]),\n    ('Sample 2: Empty Trie & Misses', 'search(a), insert(a), starts(a), starts(ab)', lambda: _run_trie_seq([('search','a'),('insert','a'),('starts','a'),('starts','ab')]), [False, True, False]),\n    ('Edge: Longer Word After Shorter', 'insert(go), insert(goal), search(go), search(goal), search(goa)', lambda: _run_trie_seq([('insert','go'),('insert','goal'),('search','go'),('search','goal'),('search','goa')]), [True, True, False]),\n    ('Edge: Branch Isolation', 'insert(cat), insert(car), search(ca), starts(ca), search(cab)', lambda: _run_trie_seq([('insert','cat'),('insert','car'),('search','ca'),('starts','ca'),('search','cab')]), [False, True, False]),\n], sample_only=__DSA_SAMPLE_ONLY__, n_samples=2)",
                        "starter_cpp": "class Trie {\npublic:\n    Trie() {\n        // TODO: Initialize root\n    }\n    void insert(string word) {\n    }\n    bool search(string word) {\n        return false;\n    }\n    bool startsWith(string prefix) {\n        return false;\n    }\n};\n",
                        "solution_cpp": "class Trie {\n    struct Node {\n        array<int, 26> next;\n        bool isEnd = false;\n        Node() { next.fill(-1); }\n    };\n    vector<Node> nodes;\n    int walk(const string& s) const {\n        int cur = 0;\n        for (char ch : s) {\n            int idx = nodes[cur].next[ch - 'a'];\n            if (idx == -1) return -1;\n            cur = idx;\n        }\n        return cur;\n    }\npublic:\n    Trie() { nodes.emplace_back(); }\n    void insert(string word) {\n        int cur = 0;\n        for (char ch : word) {\n            int c = ch - 'a';\n            if (nodes[cur].next[c] == -1) {\n                nodes[cur].next[c] = (int)nodes.size();\n                nodes.emplace_back();\n            }\n            cur = nodes[cur].next[c];\n        }\n        nodes[cur].isEnd = true;\n    }\n    bool search(string word) {\n        int idx = walk(word);\n        return idx != -1 && nodes[idx].isEnd;\n    }\n    bool startsWith(string prefix) {\n        return walk(prefix) != -1;\n    }\n};\n",
                        "harness_cpp": "int main() {\n    ostringstream _dbg; streambuf* _old = cout.rdbuf(_dbg.rdbuf());\n    vector<_DSACaseOut> _res;\n    auto runSeq = [](const vector<pair<int,string>>& ops) {\n        Trie tr;\n        vector<bool> out;\n        for (const auto& [op, arg] : ops) {\n            if (op == 0) tr.insert(arg);\n            else if (op == 1) out.push_back(tr.search(arg));\n            else out.push_back(tr.startsWith(arg));\n        }\n        return out;\n    };\n    struct T { string name, inp; vector<pair<int,string>> ops; vector<bool> exp; };\n    vector<T> tests = {\n        {\"Sample 1: apple then app\", \"insert(apple)...\", {{0,\"apple\"},{1,\"apple\"},{1,\"app\"},{2,\"app\"},{0,\"app\"},{1,\"app\"}}, {true,false,true,true}},\n        {\"Sample 2: Empty Trie & Misses\", \"search(a), insert(a)...\", {{1,\"a\"},{0,\"a\"},{2,\"a\"},{2,\"ab\"}}, {false,true,false}},\n        {\"Edge: Shorter Then Longer\", \"go, goal\", {{0,\"go\"},{0,\"goal\"},{1,\"go\"},{1,\"goal\"},{1,\"goa\"}}, {true,true,false}},\n        {\"Edge: Branch Isolation\", \"cat, car\", {{0,\"cat\"},{0,\"car\"},{1,\"ca\"},{2,\"ca\"},{1,\"cab\"}}, {false,true,false}}\n    };\n    int lim = DSA_SAMPLE_ONLY ? 2 : (int)tests.size();\n    for (int i = 0; i < lim; ++i) {\n        auto t0 = chrono::steady_clock::now();\n        auto act = runSeq(tests[i].ops);\n        double ms = chrono::duration<double, milli>(chrono::steady_clock::now() - t0).count();\n        _res.push_back({tests[i].name, tests[i].inp, _dsa_fmt(tests[i].exp), _dsa_fmt(act), \"\", act == tests[i].exp, ms});\n    }\n    cout.rdbuf(_old);\n    _dsa_emit_json(_res, _dbg.str());\n    return 0;\n}"
                    }
                ]
            },
            {
                "title": "Module 4: Coding Lab II — Counting Bits in O(N) Time (LC-338)",
                "blocks": [
                    {
                        "type": "dsa_problem",
                        "title": "Counting Bits (O(N) Bitwise DP)",
                        "platform_style": "LeetCode 338 • Coding Ninjas Bit Manipulation Sprint",
                        "difficulty": "Easy",
                        "pattern": "Bitwise DP (`dp[i] = dp[i >> 1] + (i & 1)`)",
                        "target_time": "O(N)",
                        "target_space": "O(N) output",
                        "statement": "Given an integer `n`, return an array `ans` of length `n + 1` such that for each `i` (`0 <= i <= n`), `ans[i]` is the **number of `1`'s** in the binary representation of `i`.\n\n**Challenge:** Solve it in **$O(N)$ linear time** (one single pass, without calling `popcount` or looping over bits inside an inner loop!).",
                        "examples": [
                            {"input": "n = 2", "output": "[0, 1, 1]", "explanation": "0->0 (0), 1->1 (1), 2->10 (1)."},
                            {"input": "n = 5", "output": "[0, 1, 1, 2, 1, 2]", "explanation": "3->11 (2), 4->100 (1), 5->101 (2)."}
                        ],
                        "constraints": [
                            "$0 \\le n \\le 10^5$"
                        ],
                        "approach_ladder": {
                            "brute": "Run Kernighan bit-count loop for every `i` from `0..n`: **$O(N \\log N)$**.",
                            "optimal": "Notice shifting `i` right (`i >> 1`) drops ONLY its least significant bit `(i & 1)`, leaving a smaller index `< i` already stored in `dp[i >> 1]`! Thus **`dp[i] = dp[i >> 1] + (i & 1)`** (or Kernighan DP **`dp[i] = dp[i & (i - 1)] + 1`**) runs in exact **$O(N)$**!"
                        },
                        "dry_run": "`n=5`: `dp[0]=0`, `dp[1]=dp[0]+1=1`, `dp[2]=dp[1]+0=1`, `dp[3]=dp[1]+1=2`, `dp[4]=dp[2]+0=1`, `dp[5]=dp[2]+1=2` -> **`[0, 1, 1, 2, 1, 2]`**.",
                        "edge_cases": [
                            {"title": "`n == 0` Minimum Boundary", "desc": "Returns `[0]` of length `1`."}
                        ],
                        "follow_ups": "**LC-191 Number of 1 Bits / LC-268 Missing Number:** Use `XOR` across `0..n` and `nums` to isolate the missing value in $O(1)$ space!",
                        "hint": "Fill `ans = [0] * (n + 1)`. For `i in range(1, n + 1)`: `ans[i] = ans[i >> 1] + (i & 1)`.",
                        "starter_py": "class Solution:\n    def countBits(self, n: int) -> List[int]:\n        # TODO: O(N) bitwise DP\n        return []\n",
                        "solution_py": "class Solution:\n    def countBits(self, n: int) -> List[int]:\n        ans = [0] * (n + 1)\n        for i in range(1, n + 1):\n            ans[i] = ans[i >> 1] + (i & 1)\n        return ans\n",
                        "harness_py": "_dsa_run_tests([\n    ('Sample 1: n=2', 'n = 2', lambda: Solution().countBits(2), [0, 1, 1]),\n    ('Sample 2: n=5', 'n = 5', lambda: Solution().countBits(5), [0, 1, 1, 2, 1, 2]),\n    ('Edge: n=0', 'n = 0', lambda: Solution().countBits(0), [0]),\n    ('Edge: Power of 2 Boundary n=8', 'n = 8', lambda: Solution().countBits(8), [0, 1, 1, 2, 1, 2, 2, 3, 1]),\n], sample_only=__DSA_SAMPLE_ONLY__, n_samples=2)",
                        "starter_cpp": "class Solution {\npublic:\n    vector<int> countBits(int n) {\n        // TODO: O(N) DP ans[i] = ans[i >> 1] + (i & 1)\n        return {};\n    }\n};\n",
                        "solution_cpp": "class Solution {\npublic:\n    vector<int> countBits(int n) {\n        vector<int> ans(n + 1, 0);\n        for (int i = 1; i <= n; ++i) {\n            ans[i] = ans[i >> 1] + (i & 1);\n        }\n        return ans;\n    }\n};\n",
                        "harness_cpp": "int main() {\n    ostringstream _dbg; streambuf* _old = cout.rdbuf(_dbg.rdbuf());\n    vector<_DSACaseOut> _res;\n    struct T { string name, inp; int n; vector<int> exp; };\n    vector<T> tests = {\n        {\"Sample 1: n=2\", \"n = 2\", 2, {0,1,1}},\n        {\"Sample 2: n=5\", \"n = 5\", 5, {0,1,1,2,1,2}},\n        {\"Edge: n=0\", \"n = 0\", 0, {0}},\n        {\"Edge: n=8\", \"n = 8\", 8, {0,1,1,2,1,2,2,3,1}}\n    };\n    int lim = DSA_SAMPLE_ONLY ? 2 : (int)tests.size();\n    Solution sol;\n    for (int i = 0; i < lim; ++i) {\n        auto t0 = chrono::steady_clock::now();\n        auto act = sol.countBits(tests[i].n);\n        double ms = chrono::duration<double, milli>(chrono::steady_clock::now() - t0).count();\n        _res.push_back({tests[i].name, tests[i].inp, _dsa_fmt(tests[i].exp), _dsa_fmt(act), \"\", act == tests[i].exp, ms});\n    }\n    cout.rdbuf(_old);\n    _dsa_emit_json(_res, _dbg.str());\n    return 0;\n}"
                    }
                ]
            }
        ]
    }
}
