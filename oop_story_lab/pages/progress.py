import streamlit as st
from ui import configure_page, sidebar
from story_data import STORIES

configure_page()
sidebar(active="progress")

st.markdown('<div class="workspace-eyebrow">ANALYTICS</div><h1>📈 Progress & Metrics</h1>', unsafe_allow_html=True)

completed = st.session_state.get("completed", set())
xp = st.session_state.get("xp", 0)
total_cases = len(STORIES)
completed_count = len(completed)

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total XP", f"{xp} XP")
with col2:
    st.metric("Cases Solved", f"{completed_count} / {total_cases}")
with col3:
    st.metric("Completion", f"{int((completed_count/total_cases)*100) if total_cases > 0 else 0}%")

st.markdown("---")
st.markdown("### Skill Distribution")
st.write("As you complete cases, your skill vectors will grow across different architectural domains.")

st.markdown('''
- **Memory Management**: ▆▆▆▆▆▆ 60%
- **System Design**: ▆▆▆▆ 40%
- **Modern C++**: ▆▆▆▆▆▆▆▆ 80%
- **Debugging**: ▆▆▆ 30%
''')

