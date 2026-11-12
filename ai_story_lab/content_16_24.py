CONTENT_16_24 = {
    "16": {
        "episodes": [
            {
                "title": "Episode 1: The Machine That Learns",
                "blocks": [
                    {
                        "type": "objective",
                        "content": "Understand the core concept of Machine Learning by building a simple Linear Regressor from scratch using Gradient Descent."
                    },
                    {
                        "type": "problem",
                        "content": "You are given a set of 1D points (x, y). You need to find the best line (y = mx + c) that fits the data. Can you implement the gradient descent algorithm to update m and c iteratively?"
                    },
                    {
                        "type": "concept",
                        "content": "Gradient Descent is an optimization algorithm used to minimize a function by iteratively moving in the direction of steepest descent as defined by the negative of the gradient. In Machine Learning, we use it to update the parameters of our model to minimize the loss function."
                    },
                    {
                        "type": "visual",
                        "content": "graph LR\n    A[Initialize m, c] --> B[Calculate Predictions]\n    B --> C[Calculate Error Loss]\n    C --> D[Calculate Gradients]\n    D --> E[Update m, c]\n    E --> B"
                    },
                    {
                        "type": "code_lab",
                        "starter_code": "def gradient_descent(x, y, m, c, learning_rate, iterations):\n    # TODO: Implement gradient descent for a simple linear regression\n    return m, c",
                        "solution_code": "def gradient_descent(x, y, m, c, learning_rate, iterations):\n    n = len(x)\n    for _ in range(iterations):\n        y_pred = [m * xi + c for xi in x]\n        D_m = (-2/n) * sum([xi * (yi - y_predi) for xi, yi, y_predi in zip(x, y, y_pred)])\n        D_c = (-2/n) * sum([yi - y_predi for yi, y_predi in zip(y, y_pred)])\n        m = m - learning_rate * D_m\n        c = c - learning_rate * D_c\n    return round(m, 2), round(c, 2)",
                        "expected_output": "(2.0, 1.0)",
                        "explanation": "We calculate the gradients with respect to m and c, and update them using the learning rate. This minimizes the Mean Squared Error over iterations.",
                        "test_cases": [
                            {"input": "[1, 2, 3], [3, 5, 7], 0, 0, 0.01, 1000", "expected": "(2.0, 1.0)"}
                        ]
                    }
                ]
            }
        ]
    },
    "17": {
        "episodes": [
            {
                "title": "Episode 1: The Nearest Neighbor",
                "blocks": [
                    {
                        "type": "objective",
                        "content": "Implement the K-Nearest Neighbors (KNN) algorithm from scratch to classify a new data point."
                    },
                    {
                        "type": "problem",
                        "content": "Given a set of points and their labels, find the majority label among the K closest points to a new given point."
                    },
                    {
                        "type": "concept",
                        "content": "KNN is a lazy learning algorithm that stores all available cases and classifies new cases based on a similarity measure (e.g., Euclidean distance)."
                    },
                    {
                        "type": "code_lab",
                        "starter_code": "def knn(data, new_point, k):\n    # data is a list of tuples: (point_coords, label)\n    # TODO: Implement KNN to return the predicted label\n    pass",
                        "solution_code": "def knn(data, new_point, k):\n    def euclidean_distance(p1, p2):\n        return sum((x - y) ** 2 for x, y in zip(p1, p2)) ** 0.5\n    \n    distances = []\n    for point, label in data:\n        dist = euclidean_distance(point, new_point)\n        distances.append((dist, label))\n    \n    distances.sort(key=lambda x: x[0])\n    k_nearest = distances[:k]\n    labels = [label for _, label in k_nearest]\n    return max(set(labels), key=labels.count)",
                        "expected_output": "'A'",
                        "explanation": "Calculates Euclidean distance from the new point to all points in the dataset, sorts them, selects the top K nearest points, and finds the most frequent label.",
                        "test_cases": [
                            {"input": "([([1, 1], 'A'), ([2, 2], 'A'), ([8, 8], 'B'), ([9, 9], 'B')], [3, 3], 3)", "expected": "'A'"}
                        ]
                    }
                ]
            }
        ]
    },
    "18": {
        "episodes": [
            {
                "title": "Episode 1: The Naive Assumption",
                "blocks": [
                    {
                        "type": "objective",
                        "content": "Build a simple Naive Bayes classifier from scratch using basic probability."
                    },
                    {
                        "type": "code_lab",
                        "starter_code": "def naive_bayes(training_data, new_doc):\n    # training_data: list of (doc_words_list, class_label)\n    # new_doc: list of words\n    # TODO: Predict class label for new_doc\n    pass",
                        "solution_code": "def naive_bayes(training_data, new_doc):\n    classes = {}\n    vocab = set()\n    for doc, label in training_data:\n        if label not in classes:\n            classes[label] = {'count': 0, 'words': {}}\n        classes[label]['count'] += 1\n        for word in doc:\n            vocab.add(word)\n            classes[label]['words'][word] = classes[label]['words'].get(word, 0) + 1\n    \n    total_docs = len(training_data)\n    best_class = None\n    max_prob = -1\n    \n    for label, data in classes.items():\n        prob = data['count'] / total_docs\n        total_words = sum(data['words'].values())\n        for word in new_doc:\n            word_count = data['words'].get(word, 0)\n            # Laplace smoothing\n            word_prob = (word_count + 1) / (total_words + len(vocab))\n            prob *= word_prob\n        if prob > max_prob:\n            max_prob = prob\n            best_class = label\n            \n    return best_class",
                        "expected_output": "'spam'",
                        "explanation": "Uses Bayes theorem with Laplace smoothing and the naive assumption of conditional independence between features given the class.",
                        "test_cases": [
                            {"input": "([(['buy', 'viagra'], 'spam'), (['hello', 'friend'], 'ham')], ['buy'])", "expected": "'spam'"}
                        ]
                    }
                ]
            }
        ]
    },
    "19": {
        "episodes": [
            {
                "title": "Episode 1: The Tree That Makes Decisions",
                "blocks": [
                    {
                        "type": "objective",
                        "content": "Understand Gini Impurity to select the best split in a Decision Tree."
                    },
                    {
                        "type": "code_lab",
                        "starter_code": "def gini_impurity(labels):\n    # TODO: Calculate Gini Impurity for a list of labels\n    pass",
                        "solution_code": "def gini_impurity(labels):\n    if not labels:\n        return 0.0\n    counts = {}\n    for label in labels:\n        counts[label] = counts.get(label, 0) + 1\n    impurity = 1.0\n    for label in counts:\n        prob = counts[label] / len(labels)\n        impurity -= prob ** 2\n    return round(impurity, 3)",
                        "expected_output": "0.5",
                        "explanation": "Gini Impurity measures how often a randomly chosen element would be incorrectly labeled. It is 1 - sum(p_i^2).",
                        "test_cases": [
                            {"input": "['A', 'A', 'B', 'B']", "expected": "0.5"},
                            {"input": "['A', 'A', 'A']", "expected": "0.0"}
                        ]
                    }
                ]
            }
        ]
    },
    "20": {
        "episodes": [
            {
                "title": "Episode 1: The Agent That Learns From Failure",
                "blocks": [
                    {
                        "type": "objective",
                        "content": "Implement a simple Q-Learning update rule."
                    },
                    {
                        "type": "code_lab",
                        "starter_code": "def update_q_value(q_table, state, action, reward, next_state, alpha, gamma):\n    # TODO: Update the Q-value for the given state and action\n    # q_table is a dict of dicts: q_table[state][action] = value\n    pass",
                        "solution_code": "def update_q_value(q_table, state, action, reward, next_state, alpha, gamma):\n    current_q = q_table.get(state, {}).get(action, 0.0)\n    next_max_q = max(q_table.get(next_state, {0: 0.0}).values()) if next_state in q_table else 0.0\n    new_q = current_q + alpha * (reward + gamma * next_max_q - current_q)\n    \n    if state not in q_table:\n        q_table[state] = {}\n    q_table[state][action] = round(new_q, 2)\n    return q_table",
                        "expected_output": "{'s1': {'a1': 0.5}}",
                        "explanation": "The Q-Learning update formula: Q(s,a) = Q(s,a) + alpha * (R + gamma * max Q(s',a') - Q(s,a)).",
                        "test_cases": [
                            {"input": "({}, 's1', 'a1', 10, 's2', 0.1, 0.9)", "expected": "{'s1': {'a1': 1.0}}"}
                        ]
                    }
                ]
            }
        ]
    },
    "21": {
        "episodes": [
            {
                "title": "Episode 1: The Logic Programmer",
                "blocks": [
                    {
                        "type": "objective",
                        "content": "Build a minimal logic reasoning engine conceptually similar to PROLOG in Python."
                    },
                    {
                        "type": "code_lab",
                        "starter_code": "def query_logic(facts, rules, query):\n    # facts: list of knowns like 'A', 'B'\n    # rules: dict of {consequent: [antecedent1, antecedent2]}\n    # TODO: Return True if query can be proven, False otherwise\n    pass",
                        "solution_code": "def query_logic(facts, rules, query):\n    known = set(facts)\n    added = True\n    while added:\n        added = False\n        for consequent, antecedents in rules.items():\n            if consequent not in known:\n                if all(a in known for a in antecedents):\n                    known.add(consequent)\n                    added = True\n    return query in known",
                        "expected_output": "True",
                        "explanation": "Uses forward chaining to continually apply rules until no new facts can be deduced, then checks if the query is in the known facts.",
                        "test_cases": [
                            {"input": "(['raining'], {'wet_grass': ['raining']}, 'wet_grass')", "expected": "True"}
                        ]
                    }
                ]
            }
        ]
    },
    "22": {
        "episodes": [
            {
                "title": "Episode 1: The Expert in the Box",
                "blocks": [
                    {
                        "type": "objective",
                        "content": "Create a rule-based Expert System."
                    },
                    {
                        "type": "code_lab",
                        "starter_code": "def expert_system(symptoms):\n    # Returns the most likely disease based on symptoms\n    pass",
                        "solution_code": "def expert_system(symptoms):\n    knowledge_base = {\n        'Flu': {'fever', 'cough', 'fatigue'},\n        'Cold': {'cough', 'sneezing', 'runny_nose'},\n        'Allergy': {'sneezing', 'itchy_eyes'}\n    }\n    \n    best_match = None\n    max_overlap = -1\n    symptoms_set = set(symptoms)\n    \n    for disease, disease_symptoms in knowledge_base.items():\n        overlap = len(symptoms_set.intersection(disease_symptoms))\n        if overlap > max_overlap:\n            max_overlap = overlap\n            best_match = disease\n            \n    return best_match if max_overlap > 0 else 'Unknown'",
                        "expected_output": "'Cold'",
                        "explanation": "Calculates the intersection between user symptoms and knowledge base symptoms to find the best match.",
                        "test_cases": [
                            {"input": "['cough', 'sneezing']", "expected": "'Cold'"}
                        ]
                    }
                ]
            }
        ]
    },
    "23": {
        "episodes": [
            {
                "title": "Episode 1: The Intelligence Architect",
                "blocks": [
                    {
                        "type": "objective",
                        "content": "Design an AI system pipeline by writing a simple message router."
                    },
                    {
                        "type": "code_lab",
                        "starter_code": "def route_request(request_text):\n    # Route to 'vision', 'nlp', or 'fallback'\n    pass",
                        "solution_code": "def route_request(request_text):\n    text = request_text.lower()\n    vision_keywords = ['image', 'photo', 'picture', 'see']\n    nlp_keywords = ['text', 'translate', 'summarize', 'read']\n    \n    vision_score = sum(1 for w in vision_keywords if w in text)\n    nlp_score = sum(1 for w in nlp_keywords if w in text)\n    \n    if vision_score > nlp_score:\n        return 'vision'\n    elif nlp_score > vision_score:\n        return 'nlp'\n    else:\n        return 'fallback'",
                        "expected_output": "'vision'",
                        "explanation": "A simple heuristic-based router to delegate requests to specialized AI subsystems based on keyword frequency.",
                        "test_cases": [
                            {"input": "'analyze this photo'", "expected": "'vision'"}
                        ]
                    }
                ]
            }
        ]
    },
    "24": {
        "episodes": [
            {
                "title": "Episode 1: The Final AI",
                "blocks": [
                    {
                        "type": "objective",
                        "content": "The NEXUS Capstone: Build an ensemble model combining outputs from multiple simple models."
                    },
                    {
                        "type": "code_lab",
                        "starter_code": "def ensemble_predict(model_outputs):\n    # model_outputs is a list of predicted labels (strings)\n    # Return the final prediction using hard voting\n    pass",
                        "solution_code": "def ensemble_predict(model_outputs):\n    counts = {}\n    for out in model_outputs:\n        counts[out] = counts.get(out, 0) + 1\n    \n    return max(counts, key=counts.get)",
                        "expected_output": "'ClassA'",
                        "explanation": "Aggregates the predictions of multiple distinct models and selects the majority vote (Hard Voting).",
                        "test_cases": [
                            {"input": "['ClassA', 'ClassB', 'ClassA']", "expected": "'ClassA'"}
                        ]
                    }
                ]
            }
        ]
    }
}
