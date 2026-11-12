import re

# Fix app.py
with open("app.py", "r") as f:
    content = f.read()

content = content.replace("OOP STORY LAB", "AI STORY LAB")
content = content.replace("OOP Story Lab", "AI Story Lab")
content = content.replace("C++ ENGINEERING SIMULATOR", "NEXUS INTELLIGENCE SIMULATOR")
content = content.replace("Learn C++ objects by\nbuilding architecture.", "Learn Artificial Intelligence by\nbuilding intelligent agents.")
content = content.replace("C++ Sandbox", "AI Python Sandbox")
content = content.replace("C++", "Python")

with open("app.py", "w") as f:
    f.write(content)

# Fix ui.py
with open("ui.py", "r") as f:
    content = f.read()

content = content.replace("OOP STORY LAB", "AI STORY LAB")
content = content.replace("OOP Story Lab", "AI Story Lab")
content = content.replace("C++ Sandbox", "AI Python Sandbox")
content = content.replace("C++", "Python")

with open("ui.py", "w") as f:
    f.write(content)

