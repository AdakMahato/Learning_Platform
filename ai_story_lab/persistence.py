import streamlit as st


def init_db():
    """Compatibility function retained for existing imports."""
    return


def load_progress():
    """
    Initialize progress for the current Streamlit browser session.

    Public v1 intentionally uses session-based progress so different
    visitors do not share a single SQLite record.
    """
    st.session_state.setdefault("completed", set())
    st.session_state.setdefault("xp", 0)
    st.session_state.setdefault("last_story_id", 0)
    st.session_state.setdefault("loaded", True)


def save_progress():
    """
    Progress already lives in st.session_state.

    This function is kept so the rest of the application does not need
    to change.
    """
    return


def reset_progress():
    st.session_state["completed"] = set()
    st.session_state["xp"] = 0
    st.session_state["last_story_id"] = 0

    for key in list(st.session_state.keys()):
        if key.startswith("active_level_"):
            del st.session_state[key]
