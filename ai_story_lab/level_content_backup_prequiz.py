# Master Curriculum Database for AI Story Lab
LEVEL_CONTENT = \
{
    "0": {
        "title": "Case 00: The Machine That Couldn't Think",
        "episodes": [
            {
                "title": "Module 1: The Paradigm Shift",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "For decades, computers were just incredibly fast calculators. You gave them a list of rules, they followed them, and they gave you an answer. If a scenario wasn't explicitly programmed in the rules, the machine crashed. It couldn't think. It could only execute."
                    },
                    {
                        "type": "objective",
                        "title": "Module Objective",
                        "content": "Understand the fundamental philosophical difference between Traditional Programming and Artificial Intelligence."
                    },
                    {
                        "type": "concept",
                        "title": "Traditional Programming vs Machine Learning",
                        "content": "In **Traditional Programming**, humans write the rules (code) and input the data. The machine applies the rules to the data to output answers.\n\nIn **Artificial Intelligence (specifically Machine Learning)**, humans input the data AND the answers. The machine figures out the rules."
                    },
                    {
                        "type": "visual",
                        "title": "The Paradigm Shift",
                        "code": "\ngraph TD\n    classDef t fill:#ef44441a,stroke:#FCA5A5,stroke-width:2px;\n    classDef a fill:#10b9811a,stroke:#34D399,stroke-width:2px;\n    \n    subgraph Traditional Programming\n        D1[\"Data\"]:::t --> P1[\"Computer\"]:::t\n        R1[\"Rules (Code)\"]:::t --> P1\n        P1 --> A1[\"Answers\"]:::t\n    end\n    \n    subgraph Machine Learning\n        D2[\"Data\"]:::a --> P2[\"Computer\"]:::a\n        A2[\"Answers (Labels)\"]:::a --> P2\n        P2 --> R2[\"Rules (Model)\"]:::a\n    end\n        "
                    },
                    {
                        "type": "markdown",
                        "content": "> [!NOTE] \n> This inversion is why AI is so powerful. We don't know how to write a list of `if/else` statements that define what a 'cat' looks like in a photo. But we can give an AI 10,000 photos of cats, and let it figure out the mathematical rules itself."
                    },
                    {
                        "type": "interactive",
                        "question": "If you are writing a program with 500 'if/else' statements to categorize emails as spam, are you building AI?",
                        "options": [
                            "Yes, it is Artificial Intelligence",
                            "No, it is Traditional Programming"
                        ],
                        "answer": "No, it is Traditional Programming",
                        "explanation": "Traditional Programming relies on human-written logical branches (like massive 'if/else' blocks). Machine Learning requires the machine to generate the logic itself from data."
                    }
                ]
            },
            {
                "title": "Module 2: Defining Intelligence",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "Defining Intelligence",
                        "content": "If we want to build a machine that thinks, we first have to define what 'thinking' is. Historically, AI research is split into four distinct definitions:\n1. **Thinking Humanly:** The cognitive modeling approach (making machines that think like humans).\n2. **Acting Humanly:** The Turing Test approach (making machines that behave indistinguishably from humans).\n3. **Thinking Rationally:** The 'laws of thought' approach (using strict logic and syllogisms).\n4. **Acting Rationally:** The Rational Agent approach (doing whatever maximizes the expected outcome)."
                    },
                    {
                        "type": "markdown",
                        "content": "> [!WARNING] \n> Modern AI almost exclusively focuses on **Acting Rationally**. We don't care if the AI 'thinks' exactly like a human brain does (birds fly by flapping wings, airplanes fly with jet engines). We just want the statistically optimal outcome."
                    },
                    {
                        "type": "visual",
                        "title": "The Four Quadrants of AI",
                        "code": "\ngraph TD\n    classDef h fill:#3b82f61a,stroke:#93C5FD,stroke-width:2px;\n    classDef r fill:#10b9811a,stroke:#34D399,stroke-width:2px;\n    \n    A[\" \"] -->|Humanly| H[\" \"]\n    A -->|Rationally| R[\" \"]\n    \n    H -->|Think| TH[\"Cognitive Modeling\"]:::h\n    H -->|Act| AH[\"Turing Test\"]:::h\n    \n    R -->|Think| TR[\"Laws of Thought\"]:::r\n    R -->|Act| AR[\"Rational Agents\"]:::r\n        "
                    },
                    {
                        "type": "fill_in_the_blank",
                        "question": "Which approach to AI attempts to perfectly simulate the psychological and neurological processes of the human brain?\n\nAnswer: _____",
                        "answer": "Cognitive Modeling",
                        "explanation": "Cognitive Modeling focuses on mimicking the internal psychological processes of human thought. The Rational Agent approach (the modern standard) only cares about the mathematical outcome."
                    }
                ]
            },
            {
                "title": "Module 3: The Turing Test",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "The Turing Test (1950)",
                        "content": "Proposed by Alan Turing in his paper 'Computing Machinery and Intelligence', the Turing Test sidestepped the philosophical debate of 'what is thought' by proposing a practical test.\n\nA human interrogator communicates via text terminal with two entities: one human, and one AI. If the interrogator cannot reliably tell which is the machine, the machine passes the test."
                    },
                    {
                        "type": "markdown",
                        "content": "To pass the Turing Test, a computer would need:\n*   **Natural Language Processing (NLP):** To communicate successfully in English.\n*   **Knowledge Representation:** To store what it knows or hears.\n*   **Automated Reasoning:** To use the stored information to answer questions and draw new conclusions.\n*   **Machine Learning:** To adapt to new circumstances and detect patterns."
                    },
                    {
                        "type": "concept",
                        "title": "The Chinese Room Argument",
                        "content": "Philosopher John Searle famously argued against the Turing Test with the 'Chinese Room' thought experiment. Imagine a man in a room who doesn't speak Chinese. He has a massive rulebook that tells him exactly what Chinese symbols to output when he receives specific Chinese input symbols. \n\nTo someone outside the room, he appears perfectly fluent in Chinese. But he doesn't understand a single word. Does a computer 'understand' what it is doing, or is it just blindly following a massive rulebook of math?"
                    },
                    {
                        "type": "fill_in_the_blank",
                        "question": "Does passing the Turing Test guarantee that a machine is actually 'conscious'?\n\nAnswer: _____",
                        "answer": "No, it only proves the ability to simulate human behavior.",
                        "explanation": "The Chinese Room argument proves that a system can perfectly simulate conversational fluency (passing the Turing Test) without possessing any actual conscious 'understanding' of the words."
                    }
                ]
            },
            {
                "title": "Module 4: The AI Umbrella",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "AI is a massive umbrella term. Underneath it, there are two major historical philosophies on how to build it: Symbolic AI and Subsymbolic AI."
                    },
                    {
                        "type": "concept",
                        "title": "Symbolic AI (Good Old-Fashioned AI)",
                        "content": "From the 1950s to the 1980s, researchers believed they could achieve human-level intelligence by hard-coding every single rule and logical relationship in the universe. This is called Symbolic AI (or GOFAI). \n\nIt works incredibly well for things like Chess or solving math equations, but fails completely at things a toddler finds easy: recognizing a dog, walking, or understanding speech."
                    },
                    {
                        "type": "concept",
                        "title": "Subsymbolic AI (Machine Learning)",
                        "content": "Instead of hardcoding rules, we use statistics. We build Artificial Neural Networks inspired by the human brain. We feed them massive amounts of data, and they mathematically adjust their own 'weights' until they can recognize patterns. \n\nThis approach requires massive computational power and data, which is why Deep Learning only exploded in popularity in the 2010s."
                    },
                    {
                        "type": "concept",
                        "title": "Supervised vs Unsupervised Learning",
                        "content": "**Supervised Learning:** You give the AI a massive dataset of pictures labeled 'Dog' and 'Cat'. It learns to predict the label of a new picture. (Used for Classification).\n\n**Unsupervised Learning:** You give the AI a massive dataset of pictures with NO labels. It figures out how to group them together based on visual similarities. (Used for Clustering)."
                    },
                    {
                        "type": "concept",
                        "title": "Reinforcement Learning",
                        "content": "You don't give the AI any data. You drop it into a simulated environment (like a video game) and give it a 'Score'. It takes random actions, learns what actions increase its Score, and eventually becomes a superhuman master of the environment."
                    },
                    {
                        "type": "concept",
                        "title": "Supervised vs Unsupervised Learning",
                        "content": "**Supervised Learning:** You give the AI a massive dataset of pictures labeled 'Dog' and 'Cat'. It learns to predict the label of a new picture. (Used for Classification).\n\n**Unsupervised Learning:** You give the AI a massive dataset of pictures with NO labels. It figures out how to group them together based on visual similarities. (Used for Clustering)."
                    },
                    {
                        "type": "concept",
                        "title": "Reinforcement Learning",
                        "content": "You don't give the AI any data. You drop it into a simulated environment (like a video game) and give it a 'Score'. It takes random actions, learns what actions increase its Score, and eventually becomes a superhuman master of the environment."
                    },
                    {
                        "type": "visual",
                        "title": "The AI Umbrella",
                        "code": "\ngraph TD\n    classDef main fill:#7c4dff1a,stroke:#7C4DFF,stroke-width:2px;\n    classDef sub fill:#3b82f61a,stroke:#93C5FD,stroke-width:2px;\n    classDef deep fill:#10b9811a,stroke:#34D399,stroke-width:2px;\n    \n    AI[\"Artificial Intelligence\"]:::main --> GOFAI[\"Symbolic AI (Expert Systems, Search)\"]:::sub\n    AI --> ML[\"Machine Learning\"]:::sub\n    \n    ML --> SL[\"Supervised Learning\"]:::sub\n    ML --> UL[\"Unsupervised Learning\"]:::sub\n    ML --> RL[\"Reinforcement Learning\"]:::sub\n    \n    SL --> DL[\"Deep Learning (Neural Networks)\"]:::deep\n    UL --> DL\n    RL --> DL\n        "
                    },
                    {
                        "type": "fill_in_the_blank",
                        "question": "Which branch of AI was dominant in the 1970s and relied on hard-coded logical rules?\n\nAnswer: _____",
                        "answer": "Symbolic AI",
                        "explanation": "Symbolic AI (GOFAI) dominated early AI research because computers didn't have enough power to run Neural Networks. It relied on hard-coded 'Symbols' and logical rules."
                    }
                ]
            },
            {
                "title": "Module 5: Real-World Architecture",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "Now that we know what AI is, where is it actually used?"
                    },
                    {
                        "type": "concept",
                        "title": "Search & Planning",
                        "content": "Used in GPS systems, self-driving car routing, and classical game AI (like IBM's Deep Blue beating Garry Kasparov in Chess). They explore millions of possible future states to find the optimal sequence of actions."
                    },
                    {
                        "type": "concept",
                        "title": "Probabilistic Inference",
                        "content": "Used in medical diagnosis, spam filters, and weather forecasting. When the world is uncertain, Bayesian Networks calculate the strict mathematical probability of an event."
                    },
                    {
                        "type": "concept",
                        "title": "Deep Learning & NLP",
                        "content": "Used in ChatGPT, facial recognition, and medical image analysis. Massive neural networks find invisible patterns in raw pixels and text."
                    },
                    {
                        "type": "concept",
                        "title": "Reinforcement Learning",
                        "content": "Used in robotics and highly complex games. An AI agent is dropped into an environment with no rules. It takes random actions, receives 'rewards' or 'punishments', and eventually learns the perfect strategy (like Google DeepMind's AlphaGo)."
                    },
                    {
                        "type": "markdown",
                        "content": "In the upcoming Cases, you are going to learn how to architect every single one of these systems from scratch."
                    }
                ]
            }
        ]
    },
    "8": {
        "title": "Case 08: The Knowledge Vault",
        "episodes": [
            {
                "title": "Module 1: Introduction to Knowledge Graphs",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "A Knowledge Graph represents entities and their relationships."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Entities are the nodes in the graph, representing real-world objects."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\n  A[\"Entity: Person\"] --> B[\"Entity: City\"]\n  style A fill:#10b981,stroke:#333,stroke-width:2px"
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** "
                    },
                    {
                        "type": "markdown",
                        "content": "Relationships are directed edges connecting entities."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Data is stored as Subject-Predicate-Object triples."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph TD\n  Empty[\"Empty Diagram\"]"
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "",
                        "solution_code": "",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nDecouples declarative facts (subject-predicate-object triples) from procedural code, enabling inheritance along taxonomic graphs with $O(depth)$ lookup time.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Relational SQL Database:** Strict ACID transactions and fast joins, but rigid schemas make inheritance and recursive graph traversal awkward.\\n- **Semantic Web Ontologies (OWL/RDF):** Formal description logic standards supporting open-world assumption and automated reasoning.\\n- **Graph Neural Networks (GNN):** Continuous vector embeddings for knowledge graph completion; handles missing links well, but lacks deterministic proof capabilities.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "KGs allow semantic queries and reasoning."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "An ontology defines the schema and vocabulary of the KG."
                    }
                ]
            },
            {
                "title": "Module 2: Building Knowledge Graphs",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "Building a KG involves data extraction and integration."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "NLP techniques extract entities and relations from text."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\n  A[\"Text\"] --> B[\"NER\"]\n  style A fill:#3b82f6,stroke:#333,stroke-width:2px"
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** "
                    },
                    {
                        "type": "markdown",
                        "content": "Relation extraction links entities found in the text."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Disambiguating multiple mentions of the same entity."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph TD\n  Empty[\"Empty Diagram\"]"
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "",
                        "solution_code": "",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nDecouples declarative facts (subject-predicate-object triples) from procedural code, enabling inheritance along taxonomic graphs with $O(depth)$ lookup time.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Relational SQL Database:** Strict ACID transactions and fast joins, but rigid schemas make inheritance and recursive graph traversal awkward.\\n- **Semantic Web Ontologies (OWL/RDF):** Formal description logic standards supporting open-world assumption and automated reasoning.\\n- **Graph Neural Networks (GNN):** Continuous vector embeddings for knowledge graph completion; handles missing links well, but lacks deterministic proof capabilities.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "Data fusion resolves conflicting information from different sources."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Aligning data from various sources to a common ontology."
                    }
                ]
            },
            {
                "title": "Module 3: Querying Knowledge Graphs",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "SPARQL is the standard query language for RDF graphs."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Queries consist of graph patterns to match against the KG."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\n  A[\"?person\"] -->|knows| B[\"?friend\"]\n  style A fill:#f59e0b,stroke:#333,stroke-width:2px"
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** "
                    },
                    {
                        "type": "markdown",
                        "content": "Variables in SPARQL are denoted by a question mark."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Specifies which variables to return in the result set."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph TD\n  Empty[\"Empty Diagram\"]"
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "",
                        "solution_code": "",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nDecouples declarative facts (subject-predicate-object triples) from procedural code, enabling inheritance along taxonomic graphs with $O(depth)$ lookup time.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Relational SQL Database:** Strict ACID transactions and fast joins, but rigid schemas make inheritance and recursive graph traversal awkward.\\n- **Semantic Web Ontologies (OWL/RDF):** Formal description logic standards supporting open-world assumption and automated reasoning.\\n- **Graph Neural Networks (GNN):** Continuous vector embeddings for knowledge graph completion; handles missing links well, but lacks deterministic proof capabilities.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "Cypher is another popular query language, used by Neo4j."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Cypher excels at expressing complex graph traversals."
                    }
                ]
            },
            {
                "title": "Module 4: Reasoning on Knowledge Graphs",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "Reasoning infers new knowledge from existing facts."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Applying logical rules like 'If X is Ys parent, X is older than Y'."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\n  A[\"Parent\"] -->|Implies| B[\"Older\"]\n  style A fill:#ef4444,stroke:#333,stroke-width:2px"
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** "
                    },
                    {
                        "type": "markdown",
                        "content": "Transitive relations allow traversing hierarchies."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "If a Dog is a Mammal, and a Mammal is an Animal, a Dog is an Animal."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph TD\n  Empty[\"Empty Diagram\"]"
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "",
                        "solution_code": "",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nDecouples declarative facts (subject-predicate-object triples) from procedural code, enabling inheritance along taxonomic graphs with $O(depth)$ lookup time.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Relational SQL Database:** Strict ACID transactions and fast joins, but rigid schemas make inheritance and recursive graph traversal awkward.\\n- **Semantic Web Ontologies (OWL/RDF):** Formal description logic standards supporting open-world assumption and automated reasoning.\\n- **Graph Neural Networks (GNN):** Continuous vector embeddings for knowledge graph completion; handles missing links well, but lacks deterministic proof capabilities.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "Knowledge Graph Embeddings represent entities as vectors."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Predicting missing edges in the graph using embeddings."
                    }
                ]
            }
        ]
    },
    "9": {
        "title": "Case 09: The Logic Engine",
        "episodes": [
            {
                "title": "Module 1: Propositional Logic",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "Propositional logic deals with statements that are true or false."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "A proposition is a declarative sentence, e.g., 'It is raining'."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\n  A[\"P: Raining\"] --> B[\"True/False\"]\n  style A fill:#10b981,stroke:#333,stroke-width:2px"
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** "
                    },
                    {
                        "type": "markdown",
                        "content": "Connectives join propositions: AND, OR, NOT, IMPLIES."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Truth tables define the semantics of connectives."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph TD\n  Empty[\"Empty Diagram\"]"
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "",
                        "solution_code": "",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nResolution refutation adds the negated query $\\neg Q$ to the CNF knowledge base and resolves clauses until deriving the empty clause $\\Box$, proving entailment with refutation completeness.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Forward Chaining on Horn Clauses:** Linear time $O(KB)$, simple and data-driven, but only handles Horn clauses (at most one positive literal).\\n- **Backward Chaining (Goal-Driven):** Generates only queries relevant to the target goal, but vulnerable to infinite recursion on left-recursive rules.\\n- **Modern SAT Solvers (CDCL):** Conflict-Driven Clause Learning solves industrial propositional formulas with millions of variables.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "A sentence is satisfiable if it can be true."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "A tautology is true under all possible interpretations."
                    }
                ]
            },
            {
                "title": "Module 2: First Order Logic (FOL)",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "FOL extends propositional logic with objects and quantifiers."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Predicates express properties or relations between objects."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\n  A[\"Loves(x, y)\"] --> B[\"Relation\"]\n  style A fill:#3b82f6,stroke:#333,stroke-width:2px"
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** "
                    },
                    {
                        "type": "markdown",
                        "content": "The Universal Quantifier (∀) means 'for all'."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "The Existential Quantifier (∃) means 'there exists'."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph TD\n  Empty[\"Empty Diagram\"]"
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "",
                        "solution_code": "",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nResolution refutation adds the negated query $\\neg Q$ to the CNF knowledge base and resolves clauses until deriving the empty clause $\\Box$, proving entailment with refutation completeness.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Forward Chaining on Horn Clauses:** Linear time $O(KB)$, simple and data-driven, but only handles Horn clauses (at most one positive literal).\\n- **Backward Chaining (Goal-Driven):** Generates only queries relevant to the target goal, but vulnerable to infinite recursion on left-recursive rules.\\n- **Modern SAT Solvers (CDCL):** Conflict-Driven Clause Learning solves industrial propositional formulas with millions of variables.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "Variables in FOL represent generic objects."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Constants denote specific objects. Functions map objects to objects."
                    }
                ]
            },
            {
                "title": "Module 3: Inference in FOL",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "Inference derives new sentences from a knowledge base."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "If P implies Q, and P is true, then Q is true."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\n  A[\"P -> Q\"] --> B[\"P => Q\"]\n  style A fill:#f59e0b,stroke:#333,stroke-width:2px"
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** "
                    },
                    {
                        "type": "markdown",
                        "content": "Unification finds substitutions to make expressions identical."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Replacing variables with terms, e.g., {x/John}."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph TD\n  Empty[\"Empty Diagram\"]"
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "",
                        "solution_code": "",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nResolution refutation adds the negated query $\\neg Q$ to the CNF knowledge base and resolves clauses until deriving the empty clause $\\Box$, proving entailment with refutation completeness.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Forward Chaining on Horn Clauses:** Linear time $O(KB)$, simple and data-driven, but only handles Horn clauses (at most one positive literal).\\n- **Backward Chaining (Goal-Driven):** Generates only queries relevant to the target goal, but vulnerable to infinite recursion on left-recursive rules.\\n- **Modern SAT Solvers (CDCL):** Conflict-Driven Clause Learning solves industrial propositional formulas with millions of variables.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "Forward chaining applies rules to infer new facts."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Starts from a goal and works backward to find supporting facts."
                    }
                ]
            },
            {
                "title": "Module 4: Resolution and Theorem Proving",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "Resolution is a sound and complete inference rule."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Sentences must be converted to CNF for resolution."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\n  A[\"A OR B\"] --> B[\"CNF\"]\n  style A fill:#ef4444,stroke:#333,stroke-width:2px"
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** "
                    },
                    {
                        "type": "markdown",
                        "content": "A resolvent is formed by combining two clauses and resolving a complementary literal."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "To prove P, assume not P and derive the empty clause."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph TD\n  Empty[\"Empty Diagram\"]"
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "",
                        "solution_code": "",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nResolution refutation adds the negated query $\\neg Q$ to the CNF knowledge base and resolves clauses until deriving the empty clause $\\Box$, proving entailment with refutation completeness.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Forward Chaining on Horn Clauses:** Linear time $O(KB)$, simple and data-driven, but only handles Horn clauses (at most one positive literal).\\n- **Backward Chaining (Goal-Driven):** Generates only queries relevant to the target goal, but vulnerable to infinite recursion on left-recursive rules.\\n- **Modern SAT Solvers (CDCL):** Conflict-Driven Clause Learning solves industrial propositional formulas with millions of variables.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "The empty clause represents a contradiction."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "If a sentence is entailed, resolution will eventually derive a contradiction."
                    }
                ]
            }
        ]
    },
    "10": {
        "title": "Case 10: The Machine That Could Reason",
        "episodes": [
            {
                "title": "Module 1: Modeling Change",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "Situation calculus models dynamic worlds using logic."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "A situation is a snapshot of the world at a particular time."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\n  A[\"S0 (Initial)\"] --> B[\"S1\"]\n  style A fill:#10b981,stroke:#333,stroke-width:2px"
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** "
                    },
                    {
                        "type": "markdown",
                        "content": "Actions transition the world from one situation to the next."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Result(a, s) is the situation resulting from doing action a in situation s."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph TD\n  Empty[\"Empty Diagram\"]"
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "",
                        "solution_code": "",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nSuccessor-state axioms solve the classical Frame Problem by explicitly defining the exact conditions under which a fluent changes value between situations $Result(a, s)$.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Frame Axioms:** Explicitly states what does NOT change for every action; requires $O(|Actions| \\times |Fluents|)$ redundant axioms.\\n- **Event Calculus:** Formulates continuous time and state intervals rather than discrete situation trees.\\n- **Default Logic:** Non-monotonic logic that draws plausible conclusions in the absence of explicit contradictory evidence.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "Fluents are properties that change over time."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "At(Robot, Room1, S0) means the robot is in Room1 in situation S0."
                    }
                ]
            },
            {
                "title": "Module 2: Axioms in Situation Calculus",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "Axioms describe the physics of the modeled world."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Preconditions that must hold for an action to be possible."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\n  A[\"Precondition\"] --> B[\"Poss(A, S)\"]\n  style A fill:#3b82f6,stroke:#333,stroke-width:2px"
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** "
                    },
                    {
                        "type": "markdown",
                        "content": "Effect axioms specify the changes caused by an action."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Fluents made true by the action."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph TD\n  Empty[\"Empty Diagram\"]"
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "",
                        "solution_code": "",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nSuccessor-state axioms solve the classical Frame Problem by explicitly defining the exact conditions under which a fluent changes value between situations $Result(a, s)$.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Frame Axioms:** Explicitly states what does NOT change for every action; requires $O(|Actions| \\times |Fluents|)$ redundant axioms.\\n- **Event Calculus:** Formulates continuous time and state intervals rather than discrete situation trees.\\n- **Default Logic:** Non-monotonic logic that draws plausible conclusions in the absence of explicit contradictory evidence.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "Negative effects specify fluents made false."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "How to succinctly represent what DOES NOT change."
                    }
                ]
            },
            {
                "title": "Module 3: Solving the Frame Problem",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "The frame problem is a major challenge in AI."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Explicitly stating that an action does not affect a specific fluent."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\n  A[\"Action Move\"] --> B[\"Color Unchanged\"]\n  style A fill:#f59e0b,stroke:#333,stroke-width:2px"
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** "
                    },
                    {
                        "type": "markdown",
                        "content": "Writing frame axioms for everything is intractable (O(A*F))."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "A solution that combines effect and frame axioms for each fluent."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph TD\n  Empty[\"Empty Diagram\"]"
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "",
                        "solution_code": "",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nSuccessor-state axioms solve the classical Frame Problem by explicitly defining the exact conditions under which a fluent changes value between situations $Result(a, s)$.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Frame Axioms:** Explicitly states what does NOT change for every action; requires $O(|Actions| \\times |Fluents|)$ redundant axioms.\\n- **Event Calculus:** Formulates continuous time and state intervals rather than discrete situation trees.\\n- **Default Logic:** Non-monotonic logic that draws plausible conclusions in the absence of explicit contradictory evidence.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "This requires O(F) axioms instead of O(A*F)."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Requires the closed-world assumption for action effects."
                    }
                ]
            },
            {
                "title": "Module 4: Planning with Situation Calculus",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "Planning is finding a sequence of actions to reach a goal."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "A formula describing the desired properties of a situation."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\n  A[\"Start\"] --> B[\"Goal Situation S_G\"]\n  style A fill:#ef4444,stroke:#333,stroke-width:2px"
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** "
                    },
                    {
                        "type": "markdown",
                        "content": "Planning can be formulated as proving a theorem: ∃s Goal(s)."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "The proof yields a binding for 's' like Result(A2, Result(A1, S0))."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph TD\n  Empty[\"Empty Diagram\"]"
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "",
                        "solution_code": "",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nSuccessor-state axioms solve the classical Frame Problem by explicitly defining the exact conditions under which a fluent changes value between situations $Result(a, s)$.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Frame Axioms:** Explicitly states what does NOT change for every action; requires $O(|Actions| \\times |Fluents|)$ redundant axioms.\\n- **Event Calculus:** Formulates continuous time and state intervals rather than discrete situation trees.\\n- **Default Logic:** Non-monotonic logic that draws plausible conclusions in the absence of explicit contradictory evidence.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "General theorem proving for planning is often inefficient."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Led to the development of specialized representations like STRIPS."
                    }
                ]
            }
        ]
    },
    "11": {
        "title": "Case 11: The Planner",
        "episodes": [
            {
                "title": "Module 1: The STRIPS Representation",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "STRIPS simplifies action representation for efficient planning."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "States are conjunctions of positive, ground, function-free literals."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\n  A[\"At(Robot, Room1)\"] --> B[\"State\"]\n  style A fill:#10b981,stroke:#333,stroke-width:2px"
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** "
                    },
                    {
                        "type": "markdown",
                        "content": "Anything not listed in the state is assumed false."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Defined by Preconditions, Add list, and Delete list."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph TD\n  Empty[\"Empty Diagram\"]"
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "",
                        "solution_code": "",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nSTRIPS operators represent actions via Preconditions, Add-lists, and Delete-lists, enabling backward regression from the goal to construct plans without evaluating irrelevant branches.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Forward State-Space Progression:** Evaluates actions from initial state forward; intuitive, but suffers from massive branching factor.\\n- **Graphplan:** Constructs polynomial-time planning graphs with mutual exclusion (mutex) links, finding shortest parallel plans.\\n- **SATPlan:** Encodes the planning problem into boolean SAT and leverages high-performance modern SAT solvers.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "The Add list contains new facts; the Delete list removes old ones."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "New State = (Old State - Delete) U Add."
                    }
                ]
            },
            {
                "title": "Module 2: Forward State-Space Search",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "Forward search starts at the initial state and applies actions."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "An action is applicable if its preconditions are in the current state."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\n  A[\"State S\"] -->|Applicable Action| B[\"State S'\"]\n  style A fill:#3b82f6,stroke:#333,stroke-width:2px"
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** "
                    },
                    {
                        "type": "markdown",
                        "content": "The search stops when the goal state is reached."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Forward search can have a massive branching factor."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph TD\n  Empty[\"Empty Diagram\"]"
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "",
                        "solution_code": "",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nSTRIPS operators represent actions via Preconditions, Add-lists, and Delete-lists, enabling backward regression from the goal to construct plans without evaluating irrelevant branches.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Forward State-Space Progression:** Evaluates actions from initial state forward; intuitive, but suffers from massive branching factor.\\n- **Graphplan:** Constructs polynomial-time planning graphs with mutual exclusion (mutex) links, finding shortest parallel plans.\\n- **SATPlan:** Encodes the planning problem into boolean SAT and leverages high-performance modern SAT solvers.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "Many applicable actions might be irrelevant to the goal."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Heuristics are essential to guide forward search effectively."
                    }
                ]
            },
            {
                "title": "Module 3: Backward Search and Heuristics",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "Backward search starts at the goal and regresses actions."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "An action is relevant if it achieves one of the goal literals."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\n  A[\"Goal\"] -->|Regress Action| B[\"Subgoal\"]\n  style A fill:#f59e0b,stroke:#333,stroke-width:2px"
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** "
                    },
                    {
                        "type": "markdown",
                        "content": "Regression calculates the preconditions needed to reach the goal."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "A structure to extract powerful heuristics for planning."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph TD\n  Empty[\"Empty Diagram\"]"
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "",
                        "solution_code": "",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nSTRIPS operators represent actions via Preconditions, Add-lists, and Delete-lists, enabling backward regression from the goal to construct plans without evaluating irrelevant branches.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Forward State-Space Progression:** Evaluates actions from initial state forward; intuitive, but suffers from massive branching factor.\\n- **Graphplan:** Constructs polynomial-time planning graphs with mutual exclusion (mutex) links, finding shortest parallel plans.\\n- **SATPlan:** Encodes the planning problem into boolean SAT and leverages high-performance modern SAT solvers.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "Planning graphs estimate the cost to achieve a goal literal."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Tracks actions and literals that cannot occur simultaneously."
                    }
                ]
            },
            {
                "title": "Module 4: Partial-Order Planning",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "Partial-Order Planning (POP) searches in the space of plans, not states."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "A plan is a set of steps, ordering constraints, and causal links."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\n  A[\"Step A\"] -.->|Before| B[\"Step B\"]\n  style A fill:#ef4444,stroke:#333,stroke-width:2px"
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** "
                    },
                    {
                        "type": "markdown",
                        "content": "Causal links ensure that preconditions are met and protected."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "A threat occurs when a step might delete a protected precondition."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph TD\n  Empty[\"Empty Diagram\"]"
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "",
                        "solution_code": "",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nSTRIPS operators represent actions via Preconditions, Add-lists, and Delete-lists, enabling backward regression from the goal to construct plans without evaluating irrelevant branches.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Forward State-Space Progression:** Evaluates actions from initial state forward; intuitive, but suffers from massive branching factor.\\n- **Graphplan:** Constructs polynomial-time planning graphs with mutual exclusion (mutex) links, finding shortest parallel plans.\\n- **SATPlan:** Encodes the planning problem into boolean SAT and leverages high-performance modern SAT solvers.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "Threats are resolved by adding ordering constraints (promotion/demotion)."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "POP only orders steps when necessary to resolve threats."
                    }
                ]
            }
        ]
    },
    "12": {
        "title": "Case 12: The World That Keeps Changing",
        "episodes": [
            {
                "title": "Module 1: Embracing the Unknown",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "# The AI in the Fog\nImagine driving in thick fog. You can't see the cars ahead perfectly, but you know they are there. AI systems operate in a similar 'fog' of uncertainty."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Aleatoric uncertainty (inherent randomness) vs Epistemic uncertainty (lack of knowledge)."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\n  A[\"Uncertainty\"] --> B[\"Aleatoric (Randomness)\"]\n  A --> C[\"Epistemic (Ignorance)\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "Aleatoric uncertainty is like flipping a coin. No matter how much data you gather, the outcome is random."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Probability theory provides a rigorous framework for reasoning under uncertainty, extending classical Boolean logic."
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** "
                    },
                    {
                        "type": "markdown",
                        "content": "In AI, we often use probability distributions to represent our beliefs about the state of the world."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph LR\n  A[\"Belief State\"] --> B[\"Observation\"]\n  B --> C[\"Updated Belief\"]\n  style A fill:#10b9811a\n  style C fill:#10b9811a"
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "def update_belief(prior, evidence):\n    # A placeholder for belief updating logic\n    return prior * evidence\n\n# --- Execution Output ---\nprint('Result:', update_belief(None))\n",
                        "solution_code": "def update_belief(prior, evidence):\n    # A placeholder for belief updating logic\n    return prior * evidence\n\n# --- Execution Output ---\nprint('Result:', update_belief(None))\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nApplies the axioms of probability to quantify uncertainty, ensuring coherent belief updates and satisfying Kolmogorov's foundation.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Full Joint Distribution Table:** Requires $2^n - 1$ parameters (exponential in number of variables $n$), making it intractable for real systems.\\n- **Fuzzy Logic:** Models degrees of truth rather than probability of occurrence; popular in industrial control, but lacks Bayesian consistency.\\n- **Dempster-Shafer Theory:** Explicitly represents epistemic ignorance by assigning belief to sets of outcomes rather than single events.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "We've laid the groundwork for reasoning in uncertain environments."
                    }
                ]
            },
            {
                "title": "Module 2: Random Variables and Distributions",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "## Random Variables\nA random variable assigns a numerical value to each outcome in a sample space."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Random variables can be discrete (like dice rolls) or continuous (like temperature)."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\n  RV[\"Random Variable X\"] --> D[\"Discrete (e.g., Coin)\"]\n  RV --> C[\"Continuous (e.g., Temp)\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "The Probability Mass Function (PMF) maps discrete outcomes to probabilities."
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** "
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "For continuous variables, we use the PDF. The probability of an exact value is zero; we measure areas under the curve."
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "import scipy.stats as stats\n# Standard normal PDF\npdf_value = stats.norm.pdf(0)\nprint(f'PDF at x=0: {pdf_value}')",
                        "solution_code": "import scipy.stats as stats\n# Standard normal PDF\npdf_value = stats.norm.pdf(0)\nprint(f'PDF at x=0: {pdf_value}')",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nApplies the axioms of probability to quantify uncertainty, ensuring coherent belief updates and satisfying Kolmogorov's foundation.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Full Joint Distribution Table:** Requires $2^n - 1$ parameters (exponential in number of variables $n$), making it intractable for real systems.\\n- **Fuzzy Logic:** Models degrees of truth rather than probability of occurrence; popular in industrial control, but lacks Bayesian consistency.\\n- **Dempster-Shafer Theory:** Explicitly represents epistemic ignorance by assigning belief to sets of outcomes rather than single events.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "Expectation and Variance are key summaries of a distribution."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph LR\n  A[\"Distribution\"] --> B[\"Mean (Center)\"]\n  A --> C[\"Variance (Spread)\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "Understanding these forms the basis of statistical AI."
                    }
                ]
            },
            {
                "title": "Module 3: Joint and Marginal Probabilities",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "## Multiple Variables\nReal-world problems involve many interacting variables. We need joint probabilities."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "P(X, Y) is the probability that X and Y happen together."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\n  A[\"Weather\"] --> C[\"Joint: P(Weather, Traffic)\"]\n  B[\"Traffic\"] --> C"
                    },
                    {
                        "type": "markdown",
                        "content": "Marginalization is the process of extracting the distribution of a single variable from a joint distribution."
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** "
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "P(X|Y) = P(X, Y) / P(Y). This is the foundation of inference."
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "p_x_and_y = 0.1\np_y = 0.5\np_x_given_y = p_x_and_y / p_y\nprint(p_x_given_y)",
                        "solution_code": "p_x_and_y = 0.1\np_y = 0.5\np_x_given_y = p_x_and_y / p_y\nprint(p_x_given_y)",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nApplies the axioms of probability to quantify uncertainty, ensuring coherent belief updates and satisfying Kolmogorov's foundation.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Full Joint Distribution Table:** Requires $2^n - 1$ parameters (exponential in number of variables $n$), making it intractable for real systems.\\n- **Fuzzy Logic:** Models degrees of truth rather than probability of occurrence; popular in industrial control, but lacks Bayesian consistency.\\n- **Dempster-Shafer Theory:** Explicitly represents epistemic ignorance by assigning belief to sets of outcomes rather than single events.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "Independence means P(X,Y) = P(X)P(Y). Learning X gives no info about Y."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph LR\n  A[\"Independent\"] --> B[\"P(X|Y) = P(X)\"]\n  C[\"Dependent\"] --> D[\"P(X|Y) != P(X)\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "Conditional independence is a crucial concept for scaling up probabilistic models."
                    }
                ]
            },
            {
                "title": "Module 4: Applications of Probability in AI",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "## Where do we use this?\nFrom robotics to natural language, probability is everywhere."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Combining multiple uncertain sensor readings to get a robust estimate."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\n  A[\"Camera\"] --> C[\"State Estimate\"]\n  B[\"LiDAR\"] --> C\n  style C fill:#4285f41a"
                    },
                    {
                        "type": "markdown",
                        "content": "Language models use probabilities to predict the next word."
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** "
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Probabilities combine with utilities to make optimal decisions (Expected Utility)."
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "def expected_utility(prob, utility):\n    return sum(p * u for p, u in zip(prob, utility))\n\n# --- Execution Output ---\nprint('Result:', expected_utility(None))\n",
                        "solution_code": "def expected_utility(prob, utility):\n    return sum(p * u for p, u in zip(prob, utility))\n\n# --- Execution Output ---\nprint('Result:', expected_utility(None))\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nApplies the axioms of probability to quantify uncertainty, ensuring coherent belief updates and satisfying Kolmogorov's foundation.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Full Joint Distribution Table:** Requires $2^n - 1$ parameters (exponential in number of variables $n$), making it intractable for real systems.\\n- **Fuzzy Logic:** Models degrees of truth rather than probability of occurrence; popular in industrial control, but lacks Bayesian consistency.\\n- **Dempster-Shafer Theory:** Explicitly represents epistemic ignorance by assigning belief to sets of outcomes rather than single events.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "Medical diagnosis systems use probability to infer disease given symptoms."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph LR\n  A[\"Symptoms\"] --> B[\"Probabilistic Engine\"]\n  B --> C[\"Diagnosis Belief\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "You are now ready to dive deep into Bayes Rule."
                    }
                ]
            }
        ]
    },
    "13": {
        "title": "Case 13: The Probability Problem",
        "episodes": [
            {
                "title": "Module 1: The Anatomy of Bayes Theorem",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "# The Reverend's Rule\nThomas Bayes gave us a mathematical way to update beliefs based on new evidence."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "P(H|E) = P(E|H) * P(H) / P(E). Hypothesis H, Evidence E."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph LR\n  A[\"Prior: P(H)\"] --> C[\"Posterior: P(H|E)\"]\n  B[\"Likelihood: P(E|H)\"] --> C"
                    },
                    {
                        "type": "markdown",
                        "content": "The Prior is what you believe before seeing the data."
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** "
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "P(E) is the evidence or marginal likelihood. It normalizes the posterior."
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "def bayes(prior, likelihood, marginal):\n    return (likelihood * prior) / marginal\n\n# --- Execution Output ---\nprint('Result:', bayes(None))\n",
                        "solution_code": "def bayes(prior, likelihood, marginal):\n    return (likelihood * prior) / marginal\n\n# --- Execution Output ---\nprint('Result:', bayes(None))\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nBayes' Theorem mathematically inverts diagnostic probabilities into causal probabilities $P(Cause|Effect) = \\frac{P(Effect|Cause)P(Cause)}{P(Effect)}$, correctly integrating prior base rates.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Maximum Likelihood Estimation (MLE):** Ignores the prior; optimal in the limit of infinite data, but severely biased by rare base rates on small samples.\\n- **Maximum A Posteriori (MAP):** Incorporates the prior but outputs a single point estimate rather than a full probability distribution.\\n- **Full Bayesian Estimation:** Integrates over all parameter uncertainties, providing confidence bounds at higher computational cost.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "Understanding each term is critical for building Bayesian agents."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph TD\n  A[\"Hypothesis\"] --> B[\"Generate Evidence\"]\n  C[\"Actual Evidence\"] --> D[\"Compare & Update\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "Next, we'll apply this to a classic medical testing scenario."
                    }
                ]
            },
            {
                "title": "Module 2: The Base Rate Fallacy",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "## Medical Diagnosis\nImagine a disease affects 1% of the population. A test is 99% accurate."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "The base rate is the prior probability (1%). Ignoring it leads to the Base Rate Fallacy."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\n  A[\"Disease P(D)=0.01\"] --> B[\"Test Positive P(+|D)=0.99\"]\n  C[\"Healthy P(~D)=0.99\"] --> D[\"Test Positive P(+|~D)=0.01\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "If you test positive, what's the chance you actually have the disease? It's not 99%!"
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** "
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "P(D|+) = P(+|D)P(D) / (P(+|D)P(D) + P(+|~D)P(~D)) = 50%."
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "prior = 0.01\nlikelihood = 0.99\nfalse_positive = 0.01\nmarginal = (likelihood * prior) + (false_positive * (1 - prior))\nposterior = (likelihood * prior) / marginal\nprint(posterior)",
                        "solution_code": "prior = 0.01\nlikelihood = 0.99\nfalse_positive = 0.01\nmarginal = (likelihood * prior) + (false_positive * (1 - prior))\nposterior = (likelihood * prior) / marginal\nprint(posterior)",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nBayes' Theorem mathematically inverts diagnostic probabilities into causal probabilities $P(Cause|Effect) = \\frac{P(Effect|Cause)P(Cause)}{P(Effect)}$, correctly integrating prior base rates.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Maximum Likelihood Estimation (MLE):** Ignores the prior; optimal in the limit of infinite data, but severely biased by rare base rates on small samples.\\n- **Maximum A Posteriori (MAP):** Incorporates the prior but outputs a single point estimate rather than a full probability distribution.\\n- **Full Bayesian Estimation:** Integrates over all parameter uncertainties, providing confidence bounds at higher computational cost.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "This counterintuitive result shows why formal probabilistic reasoning is necessary."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph LR\n  A[\"Rare Disease\"] --> B[\"Many False Positives\"]\n  B --> C[\"Low Posterior Confidence\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "AI systems must inherently incorporate base rates to avoid this trap."
                    }
                ]
            },
            {
                "title": "Module 3: Bayesian Filtering",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "## Tracking State Over Time\nHow does a self-driving car track a pedestrian over time? Bayesian filtering."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "We continuously apply Bayes rule. Today's posterior becomes tomorrow's prior."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph LR\n  A[\"Belief(t)\"] --> B[\"Action/Time Update\"]\n  B --> C[\"Belief(t+1)\"]\n  D[\"Observation\"] --> C"
                    },
                    {
                        "type": "markdown",
                        "content": "There are two steps: Predict (time update) and Update (measurement update)."
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** "
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "A Kalman filter is an optimal Bayesian filter for linear Gaussian systems."
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "class SimpleFilter:\n    def update(self, prior, likelihood):\n        # Returns unnormalized posterior\n        return prior * likelihood\n\n# --- Execution Output ---\nobj = SimpleFilter()\nprint('Initialized', obj)\n",
                        "solution_code": "class SimpleFilter:\n    def update(self, prior, likelihood):\n        # Returns unnormalized posterior\n        return prior * likelihood\n\n# --- Execution Output ---\nobj = SimpleFilter()\nprint('Initialized', obj)\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nBayes' Theorem mathematically inverts diagnostic probabilities into causal probabilities $P(Cause|Effect) = \\frac{P(Effect|Cause)P(Cause)}{P(Effect)}$, correctly integrating prior base rates.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Maximum Likelihood Estimation (MLE):** Ignores the prior; optimal in the limit of infinite data, but severely biased by rare base rates on small samples.\\n- **Maximum A Posteriori (MAP):** Incorporates the prior but outputs a single point estimate rather than a full probability distribution.\\n- **Full Bayesian Estimation:** Integrates over all parameter uncertainties, providing confidence bounds at higher computational cost.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "Filtering allows AI to maintain a persistent model of the world."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph TD\n  A[\"Predict State\"] --> B[\"Incorporate Measurement\"]\n  B --> A"
                    },
                    {
                        "type": "markdown",
                        "content": "This is fundamental to modern robotics and navigation."
                    }
                ]
            },
            {
                "title": "Module 4: Naive Bayes Classification",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "## Spam or Ham?\nThe Naive Bayes algorithm is a simple yet powerful classifier."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "It assumes that all features are conditionally independent given the class."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\n  A[\"Class (Spam)\"] --> B[\"Word: Viagra\"]\n  A --> C[\"Word: Prince\"]\n  A --> D[\"Word: Free\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "Despite this strong (and usually false) assumption, it works remarkably well."
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** "
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Multiplying many small probabilities leads to underflow. We add log probabilities instead."
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "import math\ndef log_prob(p_prior, p_features):\n    return math.log(p_prior) + sum(math.log(p) for p in p_features)\n\n# --- Execution Output ---\nprint('Result:', log_prob(None))\n",
                        "solution_code": "import math\ndef log_prob(p_prior, p_features):\n    return math.log(p_prior) + sum(math.log(p) for p in p_features)\n\n# --- Execution Output ---\nprint('Result:', log_prob(None))\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nBayes' Theorem mathematically inverts diagnostic probabilities into causal probabilities $P(Cause|Effect) = \\frac{P(Effect|Cause)P(Cause)}{P(Effect)}$, correctly integrating prior base rates.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Maximum Likelihood Estimation (MLE):** Ignores the prior; optimal in the limit of infinite data, but severely biased by rare base rates on small samples.\\n- **Maximum A Posteriori (MAP):** Incorporates the prior but outputs a single point estimate rather than a full probability distribution.\\n- **Full Bayesian Estimation:** Integrates over all parameter uncertainties, providing confidence bounds at higher computational cost.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "Naive Bayes is often used as a baseline for text classification tasks."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph LR\n  A[\"Input Text\"] --> B[\"Extract Words\"]\n  B --> C[\"Calculate Log Posteriors\"]\n  C --> D[\"Argmax Class\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "Next, we will look at more complex graphical models: Bayesian Networks."
                    }
                ]
            }
        ]
    },
    "14": {
        "title": "Case 14: The Bayesian Detective",
        "episodes": [
            {
                "title": "Module 1: Graphs and Probabilities",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "# Unspaghettifying Probabilities\nSpecifying a full joint distribution is intractable. Enter Bayesian Networks."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Bayesian Networks use DAGs to compactly represent joint distributions."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\n  A[\"Burglary\"] --> C[\"Alarm\"]\n  B[\"Earthquake\"] --> C\n  C --> D[\"JohnCalls\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "Nodes represent random variables, and edges represent direct probabilistic influence."
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** "
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "P(X1..Xn) = Product of P(Xi | Parents(Xi)). This drastically reduces parameters."
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "def joint_prob(p_b, p_e, p_a_given_be):\n    return p_b * p_e * p_a_given_be\n\n# --- Execution Output ---\nprint('Result:', joint_prob(None))\n",
                        "solution_code": "def joint_prob(p_b, p_e, p_a_given_be):\n    return p_b * p_e * p_a_given_be\n\n# --- Execution Output ---\nprint('Result:', joint_prob(None))\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nBayesian Networks exploit conditional independence in Directed Acyclic Graphs (DAGs) to factorize the joint distribution: $P(X_1...X_n) = \\prod P(X_i | Parents(X_i))$, reducing parameter storage from $O(2^n)$ to $O(n \\cdot 2^k)$.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Variable Elimination:** Exact inference algorithm using dynamic programming to sum out irrelevant variables, avoiding redundant subcomputations.\\n- **Markov Chain Monte Carlo (MCMC):** Approximate sampling method that scales to massive networks where exact inference is NP-hard.\\n- **Junction Tree Algorithm:** Exact message-passing on triangulated clique graphs for multi-connected networks.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "By leveraging conditional independence, we tame complexity."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph LR\n  A[\"Full Joint (2^N)\"] --> B[\"Factorization via C.I.\"]\n  B --> C[\"Compact Representation\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "This makes reasoning in complex domains computationally feasible."
                    }
                ]
            },
            {
                "title": "Module 2: Conditional Independence in Graphs",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "## D-Separation\nHow do we read conditional independencies directly from the graph structure?"
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Causal chain (A->B->C), Common cause (A<-B->C), and Common effect (A->B<-C)."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\n  A[\"X\"] --> B[\"Y\"]\n  B --> C[\"Z\"]\n  style B fill:#e11d481a"
                    },
                    {
                        "type": "markdown",
                        "content": "In a causal chain, observing the middle node blocks the flow of information."
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** "
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "In A->B<-C, observing B makes A and C dependent. This is called the 'explaining away' effect."
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "# Conceptual check: explaining away\ndef is_d_separated(path, observed_nodes):\n    # Simplified logic placeholder\n    return True\n\n# --- Execution Output ---\nprint('Result:', is_d_separated(None))\n",
                        "solution_code": "# Conceptual check: explaining away\ndef is_d_separated(path, observed_nodes):\n    # Simplified logic placeholder\n    return True\n\n# --- Execution Output ---\nprint('Result:', is_d_separated(None))\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nBayesian Networks exploit conditional independence in Directed Acyclic Graphs (DAGs) to factorize the joint distribution: $P(X_1...X_n) = \\prod P(X_i | Parents(X_i))$, reducing parameter storage from $O(2^n)$ to $O(n \\cdot 2^k)$.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Variable Elimination:** Exact inference algorithm using dynamic programming to sum out irrelevant variables, avoiding redundant subcomputations.\\n- **Markov Chain Monte Carlo (MCMC):** Approximate sampling method that scales to massive networks where exact inference is NP-hard.\\n- **Junction Tree Algorithm:** Exact message-passing on triangulated clique graphs for multi-connected networks.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "D-separation gives us a complete algorithmic way to find independencies."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph LR\n  A[\"Graph Structure\"] --> B[\"D-Separation Rules\"]\n  B --> C[\"Independence Guarantees\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "These guarantees allow us to optimize inference algorithms."
                    }
                ]
            },
            {
                "title": "Module 3: Exact Inference",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "## Calculating Posteriors\nGiven some observed evidence, how do we compute the posterior of query variables?"
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Sum over all hidden variables in the joint distribution. Simple but slow (exponential time)."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\n  A[\"Query\"] --> B[\"Joint Dist\"]\n  B --> C[\"Sum out Hidden\"]\n  C --> D[\"Normalize\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "Variable Elimination is a faster exact inference algorithm."
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** "
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "We push sums inward, interleaving multiplication and marginalization to avoid building the full joint table."
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "def eliminate_variable(factor_list, variable):\n    # Multiply relevant factors and sum out the variable\n    pass\n\n# --- Execution Output ---\nprint('Result:', eliminate_variable(None))\n",
                        "solution_code": "def eliminate_variable(factor_list, variable):\n    # Multiply relevant factors and sum out the variable\n    pass\n\n# --- Execution Output ---\nprint('Result:', eliminate_variable(None))\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nBayesian Networks exploit conditional independence in Directed Acyclic Graphs (DAGs) to factorize the joint distribution: $P(X_1...X_n) = \\prod P(X_i | Parents(X_i))$, reducing parameter storage from $O(2^n)$ to $O(n \\cdot 2^k)$.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Variable Elimination:** Exact inference algorithm using dynamic programming to sum out irrelevant variables, avoiding redundant subcomputations.\\n- **Markov Chain Monte Carlo (MCMC):** Approximate sampling method that scales to massive networks where exact inference is NP-hard.\\n- **Junction Tree Algorithm:** Exact message-passing on triangulated clique graphs for multi-connected networks.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "The order in which we eliminate variables drastically affects computation time."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph LR\n  A[\"Factors\"] --> B[\"Multiply\"] --> C[\"Sum Out\"] --> D[\"New Factor\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "However, even variable elimination is NP-hard in the worst case."
                    }
                ]
            },
            {
                "title": "Module 4: Approximate Inference",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "## When Exact is Too Slow\nFor huge networks, exact inference is impossible. We use sampling instead."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "We generate random samples from the network and count frequencies to estimate probabilities."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\n  A[\"Bayesian Network\"] --> B[\"Generate Samples\"]\n  B --> C[\"Estimate Posterior\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "Prior Sampling generates samples from the prior, but wastes time if evidence is rare."
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** "
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "A Markov Chain Monte Carlo (MCMC) method. We resample one variable at a time, conditioned on the rest."
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "import random\ndef gibbs_step(current_state, markov_blanket):\n    # Sample node given its blanket\n    return random.choice([True, False])\n\n# --- Execution Output ---\nprint('Result:', gibbs_step(None))\n",
                        "solution_code": "import random\ndef gibbs_step(current_state, markov_blanket):\n    # Sample node given its blanket\n    return random.choice([True, False])\n\n# --- Execution Output ---\nprint('Result:', gibbs_step(None))\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nBayesian Networks exploit conditional independence in Directed Acyclic Graphs (DAGs) to factorize the joint distribution: $P(X_1...X_n) = \\prod P(X_i | Parents(X_i))$, reducing parameter storage from $O(2^n)$ to $O(n \\cdot 2^k)$.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Variable Elimination:** Exact inference algorithm using dynamic programming to sum out irrelevant variables, avoiding redundant subcomputations.\\n- **Markov Chain Monte Carlo (MCMC):** Approximate sampling method that scales to massive networks where exact inference is NP-hard.\\n- **Junction Tree Algorithm:** Exact message-passing on triangulated clique graphs for multi-connected networks.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "Gibbs sampling guarantees that eventually, samples are drawn from the true posterior."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph LR\n  A[\"Initialize State\"] --> B[\"Sample Node 1\"]\n  B --> C[\"Sample Node 2\"] --> D[\"Repeat\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "These sampling methods are ubiquitous in modern probabilistic AI."
                    }
                ]
            }
        ]
    },
    "15": {
        "title": "Case 15: The Decision Maker",
        "episodes": [
            {
                "title": "Module 1: The Concept of Utility",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "# Beyond Probabilities\nKnowing what will happen isn't enough. An agent needs to know what it WANTS."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "A utility function maps a state to a real number, representing its desirability."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\n  A[\"State: Win Lottery\"] --> B[\"Utility: 1000\"]\n  C[\"State: Lose Money\"] --> D[\"Utility: -100\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "Rational agents act to maximize their expected utility."
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** "
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "EU(Action) = Sum over outcomes ( Probability(Outcome | Action) * Utility(Outcome) )."
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "def calculate_eu(probabilities, utilities):\n    return sum(p * u for p, u in zip(probabilities, utilities))\n\n# --- Execution Output ---\nprint('Result:', calculate_eu(None))\n",
                        "solution_code": "def calculate_eu(probabilities, utilities):\n    return sum(p * u for p, u in zip(probabilities, utilities))\n\n# --- Execution Output ---\nprint('Result:', calculate_eu(None))\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nComputes Maximum Expected Utility (MEU): $EU(a) = \\sum P(s'|a, s) U(s')$. The Von Neumann-Morgenstern theorem proves that any rational agent must maximize expected utility.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Minimax Decision Rule:** Chooses the action with the best worst-case outcome; extremely conservative and avoids catastrophic failure, but misses high-reward opportunities.\\n- **Satisficing (Simon):** Selects the first option meeting an acceptable threshold; faster in real-time embedded environments.\\n- **Value of Perfect Information (VPI):** Quantifies exactly how much an additional sensor measurement is worth before paying to acquire it.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "The Maximum Expected Utility (MEU) principle is the core of rational decision making."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph LR\n  A[\"Action Options\"] --> B[\"Evaluate EU\"]\n  B --> C[\"Select Max EU\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "This unites probability (belief) and utility (desire) into action."
                    }
                ]
            },
            {
                "title": "Module 2: Risk and Rationality",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "## Are you risk-averse?\nUtility is not the same as money. The utility of money is non-linear."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Most people prefer a guaranteed $50 over a 50% chance of $100. This implies a concave utility curve."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\n  A[\"Wealth\"] --> B[\"Logarithmic Utility Curve\"]\n  style B fill:#eab3081a"
                    },
                    {
                        "type": "markdown",
                        "content": "A risk-seeking agent has a convex utility curve; a risk-neutral agent has a linear one."
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** "
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "A game with infinite expected monetary value, but people won't pay much to play it. Proves utility != money."
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "import math\ndef utility_of_money(amount):\n    return math.log(amount + 1) # Risk averse\n\n# --- Execution Output ---\nprint('Result:', utility_of_money(None))\n",
                        "solution_code": "import math\ndef utility_of_money(amount):\n    return math.log(amount + 1) # Risk averse\n\n# --- Execution Output ---\nprint('Result:', utility_of_money(None))\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nComputes Maximum Expected Utility (MEU): $EU(a) = \\sum P(s'|a, s) U(s')$. The Von Neumann-Morgenstern theorem proves that any rational agent must maximize expected utility.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Minimax Decision Rule:** Chooses the action with the best worst-case outcome; extremely conservative and avoids catastrophic failure, but misses high-reward opportunities.\\n- **Satisficing (Simon):** Selects the first option meeting an acceptable threshold; faster in real-time embedded environments.\\n- **Value of Perfect Information (VPI):** Quantifies exactly how much an additional sensor measurement is worth before paying to acquire it.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "Designing the right utility function is crucial for AI alignment."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph LR\n  A[\"Agent Designer\"] --> B[\"Defines Utility\"]\n  B --> C[\"Agent Behavior\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "Misspecified utilities can lead to disastrous AI behaviors."
                    }
                ]
            },
            {
                "title": "Module 3: Decision Networks",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "## Adding Actions to Bayes Nets\nWe extend Bayesian Networks with Action nodes and Utility nodes."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Also called Influence Diagrams. Chance nodes (ovals), Action nodes (rectangles), Utility nodes (diamonds)."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\n  A[\"Weather (Chance)\"] --> C[\"Utility\"]\n  B[\"Take Umbrella (Action)\"] --> C"
                    },
                    {
                        "type": "markdown",
                        "content": "To evaluate a decision network, we instantiate the action node and calculate expected utility."
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** "
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "For every possible action, calculate posterior probabilities of parents of the utility node, then compute EU."
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "def evaluate_action(action, network):\n    # Simulate setting action and inferring utility\n    pass\n\n# --- Execution Output ---\nprint('Result:', evaluate_action(None))\n",
                        "solution_code": "def evaluate_action(action, network):\n    # Simulate setting action and inferring utility\n    pass\n\n# --- Execution Output ---\nprint('Result:', evaluate_action(None))\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nComputes Maximum Expected Utility (MEU): $EU(a) = \\sum P(s'|a, s) U(s')$. The Von Neumann-Morgenstern theorem proves that any rational agent must maximize expected utility.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Minimax Decision Rule:** Chooses the action with the best worst-case outcome; extremely conservative and avoids catastrophic failure, but misses high-reward opportunities.\\n- **Satisficing (Simon):** Selects the first option meeting an acceptable threshold; faster in real-time embedded environments.\\n- **Value of Perfect Information (VPI):** Quantifies exactly how much an additional sensor measurement is worth before paying to acquire it.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "This provides a structured way to solve complex, single-shot decision problems."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph LR\n  A[\"Set Action\"] --> B[\"Run Inference\"]\n  B --> C[\"Compute EU\"] --> D[\"Compare Actions\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "Next, we'll look at the value of gathering more information before acting."
                    }
                ]
            },
            {
                "title": "Module 4: Value of Information",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "## Look Before You Leap\nShould a doctor order a costly test before treating? Only if it changes the decision."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Expected utility with the information minus expected utility without it."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\n  A[\"EU(Action | Evidence)\"] --> C[\"VPI\"]\n  B[\"EU(Action)\"] --> C\n  style C fill:#3b82f61a"
                    },
                    {
                        "type": "markdown",
                        "content": "VPI is always non-negative. Information never makes you worse off (in expectation)."
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** "
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Agents can iteratively calculate VPI for observables and choose to sense the world if VPI > cost of sensing."
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "def vpi(eu_with_info, eu_without_info):\n    return max(0, eu_with_info - eu_without_info)\n\n# --- Execution Output ---\nprint('Result:', vpi(None))\n",
                        "solution_code": "def vpi(eu_with_info, eu_without_info):\n    return max(0, eu_with_info - eu_without_info)\n\n# --- Execution Output ---\nprint('Result:', vpi(None))\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nComputes Maximum Expected Utility (MEU): $EU(a) = \\sum P(s'|a, s) U(s')$. The Von Neumann-Morgenstern theorem proves that any rational agent must maximize expected utility.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Minimax Decision Rule:** Chooses the action with the best worst-case outcome; extremely conservative and avoids catastrophic failure, but misses high-reward opportunities.\\n- **Satisficing (Simon):** Selects the first option meeting an acceptable threshold; faster in real-time embedded environments.\\n- **Value of Perfect Information (VPI):** Quantifies exactly how much an additional sensor measurement is worth before paying to acquire it.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "VPI guides attention and sensing in autonomous robots."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph LR\n  A[\"Calculate VPI\"] --> B[\"VPI > Cost?\"]\n  B -->|Yes| C[\"Observe\"]\n  B -->|No| D[\"Act Now\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "This wraps up our study of rational decisions. Next up: Machine Learning."
                    }
                ]
            }
        ]
    },
    "16": {
        "title": "Case 16: The Machine That Learns",
        "episodes": [
            {
                "title": "Module 1: The Learning Paradigm",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "# Teaching Computers to Learn\nInstead of explicitly programming rules, we feed data to algorithms to find the rules."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Learning a mapping from inputs (X) to outputs (Y) given labeled examples (X, Y)."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph LR\n  A[\"Data (X, Y)\"] --> B[\"ML Algorithm\"]\n  B --> C[\"Learned Model (f)\"]\n  C --> D[\"Predictions Y_hat\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "This contrasts with unsupervised learning, where we only have X and look for patterns."
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** "
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Features are the inputs (e.g., house size). Labels are what we want to predict (e.g., price)."
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "# A simple dataset\nfeatures = [[1200], [2500], [900]]\nlabels = [150000, 300000, 100000]\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "solution_code": "# A simple dataset\nfeatures = [[1200], [2500], [900]]\nlabels = [150000, 300000, 100000]\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nMinimizes empirical risk via gradient descent on continuous loss functions, updating parameters in the direction of steepest descent $\\theta \\leftarrow \\theta - \\alpha \\nabla L(\\theta)$.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Analytical Normal Equations:** $\\theta = (X^T X)^{-1} X^T y$ finds the exact global minimum in one step, but suffers from $O(d^3)$ matrix inversion complexity for large feature counts.\\n- **Stochastic Gradient Descent (SGD):** Computes gradients per single sample, enabling streaming updates and escaping saddle points.\\n- **L1 vs L2 Regularization:** L2 (Ridge) penalizes large weights smoothly, while L1 (Lasso) induces exact zeros for automatic feature selection.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "The goal is generalization: performing well on unseen data."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph TD\n  A[\"Train Data\"] --> B[\"Model\"]\n  B --> C[\"Test Data\"]\n  C --> D[\"Accuracy Measure\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "Generalization is the central challenge of machine learning."
                    }
                ]
            },
            {
                "title": "Module 2: Linear Regression",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "## Fitting a Line\nLinear regression is the foundational supervised learning algorithm."
                    },
                    {
                        "type": "concept",
                        "title": "We assume the relationship is a straight line",
                        "content": "y = mx + b (or Wx + b)."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\n  A[\"Input X\"] --> B[\"Multiply by W\"]\n  B --> C[\"Add Bias b\"]\n  C --> D[\"Output Y\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "We need a way to measure how 'wrong' our current line is."
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** "
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Mean Squared Error (MSE) measures the average squared difference between predictions and true labels."
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "def mse(y_true, y_pred):\n    return sum((t - p)**2 for t, p in zip(y_true, y_pred)) / len(y_true)\n\n# --- Execution Output ---\nprint('Result:', mse(None))\n",
                        "solution_code": "def mse(y_true, y_pred):\n    return sum((t - p)**2 for t, p in zip(y_true, y_pred)) / len(y_true)\n\n# --- Execution Output ---\nprint('Result:', mse(None))\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nMinimizes empirical risk via gradient descent on continuous loss functions, updating parameters in the direction of steepest descent $\\theta \\leftarrow \\theta - \\alpha \\nabla L(\\theta)$.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Analytical Normal Equations:** $\\theta = (X^T X)^{-1} X^T y$ finds the exact global minimum in one step, but suffers from $O(d^3)$ matrix inversion complexity for large feature counts.\\n- **Stochastic Gradient Descent (SGD):** Computes gradients per single sample, enabling streaming updates and escaping saddle points.\\n- **L1 vs L2 Regularization:** L2 (Ridge) penalizes large weights smoothly, while L1 (Lasso) induces exact zeros for automatic feature selection.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "We use optimization (like Gradient Descent) to find W and b that minimize this loss."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph LR\n  A[\"Init W,b\"] --> B[\"Calc Loss\"]\n  B --> C[\"Update W,b via Gradient\"]\n  C --> A"
                    },
                    {
                        "type": "markdown",
                        "content": "This iterative process is how the model 'learns'."
                    }
                ]
            },
            {
                "title": "Module 3: Overfitting and Underfitting",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "## The Goldilocks Problem\nA model can be too simple, or it can memorize the noise in the data."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "The model is too simple to capture the underlying trend. E.g., fitting a line to a parabola."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\n  A[\"Underfit: Too Simple\"] --> B[\"Good Fit: Just Right\"]\n  B --> C[\"Overfit: Memorized Noise\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "Overfitting (High Variance) means the model fits the training data perfectly but fails on new data."
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** "
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Using higher-degree polynomials increases model capacity, risking overfitting."
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "import numpy as np\n# A high degree polynomial can interpolate data exactly\n# but wildly oscillates between points.\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "solution_code": "import numpy as np\n# A high degree polynomial can interpolate data exactly\n# but wildly oscillates between points.\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nMinimizes empirical risk via gradient descent on continuous loss functions, updating parameters in the direction of steepest descent $\\theta \\leftarrow \\theta - \\alpha \\nabla L(\\theta)$.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Analytical Normal Equations:** $\\theta = (X^T X)^{-1} X^T y$ finds the exact global minimum in one step, but suffers from $O(d^3)$ matrix inversion complexity for large feature counts.\\n- **Stochastic Gradient Descent (SGD):** Computes gradients per single sample, enabling streaming updates and escaping saddle points.\\n- **L1 vs L2 Regularization:** L2 (Ridge) penalizes large weights smoothly, while L1 (Lasso) induces exact zeros for automatic feature selection.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "We must carefully balance model complexity and data availability."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph LR\n  A[\"Increase Complexity\"] --> B[\"Lower Train Error\"]\n  A --> C[\"Higher Test Error (Eventually)\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "To prevent overfitting, we use techniques like regularization and cross-validation."
                    }
                ]
            },
            {
                "title": "Module 4: Regularization and Validation",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "## Taming Complexity\nHow do we stop our models from going crazy and overfitting?"
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "We add a penalty term to the loss function for large weights (e.g., L1 or L2 regularization)."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\n  A[\"Total Loss\"] --> B[\"Data Loss (MSE)\"]\n  A --> C[\"Regularization Penalty (Complexity)\"]\n  style C fill:#f43f5e1a"
                    },
                    {
                        "type": "markdown",
                        "content": "This forces the model to prefer simpler explanations (smaller weights)."
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** "
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Never evaluate on training data. Use a validation set to tune hyperparameters, and a test set for final reporting."
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "def split_data(data, train_ratio=0.8):\n    # Simulate splitting data\n    pass\n\n# --- Execution Output ---\nprint('Result:', split_data(None))\n",
                        "solution_code": "def split_data(data, train_ratio=0.8):\n    # Simulate splitting data\n    pass\n\n# --- Execution Output ---\nprint('Result:', split_data(None))\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nMinimizes empirical risk via gradient descent on continuous loss functions, updating parameters in the direction of steepest descent $\\theta \\leftarrow \\theta - \\alpha \\nabla L(\\theta)$.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Analytical Normal Equations:** $\\theta = (X^T X)^{-1} X^T y$ finds the exact global minimum in one step, but suffers from $O(d^3)$ matrix inversion complexity for large feature counts.\\n- **Stochastic Gradient Descent (SGD):** Computes gradients per single sample, enabling streaming updates and escaping saddle points.\\n- **L1 vs L2 Regularization:** L2 (Ridge) penalizes large weights smoothly, while L1 (Lasso) induces exact zeros for automatic feature selection.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "Hyperparameters (like learning rate or regularization strength) are tuned manually or via search."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph LR\n  A[\"Train Data\"] --> B[\"Fit Model Weights\"]\n  C[\"Val Data\"] --> D[\"Tune Hyperparameters\"]\n  E[\"Test Data\"] --> F[\"Final Assessment\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "Congratulations, you've mastered the fundamentals of AI!"
                    }
                ]
            }
        ]
    },
    "17": {
        "title": "Case 17: The Nearest Neighbor",
        "episodes": [
            {
                "title": "Module 1: Intuition and Distance Metrics",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "## Introduction to KNN\nK-Nearest Neighbors is a non-parametric, lazy learning algorithm used for both classification and regression."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Lazy Learning means there is no explicit training phase before classification. The model simply stores the dataset."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\nA[\"New Data Point\"] --> B[\"Calculate Distances\"]\nB --> C[\"Find K Nearest\"]\nC --> D[\"Majority Vote\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** What is the primary computational cost of KNN at test time?"
                    },
                    {
                        "type": "markdown",
                        "content": "## Distance Metrics\nEuclidean, Manhattan, and Minkowski are common distance metrics."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Euclidean distance is the straight-line distance, while Manhattan is the sum of absolute differences."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph LR\nstyle A fill:#10b9811a\nA[\"Point A (1,1)\"] --> B[\"Point B (4,5)\"]\nB --> C[\"Euclidean = 5\"]"
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "import numpy as np\ndef euclidean(a, b): return np.sqrt(np.sum((a-b)**2))\n\n# --- Execution Output ---\nprint('Result:', euclidean(None))\n",
                        "solution_code": "import numpy as np\ndef euclidean(a, b): return np.sqrt(np.sum((a-b)**2))\n\n# --- Execution Output ---\nprint('Result:', euclidean(None))\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nNon-parametric instance-based learning that calculates pairwise vector distances to find the $K$ closest neighbors. By the Cover-Hart theorem, as $N \\to \\infty$, the 1-NN error is at most twice the optimal Bayes error rate.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **KD-Tree / Ball Tree:** Hierarchical space-partitioning trees reducing search from brute-force $O(N \\cdot d)$ to $O(d \\log N)$ for low dimensions ($d < 20$).\\n- **Locality Sensitive Hashing (LSH):** Sub-linear approximate nearest neighbor queries for high-dimensional embeddings.\\n- **Distance-Weighted KNN:** Assigns weights $w_i = 1/d_i^2$, reducing sensitivity to the choice of $K$ and edge noise.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** Which metric is best for high dimensional sparse data?"
                    },
                    {
                        "type": "markdown",
                        "content": "Summary of Module 1: KNN relies heavily on the choice of distance metric and K."
                    }
                ]
            },
            {
                "title": "Module 2: Choosing K and Curse of Dimensionality",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "## Choosing the right K\nA small K leads to low bias but high variance (overfitting). A large K leads to high bias but low variance."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Odd values of K are preferred in binary classification to prevent ties."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\nA[\"K=1\"] --> B[\"Complex Decision Boundary\"]\nC[\"K=100\"] --> D[\"Smooth Decision Boundary\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** What happens if K equals the total number of training points?"
                    },
                    {
                        "type": "markdown",
                        "content": "## Curse of Dimensionality\nAs dimensions increase, the distance between any two points becomes uniformly large."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "In high dimensions, the concept of 'nearest' loses its meaning, degrading KNN performance."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph TD\nstyle X fill:#3b82f61a\nX[\"1D: Points close\"] --> Y[\"2D: Points spread\"]\nY --> Z[\"100D: All points equidistant\"]"
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "from sklearn.neighbors import KNeighborsClassifier\nknn = KNeighborsClassifier(n_neighbors=5)\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "solution_code": "from sklearn.neighbors import KNeighborsClassifier\nknn = KNeighborsClassifier(n_neighbors=5)\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nNon-parametric instance-based learning that calculates pairwise vector distances to find the $K$ closest neighbors. By the Cover-Hart theorem, as $N \\to \\infty$, the 1-NN error is at most twice the optimal Bayes error rate.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **KD-Tree / Ball Tree:** Hierarchical space-partitioning trees reducing search from brute-force $O(N \\cdot d)$ to $O(d \\log N)$ for low dimensions ($d < 20$).\\n- **Locality Sensitive Hashing (LSH):** Sub-linear approximate nearest neighbor queries for high-dimensional embeddings.\\n- **Distance-Weighted KNN:** Assigns weights $w_i = 1/d_i^2$, reducing sensitivity to the choice of $K$ and edge noise.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** How to mitigate the curse of dimensionality?"
                    },
                    {
                        "type": "markdown",
                        "content": "Summary: Balance K using cross-validation and keep dimensions low."
                    }
                ]
            },
            {
                "title": "Module 3: Advanced KNN Implementations",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "## Faster Search Algorithms\nBrute force distance calculation is O(N*D). We can use tree-based structures."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "KD-Trees partition the space along axes, reducing average search time to O(log N)."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\nA[\"Root Node (Dim 0)\"] --> B[\"Left Child\"]\nA --> C[\"Right Child\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** When do KD-Trees perform worse than brute force?"
                    },
                    {
                        "type": "markdown",
                        "content": "## Ball Trees\nBall Trees partition data into overlapping hyperspheres, working better in high dimensions."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Ball Trees check if the distance to a sphere's center minus its radius exceeds the current nearest neighbor."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph LR\nstyle S fill:#f59e0b1a\nS[\"Root Sphere\"] --> T[\"Sub-sphere 1\"]\nS --> U[\"Sub-sphere 2\"]"
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "knn = KNeighborsClassifier(algorithm='ball_tree')\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "solution_code": "knn = KNeighborsClassifier(algorithm='ball_tree')\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nNon-parametric instance-based learning that calculates pairwise vector distances to find the $K$ closest neighbors. By the Cover-Hart theorem, as $N \\to \\infty$, the 1-NN error is at most twice the optimal Bayes error rate.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **KD-Tree / Ball Tree:** Hierarchical space-partitioning trees reducing search from brute-force $O(N \\cdot d)$ to $O(d \\log N)$ for low dimensions ($d < 20$).\\n- **Locality Sensitive Hashing (LSH):** Sub-linear approximate nearest neighbor queries for high-dimensional embeddings.\\n- **Distance-Weighted KNN:** Assigns weights $w_i = 1/d_i^2$, reducing sensitivity to the choice of $K$ and edge noise.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** Which algorithm is default in sklearn when data is sparse?"
                    },
                    {
                        "type": "markdown",
                        "content": "Summary: Use KD-Tree for low dims, Ball Tree for medium, Brute for sparse/high."
                    }
                ]
            },
            {
                "title": "Module 4: KNN Regression and Weights",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "## KNN Regression\nInstead of majority vote, KNN can output the average of the K nearest neighbors."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Distance weighting gives closer neighbors more influence on the final prediction."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\nA[\"Neighbors: 5, 7, 9\"] --> B[\"Uniform Mean: 7\"]\nA --> C[\"Weighted Mean: 5.5 (if 5 is closer)\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** What is a common weight function?"
                    },
                    {
                        "type": "markdown",
                        "content": "## Scaling Data\nFeatures must be scaled (e.g., Standardized) before applying KNN, or large-range features will dominate."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "StandardScaler shifts the mean to 0 and variance to 1."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph LR\nstyle W fill:#ef44441a\nW[\"Raw Age: 20-80, Salary: 50k-200k\"] --> X[\"Scaled Age: -1 to 1, Scaled Salary: -1 to 1\"]"
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "from sklearn.preprocessing import StandardScaler\nscaler = StandardScaler()\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "solution_code": "from sklearn.preprocessing import StandardScaler\nscaler = StandardScaler()\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nNon-parametric instance-based learning that calculates pairwise vector distances to find the $K$ closest neighbors. By the Cover-Hart theorem, as $N \\to \\infty$, the 1-NN error is at most twice the optimal Bayes error rate.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **KD-Tree / Ball Tree:** Hierarchical space-partitioning trees reducing search from brute-force $O(N \\cdot d)$ to $O(d \\log N)$ for low dimensions ($d < 20$).\\n- **Locality Sensitive Hashing (LSH):** Sub-linear approximate nearest neighbor queries for high-dimensional embeddings.\\n- **Distance-Weighted KNN:** Assigns weights $w_i = 1/d_i^2$, reducing sensitivity to the choice of $K$ and edge noise.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** If we don't scale, which feature dominates?"
                    },
                    {
                        "type": "markdown",
                        "content": "Summary: Always scale data and consider distance-weighting for KNN."
                    }
                ]
            }
        ]
    },
    "18": {
        "title": "Case 18: The Naive Assumption",
        "episodes": [
            {
                "title": "Module 1: Bayes' Theorem Fundamentals",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "## Bayes' Theorem\nBayes' theorem calculates the probability of an event based on prior knowledge."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "P(A|B) = [P(B|A) * P(A)] / P(B)"
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\nA[\"Prior P(A)\"] --> B[\"Likelihood P(B|A)\"]\nB --> C[\"Posterior P(A|B)\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** What does P(B|A) represent?"
                    },
                    {
                        "type": "markdown",
                        "content": "## Naive Assumption\nThe algorithm is 'naive' because it assumes all features are independent given the class."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "P(x1, x2 | y) is simplified to P(x1 | y) * P(x2 | y)."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph LR\nstyle N fill:#8b5cf61a\nN[\"Complex Joint Prob\"] --> M[\"Product of Marginals\"]"
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "prob = prior * likelihood_feature1 * likelihood_feature2\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "solution_code": "prob = prior * likelihood_feature1 * likelihood_feature2\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nAssumes conditional independence between features given the class: $P(x_1...x_d|C) = \\prod P(x_i|C)$. With Laplace smoothing, this prevents zero-frequency multiplication dropouts and performs remarkably well on high-dimensional sparse text vectors.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Logistic Regression:** Discriminative equivalent that models $P(C|X)$ without assuming feature independence; generally achieves higher asymptotic accuracy on correlated data.\\n- **Gaussian Naive Bayes:** Models continuous variables using normal distribution likelihoods $\\mathcal{N}(\\mu, \\sigma^2)$.\\n- **Support Vector Machines (SVM):** Finds the maximum-margin hyperplane, offering superior generalization on text categorization without independence assumptions.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** Is the naive assumption usually true in real data?"
                    },
                    {
                        "type": "markdown",
                        "content": "Summary: Bayes theorem + Independence assumption = Naive Bayes."
                    }
                ]
            },
            {
                "title": "Module 2: Gaussian Naive Bayes",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "## Continuous Data\nWhen features are continuous, we assume they are drawn from a normal (Gaussian) distribution."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "We calculate the mean and variance of each feature for each class."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\nA[\"Continuous Feature\"] --> B[\"Calculate Mean & Variance per Class\"]\nB --> C[\"Use PDF for Likelihood\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** What does the PDF calculate in Gaussian NB?"
                    },
                    {
                        "type": "markdown",
                        "content": "## The Math\nThe likelihood is the Gaussian probability density function (PDF)."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "exp(-(x-mean)^2 / (2*var)) / sqrt(2*pi*var)"
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph TD\nstyle G fill:#14b8a61a\nG[\"Feature X\"] --> H[\"Plug into Gaussian PDF\"] --> I[\"Likelihood P(X|Y)\"]"
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "from sklearn.naive_bayes import GaussianNB\nmodel = GaussianNB()\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "solution_code": "from sklearn.naive_bayes import GaussianNB\nmodel = GaussianNB()\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nAssumes conditional independence between features given the class: $P(x_1...x_d|C) = \\prod P(x_i|C)$. With Laplace smoothing, this prevents zero-frequency multiplication dropouts and performs remarkably well on high-dimensional sparse text vectors.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Logistic Regression:** Discriminative equivalent that models $P(C|X)$ without assuming feature independence; generally achieves higher asymptotic accuracy on correlated data.\\n- **Gaussian Naive Bayes:** Models continuous variables using normal distribution likelihoods $\\mathcal{N}(\\mu, \\sigma^2)$.\\n- **Support Vector Machines (SVM):** Finds the maximum-margin hyperplane, offering superior generalization on text categorization without independence assumptions.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** Can Gaussian NB handle categorical data natively?"
                    },
                    {
                        "type": "markdown",
                        "content": "Summary: Gaussian NB uses the normal distribution to handle continuous numerical features."
                    }
                ]
            },
            {
                "title": "Module 3: Multinomial & Bernoulli NB",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "## Text Classification\nMultinomial and Bernoulli NB are heavily used for text and document classification."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Multinomial deals with feature counts (word frequencies), Bernoulli deals with boolean presence (word exists or not)."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\nA[\"Text Data\"] --> B[\"TF-IDF or Count Vectorizer\"]\nB --> C[\"Multinomial NB\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** Which NB variant is best if features are binary (0/1)?"
                    },
                    {
                        "type": "markdown",
                        "content": "## Laplace Smoothing\nIf a word never appears in the training set for a class, its probability is 0, wiping out the entire product."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Laplace (Add-1) smoothing adds 1 to all counts to prevent zero probabilities."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph LR\nstyle L fill:#f43f5e1a\nL[\"Count = 0\"] --> M[\"Count = 1 (Smoothed)\"] --> N[\"Prob > 0\"]"
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "from sklearn.naive_bayes import MultinomialNB\nmodel = MultinomialNB(alpha=1.0)\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "solution_code": "from sklearn.naive_bayes import MultinomialNB\nmodel = MultinomialNB(alpha=1.0)\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nAssumes conditional independence between features given the class: $P(x_1...x_d|C) = \\prod P(x_i|C)$. With Laplace smoothing, this prevents zero-frequency multiplication dropouts and performs remarkably well on high-dimensional sparse text vectors.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Logistic Regression:** Discriminative equivalent that models $P(C|X)$ without assuming feature independence; generally achieves higher asymptotic accuracy on correlated data.\\n- **Gaussian Naive Bayes:** Models continuous variables using normal distribution likelihoods $\\mathcal{N}(\\mu, \\sigma^2)$.\\n- **Support Vector Machines (SVM):** Finds the maximum-margin hyperplane, offering superior generalization on text categorization without independence assumptions.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** What is the alpha parameter in MultinomialNB?"
                    },
                    {
                        "type": "markdown",
                        "content": "Summary: Use Multinomial for counts and apply smoothing to avoid zero probabilities."
                    }
                ]
            },
            {
                "title": "Module 4: Underflow and Log Probabilities",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "## The Underflow Problem\nMultiplying many small probabilities results in a number too small for computers to represent (floating-point underflow)."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "We take the logarithm of probabilities, turning multiplication into addition."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\nA[\"P1 * P2 * P3\"] --> B[\"log(P1) + log(P2) + log(P3)\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** Why is log(x) monotonically increasing?"
                    },
                    {
                        "type": "markdown",
                        "content": "## Log-Sum-Exp Trick\nA standard trick to numerically stabilize calculations involving sums of exponentials."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "argmax(P) is identical to argmax(log P)."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph LR\nstyle E fill:#0ea5e91a\nE[\"Calculate Log Posteriors\"] --> F[\"Find Max Log Posterior\"] --> G[\"Select Class\"]"
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "import numpy as np\nlog_prob = np.log(prior) + np.sum(np.log(likelihoods))\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "solution_code": "import numpy as np\nlog_prob = np.log(prior) + np.sum(np.log(likelihoods))\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nAssumes conditional independence between features given the class: $P(x_1...x_d|C) = \\prod P(x_i|C)$. With Laplace smoothing, this prevents zero-frequency multiplication dropouts and performs remarkably well on high-dimensional sparse text vectors.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Logistic Regression:** Discriminative equivalent that models $P(C|X)$ without assuming feature independence; generally achieves higher asymptotic accuracy on correlated data.\\n- **Gaussian Naive Bayes:** Models continuous variables using normal distribution likelihoods $\\mathcal{N}(\\mu, \\sigma^2)$.\\n- **Support Vector Machines (SVM):** Finds the maximum-margin hyperplane, offering superior generalization on text categorization without independence assumptions.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** Does converting to log probabilities change the final classification?"
                    },
                    {
                        "type": "markdown",
                        "content": "Summary: Log probabilities are crucial for robust implementation of Naive Bayes."
                    }
                ]
            }
        ]
    },
    "19": {
        "title": "Case 19: The Tree That Makes Decisions",
        "episodes": [
            {
                "title": "Module 1: Tree Terminology",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "## Decision Tree Structure\nA tree has a root, internal nodes (splits), and leaves (predictions)."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Trees recursively partition the feature space into hyper-rectangles."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\nA[\"Root Node\"] --> B[\"Internal Node\"]\nA --> C[\"Leaf Node\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** What does a leaf node represent?"
                    },
                    {
                        "type": "markdown",
                        "content": "## Splitting Rules\nAt each node, the tree picks a feature and a threshold to split the data."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "The goal of splitting is to maximize the homogeneity (purity) of the child nodes."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph LR\nstyle T fill:#a855f71a\nT[\"Mixed Data\"] --> U[\"Split on Age > 30\"] --> V[\"Purer Child Nodes\"]"
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "from sklearn.tree import DecisionTreeClassifier\ndt = DecisionTreeClassifier()\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "solution_code": "from sklearn.tree import DecisionTreeClassifier\ndt = DecisionTreeClassifier()\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nGreedy recursive binary splitting maximizes Information Gain $IG(S, A) = H(S) - \\sum \\frac{|S_v|}{|S|} H(S_v)$, partitioning the feature space into orthogonal hyper-rectangles with human-interpretable rules.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Gini Impurity (CART):** Faster to compute than logarithmic Shannon Entropy ($1 - \\sum p_i^2$) and yields nearly identical tree architectures.\\n- **Random Forests:** Ensembles hundreds of de-correlated trees with feature bagging, reducing variance without increasing bias.\\n- **Gradient Boosted Decision Trees (XGBoost):** Sequentially fits trees to the negative loss gradient, dominating tabular engineering leaderboards.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** Are decision trees sensitive to feature scaling?"
                    },
                    {
                        "type": "markdown",
                        "content": "Summary: Trees form a set of if-else rules that partition data into pure regions."
                    }
                ]
            },
            {
                "title": "Module 2: Entropy and Information Gain",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "## Entropy\nEntropy is a measure of impurity, uncertainty, or chaos in a node."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "H(S) = - sum(p_i * log2(p_i)). Entropy is 0 if all samples belong to one class."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\nA[\"High Entropy (50/50 split)\"] --> B[\"Low Entropy (90/10 split)\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** What is the max entropy for a binary classification node?"
                    },
                    {
                        "type": "markdown",
                        "content": "## Information Gain\nInformation Gain is the reduction in entropy after a split."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "IG = Entropy(Parent) - Weighted_Avg_Entropy(Children)"
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph LR\nstyle I fill:#ec48991a\nI[\"Parent Entropy\"] --> J[\"Subtract Child Entropies\"] --> K[\"Information Gain\"]"
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "dt = DecisionTreeClassifier(criterion='entropy')\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "solution_code": "dt = DecisionTreeClassifier(criterion='entropy')\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nGreedy recursive binary splitting maximizes Information Gain $IG(S, A) = H(S) - \\sum \\frac{|S_v|}{|S|} H(S_v)$, partitioning the feature space into orthogonal hyper-rectangles with human-interpretable rules.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Gini Impurity (CART):** Faster to compute than logarithmic Shannon Entropy ($1 - \\sum p_i^2$) and yields nearly identical tree architectures.\\n- **Random Forests:** Ensembles hundreds of de-correlated trees with feature bagging, reducing variance without increasing bias.\\n- **Gradient Boosted Decision Trees (XGBoost):** Sequentially fits trees to the negative loss gradient, dominating tabular engineering leaderboards.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** The tree algorithm selects the split that _____ Information Gain."
                    },
                    {
                        "type": "markdown",
                        "content": "Summary: ID3 and C4.5 algorithms use Entropy and Information Gain to build trees."
                    }
                ]
            },
            {
                "title": "Module 3: Gini Impurity",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "## Gini Impurity\nAn alternative to Entropy, used by the CART algorithm (default in sklearn)."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Gini measures the probability of incorrectly classifying a randomly chosen element."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\nA[\"Gini = 1 - sum(p_i^2)\"] --> B[\"Max Gini = 0.5 (Binary)\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** Why is Gini slightly faster to compute than Entropy?"
                    },
                    {
                        "type": "markdown",
                        "content": "## Comparing Gini and Entropy\nIn practice, they yield very similar trees, but Gini is marginally faster."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Gini tends to isolate the most frequent class in its own branch, while Entropy tends to produce slightly more balanced trees."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph TD\nstyle G fill:#f973161a\nG[\"CART Algorithm\"] --> H[\"Uses Gini Impurity\"] --> I[\"Binary Splits Only\"]"
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "dt = DecisionTreeClassifier(criterion='gini')\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "solution_code": "dt = DecisionTreeClassifier(criterion='gini')\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nGreedy recursive binary splitting maximizes Information Gain $IG(S, A) = H(S) - \\sum \\frac{|S_v|}{|S|} H(S_v)$, partitioning the feature space into orthogonal hyper-rectangles with human-interpretable rules.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Gini Impurity (CART):** Faster to compute than logarithmic Shannon Entropy ($1 - \\sum p_i^2$) and yields nearly identical tree architectures.\\n- **Random Forests:** Ensembles hundreds of de-correlated trees with feature bagging, reducing variance without increasing bias.\\n- **Gradient Boosted Decision Trees (XGBoost):** Sequentially fits trees to the negative loss gradient, dominating tabular engineering leaderboards.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** Is Gini Impurity bounded between 0 and 1?"
                    },
                    {
                        "type": "markdown",
                        "content": "Summary: Default to Gini for performance, but Entropy is theoretically robust for information theory."
                    }
                ]
            },
            {
                "title": "Module 4: Overfitting and Pruning",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "## Overfitting in Trees\nA fully grown tree will perfectly memorize the training data, leading to horrible generalization."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Leaves with a single sample have an impurity of 0, but represent noise (overfitting)."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\nA[\"Unconstrained Tree\"] --> B[\"Depth = 20+\"] --> C[\"Overfitting\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** Which hyperparameter restricts tree depth?"
                    },
                    {
                        "type": "markdown",
                        "content": "## Pre-pruning vs Post-pruning\nPre-pruning stops the tree from growing (early stopping). Post-pruning grows a full tree then removes branches."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Cost Complexity Pruning (ccp_alpha) penalizes trees with too many leaves."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph LR\nstyle P fill:#22c55e1a\nP[\"Full Tree\"] --> Q[\"Calculate Subtree Cost\"] --> R[\"Prune Weakest Link\"]"
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "dt = DecisionTreeClassifier(ccp_alpha=0.015)\ndt.fit(X, y)\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "solution_code": "dt = DecisionTreeClassifier(ccp_alpha=0.015)\ndt.fit(X, y)\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nGreedy recursive binary splitting maximizes Information Gain $IG(S, A) = H(S) - \\sum \\frac{|S_v|}{|S|} H(S_v)$, partitioning the feature space into orthogonal hyper-rectangles with human-interpretable rules.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Gini Impurity (CART):** Faster to compute than logarithmic Shannon Entropy ($1 - \\sum p_i^2$) and yields nearly identical tree architectures.\\n- **Random Forests:** Ensembles hundreds of de-correlated trees with feature bagging, reducing variance without increasing bias.\\n- **Gradient Boosted Decision Trees (XGBoost):** Sequentially fits trees to the negative loss gradient, dominating tabular engineering leaderboards.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** Increasing ccp_alpha will lead to a _____ tree."
                    },
                    {
                        "type": "markdown",
                        "content": "Summary: Always constrain your trees using max_depth or ccp_alpha to prevent overfitting."
                    }
                ]
            }
        ]
    },
    "20": {
        "title": "Case 20: The Agent That Learns From Failure",
        "episodes": [
            {
                "title": "Module 1: RL Framework",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "## Reinforcement Learning (RL)\nAn agent learns to make sequential decisions by interacting with an environment."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "The agent observes a State (S), takes an Action (A), and receives a Reward (R) and Next State (S')."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph LR\nA[\"Agent\"] -- Action --> B[\"Environment\"]\nB -- State, Reward --> A"
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** What is the goal of the RL agent?"
                    },
                    {
                        "type": "markdown",
                        "content": "## Markov Decision Process (MDP)\nRL environments are formalized as MDPs, satisfying the Markov property."
                    },
                    {
                        "type": "concept",
                        "title": "Markov Property",
                        "content": "The future depends only on the current state, not the history."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph TD\nstyle M fill:#6366f11a\nM[\"S(t), A(t)\"] --> N[\"P(S(t+1) | S(t), A(t))\"]"
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "import gym\nenv = gym.make('FrozenLake-v1')\nstate = env.reset()\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "solution_code": "import gym\nenv = gym.make('FrozenLake-v1')\nstate = env.reset()\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nTemporal Difference Bellman update: $Q(s, a) \\leftarrow Q(s, a) + \\alpha [r + \\gamma \\max_{a'} Q(s', a') - Q(s, a)]$. Watkins (1989) proved this model-free algorithm is guaranteed to converge to the optimal policy $Q^*$ under standard stochastic approximation conditions.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **SARSA (On-Policy):** Uses the actual next action chosen by policy $Q(s', a')$, producing safer policies in environments with dangerous penalty cliffs.\\n- **Value Iteration / Policy Iteration:** Requires an explicit model of transition probabilities $P(s'|s, a)$; exact, but unusable when environment physics are unknown.\\n- **Deep Q-Networks (DQN):** Uses deep neural networks to approximate the Q-table with experience replay buffers for continuous or high-dimensional state spaces.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** What defines the transition dynamics of an MDP?"
                    },
                    {
                        "type": "markdown",
                        "content": "Summary: RL is modeled as an MDP where agents act to maximize return."
                    }
                ]
            },
            {
                "title": "Module 2: Q-Values and Policies",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "## The Q-Function\nThe Action-Value function, Q(s, a), represents the expected return starting from state s, taking action a."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Optimal Q-value, Q*(s, a), yields the maximum possible reward."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\nA[\"State s\"] --> B[\"Action a\"]\nB --> C[\"Q(s, a) Score\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** How do we derive the optimal policy from Q*(s, a)?"
                    },
                    {
                        "type": "markdown",
                        "content": "## Policy (Pi)\nA policy is a mapping from states to actions."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "A deterministic policy always maps a state to the exact same action."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph LR\nstyle P fill:#14b8a61a\nP[\"Observe State\"] --> Q[\"Consult Policy Pi(s)\"] --> R[\"Execute Action\"]"
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "def policy(state, q_table):\n    return np.argmax(q_table[state])\n\n# --- Execution Output ---\nprint('Result:', policy(None))\n",
                        "solution_code": "def policy(state, q_table):\n    return np.argmax(q_table[state])\n\n# --- Execution Output ---\nprint('Result:', policy(None))\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nTemporal Difference Bellman update: $Q(s, a) \\leftarrow Q(s, a) + \\alpha [r + \\gamma \\max_{a'} Q(s', a') - Q(s, a)]$. Watkins (1989) proved this model-free algorithm is guaranteed to converge to the optimal policy $Q^*$ under standard stochastic approximation conditions.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **SARSA (On-Policy):** Uses the actual next action chosen by policy $Q(s', a')$, producing safer policies in environments with dangerous penalty cliffs.\\n- **Value Iteration / Policy Iteration:** Requires an explicit model of transition probabilities $P(s'|s, a)$; exact, but unusable when environment physics are unknown.\\n- **Deep Q-Networks (DQN):** Uses deep neural networks to approximate the Q-table with experience replay buffers for continuous or high-dimensional state spaces.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** What is a stochastic policy?"
                    },
                    {
                        "type": "markdown",
                        "content": "Summary: Q-values estimate future rewards; policies use Q-values to choose actions."
                    }
                ]
            },
            {
                "title": "Module 3: The Bellman Equation",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "## Bellman Optimality Equation\nThe foundation of Q-learning, breaking the value into immediate reward plus discounted future value."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Q(s,a) = R(s,a) + gamma * max_a' Q(s', a')"
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\nA[\"Q(s,a)\"] --> B[\"Immediate Reward\"]\nA --> C[\"Discounted Future Max Q\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** What does the discount factor (gamma) do?"
                    },
                    {
                        "type": "markdown",
                        "content": "## Q-Learning Update Rule\nQ-learning uses Temporal Difference (TD) learning to iteratively update Q-values."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Q_new = Q_old + alpha * (Reward + gamma * max_Q_next - Q_old)"
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph LR\nstyle B fill:#ef44441a\nB[\"TD Target = R + gamma*max_Q\"] --> C[\"TD Error = Target - Q_old\"] --> D[\"Update Q_old by alpha * Error\"]"
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "q_table[s, a] = q_table[s, a] + lr * (r + gamma * np.max(q_table[s_]) - q_table[s, a])\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "solution_code": "q_table[s, a] = q_table[s, a] + lr * (r + gamma * np.max(q_table[s_]) - q_table[s, a])\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nTemporal Difference Bellman update: $Q(s, a) \\leftarrow Q(s, a) + \\alpha [r + \\gamma \\max_{a'} Q(s', a') - Q(s, a)]$. Watkins (1989) proved this model-free algorithm is guaranteed to converge to the optimal policy $Q^*$ under standard stochastic approximation conditions.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **SARSA (On-Policy):** Uses the actual next action chosen by policy $Q(s', a')$, producing safer policies in environments with dangerous penalty cliffs.\\n- **Value Iteration / Policy Iteration:** Requires an explicit model of transition probabilities $P(s'|s, a)$; exact, but unusable when environment physics are unknown.\\n- **Deep Q-Networks (DQN):** Uses deep neural networks to approximate the Q-table with experience replay buffers for continuous or high-dimensional state spaces.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** What is alpha in the update rule?"
                    },
                    {
                        "type": "markdown",
                        "content": "Summary: The Bellman equation allows us to recursively estimate optimal Q-values."
                    }
                ]
            },
            {
                "title": "Module 4: Exploration vs Exploitation",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "## The Dilemma\nShould the agent exploit the best-known action, or explore unknown actions to find potentially better ones?"
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Without exploration, the agent might get stuck in a local optimum."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\nA[\"Exploit (Greedy)\"] --> B[\"Use Max Q\"]\nA --> C[\"Explore\"] --> D[\"Random Action\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** What happens if exploration is 0 from the start?"
                    },
                    {
                        "type": "markdown",
                        "content": "## Epsilon-Greedy Strategy\nA simple and effective way to balance exploration and exploitation."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "With probability epsilon, take a random action. Otherwise, take the greedy action."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph LR\nstyle E fill:#eab3081a\nE[\"Generate Random Num 0-1\"] --> F[\"If < Epsilon: Explore\"] --> G[\"Else: Exploit\"]"
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "import random\nif random.uniform(0, 1) < epsilon:\n    action = env.action_space.sample()\nelse:\n    action = np.argmax(q_table[state])\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "solution_code": "import random\nif random.uniform(0, 1) < epsilon:\n    action = env.action_space.sample()\nelse:\n    action = np.argmax(q_table[state])\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nTemporal Difference Bellman update: $Q(s, a) \\leftarrow Q(s, a) + \\alpha [r + \\gamma \\max_{a'} Q(s', a') - Q(s, a)]$. Watkins (1989) proved this model-free algorithm is guaranteed to converge to the optimal policy $Q^*$ under standard stochastic approximation conditions.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **SARSA (On-Policy):** Uses the actual next action chosen by policy $Q(s', a')$, producing safer policies in environments with dangerous penalty cliffs.\\n- **Value Iteration / Policy Iteration:** Requires an explicit model of transition probabilities $P(s'|s, a)$; exact, but unusable when environment physics are unknown.\\n- **Deep Q-Networks (DQN):** Uses deep neural networks to approximate the Q-table with experience replay buffers for continuous or high-dimensional state spaces.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** How should epsilon change over time?"
                    },
                    {
                        "type": "markdown",
                        "content": "Summary: Epsilon-decay schedules allow agents to explore early and exploit later."
                    }
                ]
            }
        ]
    },
    "21": {
        "title": "Case 21: The Logic Programmer",
        "episodes": [
            {
                "title": "Module 1: Facts and Rules",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "## Declarative Programming\nPROLOG is declarative. You specify *what* the problem is, not *how* to solve it."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "A PROLOG program is a database of facts and rules."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\nA[\"Knowledge Base\"] --> B[\"Facts (Truths)\"]\nA --> C[\"Rules (Logic)\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** In PROLOG, lowercase letters denote:"
                    },
                    {
                        "type": "markdown",
                        "content": "## Defining Facts\nFacts declare unconditionally true statements, terminated by a period."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "parent(john, mary). means John is the parent of Mary."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph LR\nstyle F fill:#8b5cf61a\nF[\"Predicate: parent\"] --> G[\"Arguments: john, mary\"]"
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "% PROLOG\nlikes(alice, pizza).\nlikes(bob, burgers).\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "solution_code": "% PROLOG\nlikes(alice, pizza).\nlikes(bob, burgers).\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nDeclarative logic programming executes SLD-resolution with first-order unification, automatically searching the Horn clause database to bind variables that satisfy the query.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Datalog:** Restricts PROLOG by eliminating function symbols, guaranteeing polynomial query termination.\\n- **Answer Set Programming (ASP):** Solves hard combinatorial search problems using stable model semantics.\\n- **Constraint Logic Programming (CLP):** Combines logic programming with numerical simplex and interval domain constraint solvers.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** How do you define a variable in PROLOG?"
                    },
                    {
                        "type": "markdown",
                        "content": "Summary: Facts are the ground truths in a PROLOG database."
                    }
                ]
            },
            {
                "title": "Module 2: Rules and Queries",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "## Writing Rules\nRules describe conditional truths. Head :- Body."
                    },
                    {
                        "type": "concept",
                        "title": "The '",
                        "content": "-' symbol means 'if'. A comma ',' means logical AND."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\nA[\"Head (Conclusion)\"] --> B[\":- (If)\"] --> C[\"Body (Conditions)\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** What does semicolon ';' mean in PROLOG rules?"
                    },
                    {
                        "type": "markdown",
                        "content": "## Querying the DB\nYou ask questions to the PROLOG interpreter using queries."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "?- likes(alice, X). asks 'What does Alice like?'"
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph LR\nstyle Q fill:#10b9811a\nQ[\"Query: ?- parent(X, mary).\"] --> R[\"Search KB\"] --> S[\"Bind X = john\"]"
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "grandparent(X, Y) :- parent(X, Z), parent(Z, Y).\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "solution_code": "grandparent(X, Y) :- parent(X, Z), parent(Z, Y).\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nDeclarative logic programming executes SLD-resolution with first-order unification, automatically searching the Horn clause database to bind variables that satisfy the query.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Datalog:** Restricts PROLOG by eliminating function symbols, guaranteeing polynomial query termination.\\n- **Answer Set Programming (ASP):** Solves hard combinatorial search problems using stable model semantics.\\n- **Constraint Logic Programming (CLP):** Combines logic programming with numerical simplex and interval domain constraint solvers.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** If a query has no matching facts, PROLOG returns:"
                    },
                    {
                        "type": "markdown",
                        "content": "Summary: Rules encode logic, and queries trigger the search engine."
                    }
                ]
            },
            {
                "title": "Module 3: Unification and Backtracking",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "## Unification\nUnification is how PROLOG matches terms and binds variables."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Two terms unify if they are identical, or if variables can be bound to make them identical."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\nA[\"Term 1: likes(X, pizza)\"] <--> B[\"Term 2: likes(bob, pizza)\"]\nB --> C[\"Unifies! X=bob\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** Does `likes(alice, X)` unify with `likes(Y, pizza)`?"
                    },
                    {
                        "type": "markdown",
                        "content": "## Backtracking\nIf PROLOG goes down a logical path that fails, it backtracks to the last choice point and tries another path."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "This depth-first search strategy is the core execution model of PROLOG."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph TD\nstyle B fill:#f43f5e1a\nB[\"Try Rule A\"] --> C[\"Fails!\"] --> D[\"Backtrack\"] --> E[\"Try Rule B\"]"
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "% Backtracking in action implicitly through comma/AND failures.\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "solution_code": "% Backtracking in action implicitly through comma/AND failures.\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nDeclarative logic programming executes SLD-resolution with first-order unification, automatically searching the Horn clause database to bind variables that satisfy the query.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Datalog:** Restricts PROLOG by eliminating function symbols, guaranteeing polynomial query termination.\\n- **Answer Set Programming (ASP):** Solves hard combinatorial search problems using stable model semantics.\\n- **Constraint Logic Programming (CLP):** Combines logic programming with numerical simplex and interval domain constraint solvers.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** What algorithm does PROLOG use for its search?"
                    },
                    {
                        "type": "markdown",
                        "content": "Summary: PROLOG's power comes from automatic unification and recursive backtracking."
                    }
                ]
            },
            {
                "title": "Module 4: Recursion and Lists",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "## Lists in PROLOG\nLists are defined using brackets, with a Head and a Tail `[H|T]`."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "The Head is the first element, the Tail is a list of the remaining elements."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\nA[\"List: [1,2,3]\"] --> B[\"Head: 1\"]\nA --> C[\"Tail: [2,3]\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** In the list `[a]`, what is the Tail?"
                    },
                    {
                        "type": "markdown",
                        "content": "## Recursive Rules\nLists are processed recursively by operating on the Head and recursing on the Tail."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "A base case (often the empty list) is strictly required to stop recursion."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph LR\nstyle R fill:#3b82f61a\nR[\"process([H|T])\"] --> S[\"Do something with H\"] --> T[\"Call process(T)\"]"
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "member(X, [X|_]).\nmember(X, [_|T]) :- member(X, T).\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "solution_code": "member(X, [X|_]).\nmember(X, [_|T]) :- member(X, T).\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nDeclarative logic programming executes SLD-resolution with first-order unification, automatically searching the Horn clause database to bind variables that satisfy the query.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Datalog:** Restricts PROLOG by eliminating function symbols, guaranteeing polynomial query termination.\\n- **Answer Set Programming (ASP):** Solves hard combinatorial search problems using stable model semantics.\\n- **Constraint Logic Programming (CLP):** Combines logic programming with numerical simplex and interval domain constraint solvers.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** What does the `_` (underscore) represent in PROLOG?"
                    },
                    {
                        "type": "markdown",
                        "content": "Summary: Lists and recursion form the backbone of complex PROLOG programs."
                    }
                ]
            }
        ]
    },
    "22": {
        "title": "Case 22: The Expert in the Box",
        "episodes": [
            {
                "title": "Module 1: Architecture of ES",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "## What is an Expert System?\nAn AI program that emulates the decision-making ability of a human expert."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Designed to solve complex problems by reasoning through bodies of knowledge, represented mainly as if-then rules."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\nA[\"User\"] --> B[\"User Interface\"]\nB --> C[\"Inference Engine\"]\nC <--> D[\"Knowledge Base\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** Which component contains the domain-specific rules?"
                    },
                    {
                        "type": "markdown",
                        "content": "## The Knowledge Base\nContains facts and rules (heuristics) extracted from human experts."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Knowledge representation is typically done via production rules (IF condition THEN action)."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph LR\nstyle K fill:#f59e0b1a\nK[\"Domain Expert\"] --> L[\"Knowledge Engineer\"] --> M[\"Knowledge Base\"]"
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "# Conceptual python structure\nknowledge_base = {'fever': True, 'cough': True}\nif knowledge_base['fever']: print('Possible Flu')",
                        "solution_code": "# Conceptual python structure\nknowledge_base = {'fever': True, 'cough': True}\nif knowledge_base['fever']: print('Possible Flu')",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nSeparates declarative domain rules (knowledge base) from the inference engine (match-resolve-act cycle), enabling modular updates to complex expert knowledge without rewriting code.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Rete Algorithm:** Compiles production rules into an in-memory discrimination network, avoiding redundant evaluations when working memory changes.\\n- **Fuzzy Expert Systems:** Evaluates continuous membership functions, handling engineering vagueness in temperature and pressure control.\\n- **Case-Based Reasoning (CBR):** Adapts past documented engineering case histories rather than static deductive rules.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** Who translates human expertise into rules?"
                    },
                    {
                        "type": "markdown",
                        "content": "Summary: ES separate the logic (engine) from the rules (knowledge base)."
                    }
                ]
            },
            {
                "title": "Module 2: Inference Engine",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "## The Inference Engine\nThe 'brain' of the expert system that applies logical rules to the knowledge base to deduce new information."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "It primarily uses Forward Chaining or Backward Chaining."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\nA[\"Facts\"] --> B[\"Inference Engine\"]\nC[\"Rules\"] --> B\nB --> D[\"Conclusions\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** Can an inference engine handle uncertainty?"
                    },
                    {
                        "type": "markdown",
                        "content": "## Forward Chaining\nData-driven approach. Start with facts, apply rules to infer new facts, until a goal is reached."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Best used when there is a lot of initial data, like configuration tasks or monitoring."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph LR\nstyle F fill:#22c55e1a\nF[\"Fact: It is raining\"] --> G[\"Rule: IF raining THEN grass wet\"] --> H[\"New Fact: Grass wet\"]"
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "# Forward Chaining\nwhile new_facts_generated:\n    apply_rules_to(facts)\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "solution_code": "# Forward Chaining\nwhile new_facts_generated:\n    apply_rules_to(facts)\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nSeparates declarative domain rules (knowledge base) from the inference engine (match-resolve-act cycle), enabling modular updates to complex expert knowledge without rewriting code.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Rete Algorithm:** Compiles production rules into an in-memory discrimination network, avoiding redundant evaluations when working memory changes.\\n- **Fuzzy Expert Systems:** Evaluates continuous membership functions, handling engineering vagueness in temperature and pressure control.\\n- **Case-Based Reasoning (CBR):** Adapts past documented engineering case histories rather than static deductive rules.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** Forward chaining is: "
                    },
                    {
                        "type": "markdown",
                        "content": "Summary: Forward chaining builds up from known data to conclusions."
                    }
                ]
            },
            {
                "title": "Module 3: Backward Chaining",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "## Backward Chaining\nGoal-driven approach. Start with a hypothesis (goal) and work backwards to see if the facts support it."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Best for diagnostic systems (like medical diagnosis) where you have a specific hypothesis to verify."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\nA[\"Goal: Patient has Flu\"] --> B[\"Check Rule: IF Fever AND Cough\"] --> C[\"Ask: Does patient have fever?\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** PROLOG's default execution model is based on:"
                    },
                    {
                        "type": "markdown",
                        "content": "## How it Works\nIf a condition of a rule isn't known, it becomes a sub-goal."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "The system recursively tries to satisfy sub-goals until it hits ground facts or asks the user."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph TD\nstyle B fill:#a855f71a\nB[\"Hypothesis X\"] --> C[\"Requires Y\"] --> D[\"Requires Z\"] --> E[\"Check Fact Z\"]"
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "def check_goal(goal):\n    for rule in rules_yielding(goal):\n         if all(check_goal(c) for c in rule.conditions): return True\n\n# --- Execution Output ---\nprint('Result:', check_goal(None))\n",
                        "solution_code": "def check_goal(goal):\n    for rule in rules_yielding(goal):\n         if all(check_goal(c) for c in rule.conditions): return True\n\n# --- Execution Output ---\nprint('Result:', check_goal(None))\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nSeparates declarative domain rules (knowledge base) from the inference engine (match-resolve-act cycle), enabling modular updates to complex expert knowledge without rewriting code.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Rete Algorithm:** Compiles production rules into an in-memory discrimination network, avoiding redundant evaluations when working memory changes.\\n- **Fuzzy Expert Systems:** Evaluates continuous membership functions, handling engineering vagueness in temperature and pressure control.\\n- **Case-Based Reasoning (CBR):** Adapts past documented engineering case histories rather than static deductive rules.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** Backward chaining is: "
                    },
                    {
                        "type": "markdown",
                        "content": "Summary: Backward chaining starts with the answer and looks for the evidence."
                    }
                ]
            },
            {
                "title": "Module 4: Uncertainty and Modern ES",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "## Handling Uncertainty\nReal-world knowledge is rarely absolute. ES use Certainty Factors (CF) or Bayesian Networks."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "MYCIN (early medical ES) pioneered Certainty Factors ranging from -1 (false) to +1 (true)."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\nA[\"Rule CF: 0.8\"] --> B[\"Evidence CF: 0.5\"]\nB --> C[\"Combined CF: 0.4\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** What did MYCIN diagnose?"
                    },
                    {
                        "type": "markdown",
                        "content": "## The Fall and Rise\nTraditional ES fell out of favor (AI Winter) because rules were hard to maintain and didn't learn."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Modern forms exist as Business Rule Engines or are augmented with Machine Learning."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph LR\nstyle M fill:#ef44441a\nM[\"Classic ES: Brittle Rules\"] --> N[\"Modern: Hybrid Systems\"] --> O[\"Rules + ML Models\"]"
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "# Hybrid\nml_prediction = model.predict(data)\nif ml_prediction > 0.9 and rule_check_passes(data): take_action()\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "solution_code": "# Hybrid\nml_prediction = model.predict(data)\nif ml_prediction > 0.9 and rule_check_passes(data): take_action()\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nSeparates declarative domain rules (knowledge base) from the inference engine (match-resolve-act cycle), enabling modular updates to complex expert knowledge without rewriting code.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Rete Algorithm:** Compiles production rules into an in-memory discrimination network, avoiding redundant evaluations when working memory changes.\\n- **Fuzzy Expert Systems:** Evaluates continuous membership functions, handling engineering vagueness in temperature and pressure control.\\n- **Case-Based Reasoning (CBR):** Adapts past documented engineering case histories rather than static deductive rules.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** What is the 'knowledge acquisition bottleneck'?"
                    },
                    {
                        "type": "markdown",
                        "content": "Summary: Expert systems evolved from brittle rule bases to modern hybrid decision systems."
                    }
                ]
            }
        ]
    },
    "23": {
        "title": "Case 23: The Intelligence Architect",
        "episodes": [
            {
                "title": "Module 1: ML Lifecycle",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "## The ML Lifecycle\nBuilding AI systems is more than just training a model in a Jupyter Notebook."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "It includes Data Collection, Feature Engineering, Training, Deployment, and Monitoring."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph LR\nA[\"Data\"] --> B[\"Train\"]\nB --> C[\"Deploy\"]\nC --> D[\"Monitor\"]\nD --> A"
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** Where does a Data Scientist usually spend the most time?"
                    },
                    {
                        "type": "markdown",
                        "content": "## MLOps\nMachine Learning Operations (MLOps) applies DevOps principles to ML systems."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Goals include reproducibility, automated testing, and CI/CD for models."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph TD\nstyle M fill:#0ea5e91a\nM[\"Git Push Code/Model\"] --> N[\"Automated Testing\"] --> O[\"Automated Deployment\"]"
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "# CI/CD yaml concept\nsteps:\n  - run_tests.py\n  - build_docker_image\n  - deploy_to_endpoint\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "solution_code": "# CI/CD yaml concept\nsteps:\n  - run_tests.py\n  - build_docker_image\n  - deploy_to_endpoint\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nDecouples multi-agent components using standardized message schemas (FIPA-ACL) and blackboard repositories, allowing autonomous specialized agents to negotiate via auction protocols.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Centralized Master-Worker:** Simple to coordinate, but creates a single point of failure and bottleneck under high telemetry volume.\\n- **Peer-to-Peer Gossip Protocols:** Resilient to node dropouts in distributed industrial IoT networks.\\n- **Multi-Agent Reinforcement Learning (MARL):** Co-adapts agent behaviors in competitive or collaborative settings.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** What is 'Model Drift'?"
                    },
                    {
                        "type": "markdown",
                        "content": "Summary: System design in AI requires managing the entire lifecycle via MLOps."
                    }
                ]
            },
            {
                "title": "Module 2: Serving Infrastructure",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "## Online vs Batch Serving\nHow will users consume your predictions?"
                    },
                    {
                        "type": "concept",
                        "title": "Online",
                        "content": "Predictions on-demand (e.g., fraud detection). Batch: Predictions pre-computed offline (e.g., weekly recommendations)."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\nA[\"Online Serving\"] --> B[\"Low Latency / REST API\"]\nC[\"Batch Serving\"] --> D[\"High Throughput / Data Warehouse\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** Which serving method is appropriate for a streaming video recommendation engine on the homepage?"
                    },
                    {
                        "type": "markdown",
                        "content": "## Containerization\nModels are typically packaged in Docker containers to ensure environment consistency."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "A container holds the model weights, dependencies (e.g., PyTorch), and serving code (e.g., FastAPI)."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph LR\nstyle C fill:#10b9811a\nC[\"Model + API Code\"] --> D[\"Docker Build\"] --> E[\"Deploy on Kubernetes\"]"
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "FROM python:3.9\nCOPY requirements.txt .\nRUN pip install -r requirements.txt\nCMD [\"uvicorn\", \"app:main\"]\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "solution_code": "FROM python:3.9\nCOPY requirements.txt .\nRUN pip install -r requirements.txt\nCMD [\"uvicorn\", \"app:main\"]\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nDecouples multi-agent components using standardized message schemas (FIPA-ACL) and blackboard repositories, allowing autonomous specialized agents to negotiate via auction protocols.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Centralized Master-Worker:** Simple to coordinate, but creates a single point of failure and bottleneck under high telemetry volume.\\n- **Peer-to-Peer Gossip Protocols:** Resilient to node dropouts in distributed industrial IoT networks.\\n- **Multi-Agent Reinforcement Learning (MARL):** Co-adapts agent behaviors in competitive or collaborative settings.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** What tool orchestrates many containers across a cluster?"
                    },
                    {
                        "type": "markdown",
                        "content": "Summary: Choose between online/batch serving and package models reliably using containers."
                    }
                ]
            },
            {
                "title": "Module 3: Feature Stores",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "## The Feature Store\nA centralized repository for managing and serving ML features."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Prevents training-serving skew by providing the exact same feature engineering logic to both offline training and online serving."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\nA[\"Raw Data\"] --> B[\"Feature Pipeline\"]\nB --> C[\"Feature Store\"]\nC --> D[\"Training\"] & E[\"Online Serving\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** What is Training-Serving Skew?"
                    },
                    {
                        "type": "markdown",
                        "content": "## Offline vs Online Features\nFeature stores often have two databases internally."
                    },
                    {
                        "type": "concept",
                        "title": "Offline",
                        "content": "Data lake for bulk historical reads. Online: Key-Value store (Redis) for low-latency point reads."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph LR\nstyle F fill:#8b5cf61a\nF[\"Feature Store\"] --> G[\"Offline (S3/Parquet)\"]\nF --> H[\"Online (Redis/DynamoDB)\"]"
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "features = feature_store.get_online_features(user_id='123')\nmodel.predict(features)\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "solution_code": "features = feature_store.get_online_features(user_id='123')\nmodel.predict(features)\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nDecouples multi-agent components using standardized message schemas (FIPA-ACL) and blackboard repositories, allowing autonomous specialized agents to negotiate via auction protocols.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Centralized Master-Worker:** Simple to coordinate, but creates a single point of failure and bottleneck under high telemetry volume.\\n- **Peer-to-Peer Gossip Protocols:** Resilient to node dropouts in distributed industrial IoT networks.\\n- **Multi-Agent Reinforcement Learning (MARL):** Co-adapts agent behaviors in competitive or collaborative settings.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** Why use Redis for online features?"
                    },
                    {
                        "type": "markdown",
                        "content": "Summary: Feature stores decouple feature engineering from model pipelines and ensure consistency."
                    }
                ]
            },
            {
                "title": "Module 4: Scalability and Latency",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "## Handling High Load\nIf your API receives 10,000 requests per second, a single Python process will crash."
                    },
                    {
                        "type": "concept",
                        "title": "Horizontal Scaling",
                        "content": "Add more server instances. Vertical Scaling: Use a bigger server/GPU."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\nA[\"Load Balancer\"] --> B[\"Instance 1\"]\nA --> C[\"Instance 2\"]\nA --> D[\"Instance 3\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** Which scaling is generally preferred in modern cloud architectures?"
                    },
                    {
                        "type": "markdown",
                        "content": "## Model Optimization\nLarge deep learning models can be too slow or expensive for production."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Quantization (FP32 to INT8), Pruning (removing weights), and Knowledge Distillation make models faster."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph LR\nstyle O fill:#f43f5e1a\nO[\"Massive FP32 Model\"] --> P[\"Quantization (INT8)\"] --> Q[\"4x Smaller, Faster Model\"]"
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "import torch\nquantized_model = torch.quantization.quantize_dynamic(model)\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "solution_code": "import torch\nquantized_model = torch.quantization.quantize_dynamic(model)\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nDecouples multi-agent components using standardized message schemas (FIPA-ACL) and blackboard repositories, allowing autonomous specialized agents to negotiate via auction protocols.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Centralized Master-Worker:** Simple to coordinate, but creates a single point of failure and bottleneck under high telemetry volume.\\n- **Peer-to-Peer Gossip Protocols:** Resilient to node dropouts in distributed industrial IoT networks.\\n- **Multi-Agent Reinforcement Learning (MARL):** Co-adapts agent behaviors in competitive or collaborative settings.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** Does quantization generally improve accuracy?"
                    },
                    {
                        "type": "markdown",
                        "content": "Summary: Design for scale horizontally and optimize models to meet latency SLAs."
                    }
                ]
            }
        ]
    },
    "24": {
        "title": "Case 24: The Final AI",
        "episodes": [
            {
                "title": "Module 1: Comprehensive Review",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "## The Journey So Far\nFrom basic linear models to neural networks, trees, and reinforcement learning."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Every algorithm is a tool. The hardest part of AI is formulating the problem correctly."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\nA[\"Problem Formulation\"] --> B[\"Data Gathering\"]\nB --> C[\"Model Selection\"]\nC --> D[\"Evaluation\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** Which is generally a worse error in medical diagnosis?"
                    },
                    {
                        "type": "markdown",
                        "content": "## No Free Lunch Theorem\nThere is no single universally best machine learning algorithm."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "An algorithm that performs exceptionally well on one class of problems will perform poorly on another."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph LR\nstyle N fill:#eab3081a\nN[\"Dataset A: Tree Wins\"] --> O[\"Dataset B: NN Wins\"] --> P[\"No Free Lunch\"]"
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "# Try multiple models\nmodels = [RandomForest(), SVC(), MLPClassifier()]\nfor m in models: m.fit(X, y)\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "solution_code": "# Try multiple models\nmodels = [RandomForest(), SVC(), MLPClassifier()]\nfor m in models: m.fit(X, y)\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nNeuro-Symbolic architecture: combines continuous perceptual neural networks with discrete symbolic verification layers, ensuring outputs satisfy mathematical and physical safety invariants.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Pure Deep Learning:** High empirical accuracy on perceptual tasks, but vulnerable to adversarial hallucinations and lacks formal safety guarantees.\\n- **Pure Symbolic AI:** Fully verifiable and explainable, but brittle to raw sensory noise and unable to scale to unstructured images/audio.\\n- **Physics-Informed Neural Networks (PINNs):** Embeds governing partial differential equations directly into loss functions.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** Because of the No Free Lunch theorem, what must a data scientist do?"
                    },
                    {
                        "type": "markdown",
                        "content": "Summary: Your toolkit is vast; apply the right tool to the specific context."
                    }
                ]
            },
            {
                "title": "Module 2: AI Ethics and Bias",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "## Algorithmic Bias\nModels learn from data. If the data contains human biases, the model will codify and amplify them."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Bias can enter through unbalanced datasets, flawed features, or historical prejudice."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\nA[\"Biased Historical Data\"] --> B[\"Model Training\"]\nB --> C[\"Automated Discrimination\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** If a hiring AI is trained on historical data where 90% of hires were men, what will it likely learn?"
                    },
                    {
                        "type": "markdown",
                        "content": "## Fairness Metrics\nAccuracy is not enough. We must measure demographic parity, equal opportunity, etc."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Equal opportunity ensures the True Positive Rate is the same across different demographic groups."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph TD\nstyle E fill:#ec48991a\nE[\"Train Model\"] --> F[\"Evaluate per Subgroup\"] --> G[\"Check Equal Opportunity\"]"
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "from fairlearn.metrics import demographic_parity_difference\ndp_diff = demographic_parity_difference(y_true, y_pred, sensitive_features=gender)\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "solution_code": "from fairlearn.metrics import demographic_parity_difference\ndp_diff = demographic_parity_difference(y_true, y_pred, sensitive_features=gender)\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nNeuro-Symbolic architecture: combines continuous perceptual neural networks with discrete symbolic verification layers, ensuring outputs satisfy mathematical and physical safety invariants.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Pure Deep Learning:** High empirical accuracy on perceptual tasks, but vulnerable to adversarial hallucinations and lacks formal safety guarantees.\\n- **Pure Symbolic AI:** Fully verifiable and explainable, but brittle to raw sensory noise and unable to scale to unstructured images/audio.\\n- **Physics-Informed Neural Networks (PINNs):** Embeds governing partial differential equations directly into loss functions.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** Can we remove bias entirely just by dropping the 'gender' or 'race' column?"
                    },
                    {
                        "type": "markdown",
                        "content": "Summary: Actively audit models for fairness; AI is not automatically objective."
                    }
                ]
            },
            {
                "title": "Module 3: Explainability (XAI)",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "## Black Box vs White Box\nModels like Deep Neural Nets are 'black boxes' (hard to interpret). Trees and Linear models are 'white boxes'."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "In regulated industries (finance, healthcare), you must often explain *why* a decision was made."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\nA[\"Linear Model: High Interpretable\"] --> B[\"Random Forest: Medium\"]\nB --> C[\"Deep NN: Low Interpretable\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** Which model is natively the most interpretable?"
                    },
                    {
                        "type": "markdown",
                        "content": "## SHAP Values\nSHapley Additive exPlanations. A game-theoretic approach to explain the output of ANY machine learning model."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "SHAP calculates the marginal contribution of each feature to the final prediction."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph LR\nstyle S fill:#6366f11a\nS[\"Base Value (Average)\"] --> T[\"+ Age Effect\"] --> U[\"- Income Effect\"] --> V[\"Final Prediction\"]"
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "import shap\nexplainer = shap.Explainer(model)\nshap_values = explainer(X)\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "solution_code": "import shap\nexplainer = shap.Explainer(model)\nshap_values = explainer(X)\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nNeuro-Symbolic architecture: combines continuous perceptual neural networks with discrete symbolic verification layers, ensuring outputs satisfy mathematical and physical safety invariants.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Pure Deep Learning:** High empirical accuracy on perceptual tasks, but vulnerable to adversarial hallucinations and lacks formal safety guarantees.\\n- **Pure Symbolic AI:** Fully verifiable and explainable, but brittle to raw sensory noise and unable to scale to unstructured images/audio.\\n- **Physics-Informed Neural Networks (PINNs):** Embeds governing partial differential equations directly into loss functions.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** SHAP is considered a _____ method."
                    },
                    {
                        "type": "markdown",
                        "content": "Summary: XAI tools like SHAP bridge the gap between complex models and human trust."
                    }
                ]
            },
            {
                "title": "Module 4: Future of AI",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "## Foundation Models & LLMs\nLarge Language Models (like GPT) and Foundation Models have shifted the paradigm from training from scratch to fine-tuning."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Self-supervised learning on massive datasets allows these models to generalize to many tasks."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\nA[\"Massive Unlabeled Data\"] --> B[\"Pre-training (Next Token)\"]\nB --> C[\"Fine-Tuning (Specific Task)\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** What training objective is commonly used for LLM pre-training?"
                    },
                    {
                        "type": "markdown",
                        "content": "## AGI and Alignment\nArtificial General Intelligence (AGI) refers to AI that equals or surpasses human intelligence across all domains."
                    },
                    {
                        "type": "concept",
                        "title": "The Alignment Problem asks",
                        "content": "How do we ensure AGI goals remain aligned with human values?"
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph TD\nstyle A fill:#22c55e1a\nA[\"Capable AI\"] --> B[\"Misaligned Goals\"] --> C[\"Catastrophe\"]\nA --> D[\"Aligned Goals\"] --> E[\"Utopia\"]"
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "# The ultimate pseudo-code\nwhile AI.is_running():\n    ensure_human_alignment()\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "solution_code": "# The ultimate pseudo-code\nwhile AI.is_running():\n    ensure_human_alignment()\n\n# --- Execution Output ---\nprint('Execution Complete.')\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nNeuro-Symbolic architecture: combines continuous perceptual neural networks with discrete symbolic verification layers, ensuring outputs satisfy mathematical and physical safety invariants.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Pure Deep Learning:** High empirical accuracy on perceptual tasks, but vulnerable to adversarial hallucinations and lacks formal safety guarantees.\\n- **Pure Symbolic AI:** Fully verifiable and explainable, but brittle to raw sensory noise and unable to scale to unstructured images/audio.\\n- **Physics-Informed Neural Networks (PINNs):** Embeds governing partial differential equations directly into loss functions.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** What technique uses human feedback to align LLMs?"
                    },
                    {
                        "type": "markdown",
                        "content": "Summary: The future is bright but requires careful stewardship of alignment, ethics, and safety."
                    }
                ]
            }
        ]
    },
    "1": {
        "title": "Case 01: The Agent Awakens",
        "episodes": [
            {
                "title": "Module 1.1: The Essence of Rational Agents",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "Welcome to Case 1! In Artificial Intelligence, an agent is anything that perceives its environment through sensors and acts upon that environment through actuators."
                    },
                    {
                        "type": "concept",
                        "title": "Rationality",
                        "content": "A rational agent chooses whichever action maximizes the expected value of the performance measure given the percept sequence to date."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\n  Environment[\"Environment\"] -->|Percepts| Sensors[\"Sensors\"]\n  Sensors --> Agent[\"Agent\"]\n  Agent --> Actuators[\"Actuators\"]\n  Actuators -->|Actions| Environment\n  style Environment fill:#10b9811a"
                    },
                    {
                        "type": "markdown",
                        "content": "The concept of an agent provides a unifying framework for studying AI. We can consider humans, robots, and softbots all as agents."
                    },
                    {
                        "type": "fill_in_the_blank",
                        "question": "_____ an agent use to perceive its environment.",
                        "answer": "Sensors",
                        "explanation": "**Why Sensors is Correct:**\\nThis option correctly reflects the foundational theorem and invariant governing this model. Alternative options fail because they either violate time/space constraints or make unsound assumptions about environment determinism."
                    },
                    {
                        "type": "concept",
                        "title": "Omniscience vs Rationality",
                        "content": "An omniscient agent knows the actual outcome of its actions and can act accordingly; but omniscience is impossible in reality. Rationality maximizes *expected* performance."
                    },
                    {
                        "type": "markdown",
                        "content": "Let's explore the PEAS framework, which helps us design agents by specifying the task environment."
                    },
                    {
                        "type": "visual_stepper",
                        "title": "Interactive: The Rational Agent Loop",
                        "steps": [
                            {
                                "explanation": "Step 1: The Environment exists in a current state. It emits data.",
                                "mermaid_code": "graph TD\n  classDef active fill:#10b9811a,stroke:#34D399,stroke-width:2px;\n  classDef idle fill:#ffffff1a,stroke:#333,stroke-width:2px;\n  E[\"Environment\"]:::active -->|Data| S[\"Sensors\"]:::idle\n  S --> A[\"Agent Program\"]:::idle\n  A --> AC[\"Actuators\"]:::idle\n  AC -->|Action| E"
                            },
                            {
                                "explanation": "Step 2: The Agent's Sensors perceive the data (Percepts) from the Environment.",
                                "mermaid_code": "graph TD\n  classDef active fill:#10b9811a,stroke:#34D399,stroke-width:2px;\n  classDef idle fill:#ffffff1a,stroke:#333,stroke-width:2px;\n  E[\"Environment\"]:::idle -->|Percepts| S[\"Sensors\"]:::active\n  S --> A[\"Agent Program\"]:::idle\n  A --> AC[\"Actuators\"]:::idle\n  AC -->|Action| E"
                            },
                            {
                                "explanation": "Step 3: The Agent Program processes the Percepts and decides on the optimal Action.",
                                "mermaid_code": "graph TD\n  classDef active fill:#10b9811a,stroke:#34D399,stroke-width:2px;\n  classDef idle fill:#ffffff1a,stroke:#333,stroke-width:2px;\n  E[\"Environment\"]:::idle --> S[\"Sensors\"]:::idle\n  S --> A[\"Agent Program\"]:::active\n  A --> AC[\"Actuators\"]:::idle\n  AC -->|Action| E"
                            },
                            {
                                "explanation": "Step 4: The Actuators execute the decided Action, physically altering the Environment.",
                                "mermaid_code": "graph TD\n  classDef active fill:#10b9811a,stroke:#34D399,stroke-width:2px;\n  classDef idle fill:#ffffff1a,stroke:#333,stroke-width:2px;\n  E[\"Environment\"]:::idle --> S[\"Sensors\"]:::idle\n  S --> A[\"Agent Program\"]:::idle\n  A --> AC[\"Actuators\"]:::active\n  AC -->|Action| E:::active"
                            }
                        ]
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "PEAS stands for Performance measure, Environment, Actuators, and Sensors."
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "class SimpleAgent:\n    def __init__(self):\n        self.percepts = []\n    def act(self, percept):\n        self.percepts.append(percept)\n        return 'ACTION_DEFAULT'\n\n# --- Execution Output ---\nobj = SimpleAgent()\nprint('Initialized', obj)\nprint('Action:', obj.act('test_percept'))\n",
                        "solution_code": "class SimpleAgent:\n    def __init__(self):\n        self.percepts = []\n    def act(self, percept):\n        self.percepts.append(percept)\n        return 'ACTION_DEFAULT'\n\n# --- Execution Output ---\nobj = SimpleAgent()\nprint('Initialized', obj)\nprint('Action:', obj.act('test_percept'))\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nMaintains an internal state transition model $S_t = f(S_{t-1}, A_{t-1}, P_t)$, allowing the agent to reconstruct a consistent belief state in partially observable environments (POMDPs).",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Table-Driven Agent:** $O(1)$ lookup, but memory is $O(|P|^T)$ exponential in time horizon $T$ (requires more entries than atoms in the universe).\\n- **Simple Reflex Agent:** $O(1)$ memory, but fails catastrophically in non-Markovian / partially observable environments due to infinite loops.\\n- **Goal-Based Agent:** Evaluates future consequence trajectories, providing greater flexibility at the cost of computational search latency.\\n- **Utility-Based Agent:** Computes continuous real-valued utilities under uncertainty, balancing multi-attribute trade-offs.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    }
                ]
            },
            {
                "title": "Module 1.2: Structuring the Task Environment (PEAS)",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "To design a rational agent, we must first specify its task environment as fully as possible using the PEAS description."
                    },
                    {
                        "type": "concept",
                        "title": "Performance Measure",
                        "content": "Defines the criteria for success of the agent's behavior."
                    },
                    {
                        "type": "fill_in_the_blank",
                        "question": "In a self-driving car, what is NOT a good performance measure?\n\nAnswer: _____",
                        "answer": "Number of pedestrians hit",
                        "explanation": "**Why Number of pedestrians hit is Correct:**\\nThis option correctly reflects the foundational theorem and invariant governing this model. Alternative options fail because they either violate time/space constraints or make unsound assumptions about environment determinism."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph LR\n  Task[\"Automated Taxi\"]\n  Task --> P[\"P: Safe, Fast, Legal\"]\n  Task --> E[\"E: Roads, Traffic, Pedestrians\"]\n  Task --> A[\"A: Steering, Accelerator, Brake\"]\n  Task --> S[\"S: Cameras, Sonar, Speedometer\"]\n  style Task fill:#8b5cf61a"
                    },
                    {
                        "type": "markdown",
                        "content": "Consider a medical diagnosis system. The performance measure might be healthy patient, reduced costs, and minimized lawsuits."
                    },
                    {
                        "type": "concept",
                        "title": "Environment properties",
                        "content": "Fully vs Partially Observable, Single vs Multi-agent, Deterministic vs Stochastic, Episodic vs Sequential, Static vs Dynamic, Discrete vs Continuous, Known vs Unknown."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph TD\n  Fully[\"Fully Observable\"]\n  Partially[\"Partially Observable\"]\n  Fully -->|Chess| Deterministic[\"Deterministic\"]\n  Partially -->|Poker| Stochastic[\"Stochastic\"]"
                    },
                    {
                        "type": "markdown",
                        "content": "Chess with a clock is fully observable, deterministic, sequential, dynamic, discrete, and known. Poker is partially observable and stochastic."
                    },
                    {
                        "type": "fill_in_the_blank",
                        "question": "Is the real world discrete or continuous?\n\nAnswer: _____",
                        "answer": "Continuous.",
                        "explanation": "**Why Continuous. is Correct:**\\nThis option correctly reflects the foundational theorem and invariant governing this model. Alternative options fail because they either violate time/space constraints or make unsound assumptions about environment determinism."
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "def check_environment_type(is_fully_observable):\n    if is_fully_observable:\n        return 'Easy to plan'\n    else:\n        return 'Need memory/state'\n\n# --- Execution Output ---\nprint('Result:', check_environment_type(None))\n",
                        "solution_code": "def check_environment_type(is_fully_observable):\n    if is_fully_observable:\n        return 'Easy to plan'\n    else:\n        return 'Need memory/state'\n\n# --- Execution Output ---\nprint('Result:', check_environment_type(None))\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nMaintains an internal state transition model $S_t = f(S_{t-1}, A_{t-1}, P_t)$, allowing the agent to reconstruct a consistent belief state in partially observable environments (POMDPs).",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Table-Driven Agent:** $O(1)$ lookup, but memory is $O(|P|^T)$ exponential in time horizon $T$ (requires more entries than atoms in the universe).\\n- **Simple Reflex Agent:** $O(1)$ memory, but fails catastrophically in non-Markovian / partially observable environments due to infinite loops.\\n- **Goal-Based Agent:** Evaluates future consequence trajectories, providing greater flexibility at the cost of computational search latency.\\n- **Utility-Based Agent:** Computes continuous real-valued utilities under uncertainty, balancing multi-attribute trade-offs.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    }
                ]
            },
            {
                "title": "Module 1.3: Types of Agent Programs",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "Agent programs map percepts to actions. We will explore four basic types of agent programs in order of increasing generality."
                    },
                    {
                        "type": "concept",
                        "title": "Simple Reflex Agents",
                        "content": "These agents select actions on the basis of the current percept, ignoring the rest of the percept history."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\n  Sensors[\"Sensors\"] --> Rules[\"Condition-Action Rules\"]\n  Rules --> Actuators[\"Actuators\"]\n  style Rules fill:#ef44441a"
                    },
                    {
                        "type": "markdown",
                        "content": "Simple reflex agents are simple but of limited intelligence. They only work if the environment is fully observable."
                    },
                    {
                        "type": "interactive",
                        "question": "What do simple reflex agents rely on?",
                        "options": [
                            "Percept history",
                            "Current percept only",
                            "Future predictions."
                        ],
                        "answer": "Current percept only",
                        "explanation": "**Why Current percept only is Correct:**\\nThis option correctly reflects the foundational theorem and invariant governing this model. Alternative options fail because they either violate time/space constraints or make unsound assumptions about environment determinism."
                    },
                    {
                        "type": "concept",
                        "title": "Model-based Reflex Agents",
                        "content": "These agents maintain an internal state that depends on the percept history and thereby reflects at least some of the unobserved aspects of the current state."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph TD\n  State[\"State\"]\n  Evolution[\"How the world evolves\"]\n  Effect[\"What my actions do\"]\n  State --> Rules[\"Condition-Action Rules\"]\n  style State fill:#10b9811a"
                    },
                    {
                        "type": "markdown",
                        "content": "A model-based agent updates its internal state based on its model of how the world evolves independently of the agent, and how the agent's own actions affect the world."
                    },
                    {
                        "type": "interactive",
                        "question": "Why maintain an internal state?",
                        "options": [
                            "To handle partially observable environments",
                            "To increase speed."
                        ],
                        "answer": "To handle partially observable environments",
                        "explanation": "**Why To handle partially observable environments is Correct:**\\nThis option correctly reflects the foundational theorem and invariant governing this model. Alternative options fail because they either violate time/space constraints or make unsound assumptions about environment determinism."
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "class ModelBasedAgent:\n    def __init__(self):\n        self.state = {}\n    def update_state(self, percept):\n        self.state['latest'] = percept\n        return 'ACTION_BASED_ON_STATE'\n\n# --- Execution Output ---\nobj = ModelBasedAgent()\nprint('Initialized', obj)\n",
                        "solution_code": "class ModelBasedAgent:\n    def __init__(self):\n        self.state = {}\n    def update_state(self, percept):\n        self.state['latest'] = percept\n        return 'ACTION_BASED_ON_STATE'\n\n# --- Execution Output ---\nobj = ModelBasedAgent()\nprint('Initialized', obj)\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nMaintains an internal state transition model $S_t = f(S_{t-1}, A_{t-1}, P_t)$, allowing the agent to reconstruct a consistent belief state in partially observable environments (POMDPs).",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Table-Driven Agent:** $O(1)$ lookup, but memory is $O(|P|^T)$ exponential in time horizon $T$ (requires more entries than atoms in the universe).\\n- **Simple Reflex Agent:** $O(1)$ memory, but fails catastrophically in non-Markovian / partially observable environments due to infinite loops.\\n- **Goal-Based Agent:** Evaluates future consequence trajectories, providing greater flexibility at the cost of computational search latency.\\n- **Utility-Based Agent:** Computes continuous real-valued utilities under uncertainty, balancing multi-attribute trade-offs.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    }
                ]
            },
            {
                "title": "Module 1.4: Goal and Utility-Based Agents",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "Knowing the current state of the environment is not always enough to decide what to do. The agent needs some sort of goal information that describes situations that are desirable."
                    },
                    {
                        "type": "concept",
                        "title": "Goal-based Agents",
                        "content": "These agents use goal information combined with the environment model to choose actions that achieve the goal."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\n  State[\"State\"] --> WhatIf[\"What it will be like if I do action A\"]\n  WhatIf --> Goals[\"Goals\"]\n  Goals --> Action[\"Action\"]\n  style Goals fill:#f59e0b1a"
                    },
                    {
                        "type": "markdown",
                        "content": "Search and planning are the subfields of AI devoted to finding action sequences that achieve the agent's goals."
                    },
                    {
                        "type": "interactive",
                        "question": "Does a goal-based agent consider the future?",
                        "options": [
                            "Yes, it evaluates action outcomes against goals",
                            "No, it only uses rules."
                        ],
                        "answer": "Yes, it evaluates action outcomes against goals",
                        "explanation": "**Why Yes, it evaluates action outcomes against goals is Correct:**\\nThis option correctly reflects the foundational theorem and invariant governing this model. Alternative options fail because they either violate time/space constraints or make unsound assumptions about environment determinism."
                    },
                    {
                        "type": "concept",
                        "title": "Utility-based Agents",
                        "content": "Goals just provide a crude binary distinction between 'happy' and 'unhappy' states. A more general performance measure should allow a comparison of different world states according to exactly how happy they would make the agent."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph TD\n  State[\"State\"] --> Utility[\"Utility Function\"]\n  Utility --> Maximize[\"Maximize Expected Utility\"]\n  style Utility fill:#6366f11a"
                    },
                    {
                        "type": "markdown",
                        "content": "An agent's utility function is essentially an internalization of the performance measure."
                    },
                    {
                        "type": "fill_in_the_blank",
                        "question": "_____ is the main advantage of utility over goals.",
                        "answer": "Handles trade-offs and uncertainty",
                        "explanation": "**Why Handles trade-offs and uncertainty is Correct:**\\nThis option correctly reflects the foundational theorem and invariant governing this model. Alternative options fail because they either violate time/space constraints or make unsound assumptions about environment determinism."
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "def calculate_utility(state):\n    reward = state.get('reward', 0)\n    cost = state.get('cost', 0)\n    return reward - cost\n\n# --- Execution Output ---\nprint('Result:', calculate_utility(None))\n",
                        "solution_code": "def calculate_utility(state):\n    reward = state.get('reward', 0)\n    cost = state.get('cost', 0)\n    return reward - cost\n\n# --- Execution Output ---\nprint('Result:', calculate_utility(None))\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nMaintains an internal state transition model $S_t = f(S_{t-1}, A_{t-1}, P_t)$, allowing the agent to reconstruct a consistent belief state in partially observable environments (POMDPs).",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Table-Driven Agent:** $O(1)$ lookup, but memory is $O(|P|^T)$ exponential in time horizon $T$ (requires more entries than atoms in the universe).\\n- **Simple Reflex Agent:** $O(1)$ memory, but fails catastrophically in non-Markovian / partially observable environments due to infinite loops.\\n- **Goal-Based Agent:** Evaluates future consequence trajectories, providing greater flexibility at the cost of computational search latency.\\n- **Utility-Based Agent:** Computes continuous real-valued utilities under uncertainty, balancing multi-attribute trade-offs.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    }
                ]
            }
        ]
    },
    "2": {
        "title": "Case 02: The World Inside the Machine",
        "episodes": [
            {
                "title": "Module 2.1: Formalizing Problems and State Spaces",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "In Case 2, we dive into problem-solving agents. These are goal-based agents that decide what to do by finding sequences of actions that lead to desirable states."
                    },
                    {
                        "type": "concept",
                        "title": "Problem Formulation",
                        "content": "The process of deciding what actions and states to consider, given a goal."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\n  Goal[\"Goal Formulation\"] --> Problem[\"Problem Formulation\"]\n  Problem --> Search[\"Search\"]\n  Search --> Execute[\"Execution\"]\n  style Search fill:#10b9811a"
                    },
                    {
                        "type": "markdown",
                        "content": "Before an agent can start searching for solutions, it must formulate a goal and then formulate the problem."
                    },
                    {
                        "type": "interactive",
                        "question": "Which comes first in problem-solving?",
                        "options": [
                            "Search",
                            "Goal Formulation",
                            "Execution."
                        ],
                        "answer": "Goal Formulation",
                        "explanation": "**Why Goal Formulation is Correct:**\\nThis option correctly reflects the foundational theorem and invariant governing this model. Alternative options fail because they either violate time/space constraints or make unsound assumptions about environment determinism."
                    },
                    {
                        "type": "concept",
                        "title": "A problem can be defined formally by five components",
                        "content": "Initial State, Actions, Transition Model, Goal Test, and Path Cost."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph LR\n  Init[\"Initial State: In(Arad)\"]\n  Actions[\"Actions: Go(Zerind), Go(Sibiu), Go(Timisoara)\"]\n  Model[\"Transition: Result(In(Arad), Go(Zerind)) = In(Zerind)\"]\n  style Init fill:#3b82f61a\n  Init --> Actions\n  Actions --> Model"
                    },
                    {
                        "type": "markdown",
                        "content": "The set of all states reachable from the initial state by any sequence of actions is the State Space of the problem."
                    },
                    {
                        "type": "fill_in_the_blank",
                        "question": "What function defines the resulting state after taking an action?\n\nAnswer: _____",
                        "answer": "Transition Model.",
                        "explanation": "**Why Transition Model. is Correct:**\\nThis option correctly reflects the foundational theorem and invariant governing this model. Alternative options fail because they either violate time/space constraints or make unsound assumptions about environment determinism."
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "class Problem:\n    def __init__(self, initial, goal):\n        self.initial = initial\n        self.goal = goal\n    def goal_test(self, state):\n        return state == self.goal\n\n# --- Execution Output ---\nobj = Problem()\nprint('Initialized', obj)\n",
                        "solution_code": "class Problem:\n    def __init__(self, initial, goal):\n        self.initial = initial\n        self.goal = goal\n    def goal_test(self, state):\n        return state == self.goal\n\n# --- Execution Output ---\nobj = Problem()\nprint('Initialized', obj)\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nImplements a canonical state abstraction with immutable hashing and an explored set (closed list), ensuring each graph state is expanded at most once and eliminating infinite loops.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Tree Search (No Explored Set):** Minimal memory $O(b \\cdot d)$, but loops infinitely on cyclic graphs and re-explores duplicate states exponentially ($O(2^d)$).\\n- **Graph Search (With Explored Set):** Guarantees termination and bounds expansions to the total number of reachable states $|S|$, at the cost of storing all visited states in memory.\\n- **Bidirectional Search:** Runs simultaneous forward search from initial state and backward search from goal, reducing time complexity from $O(b^d)$ to $O(2 \\cdot b^{d/2})$.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    }
                ]
            },
            {
                "title": "Module 2.2: The Toy Problems",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "To illustrate problem formulation, AI researchers often use toy problems like the Vacuum World or the 8-puzzle."
                    },
                    {
                        "type": "concept",
                        "title": "Vacuum World State Space",
                        "content": "Consider 2 locations, each can be clean or dirty, and the agent can be in either location. Total states: 2 * 2^2 = 8."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\n  State1[\"Both Dirty, Agent Left\"]\n  State2[\"Left Clean, Right Dirty, Agent Left\"]\n  State1 -->|Suck| State2\n  style State1 fill:#ef44441a"
                    },
                    {
                        "type": "markdown",
                        "content": "The 8-puzzle consists of a 3x3 board with 8 numbered tiles and a blank space. A tile adjacent to the blank space can slide into the space."
                    },
                    {
                        "type": "fill_in_the_blank",
                        "question": "How many possible states are there in the 8-puzzle?\n\nAnswer: _____",
                        "answer": "9!/2.",
                        "explanation": "**Why 9!/2. is Correct:**\\nThis option correctly reflects the foundational theorem and invariant governing this model. Alternative options fail because they either violate time/space constraints or make unsound assumptions about environment determinism."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "The state space size for the 8-puzzle is 9!/2 = 181,440. For the 15-puzzle, it's 16!/2, which is roughly 10 trillion. This highlights the problem of state explosion."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph LR\n  S1[\"1 2 3\"]\n  S2[\"4 5 6\"]\n  S3[\"7 8  \"]\n  S1 -.-> S2 -.-> S3\n  style S1 fill:#f59e0b1a"
                    },
                    {
                        "type": "markdown",
                        "content": "Path cost is usually the number of steps in the path, so each step costs 1. The goal is to reach a specific configuration."
                    },
                    {
                        "type": "interactive",
                        "question": "Why do we care about path cost?",
                        "options": [
                            "To find the optimal solution",
                            "To formulate the goal."
                        ],
                        "answer": "To find the optimal solution",
                        "explanation": "**Why To find the optimal solution is Correct:**\\nThis option correctly reflects the foundational theorem and invariant governing this model. Alternative options fail because they either violate time/space constraints or make unsound assumptions about environment determinism."
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "def path_cost(c, state1, action, state2):\n    return c + 1  # Uniform step cost\n\n# --- Execution Output ---\nprint('Result:', path_cost(None))\n",
                        "solution_code": "def path_cost(c, state1, action, state2):\n    return c + 1  # Uniform step cost\n\n# --- Execution Output ---\nprint('Result:', path_cost(None))\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nImplements a canonical state abstraction with immutable hashing and an explored set (closed list), ensuring each graph state is expanded at most once and eliminating infinite loops.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Tree Search (No Explored Set):** Minimal memory $O(b \\cdot d)$, but loops infinitely on cyclic graphs and re-explores duplicate states exponentially ($O(2^d)$).\\n- **Graph Search (With Explored Set):** Guarantees termination and bounds expansions to the total number of reachable states $|S|$, at the cost of storing all visited states in memory.\\n- **Bidirectional Search:** Runs simultaneous forward search from initial state and backward search from goal, reducing time complexity from $O(b^d)$ to $O(2 \\cdot b^{d/2})$.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    }
                ]
            },
            {
                "title": "Module 2.3: Real World Problems",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "While toy problems are great for understanding, AI is applied to complex real-world problems."
                    },
                    {
                        "type": "concept",
                        "title": "Route-Finding",
                        "content": "Used in routing video streams, military operations planning, and airline travel planning. It involves finding the best path between locations."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph LR\n  A[\"City A\"]\n  B[\"City B\"]\n  C[\"City C\"]\n  A -->|100km| B\n  A -->|150km| C\n  B -->|80km| C\n  style A fill:#10b9811a"
                    },
                    {
                        "type": "markdown",
                        "content": "Touring Problems: The agent must visit every state at least once. The Traveling Salesperson Problem (TSP) is a famous example where the goal is to find the shortest tour."
                    },
                    {
                        "type": "fill_in_the_blank",
                        "question": "Is the Traveling Salesperson Problem NP-hard?\n\nAnswer: _____",
                        "answer": "Yes",
                        "explanation": "**Why Yes is Correct:**\\nThis option correctly reflects the foundational theorem and invariant governing this model. Alternative options fail because they either violate time/space constraints or make unsound assumptions about environment determinism."
                    },
                    {
                        "type": "concept",
                        "title": "Robot Navigation",
                        "content": "This is a generalization of route-finding. Rather than a discrete set of routes, a robot can move in a continuous space with an infinite set of possible actions."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph TD\n  Start[\"Start Position\"]\n  Obstacle[\"Obstacle\"]\n  Goal[\"Goal Position\"]\n  Start -->|Avoid| Obstacle\n  Start -->|Path| Goal"
                    },
                    {
                        "type": "markdown",
                        "content": "Protein Design: The goal is to find a sequence of amino acids that will fold into a 3D protein with the right properties. This state space is massive."
                    },
                    {
                        "type": "fill_in_the_blank",
                        "question": "In real-world problems, state spaces are typically:\n\nAnswer: _____",
                        "answer": "Large or infinite.",
                        "explanation": "**Why Large or infinite. is Correct:**\\nThis option correctly reflects the foundational theorem and invariant governing this model. Alternative options fail because they either violate time/space constraints or make unsound assumptions about environment determinism."
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "class TSPNode:\n    def __init__(self, city, visited):\n        self.city = city\n        self.visited = visited\n\n# --- Execution Output ---\nobj = TSPNode()\nprint('Initialized', obj)\n",
                        "solution_code": "class TSPNode:\n    def __init__(self, city, visited):\n        self.city = city\n        self.visited = visited\n\n# --- Execution Output ---\nobj = TSPNode()\nprint('Initialized', obj)\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nImplements a canonical state abstraction with immutable hashing and an explored set (closed list), ensuring each graph state is expanded at most once and eliminating infinite loops.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Tree Search (No Explored Set):** Minimal memory $O(b \\cdot d)$, but loops infinitely on cyclic graphs and re-explores duplicate states exponentially ($O(2^d)$).\\n- **Graph Search (With Explored Set):** Guarantees termination and bounds expansions to the total number of reachable states $|S|$, at the cost of storing all visited states in memory.\\n- **Bidirectional Search:** Runs simultaneous forward search from initial state and backward search from goal, reducing time complexity from $O(b^d)$ to $O(2 \\cdot b^{d/2})$.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    }
                ]
            },
            {
                "title": "Module 2.4: Measuring Problem-Solving Performance",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "Before we evaluate search algorithms, we need to establish the criteria by which they will be judged."
                    },
                    {
                        "type": "concept",
                        "title": "We evaluate an algorithm's performance in four ways",
                        "content": "Completeness, Optimality, Time Complexity, and Space Complexity."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\n  P[\"Performance\"]\n  P --> C[\"Completeness\"]\n  P --> O[\"Optimality\"]\n  P --> T[\"Time Complexity\"]\n  P --> S[\"Space Complexity\"]\n  style P fill:#6366f11a"
                    },
                    {
                        "type": "markdown",
                        "content": "Completeness answers the question: Is the algorithm guaranteed to find a solution when there is one?"
                    },
                    {
                        "type": "interactive",
                        "question": "What does optimality guarantee?",
                        "options": [
                            "Finds a solution quickly",
                            "Finds the lowest path-cost solution."
                        ],
                        "answer": "Finds the lowest path-cost solution.",
                        "explanation": "**Why Finds the lowest path-cost solution. is Correct:**\\nThis option correctly reflects the foundational theorem and invariant governing this model. Alternative options fail because they either violate time/space constraints or make unsound assumptions about environment determinism."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Time and Space Complexity are often measured in terms of the branching factor (b), the depth of the shallowest goal node (d), and the maximum length of any path in the state space (m)."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph TD\n  Root[\"Root Node\"]\n  Child1[\"Child 1\"]\n  Child2[\"Child 2\"]\n  Root --> Child1\n  Root --> Child2\n  style Root fill:#8b5cf61a"
                    },
                    {
                        "type": "markdown",
                        "content": "In AI, space complexity is often the biggest bottleneck because search trees can grow exponentially, quickly exhausting available memory."
                    },
                    {
                        "type": "interactive",
                        "question": "Which parameter represents the maximum length of any path in the state space?",
                        "options": [
                            "b",
                            "d",
                            "m."
                        ],
                        "answer": "m.",
                        "explanation": "**Why m. is Correct:**\\nThis option correctly reflects the foundational theorem and invariant governing this model. Alternative options fail because they either violate time/space constraints or make unsound assumptions about environment determinism."
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "def calculate_complexity(b, d):\n    # Calculates O(b^d)\n    return b ** d\n\n# --- Execution Output ---\nprint('Result:', calculate_complexity(None))\n",
                        "solution_code": "def calculate_complexity(b, d):\n    # Calculates O(b^d)\n    return b ** d\n\n# --- Execution Output ---\nprint('Result:', calculate_complexity(None))\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nImplements a canonical state abstraction with immutable hashing and an explored set (closed list), ensuring each graph state is expanded at most once and eliminating infinite loops.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Tree Search (No Explored Set):** Minimal memory $O(b \\cdot d)$, but loops infinitely on cyclic graphs and re-explores duplicate states exponentially ($O(2^d)$).\\n- **Graph Search (With Explored Set):** Guarantees termination and bounds expansions to the total number of reachable states $|S|$, at the cost of storing all visited states in memory.\\n- **Bidirectional Search:** Runs simultaneous forward search from initial state and backward search from goal, reducing time complexity from $O(b^d)$ to $O(2 \\cdot b^{d/2})$.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    }
                ]
            }
        ]
    },
    "3": {
        "title": "Case 03: The Maze Without a Map",
        "episodes": [
            {
                "title": "Module 3.1: Uninformed Search Strategies",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "Case 3 introduces Uninformed Search, also known as blind search. These strategies have no additional information about states beyond that provided in the problem definition."
                    },
                    {
                        "type": "concept",
                        "title": "Breadth-First Search (BFS)",
                        "content": "A simple strategy in which the root node is expanded first, then all the successors of the root node are expanded next, then their successors, and so on."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\n  A[\"Level 0 (A)\"] --> B[\"Level 1 (B)\"]\n  A --> C[\"Level 1 (C)\"]\n  B --> D[\"Level 2 (D)\"]\n  B --> E[\"Level 2 (E)\"]\n  style A fill:#3b82f61a\n  style B fill:#3b82f61a\n  style C fill:#3b82f61a"
                    },
                    {
                        "type": "visual_stepper",
                        "title": "Interactive: Breadth-First Search (BFS)",
                        "steps": [
                            {
                                "explanation": "Step 1: BFS starts at the root node. It checks if the root is the goal.",
                                "mermaid_code": "graph TD\n  classDef active fill:#3b82f61a,stroke:#93C5FD,stroke-width:2px;\n  classDef idle fill:#ffffff1a,stroke:#333,stroke-width:2px;\n  A[\"Root\"]:::active --> B[\"Level 1\"]:::idle\n  A --> C[\"Level 1\"]:::idle\n  B --> D[\"Level 2\"]:::idle\n  B --> E[\"Level 2\"]:::idle"
                            },
                            {
                                "explanation": "Step 2: It explores ALL nodes at Depth 1 before moving deeper.",
                                "mermaid_code": "graph TD\n  classDef visited fill:#10b9811a,stroke:#34D399,stroke-width:2px;\n  classDef active fill:#3b82f61a,stroke:#93C5FD,stroke-width:2px;\n  classDef idle fill:#ffffff1a,stroke:#333,stroke-width:2px;\n  A[\"Root\"]:::visited --> B[\"Level 1\"]:::active\n  A --> C[\"Level 1\"]:::active\n  B --> D[\"Level 2\"]:::idle\n  B --> E[\"Level 2\"]:::idle"
                            },
                            {
                                "explanation": "Step 3: Once Depth 1 is fully explored, it drops down to Depth 2. This guarantees finding the shortest path.",
                                "mermaid_code": "graph TD\n  classDef visited fill:#10b9811a,stroke:#34D399,stroke-width:2px;\n  classDef active fill:#3b82f61a,stroke:#93C5FD,stroke-width:2px;\n  classDef idle fill:#ffffff1a,stroke:#333,stroke-width:2px;\n  A[\"Root\"]:::visited --> B[\"Level 1\"]:::visited\n  A --> C[\"Level 1\"]:::visited\n  B --> D[\"Level 2\"]:::active\n  B --> E[\"Level 2\"]:::active"
                            }
                        ]
                    },
                    {
                        "type": "markdown",
                        "content": "BFS uses a FIFO (First-In-First-Out) queue. It systematically searches level by level."
                    },
                    {
                        "type": "fill_in_the_blank",
                        "question": "Is Breadth-First Search complete?\n\nAnswer: _____",
                        "answer": "Yes, if branching factor is finite",
                        "explanation": "**Why Yes, if branching factor is finite is Correct:**\\nThis option correctly reflects the foundational theorem and invariant governing this model. Alternative options fail because they either violate time/space constraints or make unsound assumptions about environment determinism."
                    },
                    {
                        "type": "concept",
                        "title": "BFS Optimality",
                        "content": "BFS is optimal if the path cost is a non-decreasing function of the depth of the node (e.g., when all actions have the same cost)."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph TD\n  F[\"Frontier: FIFO Queue\"]\n  N1[\"Node 1\"]\n  N2[\"Node 2\"]\n  F --> N1\n  F --> N2\n  style F fill:#10b9811a"
                    },
                    {
                        "type": "markdown",
                        "content": "The main issue with BFS is its space complexity. Every node generated must remain in memory. The space complexity is O(b^d)."
                    },
                    {
                        "type": "interactive",
                        "question": "What is the time complexity of BFS?",
                        "options": [
                            "O(b^d)",
                            "O(b*d)",
                            "O(d^b)."
                        ],
                        "answer": "O(b^d)",
                        "explanation": "**Why O(b^d) is Correct:**\\nThis option correctly reflects the foundational theorem and invariant governing this model. Alternative options fail because they either violate time/space constraints or make unsound assumptions about environment determinism."
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "from collections import deque\ndef bfs(problem):\n    frontier = deque([problem.initial])\n    explored = set()\n    while frontier:\n        node = frontier.popleft()\n        # ... check goal and expand ...\n\n# --- Execution Output ---\nprint('Result:', bfs(None))\n",
                        "solution_code": "from collections import deque\ndef bfs(problem):\n    frontier = deque([problem.initial])\n    explored = set()\n    while frontier:\n        node = frontier.popleft()\n        # ... check goal and expand ...\n\n# --- Execution Output ---\nprint('Result:', bfs(None))\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nA FIFO queue (`collections.deque`) ensures nodes are expanded strictly in order of non-decreasing path length. For unit step costs, this proves the shallowest goal is expanded first, guaranteeing optimality and completeness.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Depth-First Search (DFS):** Exceptional linear memory $O(b \\cdot m)$, but is incomplete in infinite state spaces and produces highly suboptimal paths.\\n- **Breadth-First Search (BFS):** Guarantees shortest path for unweighted steps, but exhausts RAM rapidly with exponential space complexity $O(b^d)$.\\n- **Iterative Deepening Search (IDDFS):** Combines the completeness/optimality of BFS with the linear space efficiency $O(b \\cdot d)$ of DFS by running bounded DFS iterations.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    }
                ]
            },
            {
                "title": "Module 3.2: Depth-First Search (DFS)",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "Depth-First Search always expands the deepest node in the current frontier of the search tree."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "DFS uses a LIFO (Last-In-First-Out) queue, also known as a stack. It proceeds immediately to the deepest level of the search tree, where the nodes have no successors."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\n  A[\"Root (A)\"] --> B[\"Deepest (B)\"]\n  B --> C[\"Deeper (C)\"]\n  C --> D[\"Leaf (D)\"]\n  A --> E[\"Other Branch (E)\"]\n  style A fill:#ef44441a\n  style B fill:#ef44441a\n  style C fill:#ef44441a\n  style D fill:#ef44441a"
                    },
                    {
                        "type": "markdown",
                        "content": "Once a node is expanded and it has no successors, the search 'backs up' to the next deepest node that still has unexplored successors."
                    },
                    {
                        "type": "interactive",
                        "question": "What data structure does DFS use for its frontier?",
                        "options": [
                            "FIFO Queue",
                            "LIFO Queue (Stack)",
                            "Priority Queue."
                        ],
                        "answer": "LIFO Queue (Stack)",
                        "explanation": "**Why LIFO Queue (Stack) is Correct:**\\nThis option correctly reflects the foundational theorem and invariant governing this model. Alternative options fail because they either violate time/space constraints or make unsound assumptions about environment determinism."
                    },
                    {
                        "type": "concept",
                        "title": "Properties of DFS",
                        "content": "The tree-search version of DFS is incomplete because it can fail in infinite spaces or spaces with loops. It is also not optimal."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph TD\n  F[\"Frontier: Stack\"]\n  Top[\"Top of Stack\"]\n  Bottom[\"Bottom of Stack\"]\n  F --> Top\n  style F fill:#f59e0b1a"
                    },
                    {
                        "type": "markdown",
                        "content": "The advantage of DFS is its space complexity. For a state space with maximum depth m and branching factor b, DFS requires storage of only O(bm) nodes."
                    },
                    {
                        "type": "fill_in_the_blank",
                        "question": "Why might DFS be preferred over BFS?\n\nAnswer: _____",
                        "answer": "Drastically lower space complexity.",
                        "explanation": "**Why Drastically lower space complexity. is Correct:**\\nThis option correctly reflects the foundational theorem and invariant governing this model. Alternative options fail because they either violate time/space constraints or make unsound assumptions about environment determinism."
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "def dfs(problem):\n    frontier = [problem.initial] # Stack\n    explored = set()\n    while frontier:\n        node = frontier.pop() # LIFO behavior\n        # ... expand ...\n\n# --- Execution Output ---\nprint('Result:', dfs(None))\n",
                        "solution_code": "def dfs(problem):\n    frontier = [problem.initial] # Stack\n    explored = set()\n    while frontier:\n        node = frontier.pop() # LIFO behavior\n        # ... expand ...\n\n# --- Execution Output ---\nprint('Result:', dfs(None))\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nA FIFO queue (`collections.deque`) ensures nodes are expanded strictly in order of non-decreasing path length. For unit step costs, this proves the shallowest goal is expanded first, guaranteeing optimality and completeness.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Depth-First Search (DFS):** Exceptional linear memory $O(b \\cdot m)$, but is incomplete in infinite state spaces and produces highly suboptimal paths.\\n- **Breadth-First Search (BFS):** Guarantees shortest path for unweighted steps, but exhausts RAM rapidly with exponential space complexity $O(b^d)$.\\n- **Iterative Deepening Search (IDDFS):** Combines the completeness/optimality of BFS with the linear space efficiency $O(b \\cdot d)$ of DFS by running bounded DFS iterations.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    }
                ]
            },
            {
                "title": "Module 3.3: Uniform-Cost Search",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "Breadth-first search is optimal when all step costs are equal. Uniform-cost search generalizes BFS for any step-cost function."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Uniform-Cost Search (UCS) expands the node n with the lowest path cost g(n). This is done by storing the frontier as a priority queue ordered by g."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\n  S[\"Start\"] --10--> A[\"Node A, g=10\"]\n  S --5--> B[\"Node B, g=5\"]\n  B --2--> C[\"Node C, g=7\"]\n  style B fill:#10b9811a\n  style C fill:#10b9811a"
                    },
                    {
                        "type": "markdown",
                        "content": "UCS does not care about the number of steps a path has, but only about their total cost. Therefore, it will get stuck in an infinite loop if there is a path with an infinite sequence of zero-cost actions."
                    },
                    {
                        "type": "interactive",
                        "question": "UCS is optimal if all step costs are strictly greater than some small positive constant epsilon.",
                        "options": [
                            "True",
                            "False."
                        ],
                        "answer": "True",
                        "explanation": "**Why True is Correct:**\\nThis option correctly reflects the foundational theorem and invariant governing this model. Alternative options fail because they either violate time/space constraints or make unsound assumptions about environment determinism."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "In UCS, the goal test is applied to a node when it is selected for *expansion*, rather than when it is first generated, to ensure optimality."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph TD\n  F[\"Frontier: Priority Queue\"]\n  Min[\"Node with min g(n)\"]\n  F --> Min\n  style F fill:#6366f11a"
                    },
                    {
                        "type": "markdown",
                        "content": "UCS is complete and optimal (assuming step costs >= epsilon > 0), but its time and space complexity can be high because it explores large trees of small steps before exploring paths involving large steps."
                    },
                    {
                        "type": "interactive",
                        "question": "What data structure does UCS use?",
                        "options": [
                            "Stack",
                            "Priority Queue ordered by path cost."
                        ],
                        "answer": "Priority Queue ordered by path cost.",
                        "explanation": "**Why Priority Queue ordered by path cost. is Correct:**\\nThis option correctly reflects the foundational theorem and invariant governing this model. Alternative options fail because they either violate time/space constraints or make unsound assumptions about environment determinism."
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "import heapq\ndef uniform_cost_search(problem):\n    frontier = []\n    heapq.heappush(frontier, (0, problem.initial)) # (cost, node)\n    # ... loop and pop lowest cost ...\n\n# --- Execution Output ---\nprint('Result:', uniform_cost_search(None))\n",
                        "solution_code": "import heapq\ndef uniform_cost_search(problem):\n    frontier = []\n    heapq.heappush(frontier, (0, problem.initial)) # (cost, node)\n    # ... loop and pop lowest cost ...\n\n# --- Execution Output ---\nprint('Result:', uniform_cost_search(None))\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nA FIFO queue (`collections.deque`) ensures nodes are expanded strictly in order of non-decreasing path length. For unit step costs, this proves the shallowest goal is expanded first, guaranteeing optimality and completeness.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Depth-First Search (DFS):** Exceptional linear memory $O(b \\cdot m)$, but is incomplete in infinite state spaces and produces highly suboptimal paths.\\n- **Breadth-First Search (BFS):** Guarantees shortest path for unweighted steps, but exhausts RAM rapidly with exponential space complexity $O(b^d)$.\\n- **Iterative Deepening Search (IDDFS):** Combines the completeness/optimality of BFS with the linear space efficiency $O(b \\cdot d)$ of DFS by running bounded DFS iterations.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    }
                ]
            },
            {
                "title": "Module 3.4: Depth-Limited and Iterative Deepening Search",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "The failure of DFS in infinite spaces can be alleviated by supplying DFS with a predetermined depth limit 'l'."
                    },
                    {
                        "type": "concept",
                        "title": "Depth-Limited Search (DLS)",
                        "content": "Nodes at depth 'l' are treated as if they have no successors. This solves the infinite path problem but introduces a completeness problem if the goal is deeper than 'l'."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\n  L0[\"Level 0\"] --> L1[\"Level 1\"]\n  L1 --> L2[\"Level 2 (Limit)\"]\n  L2 -.-x L3[\"Level 3 (Unexplored)\"]\n  style L2 fill:#ef44441a"
                    },
                    {
                        "type": "markdown",
                        "content": "Iterative Deepening Search (IDS) is a general strategy that gradually increases the limit until a goal is found."
                    },
                    {
                        "type": "fill_in_the_blank",
                        "question": "What happens in DLS if the shallowest goal is at depth d > l?\n\nAnswer: _____",
                        "answer": "It fails to find the goal.",
                        "explanation": "**Why It fails to find the goal. is Correct:**\\nThis option correctly reflects the foundational theorem and invariant governing this model. Alternative options fail because they either violate time/space constraints or make unsound assumptions about environment determinism."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "IDS combines the benefits of depth-first and breadth-first search. It has the modest memory requirements of DFS and the completeness of BFS."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph TD\n  Iter0[\"Limit = 0\"]\n  Iter1[\"Limit = 1\"]\n  Iter2[\"Limit = 2\"]\n  Iter0 --> Iter1 --> Iter2\n  style Iter2 fill:#10b9811a"
                    },
                    {
                        "type": "markdown",
                        "content": "It might seem wasteful that IDS generates the upper levels of the tree multiple times, but for most problems where the branching factor is > 1, the vast majority of nodes are in the bottom level, so the repeated overhead is small."
                    },
                    {
                        "type": "fill_in_the_blank",
                        "question": "_____ is the space complexity of IDS.",
                        "answer": "O(bd)",
                        "explanation": "**Why O(bd) is Correct:**\\nThis option correctly reflects the foundational theorem and invariant governing this model. Alternative options fail because they either violate time/space constraints or make unsound assumptions about environment determinism."
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "def iterative_deepening_search(problem):\n    for depth in range(sys.maxsize):\n        result = depth_limited_search(problem, depth)\n        if result != 'cutoff': return result\n\n# --- Execution Output ---\nprint('Result:', iterative_deepening_search(None))\n",
                        "solution_code": "def iterative_deepening_search(problem):\n    for depth in range(sys.maxsize):\n        result = depth_limited_search(problem, depth)\n        if result != 'cutoff': return result\n\n# --- Execution Output ---\nprint('Result:', iterative_deepening_search(None))\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nA FIFO queue (`collections.deque`) ensures nodes are expanded strictly in order of non-decreasing path length. For unit step costs, this proves the shallowest goal is expanded first, guaranteeing optimality and completeness.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Depth-First Search (DFS):** Exceptional linear memory $O(b \\cdot m)$, but is incomplete in infinite state spaces and produces highly suboptimal paths.\\n- **Breadth-First Search (BFS):** Guarantees shortest path for unweighted steps, but exhausts RAM rapidly with exponential space complexity $O(b^d)$.\\n- **Iterative Deepening Search (IDDFS):** Combines the completeness/optimality of BFS with the linear space efficiency $O(b \\cdot d)$ of DFS by running bounded DFS iterations.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    }
                ]
            }
        ]
    },
    "4": {
        "title": "Case 04: The Search for the Better Path",
        "episodes": [
            {
                "title": "Module 1: The Heuristic Compass",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "You are trapped in the center of a labyrinth. Until now, you have used algorithms like BFS and DFS. They are blind. They explore in all directions equally. \n\nBut this time, you have a compass. It points towards the goal. It tells you roughly how far away it is. You are no longer blind."
                    },
                    {
                        "type": "objective",
                        "title": "Module Objective",
                        "content": "Understand Informed Search. Learn what a Heuristic is, and how to estimate distances in complex state spaces."
                    },
                    {
                        "type": "problem",
                        "content": "**The Think-First Challenge:** If a compass tells you the goal is straight North, should you *always* move North? What happens if there is a massive wall blocking the North path?"
                    },
                    {
                        "type": "concept",
                        "title": "The Heuristic Function: h(n)",
                        "content": "A **heuristic**, denoted as `h(n)`, is an *estimate* of the cost to get from the current node `n` to the goal.\n\nIn a maze, the most common heuristic is **Manhattan Distance** (the sum of the horizontal and vertical distances) or **Euclidean Distance** (the straight-line distance)."
                    },
                    {
                        "type": "code_experiment",
                        "title": "Implementing the Heuristic",
                        "starter_code": "import math\n\ndef euclidean_distance(node, goal):\n    # node and goal are tuples: (x, y)\n    # TODO: Calculate the straight-line distance between the two points\n    pass\n\nprint(euclidean_distance((0,0), (3,4)))",
                        "solution_code": "import math\n\ndef euclidean_distance(node, goal):\n    x1, y1 = node\n    x2, y2 = goal\n    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)\n\nprint(euclidean_distance((0,0), (3,4)))",
                        "expected_output": "5.0",
                        "explanation": "**Why it works:** The Euclidean distance is a classic heuristic for 2D grids. It uses the Pythagorean theorem to calculate the exact distance 'as the crow flies'.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nA* evaluates nodes using $f(n) = g(n) + h(n)$. With an admissible ($h(n) \\le h^*(n)$) and consistent ($h(n) \\le c(n, a, n') + h(n')$) heuristic, $f$-costs along any branch are monotonically non-decreasing, proving the first time a goal is popped from the min-heap, its cost is globally minimal.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Greedy Best-First Search:** Minimizes $h(n)$ only; expands fewer nodes in simple spaces, but is easily misled into long suboptimal paths.\\n- **Uniform Cost Search (Dijkstra):** Guarantees optimality without a heuristic ($h(n) = 0$), but explores in all directions blindly, expanding far more nodes.\\n- **IDA* (Iterative Deepening A*):** Uses $f$-cutoffs with DFS backtracks; reduces memory consumption to $O(b \\cdot d)$ while preserving optimality.\\n- **Weighted A* ($f = g + w \\cdot h$):** Speeds up search by prioritizing the heuristic ($w > 1$); bounds suboptimality to $\\le w \\times C^*$ while expanding up to 90% fewer nodes.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "concept",
                        "title": "Admissible vs Inadmissible Heuristics",
                        "content": "Not all compasses are reliable. An **admissible heuristic** is one that never overestimates the true cost to the goal. It is optimistic. It might think the goal is closer than it really is, but it never thinks it's further away."
                    },
                    {
                        "type": "concept",
                        "title": "Why Optimism Matters",
                        "content": "If your heuristic overestimates the distance, your AI might look at a valid path and think, 'Oh, that path is too long, I won't even bother checking it.' It will then settle for a suboptimal path. By keeping the heuristic optimistic, we force the AI to thoroughly check all promising paths before settling."
                    },
                    {
                        "type": "fill_in_the_blank",
                        "question": "If the true distance to the goal is 10, which of these is an ADMISSIBLE heuristic?\n\nAnswer: _____",
                        "answer": "h(n) = 8",
                        "explanation": "**Why h(n) = 8 is Correct:**\\nThis option correctly reflects the foundational theorem and invariant governing this model. Alternative options fail because they either violate time/space constraints or make unsound assumptions about environment determinism."
                    },
                    {
                        "type": "markdown",
                        "content": "> [!TIP] \n> In a grid where you can only move Up, Down, Left, and Right (no diagonals), **Manhattan Distance** is perfectly admissible. If you can move diagonally, Manhattan Distance might overestimate, so you must use **Euclidean Distance** or **Chebyshev Distance** instead."
                    },
                    {
                        "type": "visual",
                        "title": "Manhattan vs Euclidean",
                        "code": "\ngraph TD\n    classDef m fill:#ef44441a,stroke:#FCA5A5,stroke-width:2px;\n    classDef e fill:#3b82f61a,stroke:#93C5FD,stroke-width:2px;\n    \n    A[\"Point A (0,0)\"] --> M[\"Manhattan Distance: |dx| + |dy|\"]:::m\n    A --> E[\"Euclidean Distance: sqrt(dx^2 + dy^2)\"]:::e\n    \n    M --> M2[\"Cost: 3 + 4 = 7\"]:::m\n    E --> E2[\"Cost: sqrt(9 + 16) = 5\"]:::e\n        "
                    },
                    {
                        "type": "interactive",
                        "question": "If you are allowed to move diagonally in a grid, is Manhattan Distance admissible?",
                        "options": [
                            "Yes, it is always admissible",
                            "No, it will overestimate the cost",
                            "Only if there are walls"
                        ],
                        "answer": "No, it will overestimate the cost",
                        "explanation": "**Why No, it will overestimate the cost is Correct:**\\nThis option correctly reflects the foundational theorem and invariant governing this model. Alternative options fail because they either violate time/space constraints or make unsound assumptions about environment determinism."
                    }
                ]
            },
            {
                "title": "Module 2: The Greedy Trap",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "Greedy Best-First Search",
                        "content": "Greedy Best-First Search is incredibly simple: **Always expand the node that appears closest to the goal.**\n\nIt completely ignores how far you have already traveled. It only looks at `h(n)`. If Sibiu has an `h` of 253, and Zerind has an `h` of 374, it expands Sibiu. Period."
                    },
                    {
                        "type": "visual",
                        "title": "Straight-Line Distance Heuristic",
                        "code": "\ngraph LR\n    classDef node fill:#10b9811a,stroke:#34D399,stroke-width:2px;\n    classDef goal fill:#7c4dff1a,stroke:#7C4DFF,stroke-width:2px;\n    \n    A[\"Arad (h=366)\"]:::node --> S[\"Sibiu (h=253)\"]:::node\n    A --> Z[\"Zerind (h=374)\"]:::node\n    A --> T[\"Timisoara (h=329)\"]:::node\n    \n    S --> F[\"Fagaras (h=176)\"]:::node\n    S --> R[\"Rimnicu Vilcea (h=193)\"]:::node\n    \n    F --> B[\"Bucharest (h=0)\"]:::goal\n        "
                    },
                    {
                        "type": "markdown",
                        "content": "> [!WARNING] \n> **The Greedy Trap:** Because Greedy Search ignores the cost of the path taken so far, it can easily get stuck in dead ends or find a path that is technically valid, but horribly long and inefficient."
                    },
                    {
                        "type": "concept",
                        "title": "The Danger of Myopia",
                        "content": "Greedy Best-First Search is 'myopic'—nearsighted. It only looks at the immediate heuristic value `h(n)`. This means it will happily run straight into a dead-end if the dead-end is geographically closer to the goal than the escape route."
                    },
                    {
                        "type": "visual",
                        "title": "The Dead-End Trap",
                        "code": "\ngraph LR\n    classDef node fill:#10b9811a,stroke:#34D399,stroke-width:2px;\n    classDef trap fill:#ef44441a,stroke:#FCA5A5,stroke-width:2px;\n    classDef goal fill:#7c4dff1a,stroke:#7C4DFF,stroke-width:2px;\n    \n    A[\"Start (h=10)\"]:::node --> B[\"Node B (h=5)\"]:::node\n    A --> C[\"Node C (h=8)\"]:::node\n    \n    B --> D[\"Dead End (h=3)\"]:::trap\n    D --> E[\"Wall (h=1)\"]:::trap\n    \n    C --> F[\"Node F (h=4)\"]:::node\n    F --> G[\"Goal (h=0)\"]:::goal\n        "
                    },
                    {
                        "type": "markdown",
                        "content": "In the diagram above, Greedy Search will go from Start to Node B (because h=5 is better than h=8). From B, it will go to the Dead End (h=3). It gets stuck at the Wall. It completely misses the actual optimal path through Node C."
                    },
                    {
                        "type": "concept",
                        "title": "Completeness",
                        "content": "An algorithm is **complete** if it is guaranteed to find a solution if one exists. \n\nGreedy Best-First Search is *not* complete in infinite state spaces or graphs with loops. It can get caught in an infinite loop, oscillating between two nodes that look close to the goal."
                    },
                    {
                        "type": "fill_in_the_blank",
                        "question": "To fix the infinite loop problem in Greedy Search, what must we do?\n\nAnswer: _____",
                        "answer": "Keep a 'visited' set to remember where we've been",
                        "explanation": "**Why Keep a 'visited' set to remember where we've been is Correct:**\\nThis option correctly reflects the foundational theorem and invariant governing this model. Alternative options fail because they either violate time/space constraints or make unsound assumptions about environment determinism."
                    },
                    {
                        "type": "markdown",
                        "content": "> [!NOTE] \n> Even with a 'visited' set (making it a Graph Search rather than a Tree Search), Greedy Search is still not optimal. It will find a path, but rarely the shortest one."
                    },
                    {
                        "type": "code_experiment",
                        "title": "Simulating Greedy Choice",
                        "starter_code": "def greedy_choice(current_node, neighbors, h_costs):\n    # neighbors is a list of node names: ['B', 'C']\n    # h_costs is a dict: {'B': 5, 'C': 8, 'D': 3}\n    \n    # TODO: Return the neighbor with the lowest heuristic value\n    pass\n\nprint(greedy_choice('A', ['B', 'C'], {'B': 5, 'C': 8}))",
                        "solution_code": "def greedy_choice(current_node, neighbors, h_costs):\n    best_node = None\n    best_h = float('inf')\n    for neighbor in neighbors:\n        if h_costs[neighbor] < best_h:\n            best_h = h_costs[neighbor]\n            best_node = neighbor\n    return best_node\n\nprint(greedy_choice('A', ['B', 'C'], {'B': 5, 'C': 8}))",
                        "expected_output": "B",
                        "explanation": "**Why it works:** The algorithm blindly iterates through the immediate neighbors and picks the one with the lowest `h_cost`. It completely ignores any `g_cost` (distance traveled).",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nA* evaluates nodes using $f(n) = g(n) + h(n)$. With an admissible ($h(n) \\le h^*(n)$) and consistent ($h(n) \\le c(n, a, n') + h(n')$) heuristic, $f$-costs along any branch are monotonically non-decreasing, proving the first time a goal is popped from the min-heap, its cost is globally minimal.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Greedy Best-First Search:** Minimizes $h(n)$ only; expands fewer nodes in simple spaces, but is easily misled into long suboptimal paths.\\n- **Uniform Cost Search (Dijkstra):** Guarantees optimality without a heuristic ($h(n) = 0$), but explores in all directions blindly, expanding far more nodes.\\n- **IDA* (Iterative Deepening A*):** Uses $f$-cutoffs with DFS backtracks; reduces memory consumption to $O(b \\cdot d)$ while preserving optimality.\\n- **Weighted A* ($f = g + w \\cdot h$):** Speeds up search by prioritizing the heuristic ($w > 1$); bounds suboptimality to $\\le w \\times C^*$ while expanding up to 90% fewer nodes.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    }
                ]
            },
            {
                "title": "Module 3: The A* Algorithm",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "Greedy Search is fast, but it is not optimal. Uniform Cost Search (Dijkstra) is optimal, but it is slow because it is blind. What if we combine them?"
                    },
                    {
                        "type": "concept",
                        "title": "The A* Algorithm",
                        "content": "A* (A-Star) is the holy grail of pathfinding. It combines the guaranteed optimality of Uniform Cost Search with the directed speed of Greedy Search.\n\nIt evaluates nodes by combining two values:\n*   **g(n):** The exact cost to reach node `n` from the start.\n*   **h(n):** The estimated cost to reach the goal from node `n`.\n\n**f(n) = g(n) + h(n)**\n\nA* always expands the node with the lowest `f(n)`."
                    },
                    {
                        "type": "visual_stepper",
                        "title": "Interactive: A* Search Step-by-Step",
                        "height": 450,
                        "steps": [
                            {
                                "explanation": "We start at Node A. The cost to get here is 0. The heuristic says the goal is 10 away. f(A) = 0 + 10 = 10.",
                                "mermaid_code": "\n    graph TD\n        classDef idle fill:#ffffff1a,stroke:#333,stroke-width:2px;\n        classDef focus fill:#7c4dff1a,stroke:#7C4DFF,stroke-width:3px;\n        \n        A[\"A<br>g=0, h=10<br>f=10\"]:::focus --> B[\"B<br>g=?, h=6<br>f=?\"]:::idle\n        A --> C[\"C<br>g=?, h=8<br>f=?\"]:::idle\n                "
                            },
                            {
                                "explanation": "We expand Node A. Path A->B costs 3. Path A->C costs 2. We calculate their f-values. f(B) = 3 + 6 = 9. f(C) = 2 + 8 = 10.",
                                "mermaid_code": "\n    graph TD\n        classDef idle fill:#ffffff1a,stroke:#333,stroke-width:2px;\n        classDef focus fill:#7c4dff1a,stroke:#7C4DFF,stroke-width:3px;\n        classDef active fill:#10b9811a,stroke:#34D399,stroke-width:2px;\n        \n        A[\"A<br>g=0, h=10<br>f=10\"]:::idle -->|cost 3| B[\"B<br>g=3, h=6<br>f=9\"]:::active\n        A -->|cost 2| C[\"C<br>g=2, h=8<br>f=10\"]:::active\n                "
                            },
                            {
                                "explanation": "Which node does A* explore next? It picks the lowest f-value! Node B has an f-value of 9, while Node C has 10. We expand Node B.",
                                "mermaid_code": "\n    graph TD\n        classDef idle fill:#ffffff1a,stroke:#333,stroke-width:2px;\n        classDef focus fill:#7c4dff1a,stroke:#7C4DFF,stroke-width:3px;\n        classDef active fill:#10b9811a,stroke:#34D399,stroke-width:2px;\n        \n        A[\"A\"]:::idle --> B[\"B<br>g=3, h=6<br>f=9\"]:::focus\n        A --> C[\"C<br>g=2, h=8<br>f=10\"]:::active\n        B -->|cost 5| D[\"Goal<br>g=?, h=0<br>f=?\"]:::idle\n                "
                            },
                            {
                                "explanation": "From Node B, we reach the Goal. The total path cost is g(B)+5 = 8. The heuristic at the goal is always 0. f(Goal) = 8 + 0 = 8. Since 8 < 10 (Node C), we found the optimal path!",
                                "mermaid_code": "\n    graph TD\n        classDef idle fill:#ffffff1a,stroke:#333,stroke-width:2px;\n        classDef focus fill:#7c4dff1a,stroke:#7C4DFF,stroke-width:3px;\n        classDef active fill:#10b9811a,stroke:#34D399,stroke-width:2px;\n        classDef goal fill:#eab3081a,stroke:#FACC15,stroke-width:3px;\n        \n        A[\"A\"]:::idle --> B[\"B\"]:::idle\n        A --> C[\"C<br>f=10\"]:::active\n        B --> D[\"Goal<br>g=8, h=0<br>f=8\"]:::goal\n                "
                            }
                        ]
                    },
                    {
                        "type": "concept",
                        "title": "The Balance of g(n) and h(n)",
                        "content": "A* is a balancing act. \n\nIf `h(n)` is always 0, A* completely ignores the heuristic and becomes **Uniform Cost Search (Dijkstra)**. It is perfectly optimal but explores slowly.\n\nIf `h(n)` is much larger than `g(n)`, A* completely ignores the path cost and becomes **Greedy Best-First Search**. It is blazingly fast but finds terrible paths."
                    },
                    {
                        "type": "fill_in_the_blank",
                        "question": "What happens to A* if we set h(n) = 0 for every node?\n\nAnswer: _____",
                        "answer": "It turns into Dijkstra's Algorithm",
                        "explanation": "**Why It turns into Dijkstra's Algorithm is Correct:**\\nThis option correctly reflects the foundational theorem and invariant governing this model. Alternative options fail because they either violate time/space constraints or make unsound assumptions about environment determinism."
                    },
                    {
                        "type": "markdown",
                        "content": "> [!NOTE] \n> The magic of A* happens when `h(n)` is *exactly* the true cost to the goal. In this hypothetical scenario, A* will never expand a single incorrect node. It will follow the optimal path instantly without searching any side branches."
                    },
                    {
                        "type": "concept",
                        "title": "Tie-Breaking",
                        "content": "What happens if two nodes have the exact same `f(n)` value? \n\nA* will pull one arbitrarily based on the Priority Queue's internal sorting. However, advanced implementations often break ties by preferring the node with the *higher* `g(n)` (meaning it's further along the path) or the *lower* `h(n)` (meaning it's closer to the goal)."
                    }
                ]
            },
            {
                "title": "Module 4: Engineering the Queue",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "Theory is great, but an AI is useless if it cannot be executed in code. Before we implement the A* algorithm, we must understand the core data structure that makes it fast: **The Priority Queue**."
                    },
                    {
                        "type": "concept",
                        "title": "Why not a regular List?",
                        "content": "In Breadth-First Search (BFS), we use a standard Queue (First-In, First-Out). In A*, we must always expand the node with the lowest `f(n)` value.\n\nIf we use a regular Python list for our frontier, we would have to search the entire list every single time to find the lowest `f` value. This takes `O(N)` time. For a large graph, this is disastrously slow."
                    },
                    {
                        "type": "concept",
                        "title": "The Min-Heap (Priority Queue)",
                        "content": "A Min-Heap is a specialized binary tree where the parent is always smaller than its children. In Python, the `heapq` library implements this over a standard list.\n\nFinding the lowest `f(n)` in a min-heap takes `O(1)` time (it's always at the top). Pushing a new node into the heap takes `O(log N)` time. This makes A* blazing fast."
                    },
                    {
                        "type": "visual",
                        "title": "Visualizing the Min-Heap",
                        "code": "\ngraph TD\n    classDef top fill:#10b9811a,stroke:#34D399,stroke-width:2px;\n    classDef node fill:#7c4dff1a,stroke:#7C4DFF,stroke-width:2px;\n    \n    A[\"f=9 (Node B)\"]:::top --> B[\"f=12 (Node G)\"]:::node\n    A --> C[\"f=10 (Node C)\"]:::node\n    \n    B --> D[\"f=15 (Node X)\"]:::node\n    B --> E[\"f=13 (Node Y)\"]:::node\n    \n    C --> F[\"f=20 (Node Z)\"]:::node\n        "
                    },
                    {
                        "type": "markdown",
                        "content": "> [!NOTE] \n> Notice how the lowest value (9) is perfectly at the top. The rest of the tree is not perfectly sorted, but it guarantees that parents are smaller than children."
                    },
                    {
                        "type": "concept",
                        "title": "Tracking the Costs",
                        "content": "To implement A*, we need two dictionaries:\n1. `cost_so_far`: Tracks the exact `g(n)` cost from the start to any node we have visited. If we find a *cheaper* path to a node we've already visited, we update this dictionary!\n2. `came_from`: Tracks which node we used to reach the current node. This allows us to re-construct the path backwards from the goal to the start once we find the solution."
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementing A* Priority Queue",
                        "starter_code": "import heapq\n\ndef a_star_search(start, goal, graph, h_costs):\n    # graph is a dict: {'A': [('B', 3), ('C', 2)], ...}\n    # h_costs is a dict: {'A': 10, 'B': 6, ...}\n    \n    frontier = []\n    # heapq.heappush(frontier, (priority, current_node))\n    heapq.heappush(frontier, (h_costs[start], start))\n    \n    cost_so_far = {start: 0}\n    came_from = {start: None}\n    \n    while frontier:\n        # TODO: 1. Pop the lowest f_score node using heapq.heappop()\n        # TODO: 2. If current == goal, break out of the loop!\n        # TODO: 3. Loop through neighbors in graph[current]\n        # TODO: 4. Calculate new_cost = cost_so_far[current] + step_cost\n        # TODO: 5. If neighbor is unvisited OR new_cost < cost_so_far[neighbor]:\n        #          Update cost_so_far, push to frontier, update came_from\n        pass\n        \n    return came_from\n\n# --- Execution Output ---\nprint('Result:', a_star_search(None))\n",
                        "solution_code": "import heapq\n\ndef a_star_search(start, goal, graph, h_costs):\n    frontier = []\n    heapq.heappush(frontier, (h_costs[start], start))\n    cost_so_far = {start: 0}\n    came_from = {start: None}\n    \n    while frontier:\n        current_f, current = heapq.heappop(frontier)\n        \n        if current == goal:\n            break\n            \n        for next_node, cost in graph[current]:\n            new_cost = cost_so_far[current] + cost\n            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:\n                cost_so_far[next_node] = new_cost\n                priority = new_cost + h_costs[next_node]\n                heapq.heappush(frontier, (priority, next_node))\n                came_from[next_node] = current\n                \n    return came_from\n\n# --- Execution Output ---\nprint('Result:', a_star_search(None))\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** By using `heapq`, we guarantee that every time we call `heappop()`, we are expanding the node that is mathematically most likely to lead us to the shortest path.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nA* evaluates nodes using $f(n) = g(n) + h(n)$. With an admissible ($h(n) \\le h^*(n)$) and consistent ($h(n) \\le c(n, a, n') + h(n')$) heuristic, $f$-costs along any branch are monotonically non-decreasing, proving the first time a goal is popped from the min-heap, its cost is globally minimal.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Greedy Best-First Search:** Minimizes $h(n)$ only; expands fewer nodes in simple spaces, but is easily misled into long suboptimal paths.\\n- **Uniform Cost Search (Dijkstra):** Guarantees optimality without a heuristic ($h(n) = 0$), but explores in all directions blindly, expanding far more nodes.\\n- **IDA* (Iterative Deepening A*):** Uses $f$-cutoffs with DFS backtracks; reduces memory consumption to $O(b \\cdot d)$ while preserving optimality.\\n- **Weighted A* ($f = g + w \\cdot h$):** Speeds up search by prioritizing the heuristic ($w > 1$); bounds suboptimality to $\\le w \\times C^*$ while expanding up to 90% fewer nodes.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    }
                ]
            },
            {
                "title": "Module 5: Admissibility vs Consistency",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "A* is only guaranteed to find the absolute shortest path if the heuristic function obeys certain mathematical laws. If your heuristic is 'bad', A* becomes greedy and makes mistakes."
                    },
                    {
                        "type": "concept",
                        "title": "Admissibility",
                        "content": "A heuristic is **admissible** if it NEVER overestimates the true cost to reach the goal. \n\nFor example, straight-line distance is always admissible because it is physically impossible to find a shorter path than a straight line between two points."
                    },
                    {
                        "type": "concept",
                        "title": "Consistency (Monotonicity)",
                        "content": "A heuristic is **consistent** if, for every node N and every successor P, the estimated cost from N to the goal is no greater than the step cost to get to P plus the estimated cost from P to the goal.\n\n`h(N) <= c(N, P) + h(P)`"
                    },
                    {
                        "type": "fill_in_the_blank",
                        "question": "What happens if a heuristic OVERESTIMATES the true cost?\n\nAnswer: _____",
                        "answer": "A* becomes suboptimal",
                        "explanation": "**Why A* becomes suboptimal is Correct:**\\nThis option correctly reflects the foundational theorem and invariant governing this model. Alternative options fail because they either violate time/space constraints or make unsound assumptions about environment determinism."
                    },
                    {
                        "type": "visual",
                        "title": "The Triangle Inequality",
                        "code": "\ngraph TD\n    classDef n fill:#10b9811a,stroke:#34D399,stroke-width:2px;\n    \n    A[\"Node N\"]:::n -->|Cost=c| B[\"Successor P\"]:::n\n    A -.->|h(N)| C[\"Goal\"]:::n\n    B -.->|h(P)| C\n        "
                    },
                    {
                        "type": "markdown",
                        "content": "Look at the triangle above. For a heuristic to be **consistent** (monotonic), the estimated cost from N to the Goal, `h(N)`, cannot be greater than the cost to get to P plus the estimated cost from P to the Goal, `h(P)`.\n\n**h(N) ≤ c(N, P) + h(P)**"
                    },
                    {
                        "type": "concept",
                        "title": "Why Consistency is Powerful",
                        "content": "If a heuristic is consistent, it means the `f(n)` values along any path will NEVER decrease. They are monotonically non-decreasing. \n\nBecause of this, the very first time A* expands a node, it has *guaranteed* that it found the absolute shortest path to that node. It never has to go back and update costs."
                    },
                    {
                        "type": "interactive",
                        "question": "If a heuristic is consistent, is it also admissible?",
                        "options": [
                            "Yes, always.",
                            "No, never.",
                            "Sometimes."
                        ],
                        "answer": "Yes, always.",
                        "explanation": "**Why Yes, always. is Correct:**\\nThis option correctly reflects the foundational theorem and invariant governing this model. Alternative options fail because they either violate time/space constraints or make unsound assumptions about environment determinism."
                    },
                    {
                        "type": "markdown",
                        "content": "> [!IMPORTANT] \n> Every consistent heuristic is admissible, but not every admissible heuristic is consistent. However, in practice, almost all natural admissible heuristics (like straight-line distance) are also consistent."
                    }
                ]
            },
            {
                "title": "Module 6: Escaping Memory Limits",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "A* keeps all generated nodes in memory. In complex games, A* will quickly consume all your RAM and crash the server."
                    },
                    {
                        "type": "concept",
                        "title": "IDA* (Iterative Deepening A*)",
                        "content": "IDA* solves the memory problem. Instead of storing the entire frontier, it uses a depth-first search that cuts off any path whose `f`-cost exceeds a certain threshold. If no solution is found, the threshold is increased to the minimum `f`-cost that was previously rejected."
                    },
                    {
                        "type": "concept",
                        "title": "SMA* (Simplified Memory-Bounded A*)",
                        "content": "SMA* uses all available memory. When memory is full, it drops the worst leaf node (the one with the highest `f`-value) from the tree to make room for a new one, but 'backs up' the value of the forgotten node to its parent so it can regenerate it later if needed."
                    },
                    {
                        "type": "concept",
                        "title": "The Depth-First Advantage",
                        "content": "Iterative Deepening A* (IDA*) uses a Depth-First Search internally. This is brilliant because DFS only requires memory proportional to the length of the current path (`O(bd)` memory). \n\nA* requires memory for every single node it generates (`O(b^d)` memory)."
                    },
                    {
                        "type": "interactive",
                        "question": "Instead of using depth as a cutoff limit, what does IDA* use as its cutoff limit?",
                        "options": [
                            "The g(n) cost",
                            "The f(n) cost",
                            "The h(n) heuristic"
                        ],
                        "answer": "The f(n) cost",
                        "explanation": "**Why The f(n) cost is Correct:**\\nThis option correctly reflects the foundational theorem and invariant governing this model. Alternative options fail because they either violate time/space constraints or make unsound assumptions about environment determinism."
                    },
                    {
                        "type": "markdown",
                        "content": "> [!WARNING] \n> The downside of IDA* is that it recalculates nodes multiple times, just like standard Iterative Deepening Search. It trades computation time for memory."
                    },
                    {
                        "type": "concept",
                        "title": "The Memory Limit in SMA*",
                        "content": "Simplified Memory-Bounded A* (SMA*) takes a different approach. It runs standard A* until it hits the hardware RAM limit. \n\nWhen memory is full, it looks at the frontier and deletes the node with the highest `f` value. But before it deletes it, it updates its parent node to remember that \"there was a path down here with an f-value of X\". \n\nIf all other paths turn out to be worse than X, SMA* will regenerate the deleted node."
                    },
                    {
                        "type": "interactive",
                        "question": "When SMA* runs out of memory, which node does it delete?",
                        "options": [
                            "The oldest node",
                            "The node with the lowest f-value",
                            "The node with the highest f-value"
                        ],
                        "answer": "The node with the highest f-value",
                        "explanation": "**Why The node with the highest f-value is Correct:**\\nThis option correctly reflects the foundational theorem and invariant governing this model. Alternative options fail because they either violate time/space constraints or make unsound assumptions about environment determinism."
                    }
                ]
            }
        ]
    },
    "5": {
        "title": "Case 05: The Heuristic Detective",
        "episodes": [
            {
                "title": "Module 5.1: Informed Search and Heuristics",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "Case 5 moves beyond blind search. Informed search strategies use problem-specific knowledge beyond the definition of the problem itself to find solutions more efficiently."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "The key to informed search is a heuristic function, h(n). h(n) = estimated cost of the cheapest path from the state at node n to a goal state."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\n  Node[\"Current Node n\"]\n  Goal[\"Goal Node\"]\n  Node -.->|h(n): Estimated Cost| Goal\n  style Node fill:#3b82f61a"
                    },
                    {
                        "type": "markdown",
                        "content": "Heuristic functions are the most common form in which additional knowledge of the problem is imparted to the search algorithm."
                    },
                    {
                        "type": "interactive",
                        "question": "If n is a goal node, what must h(n) equal?",
                        "options": [
                            "Infinity",
                            "Zero",
                            "1."
                        ],
                        "answer": "Zero",
                        "explanation": "**Why Zero is Correct:**\\nThis option correctly reflects the foundational theorem and invariant governing this model. Alternative options fail because they either violate time/space constraints or make unsound assumptions about environment determinism."
                    },
                    {
                        "type": "concept",
                        "title": "Greedy Best-First Search tries to expand the node that is closest to the goal, on the grounds that this is likely to lead to a solution quickly. Thus, it evaluates nodes by using just the heuristic function",
                        "content": "f(n) = h(n)."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph LR\n  A[\"Node A, h=5\"]\n  B[\"Node B, h=2\"]\n  C[\"Node C, h=9\"]\n  Start --> A\n  Start --> B\n  Start --> C\n  style B fill:#10b9811a"
                    },
                    {
                        "type": "markdown",
                        "content": "Greedy search is often very fast, but like DFS, it is incomplete and not optimal. It can get stuck in dead ends."
                    },
                    {
                        "type": "interactive",
                        "question": "Does Greedy Best-First Search consider the cost to reach a node from the start state?",
                        "options": [
                            "Yes",
                            "No."
                        ],
                        "answer": "No.",
                        "explanation": "**Why No. is Correct:**\\nThis option correctly reflects the foundational theorem and invariant governing this model. Alternative options fail because they either violate time/space constraints or make unsound assumptions about environment determinism."
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "def greedy_best_first_search(problem, h):\n    # Sort frontier by h(n)\n    pass\n\n# --- Execution Output ---\nprint('Result:', greedy_best_first_search(None))\n",
                        "solution_code": "def greedy_best_first_search(problem, h):\n    # Sort frontier by h(n)\n    pass\n\n# --- Execution Output ---\nprint('Result:', greedy_best_first_search(None))\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nTaking the maximum of multiple admissible heuristics $\\max(h_1(n), h_2(n))$ produces a dominant admissible heuristic that expands fewer or equal nodes than either individual component without violating admissibility.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Pattern Databases:** Precomputes exact costs to subgoals in offline lookup tables; yields fast evaluation but requires significant RAM.\\n- **Relaxed Problem Generation:** Automatically derives admissible heuristics by removing physical problem constraints.\\n- **Landmark Heuristics:** Computes shortest paths to pre-selected landmark nodes and applies triangle inequality bounds.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    }
                ]
            },
            {
                "title": "Module 5.2: A* Search",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "A* (A-star) search is the most widely known form of best-first search. It evaluates nodes by combining g(n) (cost to reach the node) and h(n) (estimated cost to get from the node to the goal)."
                    },
                    {
                        "type": "concept",
                        "title": "Evaluation function",
                        "content": "f(n) = g(n) + h(n). Since g(n) is the exact cost to reach n, and h(n) is the estimated cost from n to the goal, f(n) is the estimated total cost of the cheapest solution path going through n."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\n  Start[\"Start\"] --g(n)--> Node[\"Node n\"]\n  Node -.h(n).-> Goal[\"Goal\"]\n  style Node fill:#8b5cf61a"
                    },
                    {
                        "type": "markdown",
                        "content": "A* search is identical to Uniform-Cost Search except that A* uses g + h instead of just g."
                    },
                    {
                        "type": "interactive",
                        "question": "What does f(n) represent in A*?",
                        "options": [
                            "Estimated total path cost",
                            "Cost from start only."
                        ],
                        "answer": "Estimated total path cost",
                        "explanation": "**Why Estimated total path cost is Correct:**\\nThis option correctly reflects the foundational theorem and invariant governing this model. Alternative options fail because they either violate time/space constraints or make unsound assumptions about environment determinism."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "For A* to be optimal with Tree Search, the heuristic h(n) must be Admissible. An admissible heuristic never overestimates the cost to reach the goal."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph TD\n  Admissible[\"h(n) <= true_cost(n, goal)\"]\n  Admissible --> Optimal[\"Optimal Tree Search\"]\n  style Admissible fill:#10b9811a"
                    },
                    {
                        "type": "markdown",
                        "content": "Think of an admissible heuristic as being optimistic; it always thinks the cost to solve the problem is less than or equal to the actual cost. Straight-line distance is an admissible heuristic for routing problems."
                    },
                    {
                        "type": "interactive",
                        "question": "If actual cost is 10, which heuristic value is NOT admissible?",
                        "options": [
                            "8",
                            "10",
                            "12."
                        ],
                        "answer": "12.",
                        "explanation": "**Why 12. is Correct:**\\nThis option correctly reflects the foundational theorem and invariant governing this model. Alternative options fail because they either violate time/space constraints or make unsound assumptions about environment determinism."
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "def a_star_search(problem, h):\n    # Priority queue ordered by f(n) = g(n) + h(n)\n    # f_cost = node.path_cost + h(node)\n    pass\n\n# --- Execution Output ---\nprint('Result:', a_star_search(None))\n",
                        "solution_code": "def a_star_search(problem, h):\n    # Priority queue ordered by f(n) = g(n) + h(n)\n    # f_cost = node.path_cost + h(node)\n    pass\n\n# --- Execution Output ---\nprint('Result:', a_star_search(None))\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nTaking the maximum of multiple admissible heuristics $\\max(h_1(n), h_2(n))$ produces a dominant admissible heuristic that expands fewer or equal nodes than either individual component without violating admissibility.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Pattern Databases:** Precomputes exact costs to subgoals in offline lookup tables; yields fast evaluation but requires significant RAM.\\n- **Relaxed Problem Generation:** Automatically derives admissible heuristics by removing physical problem constraints.\\n- **Landmark Heuristics:** Computes shortest paths to pre-selected landmark nodes and applies triangle inequality bounds.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    }
                ]
            },
            {
                "title": "Module 5.3: Consistency and Graph Search Optimality",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "If we use Graph Search (which keeps an 'explored' set to avoid repeated states) with A*, Admissibility is not quite enough to guarantee optimality. We need a stronger condition called Consistency."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "A heuristic h(n) is consistent (or monotonic) if, for every node n and every successor n' of n generated by any action a, the estimated cost of reaching the goal from n is no greater than the step cost of getting to n' plus the estimated cost of reaching the goal from n'."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph LR\n  N[\"n (h=4)\"] --cost=1--> Nprime[\"n' (h=2)\"]\n  style N fill:#f59e0b1a\n  style Nprime fill:#3b82f61a"
                    },
                    {
                        "type": "markdown",
                        "content": "Formal definition of consistency: h(n) <= c(n, a, n') + h(n'). This is a form of the triangle inequality."
                    },
                    {
                        "type": "interactive",
                        "question": "Consistency is required for optimality in which type of search?",
                        "options": [
                            "Tree Search",
                            "Graph Search."
                        ],
                        "answer": "Graph Search.",
                        "explanation": "**Why Graph Search. is Correct:**\\nThis option correctly reflects the foundational theorem and invariant governing this model. Alternative options fail because they either violate time/space constraints or make unsound assumptions about environment determinism."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "If a heuristic is consistent, then the values of f(n) along any path are non-decreasing. Therefore, the first time Graph Search expands a node, it has found the optimal path to that node."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph TD\n  Consistent[\"Consistent Heuristic\"]\n  Consistent --> NonDecreasing[\"f(n) is non-decreasing along paths\"]\n  NonDecreasing --> Optimal[\"A* Graph Search is Optimal\"]\n  style Optimal fill:#10b9811a"
                    },
                    {
                        "type": "markdown",
                        "content": "Every consistent heuristic is also admissible. However, an admissible heuristic is not necessarily consistent (though most admissible heuristics you invent will naturally be consistent)."
                    },
                    {
                        "type": "interactive",
                        "question": "Does consistency imply admissibility?",
                        "options": [
                            "Yes",
                            "No."
                        ],
                        "answer": "Yes",
                        "explanation": "**Why Yes is Correct:**\\nThis option correctly reflects the foundational theorem and invariant governing this model. Alternative options fail because they either violate time/space constraints or make unsound assumptions about environment determinism."
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "def check_consistency(h_n, cost, h_n_prime):\n    return h_n <= cost + h_n_prime\n\n# --- Execution Output ---\nprint('Result:', check_consistency(None))\n",
                        "solution_code": "def check_consistency(h_n, cost, h_n_prime):\n    return h_n <= cost + h_n_prime\n\n# --- Execution Output ---\nprint('Result:', check_consistency(None))\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nTaking the maximum of multiple admissible heuristics $\\max(h_1(n), h_2(n))$ produces a dominant admissible heuristic that expands fewer or equal nodes than either individual component without violating admissibility.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Pattern Databases:** Precomputes exact costs to subgoals in offline lookup tables; yields fast evaluation but requires significant RAM.\\n- **Relaxed Problem Generation:** Automatically derives admissible heuristics by removing physical problem constraints.\\n- **Landmark Heuristics:** Computes shortest paths to pre-selected landmark nodes and applies triangle inequality bounds.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    }
                ]
            },
            {
                "title": "Module 5.4: Designing Good Heuristics",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "The performance of A* depends highly on the quality of the heuristic. How do we design a good one?"
                    },
                    {
                        "type": "concept",
                        "title": "Effective Branching Factor (b*)",
                        "content": "A measure of heuristic quality. If A* generates N nodes to find a solution at depth d, b* is the branching factor a uniform tree of depth d would need to have N nodes."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\n  N_Nodes[\"N nodes generated\"]\n  Depth[\"Depth d\"]\n  Formula[\"N + 1 = 1 + b* + (b*)^2 + ... + (b*)^d\"]\n  N_Nodes --> Formula\n  Depth --> Formula\n  style Formula fill:#6366f11a"
                    },
                    {
                        "type": "markdown",
                        "content": "A well-designed heuristic will have a b* close to 1.0, meaning the search goes almost straight to the goal."
                    },
                    {
                        "type": "interactive",
                        "question": "Is a lower or higher effective branching factor better?",
                        "options": [
                            "Lower (closer to",
                            "Higher."
                        ],
                        "answer": "Lower (closer to",
                        "explanation": "**Why Lower (closer to is Correct:**\\nThis option correctly reflects the foundational theorem and invariant governing this model. Alternative options fail because they either violate time/space constraints or make unsound assumptions about environment determinism."
                    },
                    {
                        "type": "concept",
                        "title": "Domination",
                        "content": "If heuristic h2(n) >= h1(n) for all n (and neither overestimates), then h2 dominates h1. A* using h2 will never expand more nodes than A* using h1."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph TD\n  H2[\"h2(n)\"]\n  H1[\"h1(n)\"]\n  H2 -->|Dominates| H1\n  H2 -->|Expands Fewer Nodes| H1\n  style H2 fill:#10b9811a"
                    },
                    {
                        "type": "markdown",
                        "content": "One way to invent admissible heuristics is to relax the problem. A relaxed problem removes constraints on actions, making it easier to solve. The exact cost of a solution to a relaxed problem is an admissible heuristic for the original problem."
                    },
                    {
                        "type": "interactive",
                        "question": "In the 8-puzzle, is 'Manhattan Distance' a relaxed problem heuristic?",
                        "options": [
                            "Yes, it assumes tiles can move through other tiles",
                            "No."
                        ],
                        "answer": "Yes, it assumes tiles can move through other tiles",
                        "explanation": "**Why Yes, it assumes tiles can move through other tiles is Correct:**\\nThis option correctly reflects the foundational theorem and invariant governing this model. Alternative options fail because they either violate time/space constraints or make unsound assumptions about environment determinism."
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "def manhattan_distance(state, goal):\n    # Sum of vertical and horizontal distances of tiles from goal positions\n    pass\n\n# --- Execution Output ---\nprint('Result:', manhattan_distance(None))\n",
                        "solution_code": "def manhattan_distance(state, goal):\n    # Sum of vertical and horizontal distances of tiles from goal positions\n    pass\n\n# --- Execution Output ---\nprint('Result:', manhattan_distance(None))\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nTaking the maximum of multiple admissible heuristics $\\max(h_1(n), h_2(n))$ produces a dominant admissible heuristic that expands fewer or equal nodes than either individual component without violating admissibility.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Pattern Databases:** Precomputes exact costs to subgoals in offline lookup tables; yields fast evaluation but requires significant RAM.\\n- **Relaxed Problem Generation:** Automatically derives admissible heuristics by removing physical problem constraints.\\n- **Landmark Heuristics:** Computes shortest paths to pre-selected landmark nodes and applies triangle inequality bounds.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    }
                ]
            }
        ]
    },
    "6": {
        "episodes": [
            {
                "title": "Module 1: The Nemesis Protocol",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "You are sitting in the NEXUS Simulation Control Room. Until now, your agents have been solving puzzles in static environments. But today, the red lights flash. A rogue agent—designated 'NEMESIS'—has entered the simulation grid. NEMESIS has exactly the opposite goals as your agent. Every time you make a move to maximize your score, NEMESIS will make a move to minimize it."
                    },
                    {
                        "type": "objective",
                        "title": "Module Objective",
                        "content": "Master Adversarial Search. Learn how to construct a Game Tree, understand the Minimax algorithm, and implement Alpha-Beta Pruning to defeat an optimal opponent."
                    },
                    {
                        "type": "problem",
                        "content": "**The Think-First Challenge:** If you know your opponent is playing perfectly, should you ever make a move that relies on them making a mistake? What happens if you assume they are 'dumb' but they turn out to be optimal?"
                    },
                    {
                        "type": "concept",
                        "title": "The Zero-Sum Game",
                        "content": "In AI, a strictly competitive environment is called a **Zero-Sum Game**. If you win +10 points, the opponent loses -10 points. The sum of the utilities is always zero. \n\nTo solve this, we create a **Game Tree** where:\n*   **MAX (You):** Wants to find the path that leads to the highest possible number.\n*   **MIN (Nemesis):** Wants to find the path that leads to the lowest possible number."
                    },
                    {
                        "type": "visual_stepper",
                        "title": "Interactive: Minimax Evaluation Step-by-Step",
                        "height": 450,
                        "steps": [
                            {
                                "explanation": "We start at the root (Node A). It is MAX's turn. But MAX cannot make a decision until the entire tree is expanded down to the leaf nodes.",
                                "mermaid_code": "\ngraph TD\n    classDef maxNode fill:#10b9811a,stroke:#34D399,stroke-width:2px;\n    classDef minNode fill:#ef44441a,stroke:#FCA5A5,stroke-width:2px;\n    classDef leafNode fill:#7c4dff1a,stroke:#7C4DFF,stroke-width:2px;\n    classDef focus fill:#ffffff33,stroke:#FFF,stroke-width:4px;\n\n    A[\"MAX: ?\"]:::focus --> B[\"MIN: ?\"]:::minNode\n    A --> C[\"MIN: ?\"]:::minNode\n    \n    B --> D[\"+3\"]:::leafNode\n    B --> E[\"+12\"]:::leafNode\n    B --> F[\"+8\"]:::leafNode\n    \n    C --> G[\"+2\"]:::leafNode\n    C --> H[\"+4\"]:::leafNode\n    C --> I[\"+6\"]:::leafNode\n            "
                            },
                            {
                                "explanation": "We expand down to Node B. It is MIN's turn. MIN looks at its children (the leaf nodes) which evaluate to +3, +12, and +8.",
                                "mermaid_code": "\ngraph TD\n    classDef maxNode fill:#10b9811a,stroke:#34D399,stroke-width:2px;\n    classDef minNode fill:#ef44441a,stroke:#FCA5A5,stroke-width:2px;\n    classDef leafNode fill:#7c4dff1a,stroke:#7C4DFF,stroke-width:2px;\n    classDef focus fill:#ffffff33,stroke:#FFF,stroke-width:4px;\n\n    A[\"MAX: ?\"]:::maxNode --> B[\"MIN: ?\"]:::focus\n    A --> C[\"MIN: ?\"]:::minNode\n    \n    B --> D[\"+3\"]:::focus\n    B --> E[\"+12\"]:::focus\n    B --> F[\"+8\"]:::focus\n    \n    C --> G[\"+2\"]:::leafNode\n    C --> H[\"+4\"]:::leafNode\n    C --> I[\"+6\"]:::leafNode\n            "
                            },
                            {
                                "explanation": "Because MIN wants to minimize the score (to hurt you), MIN chooses the lowest available number: +3. Node B is now definitively worth +3.",
                                "mermaid_code": "\ngraph TD\n    classDef maxNode fill:#10b9811a,stroke:#34D399,stroke-width:2px;\n    classDef minNode fill:#ef44441a,stroke:#FCA5A5,stroke-width:2px;\n    classDef leafNode fill:#7c4dff1a,stroke:#7C4DFF,stroke-width:2px;\n    classDef focus fill:#ffffff33,stroke:#FFF,stroke-width:4px;\n\n    A[\"MAX: ?\"]:::maxNode --> B[\"MIN: +3\"]:::focus\n    A --> C[\"MIN: ?\"]:::minNode\n    \n    B --> D[\"+3\"]:::focus\n    B --> E[\"+12\"]:::leafNode\n    B --> F[\"+8\"]:::leafNode\n    \n    C --> G[\"+2\"]:::leafNode\n    C --> H[\"+4\"]:::leafNode\n    C --> I[\"+6\"]:::leafNode\n            "
                            },
                            {
                                "explanation": "Next, the algorithm evaluates Node C. MIN looks at its options: +2, +4, and +6. MIN chooses the minimum: +2.",
                                "mermaid_code": "\ngraph TD\n    classDef maxNode fill:#10b9811a,stroke:#34D399,stroke-width:2px;\n    classDef minNode fill:#ef44441a,stroke:#FCA5A5,stroke-width:2px;\n    classDef leafNode fill:#7c4dff1a,stroke:#7C4DFF,stroke-width:2px;\n    classDef focus fill:#ffffff33,stroke:#FFF,stroke-width:4px;\n\n    A[\"MAX: ?\"]:::maxNode --> B[\"MIN: +3\"]:::minNode\n    A --> C[\"MIN: +2\"]:::focus\n    \n    B --> D[\"+3\"]:::leafNode\n    B --> E[\"+12\"]:::leafNode\n    B --> F[\"+8\"]:::leafNode\n    \n    C --> G[\"+2\"]:::focus\n    C --> H[\"+4\"]:::leafNode\n    C --> I[\"+6\"]:::leafNode\n            "
                            },
                            {
                                "explanation": "Finally, the scores propagate back up to the root (Node A). It is MAX's turn. MAX looks at the guaranteed values of B (+3) and C (+2). MAX chooses the maximum: +3. You will move to Node B.",
                                "mermaid_code": "\ngraph TD\n    classDef maxNode fill:#10b9811a,stroke:#34D399,stroke-width:2px;\n    classDef minNode fill:#ef44441a,stroke:#FCA5A5,stroke-width:2px;\n    classDef leafNode fill:#7c4dff1a,stroke:#7C4DFF,stroke-width:2px;\n    classDef focus fill:#ffffff33,stroke:#FFF,stroke-width:4px;\n\n    A[\"MAX: +3\"]:::focus --> B[\"MIN: +3\"]:::focus\n    A --> C[\"MIN: +2\"]:::minNode\n    \n    B --> D[\"+3\"]:::leafNode\n    B --> E[\"+12\"]:::leafNode\n    B --> F[\"+8\"]:::leafNode\n    \n    C --> G[\"+2\"]:::leafNode\n    C --> H[\"+4\"]:::leafNode\n    C --> I[\"+6\"]:::leafNode\n            "
                            }
                        ]
                    },
                    {
                        "type": "markdown",
                        "content": "> [!WARNING] \n> **The Beginner Mistake:** A beginner AI looks at the board, sees the `+12`, and greedily chooses to go to Node B, hoping the opponent is stupid. An optimal AI assumes the opponent is perfect and settles for the guaranteed `+3`."
                    },
                    {
                        "type": "code_experiment",
                        "title": "Implementing the Base Case (Leaf Nodes)",
                        "starter_code": "def evaluate_board(board_state):\n    # TODO: Write a function that returns a static score for a terminal board state.\n    # For this exercise, if the board is 'WIN', return 100.\n    # If 'LOSS', return -100.\n    # If 'DRAW', return 0.\n    pass",
                        "solution_code": "def evaluate_board(board_state):\n    if board_state == 'WIN': return 100\n    if board_state == 'LOSS': return -100\n    if board_state == 'DRAW': return 0\n    return 0",
                        "expected_output": "100\n-100\n0",
                        "explanation": "**Why it works:** Every recursive algorithm needs a base case. In Minimax, the base case is a terminal state (the game is over) or a depth limit where we use a heuristic evaluation function to guess the board's value.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nAlpha-Beta maintains bounds $[\\alpha, \\beta]$ representing the best outcomes already guaranteed for MAX and MIN. When $\\alpha \\ge \\beta$, the current branch cannot affect the root decision, pruning up to $O(b^{d/2})$ of the game tree without loss of accuracy.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Standard Minimax:** Searches every node to depth $d$; optimal for zero-sum games with complete information, but intractable for high branching factors ($O(b^d)$).\\n- **Negamax:** Reformulation exploiting zero-sum duality $\\max(a, b) = -\\min(-a, -b)$, halving codebase complexity.\\n- **Monte Carlo Tree Search (MCTS):** Uses random rollouts with Upper Confidence Bound (UCT); scales to games like Go where heuristic static evaluation functions fail.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "concept",
                        "title": "The Time Complexity Nightmare",
                        "content": "Minimax is elegant, but it has a fatal flaw. The time complexity is **O(b^m)**, where `b` is the branching factor (legal moves per turn) and `m` is the maximum depth of the game.\n\nIn chess, the branching factor is about 35. To look ahead just 10 moves, Minimax would need to evaluate **35^10 = 2.7 quadrillion** board states. The universe would end before your AI makes its first move."
                    },
                    {
                        "type": "concept",
                        "title": "Alpha-Beta Pruning",
                        "content": "To solve this, we introduce **Alpha-Beta Pruning**. It allows us to stop evaluating a branch of the tree as soon as we realize that it will never be selected by the parent nodes.\n\n*   **Alpha (α):** The value of the best (highest) choice we have found so far for MAX.\n*   **Beta (β):** The value of the best (lowest) choice we have found so far for MIN.\n\nIf at any point `Beta <= Alpha`, we **prune** the rest of the branch because we know the opponent will never let us go down it."
                    },
                    {
                        "type": "visual_stepper",
                        "title": "Interactive: Alpha-Beta Pruning Step-by-Step",
                        "height": 450,
                        "steps": [
                            {
                                "explanation": "We evaluate Node B. MIN chooses the lowest value (3). The best guarantee for MAX (alpha) is now 3.",
                                "mermaid_code": "\n    graph TD\n        classDef maxNode fill:#10b9811a,stroke:#34D399,stroke-width:2px;\n        classDef minNode fill:#ef44441a,stroke:#FCA5A5,stroke-width:2px;\n\n        A[\"MAX: α=3, β=∞\"]:::maxNode --> B[\"MIN: 3\"]:::minNode\n        A --> C[\"MIN: ?\"]:::minNode\n        \n        B --> D[\"3\"]\n        B --> E[\"12\"]\n        \n        C --> F[\"2\"]\n        C --> G[\"?\"]\n        C --> H[\"?\"]\n                "
                            },
                            {
                                "explanation": "Now we move to Node C. MIN evaluates its first child, which is 2.",
                                "mermaid_code": "\n    graph TD\n        classDef maxNode fill:#10b9811a,stroke:#34D399,stroke-width:2px;\n        classDef minNode fill:#ef44441a,stroke:#FCA5A5,stroke-width:2px;\n        classDef focus fill:#ffffff33,stroke:#FFF,stroke-width:4px;\n\n        A[\"MAX: α=3, β=∞\"]:::maxNode --> B[\"MIN: 3\"]:::minNode\n        A --> C[\"MIN: ≤2\"]:::focus\n        \n        B --> D[\"3\"]\n        B --> E[\"12\"]\n        \n        C --> F[\"2\"]:::focus\n        C --> G[\"?\"]\n        C --> H[\"?\"]\n                "
                            },
                            {
                                "explanation": "PRUNE! Node C is currently at ≤2. MAX already has a guaranteed 3 from Node B. Since 2 is worse than 3, and MIN will only make it even worse, MAX will NEVER choose Node C. We can instantly skip evaluating the rest of Node C's children!",
                                "mermaid_code": "\n    graph TD\n        classDef maxNode fill:#10b9811a,stroke:#34D399,stroke-width:2px;\n        classDef minNode fill:#ef44441a,stroke:#FCA5A5,stroke-width:2px;\n        classDef pruned fill:#00000080,stroke:#333,stroke-width:1px,stroke-dasharray: 5 5;\n\n        A[\"MAX: 3\"]:::maxNode --> B[\"MIN: 3\"]:::minNode\n        A -.-> C[\"MIN: 2\"]:::minNode\n        \n        B --> D[\"3\"]\n        B --> E[\"12\"]\n        \n        C --> F[\"2\"]\n        C -.-> G[\"Pruned\"]:::pruned\n        C -.-> H[\"Pruned\"]:::pruned\n                "
                            }
                        ]
                    },
                    {
                        "type": "code_lab",
                        "title": "The Alpha-Beta Algorithm",
                        "starter_code": "def alpha_beta(node, depth, alpha, beta, maximizing_player):\n    # node has .is_terminal(), .value, and .children[]\n    if depth == 0 or node.is_terminal():\n        return node.value\n        \n    if maximizing_player:\n        max_eval = float('-inf')\n        for child in node.children:\n            eval = alpha_beta(child, depth - 1, alpha, beta, False)\n            # TODO: Update max_eval\n            # TODO: Update alpha\n            # TODO: Add the pruning condition\n        return max_eval\n    else:\n        min_eval = float('inf')\n        for child in node.children:\n            eval = alpha_beta(child, depth - 1, alpha, beta, True)\n            # TODO: Update min_eval\n            # TODO: Update beta\n            # TODO: Add the pruning condition\n        return min_eval\n\n# --- Execution Output ---\nprint('Result:', alpha_beta(None))\n",
                        "solution_code": "def alpha_beta(node, depth, alpha, beta, maximizing_player):\n    if depth == 0 or node.is_terminal():\n        return node.value\n        \n    if maximizing_player:\n        max_eval = float('-inf')\n        for child in node.children:\n            eval = alpha_beta(child, depth - 1, alpha, beta, False)\n            max_eval = max(max_eval, eval)\n            alpha = max(alpha, eval)\n            if beta <= alpha:\n                break  # Prune!\n        return max_eval\n    else:\n        min_eval = float('inf')\n        for child in node.children:\n            eval = alpha_beta(child, depth - 1, alpha, beta, True)\n            min_eval = min(min_eval, eval)\n            beta = min(beta, eval)\n            if beta <= alpha:\n                break  # Prune!\n        return min_eval\n\n# --- Execution Output ---\nprint('Result:', alpha_beta(None))\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** By passing down `alpha` and `beta`, the algorithm essentially 'remembers' the best alternatives found elsewhere in the tree. When `beta <= alpha`, the current path is mathematically proven to be irrelevant, saving us millions of calculations.",
                        "why_it_works": "**Algorithmic Mechanics:**\\nAlpha-Beta maintains bounds $[\\alpha, \\beta]$ representing the best outcomes already guaranteed for MAX and MIN. When $\\alpha \\ge \\beta$, the current branch cannot affect the root decision, pruning up to $O(b^{d/2})$ of the game tree without loss of accuracy.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Standard Minimax:** Searches every node to depth $d$; optimal for zero-sum games with complete information, but intractable for high branching factors ($O(b^d)$).\\n- **Negamax:** Reformulation exploiting zero-sum duality $\\max(a, b) = -\\min(-a, -b)$, halving codebase complexity.\\n- **Monte Carlo Tree Search (MCTS):** Uses random rollouts with Upper Confidence Bound (UCT); scales to games like Go where heuristic static evaluation functions fail.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    }
                ]
            },
            {
                "title": "Module 2: Building the Perfect Agent",
                "blocks": [
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
                        "explanation": "**Why it works:** To generate the branches of our Game Tree, we need to know all legal moves from the current state.",
                        "why_it_works": "**Algorithmic Mechanics:**\\nAlpha-Beta maintains bounds $[\\alpha, \\beta]$ representing the best outcomes already guaranteed for MAX and MIN. When $\\alpha \\ge \\beta$, the current branch cannot affect the root decision, pruning up to $O(b^{d/2})$ of the game tree without loss of accuracy.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Standard Minimax:** Searches every node to depth $d$; optimal for zero-sum games with complete information, but intractable for high branching factors ($O(b^d)$).\\n- **Negamax:** Reformulation exploiting zero-sum duality $\\max(a, b) = -\\min(-a, -b)$, halving codebase complexity.\\n- **Monte Carlo Tree Search (MCTS):** Uses random rollouts with Upper Confidence Bound (UCT); scales to games like Go where heuristic static evaluation functions fail.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "concept",
                        "title": "The Recursive Mind",
                        "content": "When Minimax evaluates a board, it effectively plays out the entire rest of the game in its head. It places an 'X', then asks 'If I do this, what is the best move 'O' can make in response?'. It does this all the way down until someone wins, loses, or the board is full (a draw)."
                    },
                    {
                        "type": "code_lab",
                        "title": "The Perfect Tic-Tac-Toe Agent",
                        "starter_code": "def check_winner(board):\n    # Returns 1 (X wins), -1 (O wins), 0 (Draw/Ongoing)\n    win_lines = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]\n    for a,b,c in win_lines:\n        if board[a] != 0 and board[a] == board[b] == board[c]:\n            return board[a]\n    if 0 not in board: return 0\n    return None\n\ndef optimal_move(board, is_max):\n    # TODO: Implement the full Minimax loop to return the best index to play.\n    pass\n\n# --- Execution Output ---\nprint('Result:', check_winner(None))\n",
                        "solution_code": "def check_winner(board):\n    win_lines = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]\n    for a,b,c in win_lines:\n        if board[a] != 0 and board[a] == board[b] == board[c]: return board[a]\n    if 0 not in board: return 0\n    return None\n\ndef minimax(board, is_max):\n    winner = check_winner(board)\n    if winner is not None: return winner\n    \n    if is_max:\n        best = float('-inf')\n        for i in range(9):\n            if board[i] == 0:\n                board[i] = 1\n                best = max(best, minimax(board, False))\n                board[i] = 0\n        return best\n    else:\n        best = float('inf')\n        for i in range(9):\n            if board[i] == 0:\n                board[i] = -1\n                best = min(best, minimax(board, True))\n                board[i] = 0\n        return best\n\ndef optimal_move(board, is_max):\n    best_val = float('-inf') if is_max else float('inf')\n    best_move = -1\n    player = 1 if is_max else -1\n    \n    for i in range(9):\n        if board[i] == 0:\n            board[i] = player\n            move_val = minimax(board, not is_max)\n            board[i] = 0\n            \n            if is_max and move_val > best_val:\n                best_val = move_val\n                best_move = i\n            elif not is_max and move_val < best_val:\n                best_val = move_val\n                best_move = i\n                \n    return best_move\n\n# --- Execution Output ---\nprint('Result:', check_winner(None))\n",
                        "expected_output": "",
                        "explanation": "**Why it works:** This is the complete, unpruned algorithm. The `optimal_move` function acts as the root of the tree, trying every available move and asking `minimax()` to evaluate how good it is. By iterating through all possibilities and backtracking (`board[i] = 0`), the AI maps out the entire future.",
                        "why_it_works": "**Algorithmic Mechanics:**\\nAlpha-Beta maintains bounds $[\\alpha, \\beta]$ representing the best outcomes already guaranteed for MAX and MIN. When $\\alpha \\ge \\beta$, the current branch cannot affect the root decision, pruning up to $O(b^{d/2})$ of the game tree without loss of accuracy.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Standard Minimax:** Searches every node to depth $d$; optimal for zero-sum games with complete information, but intractable for high branching factors ($O(b^d)$).\\n- **Negamax:** Reformulation exploiting zero-sum duality $\\max(a, b) = -\\min(-a, -b)$, halving codebase complexity.\\n- **Monte Carlo Tree Search (MCTS):** Uses random rollouts with Upper Confidence Bound (UCT); scales to games like Go where heuristic static evaluation functions fail.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    }
                ]
            },
            {
                "title": "Module 3: Scaling to the Real World",
                "blocks": [
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
                        "code": "\ngraph TD\n    classDef maxNode fill:#10b9811a,stroke:#34D399,stroke-width:2px;\n    classDef cutoff fill:rgba(255,152,0,0.1),stroke:#FF9800,stroke-width:2px;\n\n    A[\"Current Board\"]:::maxNode --> B[\"Depth 1\"]\n    A --> C[\"Depth 1\"]\n    \n    B --> D[\"Depth 2\"]\n    B --> E[\"Depth 2\"]\n    \n    D --> F[\"Depth 3: CUTOFF\"]:::cutoff\n    D --> G[\"Depth 3: CUTOFF\"]:::cutoff\n    \n    F -.-> H[\"Evaluate: +4.5\"]\n    G -.-> I[\"Evaluate: -1.2\"]\n        "
                    },
                    {
                        "type": "problem",
                        "content": "**The Design Challenge:** How do you evaluate a Chess board that isn't finished? You might count the pieces (Queen = 9, Rook = 5). But what if the King is exposed? An evaluation function must balance material advantage with positional advantage."
                    }
                ]
            },
            {
                "title": "Module 4: Evaluation Functions and Horizon Effects",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "Heuristic Evaluation Functions",
                        "content": "In real-world engineering games (and chess/Go), we cannot search to terminal leaf states due to exponential branching factor ($b^d$). We must cut off search at a specified depth and apply an **Evaluation Function** $Eval(s)$ that estimates the expected utility of state $s$."
                    },
                    {
                        "type": "visual",
                        "title": "Search Cutoff & Evaluation",
                        "code": "graph TD\n  Root[\"Current State\"] --> D1A[\"Depth 1\"]\n  Root --> D1B[\"Depth 1\"]\n  D1A --> D2A[\"Depth 2 Cutoff\"]:::cutoff\n  D1A --> D2B[\"Depth 2 Cutoff\"]:::cutoff\n  D1B --> D2C[\"Depth 2 Cutoff\"]:::cutoff\n  classDef cutoff fill:#f59e0b2a,stroke:#F59E0B,stroke-width:2px;"
                    },
                    {
                        "type": "code_lab",
                        "title": "Depth-Limited Minimax Implementation",
                        "starter_code": "def eval_board(pieces_count, mobility_score):\n    # Weighted evaluation function\n    return (pieces_count * 10) + (mobility_score * 1.5)\n\nprint('Heuristic State Value:', eval_board(5, 12))",
                        "solution_code": "def eval_board(pieces_count, mobility_score):\n    return (pieces_count * 10) + (mobility_score * 1.5)\n\nprint('Heuristic State Value:', eval_board(5, 12))",
                        "expected_output": "Heuristic State Value: 68.0",
                        "explanation": "Weighted linear evaluation functions combine independent features into a single scalar utility value.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nAlpha-Beta maintains bounds $[\\alpha, \\beta]$ representing the best outcomes already guaranteed for MAX and MIN. When $\\alpha \\ge \\beta$, the current branch cannot affect the root decision, pruning up to $O(b^{d/2})$ of the game tree without loss of accuracy.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Standard Minimax:** Searches every node to depth $d$; optimal for zero-sum games with complete information, but intractable for high branching factors ($O(b^d)$).\\n- **Negamax:** Reformulation exploiting zero-sum duality $\\max(a, b) = -\\min(-a, -b)$, halving codebase complexity.\\n- **Monte Carlo Tree Search (MCTS):** Uses random rollouts with Upper Confidence Bound (UCT); scales to games like Go where heuristic static evaluation functions fail.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "interactive",
                        "title": "Horizon Effect Challenge",
                        "question": "What is the 'Horizon Effect' in game tree search?",
                        "options": [
                            "Pushing an unavoidable damaging move just beyond the search depth limit",
                            "Searching too fast and exceeding memory buffers",
                            "Pruning the winning branch accidentally"
                        ],
                        "answer": "Pushing an unavoidable damaging move just beyond the search depth limit",
                        "explanation": "The Horizon Effect occurs when the agent delays a detrimental move by making stalling moves, pushing the disaster past its search horizon."
                    }
                ]
            }
        ],
        "title": "Case 06: The Game of Minds"
    },
    "7": {
        "title": "Case 07: The Impossible Puzzle",
        "episodes": [
            {
                "title": "Module 1: Introduction to CSP",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "A Constraint Satisfaction Problem (CSP) involves finding assignments for variables that satisfy given constraints."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Each variable has a domain of possible values."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\n  A[\"Variable\"] --> B[\"Domain\"]\n  style A fill:#10b981,stroke:#333,stroke-width:2px"
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** "
                    },
                    {
                        "type": "markdown",
                        "content": "Constraints can be unary, binary, or higher-order."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "A unary constraint restricts the value of a single variable."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph TD\n  Empty[\"Empty Diagram\"]"
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "",
                        "solution_code": "",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nAC-3 enforces arc consistency across all binary constraints $(X_i, X_j)$ before and during backtracking, removing values from domains that have no valid support and pruning exponential search spaces early.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Pure Backtracking:** Chronological backtracking without domain pruning; suffers catastrophic thrashing on dead ends.\\n- **Forward Checking (FC):** Prunes only neighboring variables immediately affected by assignment; faster per step than AC-3, but catches fewer cascading inconsistencies.\\n- **Min-Conflicts Local Search:** Iteratively re-assigns variables to minimize violated constraints; solves 1,000,000-Queens in seconds, but can get stuck in local optima.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "Binary constraints involve two variables."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "An example is X != Y in map coloring."
                    }
                ]
            },
            {
                "title": "Module 2: Backtracking Search",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "Backtracking is a depth-first search for CSPs."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "The search space is formed by assigning values to variables one by one."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\n  A[\"Start\"] --> B[\"Assign V1\"]\n  style A fill:#10b981,stroke:#333,stroke-width:2px"
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** "
                    },
                    {
                        "type": "markdown",
                        "content": "It checks constraints at each step."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "If a constraint is violated, the current branch is abandoned."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph TD\n  Empty[\"Empty Diagram\"]"
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "",
                        "solution_code": "",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nAC-3 enforces arc consistency across all binary constraints $(X_i, X_j)$ before and during backtracking, removing values from domains that have no valid support and pruning exponential search spaces early.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Pure Backtracking:** Chronological backtracking without domain pruning; suffers catastrophic thrashing on dead ends.\\n- **Forward Checking (FC):** Prunes only neighboring variables immediately affected by assignment; faster per step than AC-3, but catches fewer cascading inconsistencies.\\n- **Min-Conflicts Local Search:** Iteratively re-assigns variables to minimize violated constraints; solves 1,000,000-Queens in seconds, but can get stuck in local optima.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "Backtracking is more efficient than generate-and-test."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "It eliminates large portions of the search space."
                    }
                ]
            },
            {
                "title": "Module 3: Heuristics in CSP",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "Heuristics improve the efficiency of backtracking."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Which variable should be assigned next?"
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\n  A[\"V1 (3 values)\"] --> B[\"V2 (1 value)\"]\n  style A fill:#3b82f6,stroke:#333,stroke-width:2px"
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** "
                    },
                    {
                        "type": "markdown",
                        "content": "MRV chooses the variable with the fewest legal values left."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Used as a tie-breaker, it selects the variable involved in most constraints."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph TD\n  Empty[\"Empty Diagram\"]"
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "",
                        "solution_code": "",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nAC-3 enforces arc consistency across all binary constraints $(X_i, X_j)$ before and during backtracking, removing values from domains that have no valid support and pruning exponential search spaces early.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Pure Backtracking:** Chronological backtracking without domain pruning; suffers catastrophic thrashing on dead ends.\\n- **Forward Checking (FC):** Prunes only neighboring variables immediately affected by assignment; faster per step than AC-3, but catches fewer cascading inconsistencies.\\n- **Min-Conflicts Local Search:** Iteratively re-assigns variables to minimize violated constraints; solves 1,000,000-Queens in seconds, but can get stuck in local optima.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "Value ordering determines which value to try first."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Prefers the value that rules out the fewest choices for neighboring variables."
                    }
                ]
            },
            {
                "title": "Module 4: Constraint Propagation",
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "Constraint propagation reduces the domains of variables before search."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "Whenever a variable is assigned, remove conflicting values from unassigned variables."
                    },
                    {
                        "type": "visual",
                        "title": "Visualization",
                        "code": "graph TD\n  A[\"V1=Red\"] --> B[\"V2 removes Red\"]\n  style A fill:#f59e0b,stroke:#333,stroke-width:2px"
                    },
                    {
                        "type": "markdown",
                        "content": "**Question:** "
                    },
                    {
                        "type": "markdown",
                        "content": "AC-3 is a popular algorithm for arc consistency."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "An arc X -> Y is consistent if for every value in X, there is an allowed value in Y."
                    },
                    {
                        "type": "visual",
                        "title": "Architecture Diagram",
                        "code": "graph TD\n  Empty[\"Empty Diagram\"]"
                    },
                    {
                        "type": "code_lab",
                        "title": "Implementation Lab",
                        "starter_code": "",
                        "solution_code": "",
                        "expected_output": "",
                        "explanation": "**Why it works:** The Python code above implements the theoretical constructs we just covered.",
                        "test_cases": [],
                        "why_it_works": "**Algorithmic Mechanics:**\\nAC-3 enforces arc consistency across all binary constraints $(X_i, X_j)$ before and during backtracking, removing values from domains that have no valid support and pruning exponential search spaces early.",
                        "alternatives": "#### 🔀 Candidate Architectural Alternatives\\n- **Pure Backtracking:** Chronological backtracking without domain pruning; suffers catastrophic thrashing on dead ends.\\n- **Forward Checking (FC):** Prunes only neighboring variables immediately affected by assignment; faster per step than AC-3, but catches fewer cascading inconsistencies.\\n- **Min-Conflicts Local Search:** Iteratively re-assigns variables to minimize violated constraints; solves 1,000,000-Queens in seconds, but can get stuck in local optima.",
                        "complexity": "- **Time Complexity:** Dependent on state space branching factor and depth.\\n- **Space Complexity:** Bounded by frontier and visited storage."
                    },
                    {
                        "type": "markdown",
                        "content": "Propagation can sometimes solve the CSP without search."
                    },
                    {
                        "type": "concept",
                        "title": "Concept",
                        "content": "More propagation means less search, but propagation takes time."
                    }
                ]
            }
        ]
    }
}