import streamlit as st
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from ui import configure_page, render_episodic_page
from story_data import STORIES
from level_content import LEVEL_CONTENT

configure_page()
story_id = 20
story = next((s for s in STORIES if s["id"] == story_id), STORIES[0])
data = LEVEL_CONTENT.get(str(story_id), {"episodes": []})

render_episodic_page(story_id, story, data)
