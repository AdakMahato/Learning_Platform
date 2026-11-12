 CONTENT_08_15 = {
    "8": {
        "title": "The Knowledge Vault",
        "description": "Ontologies and Knowledge Graphs",
        "episodes": [
            {
                "title": "Episode 1: Structuring the World",
                "blocks": [
                    {
                        "type": "objective",
                        "content": "Understand how AI organizes information using Ontologies and Knowledge Graphs."
                    },
                    {
                        "type": "markdown",
                        "content": "To reason about the world, an AI must first represent it. A **Knowledge Graph (KG)** is a network of real-world entities (objects, events, situations, or concepts) and illustrates the relationship between them. This information is usually stored in triples: (Subject, Predicate, Object)."
                    },
                    {
                        "type": "visual",
                        "content": "graph LR\n  A[Alice] -- is_friend_of --> B[Bob]\n  B -- works_at --> C[OpenAI]\n  A -- interested_in --> D[AI]"
                    },
                    {
                        "type": "code_lab",
                        "title": "Building a Simple Knowledge Graph",
                        "instructions": "Write a function `query_graph(graph, subject, predicate)` that returns all objects associated with a subject and predicate in a given graph. The graph is represented as a list of tuples.",
                        "starter_code": "def query_graph(graph, subject, predicate):\n    # TODO: return a list of objects\n    pass",
                        "solution_code": "def query_graph(graph, subject, predicate):\n    return [obj for sub, pred, obj in graph if sub == subject and pred == predicate]",
                        "expected_output": "['Bob']",
                        "explanation": "By iterating through the triples, we filter those that match the given subject and predicate.",
                        "test_cases": [
                            {
                                "input": "([('Alice', 'friend', 'Bob'), ('Alice', 'friend', 'Charlie'), ('Bob', 'works', 'Tech')], 'Alice', 'friend')",
                                "expected": "['Bob', 'Charlie']"
                            }
                        ]
                    }
                ]
            }
        ]
    },
    "9": {
        "title": "The Logic Engine",
        "description": "Propositional & First-Order Logic",
        "episodes": [
            {
                "title": "Episode 1: The Foundations of Logic",
                "blocks": [
                    {
                        "type": "objective",
                        "content": "Learn how AI uses propositional logic to deduce new facts."
                    },
                    {
                        "type": "concept",
                        "content": "**Propositional Logic** uses propositions (statements that are either true or false) and logical connectives (AND, OR, NOT, IMPLIES) to form complex sentences. Modus Ponens is a basic rule of inference: If P implies Q, and P is true, then Q is true."
                    },
                    {
                        "type": "code_lab",
                        "title": "Modus Ponens Engine",
                        "instructions": "Write a function `apply_modus_ponens(rules, facts)` where rules is a dictionary `{P: Q}` meaning 'P implies Q', and facts is a set of known true propositions. The function should return a new set of facts derived by applying Modus Ponens once.",
                        "starter_code": "def apply_modus_ponens(rules, facts):\n    new_facts = set(facts)\n    # TODO: apply rules\n    return new_facts",
                        "solution_code": "def apply_modus_ponens(rules, facts):\n    new_facts = set(facts)\n    for p, q in rules.items():\n        if p in facts:\n            new_facts.add(q)\n    return new_facts",
                        "expected_output": "{'Raining', 'WetGrass'}",
                        "explanation": "If 'Raining' is a fact, and 'Raining' implies 'WetGrass' is in our rules, we can add 'WetGrass' to our facts.",
                        "test_cases": [
                            {
                                "input": "({'A': 'B', 'B': 'C'}, {'A'})",
                                "expected": "{'A', 'B'}"
                            }
                        ]
                    }
                ]
            }
        ]
    },
    "10": {
        "title": "The Machine That Could Reason",
        "description": "Situation Calculus",
        "episodes": [
            {
                "title": "Episode 1: Time and Actions",
                "blocks": [
                    {
                        "type": "objective",
                        "content": "Understand how situation calculus models a changing world."
                    },
                    {
                        "type": "markdown",
                        "content": "**Situation Calculus** is a logic formalism designed for representing and reasoning about dynamic domains. It uses 'Fluents' (properties that change over time) and 'Actions' (events that transition the world from one situation to another). A major challenge here is the **Frame Problem**: specifying what *does not* change when an action occurs."
                    },
                    {
                        "type": "code_lab",
                        "title": "State Transition",
                        "instructions": "Write a function `apply_action(state, action_effects)` that takes a current state (dictionary of fluents) and action_effects (dictionary of changes). It should return a new state.",
                        "starter_code": "def apply_action(state, action_effects):\n    # TODO: return updated state\n    pass",
                        "solution_code": "def apply_action(state, action_effects):\n    new_state = state.copy()\n    new_state.update(action_effects)\n    return new_state",
                        "expected_output": "{'door_open': True, 'light_on': True}",
                        "explanation": "The frame problem is solved simply here by copying the state (inertia) and only overriding the explicit effects of the action.",
                        "test_cases": [
                            {
                                "input": "({'loc': 'roomA', 'has_key': False}, {'has_key': True})",
                                "expected": "{'loc': 'roomA', 'has_key': True}"
                            }
                        ]
                    }
                ]
            }
        ]
    },
    "11": {
        "title": "The Planner",
        "description": "Action Representation and Planning Graphs",
        "episodes": [
            {
                "title": "Episode 1: STRIPS Planning",
                "blocks": [
                    {
                        "type": "objective",
                        "content": "Learn how AI creates sequences of actions to achieve goals."
                    },
                    {
                        "type": "concept",
                        "content": "In STRIPS (Stanford Research Institute Problem Solver), an action is defined by **Preconditions** (what must be true to execute it) and **Effects** (what becomes true/false afterward). Planning is finding a path from an initial state to a goal state."
                    },
                    {
                        "type": "code_lab",
                        "title": "Checking Preconditions",
                        "instructions": "Write a function `can_execute(state, preconditions)` that returns True if all preconditions (a set of strings) are present in the current state (a set of strings).",
                        "starter_code": "def can_execute(state, preconditions):\n    # TODO: check if preconditions are met\n    pass",
                        "solution_code": "def can_execute(state, preconditions):\n    return preconditions.issubset(state)",
                        "expected_output": "True",
                        "explanation": "The action can only be executed if the current state satisfies all required preconditions.",
                        "test_cases": [
                            {
                                "input": "({'At(Home)', 'Have(Car)'}, {'At(Home)', 'Have(Keys)'})",
                                "expected": "False"
                            }
                        ]
                    }
                ]
            }
        ]
    },
    "12": {
        "title": "The World That Keeps Changing",
        "description": "Uncertainty and Randomness",
        "episodes": [
            {
                "title": "Episode 1: Embracing the Unknown",
                "blocks": [
                    {
                        "type": "objective",
                        "content": "Model uncertainty using probability distributions."
                    },
                    {
                        "type": "markdown",
                        "content": "Real-world environments are rarely deterministic. Sensors are noisy, and actions can fail. AI uses probability theory to quantify this uncertainty. A probability distribution assigns a probability (between 0 and 1) to every possible outcome of a random variable, and all probabilities must sum to 1."
                    },
                    {
                        "type": "code_lab",
                        "title": "Normalizing Distributions",
                        "instructions": "Write a function `normalize(distribution)` that takes a dictionary of raw counts/weights and returns a valid probability distribution where values sum to 1.",
                        "starter_code": "def normalize(distribution):\n    # TODO: return normalized dictionary\n    pass",
                        "solution_code": "def normalize(distribution):\n    total = sum(distribution.values())\n    return {k: v / total for k, v in distribution.items()}",
                        "expected_output": "{'A': 0.2, 'B': 0.8}",
                        "explanation": "Dividing each weight by the total sum ensures that the resulting probabilities add up to 1.0.",
                        "test_cases": [
                            {
                                "input": "({'sun': 3, 'rain': 1})",
                                "expected": "{'sun': 0.75, 'rain': 0.25}"
                            }
                        ]
                    }
                ]
            }
        ]
    },
    "13": {
        "title": "The Probability Problem",
        "description": "Independence and Bayes Rule",
        "episodes": [
            {
                "title": "Episode 1: Updating Beliefs",
                "blocks": [
                    {
                        "type": "objective",
                        "content": "Learn how Bayes' Rule allows AI to update its beliefs given new evidence."
                    },
                    {
                        "type": "concept",
                        "content": "**Bayes' Rule** is the cornerstone of probabilistic reasoning. It provides a way to calculate the probability of a hypothesis given evidence: P(H|E) = (P(E|H) * P(H)) / P(E). P(H) is the prior, P(E|H) is the likelihood, and P(H|E) is the posterior."
                    },
                    {
                        "type": "code_lab",
                        "title": "Bayesian Updater",
                        "instructions": "Write a function `bayes_rule(prior_H, prob_E_given_H, prob_E_given_not_H)` to calculate P(H|E). Note: P(E) = P(E|H)*P(H) + P(E|~H)*P(~H).",
                        "starter_code": "def bayes_rule(prior_H, prob_E_given_H, prob_E_given_not_H):\n    # TODO: compute posterior\n    pass",
                        "solution_code": "def bayes_rule(prior_H, prob_E_given_H, prob_E_given_not_H):\n    prior_not_H = 1.0 - prior_H\n    prob_E = (prob_E_given_H * prior_H) + (prob_E_given_not_H * prior_not_H)\n    return (prob_E_given_H * prior_H) / prob_E",
                        "expected_output": "0.8",
                        "explanation": "We first calculate the total probability of the evidence P(E) using the law of total probability, then apply Bayes' rule.",
                        "test_cases": [
                            {
                                "input": "(0.01, 0.9, 0.1)",
                                "expected": "0.08333333333333334"
                            }
                        ]
                    }
                ]
            }
        ]
    },
    "14": {
        "title": "The Bayesian Detective",
        "description": "Bayesian Networks and Inference",
        "episodes": [
            {
                "title": "Episode 1: Networks of Belief",
                "blocks": [
                    {
                        "type": "objective",
                        "content": "Understand how Bayesian Networks compactly represent joint probability distributions."
                    },
                    {
                        "type": "markdown",
                        "content": "A **Bayesian Network** is a directed acyclic graph (DAG) where nodes represent random variables and edges represent conditional dependencies. It simplifies probability calculations by exploiting conditional independence. The joint probability is the product of individual conditional probabilities: P(x_1, ..., x_n) = Product P(x_i | Parents(x_i))."
                    },
                    {
                        "type": "visual",
                        "content": "graph LR\n  Burglary --> Alarm\n  Earthquake --> Alarm\n  Alarm --> JohnCalls\n  Alarm --> MaryCalls"
                    },
                    {
                        "type": "code_lab",
                        "title": "Joint Probability Calculation",
                        "instructions": "Write a function `joint_prob(network, assignment)` where network is a dict mapping node names to their computed P(node | parents) for the given assignment. Return the overall joint probability.",
                        "starter_code": "def joint_prob(network_probs):\n    # TODO: return product of all probabilities\n    pass",
                        "solution_code": "def joint_prob(network_probs):\n    prob = 1.0\n    for p in network_probs.values():\n        prob *= p\n    return prob",
                        "expected_output": "0.0001",
                        "explanation": "Because of the chain rule for Bayesian Networks, the joint probability is simply the product of the local conditional probabilities.",
                        "test_cases": [
                            {
                                "input": "({'B': 0.001, 'E': 0.998, 'A_given_B_E': 0.94})",
                                "expected": "0.0009381200000000001"
                            }
                        ]
                    }
                ]
            }
        ]
    },
    "15": {
        "title": "The Decision Maker",
        "description": "Utility Theory and Decision Theory",
        "episodes": [
            {
                "title": "Episode 1: Maximizing Expected Utility",
                "blocks": [
                    {
                        "type": "objective",
                        "content": "Learn how AI makes optimal decisions under uncertainty."
                    },
                    {
                        "type": "concept",
                        "content": "**Decision Theory = Probability Theory + Utility Theory**. An AI agent must not only know the probabilities of outcomes, but also how desirable those outcomes are (their Utility). The Principle of Maximum Expected Utility (MEU) states that a rational agent should choose the action that maximizes its expected utility."
                    },
                    {
                        "type": "code_lab",
                        "title": "Expected Utility Calculator",
                        "instructions": "Write a function `expected_utility(outcomes)` where outcomes is a list of tuples `(probability, utility)`. Return the total expected utility.",
                        "starter_code": "def expected_utility(outcomes):\n    # TODO: calculate expected utility\n    pass",
                        "solution_code": "def expected_utility(outcomes):\n    return sum(prob * util for prob, util in outcomes)",
                        "expected_output": "45.0",
                        "explanation": "Expected utility is the sum of the utility of each outcome weighted by its probability.",
                        "test_cases": [
                            {
                                "input": "([(0.2, 100), (0.8, -10)])",
                                "expected": "12.0"
                            }
                        ]
                    }
                ]
            }
        ]
    }
}
