import streamlit as st
from ui import configure_page, sidebar

configure_page()
sidebar(active="notebook")

st.markdown('<div class="workspace-eyebrow">PERSONAL NOTES</div><h1>▣ Field Notebook</h1>', unsafe_allow_html=True)
st.write("Jot down architectural patterns, terminal outputs, or C++ snippets you want to remember.")

if "notebook_content" not in st.session_state:
    st.session_state.notebook_content = ""

content = st.text_area("Your Notes (Markdown supported)", value=st.session_state.notebook_content, height=400)

if st.button("Save Notes", type="primary"):
    st.session_state.notebook_content = content
    st.success("Notes saved securely to your session.")
    
if st.session_state.notebook_content:
    st.markdown("### Preview")
    st.markdown(st.session_state.notebook_content)
