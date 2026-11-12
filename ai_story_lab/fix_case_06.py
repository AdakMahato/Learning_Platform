import json
from level_content import LEVEL_CONTENT

deep_blocks = [
    {
        "type": "markdown",
        "content": "You are sitting in the NEXUS Simulation Control Room. Until now, your agents have been solving puzzles in static environments. But today, the red lights flash. A rogue agent—designated 'NEMESIS'—has entered the simulation grid. NEMESIS has exactly the opposite goals as your agent. Every time you make a move to maximize your score, NEMESIS will make a move to minimize it."
    },
    {
        "type": "objective",
        "title": "Module Objective",
        "content": "Master Adversarial Search. Learn how to construct a Game Tree, understand the Minimax algorithm, and implement Alpha-Beta Pruning to defeat an optimal opponent."
    },
    {
        "type": "problem",
        "content": "**The Think-First Challenge:** If you know your opponent is playing perfectly, should you ever make a move that relies on them making a mistake? What happens if you assume they are 'dumb' but they turn out to be optimal?"
    },
    {
        "type": "concept",
        "title": "The Zero-Sum Game",
        "content": "In AI, a strictly competitive environment is called a **Zero-Sum Game**. If you win +10 points, the opponent loses -10 points. The sum of the utilities is always zero. \n\nTo solve this, we create a **Game Tree** where:\n*   **MAX (You):** Wants to find the path that leads to the highest possible number.\n*   **MIN (Nemesis):** Wants to find the path that leads to the lowest possible number."
    },
    {
        "type": "visual",
        "title": "The Minimax Decision Tree",
        "code": """
graph TD
    classDef maxNode fill:rgba(16, 185, 129, 0.1),stroke:#34D399,stroke-width:2px;
    classDef minNode fill:rgba(239, 68, 68, 0.1),stroke:#FCA5A5,stroke-width:2px;
    classDef leafNode fill:rgba(124, 77, 255, 0.1),stroke:#7C4DFF,stroke-width:2px;

    A[MAX: Your Turn]:::maxNode --> B[MIN: Nemesis Turn]:::minNode
    A --> C[MIN: Nemesis Turn]:::minNode
    
    B --> D[+3]:::leafNode
    B --> E[+12]:::leafNode
    B --> F[+8]:::leafNode
    
    C --> G[+2]:::leafNode
    C --> H[+4]:::leafNode
    C --> I[+6]:::leafNode
        """
    },
    {
        "type": "concept",
        "title": "Working Through the Tree",
        "content": "Let's trace the diagram above from the bottom up. \n\n1. At node **B**, it is MIN's turn. MIN looks at the choices: `+3`, `+12`, and `+8`. Because MIN wants to hurt you, MIN chooses the lowest number: `+3`.\n2. At node **C**, MIN looks at `+2`, `+4`, and `+6`. MIN chooses `+2`.\n3. Now we go up to node **A**. It is MAX's turn. You look at the values that MIN passed up to you: Node B is worth `+3`, and Node C is worth `+2`. You want the highest number, so you choose to go to Node B.\n\nEven though Node B hides a massive `+12`, you will never get it, because MIN is smart enough to block you and force you into the `+3`."
    },
    {
        "type": "markdown",
        "content": "> [!WARNING] \n> **The Beginner Mistake:** A beginner AI looks at the board, sees the `+12`, and greedily chooses to go to Node B, hoping the opponent is stupid. An optimal AI assumes the opponent is perfect and settles for the guaranteed `+3`."
    },
    {
        "type": "code_experiment",
        "title": "Implementing the Base Case (Leaf Nodes)",
        "starter_code": "def evaluate_board(board_state):\n    # TODO: Write a function that returns a static score for a terminal board state.\n    # For this exercise, if the board is 'WIN', return 100.\n    # If 'LOSS', return -100.\n    # If 'DRAW', return 0.\n    pass",
        "solution_code": "def evaluate_board(board_state):\n    if board_state == 'WIN': return 100\n    if board_state == 'LOSS': return -100\n    if board_state == 'DRAW': return 0\n    return 0",
        "expected_output": "100\n-100\n0",
        "explanation": "**Why it works:** Every recursive algorithm needs a base case. In Minimax, the base case is a terminal state (the game is over) or a depth limit where we use a heuristic evaluation function to guess the board's value.",
        "test_cases": []
    },
    {
        "type": "concept",
        "title": "The Time Complexity Nightmare",
        "content": "Minimax is elegant, but it has a fatal flaw. The time complexity is **O(b^m)**, where `b` is the branching factor (legal moves per turn) and `m` is the maximum depth of the game.\n\nIn chess, the branching factor is about 35. To look ahead just 10 moves, Minimax would need to evaluate **35^10 = 2.7 quadrillion** board states. The universe would end before your AI makes its first move."
    },
    {
        "type": "concept",
        "title": "Alpha-Beta Pruning",
        "content": "To solve this, we introduce **Alpha-Beta Pruning**. It allows us to stop evaluating a branch of the tree as soon as we realize that it will never be selected by the parent nodes.\n\n*   **Alpha (α):** The value of the best (highest) choice we have found so far for MAX.\n*   **Beta (β):** The value of the best (lowest) choice we have found so far for MIN.\n\nIf at any point `Beta <= Alpha`, we **prune** the rest of the branch because we know the opponent will never let us go down it."
    },
    {
        "type": "visual",
        "title": "Visualizing the Prune",
        "code": """
graph TD
    classDef maxNode fill:rgba(16, 185, 129, 0.1),stroke:#34D399,stroke-width:2px;
    classDef minNode fill:rgba(239, 68, 68, 0.1),stroke:#FCA5A5,stroke-width:2px;
    classDef pruned fill:rgba(0,0,0,0.5),stroke:#333,stroke-width:1px,stroke-dasharray: 5 5;

    A[MAX]:::maxNode --> B[MIN: Current best is 3]:::minNode
    A --> C[MIN]:::minNode
    
    B --> D[3]
    B --> E[12]
    
    C --> F[2]
    C -.-> G[Pruned]:::pruned
    C -.-> H[Pruned]:::pruned
        """
    },
    {
        "type": "markdown",
        "content": "> [!NOTE] \n> In the diagram above, Node C evaluates its first child and gets `2`. Because MAX already has a guaranteed `3` from Node B, MAX will *never* choose Node C (since `2` is worse than `3`, and MIN will only make it even worse). Therefore, we can immediately stop evaluating Node C's other children!"
    },
    {
        "type": "code_lab",
        "title": "The Alpha-Beta Algorithm",
        "starter_code": "def alpha_beta(node, depth, alpha, beta, maximizing_player):\n    # node has .is_terminal(), .value, and .children[]\n    if depth == 0 or node.is_terminal():\n        return node.value\n        \n    if maximizing_player:\n        max_eval = float('-inf')\n        for child in node.children:\n            eval = alpha_beta(child, depth - 1, alpha, beta, False)\n            # TODO: Update max_eval\n            # TODO: Update alpha\n            # TODO: Add the pruning condition\n        return max_eval\n    else:\n        min_eval = float('inf')\n        for child in node.children:\n            eval = alpha_beta(child, depth - 1, alpha, beta, True)\n            # TODO: Update min_eval\n            # TODO: Update beta\n            # TODO: Add the pruning condition\n        return min_eval",
        "solution_code": "def alpha_beta(node, depth, alpha, beta, maximizing_player):\n    if depth == 0 or node.is_terminal():\n        return node.value\n        \n    if maximizing_player:\n        max_eval = float('-inf')\n        for child in node.children:\n            eval = alpha_beta(child, depth - 1, alpha, beta, False)\n            max_eval = max(max_eval, eval)\n            alpha = max(alpha, eval)\n            if beta <= alpha:\n                break  # Prune!\n        return max_eval\n    else:\n        min_eval = float('inf')\n        for child in node.children:\n            eval = alpha_beta(child, depth - 1, alpha, beta, True)\n            min_eval = min(min_eval, eval)\n            beta = min(beta, eval)\n            if beta <= alpha:\n                break  # Prune!\n        return min_eval",
        "expected_output": "",
        "explanation": "**Why it works:** By passing down `alpha` and `beta`, the algorithm essentially 'remembers' the best alternatives found elsewhere in the tree. When `beta <= alpha`, the current path is mathematically proven to be irrelevant, saving us millions of calculations."
    }
]

LEVEL_CONTENT['6'] = {
    "episodes": [
        {
            "blocks": deep_blocks
        }
    ]
}

with open('level_content.py', 'w', encoding='utf-8') as f:
    f.write("LEVEL_CONTENT = \\\n")
    json.dump(LEVEL_CONTENT, f, indent=4, ensure_ascii=False)

print("Injected deep content into Case 06!")
