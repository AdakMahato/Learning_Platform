with open("ui.py", "r") as f:
    content = f.read()

# Change default height from 400 to 200 for simple visual blocks
content = content.replace('st_mermaid(block.get("code", ""), height=block.get("height", 400))',
                          'st_mermaid(block.get("code", ""), height=block.get("height", 150))')

with open("ui.py", "w") as f:
    f.write(content)

print("Fixed UI diagram heights!")
