CONTENT_12_16 = {
    "12": {
        "title": "Case 12: Uncertainty in AI",
        "modules": [
            {
                "title": "Module 1: Embracing the Unknown",
                "episodes": [
                    {"type": "markdown", "content": "# The AI in the Fog\nImagine driving in thick fog. You can't see the cars ahead perfectly, but you know they are there. AI systems operate in a similar 'fog' of uncertainty."},
                    {"type": "concept", "title": "Types of Uncertainty", "content": "Aleatoric uncertainty (inherent randomness) vs Epistemic uncertainty (lack of knowledge)."},
                    {"type": "visual", "content": "graph TD\n  A[\"Uncertainty\"] --> B[\"Aleatoric (Randomness)\"]\n  A --> C[\"Epistemic (Ignorance)\"]"},
                    {"type": "markdown", "content": "Aleatoric uncertainty is like flipping a coin. No matter how much data you gather, the outcome is random."},
                    {"type": "concept", "title": "Probability as Logic", "content": "Probability theory provides a rigorous framework for reasoning under uncertainty, extending classical Boolean logic."},
                    {"type": "interactive", "question": "Which type of uncertainty can be reduced by collecting more data?", "options": ["Epistemic", "Aleatoric", "Both"], "answer": "Epistemic"},
                    {"type": "markdown", "content": "In AI, we often use probability distributions to represent our beliefs about the state of the world."},
                    {"type": "visual_stepper", "content": "graph LR\n  A[\"Belief State\"] --> B[\"Observation\"]\n  B --> C[\"Updated Belief\"]\n  style A fill:#10b9811a\n  style C fill:#10b9811a"},
                    {"type": "code_lab", "language": "python", "content": "def update_belief(prior, evidence):\n    # A placeholder for belief updating logic\n    return prior * evidence"},
                    {"type": "markdown", "content": "We've laid the groundwork for reasoning in uncertain environments."}
                ]
            },
            {
                "title": "Module 2: Random Variables and Distributions",
                "episodes": [
                    {"type": "markdown", "content": "## Random Variables\nA random variable assigns a numerical value to each outcome in a sample space."},
                    {"type": "concept", "title": "Discrete vs Continuous", "content": "Random variables can be discrete (like dice rolls) or continuous (like temperature)."},
                    {"type": "visual", "content": "graph TD\n  RV[\"Random Variable X\"] --> D[\"Discrete (e.g., Coin)\"]\n  RV --> C[\"Continuous (e.g., Temp)\"]"},
                    {"type": "markdown", "content": "The Probability Mass Function (PMF) maps discrete outcomes to probabilities."},
                    {"type": "interactive", "question": "What is the sum of all probabilities in a valid PMF?", "options": ["0", "1", "Infinity", "0.5"], "answer": "1"},
                    {"type": "concept", "title": "Probability Density Function", "content": "For continuous variables, we use the PDF. The probability of an exact value is zero; we measure areas under the curve."},
                    {"type": "code_lab", "language": "python", "content": "import scipy.stats as stats\n# Standard normal PDF\npdf_value = stats.norm.pdf(0)\nprint(f'PDF at x=0: {pdf_value}')"},
                    {"type": "markdown", "content": "Expectation and Variance are key summaries of a distribution."},
                    {"type": "visual_stepper", "content": "graph LR\n  A[\"Distribution\"] --> B[\"Mean (Center)\"]\n  A --> C[\"Variance (Spread)\"]"},
                    {"type": "markdown", "content": "Understanding these forms the basis of statistical AI."}
                ]
            },
            {
                "title": "Module 3: Joint and Marginal Probabilities",
                "episodes": [
                    {"type": "markdown", "content": "## Multiple Variables\nReal-world problems involve many interacting variables. We need joint probabilities."},
                    {"type": "concept", "title": "Joint Probability", "content": "P(X, Y) is the probability that X and Y happen together."},
                    {"type": "visual", "content": "graph TD\n  A[\"Weather\"] --> C[\"Joint: P(Weather, Traffic)\"]\n  B[\"Traffic\"] --> C"},
                    {"type": "markdown", "content": "Marginalization is the process of extracting the distribution of a single variable from a joint distribution."},
                    {"type": "interactive", "question": "How do we get P(X) from P(X, Y) for discrete variables?", "options": ["Sum over Y", "Multiply by Y", "Divide by P(Y)"], "answer": "Sum over Y"},
                    {"type": "concept", "title": "Conditional Probability", "content": "P(X|Y) = P(X, Y) / P(Y). This is the foundation of inference."},
                    {"type": "code_lab", "language": "python", "content": "p_x_and_y = 0.1\np_y = 0.5\np_x_given_y = p_x_and_y / p_y\nprint(p_x_given_y)"},
                    {"type": "markdown", "content": "Independence means P(X,Y) = P(X)P(Y). Learning X gives no info about Y."},
                    {"type": "visual_stepper", "content": "graph LR\n  A[\"Independent\"] --> B[\"P(X|Y) = P(X)\"]\n  C[\"Dependent\"] --> D[\"P(X|Y) != P(X)\"]"},
                    {"type": "markdown", "content": "Conditional independence is a crucial concept for scaling up probabilistic models."}
                ]
            },
            {
                "title": "Module 4: Applications of Probability in AI",
                "episodes": [
                    {"type": "markdown", "content": "## Where do we use this?\nFrom robotics to natural language, probability is everywhere."},
                    {"type": "concept", "title": "Sensor Fusion", "content": "Combining multiple uncertain sensor readings to get a robust estimate."},
                    {"type": "visual", "content": "graph TD\n  A[\"Camera\"] --> C[\"State Estimate\"]\n  B[\"LiDAR\"] --> C\n  style C fill:#4285f41a"},
                    {"type": "markdown", "content": "Language models use probabilities to predict the next word."},
                    {"type": "interactive", "question": "What does an AI use to represent its belief about an object's location?", "options": ["A boolean flag", "A probability distribution", "A static constant"], "answer": "A probability distribution"},
                    {"type": "concept", "title": "Decision Making", "content": "Probabilities combine with utilities to make optimal decisions (Expected Utility)."},
                    {"type": "code_lab", "language": "python", "content": "def expected_utility(prob, utility):\n    return sum(p * u for p, u in zip(prob, utility))"},
                    {"type": "markdown", "content": "Medical diagnosis systems use probability to infer disease given symptoms."},
                    {"type": "visual_stepper", "content": "graph LR\n  A[\"Symptoms\"] --> B[\"Probabilistic Engine\"]\n  B --> C[\"Diagnosis Belief\"]"},
                    {"type": "markdown", "content": "You are now ready to dive deep into Bayes Rule."}
                ]
            }
        ]
    },
    "13": {
        "title": "Case 13: Bayes Rule in Action",
        "modules": [
            {
                "title": "Module 1: The Anatomy of Bayes Theorem",
                "episodes": [
                    {"type": "markdown", "content": "# The Reverend's Rule\nThomas Bayes gave us a mathematical way to update beliefs based on new evidence."},
                    {"type": "concept", "title": "Bayes Theorem", "content": "P(H|E) = P(E|H) * P(H) / P(E). Hypothesis H, Evidence E."},
                    {"type": "visual", "content": "graph LR\n  A[\"Prior: P(H)\"] --> C[\"Posterior: P(H|E)\"]\n  B[\"Likelihood: P(E|H)\"] --> C"},
                    {"type": "markdown", "content": "The Prior is what you believe before seeing the data."},
                    {"type": "interactive", "question": "In Bayes Theorem, what represents the probability of the data given the hypothesis?", "options": ["Prior", "Posterior", "Likelihood", "Marginal"], "answer": "Likelihood"},
                    {"type": "concept", "title": "The Denominator", "content": "P(E) is the evidence or marginal likelihood. It normalizes the posterior."},
                    {"type": "code_lab", "language": "python", "content": "def bayes(prior, likelihood, marginal):\n    return (likelihood * prior) / marginal"},
                    {"type": "markdown", "content": "Understanding each term is critical for building Bayesian agents."},
                    {"type": "visual_stepper", "content": "graph TD\n  A[\"Hypothesis\"] --> B[\"Generate Evidence\"]\n  C[\"Actual Evidence\"] --> D[\"Compare & Update\"]"},
                    {"type": "markdown", "content": "Next, we'll apply this to a classic medical testing scenario."}
                ]
            },
            {
                "title": "Module 2: The Base Rate Fallacy",
                "episodes": [
                    {"type": "markdown", "content": "## Medical Diagnosis\nImagine a disease affects 1% of the population. A test is 99% accurate."},
                    {"type": "concept", "title": "Base Rates", "content": "The base rate is the prior probability (1%). Ignoring it leads to the Base Rate Fallacy."},
                    {"type": "visual", "content": "graph TD\n  A[\"Disease P(D)=0.01\"] --> B[\"Test Positive P(+|D)=0.99\"]\n  C[\"Healthy P(~D)=0.99\"] --> D[\"Test Positive P(+|~D)=0.01\"]"},
                    {"type": "markdown", "content": "If you test positive, what's the chance you actually have the disease? It's not 99%!"},
                    {"type": "interactive", "question": "Why is the posterior probability much lower than 99%?", "options": ["The test is faulty", "The base rate (prior) is very low", "Math error"], "answer": "The base rate (prior) is very low"},
                    {"type": "concept", "title": "Calculating the Posterior", "content": "P(D|+) = P(+|D)P(D) / (P(+|D)P(D) + P(+|~D)P(~D)) = 50%."},
                    {"type": "code_lab", "language": "python", "content": "prior = 0.01\nlikelihood = 0.99\nfalse_positive = 0.01\nmarginal = (likelihood * prior) + (false_positive * (1 - prior))\nposterior = (likelihood * prior) / marginal\nprint(posterior)"},
                    {"type": "markdown", "content": "This counterintuitive result shows why formal probabilistic reasoning is necessary."},
                    {"type": "visual_stepper", "content": "graph LR\n  A[\"Rare Disease\"] --> B[\"Many False Positives\"]\n  B --> C[\"Low Posterior Confidence\"]"},
                    {"type": "markdown", "content": "AI systems must inherently incorporate base rates to avoid this trap."}
                ]
            },
            {
                "title": "Module 3: Bayesian Filtering",
                "episodes": [
                    {"type": "markdown", "content": "## Tracking State Over Time\nHow does a self-driving car track a pedestrian over time? Bayesian filtering."},
                    {"type": "concept", "title": "Recursive State Estimation", "content": "We continuously apply Bayes rule. Today's posterior becomes tomorrow's prior."},
                    {"type": "visual", "content": "graph LR\n  A[\"Belief(t)\"] --> B[\"Action/Time Update\"]\n  B --> C[\"Belief(t+1)\"]\n  D[\"Observation\"] --> C"},
                    {"type": "markdown", "content": "There are two steps: Predict (time update) and Update (measurement update)."},
                    {"type": "interactive", "question": "In recursive filtering, what happens to the posterior after a measurement update?", "options": ["It is discarded", "It becomes the new prior for the next step", "It is multiplied by zero"], "answer": "It becomes the new prior for the next step"},
                    {"type": "concept", "title": "Kalman Filters", "content": "A Kalman filter is an optimal Bayesian filter for linear Gaussian systems."},
                    {"type": "code_lab", "language": "python", "content": "class SimpleFilter:\n    def update(self, prior, likelihood):\n        # Returns unnormalized posterior\n        return prior * likelihood"},
                    {"type": "markdown", "content": "Filtering allows AI to maintain a persistent model of the world."},
                    {"type": "visual_stepper", "content": "graph TD\n  A[\"Predict State\"] --> B[\"Incorporate Measurement\"]\n  B --> A"},
                    {"type": "markdown", "content": "This is fundamental to modern robotics and navigation."}
                ]
            },
            {
                "title": "Module 4: Naive Bayes Classification",
                "episodes": [
                    {"type": "markdown", "content": "## Spam or Ham?\nThe Naive Bayes algorithm is a simple yet powerful classifier."},
                    {"type": "concept", "title": "The Naive Assumption", "content": "It assumes that all features are conditionally independent given the class."},
                    {"type": "visual", "content": "graph TD\n  A[\"Class (Spam)\"] --> B[\"Word: Viagra\"]\n  A --> C[\"Word: Prince\"]\n  A --> D[\"Word: Free\"]"},
                    {"type": "markdown", "content": "Despite this strong (and usually false) assumption, it works remarkably well."},
                    {"type": "interactive", "question": "What is 'naive' about the Naive Bayes algorithm?", "options": ["It uses simple math", "It ignores priors", "It assumes conditional independence of features"], "answer": "It assumes conditional independence of features"},
                    {"type": "concept", "title": "Log Probabilities", "content": "Multiplying many small probabilities leads to underflow. We add log probabilities instead."},
                    {"type": "code_lab", "language": "python", "content": "import math\ndef log_prob(p_prior, p_features):\n    return math.log(p_prior) + sum(math.log(p) for p in p_features)"},
                    {"type": "markdown", "content": "Naive Bayes is often used as a baseline for text classification tasks."},
                    {"type": "visual_stepper", "content": "graph LR\n  A[\"Input Text\"] --> B[\"Extract Words\"]\n  B --> C[\"Calculate Log Posteriors\"]\n  C --> D[\"Argmax Class\"]"},
                    {"type": "markdown", "content": "Next, we will look at more complex graphical models: Bayesian Networks."}
                ]
            }
        ]
    },
    "14": {
        "title": "Case 14: Bayesian Networks",
        "modules": [
            {
                "title": "Module 1: Graphs and Probabilities",
                "episodes": [
                    {"type": "markdown", "content": "# Unspaghettifying Probabilities\nSpecifying a full joint distribution is intractable. Enter Bayesian Networks."},
                    {"type": "concept", "title": "Directed Acyclic Graphs (DAGs)", "content": "Bayesian Networks use DAGs to compactly represent joint distributions."},
                    {"type": "visual", "content": "graph TD\n  A[\"Burglary\"] --> C[\"Alarm\"]\n  B[\"Earthquake\"] --> C\n  C --> D[\"JohnCalls\"]"},
                    {"type": "markdown", "content": "Nodes represent random variables, and edges represent direct probabilistic influence."},
                    {"type": "interactive", "question": "Can a Bayesian Network graph contain cycles (loops)?", "options": ["Yes", "No", "Only if variables are discrete"], "answer": "No"},
                    {"type": "concept", "title": "The Chain Rule for Bayes Nets", "content": "P(X1..Xn) = Product of P(Xi | Parents(Xi)). This drastically reduces parameters."},
                    {"type": "code_lab", "language": "python", "content": "def joint_prob(p_b, p_e, p_a_given_be):\n    return p_b * p_e * p_a_given_be"},
                    {"type": "markdown", "content": "By leveraging conditional independence, we tame complexity."},
                    {"type": "visual_stepper", "content": "graph LR\n  A[\"Full Joint (2^N)\"] --> B[\"Factorization via C.I.\"]\n  B --> C[\"Compact Representation\"]"},
                    {"type": "markdown", "content": "This makes reasoning in complex domains computationally feasible."}
                ]
            },
            {
                "title": "Module 2: Conditional Independence in Graphs",
                "episodes": [
                    {"type": "markdown", "content": "## D-Separation\nHow do we read conditional independencies directly from the graph structure?"},
                    {"type": "concept", "title": "The Three Patterns", "content": "Causal chain (A->B->C), Common cause (A<-B->C), and Common effect (A->B<-C)."},
                    {"type": "visual", "content": "graph TD\n  A[\"X\"] --> B[\"Y\"]\n  B --> C[\"Z\"]\n  style B fill:#e11d481a"},
                    {"type": "markdown", "content": "In a causal chain, observing the middle node blocks the flow of information."},
                    {"type": "interactive", "question": "In the common effect (V-structure) A->B<-C, are A and C independent BEFORE observing B?", "options": ["Yes", "No"], "answer": "Yes"},
                    {"type": "concept", "title": "Explaining Away", "content": "In A->B<-C, observing B makes A and C dependent. This is called the 'explaining away' effect."},
                    {"type": "code_lab", "language": "python", "content": "# Conceptual check: explaining away\ndef is_d_separated(path, observed_nodes):\n    # Simplified logic placeholder\n    return True"},
                    {"type": "markdown", "content": "D-separation gives us a complete algorithmic way to find independencies."},
                    {"type": "visual_stepper", "content": "graph LR\n  A[\"Graph Structure\"] --> B[\"D-Separation Rules\"]\n  B --> C[\"Independence Guarantees\"]"},
                    {"type": "markdown", "content": "These guarantees allow us to optimize inference algorithms."}
                ]
            },
            {
                "title": "Module 3: Exact Inference",
                "episodes": [
                    {"type": "markdown", "content": "## Calculating Posteriors\nGiven some observed evidence, how do we compute the posterior of query variables?"},
                    {"type": "concept", "title": "Inference by Enumeration", "content": "Sum over all hidden variables in the joint distribution. Simple but slow (exponential time)."},
                    {"type": "visual", "content": "graph TD\n  A[\"Query\"] --> B[\"Joint Dist\"]\n  B --> C[\"Sum out Hidden\"]\n  C --> D[\"Normalize\"]"},
                    {"type": "markdown", "content": "Variable Elimination is a faster exact inference algorithm."},
                    {"type": "interactive", "question": "What is the main computational problem with inference by enumeration?", "options": ["It is inaccurate", "It takes exponential time", "It only works for continuous variables"], "answer": "It takes exponential time"},
                    {"type": "concept", "title": "Variable Elimination", "content": "We push sums inward, interleaving multiplication and marginalization to avoid building the full joint table."},
                    {"type": "code_lab", "language": "python", "content": "def eliminate_variable(factor_list, variable):\n    # Multiply relevant factors and sum out the variable\n    pass"},
                    {"type": "markdown", "content": "The order in which we eliminate variables drastically affects computation time."},
                    {"type": "visual_stepper", "content": "graph LR\n  A[\"Factors\"] --> B[\"Multiply\"] --> C[\"Sum Out\"] --> D[\"New Factor\"]"},
                    {"type": "markdown", "content": "However, even variable elimination is NP-hard in the worst case."}
                ]
            },
            {
                "title": "Module 4: Approximate Inference",
                "episodes": [
                    {"type": "markdown", "content": "## When Exact is Too Slow\nFor huge networks, exact inference is impossible. We use sampling instead."},
                    {"type": "concept", "title": "Monte Carlo Methods", "content": "We generate random samples from the network and count frequencies to estimate probabilities."},
                    {"type": "visual", "content": "graph TD\n  A[\"Bayesian Network\"] --> B[\"Generate Samples\"]\n  B --> C[\"Estimate Posterior\"]"},
                    {"type": "markdown", "content": "Prior Sampling generates samples from the prior, but wastes time if evidence is rare."},
                    {"type": "interactive", "question": "Why is Rejection Sampling inefficient for rare evidence?", "options": ["It generates too many accepted samples", "It rejects almost all samples", "It biases the results"], "answer": "It rejects almost all samples"},
                    {"type": "concept", "title": "Gibbs Sampling", "content": "A Markov Chain Monte Carlo (MCMC) method. We resample one variable at a time, conditioned on the rest."},
                    {"type": "code_lab", "language": "python", "content": "import random\ndef gibbs_step(current_state, markov_blanket):\n    # Sample node given its blanket\n    return random.choice([True, False])"},
                    {"type": "markdown", "content": "Gibbs sampling guarantees that eventually, samples are drawn from the true posterior."},
                    {"type": "visual_stepper", "content": "graph LR\n  A[\"Initialize State\"] --> B[\"Sample Node 1\"]\n  B --> C[\"Sample Node 2\"] --> D[\"Repeat\"]"},
                    {"type": "markdown", "content": "These sampling methods are ubiquitous in modern probabilistic AI."}
                ]
            }
        ]
    },
    "15": {
        "title": "Case 15: Utility Theory and Decisions",
        "modules": [
            {
                "title": "Module 1: The Concept of Utility",
                "episodes": [
                    {"type": "markdown", "content": "# Beyond Probabilities\nKnowing what will happen isn't enough. An agent needs to know what it WANTS."},
                    {"type": "concept", "title": "Utility Functions", "content": "A utility function maps a state to a real number, representing its desirability."},
                    {"type": "visual", "content": "graph TD\n  A[\"State: Win Lottery\"] --> B[\"Utility: 1000\"]\n  C[\"State: Lose Money\"] --> D[\"Utility: -100\"]"},
                    {"type": "markdown", "content": "Rational agents act to maximize their expected utility."},
                    {"type": "interactive", "question": "What does a utility function output?", "options": ["A probability", "A real number representing desirability", "A boolean action"], "answer": "A real number representing desirability"},
                    {"type": "concept", "title": "Expected Utility", "content": "EU(Action) = Sum over outcomes ( Probability(Outcome | Action) * Utility(Outcome) )."},
                    {"type": "code_lab", "language": "python", "content": "def calculate_eu(probabilities, utilities):\n    return sum(p * u for p, u in zip(probabilities, utilities))"},
                    {"type": "markdown", "content": "The Maximum Expected Utility (MEU) principle is the core of rational decision making."},
                    {"type": "visual_stepper", "content": "graph LR\n  A[\"Action Options\"] --> B[\"Evaluate EU\"]\n  B --> C[\"Select Max EU\"]"},
                    {"type": "markdown", "content": "This unites probability (belief) and utility (desire) into action."}
                ]
            },
            {
                "title": "Module 2: Risk and Rationality",
                "episodes": [
                    {"type": "markdown", "content": "## Are you risk-averse?\nUtility is not the same as money. The utility of money is non-linear."},
                    {"type": "concept", "title": "Risk Aversion", "content": "Most people prefer a guaranteed $50 over a 50% chance of $100. This implies a concave utility curve."},
                    {"type": "visual", "content": "graph TD\n  A[\"Wealth\"] --> B[\"Logarithmic Utility Curve\"]\n  style B fill:#eab3081a"},
                    {"type": "markdown", "content": "A risk-seeking agent has a convex utility curve; a risk-neutral agent has a linear one."},
                    {"type": "interactive", "question": "If an agent strictly maximizes expected monetary value, what is its risk attitude?", "options": ["Risk-averse", "Risk-neutral", "Risk-seeking"], "answer": "Risk-neutral"},
                    {"type": "concept", "title": "The St. Petersburg Paradox", "content": "A game with infinite expected monetary value, but people won't pay much to play it. Proves utility != money."},
                    {"type": "code_lab", "language": "python", "content": "import math\ndef utility_of_money(amount):\n    return math.log(amount + 1) # Risk averse"},
                    {"type": "markdown", "content": "Designing the right utility function is crucial for AI alignment."},
                    {"type": "visual_stepper", "content": "graph LR\n  A[\"Agent Designer\"] --> B[\"Defines Utility\"]\n  B --> C[\"Agent Behavior\"]"},
                    {"type": "markdown", "content": "Misspecified utilities can lead to disastrous AI behaviors."}
                ]
            },
            {
                "title": "Module 3: Decision Networks",
                "episodes": [
                    {"type": "markdown", "content": "## Adding Actions to Bayes Nets\nWe extend Bayesian Networks with Action nodes and Utility nodes."},
                    {"type": "concept", "title": "Decision Networks", "content": "Also called Influence Diagrams. Chance nodes (ovals), Action nodes (rectangles), Utility nodes (diamonds)."},
                    {"type": "visual", "content": "graph TD\n  A[\"Weather (Chance)\"] --> C[\"Utility\"]\n  B[\"Take Umbrella (Action)\"] --> C"},
                    {"type": "markdown", "content": "To evaluate a decision network, we instantiate the action node and calculate expected utility."},
                    {"type": "interactive", "question": "In a Decision Network, what shape usually represents an Action node?", "options": ["Oval", "Diamond", "Rectangle"], "answer": "Rectangle"},
                    {"type": "concept", "title": "Evaluating a Network", "content": "For every possible action, calculate posterior probabilities of parents of the utility node, then compute EU."},
                    {"type": "code_lab", "language": "python", "content": "def evaluate_action(action, network):\n    # Simulate setting action and inferring utility\n    pass"},
                    {"type": "markdown", "content": "This provides a structured way to solve complex, single-shot decision problems."},
                    {"type": "visual_stepper", "content": "graph LR\n  A[\"Set Action\"] --> B[\"Run Inference\"]\n  B --> C[\"Compute EU\"] --> D[\"Compare Actions\"]"},
                    {"type": "markdown", "content": "Next, we'll look at the value of gathering more information before acting."}
                ]
            },
            {
                "title": "Module 4: Value of Information",
                "episodes": [
                    {"type": "markdown", "content": "## Look Before You Leap\nShould a doctor order a costly test before treating? Only if it changes the decision."},
                    {"type": "concept", "title": "Value of Perfect Information (VPI)", "content": "Expected utility with the information minus expected utility without it."},
                    {"type": "visual", "content": "graph TD\n  A[\"EU(Action | Evidence)\"] --> C[\"VPI\"]\n  B[\"EU(Action)\"] --> C\n  style C fill:#3b82f61a"},
                    {"type": "markdown", "content": "VPI is always non-negative. Information never makes you worse off (in expectation)."},
                    {"type": "interactive", "question": "Can the Value of Perfect Information be negative?", "options": ["Yes, if the news is bad", "No, it is always >= 0", "Only for risk-seeking agents"], "answer": "No, it is always >= 0"},
                    {"type": "concept", "title": "Information Gathering Agents", "content": "Agents can iteratively calculate VPI for observables and choose to sense the world if VPI > cost of sensing."},
                    {"type": "code_lab", "language": "python", "content": "def vpi(eu_with_info, eu_without_info):\n    return max(0, eu_with_info - eu_without_info)"},
                    {"type": "markdown", "content": "VPI guides attention and sensing in autonomous robots."},
                    {"type": "visual_stepper", "content": "graph LR\n  A[\"Calculate VPI\"] --> B[\"VPI > Cost?\"]\n  B -->|Yes| C[\"Observe\"]\n  B -->|No| D[\"Act Now\"]"},
                    {"type": "markdown", "content": "This wraps up our study of rational decisions. Next up: Machine Learning."}
                ]
            }
        ]
    },
    "16": {
        "title": "Case 16: Introduction to Machine Learning",
        "modules": [
            {
                "title": "Module 1: The Learning Paradigm",
                "episodes": [
                    {"type": "markdown", "content": "# Teaching Computers to Learn\nInstead of explicitly programming rules, we feed data to algorithms to find the rules."},
                    {"type": "concept", "title": "Supervised Learning", "content": "Learning a mapping from inputs (X) to outputs (Y) given labeled examples (X, Y)."},
                    {"type": "visual", "content": "graph LR\n  A[\"Data (X, Y)\"] --> B[\"ML Algorithm\"]\n  B --> C[\"Learned Model (f)\"]\n  C --> D[\"Predictions Y_hat\"]"},
                    {"type": "markdown", "content": "This contrasts with unsupervised learning, where we only have X and look for patterns."},
                    {"type": "interactive", "question": "Which learning type uses labeled examples?", "options": ["Unsupervised", "Supervised", "Reinforcement"], "answer": "Supervised"},
                    {"type": "concept", "title": "Features and Labels", "content": "Features are the inputs (e.g., house size). Labels are what we want to predict (e.g., price)."},
                    {"type": "code_lab", "language": "python", "content": "# A simple dataset\nfeatures = [[1200], [2500], [900]]\nlabels = [150000, 300000, 100000]"},
                    {"type": "markdown", "content": "The goal is generalization: performing well on unseen data."},
                    {"type": "visual_stepper", "content": "graph TD\n  A[\"Train Data\"] --> B[\"Model\"]\n  B --> C[\"Test Data\"]\n  C --> D[\"Accuracy Measure\"]"},
                    {"type": "markdown", "content": "Generalization is the central challenge of machine learning."}
                ]
            },
            {
                "title": "Module 2: Linear Regression",
                "episodes": [
                    {"type": "markdown", "content": "## Fitting a Line\nLinear regression is the foundational supervised learning algorithm."},
                    {"type": "concept", "title": "Hypothesis Class", "content": "We assume the relationship is a straight line: y = mx + b (or Wx + b)."},
                    {"type": "visual", "content": "graph TD\n  A[\"Input X\"] --> B[\"Multiply by W\"]\n  B --> C[\"Add Bias b\"]\n  C --> D[\"Output Y\"]"},
                    {"type": "markdown", "content": "We need a way to measure how 'wrong' our current line is."},
                    {"type": "interactive", "question": "What parameter controls the slope of the line in y=Wx+b?", "options": ["b (bias)", "W (weights)", "y (output)"], "answer": "W (weights)"},
                    {"type": "concept", "title": "Loss Function", "content": "Mean Squared Error (MSE) measures the average squared difference between predictions and true labels."},
                    {"type": "code_lab", "language": "python", "content": "def mse(y_true, y_pred):\n    return sum((t - p)**2 for t, p in zip(y_true, y_pred)) / len(y_true)"},
                    {"type": "markdown", "content": "We use optimization (like Gradient Descent) to find W and b that minimize this loss."},
                    {"type": "visual_stepper", "content": "graph LR\n  A[\"Init W,b\"] --> B[\"Calc Loss\"]\n  B --> C[\"Update W,b via Gradient\"]\n  C --> A"},
                    {"type": "markdown", "content": "This iterative process is how the model 'learns'."}
                ]
            },
            {
                "title": "Module 3: Overfitting and Underfitting",
                "episodes": [
                    {"type": "markdown", "content": "## The Goldilocks Problem\nA model can be too simple, or it can memorize the noise in the data."},
                    {"type": "concept", "title": "Underfitting (High Bias)", "content": "The model is too simple to capture the underlying trend. E.g., fitting a line to a parabola."},
                    {"type": "visual", "content": "graph TD\n  A[\"Underfit: Too Simple\"] --> B[\"Good Fit: Just Right\"]\n  B --> C[\"Overfit: Memorized Noise\"]"},
                    {"type": "markdown", "content": "Overfitting (High Variance) means the model fits the training data perfectly but fails on new data."},
                    {"type": "interactive", "question": "If a model has 100% training accuracy but 50% test accuracy, it is likely:", "options": ["Underfitting", "Overfitting", "Perfect"], "answer": "Overfitting"},
                    {"type": "concept", "title": "Polynomial Regression", "content": "Using higher-degree polynomials increases model capacity, risking overfitting."},
                    {"type": "code_lab", "language": "python", "content": "import numpy as np\n# A high degree polynomial can interpolate data exactly\n# but wildly oscillates between points."},
                    {"type": "markdown", "content": "We must carefully balance model complexity and data availability."},
                    {"type": "visual_stepper", "content": "graph LR\n  A[\"Increase Complexity\"] --> B[\"Lower Train Error\"]\n  A --> C[\"Higher Test Error (Eventually)\"]"},
                    {"type": "markdown", "content": "To prevent overfitting, we use techniques like regularization and cross-validation."}
                ]
            },
            {
                "title": "Module 4: Regularization and Validation",
                "episodes": [
                    {"type": "markdown", "content": "## Taming Complexity\nHow do we stop our models from going crazy and overfitting?"},
                    {"type": "concept", "title": "Regularization", "content": "We add a penalty term to the loss function for large weights (e.g., L1 or L2 regularization)."},
                    {"type": "visual", "content": "graph TD\n  A[\"Total Loss\"] --> B[\"Data Loss (MSE)\"]\n  A --> C[\"Regularization Penalty (Complexity)\"]\n  style C fill:#f43f5e1a"},
                    {"type": "markdown", "content": "This forces the model to prefer simpler explanations (smaller weights)."},
                    {"type": "interactive", "question": "What is the primary purpose of regularization?", "options": ["To speed up training", "To reduce overfitting", "To increase training accuracy"], "answer": "To reduce overfitting"},
                    {"type": "concept", "title": "Train, Validation, Test Sets", "content": "Never evaluate on training data. Use a validation set to tune hyperparameters, and a test set for final reporting."},
                    {"type": "code_lab", "language": "python", "content": "def split_data(data, train_ratio=0.8):\n    # Simulate splitting data\n    pass"},
                    {"type": "markdown", "content": "Hyperparameters (like learning rate or regularization strength) are tuned manually or via search."},
                    {"type": "visual_stepper", "content": "graph LR\n  A[\"Train Data\"] --> B[\"Fit Model Weights\"]\n  C[\"Val Data\"] --> D[\"Tune Hyperparameters\"]\n  E[\"Test Data\"] --> F[\"Final Assessment\"]"},
                    {"type": "markdown", "content": "Congratulations, you've mastered the fundamentals of AI!"}
                ]
            }
        ]
    }
}
