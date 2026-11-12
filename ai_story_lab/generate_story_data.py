import json

titles = [
    ("The Machine That Couldn't Think", "🧠", "What is AI?", "AI Foundations"),
    ("The Agent Awakens", "🤖", "How does a machine interact with the world?", "Agents & PEAS"),
    ("The World Inside the Machine", "🌐", "How do we represent problems?", "State Spaces"),
    ("The Maze Without a Map", "🗺️", "How to search without a guide.", "Uninformed Search"),
    ("The Search for the Better Path", "🧭", "Adding intelligence to search.", "Heuristic Search"),
    ("The Heuristic Detective", "🕵️", "Proving a heuristic is perfect.", "Deep A* & AO*"),
    ("The Game of Minds", "⚔️", "How to play a perfect game.", "Adversarial Search"),
    ("The Impossible Puzzle", "🧩", "Solving constraint problems.", "CSP"),
    ("The Knowledge Vault", "🗄️", "How a machine remembers facts.", "Knowledge Representation"),
    ("The Logic Engine", "⚙️", "How a machine proves truth.", "First-Order Logic"),
    ("The Machine That Could Reason", "⚖️", "Reasoning about action and time.", "Advanced Logic"),
    ("The Planner", "📋", "How to achieve a sequence of goals.", "Planning"),
    ("The World That Keeps Changing", "🎲", "Dealing with uncertainty.", "Probability Basics"),
    ("The Probability Problem", "📊", "Calculating the odds.", "Bayes Theorem"),
    ("The Bayesian Detective", "🕸️", "Inference over networks.", "Bayesian Networks"),
    ("The Decision Maker", "⚖️", "Choosing the best action under risk.", "Decision Theory"),
    ("The Machine That Learns", "🌱", "How to learn from data.", "Machine Learning"),
    ("The Nearest Neighbor", "📍", "Learning by similarity.", "KNN"),
    ("The Naive Assumption", "✉️", "Learning by probability.", "Naive Bayes"),
    ("The Tree That Makes Decisions", "🌳", "Learning by splitting data.", "Decision Trees"),
    ("The Agent That Learns From Failure", "🕹️", "Learning by trial and error.", "Reinforcement Learning"),
    ("The Logic Programmer", "📜", "The languages of old AI.", "PROLOG & LISP"),
    ("The Expert in the Box", "🧰", "Capturing human expertise.", "Expert Systems"),
    ("The Intelligence Architect", "🏗️", "Designing a complete system.", "System Architecture"),
    ("The Final AI", "🚀", "Deploying the ultimate agent.", "NEXUS Capstone")
]

stories = []
for i, (title, icon, hook, primary) in enumerate(titles):
    stories.append({
        "id": i,
        "title": title,
        "icon": icon,
        "genre": "Artificial Intelligence",
        "difficulty": "Beginner" if i < 5 else "Intermediate" if i < 20 else "Advanced",
        "hook": hook,
        "primary": primary
    })

with open("story_data.py", "w", encoding="utf-8") as f:
    f.write("STORIES = \\\n")
    json.dump(stories, f, indent=4, ensure_ascii=False)

