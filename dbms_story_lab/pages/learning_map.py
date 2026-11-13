import streamlit as st
from ui import sidebar, configure_page, PAGE_PATHS
from story_data import STORIES
from persistence import load_progress

load_progress()
configure_page("Journey")
sidebar(active="map")

st.markdown('''
<style>
.path-container { display: flex; flex-direction: column; gap: 0; position: relative; margin-top: 32px; }
.path-node { display: flex; align-items: stretch; gap: 32px; position: relative; }
.path-line-container { width: 40px; display: flex; flex-direction: column; align-items: center; }
.path-icon { width: 40px; height: 40px; border-radius: 20px; display: flex; align-items: center; justify-content: center; z-index: 2; font-weight: 800; font-size: 0.9rem; }
.path-line { flex: 1; width: 2px; background: rgba(255,255,255,0.05); }

/* States */
.node-completed .path-icon { background: rgba(52, 211, 153, 0.1); color: #34D399; border: 1px solid #34D399; }
.node-completed .path-line { background: #34D399; }
.node-completed .path-content { opacity: 0.7; }

.node-active .path-icon { background: #7C4DFF; color: #F8F7FF; border: 4px solid #121B32; box-shadow: 0 0 0 2px #7C4DFF; }
.node-active .path-content { background: #121B32; border-color: rgba(124,77,255,0.3); box-shadow: 0 8px 32px rgba(124,77,255,0.1); }

.node-locked .path-icon { background: #0B1225; color: #64748B; border: 1px solid rgba(255,255,255,0.1); }
.node-locked .path-content { opacity: 0.4; }

.path-content { flex: 1; background: #0B1225; border: 1px solid rgba(255,255,255,0.05); padding: 24px 32px; border-radius: 20px; margin-bottom: 32px; transition: all 0.2s; }
.path-title { font-size: 1.2rem; font-weight: 800; color: #F8F7FF; margin-bottom: 8px; display: flex; align-items: center; gap: 12px; }
.path-desc { color: #AAB3CC; font-size: 0.95rem; line-height: 1.5; }
</style>
''', unsafe_allow_html=True)

st.title("Database Foundations")
st.markdown("<p style='color: #AAB3CC; margin-bottom: 48px;'>Follow the story to master DBMS concepts.</p>", unsafe_allow_html=True)

st.markdown('<div class="path-container">', unsafe_allow_html=True)

for i, story in enumerate(STORIES):
    sid = story["id"]
    is_completed = sid in st.session_state.completed
    # Determine if active. It's active if the previous one is completed, or it's the very first one
    # Or if the user has explicitly started it.
    if sid == 1:
        is_active = not is_completed
        is_locked = False
    else:
        prev_sid = STORIES[i-1]["id"]
        is_active = (prev_sid in st.session_state.completed) and not is_completed
        is_locked = not (prev_sid in st.session_state.completed) and not is_completed

    if is_completed:
        state_class = "node-completed"
        icon = "✓"
    elif is_active:
        state_class = "node-active"
        icon = f"{sid:02d}"
    else:
        state_class = "node-locked"
        icon = f"{sid:02d}"

    st.markdown(f'''
    <div class="path-node {state_class}">
        <div class="path-line-container">
            <div class="path-icon">{icon}</div>
            {'' if i == len(STORIES)-1 else '<div class="path-line"></div>'}
        </div>
        <div class="path-content">
            <div class="path-title">
                <span style="color: #64748B; font-size: 0.9rem;">{sid:02d} ──</span>
                {story["title"]}
            </div>
            <div class="path-desc">{story["hook"]}</div>
    ''', unsafe_allow_html=True)
    
    if not is_locked:
        btn_label = "Review Chapter" if is_completed else "Continue Investigation →"
        btn_type = "secondary" if is_completed else "primary"
        if st.button(btn_label, key=f"btn_story_{sid}", type=btn_type):
            st.switch_page(PAGE_PATHS[sid])
            
    st.markdown('</div></div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
