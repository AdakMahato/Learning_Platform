import re

with open("ui.py", "r") as f:
    content = f.read()

content = content.replace("language='c_cpp'", "language='python'")
content = content.replace('language="cpp"', 'language="python"')
content = content.replace("C++ Code", "Python Code")
content = content.replace("cpp_runner", "py_runner")
content = content.replace("run_cpp", "run_py")

with open("ui.py", "w") as f:
    f.write(content)

