import streamlit as st
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from ui import configure_page, render_episodic_page
from story_data import STORIES
from level_content import LEVEL_CONTENT

story_id = 2
story = next(s for s in STORIES if s["id"] == story_id)
data = LEVEL_CONTENT.get(str(story_id), LEVEL_CONTENT.get(story_id, {}))

configure_page(f"Case {story_id:02d} | {story['title']}", "case")
render_episodic_page(story_id, story, data)
