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
        "content": "Understand the fundamental difference between Traditional Programming and Artificial Intelligence, and explore the concept of the Turing Test."
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
        "content": "> [!NOTE] \n> Modern AI almost exclusively focuses on **Acting Rationally**. We don't care if the AI 'thinks' exactly like a human brain does, as long as it makes the statistically optimal decisions to achieve its goal."
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
        "question": "Which approach to AI attempts to perfectly simulate the psychological processes of the human brain?",
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
        "content": "Let's explore the difference between a static rule-based system and a learning system in code."
    },
    {
        "type": "code_lab",
        "title": "Hardcoded Rules vs Simple Learning",
        "starter_code": "def traditional_spam_filter(email_text):\n    # TODO: Write a traditional rule-based filter that returns True if the email contains 'lottery' or 'free money'\n    pass\n\ndef machine_learning_spam_filter(email_text, spam_words_db):\n    # TODO: Write a filter that checks if the email contains any word in the dynamic spam_words_db\n    pass\n\nprint(\"Traditional:\", traditional_spam_filter(\"You won the lottery!\"))\nprint(\"ML:\", machine_learning_spam_filter(\"Buy this cheap watch!\", [\"cheap\", \"watch\"]))",
        "solution_code": "def traditional_spam_filter(email_text):\n    text = email_text.lower()\n    if 'lottery' in text or 'free money' in text:\n        return True\n    return False\n\ndef machine_learning_spam_filter(email_text, spam_words_db):\n    text = email_text.lower()\n    for word in spam_words_db:\n        if word in text:\n            return True\n    return False\n\nprint(\"Traditional:\", traditional_spam_filter(\"You won the lottery!\"))\nprint(\"ML:\", machine_learning_spam_filter(\"Buy this cheap watch!\", [\"cheap\", \"watch\"]))",
        "expected_output": "",
        "explanation": "**Why it works:** The traditional filter is brittle; if the spammer writes 'l0ttery', it fails. The ML filter is dynamic; the `spam_words_db` acts as the 'weights' or 'learned rules' that can be updated over time without changing the core code.",
        "test_cases": []
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
            "title": "Module 4: Rule-Based vs Learning",
            "blocks": mod4
        }
    ]
}

with open('level_content.py', 'w', encoding='utf-8') as f:
    f.write("LEVEL_CONTENT = \\\n")
    json.dump(LEVEL_CONTENT, f, indent=4, ensure_ascii=False)

print("Injected extreme depth into Case 00!")
