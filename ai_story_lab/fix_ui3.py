with open("ui.py", "r") as f:
    content = f.read()

content = content.replace('elif btype == "concept":', 'elif btype in ("concept", "objective"):')

with open("ui.py", "w") as f:
    f.write(content)
