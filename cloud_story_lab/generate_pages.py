import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from story_data import STORIES, get_page_path

# Clean existing pages directory first
pages_dir = os.path.join(os.path.dirname(__file__), "pages")
os.makedirs(pages_dir, exist_ok=True)
for f in os.listdir(pages_dir):
    if f.endswith(".py"):
        os.remove(os.path.join(pages_dir, f))

for story in STORIES:
    sid = story["id"]
    rel_path = get_page_path(sid, story["title"])
    filename = os.path.basename(rel_path)
    filepath = os.path.join(pages_dir, filename)
    
    content = f'''import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import ui
from story_data import STORIES
try:
    from level_content import LEVEL_CONTENT
except ImportError:
    LEVEL_CONTENT = {{}}

story_id = {sid}
story = next(s for s in STORIES if s["id"] == story_id)
ui.configure_page(title=f"Case {sid:02d}: {{story['title']}} | Cloud Story Lab", active_nav="case")
ui.render_episodic_page(story_id, story, LEVEL_CONTENT.get(str(story_id), {{}}))
'''
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Generated {len(STORIES)} clean page files in {pages_dir}!")
