import json
import re

print("Loading level_content.py...")
with open('/Users/aadarshamahato/Downloads/LEARNING_PLATFORM/ai_story_lab/level_content.py', 'r', encoding='utf-8') as f:
    text = f.read()

ns = {}
exec(text, ns)
LEVEL_CONTENT = ns['LEVEL_CONTENT']

# Comprehensive updates for the 19 fill-in-the-blank blocks
FIB_UPDATES = {
    # Case 0 Ep 1 Block 3
    ("0", 1, 3): {
        "question": "Which approach to AI attempts to perfectly simulate the psychological and neurological processes of the human brain?\n\nAnswer: _____",
        "answer": "Cognitive Modeling",
        "alternatives": ["Cognitive Modeling (Thinking Humanly)", "Thinking Humanly", "Cognitive Science", "Cognitive model"],
        "explanation": "**Why Cognitive Modeling is Correct:**\n**Cognitive Modeling** (the 'Thinking Humanly' approach) focuses on developing computational models that accurately simulate internal human psychological and neurological decision-making processes."
    },
    # Case 0 Ep 2 Block 3
    ("0", 2, 3): {
        "question": "Does passing the Turing Test guarantee that a machine possesses real conscious understanding?\n\nAnswer: _____",
        "answer": "No",
        "alternatives": ["No", "False", "It does not", "No it does not", "Negative"],
        "explanation": "**Why No is Correct:**\nJohn Searle's **Chinese Room Argument** demonstrated that a system can manipulate syntactic symbols perfectly to pass the Turing Test without possessing any actual semantic understanding or conscious awareness."
    },
    # Case 0 Ep 3 Block 8
    ("0", 3, 8): {
        "question": "Which branch of classical AI was dominant in the 1960s–1970s and relied on hard-coded logical rules?\n\nAnswer: _____",
        "answer": "Symbolic AI",
        "alternatives": ["Symbolic AI", "GOFAI", "Rule-Based AI", "Symbolic", "Good Old Fashioned AI"],
        "explanation": "**Why Symbolic AI is Correct:**\n**Symbolic AI** (Good Old-Fashioned AI or GOFAI) dominated early research by representing knowledge through explicit discrete symbols and manipulating them using formal logical deduction rules."
    },
    # Case 1 Ep 0 Block 4
    ("1", 0, 4): {
        "question": "An agent uses _____ to observe and receive telemetry from its physical environment.\n\nAnswer: _____",
        "answer": "Sensors",
        "alternatives": ["Sensors", "Sensor", "Perception sensors", "Telemetry sensors"],
        "explanation": "**Why Sensors is Correct:**\n**Sensors** (cameras, LiDAR, encoders, thermometers) are the input transducers that allow an intelligent agent to perceive changes in the external world state."
    },
    # Case 1 Ep 1 Block 2
    ("1", 1, 2): {
        "question": "In an autonomous vehicle, the metric determining driving efficiency and safety is called the _____ measure.\n\nAnswer: _____",
        "answer": "Performance",
        "alternatives": ["Performance", "Performance measure", "Utility", "Objective"],
        "explanation": "**Why Performance is Correct:**\nA **Performance Measure** provides the external mathematical criterion by which the success of an agent's behavior is objectively evaluated."
    },
    # Case 1 Ep 1 Block 8
    ("1", 1, 8): {
        "question": "Is the physical real-world environment fundamentally discrete or continuous?\n\nAnswer: _____",
        "answer": "Continuous",
        "alternatives": ["Continuous", "Continuous environment"],
        "explanation": "**Why Continuous is Correct:**\nReal-world physical environments (time, vehicle speed, coordinates, motor torque) vary continuously over real numbers ℝ."
    },
    # Case 1 Ep 3 Block 8
    ("1", 3, 8): {
        "question": "What mathematical function allows an agent to make rational trade-offs between conflicting goals under uncertainty?\n\nAnswer: _____",
        "answer": "Utility Function",
        "alternatives": ["Utility Function", "Utility", "Expected Utility", "Utility function"],
        "explanation": "**Why Utility Function is Correct:**\nA **Utility Function** maps states to real-valued scalar scores, enabling an agent to weigh risk versus reward when no single action guarantees perfect success."
    },
    # Case 2 Ep 0 Block 8 (The user's screenshot)
    ("2", 0, 8): {
        "question": "What function defines the resulting state after taking an action in a problem formulation?\n\nAnswer: _____",
        "answer": "Transition Model",
        "alternatives": ["Transition Model", "Transition Function", "Result Function", "Result(s, a)", "Result", "Transition model"],
        "explanation": "**Why Transition Model is Correct:**\nThe **Transition Model** (formalized as Result(s, a) or state transition probability P(s' | s, a)) defines the outcome state produced by executing action a in state s."
    },
    # Case 2 Ep 1 Block 4
    ("2", 1, 4): {
        "question": "How many legally reachable states exist in the standard 8-puzzle state space?\n\nAnswer: _____",
        "answer": "181440",
        "alternatives": ["181440", "181,440", "9!/2", "9! / 2", "181440 states"],
        "explanation": "**Why 181,440 is Correct:**\nThe total permutations of 9 tiles is 9! = 362,880. Because sliding tile moves preserve the mathematical parity of inversions, exactly half the permutations (9! / 2 = 181,440) are reachable from any valid start state."
    },
    # Case 2 Ep 2 Block 4
    ("2", 2, 4): {
        "question": "Is the Traveling Salesperson Problem (TSP) classified as an NP-hard problem?\n\nAnswer: _____",
        "answer": "Yes",
        "alternatives": ["Yes", "True", "NP-hard", "NP hard"],
        "explanation": "**Why Yes is Correct:**\nThe **Traveling Salesperson Problem (TSP)** is famously NP-hard; finding the guaranteed optimal Hamiltonian cycle through N cities has worst-case factorial time complexity O(N!)."
    },
    # Case 2 Ep 2 Block 8
    ("2", 2, 8): {
        "question": "In real-world engineering problems (such as chess or robot kinematics), state spaces are typically:\n\nAnswer: _____",
        "answer": "Large or infinite",
        "alternatives": ["Large or infinite", "Infinite", "Large", "Continuous", "Combinatorial"],
        "explanation": "**Why Large or Infinite is Correct:**\nReal-world problem spaces (e.g. continuous motion planning or games with 10^120 branches) are far too massive to enumerate exhaustively, requiring heuristic search algorithms."
    },
    # Case 3 Ep 0 Block 5
    ("3", 0, 5): {
        "question": "Is Breadth-First Search (BFS) guaranteed to be complete on finite graphs with finite branching factor b?\n\nAnswer: _____",
        "answer": "Yes",
        "alternatives": ["Yes", "True", "Guaranteed", "Complete"],
        "explanation": "**Why Yes is Correct:**\n**Breadth-First Search** is complete: as long as the shallowest goal is at some finite depth d and branching factor b is finite, BFS will always systematically find it."
    },
    # Case 3 Ep 1 Block 8
    ("3", 1, 8): {
        "question": "What is the primary architectural advantage of Depth-First Search over Breadth-First Search?\n\nAnswer: _____",
        "answer": "Lower space complexity",
        "alternatives": ["Lower space complexity", "Space complexity", "Memory", "Linear space", "Less memory", "O(bm) space", "Low memory"],
        "explanation": "**Why Lower Space Complexity is Correct:**\nDFS only stores the current active search path and unexpanded siblings, requiring only linear memory O(b · m) compared to BFS's exponential memory O(b^d)."
    },
    # Case 3 Ep 3 Block 4
    ("3", 3, 4): {
        "question": "In Depth-Limited Search (DLS), what is returned if the search reaches depth limit l without finding the goal?\n\nAnswer: _____",
        "answer": "Cutoff",
        "alternatives": ["Cutoff", "Cutoff failure", "Failure", "Cut off"],
        "explanation": "**Why Cutoff is Correct:**\nWhen DLS hits the depth limit l without locating a goal, it returns a special **cutoff** value to signal that the goal may exist deeper in the tree."
    },
    # Case 3 Ep 3 Block 8
    ("3", 3, 8): {
        "question": "What is the asymptotic space complexity of Iterative Deepening Search (IDS)?\n\nAnswer: _____",
        "answer": "O(bd)",
        "alternatives": ["O(bd)", "O(b*d)", "O(b d)", "Linear", "O(b*d)"],
        "explanation": "**Why O(bd) is Correct:**\nIDS combines the linear space complexity of DFS (O(b · d)) with the completeness and shallowest-depth optimality of BFS."
    },
    # Case 4 Ep 0 Block 7
    ("4", 0, 7): {
        "question": "To be considered admissible, a heuristic function h(n) must never _____ the true cost to the goal.\n\nAnswer: _____",
        "answer": "Overestimate",
        "alternatives": ["Overestimate", "Over estimate", "Exceed"],
        "explanation": "**Why Overestimate is Correct:**\nAn **Admissible Heuristic** is an optimistic lower bound (h(n) <= h*(n)). If it never overestimates, A* tree search is guaranteed to return the optimal cost path."
    },
    # Case 4 Ep 1 Block 7
    ("4", 1, 7): {
        "question": "To guarantee that A* graph search never re-expands a suboptimal path, the heuristic must satisfy:\n\nAnswer: _____",
        "answer": "Consistency",
        "alternatives": ["Consistency", "Monotonicity", "Consistent", "Monotonic", "Triangle inequality"],
        "explanation": "**Why Consistency is Correct:**\nA **Consistent (Monotonic)** heuristic satisfies the triangle inequality h(n) <= c(n, a, n') + h(n'), guaranteeing that f(n) values along any path are non-decreasing."
    },
    # Case 4 Ep 2 Block 4
    ("4", 2, 4): {
        "question": "If we set the heuristic h(n) = 0 for every node, A* becomes identical to which algorithm?\n\nAnswer: _____",
        "answer": "Uniform-Cost Search",
        "alternatives": ["Uniform-Cost Search", "Uniform Cost Search", "UCS", "Dijkstra", "Dijkstra's algorithm"],
        "explanation": "**Why Uniform-Cost Search is Correct:**\nWhen h(n) = 0, the evaluation function f(n) = g(n) + h(n) simplifies strictly to f(n) = g(n), expanding nodes in order of cumulative path cost."
    },
    # Case 4 Ep 4 Block 3
    ("4", 4, 3): {
        "question": "What happens to the optimality guarantee of A* if the heuristic overestimates the true cost?\n\nAnswer: _____",
        "answer": "Suboptimal",
        "alternatives": ["Suboptimal", "Loses optimality", "Not optimal", "May find suboptimal path", "Sub-optimal"],
        "explanation": "**Why Suboptimal is Correct:**\nIf h(n) > h*(n), the heuristic can falsely inflate the cost of the optimal path, causing A* to terminate on a cheaper-looking suboptimal goal first."
    }
}

updated_fib = 0
for (case_num, ep_idx, b_idx), data in FIB_UPDATES.items():
    if case_num in LEVEL_CONTENT:
        eps = LEVEL_CONTENT[case_num].get('episodes', [])
        if ep_idx < len(eps):
            blocks = eps[ep_idx].get('blocks', [])
            if b_idx < len(blocks):
                block = blocks[b_idx]
                block['type'] = 'fill_in_the_blank'
                block['question'] = data['question']
                block['answer'] = data['answer']
                block['alternatives'] = data['alternatives']
                block['explanation'] = data['explanation']
                updated_fib += 1
                print(f"Updated FIB for Case {case_num} Ep {ep_idx} Block {b_idx} -> {data['answer']}")

# Also scan all interactive blocks: if answer is short (<= 4 words) and ends with '.', strip the trailing '.'
stripped_dots = 0
for case_num, case in LEVEL_CONTENT.items():
    for ep_idx, ep in enumerate(case.get('episodes', [])):
        for b_idx, b in enumerate(ep.get('blocks', [])):
            if 'answer' in b and isinstance(b['answer'], str):
                ans = b['answer'].strip()
                if ans.endswith('.') and len(ans.split()) <= 4 and not ans.endswith('..'):
                    new_ans = ans.rstrip('.').strip()
                    b['answer'] = new_ans
                    stripped_dots += 1
            if 'explanation' in b and isinstance(b['explanation'], str):
                # Clean up any "**Why XYZ. is Correct:**" headers
                b['explanation'] = re.sub(r'\*\*(Why\s+.*?)\.\s+(is Correct:)\*\*', r'**\1 \2**', b['explanation'])

print(f"Total FIB blocks updated: {updated_fib}")
print(f"Total trailing periods stripped from answers: {stripped_dots}")

# Save back cleanly
dumped = json.dumps(LEVEL_CONTENT, indent=4, ensure_ascii=False)
dumped = re.sub(r':\s*true\b', ': True', dumped)
dumped = re.sub(r':\s*false\b', ': False', dumped)
dumped = re.sub(r':\s*null\b', ': None', dumped)

with open('/Users/aadarshamahato/Downloads/LEARNING_PLATFORM/ai_story_lab/level_content.py', 'w', encoding='utf-8') as f:
    f.write("# Master Curriculum Database for AI Story Lab\n")
    f.write("LEVEL_CONTENT = {\n")
    first_brace = dumped.find('{')
    f.write(dumped[first_brace+1:])
    f.write("\n")

print("Successfully written level_content.py!")
