with open("ui.py", "r") as f:
    content = f.read()

content = content.replace('elif btype in ("micro_challenge", "mastery_challenge"):', 'elif btype in ("micro_challenge", "mastery_challenge", "interactive"):')

with open("ui.py", "w") as f:
    f.write(content)
