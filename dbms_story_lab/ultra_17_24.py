CONTENT_17_24 = {
    "17": {
        "title": "Case 17: K-Nearest Neighbors (KNN)",
        "modules": [
            {
                "title": "Module 1: Intuition and Distance Metrics",
                "episodes": [
                    {"type": "markdown", "content": "## Introduction to KNN\nK-Nearest Neighbors is a non-parametric, lazy learning algorithm used for both classification and regression."},
                    {"type": "concept", "content": "Lazy Learning means there is no explicit training phase before classification. The model simply stores the dataset."},
                    {"type": "visual", "content": "graph TD\nA[\"New Data Point\"] --> B[\"Calculate Distances\"]\nB --> C[\"Find K Nearest\"]\nC --> D[\"Majority Vote\"]"},
                    {"type": "interactive", "content": "What is the primary computational cost of KNN at test time?", "options": ["Calculating distance to all training samples", "Updating weights", "Building trees"], "answer": "Calculating distance to all training samples"},
                    {"type": "markdown", "content": "## Distance Metrics\nEuclidean, Manhattan, and Minkowski are common distance metrics."},
                    {"type": "concept", "content": "Euclidean distance is the straight-line distance, while Manhattan is the sum of absolute differences."},
                    {"type": "visual_stepper", "content": "graph LR\nstyle A fill:#10b9811a\nA[\"Point A (1,1)\"] --> B[\"Point B (4,5)\"]\nB --> C[\"Euclidean = 5\"]"},
                    {"type": "code_lab", "content": "import numpy as np\ndef euclidean(a, b): return np.sqrt(np.sum((a-b)**2))"},
                    {"type": "interactive", "content": "Which metric is best for high dimensional sparse data?", "options": ["Cosine Similarity", "Euclidean", "Manhattan"], "answer": "Cosine Similarity"},
                    {"type": "markdown", "content": "Summary of Module 1: KNN relies heavily on the choice of distance metric and K."}
                ]
            },
            {
                "title": "Module 2: Choosing K and Curse of Dimensionality",
                "episodes": [
                    {"type": "markdown", "content": "## Choosing the right K\nA small K leads to low bias but high variance (overfitting). A large K leads to high bias but low variance."},
                    {"type": "concept", "content": "Odd values of K are preferred in binary classification to prevent ties."},
                    {"type": "visual", "content": "graph TD\nA[\"K=1\"] --> B[\"Complex Decision Boundary\"]\nC[\"K=100\"] --> D[\"Smooth Decision Boundary\"]"},
                    {"type": "interactive", "content": "What happens if K equals the total number of training points?", "options": ["Predicts the majority class always", "Perfect accuracy", "Random guessing"], "answer": "Predicts the majority class always"},
                    {"type": "markdown", "content": "## Curse of Dimensionality\nAs dimensions increase, the distance between any two points becomes uniformly large."},
                    {"type": "concept", "content": "In high dimensions, the concept of 'nearest' loses its meaning, degrading KNN performance."},
                    {"type": "visual_stepper", "content": "graph TD\nstyle X fill:#3b82f61a\nX[\"1D: Points close\"] --> Y[\"2D: Points spread\"]\nY --> Z[\"100D: All points equidistant\"]"},
                    {"type": "code_lab", "content": "from sklearn.neighbors import KNeighborsClassifier\nknn = KNeighborsClassifier(n_neighbors=5)"},
                    {"type": "interactive", "content": "How to mitigate the curse of dimensionality?", "options": ["PCA/Feature Selection", "Increase K", "Decrease K"], "answer": "PCA/Feature Selection"},
                    {"type": "markdown", "content": "Summary: Balance K using cross-validation and keep dimensions low."}
                ]
            },
            {
                "title": "Module 3: Advanced KNN Implementations",
                "episodes": [
                    {"type": "markdown", "content": "## Faster Search Algorithms\nBrute force distance calculation is O(N*D). We can use tree-based structures."},
                    {"type": "concept", "content": "KD-Trees partition the space along axes, reducing average search time to O(log N)."},
                    {"type": "visual", "content": "graph TD\nA[\"Root Node (Dim 0)\"] --> B[\"Left Child\"]\nA --> C[\"Right Child\"]"},
                    {"type": "interactive", "content": "When do KD-Trees perform worse than brute force?", "options": ["High Dimensions (D > 20)", "Low Dimensions", "Large N"], "answer": "High Dimensions (D > 20)"},
                    {"type": "markdown", "content": "## Ball Trees\nBall Trees partition data into overlapping hyperspheres, working better in high dimensions."},
                    {"type": "concept", "content": "Ball Trees check if the distance to a sphere's center minus its radius exceeds the current nearest neighbor."},
                    {"type": "visual_stepper", "content": "graph LR\nstyle S fill:#f59e0b1a\nS[\"Root Sphere\"] --> T[\"Sub-sphere 1\"]\nS --> U[\"Sub-sphere 2\"]"},
                    {"type": "code_lab", "content": "knn = KNeighborsClassifier(algorithm='ball_tree')"},
                    {"type": "interactive", "content": "Which algorithm is default in sklearn when data is sparse?", "options": ["Brute force", "KD-Tree", "Ball Tree"], "answer": "Brute force"},
                    {"type": "markdown", "content": "Summary: Use KD-Tree for low dims, Ball Tree for medium, Brute for sparse/high."}
                ]
            },
            {
                "title": "Module 4: KNN Regression and Weights",
                "episodes": [
                    {"type": "markdown", "content": "## KNN Regression\nInstead of majority vote, KNN can output the average of the K nearest neighbors."},
                    {"type": "concept", "content": "Distance weighting gives closer neighbors more influence on the final prediction."},
                    {"type": "visual", "content": "graph TD\nA[\"Neighbors: 5, 7, 9\"] --> B[\"Uniform Mean: 7\"]\nA --> C[\"Weighted Mean: 5.5 (if 5 is closer)\"]"},
                    {"type": "interactive", "content": "What is a common weight function?", "options": ["Inverse of distance", "Square of distance", "Log of distance"], "answer": "Inverse of distance"},
                    {"type": "markdown", "content": "## Scaling Data\nFeatures must be scaled (e.g., Standardized) before applying KNN, or large-range features will dominate."},
                    {"type": "concept", "content": "StandardScaler shifts the mean to 0 and variance to 1."},
                    {"type": "visual_stepper", "content": "graph LR\nstyle W fill:#ef44441a\nW[\"Raw Age: 20-80, Salary: 50k-200k\"] --> X[\"Scaled Age: -1 to 1, Scaled Salary: -1 to 1\"]"},
                    {"type": "code_lab", "content": "from sklearn.preprocessing import StandardScaler\nscaler = StandardScaler()"},
                    {"type": "interactive", "content": "If we don't scale, which feature dominates?", "options": ["The one with the largest magnitude/variance", "The one with the smallest", "They have equal impact"], "answer": "The one with the largest magnitude/variance"},
                    {"type": "markdown", "content": "Summary: Always scale data and consider distance-weighting for KNN."}
                ]
            }
        ]
    },
    "18": {
        "title": "Case 18: Naive Bayes",
        "modules": [
            {
                "title": "Module 1: Bayes' Theorem Fundamentals",
                "episodes": [
                    {"type": "markdown", "content": "## Bayes' Theorem\nBayes' theorem calculates the probability of an event based on prior knowledge."},
                    {"type": "concept", "content": "P(A|B) = [P(B|A) * P(A)] / P(B)"},
                    {"type": "visual", "content": "graph TD\nA[\"Prior P(A)\"] --> B[\"Likelihood P(B|A)\"]\nB --> C[\"Posterior P(A|B)\"]"},
                    {"type": "interactive", "content": "What does P(B|A) represent?", "options": ["Likelihood", "Prior", "Evidence"], "answer": "Likelihood"},
                    {"type": "markdown", "content": "## Naive Assumption\nThe algorithm is 'naive' because it assumes all features are independent given the class."},
                    {"type": "concept", "content": "P(x1, x2 | y) is simplified to P(x1 | y) * P(x2 | y)."},
                    {"type": "visual_stepper", "content": "graph LR\nstyle N fill:#8b5cf61a\nN[\"Complex Joint Prob\"] --> M[\"Product of Marginals\"]"},
                    {"type": "code_lab", "content": "prob = prior * likelihood_feature1 * likelihood_feature2"},
                    {"type": "interactive", "content": "Is the naive assumption usually true in real data?", "options": ["No", "Yes"], "answer": "No"},
                    {"type": "markdown", "content": "Summary: Bayes theorem + Independence assumption = Naive Bayes."}
                ]
            },
            {
                "title": "Module 2: Gaussian Naive Bayes",
                "episodes": [
                    {"type": "markdown", "content": "## Continuous Data\nWhen features are continuous, we assume they are drawn from a normal (Gaussian) distribution."},
                    {"type": "concept", "content": "We calculate the mean and variance of each feature for each class."},
                    {"type": "visual", "content": "graph TD\nA[\"Continuous Feature\"] --> B[\"Calculate Mean & Variance per Class\"]\nB --> C[\"Use PDF for Likelihood\"]"},
                    {"type": "interactive", "content": "What does the PDF calculate in Gaussian NB?", "options": ["Likelihood", "Prior", "Posterior"], "answer": "Likelihood"},
                    {"type": "markdown", "content": "## The Math\nThe likelihood is the Gaussian probability density function (PDF)."},
                    {"type": "concept", "content": "exp(-(x-mean)^2 / (2*var)) / sqrt(2*pi*var)"},
                    {"type": "visual_stepper", "content": "graph TD\nstyle G fill:#14b8a61a\nG[\"Feature X\"] --> H[\"Plug into Gaussian PDF\"] --> I[\"Likelihood P(X|Y)\"]"},
                    {"type": "code_lab", "content": "from sklearn.naive_bayes import GaussianNB\nmodel = GaussianNB()"},
                    {"type": "interactive", "content": "Can Gaussian NB handle categorical data natively?", "options": ["No", "Yes"], "answer": "No"},
                    {"type": "markdown", "content": "Summary: Gaussian NB uses the normal distribution to handle continuous numerical features."}
                ]
            },
            {
                "title": "Module 3: Multinomial & Bernoulli NB",
                "episodes": [
                    {"type": "markdown", "content": "## Text Classification\nMultinomial and Bernoulli NB are heavily used for text and document classification."},
                    {"type": "concept", "content": "Multinomial deals with feature counts (word frequencies), Bernoulli deals with boolean presence (word exists or not)."},
                    {"type": "visual", "content": "graph TD\nA[\"Text Data\"] --> B[\"TF-IDF or Count Vectorizer\"]\nB --> C[\"Multinomial NB\"]"},
                    {"type": "interactive", "content": "Which NB variant is best if features are binary (0/1)?", "options": ["Bernoulli", "Gaussian", "Multinomial"], "answer": "Bernoulli"},
                    {"type": "markdown", "content": "## Laplace Smoothing\nIf a word never appears in the training set for a class, its probability is 0, wiping out the entire product."},
                    {"type": "concept", "content": "Laplace (Add-1) smoothing adds 1 to all counts to prevent zero probabilities."},
                    {"type": "visual_stepper", "content": "graph LR\nstyle L fill:#f43f5e1a\nL[\"Count = 0\"] --> M[\"Count = 1 (Smoothed)\"] --> N[\"Prob > 0\"]"},
                    {"type": "code_lab", "content": "from sklearn.naive_bayes import MultinomialNB\nmodel = MultinomialNB(alpha=1.0)"},
                    {"type": "interactive", "content": "What is the alpha parameter in MultinomialNB?", "options": ["Smoothing parameter", "Learning rate", "Regularization"], "answer": "Smoothing parameter"},
                    {"type": "markdown", "content": "Summary: Use Multinomial for counts and apply smoothing to avoid zero probabilities."}
                ]
            },
            {
                "title": "Module 4: Underflow and Log Probabilities",
                "episodes": [
                    {"type": "markdown", "content": "## The Underflow Problem\nMultiplying many small probabilities results in a number too small for computers to represent (floating-point underflow)."},
                    {"type": "concept", "content": "We take the logarithm of probabilities, turning multiplication into addition."},
                    {"type": "visual", "content": "graph TD\nA[\"P1 * P2 * P3\"] --> B[\"log(P1) + log(P2) + log(P3)\"]"},
                    {"type": "interactive", "content": "Why is log(x) monotonically increasing?", "options": ["It preserves the ordering of probabilities", "It changes the predicted class", "It makes values positive"], "answer": "It preserves the ordering of probabilities"},
                    {"type": "markdown", "content": "## Log-Sum-Exp Trick\nA standard trick to numerically stabilize calculations involving sums of exponentials."},
                    {"type": "concept", "content": "argmax(P) is identical to argmax(log P)."},
                    {"type": "visual_stepper", "content": "graph LR\nstyle E fill:#0ea5e91a\nE[\"Calculate Log Posteriors\"] --> F[\"Find Max Log Posterior\"] --> G[\"Select Class\"]"},
                    {"type": "code_lab", "content": "import numpy as np\nlog_prob = np.log(prior) + np.sum(np.log(likelihoods))"},
                    {"type": "interactive", "content": "Does converting to log probabilities change the final classification?", "options": ["No", "Yes"], "answer": "No"},
                    {"type": "markdown", "content": "Summary: Log probabilities are crucial for robust implementation of Naive Bayes."}
                ]
            }
        ]
    },
    "19": {
        "title": "Case 19: Decision Trees",
        "modules": [
            {
                "title": "Module 1: Tree Terminology",
                "episodes": [
                    {"type": "markdown", "content": "## Decision Tree Structure\nA tree has a root, internal nodes (splits), and leaves (predictions)."},
                    {"type": "concept", "content": "Trees recursively partition the feature space into hyper-rectangles."},
                    {"type": "visual", "content": "graph TD\nA[\"Root Node\"] --> B[\"Internal Node\"]\nA --> C[\"Leaf Node\"]"},
                    {"type": "interactive", "content": "What does a leaf node represent?", "options": ["A class label or value", "A feature to split on", "The entire dataset"], "answer": "A class label or value"},
                    {"type": "markdown", "content": "## Splitting Rules\nAt each node, the tree picks a feature and a threshold to split the data."},
                    {"type": "concept", "content": "The goal of splitting is to maximize the homogeneity (purity) of the child nodes."},
                    {"type": "visual_stepper", "content": "graph LR\nstyle T fill:#a855f71a\nT[\"Mixed Data\"] --> U[\"Split on Age > 30\"] --> V[\"Purer Child Nodes\"]"},
                    {"type": "code_lab", "content": "from sklearn.tree import DecisionTreeClassifier\ndt = DecisionTreeClassifier()"},
                    {"type": "interactive", "content": "Are decision trees sensitive to feature scaling?", "options": ["No", "Yes"], "answer": "No"},
                    {"type": "markdown", "content": "Summary: Trees form a set of if-else rules that partition data into pure regions."}
                ]
            },
            {
                "title": "Module 2: Entropy and Information Gain",
                "episodes": [
                    {"type": "markdown", "content": "## Entropy\nEntropy is a measure of impurity, uncertainty, or chaos in a node."},
                    {"type": "concept", "content": "H(S) = - sum(p_i * log2(p_i)). Entropy is 0 if all samples belong to one class."},
                    {"type": "visual", "content": "graph TD\nA[\"High Entropy (50/50 split)\"] --> B[\"Low Entropy (90/10 split)\"]"},
                    {"type": "interactive", "content": "What is the max entropy for a binary classification node?", "options": ["1.0", "0.5", "0.0"], "answer": "1.0"},
                    {"type": "markdown", "content": "## Information Gain\nInformation Gain is the reduction in entropy after a split."},
                    {"type": "concept", "content": "IG = Entropy(Parent) - Weighted_Avg_Entropy(Children)"},
                    {"type": "visual_stepper", "content": "graph LR\nstyle I fill:#ec48991a\nI[\"Parent Entropy\"] --> J[\"Subtract Child Entropies\"] --> K[\"Information Gain\"]"},
                    {"type": "code_lab", "content": "dt = DecisionTreeClassifier(criterion='entropy')"},
                    {"type": "interactive", "content": "The tree algorithm selects the split that _____ Information Gain.", "options": ["Maximizes", "Minimizes", "Ignores"], "answer": "Maximizes"},
                    {"type": "markdown", "content": "Summary: ID3 and C4.5 algorithms use Entropy and Information Gain to build trees."}
                ]
            },
            {
                "title": "Module 3: Gini Impurity",
                "episodes": [
                    {"type": "markdown", "content": "## Gini Impurity\nAn alternative to Entropy, used by the CART algorithm (default in sklearn)."},
                    {"type": "concept", "content": "Gini measures the probability of incorrectly classifying a randomly chosen element."},
                    {"type": "visual", "content": "graph TD\nA[\"Gini = 1 - sum(p_i^2)\"] --> B[\"Max Gini = 0.5 (Binary)\"]"},
                    {"type": "interactive", "content": "Why is Gini slightly faster to compute than Entropy?", "options": ["No logarithm calculation", "It only handles binary trees", "It ignores some data"], "answer": "No logarithm calculation"},
                    {"type": "markdown", "content": "## Comparing Gini and Entropy\nIn practice, they yield very similar trees, but Gini is marginally faster."},
                    {"type": "concept", "content": "Gini tends to isolate the most frequent class in its own branch, while Entropy tends to produce slightly more balanced trees."},
                    {"type": "visual_stepper", "content": "graph TD\nstyle G fill:#f973161a\nG[\"CART Algorithm\"] --> H[\"Uses Gini Impurity\"] --> I[\"Binary Splits Only\"]"},
                    {"type": "code_lab", "content": "dt = DecisionTreeClassifier(criterion='gini')"},
                    {"type": "interactive", "content": "Is Gini Impurity bounded between 0 and 1?", "options": ["Yes", "No"], "answer": "Yes"},
                    {"type": "markdown", "content": "Summary: Default to Gini for performance, but Entropy is theoretically robust for information theory."}
                ]
            },
            {
                "title": "Module 4: Overfitting and Pruning",
                "episodes": [
                    {"type": "markdown", "content": "## Overfitting in Trees\nA fully grown tree will perfectly memorize the training data, leading to horrible generalization."},
                    {"type": "concept", "content": "Leaves with a single sample have an impurity of 0, but represent noise (overfitting)."},
                    {"type": "visual", "content": "graph TD\nA[\"Unconstrained Tree\"] --> B[\"Depth = 20+\"] --> C[\"Overfitting\"]"},
                    {"type": "interactive", "content": "Which hyperparameter restricts tree depth?", "options": ["max_depth", "min_samples_leaf", "Both"], "answer": "Both"},
                    {"type": "markdown", "content": "## Pre-pruning vs Post-pruning\nPre-pruning stops the tree from growing (early stopping). Post-pruning grows a full tree then removes branches."},
                    {"type": "concept", "content": "Cost Complexity Pruning (ccp_alpha) penalizes trees with too many leaves."},
                    {"type": "visual_stepper", "content": "graph LR\nstyle P fill:#22c55e1a\nP[\"Full Tree\"] --> Q[\"Calculate Subtree Cost\"] --> R[\"Prune Weakest Link\"]"},
                    {"type": "code_lab", "content": "dt = DecisionTreeClassifier(ccp_alpha=0.015)\ndt.fit(X, y)"},
                    {"type": "interactive", "content": "Increasing ccp_alpha will lead to a _____ tree.", "options": ["Smaller", "Larger", "Identical"], "answer": "Smaller"},
                    {"type": "markdown", "content": "Summary: Always constrain your trees using max_depth or ccp_alpha to prevent overfitting."}
                ]
            }
        ]
    },
    "20": {
        "title": "Case 20: Q-Learning & RL",
        "modules": [
            {
                "title": "Module 1: RL Framework",
                "episodes": [
                    {"type": "markdown", "content": "## Reinforcement Learning (RL)\nAn agent learns to make sequential decisions by interacting with an environment."},
                    {"type": "concept", "content": "The agent observes a State (S), takes an Action (A), and receives a Reward (R) and Next State (S')."},
                    {"type": "visual", "content": "graph LR\nA[\"Agent\"] -- Action --> B[\"Environment\"]\nB -- State, Reward --> A"},
                    {"type": "interactive", "content": "What is the goal of the RL agent?", "options": ["Maximize cumulative reward", "Minimize loss function", "Memorize states"], "answer": "Maximize cumulative reward"},
                    {"type": "markdown", "content": "## Markov Decision Process (MDP)\nRL environments are formalized as MDPs, satisfying the Markov property."},
                    {"type": "concept", "content": "Markov Property: The future depends only on the current state, not the history."},
                    {"type": "visual_stepper", "content": "graph TD\nstyle M fill:#6366f11a\nM[\"S(t), A(t)\"] --> N[\"P(S(t+1) | S(t), A(t))\"]"},
                    {"type": "code_lab", "content": "import gym\nenv = gym.make('FrozenLake-v1')\nstate = env.reset()"},
                    {"type": "interactive", "content": "What defines the transition dynamics of an MDP?", "options": ["Transition Probability Matrix", "The Agent's Policy", "The Reward Function"], "answer": "Transition Probability Matrix"},
                    {"type": "markdown", "content": "Summary: RL is modeled as an MDP where agents act to maximize return."}
                ]
            },
            {
                "title": "Module 2: Q-Values and Policies",
                "episodes": [
                    {"type": "markdown", "content": "## The Q-Function\nThe Action-Value function, Q(s, a), represents the expected return starting from state s, taking action a."},
                    {"type": "concept", "content": "Optimal Q-value, Q*(s, a), yields the maximum possible reward."},
                    {"type": "visual", "content": "graph TD\nA[\"State s\"] --> B[\"Action a\"]\nB --> C[\"Q(s, a) Score\"]"},
                    {"type": "interactive", "content": "How do we derive the optimal policy from Q*(s, a)?", "options": ["Take argmax over actions for a given state", "Take average of actions", "Random selection"], "answer": "Take argmax over actions for a given state"},
                    {"type": "markdown", "content": "## Policy (Pi)\nA policy is a mapping from states to actions."},
                    {"type": "concept", "content": "A deterministic policy always maps a state to the exact same action."},
                    {"type": "visual_stepper", "content": "graph LR\nstyle P fill:#14b8a61a\nP[\"Observe State\"] --> Q[\"Consult Policy Pi(s)\"] --> R[\"Execute Action\"]"},
                    {"type": "code_lab", "content": "def policy(state, q_table):\n    return np.argmax(q_table[state])"},
                    {"type": "interactive", "content": "What is a stochastic policy?", "options": ["Outputs a probability distribution over actions", "Outputs a single action", "Outputs a reward"], "answer": "Outputs a probability distribution over actions"},
                    {"type": "markdown", "content": "Summary: Q-values estimate future rewards; policies use Q-values to choose actions."}
                ]
            },
            {
                "title": "Module 3: The Bellman Equation",
                "episodes": [
                    {"type": "markdown", "content": "## Bellman Optimality Equation\nThe foundation of Q-learning, breaking the value into immediate reward plus discounted future value."},
                    {"type": "concept", "content": "Q(s,a) = R(s,a) + gamma * max_a' Q(s', a')"},
                    {"type": "visual", "content": "graph TD\nA[\"Q(s,a)\"] --> B[\"Immediate Reward\"]\nA --> C[\"Discounted Future Max Q\"]"},
                    {"type": "interactive", "content": "What does the discount factor (gamma) do?", "options": ["Values present rewards higher than future rewards", "Increases learning rate", "Explores new states"], "answer": "Values present rewards higher than future rewards"},
                    {"type": "markdown", "content": "## Q-Learning Update Rule\nQ-learning uses Temporal Difference (TD) learning to iteratively update Q-values."},
                    {"type": "concept", "content": "Q_new = Q_old + alpha * (Reward + gamma * max_Q_next - Q_old)"},
                    {"type": "visual_stepper", "content": "graph LR\nstyle B fill:#ef44441a\nB[\"TD Target = R + gamma*max_Q\"] --> C[\"TD Error = Target - Q_old\"] --> D[\"Update Q_old by alpha * Error\"]"},
                    {"type": "code_lab", "content": "q_table[s, a] = q_table[s, a] + lr * (r + gamma * np.max(q_table[s_]) - q_table[s, a])"},
                    {"type": "interactive", "content": "What is alpha in the update rule?", "options": ["Learning Rate", "Discount Factor", "Reward"], "answer": "Learning Rate"},
                    {"type": "markdown", "content": "Summary: The Bellman equation allows us to recursively estimate optimal Q-values."}
                ]
            },
            {
                "title": "Module 4: Exploration vs Exploitation",
                "episodes": [
                    {"type": "markdown", "content": "## The Dilemma\nShould the agent exploit the best-known action, or explore unknown actions to find potentially better ones?"},
                    {"type": "concept", "content": "Without exploration, the agent might get stuck in a local optimum."},
                    {"type": "visual", "content": "graph TD\nA[\"Exploit (Greedy)\"] --> B[\"Use Max Q\"]\nA --> C[\"Explore\"] --> D[\"Random Action\"]"},
                    {"type": "interactive", "content": "What happens if exploration is 0 from the start?", "options": ["Agent will likely learn a suboptimal policy", "Agent learns optimally", "Agent takes forever to learn"], "answer": "Agent will likely learn a suboptimal policy"},
                    {"type": "markdown", "content": "## Epsilon-Greedy Strategy\nA simple and effective way to balance exploration and exploitation."},
                    {"type": "concept", "content": "With probability epsilon, take a random action. Otherwise, take the greedy action."},
                    {"type": "visual_stepper", "content": "graph LR\nstyle E fill:#eab3081a\nE[\"Generate Random Num 0-1\"] --> F[\"If < Epsilon: Explore\"] --> G[\"Else: Exploit\"]"},
                    {"type": "code_lab", "content": "import random\nif random.uniform(0, 1) < epsilon:\n    action = env.action_space.sample()\nelse:\n    action = np.argmax(q_table[state])"},
                    {"type": "interactive", "content": "How should epsilon change over time?", "options": ["Decay (decrease) over time", "Increase over time", "Stay constant"], "answer": "Decay (decrease) over time"},
                    {"type": "markdown", "content": "Summary: Epsilon-decay schedules allow agents to explore early and exploit later."}
                ]
            }
        ]
    },
    "21": {
        "title": "Case 21: PROLOG & Logic Programming",
        "modules": [
            {
                "title": "Module 1: Facts and Rules",
                "episodes": [
                    {"type": "markdown", "content": "## Declarative Programming\nPROLOG is declarative. You specify *what* the problem is, not *how* to solve it."},
                    {"type": "concept", "content": "A PROLOG program is a database of facts and rules."},
                    {"type": "visual", "content": "graph TD\nA[\"Knowledge Base\"] --> B[\"Facts (Truths)\"]\nA --> C[\"Rules (Logic)\"]"},
                    {"type": "interactive", "content": "In PROLOG, lowercase letters denote:", "options": ["Atoms/Constants", "Variables", "Functions"], "answer": "Atoms/Constants"},
                    {"type": "markdown", "content": "## Defining Facts\nFacts declare unconditionally true statements, terminated by a period."},
                    {"type": "concept", "content": "parent(john, mary). means John is the parent of Mary."},
                    {"type": "visual_stepper", "content": "graph LR\nstyle F fill:#8b5cf61a\nF[\"Predicate: parent\"] --> G[\"Arguments: john, mary\"]"},
                    {"type": "code_lab", "content": "% PROLOG\nlikes(alice, pizza).\nlikes(bob, burgers)."},
                    {"type": "interactive", "content": "How do you define a variable in PROLOG?", "options": ["Capital letter or underscore", "Lowercase letter", "$ sign"], "answer": "Capital letter or underscore"},
                    {"type": "markdown", "content": "Summary: Facts are the ground truths in a PROLOG database."}
                ]
            },
            {
                "title": "Module 2: Rules and Queries",
                "episodes": [
                    {"type": "markdown", "content": "## Writing Rules\nRules describe conditional truths. Head :- Body."},
                    {"type": "concept", "content": "The ':-' symbol means 'if'. A comma ',' means logical AND."},
                    {"type": "visual", "content": "graph TD\nA[\"Head (Conclusion)\"] --> B[\":- (If)\"] --> C[\"Body (Conditions)\"]"},
                    {"type": "interactive", "content": "What does semicolon ';' mean in PROLOG rules?", "options": ["Logical OR", "Logical AND", "End of line"], "answer": "Logical OR"},
                    {"type": "markdown", "content": "## Querying the DB\nYou ask questions to the PROLOG interpreter using queries."},
                    {"type": "concept", "content": "?- likes(alice, X). asks 'What does Alice like?'"},
                    {"type": "visual_stepper", "content": "graph LR\nstyle Q fill:#10b9811a\nQ[\"Query: ?- parent(X, mary).\"] --> R[\"Search KB\"] --> S[\"Bind X = john\"]"},
                    {"type": "code_lab", "content": "grandparent(X, Y) :- parent(X, Z), parent(Z, Y)."},
                    {"type": "interactive", "content": "If a query has no matching facts, PROLOG returns:", "options": ["false", "error", "null"], "answer": "false"},
                    {"type": "markdown", "content": "Summary: Rules encode logic, and queries trigger the search engine."}
                ]
            },
            {
                "title": "Module 3: Unification and Backtracking",
                "episodes": [
                    {"type": "markdown", "content": "## Unification\nUnification is how PROLOG matches terms and binds variables."},
                    {"type": "concept", "content": "Two terms unify if they are identical, or if variables can be bound to make them identical."},
                    {"type": "visual", "content": "graph TD\nA[\"Term 1: likes(X, pizza)\"] <--> B[\"Term 2: likes(bob, pizza)\"]\nB --> C[\"Unifies! X=bob\"]"},
                    {"type": "interactive", "content": "Does `likes(alice, X)` unify with `likes(Y, pizza)`?", "options": ["Yes, X=pizza, Y=alice", "No"], "answer": "Yes, X=pizza, Y=alice"},
                    {"type": "markdown", "content": "## Backtracking\nIf PROLOG goes down a logical path that fails, it backtracks to the last choice point and tries another path."},
                    {"type": "concept", "content": "This depth-first search strategy is the core execution model of PROLOG."},
                    {"type": "visual_stepper", "content": "graph TD\nstyle B fill:#f43f5e1a\nB[\"Try Rule A\"] --> C[\"Fails!\"] --> D[\"Backtrack\"] --> E[\"Try Rule B\"]"},
                    {"type": "code_lab", "content": "% Backtracking in action implicitly through comma/AND failures."},
                    {"type": "interactive", "content": "What algorithm does PROLOG use for its search?", "options": ["Depth-First Search", "Breadth-First Search", "A*"], "answer": "Depth-First Search"},
                    {"type": "markdown", "content": "Summary: PROLOG's power comes from automatic unification and recursive backtracking."}
                ]
            },
            {
                "title": "Module 4: Recursion and Lists",
                "episodes": [
                    {"type": "markdown", "content": "## Lists in PROLOG\nLists are defined using brackets, with a Head and a Tail `[H|T]`."},
                    {"type": "concept", "content": "The Head is the first element, the Tail is a list of the remaining elements."},
                    {"type": "visual", "content": "graph TD\nA[\"List: [1,2,3]\"] --> B[\"Head: 1\"]\nA --> C[\"Tail: [2,3]\"]"},
                    {"type": "interactive", "content": "In the list `[a]`, what is the Tail?", "options": ["[] (empty list)", "a", "error"], "answer": "[] (empty list)"},
                    {"type": "markdown", "content": "## Recursive Rules\nLists are processed recursively by operating on the Head and recursing on the Tail."},
                    {"type": "concept", "content": "A base case (often the empty list) is strictly required to stop recursion."},
                    {"type": "visual_stepper", "content": "graph LR\nstyle R fill:#3b82f61a\nR[\"process([H|T])\"] --> S[\"Do something with H\"] --> T[\"Call process(T)\"]"},
                    {"type": "code_lab", "content": "member(X, [X|_]).\nmember(X, [_|T]) :- member(X, T)."},
                    {"type": "interactive", "content": "What does the `_` (underscore) represent in PROLOG?", "options": ["Anonymous variable (don't care)", "Syntax error", "Null pointer"], "answer": "Anonymous variable (don't care)"},
                    {"type": "markdown", "content": "Summary: Lists and recursion form the backbone of complex PROLOG programs."}
                ]
            }
        ]
    },
    "22": {
        "title": "Case 22: Expert Systems",
        "modules": [
            {
                "title": "Module 1: Architecture of ES",
                "episodes": [
                    {"type": "markdown", "content": "## What is an Expert System?\nAn AI program that emulates the decision-making ability of a human expert."},
                    {"type": "concept", "content": "Designed to solve complex problems by reasoning through bodies of knowledge, represented mainly as if-then rules."},
                    {"type": "visual", "content": "graph TD\nA[\"User\"] --> B[\"User Interface\"]\nB --> C[\"Inference Engine\"]\nC <--> D[\"Knowledge Base\"]"},
                    {"type": "interactive", "content": "Which component contains the domain-specific rules?", "options": ["Knowledge Base", "Inference Engine", "User Interface"], "answer": "Knowledge Base"},
                    {"type": "markdown", "content": "## The Knowledge Base\nContains facts and rules (heuristics) extracted from human experts."},
                    {"type": "concept", "content": "Knowledge representation is typically done via production rules (IF condition THEN action)."},
                    {"type": "visual_stepper", "content": "graph LR\nstyle K fill:#f59e0b1a\nK[\"Domain Expert\"] --> L[\"Knowledge Engineer\"] --> M[\"Knowledge Base\"]"},
                    {"type": "code_lab", "content": "# Conceptual python structure\nknowledge_base = {'fever': True, 'cough': True}\nif knowledge_base['fever']: print('Possible Flu')"},
                    {"type": "interactive", "content": "Who translates human expertise into rules?", "options": ["Knowledge Engineer", "The User", "The Inference Engine"], "answer": "Knowledge Engineer"},
                    {"type": "markdown", "content": "Summary: ES separate the logic (engine) from the rules (knowledge base)."}
                ]
            },
            {
                "title": "Module 2: Inference Engine",
                "episodes": [
                    {"type": "markdown", "content": "## The Inference Engine\nThe 'brain' of the expert system that applies logical rules to the knowledge base to deduce new information."},
                    {"type": "concept", "content": "It primarily uses Forward Chaining or Backward Chaining."},
                    {"type": "visual", "content": "graph TD\nA[\"Facts\"] --> B[\"Inference Engine\"]\nC[\"Rules\"] --> B\nB --> D[\"Conclusions\"]"},
                    {"type": "interactive", "content": "Can an inference engine handle uncertainty?", "options": ["Yes, using certainty factors or fuzzy logic", "No, it requires strict boolean logic"], "answer": "Yes, using certainty factors or fuzzy logic"},
                    {"type": "markdown", "content": "## Forward Chaining\nData-driven approach. Start with facts, apply rules to infer new facts, until a goal is reached."},
                    {"type": "concept", "content": "Best used when there is a lot of initial data, like configuration tasks or monitoring."},
                    {"type": "visual_stepper", "content": "graph LR\nstyle F fill:#22c55e1a\nF[\"Fact: It is raining\"] --> G[\"Rule: IF raining THEN grass wet\"] --> H[\"New Fact: Grass wet\"]"},
                    {"type": "code_lab", "content": "# Forward Chaining\nwhile new_facts_generated:\n    apply_rules_to(facts)"},
                    {"type": "interactive", "content": "Forward chaining is: ", "options": ["Data-driven", "Goal-driven"], "answer": "Data-driven"},
                    {"type": "markdown", "content": "Summary: Forward chaining builds up from known data to conclusions."}
                ]
            },
            {
                "title": "Module 3: Backward Chaining",
                "episodes": [
                    {"type": "markdown", "content": "## Backward Chaining\nGoal-driven approach. Start with a hypothesis (goal) and work backwards to see if the facts support it."},
                    {"type": "concept", "content": "Best for diagnostic systems (like medical diagnosis) where you have a specific hypothesis to verify."},
                    {"type": "visual", "content": "graph TD\nA[\"Goal: Patient has Flu\"] --> B[\"Check Rule: IF Fever AND Cough\"] --> C[\"Ask: Does patient have fever?\"]"},
                    {"type": "interactive", "content": "PROLOG's default execution model is based on:", "options": ["Backward Chaining", "Forward Chaining"], "answer": "Backward Chaining"},
                    {"type": "markdown", "content": "## How it Works\nIf a condition of a rule isn't known, it becomes a sub-goal."},
                    {"type": "concept", "content": "The system recursively tries to satisfy sub-goals until it hits ground facts or asks the user."},
                    {"type": "visual_stepper", "content": "graph TD\nstyle B fill:#a855f71a\nB[\"Hypothesis X\"] --> C[\"Requires Y\"] --> D[\"Requires Z\"] --> E[\"Check Fact Z\"]"},
                    {"type": "code_lab", "content": "def check_goal(goal):\n    for rule in rules_yielding(goal):\n         if all(check_goal(c) for c in rule.conditions): return True"},
                    {"type": "interactive", "content": "Backward chaining is: ", "options": ["Goal-driven", "Data-driven"], "answer": "Goal-driven"},
                    {"type": "markdown", "content": "Summary: Backward chaining starts with the answer and looks for the evidence."}
                ]
            },
            {
                "title": "Module 4: Uncertainty and Modern ES",
                "episodes": [
                    {"type": "markdown", "content": "## Handling Uncertainty\nReal-world knowledge is rarely absolute. ES use Certainty Factors (CF) or Bayesian Networks."},
                    {"type": "concept", "content": "MYCIN (early medical ES) pioneered Certainty Factors ranging from -1 (false) to +1 (true)."},
                    {"type": "visual", "content": "graph TD\nA[\"Rule CF: 0.8\"] --> B[\"Evidence CF: 0.5\"]\nB --> C[\"Combined CF: 0.4\"]"},
                    {"type": "interactive", "content": "What did MYCIN diagnose?", "options": ["Bacterial Blood Infections", "Car Engine Faults", "Weather Patterns"], "answer": "Bacterial Blood Infections"},
                    {"type": "markdown", "content": "## The Fall and Rise\nTraditional ES fell out of favor (AI Winter) because rules were hard to maintain and didn't learn."},
                    {"type": "concept", "content": "Modern forms exist as Business Rule Engines or are augmented with Machine Learning."},
                    {"type": "visual_stepper", "content": "graph LR\nstyle M fill:#ef44441a\nM[\"Classic ES: Brittle Rules\"] --> N[\"Modern: Hybrid Systems\"] --> O[\"Rules + ML Models\"]"},
                    {"type": "code_lab", "content": "# Hybrid\nml_prediction = model.predict(data)\nif ml_prediction > 0.9 and rule_check_passes(data): take_action()"},
                    {"type": "interactive", "content": "What is the 'knowledge acquisition bottleneck'?", "options": ["Difficulty of extracting rules from experts", "Slow CPU speed", "Lack of memory"], "answer": "Difficulty of extracting rules from experts"},
                    {"type": "markdown", "content": "Summary: Expert systems evolved from brittle rule bases to modern hybrid decision systems."}
                ]
            }
        ]
    },
    "23": {
        "title": "Case 23: AI System Design",
        "modules": [
            {
                "title": "Module 1: ML Lifecycle",
                "episodes": [
                    {"type": "markdown", "content": "## The ML Lifecycle\nBuilding AI systems is more than just training a model in a Jupyter Notebook."},
                    {"type": "concept", "content": "It includes Data Collection, Feature Engineering, Training, Deployment, and Monitoring."},
                    {"type": "visual", "content": "graph LR\nA[\"Data\"] --> B[\"Train\"]\nB --> C[\"Deploy\"]\nC --> D[\"Monitor\"]\nD --> A"},
                    {"type": "interactive", "content": "Where does a Data Scientist usually spend the most time?", "options": ["Data cleaning and preparation", "Tuning hyper-parameters", "Writing deployment YAMLs"], "answer": "Data cleaning and preparation"},
                    {"type": "markdown", "content": "## MLOps\nMachine Learning Operations (MLOps) applies DevOps principles to ML systems."},
                    {"type": "concept", "content": "Goals include reproducibility, automated testing, and CI/CD for models."},
                    {"type": "visual_stepper", "content": "graph TD\nstyle M fill:#0ea5e91a\nM[\"Git Push Code/Model\"] --> N[\"Automated Testing\"] --> O[\"Automated Deployment\"]"},
                    {"type": "code_lab", "content": "# CI/CD yaml concept\nsteps:\n  - run_tests.py\n  - build_docker_image\n  - deploy_to_endpoint"},
                    {"type": "interactive", "content": "What is 'Model Drift'?", "options": ["Model accuracy degrading over time as real-world data changes", "Moving a model to a new server", "Changing the model architecture"], "answer": "Model accuracy degrading over time as real-world data changes"},
                    {"type": "markdown", "content": "Summary: System design in AI requires managing the entire lifecycle via MLOps."}
                ]
            },
            {
                "title": "Module 2: Serving Infrastructure",
                "episodes": [
                    {"type": "markdown", "content": "## Online vs Batch Serving\nHow will users consume your predictions?"},
                    {"type": "concept", "content": "Online: Predictions on-demand (e.g., fraud detection). Batch: Predictions pre-computed offline (e.g., weekly recommendations)."},
                    {"type": "visual", "content": "graph TD\nA[\"Online Serving\"] --> B[\"Low Latency / REST API\"]\nC[\"Batch Serving\"] --> D[\"High Throughput / Data Warehouse\"]"},
                    {"type": "interactive", "content": "Which serving method is appropriate for a streaming video recommendation engine on the homepage?", "options": ["Online (Real-time)", "Batch (Offline)"], "answer": "Online (Real-time)"},
                    {"type": "markdown", "content": "## Containerization\nModels are typically packaged in Docker containers to ensure environment consistency."},
                    {"type": "concept", "content": "A container holds the model weights, dependencies (e.g., PyTorch), and serving code (e.g., FastAPI)."},
                    {"type": "visual_stepper", "content": "graph LR\nstyle C fill:#10b9811a\nC[\"Model + API Code\"] --> D[\"Docker Build\"] --> E[\"Deploy on Kubernetes\"]"},
                    {"type": "code_lab", "content": "FROM python:3.9\nCOPY requirements.txt .\nRUN pip install -r requirements.txt\nCMD [\"uvicorn\", \"app:main\"]"},
                    {"type": "interactive", "content": "What tool orchestrates many containers across a cluster?", "options": ["Kubernetes", "Git", "Jupyter"], "answer": "Kubernetes"},
                    {"type": "markdown", "content": "Summary: Choose between online/batch serving and package models reliably using containers."}
                ]
            },
            {
                "title": "Module 3: Feature Stores",
                "episodes": [
                    {"type": "markdown", "content": "## The Feature Store\nA centralized repository for managing and serving ML features."},
                    {"type": "concept", "content": "Prevents training-serving skew by providing the exact same feature engineering logic to both offline training and online serving."},
                    {"type": "visual", "content": "graph TD\nA[\"Raw Data\"] --> B[\"Feature Pipeline\"]\nB --> C[\"Feature Store\"]\nC --> D[\"Training\"] & E[\"Online Serving\"]"},
                    {"type": "interactive", "content": "What is Training-Serving Skew?", "options": ["When data/features used in training differ from what is seen in production", "When models take too long to train", "When hardware differs"], "answer": "When data/features used in training differ from what is seen in production"},
                    {"type": "markdown", "content": "## Offline vs Online Features\nFeature stores often have two databases internally."},
                    {"type": "concept", "content": "Offline: Data lake for bulk historical reads. Online: Key-Value store (Redis) for low-latency point reads."},
                    {"type": "visual_stepper", "content": "graph LR\nstyle F fill:#8b5cf61a\nF[\"Feature Store\"] --> G[\"Offline (S3/Parquet)\"]\nF --> H[\"Online (Redis/DynamoDB)\"]"},
                    {"type": "code_lab", "content": "features = feature_store.get_online_features(user_id='123')\nmodel.predict(features)"},
                    {"type": "interactive", "content": "Why use Redis for online features?", "options": ["Low latency retrieval (milliseconds)", "Infinite storage capacity", "Native SQL support"], "answer": "Low latency retrieval (milliseconds)"},
                    {"type": "markdown", "content": "Summary: Feature stores decouple feature engineering from model pipelines and ensure consistency."}
                ]
            },
            {
                "title": "Module 4: Scalability and Latency",
                "episodes": [
                    {"type": "markdown", "content": "## Handling High Load\nIf your API receives 10,000 requests per second, a single Python process will crash."},
                    {"type": "concept", "content": "Horizontal Scaling: Add more server instances. Vertical Scaling: Use a bigger server/GPU."},
                    {"type": "visual", "content": "graph TD\nA[\"Load Balancer\"] --> B[\"Instance 1\"]\nA --> C[\"Instance 2\"]\nA --> D[\"Instance 3\"]"},
                    {"type": "interactive", "content": "Which scaling is generally preferred in modern cloud architectures?", "options": ["Horizontal Scaling", "Vertical Scaling"], "answer": "Horizontal Scaling"},
                    {"type": "markdown", "content": "## Model Optimization\nLarge deep learning models can be too slow or expensive for production."},
                    {"type": "concept", "content": "Quantization (FP32 to INT8), Pruning (removing weights), and Knowledge Distillation make models faster."},
                    {"type": "visual_stepper", "content": "graph LR\nstyle O fill:#f43f5e1a\nO[\"Massive FP32 Model\"] --> P[\"Quantization (INT8)\"] --> Q[\"4x Smaller, Faster Model\"]"},
                    {"type": "code_lab", "content": "import torch\nquantized_model = torch.quantization.quantize_dynamic(model)"},
                    {"type": "interactive", "content": "Does quantization generally improve accuracy?", "options": ["No, it usually trades a tiny bit of accuracy for speed", "Yes, it always improves accuracy"], "answer": "No, it usually trades a tiny bit of accuracy for speed"},
                    {"type": "markdown", "content": "Summary: Design for scale horizontally and optimize models to meet latency SLAs."}
                ]
            }
        ]
    },
    "24": {
        "title": "Case 24: Capstone & Ethics",
        "modules": [
            {
                "title": "Module 1: Comprehensive Review",
                "episodes": [
                    {"type": "markdown", "content": "## The Journey So Far\nFrom basic linear models to neural networks, trees, and reinforcement learning."},
                    {"type": "concept", "content": "Every algorithm is a tool. The hardest part of AI is formulating the problem correctly."},
                    {"type": "visual", "content": "graph TD\nA[\"Problem Formulation\"] --> B[\"Data Gathering\"]\nB --> C[\"Model Selection\"]\nC --> D[\"Evaluation\"]"},
                    {"type": "interactive", "content": "Which is generally a worse error in medical diagnosis?", "options": ["False Negative", "False Positive", "True Negative"], "answer": "False Negative"},
                    {"type": "markdown", "content": "## No Free Lunch Theorem\nThere is no single universally best machine learning algorithm."},
                    {"type": "concept", "content": "An algorithm that performs exceptionally well on one class of problems will perform poorly on another."},
                    {"type": "visual_stepper", "content": "graph LR\nstyle N fill:#eab3081a\nN[\"Dataset A: Tree Wins\"] --> O[\"Dataset B: NN Wins\"] --> P[\"No Free Lunch\"]"},
                    {"type": "code_lab", "content": "# Try multiple models\nmodels = [RandomForest(), SVC(), MLPClassifier()]\nfor m in models: m.fit(X, y)"},
                    {"type": "interactive", "content": "Because of the No Free Lunch theorem, what must a data scientist do?", "options": ["Experiment and validate different models", "Always use Deep Learning", "Give up"], "answer": "Experiment and validate different models"},
                    {"type": "markdown", "content": "Summary: Your toolkit is vast; apply the right tool to the specific context."}
                ]
            },
            {
                "title": "Module 2: AI Ethics and Bias",
                "episodes": [
                    {"type": "markdown", "content": "## Algorithmic Bias\nModels learn from data. If the data contains human biases, the model will codify and amplify them."},
                    {"type": "concept", "content": "Bias can enter through unbalanced datasets, flawed features, or historical prejudice."},
                    {"type": "visual", "content": "graph TD\nA[\"Biased Historical Data\"] --> B[\"Model Training\"]\nB --> C[\"Automated Discrimination\"]"},
                    {"type": "interactive", "content": "If a hiring AI is trained on historical data where 90% of hires were men, what will it likely learn?", "options": ["To prefer male candidates", "To ignore gender", "To prefer female candidates"], "answer": "To prefer male candidates"},
                    {"type": "markdown", "content": "## Fairness Metrics\nAccuracy is not enough. We must measure demographic parity, equal opportunity, etc."},
                    {"type": "concept", "content": "Equal opportunity ensures the True Positive Rate is the same across different demographic groups."},
                    {"type": "visual_stepper", "content": "graph TD\nstyle E fill:#ec48991a\nE[\"Train Model\"] --> F[\"Evaluate per Subgroup\"] --> G[\"Check Equal Opportunity\"]"},
                    {"type": "code_lab", "content": "from fairlearn.metrics import demographic_parity_difference\ndp_diff = demographic_parity_difference(y_true, y_pred, sensitive_features=gender)"},
                    {"type": "interactive", "content": "Can we remove bias entirely just by dropping the 'gender' or 'race' column?", "options": ["No, due to proxy variables (e.g. zip code)", "Yes"], "answer": "No, due to proxy variables (e.g. zip code)"},
                    {"type": "markdown", "content": "Summary: Actively audit models for fairness; AI is not automatically objective."}
                ]
            },
            {
                "title": "Module 3: Explainability (XAI)",
                "episodes": [
                    {"type": "markdown", "content": "## Black Box vs White Box\nModels like Deep Neural Nets are 'black boxes' (hard to interpret). Trees and Linear models are 'white boxes'."},
                    {"type": "concept", "content": "In regulated industries (finance, healthcare), you must often explain *why* a decision was made."},
                    {"type": "visual", "content": "graph TD\nA[\"Linear Model: High Interpretable\"] --> B[\"Random Forest: Medium\"]\nB --> C[\"Deep NN: Low Interpretable\"]"},
                    {"type": "interactive", "content": "Which model is natively the most interpretable?", "options": ["Decision Tree", "Deep Neural Network", "Support Vector Machine"], "answer": "Decision Tree"},
                    {"type": "markdown", "content": "## SHAP Values\nSHapley Additive exPlanations. A game-theoretic approach to explain the output of ANY machine learning model."},
                    {"type": "concept", "content": "SHAP calculates the marginal contribution of each feature to the final prediction."},
                    {"type": "visual_stepper", "content": "graph LR\nstyle S fill:#6366f11a\nS[\"Base Value (Average)\"] --> T[\"+ Age Effect\"] --> U[\"- Income Effect\"] --> V[\"Final Prediction\"]"},
                    {"type": "code_lab", "content": "import shap\nexplainer = shap.Explainer(model)\nshap_values = explainer(X)"},
                    {"type": "interactive", "content": "SHAP is considered a _____ method.", "options": ["Model-Agnostic", "Model-Specific", "Data-Agnostic"], "answer": "Model-Agnostic"},
                    {"type": "markdown", "content": "Summary: XAI tools like SHAP bridge the gap between complex models and human trust."}
                ]
            },
            {
                "title": "Module 4: Future of AI",
                "episodes": [
                    {"type": "markdown", "content": "## Foundation Models & LLMs\nLarge Language Models (like GPT) and Foundation Models have shifted the paradigm from training from scratch to fine-tuning."},
                    {"type": "concept", "content": "Self-supervised learning on massive datasets allows these models to generalize to many tasks."},
                    {"type": "visual", "content": "graph TD\nA[\"Massive Unlabeled Data\"] --> B[\"Pre-training (Next Token)\"]\nB --> C[\"Fine-Tuning (Specific Task)\"]"},
                    {"type": "interactive", "content": "What training objective is commonly used for LLM pre-training?", "options": ["Next-token prediction", "Supervised classification", "K-Means Clustering"], "answer": "Next-token prediction"},
                    {"type": "markdown", "content": "## AGI and Alignment\nArtificial General Intelligence (AGI) refers to AI that equals or surpasses human intelligence across all domains."},
                    {"type": "concept", "content": "The Alignment Problem asks: How do we ensure AGI goals remain aligned with human values?"},
                    {"type": "visual_stepper", "content": "graph TD\nstyle A fill:#22c55e1a\nA[\"Capable AI\"] --> B[\"Misaligned Goals\"] --> C[\"Catastrophe\"]\nA --> D[\"Aligned Goals\"] --> E[\"Utopia\"]"},
                    {"type": "code_lab", "content": "# The ultimate pseudo-code\nwhile AI.is_running():\n    ensure_human_alignment()"},
                    {"type": "interactive", "content": "What technique uses human feedback to align LLMs?", "options": ["RLHF (Reinforcement Learning from Human Feedback)", "CNNs", "Grid Search"], "answer": "RLHF (Reinforcement Learning from Human Feedback)"},
                    {"type": "markdown", "content": "Summary: The future is bright but requires careful stewardship of alignment, ethics, and safety."}
                ]
            }
        ]
    }
}
