import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import ui
from story_data import STORIES
try:
    from level_content import LEVEL_CONTENT
except ImportError:
    LEVEL_CONTENT = {}

story_id = 13
story = next(s for s in STORIES if s["id"] == story_id)
ui.configure_page(title=f"Case 13: {story['title']} | Cloud Story Lab", active_nav="case")
ui.render_episodic_page(story_id, story, LEVEL_CONTENT.get(str(story_id), {}))
