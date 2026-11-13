import streamlit as st
from story_data import STORIES
from level_content import LEVEL_CONTENT
from ui import render_episodic_page, render_story_page

story_id = 2
story = next((s for s in STORIES if s["id"] == story_id), None)

if story:
    data = LEVEL_CONTENT.get(str(story_id), None)
    if data and data.get("format") == "episodic":
        render_episodic_page(story_id, story, data)
    else:
        render_story_page(story_id)
else:
    st.error("Story not found!")
