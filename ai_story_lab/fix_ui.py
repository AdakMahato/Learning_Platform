with open("ui.py", "r") as f:
    content = f.read()

content = content.replace('elif btype == "story":', 'elif btype in ("story", "markdown", "narrative", "text"):')

with open("ui.py", "w") as f:
    f.write(content)
