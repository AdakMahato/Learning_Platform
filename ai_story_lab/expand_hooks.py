import json

from story_data import STORIES

new_hooks = {
    0: "Your first day at NEXUS Intelligence. Before we can build an AI, you must understand what intelligence actually means. Learn why traditional if-else rules fail in the real world, and what makes a machine truly intelligent.",
    1: "A machine is blind and deaf until it interacts with its environment. Discover the PEAS framework, build a Rational Agent, and explore how deterministic, stochastic, and partially observable environments change the way an AI must act.",
    2: "To solve a problem, an AI must first understand it. Learn how to translate real-world challenges—like navigating a maze or solving a puzzle—into strict mathematical State Spaces with initial states, actions, and goal tests.",
    3: "Your agent is lost in a massive maze. Implement classic Uninformed Search algorithms like BFS, DFS, and Uniform Cost Search. Trace their expansion step-by-step and learn why being blind is extremely computationally expensive.",
    4: "Why wander blindly when you have a map? Introduce Heuristics to guide your AI. Build Greedy Best-First Search and the legendary A* algorithm to find the optimal path without searching the entire universe of possibilities.",
    5: "Your A* agent failed to find the shortest route. Why? Dive deep into heuristic admissibility and consistency. Prove your heuristic is perfect, learn how to handle memory limits, and explore the advanced AO* algorithm for AND/OR graphs.",
    6: "Your AI is now playing against an opponent who wants it to lose. Master Adversarial Search by implementing Minimax. Then, optimize your game tree drastically by building Alpha-Beta Pruning to skip irrelevant moves.",
    7: "Not every problem is a path. Some are puzzles with strict rules. Build a Constraint Satisfaction Problem (CSP) solver using Backtracking, Arc Consistency, and the Minimum Remaining Values heuristic to solve complex logic puzzles instantly.",
    8: "An AI cannot reason without facts. Explore Knowledge Representation by building ontologies, taxonomies, and Knowledge Graphs to store data about objects, relations, and events in a way the machine can traverse.",
    9: "Given facts, how does a machine prove truth? Build a Logic Engine that uses Propositional Logic, First-Order Logic, and Inference rules to deduce new facts through forward and backward chaining.",
    10: "The world changes over time. Master Situation Calculus and Default Reasoning to allow your AI to reason about the past and predict the consequences of its actions in a dynamic, ever-changing environment.",
    11: "Your robot needs to achieve a complex goal. Implement Planning as Search. Define action preconditions and effects, build a Planning Graph, and use Partial-Order Planning to execute multiple tasks efficiently.",
    12: "The real world is messy, unpredictable, and full of hidden variables. Shift your AI from absolute logic to Probability. Master random variables, events, and conditional probabilities to handle uncertainty.",
    13: "How do you calculate the odds of an event when you only have partial evidence? Dive into the mathematics of Independence and Bayes Rule to update your AI's beliefs dynamically as new data arrives.",
    14: "Build an interactive Bayesian Network! Map out conditional dependencies visually, inject prior probabilities, and watch the inference engine calculate the likelihood of hidden diseases or system failures.",
    15: "The most probable outcome isn't always the best decision. Combine probability with Utility Theory to build a Decision Maker agent that weighs risks and rewards to choose the optimal sequential action.",
    16: "Bridge the gap between classical AI and Machine Learning. Understand how a machine learns from data instead of hardcoded rules. Explore features, labels, and the deadly traps of overfitting and underfitting.",
    17: "Learning by similarity. Build a K-Nearest Neighbors (KNN) classifier from scratch. Plot points in a 2D feature space, calculate Euclidean distances, and watch the decision boundaries shift as you change K.",
    18: "Learning by probability. Exploit Bayes Theorem to build a Naive Bayes classifier. Understand the 'naive' assumption of conditional independence and train your AI to classify spam messages instantly.",
    19: "Learning by splitting data. Build an interactive Decision Tree. Calculate Entropy and Information Gain to determine the most important features, and learn how to prune your tree to prevent it from memorizing the data.",
    20: "Learning by trial and error. Your agent is placed in an unknown grid-world. Implement Q-Learning and Temporal-Difference updates to watch a Reinforcement Learning agent discover the optimal policy through exploration.",
    21: "Step back into the history of AI. Explore the declarative nature of PROLOG and LISP. Learn how symbolic reasoning and recursion defined the first wave of artificial intelligence research.",
    22: "Capture human expertise in a box. Build the architecture of a classical Expert System (like MYCIN). Combine a knowledge base with an inference engine to diagnose complex domain-specific problems.",
    23: "Stop writing isolated algorithms. You are now the Intelligence Architect. Analyze real-world engineering scenarios and justify your selection of agent architectures, search methods, and learning models.",
    24: "The Ultimate Test. NEXUS requires you to deploy a fully autonomous rescue system. Integrate perception, state spaces, A* search, probabilistic reasoning, and decision theory into a single, cohesive Capstone architecture."
}

for s in STORIES:
    if s["id"] in new_hooks:
        s["hook"] = new_hooks[s["id"]]

with open("story_data.py", "w", encoding="utf-8") as f:
    f.write("STORIES = \\\n")
    json.dump(STORIES, f, indent=4, ensure_ascii=False)

