CONTENT_17_24 = {
    "case_17": {
        "title": "Case 17: The Nearest Neighbor (KNN)",
        "modules": [
            {
                "title": "Episode 1: Proximity and Similarity",
                "blocks": [
                    {"type": "text", "content": "Welcome to Case 17. The city's criminal underbelly has a structure. Similar crimes cluster together."},
                    {"type": "text", "content": "You are tasked with classifying a new crime scene. Is it the work of the 'Red Hand' or the 'Blue Vipers'?"},
                    {"type": "dialogue", "speaker": "Detective Turing", "text": "We don't need a complex model, kid. We just need to see who their neighbors are. Tell me, who operates closest to this location?"},
                    {"type": "visual_stepper", "steps": [
                        {
                            "text": "Step 1: The Unknown Point",
                            "mermaid": "graph TD\n  U[\"Unknown Point\"]:::unknown\n  classDef unknown fill:#cccccc,stroke:#333,stroke-width:2px;"
                        },
                        {
                            "text": "Step 2: Identifying Neighbors",
                            "mermaid": "graph TD\n  U[\"Unknown Point\"] --> N1[\"Neighbor 1 (Red)\"]\n  U --> N2[\"Neighbor 2 (Blue)\"]\n  U --> N3[\"Neighbor 3 (Red)\"]\n  classDef unknown fill:#cccccc;\n  style N1 fill:#ff0000;\n  style N2 fill:#0000ff;\n  style N3 fill:#ff0000;"
                        },
                        {
                            "text": "Step 3: Majority Vote",
                            "mermaid": "graph TD\n  U[\"Classified as Red Point\"] --> N1[\"Neighbor 1 (Red)\"]\n  U --> N2[\"Neighbor 2 (Blue)\"]\n  U --> N3[\"Neighbor 3 (Red)\"]\n  style U fill:#ff0000;\n  style N1 fill:#ff0000;\n  style N2 fill:#0000ff;\n  style N3 fill:#ff0000;"
                        }
                    ]},
                    {"type": "text", "content": "By observing the K nearest neighbors, we can predict the nature of the unknown point."},
                    {"type": "text", "content": "But how do we define 'nearest'?"},
                    {"type": "code", "language": "python", "code": "def euclidean_distance(p1, p2):\n    return sum((a - b) ** 2 for a, b in zip(p1, p2)) ** 0.5"},
                    {"type": "text", "content": "Euclidean distance is the straight-line distance. Let's calculate the distances for our K=3 example."},
                    {"type": "interactive_prompt", "question": "If Point A is at (0, 0) and Point B is at (3, 4), what is the Euclidean distance?", "answer": "5"},
                    {"type": "text", "content": "Correct. Distance calculation is the core of the K-Nearest Neighbors algorithm."},
                    {"type": "text", "content": "However, computing distance against *every* point in the dataset can be slow for large cities."}
                ]
            },
            {
                "title": "Episode 2: Scaling the Search",
                "blocks": [
                    {"type": "text", "content": "With thousands of past crimes, checking every single one takes too long."},
                    {"type": "text", "content": "We need data structures that can query nearest neighbors efficiently, like KD-Trees."},
                    {"type": "visual_stepper", "steps": [
                        {
                            "text": "Step 1: Splitting by X-axis",
                            "mermaid": "graph TD\n  Root[\"Root (X-split)\"] --> Left1[\"Left Child\"]\n  Root --> Right1[\"Right Child\"]\n  style Root fill:#f4a261;"
                        },
                        {
                            "text": "Step 2: Splitting by Y-axis",
                            "mermaid": "graph TD\n  Root[\"Root (X-split)\"] --> Left1[\"Left Child (Y-split)\"]\n  Root --> Right1[\"Right Child (Y-split)\"]\n  Left1 --> L1_1[\"Point A\"]\n  Left1 --> L1_2[\"Point B\"]\n  style Root fill:#f4a261;\n  style Left1 fill:#2a9d8f;\n  style Right1 fill:#2a9d8f;"
                        }
                    ]},
                    {"type": "text", "content": "KD-Trees partition the space, narrowing down the search area logarithmically."},
                    {"type": "text", "content": "This brings our search time down significantly."},
                    {"type": "text", "content": "Now we are ready to predict crime hotspots in real-time."}
                ]
            }
        ]
    },
    "case_18": {
        "title": "Case 18: The Naive Assumption (Naive Bayes)",
        "modules": [
            {
                "title": "Episode 1: Probability and Evidence",
                "blocks": [
                    {"type": "text", "content": "Not all evidence is conclusive. Some evidence just shifts our belief."},
                    {"type": "text", "content": "We have an encrypted message. Is it 'Spam' from the Syndicate or 'Ham' from a civilian?"},
                    {"type": "text", "content": "We use Bayes' Theorem to update our probabilities as we see words like 'urgent', 'cash', or 'family'."},
                    {"type": "visual_stepper", "steps": [
                        {
                            "text": "Step 1: Prior Probability",
                            "mermaid": "graph LR\n  P_Spam[\"P(Spam) = 0.4\"]\n  P_Ham[\"P(Ham) = 0.6\"]\n  style P_Spam fill:#e76f51;\n  style P_Ham fill:#2a9d8f;"
                        },
                        {
                            "text": "Step 2: Likelihood of evidence 'Urgent'",
                            "mermaid": "graph LR\n  Spam[\"Spam\"] -->|P('Urgent'|Spam) = 0.8| Ev1[\"Word: 'Urgent'\"]\n  Ham[\"Ham\"] -->|P('Urgent'|Ham) = 0.1| Ev1\n  style Spam fill:#e76f51;\n  style Ham fill:#2a9d8f;\n  style Ev1 fill:#e9c46a;"
                        },
                        {
                            "text": "Step 3: Posterior Probability (Updating Belief)",
                            "mermaid": "graph LR\n  Ev1[\"Word: 'Urgent'\"] --> P_Spam_Given_Ev[\"P(Spam|'Urgent') > P(Ham|'Urgent')\"]\n  style P_Spam_Given_Ev fill:#e76f51;"
                        }
                    ]},
                    {"type": "text", "content": "But why is it called the 'Naive' assumption?"},
                    {"type": "text", "content": "Because it assumes every piece of evidence (every word) is independent of the others."},
                    {"type": "text", "content": "In reality, 'urgent' and 'cash' often appear together, but Naive Bayes treats their probabilities as independent multipliers."}
                ]
            }
        ]
    },
    "case_19": {
        "title": "Case 19: The Tree That Makes Decisions (Decision Trees)",
        "modules": [
            {
                "title": "Episode 1: Splitting the Truth",
                "blocks": [
                    {"type": "text", "content": "Sometimes you just need a flowchart of yes/no questions to reach a conclusion."},
                    {"type": "text", "content": "We are classifying suspects. What is the best question to ask first?"},
                    {"type": "text", "content": "We want to ask the question that reduces uncertainty (entropy) the most."},
                    {"type": "visual_stepper", "steps": [
                        {
                            "text": "Step 1: High Entropy (Mixed Group)",
                            "mermaid": "graph TD\n  Root[\"Suspects: 5 Guilty, 5 Innocent\"]\n  style Root fill:#e9c46a;"
                        },
                        {
                            "text": "Step 2: Best Split (Alibi Check)",
                            "mermaid": "graph TD\n  Root[\"Suspects: 5 Guilty, 5 Innocent\"] -->|Has Alibi? Yes| Left[\"1 Guilty, 5 Innocent\"]\n  Root -->|Has Alibi? No| Right[\"4 Guilty, 0 Innocent\"]\n  style Left fill:#2a9d8f;\n  style Right fill:#e76f51;"
                        },
                        {
                            "text": "Step 3: Leaf Node",
                            "mermaid": "graph TD\n  Right[\"4 Guilty, 0 Innocent\"] --> Decision[\"Decision: Likely Guilty\"]\n  style Right fill:#e76f51;\n  style Decision fill:#e76f51;"
                        }
                    ]},
                    {"type": "text", "content": "The Information Gain measures the drop in entropy after the split."}
                ]
            }
        ]
    },
    "case_20": {
        "title": "Case 20: The Agent That Learns From Failure (Q-Learning)",
        "modules": [
            {
                "title": "Episode 1: Navigating the Grid",
                "blocks": [
                    {"type": "text", "content": "Our drone needs to navigate an underground maze with traps and rewards."},
                    {"type": "text", "content": "We use Reinforcement Learning. The drone learns the 'quality' (Q-value) of actions in different states."},
                    {"type": "text", "content": "The Bellman Equation helps update these Q-values based on immediate rewards and future expected rewards."},
                    {"type": "visual_stepper", "steps": [
                        {
                            "text": "Step 1: Initial State",
                            "mermaid": "graph LR\n  S1[\"State 1\"] -->|Action: Right| S2[\"State 2 (Unknown)\"]\n  style S1 fill:#264653;\n  style S2 fill:#2a9d8f;"
                        },
                        {
                            "text": "Step 2: Receiving Reward",
                            "mermaid": "graph LR\n  S1[\"State 1\"] -->|Action: Right| S2[\"State 2\"]\n  S2 --> Reward[\"Reward: +10\"]\n  style S2 fill:#2a9d8f;\n  style Reward fill:#e9c46a;"
                        },
                        {
                            "text": "Step 3: Q-Value Update",
                            "mermaid": "graph TD\n  Update[\"Q(S1, Right) = Q(S1, Right) + alpha * (Reward + gamma * Max(Q(S2, a)) - Q(S1, Right))\"]\n  style Update fill:#f4a261;"
                        }
                    ]},
                    {"type": "text", "content": "Exploration vs Exploitation is the key dilemma: Should the drone try unknown paths, or stick to the known good paths?"}
                ]
            }
        ]
    },
    "case_21": {
        "title": "Case 21: The Logic Programmer (PROLOG)",
        "modules": [
            {
                "title": "Episode 1: Facts and Rules",
                "blocks": [
                    {"type": "text", "content": "Before Neural Networks, AI was heavily based on symbolic logic and rules."},
                    {"type": "text", "content": "We use Prolog to define a knowledge base of facts and infer new truths."},
                    {"type": "code", "language": "prolog", "code": "parent(john, mary).\nparent(mary, susan).\ngrandparent(X, Y) :- parent(X, Z), parent(Z, Y)."},
                    {"type": "visual_stepper", "steps": [
                        {
                            "text": "Step 1: Query",
                            "mermaid": "graph TD\n  Q[\"?- grandparent(john, susan).\"]\n  style Q fill:#2a9d8f;"
                        },
                        {
                            "text": "Step 2: Unification",
                            "mermaid": "graph TD\n  Rule[\"grandparent(X, Y) :- parent(X, Z), parent(Z, Y)\"]\n  Match[\"X=john, Y=susan\"]\n  Rule --> Match\n  style Rule fill:#e9c46a;\n  style Match fill:#f4a261;"
                        },
                        {
                            "text": "Step 3: Resolution",
                            "mermaid": "graph TD\n  SubGoal1[\"parent(john, mary)\"] --> SubGoal2[\"parent(mary, susan)\"]\n  SubGoal2 --> Success[\"True!\"]\n  style SubGoal1 fill:#2a9d8f;\n  style SubGoal2 fill:#2a9d8f;\n  style Success fill:#e9c46a;"
                        }
                    ]}
                ]
            }
        ]
    },
    "case_22": {
        "title": "Case 22: The Expert in the Box (Expert Systems)",
        "modules": [
            {
                "title": "Episode 1: Knowledge Engineering",
                "blocks": [
                    {"type": "text", "content": "We extract the knowledge from human experts and encode it into inference engines."},
                    {"type": "text", "content": "This involves a Knowledge Base and an Inference Engine (Forward or Backward Chaining)."},
                    {"type": "visual_stepper", "steps": [
                        {
                            "text": "Step 1: User Input",
                            "mermaid": "graph LR\n  User[\"Symptoms: Fever, Cough\"]\n  style User fill:#e76f51;"
                        },
                        {
                            "text": "Step 2: Forward Chaining",
                            "mermaid": "graph LR\n  Rule1[\"IF Fever AND Cough THEN Rule_Out(Allergy)\"]\n  Rule2[\"IF Fever AND Cough THEN Suspect(Flu)\"]\n  style Rule1 fill:#2a9d8f;\n  style Rule2 fill:#2a9d8f;"
                        },
                        {
                            "text": "Step 3: Conclusion",
                            "mermaid": "graph TD\n  Sys[\"Expert System output: High probability of Flu.\"]\n  style Sys fill:#e9c46a;"
                        }
                    ]}
                ]
            }
        ]
    },
    "case_23": {
        "title": "Case 23: The Intelligence Architect (System Design)",
        "modules": [
            {
                "title": "Episode 1: Scaling AI",
                "blocks": [
                    {"type": "text", "content": "Building a model is only 10% of the work. Deploying and scaling it is the other 90%."},
                    {"type": "text", "content": "We need to design a system that handles streaming data, model versioning, and low latency."},
                    {"type": "visual_stepper", "steps": [
                        {
                            "text": "Step 1: Data Ingestion",
                            "mermaid": "graph LR\n  App[\"Client App\"] --> API[\"API Gateway\"]\n  API --> Kafka[\"Kafka Stream\"]\n  style App fill:#264653;\n  style Kafka fill:#e76f51;"
                        },
                        {
                            "text": "Step 2: Model Inference",
                            "mermaid": "graph LR\n  Kafka[\"Kafka Stream\"] --> Model[\"TensorFlow Serving\"]\n  Model --> DB[\"PostgreSQL\"]\n  style Kafka fill:#e76f51;\n  style Model fill:#2a9d8f;\n  style DB fill:#f4a261;"
                        }
                    ]}
                ]
            }
        ]
    },
    "case_24": {
        "title": "Case 24: The Final AI (Capstone)",
        "modules": [
            {
                "title": "Episode 1: The Master Controller",
                "blocks": [
                    {"type": "text", "content": "You have mastered all the algorithms. Now you must build the Ultimate Agent."},
                    {"type": "text", "content": "This agent combines Search, Probability, Neural Networks, and Logic."},
                    {"type": "visual_stepper", "steps": [
                        {
                            "text": "Step 1: Perception",
                            "mermaid": "graph TD\n  Sensors[\"Raw Data\"] --> CNN[\"Vision Model\"]\n  CNN --> Entities[\"Identified Entities\"]\n  style Sensors fill:#e9c46a;\n  style CNN fill:#2a9d8f;"
                        },
                        {
                            "text": "Step 2: Reasoning",
                            "mermaid": "graph TD\n  Entities[\"Identified Entities\"] --> RuleEngine[\"Logic Rules\"]\n  RuleEngine --> QAgent[\"Q-Learning Policy\"]\n  style Entities fill:#2a9d8f;\n  style QAgent fill:#e76f51;"
                        },
                        {
                            "text": "Step 3: Action",
                            "mermaid": "graph TD\n  QAgent[\"Optimal Policy\"] --> Actuators[\"Execute Move\"]\n  style Actuators fill:#f4a261;"
                        }
                    ]},
                    {"type": "text", "content": "Congratulations on completing the AI Story Lab!"}
                ]
            }
        ]
    }
}
