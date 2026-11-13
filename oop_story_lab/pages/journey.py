import streamlit as st
from ui import configure_page, sidebar
from story_data import STORIES

configure_page()
sidebar(active="map")

st.markdown('<div class="workspace-eyebrow">CURRICULUM OVERVIEW</div><h1>▣ Learning Journey</h1>', unsafe_allow_html=True)
st.markdown("### The Path to Nexus Core Architecture")
st.write("Your journey is broken down into thematic arcs. Complete each arc to master the underlying engineering principles of modern C++.")

arcs = {
    "Bootcamp: Programming Fundamentals": (0, 5),
    "Arc 1: The Foundations of State": (5, 10),
    "Arc 2: Polymorphism & Contracts": (10, 15),
    "Arc 3: Resource Management": (15, 20),
    "Arc 4: Systems Architecture": (20, 25),
    "Arc 5: The Master Engineer": (25, 29)
}

completed = st.session_state.get("completed", set())

for arc_name, (start, end) in arcs.items():
    st.markdown(f"#### {arc_name}")
    
    cols = st.columns(end - start)
    for i, case_idx in enumerate(range(start, end)):
        if case_idx < len(STORIES):
            story = STORIES[case_idx]
            is_completed = story["id"] in completed
            
            with cols[i]:
                border_color = "#7C4DFF" if is_completed else "#334155"
                bg_color = "rgba(124,77,255,0.1)" if is_completed else "transparent"
                icon = "✓" if is_completed else "🔒"
                
                st.markdown(f'''
                <div style="border: 2px solid {border_color}; background: {bg_color}; border-radius: 8px; padding: 12px; margin-bottom: 16px; height: 120px;">
                    <div style="font-size: 0.75rem; color: #94A3B8; margin-bottom: 4px;">CASE {story["id"]:02d}</div>
                    <div style="font-weight: 700; font-size: 0.9rem; margin-bottom: 8px; line-height: 1.2;">{story["title"]}</div>
                    <div style="color: {border_color}; font-weight: 800;">{icon}</div>
                </div>
                ''', unsafe_allow_html=True)
