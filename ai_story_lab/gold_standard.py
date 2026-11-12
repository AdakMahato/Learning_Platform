import json

INSTRUCTIONS = """
You are an elite AI Curriculum Architect. You are rewriting the AI Story Lab cases.
Previously, you generated shallow content. The user rejected it.
You MUST write content with EXTREME DEPTH, matching the density of the provided example.

RULES:
1. Every Case MUST have at least 4 to 6 Modules (episodes).
2. Every Module MUST have at least 8 to 15 blocks.
3. You MUST use 'episodes' as the array key, NOT 'modules'.
4. Block types to mix heavily: `markdown`, `concept`, `interactive` (quizzes), `visual` (Mermaid graphs), `visual_stepper` (step-by-step algorithms), `code_lab` (Python).
5. Mermaid nodes MUST have double quotes (e.g., A["Node"]).
6. Mermaid colors MUST be standard Hex (e.g., #10b9811a), NEVER rgba().
7. Do NOT skip the Code Labs. At least one module per case MUST have a `code_lab`.
8. Output a Python dictionary. DO NOT output JSON strings.

If you generate less than 30 blocks total for a single Case, you have failed the assignment.
"""
with open("gold_standard_instructions.txt", "w") as f:
    f.write(INSTRUCTIONS)
