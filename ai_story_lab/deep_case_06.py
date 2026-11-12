import json
from level_content import LEVEL_CONTENT

# Recombine into Module 1
blocks_mod_1 = []
for ep in LEVEL_CONTENT['6']['episodes']:
    blocks_mod_1.extend(ep['blocks'])

# Generate a MASSIVE Module 2
blocks_mod_2 = [
    {
        "type": "markdown",
        "content": "Now that you understand the theory of Alpha-Beta Pruning, it's time to build a real AI. NEMESIS has challenged you to a game of Tic-Tac-Toe. It sounds trivial, but a fully optimal Minimax agent will never lose."
    },
    {
        "type": "objective",
        "title": "Module Objective",
        "content": "Implement a complete, working Minimax agent for Tic-Tac-Toe that cannot be defeated."
    },
    {
        "type": "concept",
        "title": "Representing the State Space",
        "content": "Before we can search, we must represent the board. We will use a simple 1D array of length 9, where `0` is empty, `1` is MAX (X), and `-1` is MIN (O)."
    },
    {
        "type": "code_experiment",
        "title": "State Transition Function",
        "starter_code": "def get_available_moves(board):\n    # TODO: Return a list of indices (0-8) that are currently empty (0)\n    pass",
        "solution_code": "def get_available_moves(board):\n    return [i for i, spot in enumerate(board) if spot == 0]",
        "expected_output": "",
        "explanation": "**Why it works:** To generate the branches of our Game Tree, we need to know all legal moves from the current state."
    },
    {
        "type": "concept",
        "title": "The Recursive Mind",
        "content": "When Minimax evaluates a board, it effectively plays out the entire rest of the game in its head. It places an 'X', then asks 'If I do this, what is the best move 'O' can make in response?'. It does this all the way down until someone wins, loses, or the board is full (a draw)."
    },
    {
        "type": "code_lab",
        "title": "The Perfect Tic-Tac-Toe Agent",
        "starter_code": "def check_winner(board):\n    # Returns 1 (X wins), -1 (O wins), 0 (Draw/Ongoing)\n    win_lines = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]\n    for a,b,c in win_lines:\n        if board[a] != 0 and board[a] == board[b] == board[c]:\n            return board[a]\n    if 0 not in board: return 0\n    return None\n\ndef optimal_move(board, is_max):\n    # TODO: Implement the full Minimax loop to return the best index to play.\n    pass",
        "solution_code": "def check_winner(board):\n    win_lines = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]\n    for a,b,c in win_lines:\n        if board[a] != 0 and board[a] == board[b] == board[c]: return board[a]\n    if 0 not in board: return 0\n    return None\n\ndef minimax(board, is_max):\n    winner = check_winner(board)\n    if winner is not None: return winner\n    \n    if is_max:\n        best = float('-inf')\n        for i in range(9):\n            if board[i] == 0:\n                board[i] = 1\n                best = max(best, minimax(board, False))\n                board[i] = 0\n        return best\n    else:\n        best = float('inf')\n        for i in range(9):\n            if board[i] == 0:\n                board[i] = -1\n                best = min(best, minimax(board, True))\n                board[i] = 0\n        return best\n\ndef optimal_move(board, is_max):\n    best_val = float('-inf') if is_max else float('inf')\n    best_move = -1\n    player = 1 if is_max else -1\n    \n    for i in range(9):\n        if board[i] == 0:\n            board[i] = player\n            move_val = minimax(board, not is_max)\n            board[i] = 0\n            \n            if is_max and move_val > best_val:\n                best_val = move_val\n                best_move = i\n            elif not is_max and move_val < best_val:\n                best_val = move_val\n                best_move = i\n                \n    return best_move",
        "expected_output": "",
        "explanation": "**Why it works:** This is the complete, unpruned algorithm. The `optimal_move` function acts as the root of the tree, trying every available move and asking `minimax()` to evaluate how good it is. By iterating through all possibilities and backtracking (`board[i] = 0`), the AI maps out the entire future."
    }
]

# Generate Module 3: Advanced Optimization
blocks_mod_3 = [
    {
        "type": "markdown",
        "content": "Tic-Tac-Toe has 255,168 possible games. Minimax solves this instantly. But what if NEMESIS challenges you to Connect 4? That game has 4.5 trillion states. Chess has 10^43 states. Raw Minimax is completely useless here."
    },
    {
        "type": "concept",
        "title": "Depth-Limited Search & Evaluation Functions",
        "content": "When we cannot reach a terminal state (a win or loss), we must stop the search early. We introduce a `depth` limit. When the depth hits 0, we call an **Evaluation Function**."
    },
    {
        "type": "visual",
        "title": "Depth-Limited Pruning",
        "code": """
graph TD
    classDef maxNode fill:rgba(16, 185, 129, 0.1),stroke:#34D399,stroke-width:2px;
    classDef cutoff fill:rgba(255, 152, 0, 0.1),stroke:#FF9800,stroke-width:2px;

    A[Current Board]:::maxNode --> B[Depth 1]
    A --> C[Depth 1]
    
    B --> D[Depth 2]
    B --> E[Depth 2]
    
    D --> F[Depth 3: CUTOFF]:::cutoff
    D --> G[Depth 3: CUTOFF]:::cutoff
    
    F -.-> H[Evaluate: +4.5]
    G -.-> I[Evaluate: -1.2]
        """
    },
    {
        "type": "problem",
        "content": "**The Design Challenge:** How do you evaluate a Chess board that isn't finished? You might count the pieces (Queen = 9, Rook = 5). But what if the King is exposed? An evaluation function must balance material advantage with positional advantage."
    }
]

LEVEL_CONTENT['6'] = {
    "episodes": [
        {
            "title": "Module 1: The Nemesis Protocol",
            "blocks": blocks_mod_1
        },
        {
            "title": "Module 2: Building the Perfect Agent",
            "blocks": blocks_mod_2
        },
        {
            "title": "Module 3: Scaling to the Real World",
            "blocks": blocks_mod_3
        }
    ]
}

with open('level_content.py', 'w', encoding='utf-8') as f:
    f.write("LEVEL_CONTENT = \\\n")
    json.dump(LEVEL_CONTENT, f, indent=4, ensure_ascii=False)

print("Injected extreme depth into Case 06!")
