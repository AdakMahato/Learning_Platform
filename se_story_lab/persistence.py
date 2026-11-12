import streamlit as st

def init_db():
    """Compatibility function retained for existing imports."""
    return

def load_progress():
    """
    Initialize progress for the current Streamlit browser session.
    Session-based progress ensures isolated state per student.
    """
    st.session_state.setdefault("completed", set())
    st.session_state.setdefault("xp", 0)
    st.session_state.setdefault("last_story_id", 0)
    st.session_state.setdefault("loaded", True)

def save_progress():
    return

def reset_progress():
    st.session_state["completed"] = set()
    st.session_state["xp"] = 0
    st.session_state["last_story_id"] = 0

    for key in list(st.session_state.keys()):
        if key.startswith("active_level_"):
            del st.session_state[key]
