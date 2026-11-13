import streamlit as st
from ui import configure_page, sidebar
import cpp_runner

configure_page()
sidebar(active="practice")

st.title("⌘ C++ Sandbox")
st.write("Write, compile, and run C++ code right in your browser.")

code = st.text_area("C++ Code", height=300, value="#include <iostream>\n\nint main() {\n    std::cout << \"Hello, OOP Story Lab!\" << std::endl;\n    return 0;\n}")
if st.button("Compile & Run"):
    with st.spinner("Running..."):
        success, out, err = cpp_runner.run_cpp(code)
        if success:
            st.success("Output:")
            st.code(out, language="text")
        else:
            st.error("Error:")
            st.code(err, language="text")
