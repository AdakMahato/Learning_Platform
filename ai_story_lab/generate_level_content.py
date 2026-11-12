import json

LEVEL_CONTENT = {
    "0": {
        "episodes": [
            {
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "You arrive at the NEXUS Intelligence facility. It is 0600 hours. The halls are eerily quiet, save for the hum of the cooling towers keeping the massive server farms from melting down. You've just been hired as a Junior AI Engineer. Your first task isn't to write code. It's to figure out what intelligence actually means."
                    },
                    {
                        "type": "objective",
                        "title": "Module Objective",
                        "content": "Understand the core definition of Artificial Intelligence and distinguish it from traditional programming."
                    },
                    {
                        "type": "problem",
                        "content": "**The Think-First Challenge:** Suppose you write a program to play Tic-Tac-Toe using `if-else` statements covering every possible board state. Is that program 'intelligent'?"
                    },
                    {
                        "type": "concept",
                        "title": "What is Intelligence?",
                        "content": "Before we can build Artificial Intelligence, we must define intelligence itself. In AI literature, intelligence is often defined by **rationality**—the ability to choose an action that maximizes the expected performance measure, given the available information.\n\nAI is traditionally divided into four approaches:\n1. Thinking humanly (Cognitive modeling)\n2. Acting humanly (The Turing Test)\n3. Thinking rationally (Laws of thought)\n4. Acting rationally (Rational agents)"
                    },
                    {
                        "type": "visual",
                        "title": "Traditional Programming vs AI",
                        "code": """
graph LR
    subgraph Traditional Programming
        D1[Data] --> P1[Program]
        R1[Rules] --> P1
        P1 --> O1[Answers]
    end

    subgraph Machine Learning / AI
        D2[Data] --> P2[AI Algorithm]
        O2[Answers] --> P2
        P2 --> R2[Rules / Model]
    end
                        """
                    }
                ]
            },
            {
                "blocks": [
                    {
                        "type": "markdown",
                        "content": "Your manager, Dr. Aris, pulls up a simulation on the screen. 'A traditional program expects the world to be perfect,' she says. 'It follows instructions blindly. An AI expects the world to be messy. It adapts.'"
                    },
                    {
                        "type": "concept",
                        "title": "Why Traditional Programming Fails",
                        "content": "In traditional programming, you must explicitly code every rule and edge case. This works for a payroll system. It completely fails for a self-driving car, because you cannot write an `if-else` statement for every possible configuration of pedestrians, weather, and traffic."
                    },
                    {
                        "type": "code_experiment",
                        "title": "The Limits of Hardcoding",
                        "starter_code": "def identify_object(pixels):\n    # TODO: Write rules to identify a 'cat' using just pixel RGB values.\n    if pixels[0][0] == (255, 255, 255):\n        return 'Empty'\n    return 'Cat'\n\nprint(identify_object([[(0,0,0)]]))",
                        "solution_code": "def identify_object(pixels):\n    # It is virtually impossible to hardcode rules for vision.\n    # AI shifts this burden to statistical learning.\n    pass",
                        "expected_output": "Cat",
                        "explanation": "**Why it works (or doesn't):** You quickly realize it is mathematically impossible to hardcode a rule for every pixel variation of a cat. This realization is the birthplace of modern AI—we must build systems that infer rules from data, rather than systems where we hardcode the rules."
                    }
                ]
            }
        ]
    }
}

with open("level_content.py", "w", encoding="utf-8") as f:
    f.write("LEVEL_CONTENT = \\\n")
    json.dump(LEVEL_CONTENT, f, indent=4, ensure_ascii=False)

