import json
import os
from story_data import STORIES

PAGE_PATHS = {}

for s in STORIES:
    title_safe = s['title'].lower().replace(' ', '_').replace('\'', '').replace('-', '_').replace(',', '')
    filename = f"{s['id']:02d}_{title_safe}.py"
    path = os.path.join("pages", filename)
    PAGE_PATHS[s['id']] = path
    
    with open(path, "w") as f:
        f.write(f"""import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import ui
from story_data import STORIES
try:
    from level_content import LEVEL_CONTENT
except ImportError:
    LEVEL_CONTENT = {{}}

story_id = {s['id']}
story = next(s for s in STORIES if s["id"] == story_id)
ui.configure_page(title=story["title"], active_nav="case")
ui.render_episodic_page(story_id, story, LEVEL_CONTENT.get(str(story_id), {{}}))
""")

with open("ui.py", "r") as f:
    ui_content = f.read()

# Update PAGE_PATHS in ui.py
import re
ui_content = re.sub(r'PAGE_PATHS = \{.*?\}', f'PAGE_PATHS = {PAGE_PATHS}', ui_content, flags=re.DOTALL)
with open("ui.py", "w") as f:
    f.write(ui_content)

