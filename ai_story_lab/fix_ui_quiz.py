with open("ui.py", "r") as f:
    content = f.read()

# Replace the condition to handle both integer indices and exact string matches
old_logic = '''                    idx = block["options"].index(chosen)
                    if idx == block.get("answer", -1):'''
new_logic = '''                    idx = block["options"].index(chosen)
                    ans = block.get("answer", -1)
                    if idx == ans or chosen == ans:'''

content = content.replace(old_logic, new_logic)

with open("ui.py", "w") as f:
    f.write(content)
