import json
from level_content import LEVEL_CONTENT

# EXPAND MODULE 3
mod3 = LEVEL_CONTENT['4']['episodes'][2]['blocks']
mod3.extend([
    {
        "type": "concept",
        "title": "The Balance of g(n) and h(n)",
        "content": "A* is a balancing act. \n\nIf `h(n)` is always 0, A* completely ignores the heuristic and becomes **Uniform Cost Search (Dijkstra)**. It is perfectly optimal but explores slowly.\n\nIf `h(n)` is much larger than `g(n)`, A* completely ignores the path cost and becomes **Greedy Best-First Search**. It is blazingly fast but finds terrible paths."
    },
    {
        "type": "interactive",
        "question": "What happens to A* if we set h(n) = 0 for every node?",
        "options": [
            "It turns into Breadth-First Search",
            "It turns into Dijkstra's Algorithm",
            "It turns into Greedy Search"
        ],
        "answer": "It turns into Dijkstra's Algorithm"
    },
    {
        "type": "markdown",
        "content": "> [!NOTE] \n> The magic of A* happens when `h(n)` is *exactly* the true cost to the goal. In this hypothetical scenario, A* will never expand a single incorrect node. It will follow the optimal path instantly without searching any side branches."
    },
    {
        "type": "concept",
        "title": "Tie-Breaking",
        "content": "What happens if two nodes have the exact same `f(n)` value? \n\nA* will pull one arbitrarily based on the Priority Queue's internal sorting. However, advanced implementations often break ties by preferring the node with the *higher* `g(n)` (meaning it's further along the path) or the *lower* `h(n)` (meaning it's closer to the goal)."
    }
])

# EXPAND MODULE 5
mod5 = LEVEL_CONTENT['4']['episodes'][4]['blocks']
mod5.extend([
    {
        "type": "visual",
        "title": "The Triangle Inequality",
        "code": """
graph TD
    classDef n fill:#10b9811a,stroke:#34D399,stroke-width:2px;
    
    A["Node N"]:::n -->|Cost=c| B["Successor P"]:::n
    A -.->|h(N)| C["Goal"]:::n
    B -.->|h(P)| C
        """
    },
    {
        "type": "markdown",
        "content": "Look at the triangle above. For a heuristic to be **consistent** (monotonic), the estimated cost from N to the Goal, `h(N)`, cannot be greater than the cost to get to P plus the estimated cost from P to the Goal, `h(P)`.\n\n**h(N) ≤ c(N, P) + h(P)**"
    },
    {
        "type": "concept",
        "title": "Why Consistency is Powerful",
        "content": "If a heuristic is consistent, it means the `f(n)` values along any path will NEVER decrease. They are monotonically non-decreasing. \n\nBecause of this, the very first time A* expands a node, it has *guaranteed* that it found the absolute shortest path to that node. It never has to go back and update costs."
    },
    {
        "type": "interactive",
        "question": "If a heuristic is consistent, is it also admissible?",
        "options": [
            "Yes, always.",
            "No, never.",
            "Sometimes."
        ],
        "answer": "Yes, always."
    },
    {
        "type": "markdown",
        "content": "> [!IMPORTANT] \n> Every consistent heuristic is admissible, but not every admissible heuristic is consistent. However, in practice, almost all natural admissible heuristics (like straight-line distance) are also consistent."
    }
])

# EXPAND MODULE 6
mod6 = LEVEL_CONTENT['4']['episodes'][5]['blocks']
mod6.extend([
    {
        "type": "concept",
        "title": "The Depth-First Advantage",
        "content": "Iterative Deepening A* (IDA*) uses a Depth-First Search internally. This is brilliant because DFS only requires memory proportional to the length of the current path (`O(bd)` memory). \n\nA* requires memory for every single node it generates (`O(b^d)` memory)."
    },
    {
        "type": "interactive",
        "question": "Instead of using depth as a cutoff limit, what does IDA* use as its cutoff limit?",
        "options": [
            "The g(n) cost",
            "The f(n) cost",
            "The h(n) heuristic"
        ],
        "answer": "The f(n) cost"
    },
    {
        "type": "markdown",
        "content": "> [!WARNING] \n> The downside of IDA* is that it recalculates nodes multiple times, just like standard Iterative Deepening Search. It trades computation time for memory."
    },
    {
        "type": "concept",
        "title": "The Memory Limit in SMA*",
        "content": "Simplified Memory-Bounded A* (SMA*) takes a different approach. It runs standard A* until it hits the hardware RAM limit. \n\nWhen memory is full, it looks at the frontier and deletes the node with the highest `f` value. But before it deletes it, it updates its parent node to remember that \"there was a path down here with an f-value of X\". \n\nIf all other paths turn out to be worse than X, SMA* will regenerate the deleted node."
    },
    {
        "type": "interactive",
        "question": "When SMA* runs out of memory, which node does it delete?",
        "options": [
            "The oldest node",
            "The node with the lowest f-value",
            "The node with the highest f-value"
        ],
        "answer": "The node with the highest f-value"
    }
])

with open('level_content.py', 'w', encoding='utf-8') as f:
    f.write("LEVEL_CONTENT = \\\n")
    json.dump(LEVEL_CONTENT, f, indent=4, ensure_ascii=False)

print("Massively expanded Modules 3, 5, and 6!")
