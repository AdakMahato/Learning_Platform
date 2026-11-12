import json
from level_content import LEVEL_CONTENT

mod1 = [
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
        "code": """
graph TD
    classDef t fill:#ef44441a,stroke:#FCA5A5,stroke-width:2px;
    classDef a fill:#10b9811a,stroke:#34D399,stroke-width:2px;
    
    subgraph Traditional Programming
        D1["Data"]:::t --> P1["Computer"]:::t
        R1["Rules (Code)"]:::t --> P1
        P1 --> A1["Answers"]:::t
    end
    
    subgraph Machine Learning
        D2["Data"]:::a --> P2["Computer"]:::a
        A2["Answers (Labels)"]:::a --> P2
        P2 --> R2["Rules (Model)"]:::a
    end
        """
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
        "answer": "No, it is Traditional Programming"
    }
]

mod2 = [
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
        "code": """
graph TD
    classDef h fill:#3b82f61a,stroke:#93C5FD,stroke-width:2px;
    classDef r fill:#10b9811a,stroke:#34D399,stroke-width:2px;
    
    A[" "] -->|Humanly| H[" "]
    A -->|Rationally| R[" "]
    
    H -->|Think| TH["Cognitive Modeling"]:::h
    H -->|Act| AH["Turing Test"]:::h
    
    R -->|Think| TR["Laws of Thought"]:::r
    R -->|Act| AR["Rational Agents"]:::r
        """
    },
    {
        "type": "interactive",
        "question": "Which approach to AI attempts to perfectly simulate the psychological and neurological processes of the human brain?",
        "options": [
            "The Rational Agent approach",
            "The Turing Test",
            "Cognitive Modeling"
        ],
        "answer": "Cognitive Modeling"
    }
]

mod3 = [
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
        "type": "interactive",
        "question": "Does passing the Turing Test guarantee that a machine is actually 'conscious'?",
        "options": [
            "Yes, it proves consciousness.",
            "No, it only proves the ability to simulate human behavior."
        ],
        "answer": "No, it only proves the ability to simulate human behavior."
    }
]

mod4 = [
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
        "type": "visual",
        "title": "The AI Umbrella",
        "code": """
graph TD
    classDef main fill:#7c4dff1a,stroke:#7C4DFF,stroke-width:2px;
    classDef sub fill:#3b82f61a,stroke:#93C5FD,stroke-width:2px;
    classDef deep fill:#10b9811a,stroke:#34D399,stroke-width:2px;
    
    AI["Artificial Intelligence"]:::main --> GOFAI["Symbolic AI (Expert Systems, Search)"]:::sub
    AI --> ML["Machine Learning"]:::sub
    
    ML --> SL["Supervised Learning"]:::sub
    ML --> UL["Unsupervised Learning"]:::sub
    ML --> RL["Reinforcement Learning"]:::sub
    
    SL --> DL["Deep Learning (Neural Networks)"]:::deep
    UL --> DL
    RL --> DL
        """
    },
    {
        "type": "interactive",
        "question": "Which branch of AI was dominant in the 1970s and relied on hard-coded logical rules?",
        "options": [
            "Deep Learning",
            "Symbolic AI",
            "Reinforcement Learning"
        ],
        "answer": "Symbolic AI"
    }
]

mod5 = [
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

LEVEL_CONTENT['0'] = {
    "title": "Case 00: The Machine That Couldn't Think",
    "episodes": [
        {
            "title": "Module 1: The Paradigm Shift",
            "blocks": mod1
        },
        {
            "title": "Module 2: Defining Intelligence",
            "blocks": mod2
        },
        {
            "title": "Module 3: The Turing Test",
            "blocks": mod3
        },
        {
            "title": "Module 4: The AI Umbrella",
            "blocks": mod4
        },
        {
            "title": "Module 5: Real-World Architecture",
            "blocks": mod5
        }
    ]
}

with open('level_content.py', 'w', encoding='utf-8') as f:
    f.write("LEVEL_CONTENT = \\\n")
    json.dump(LEVEL_CONTENT, f, indent=4, ensure_ascii=False)

print("Injected ultra extreme theoretical depth into Case 00!")
