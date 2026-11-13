CONTENT_12_16 = {
    "case_12": {
        "title": "Case 12: The World That Keeps Changing (Uncertainty)",
        "modules": [
            {
                "title": "Module 1: The Nature of Uncertainty",
                "blocks": [
                    {"type": "text", "content": "Welcome back, detective. We've been working with deterministic environments, but the real world is messy."},
                    {"type": "dialogue", "speaker": "Dr. Turing", "content": "In most real-world scenarios, we cannot be 100% certain about the state of the world."},
                    {"type": "text", "content": "Uncertainty arises from partial observability, nondeterminism, or a combination of both."},
                    {"type": "visual_stepper", "content": "Let's look at how uncertainty branches out.", "mermaid": "graph TD\n  S0[\"Current State\"] -->|Action| S1[\"Possible State 1 (60%)\"]\n  S0 -->|Action| S2[\"Possible State 2 (40%)\"]\n  style S0 fill:#4CAF50\n  style S1 fill:#FFC107\n  style S2 fill:#FF9800"},
                    {"type": "text", "content": "When dealing with uncertainty, we must rely on probability theory to make informed guesses."},
                    {"type": "quiz", "question": "What are the two main causes of uncertainty?", "options": ["Partial observability and nondeterminism", "Errors and bugs", "Logic and reasoning"], "answer": 0}
                ]
            },
            {
                "title": "Module 2: Modeling the Unknown",
                "blocks": [
                    {"type": "text", "content": "To act rationally under uncertainty, we assign probabilities to states."},
                    {"type": "dialogue", "speaker": "Ada", "content": "A probability distribution tells us how likely each possible state is."},
                    {"type": "visual_stepper", "content": "Here is a visualization of probability distribution.", "mermaid": "pie title \"Probability of Weather\"\n  \"Sunny\" : 50\n  \"Rainy\" : 30\n  \"Cloudy\" : 20"},
                    {"type": "text", "content": "By maintaining a 'belief state', an agent can keep track of probabilities as it moves and senses."},
                    {"type": "quiz", "question": "What is a belief state?", "options": ["A state of mind", "A probability distribution over all possible states", "A deterministic path"], "answer": 1},
                    {"type": "text", "content": "Understanding probability helps us build robust agents."}
                ]
            },
            {
                "title": "Module 3: Dealing with Partial Observability",
                "blocks": [
                    {"type": "text", "content": "In many scenarios, the agent cannot see the entire state of the world. This is partial observability."},
                    {"type": "dialogue", "speaker": "Dr. Turing", "content": "We use hidden Markov models (HMMs) or Partially Observable Markov Decision Processes (POMDPs) to model this."},
                    {"type": "visual_stepper", "content": "Partial Observability concept:", "mermaid": "graph TD\n  H1[\"Hidden State 1\"] --> H2[\"Hidden State 2\"]\n  H1 -.-> O1[\"Observation 1\"]\n  H2 -.-> O2[\"Observation 2\"]\n  style H1 fill:#607D8B\n  style H2 fill:#607D8B\n  style O1 fill:#009688\n  style O2 fill:#009688"},
                    {"type": "text", "content": "The agent must infer the hidden state from its observations."},
                    {"type": "quiz", "question": "What does a POMDP add to a standard Markov Decision Process?", "options": ["Partial observability", "Deterministic actions", "Infinite states"], "answer": 0}
                ]
            }
        ]
    },
    "case_13": {
        "title": "Case 13: The Probability Problem (Bayes Rule)",
        "modules": [
            {
                "title": "Module 1: The Foundations of Bayes",
                "blocks": [
                    {"type": "text", "content": "We often have prior beliefs that get updated when we see new evidence."},
                    {"type": "dialogue", "speaker": "Dr. Turing", "content": "This is exactly what Bayes' Theorem allows us to do mathematically."},
                    {"type": "visual_stepper", "content": "The components of Bayes Rule:", "mermaid": "graph LR\n  Prior[\"Prior Probability P(H)\"] --> Update[\"Update with Evidence P(E|H)\"]\n  Update --> Posterior[\"Posterior Probability P(H|E)\"]\n  style Prior fill:#2196F3\n  style Update fill:#9C27B0\n  style Posterior fill:#E91E63"},
                    {"type": "text", "content": "P(H|E) = (P(E|H) * P(H)) / P(E). Let's break this down."},
                    {"type": "quiz", "question": "What does P(H) represent?", "options": ["The prior probability", "The posterior probability", "The evidence"], "answer": 0}
                ]
            },
            {
                "title": "Module 2: Applying Bayes Rule",
                "blocks": [
                    {"type": "text", "content": "Imagine a medical diagnosis scenario. A disease is rare, but the test is mostly accurate."},
                    {"type": "dialogue", "speaker": "Ada", "content": "Even with an accurate test, the rarity of the disease means a positive result might still be a false positive."},
                    {"type": "visual_stepper", "content": "Updating belief after a positive test:", "mermaid": "graph TD\n  Start[\"Prior: Disease (1%)\"] --> Test[\"Positive Test\"]\n  Test --> Update[\"Apply Bayes Rule\"]\n  Update --> Result[\"Posterior: Disease given Test (~9%)\"]\n  style Start fill:#F44336\n  style Result fill:#8BC34A"},
                    {"type": "text", "content": "Notice how the posterior probability is much lower than the test's accuracy. This is the base rate fallacy!"},
                    {"type": "quiz", "question": "Why might a highly accurate test yield a low posterior probability for a positive result?", "options": ["The base rate (prior) of the disease is very low", "The test is broken", "Bayes rule is flawed"], "answer": 0},
                    {"type": "text", "content": "Bayes rule is our shield against cognitive biases."}
                ]
            },
            {
                "title": "Module 3: Naive Bayes Classifiers",
                "blocks": [
                    {"type": "text", "content": "Bayes theorem is the foundation for one of the simplest yet most effective machine learning algorithms: Naive Bayes."},
                    {"type": "dialogue", "speaker": "Dr. Turing", "content": "It's called 'naive' because it assumes that all features are independent of each other given the class label."},
                    {"type": "visual_stepper", "content": "Naive Bayes Assumption:", "mermaid": "graph TD\n  Class[\"Class C\"] --> F1[\"Feature 1\"]\n  Class --> F2[\"Feature 2\"]\n  Class --> F3[\"Feature 3\"]\n  style Class fill:#9C27B0\n  style F1 fill:#00BCD4\n  style F2 fill:#00BCD4\n  style F3 fill:#00BCD4"},
                    {"type": "text", "content": "Despite this strong assumption, it works incredibly well for tasks like spam filtering."},
                    {"type": "quiz", "question": "What is the 'naive' assumption in Naive Bayes?", "options": ["Features are conditionally independent given the class", "The prior probability is always 50%", "All features are equally important"], "answer": 0}
                ]
            }
        ]
    },
    "case_14": {
        "title": "Case 14: The Bayesian Detective (Bayesian Networks)",
        "modules": [
            {
                "title": "Module 1: Connecting the Dots",
                "blocks": [
                    {"type": "text", "content": "When dealing with many variables, calculating joint probabilities becomes intractable."},
                    {"type": "dialogue", "speaker": "Dr. Turing", "content": "Bayesian Networks come to the rescue by exploiting conditional independence."},
                    {"type": "visual_stepper", "content": "A simple Bayesian Network:", "mermaid": "graph TD\n  Burglar[\"Burglar\"] --> Alarm[\"Alarm\"]\n  Earthquake[\"Earthquake\"] --> Alarm\n  Alarm --> JohnCalls[\"John Calls\"]\n  Alarm --> MaryCalls[\"Mary Calls\"]\n  style Burglar fill:#FF5722\n  style Earthquake fill:#FF5722\n  style Alarm fill:#FFEB3B\n  style JohnCalls fill:#03A9F4\n  style MaryCalls fill:#03A9F4"},
                    {"type": "text", "content": "Nodes represent variables, and edges represent direct causal relationships."},
                    {"type": "quiz", "question": "What do edges in a Bayesian Network represent?", "options": ["Direct probabilistic dependencies", "Deterministic paths", "Time sequences"], "answer": 0}
                ]
            },
            {
                "title": "Module 2: Inference in Bayesian Networks",
                "blocks": [
                    {"type": "text", "content": "We can query the network to find out the probability of an event given some evidence."},
                    {"type": "dialogue", "speaker": "Ada", "content": "For example, if John calls, what's the probability there was a burglar?"},
                    {"type": "visual_stepper", "content": "Inference direction:", "mermaid": "graph BT\n  JohnCalls[\"Evidence: John Calls (True)\"] --> Alarm[\"Infer Alarm\"]\n  Alarm --> Burglar[\"Infer Burglar\"]\n  style JohnCalls fill:#4CAF50\n  style Alarm fill:#FFEB3B\n  style Burglar fill:#F44336"},
                    {"type": "text", "content": "This is diagnostic inference, reasoning from effects back to causes."},
                    {"type": "quiz", "question": "What type of inference reasons from effects to causes?", "options": ["Diagnostic inference", "Causal inference", "Intercausal inference"], "answer": 0},
                    {"type": "text", "content": "Bayesian networks are powerful tools for reasoning under uncertainty."}
                ]
            },
            {
                "title": "Module 3: Constructing a Bayesian Network",
                "blocks": [
                    {"type": "text", "content": "To build a Bayesian network, we need to specify its topology and the conditional probability tables (CPTs)."},
                    {"type": "dialogue", "speaker": "Dr. Turing", "content": "The CPT for a node tells us the probability of its states given the states of its parents."},
                    {"type": "visual_stepper", "content": "Conditional Probability Tables:", "mermaid": "graph TD\n  Parent[\"Parent Node\"] --> Child[\"Child Node (CPT)\"]\n  style Parent fill:#673AB7\n  style Child fill:#E91E63"},
                    {"type": "text", "content": "By carefully defining these probabilities, we encapsulate domain knowledge into the model."},
                    {"type": "quiz", "question": "What does a CPT specify in a Bayesian network?", "options": ["The probabilities of a node given its parents", "The prior probability of all nodes", "The list of children for a node"], "answer": 0}
                ]
            }
        ]
    },
    "case_15": {
        "title": "Case 15: The Decision Maker (Utility & Decision Theory)",
        "modules": [
            {
                "title": "Module 1: The Value of Outcomes",
                "blocks": [
                    {"type": "text", "content": "Probabilities tell us what might happen, but how do we choose what to do?"},
                    {"type": "dialogue", "speaker": "Dr. Turing", "content": "We need to quantify how much we prefer certain outcomes using Utility Theory."},
                    {"type": "visual_stepper", "content": "Utility of states:", "mermaid": "graph LR\n  Action[\"Action\"] -->|60%| Win[\"Win Lottery (+1000)\"]\n  Action -->|40%| Lose[\"Lose Ticket (-10)\"]\n  style Win fill:#4CAF50\n  style Lose fill:#F44336"},
                    {"type": "text", "content": "A utility function maps a state to a real number indicating its desirability."},
                    {"type": "quiz", "question": "What does a utility function do?", "options": ["Assigns a numerical value to the desirability of a state", "Calculates the probability of a state", "Determines the next action deterministically"], "answer": 0}
                ]
            },
            {
                "title": "Module 2: Expected Utility",
                "blocks": [
                    {"type": "text", "content": "To make a decision, we calculate the Expected Utility of each action."},
                    {"type": "dialogue", "speaker": "Ada", "content": "The principle of Maximum Expected Utility (MEU) states a rational agent should choose the action that maximizes expected utility."},
                    {"type": "visual_stepper", "content": "Calculating Expected Utility:", "mermaid": "graph TD\n  Act1[\"Action A\"] --> EU1[\"EU: 0.6*100 + 0.4*0 = 60\"]\n  Act2[\"Action B\"] --> EU2[\"EU: 1.0*50 = 50\"]\n  EU1 --> Choice[\"Choose Action A\"]\n  style Act1 fill:#2196F3\n  style EU1 fill:#4CAF50\n  style Choice fill:#9C27B0"},
                    {"type": "text", "content": "Expected utility combines our beliefs (probabilities) with our desires (utilities)."},
                    {"type": "quiz", "question": "What is the principle of MEU?", "options": ["Choose the action with the highest expected utility", "Choose the action with the highest probability of success", "Choose the action with the lowest risk"], "answer": 0},
                    {"type": "text", "content": "Decision theory provides a formal basis for rational behavior."}
                ]
            },
            {
                "title": "Module 3: Decision Networks",
                "blocks": [
                    {"type": "text", "content": "We can extend Bayesian networks to include decisions and utilities."},
                    {"type": "dialogue", "speaker": "Dr. Turing", "content": "These are called Decision Networks or Influence Diagrams."},
                    {"type": "visual_stepper", "content": "Components of a Decision Network:", "mermaid": "graph TD\n  Chance[\"Chance Node (Ovals)\"] --> Utility[\"Utility Node (Diamonds)\"]\n  Decision[\"Decision Node (Rectangles)\"] --> Utility\n  style Chance fill:#03A9F4\n  style Utility fill:#FFEB3B\n  style Decision fill:#8BC34A"},
                    {"type": "text", "content": "They allow us to model complex decision problems visually and computationally."},
                    {"type": "quiz", "question": "What shape typically represents a decision node in a Decision Network?", "options": ["Rectangle", "Oval", "Diamond"], "answer": 0}
                ]
            }
        ]
    },
    "case_16": {
        "title": "Case 16: The Machine That Learns (ML Intro, Overfitting)",
        "modules": [
            {
                "title": "Module 1: Learning from Data",
                "blocks": [
                    {"type": "text", "content": "Until now, we've programmed the agent's knowledge directly. But what if it could learn?"},
                    {"type": "dialogue", "speaker": "Dr. Turing", "content": "Machine learning allows systems to improve their performance on a task based on experience."},
                    {"type": "visual_stepper", "content": "The ML Pipeline:", "mermaid": "graph LR\n  Data[\"Training Data\"] --> Model[\"Learning Algorithm\"]\n  Model --> Hypothesis[\"Hypothesis/Model\"]\n  Hypothesis --> Prediction[\"Predictions on New Data\"]\n  style Data fill:#FF9800\n  style Model fill:#00BCD4\n  style Prediction fill:#8BC34A"},
                    {"type": "text", "content": "The goal is to find a hypothesis that accurately maps inputs to outputs."},
                    {"type": "quiz", "question": "What is the primary goal of machine learning?", "options": ["To generalize to unseen data", "To memorize the training data", "To follow explicit instructions"], "answer": 0}
                ]
            },
            {
                "title": "Module 2: The Danger of Overfitting",
                "blocks": [
                    {"type": "text", "content": "A model can learn the training data too well, capturing noise instead of the underlying pattern."},
                    {"type": "dialogue", "speaker": "Ada", "content": "This is called overfitting. The model performs well on training data but poorly on test data."},
                    {"type": "visual_stepper", "content": "Overfitting vs Generalization:", "mermaid": "graph TD\n  Model[\"Complex Model\"] --> Fit[\"Perfect Training Accuracy\"]\n  Fit --> Fail[\"Poor Test Accuracy (Overfitting)\"]\n  Simple[\"Simpler Model\"] --> Good[\"Good Test Accuracy (Generalization)\"]\n  style Fail fill:#F44336\n  style Good fill:#4CAF50"},
                    {"type": "text", "content": "We use techniques like cross-validation and regularization to prevent overfitting."},
                    {"type": "quiz", "question": "What characterizes an overfitted model?", "options": ["High training accuracy, low test accuracy", "Low training accuracy, high test accuracy", "Low training accuracy, low test accuracy"], "answer": 0},
                    {"type": "text", "content": "Finding the right balance of complexity is the art of machine learning."}
                ]
            },
            {
                "title": "Module 3: Evaluating Models",
                "blocks": [
                    {"type": "text", "content": "To know if we're overfitting, we must evaluate our model properly."},
                    {"type": "dialogue", "speaker": "Dr. Turing", "content": "We split our data into a training set and a testing set. The model never sees the test set during training."},
                    {"type": "visual_stepper", "content": "Train/Test Split:", "mermaid": "graph LR\n  AllData[\"All Available Data\"] --> Train[\"Training Set (e.g., 80%)\"]\n  AllData --> Test[\"Test Set (e.g., 20%)\"]\n  style AllData fill:#9E9E9E\n  style Train fill:#4CAF50\n  style Test fill:#F44336"},
                    {"type": "text", "content": "This simulates how the model will perform in the real world on unseen data."},
                    {"type": "quiz", "question": "Why do we use a separate test set?", "options": ["To evaluate the model's ability to generalize", "To give the model more data to learn from", "To speed up training"], "answer": 0}
                ]
            }
        ]
    }
}
