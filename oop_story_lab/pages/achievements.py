import streamlit as st
from ui import configure_page, sidebar

configure_page()
sidebar(active="achievements")

st.markdown('<div class="workspace-eyebrow">REWARDS</div><h1>🏆 Achievements</h1>', unsafe_allow_html=True)

achievements = [
    {"name": "The Architect", "desc": "Completed all 24 cases.", "unlocked": False, "icon": "🏛️"},
    {"name": "Memory Master", "desc": "Wrote a custom Smart Pointer.", "unlocked": True, "icon": "🧠"},
    {"name": "Polymorph", "desc": "Used virtual functions in 5 cases.", "unlocked": False, "icon": "🐉"},
    {"name": "Rule of Zero", "desc": "Deleted a custom destructor.", "unlocked": True, "icon": "0️⃣"}
]

for a in achievements:
    color = "#F8F7FF" if a["unlocked"] else "#475569"
    icon_opacity = "1.0" if a["unlocked"] else "0.3"
    
    st.markdown(f'''
    <div style="display: flex; align-items: center; padding: 16px; background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.1); border-radius: 8px; margin-bottom: 12px;">
        <div style="font-size: 2rem; opacity: {icon_opacity}; margin-right: 16px;">{a["icon"]}</div>
        <div>
            <div style="color: {color}; font-weight: 700; font-size: 1.1rem;">{a["name"]}</div>
            <div style="color: #94A3B8; font-size: 0.9rem;">{a["desc"]}</div>
        </div>
    </div>
    ''', unsafe_allow_html=True)

