import streamlit as st
from ui import sidebar, configure_page

configure_page("Concepts")
sidebar(active="concepts")

st.title("Concept Library")
st.markdown("<p style='color: #AAB3CC;'>Your centralized repository of database concepts.</p>", unsafe_allow_html=True)
st.info("Concept Library automatically links to your Field Notebook. See Field Notebook for discovered concepts.")
if st.button("Go to Field Notebook"):
    st.switch_page("pages/12_field_notebook.py")
