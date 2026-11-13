import streamlit as st
import sys
import os

sys.path.append(os.path.dirname(__file__))

from ui import configure_page, workspace_css, story_status, ensure_state, sidebar
from story_data import STORIES

# We need a PAGE_PATHS dict
pages_dir = os.path.join(os.path.dirname(__file__), "pages")
PAGE_PATHS = {}
for story in STORIES:
    sid = story["id"]
    title_safe = story["title"].lower().replace(" ", "_").replace("'", "").replace("-", "_").replace(",", "")
    PAGE_PATHS[sid] = f"pages/{sid:02d}_{title_safe}.py"

configure_page("Home | OOP Story Lab")
workspace_css()
ensure_state()
sidebar("home")


last_case_id = st.session_state.get("last_story_id", 0)
last_story = next((s for s in STORIES if s["id"] == last_case_id), STORIES[0])
last_level = st.session_state.get(f"active_level_{last_case_id}", 1)

# Floating status bar at the top right


st.markdown('''
<div style="padding: 48px 0;">
<div style="color: #7C4DFF; font-weight: 800; font-size: 0.85rem; letter-spacing: 0.15em; margin-bottom: 16px;">C++ ENGINEERING SIMULATOR</div>
<h1 style="font-size: 3.5rem; line-height: 1.1; margin-bottom: 24px; color: #F8F7FF;">Learn C++ objects by<br>building architecture.</h1>
<p style="font-size: 1.2rem; color: #AAB3CC; max-width: 600px; line-height: 1.6; margin-bottom: 32px;">
Explore real engineering problems,<br>
understand the concepts behind them,<br>
then write C++ to solve the mystery.
</p>
</div>
''', unsafe_allow_html=True)

col_hero1, col_hero2 = st.columns([1.5, 1])
with col_hero1:
    if st.button("Continue Engineering →", type="primary", use_container_width=False):
        st.switch_page(PAGE_PATHS[last_case_id])
    
    st.markdown(f'''
<div style="margin-top: 32px; max-width: 400px;">
<div style="display: flex; justify-content: space-between; font-size: 0.85rem; font-weight: 700; color: #AAB3CC; margin-bottom: 8px;">
<span>Case Progress</span>
<span>{min(last_level * 12, 100)}%</span>
</div>
<div style="width: 100%; height: 8px; background: rgba(255,255,255,0.05); border-radius: 4px; overflow: hidden;">
<div style="width: {min(last_level * 12, 100)}%; height: 100%; background: linear-gradient(90deg, #7C4DFF, #A78BFA);"></div>
</div>
</div>
''', unsafe_allow_html=True)

with col_hero2:
    st.markdown('''
<div style="background: rgba(124, 77, 255, 0.05); border: 1px solid rgba(124, 77, 255, 0.2); border-radius: 24px; padding: 32px; position: relative; overflow: hidden;">
<div style="position: absolute; top: -50%; left: -50%; width: 200%; height: 200%; background: radial-gradient(circle at center, rgba(124, 77, 255, 0.1) 0%, transparent 70%); z-index: 0;"></div>
<div style="position: relative; z-index: 1; font-family: monospace; color: #A78BFA; font-size: 0.9rem; line-height: 1.6;">
> class PaymentProcessor {<br>
> &nbsp;&nbsp;public:<br>
> &nbsp;&nbsp;&nbsp;&nbsp;virtual void process() = 0;<br>
> &nbsp;&nbsp;&nbsp;&nbsp;virtual ~PaymentProcessor() = default;<br>
> };<br><br>
<span style="color: #34D399;">SUCCESS:</span> System compiled.<br>
> Interface loaded into vtable.
</div>
</div>
''', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown('<div style="font-size: 0.8rem; font-weight: 800; letter-spacing: 0.2em; color: #AAB3CC; margin-bottom: 24px;">CURRENT ARCHITECTURE MISSION</div>', unsafe_allow_html=True)

st.markdown(f'''
<div style="background: #121B32; border: 1px solid rgba(255,255,255,0.05); border-radius: 24px; display: flex; overflow: hidden; box-shadow: 0 24px 48px rgba(0,0,0,0.4);">
<div style="flex: 1; padding: 48px;">
<div style="color: #64748B; font-weight: 800; font-size: 0.85rem; letter-spacing: 0.15em; margin-bottom: 12px;">CASE {last_case_id:02d} · C++ INVESTIGATION</div>
<h2 style="margin: 0 0 16px 0; font-size: 2.5rem; color: #F8F7FF;">{last_story["title"].upper()}</h2>
<p style="color: #AAB3CC; font-size: 1.1rem; line-height: 1.6; margin-bottom: 32px;">{last_story["hook"]}</p>

<hr style="border:none; border-top: 1px solid rgba(255,255,255,0.1); margin: 32px 0;">

<div style="display: flex; gap: 64px;">
<div>
<div style="color: #64748B; font-weight: 800; font-size: 0.75rem; letter-spacing: 0.15em; margin-bottom: 12px;">CASE STATUS</div>
<div style="color: #F8F7FF; font-weight: 700;">{min(last_level * 12, 100)}% Investigated</div>
</div>
<div>
<div style="color: #64748B; font-weight: 800; font-size: 0.75rem; letter-spacing: 0.15em; margin-bottom: 12px;">CONCEPTS</div>
<div style="color: #AAB3CC; display: flex; flex-direction: column; gap: 8px;">
<div>• Memory Management</div>
<div>• OOP Architecture</div>
<div>• SOLID Principles</div>
</div>
</div>
</div>
<div style="margin-top: 48px;">
''', unsafe_allow_html=True)

if st.button("Enter Investigation →", key="enter_investigation", type="primary"):
    st.switch_page(PAGE_PATHS[last_case_id])

st.markdown('''
</div>
</div>
<div style="flex: 1; background: #0B1225; padding: 48px; border-left: 1px solid rgba(255,255,255,0.05); display: flex; align-items: center; justify-content: center; position: relative;">
<div style="font-family: monospace; color: #AAB3CC; font-size: 0.85rem;">
<pre style="background: transparent; color: #A78BFA; border: none;">
  class IEngine {{
  public:
      virtual void start() = 0;
      virtual ~IEngine() = default;
  }};
  
         ▲
         │ (implements)
         │
  class V8Engine : public IEngine {{
  public:
      void start() override;
  }};
</pre>
</div>
</div>
</div>
''', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown('<div style="font-size: 0.8rem; font-weight: 800; letter-spacing: 0.2em; color: #AAB3CC; margin-bottom: 24px;">ALL INVESTIGATIONS</div>', unsafe_allow_html=True)

st.markdown("<div style='display: flex; gap: 24px; overflow-x: auto; padding-bottom: 24px; margin-bottom: 24px;'>", unsafe_allow_html=True)

for i in range(0, len(STORIES), 4):
    cols = st.columns(4)
    for j in range(4):
        if i + j < len(STORIES):
            story = STORIES[i + j]
            with cols[j]:
                status_text, status_class = story_status(story["id"])
                
                if "Completed" in status_text:
                    bg = "rgba(167, 243, 208, 0.1)"
                    border = "1px solid #34D399"
                    icon_color = "#34D399"
                    title_color = "#F8F7FF"
                    desc_color = "#AAB3CC"
                    bottom_icon = '<div style="width: 32px; height: 32px; border-radius: 16px; background: #34D399; color: #064E3B; display: flex; align-items: center; justify-content: center; font-weight: 800; margin: 0 auto;">✓</div>'
                elif "progress" in status_text:
                    bg = "rgba(124, 77, 255, 0.1)"
                    border = "2px solid #7C4DFF"
                    icon_color = "#A78BFA"
                    title_color = "#F8F7FF"
                    desc_color = "#AAB3CC"
                    bottom_icon = '<div style="background: rgba(124, 77, 255, 0.2); color: #C4B5FD; border-radius: 12px; padding: 6px 0; text-align: center; font-weight: 700; font-size: 0.85rem; width: 60px; margin: 0 auto;">Active</div>'
                else:
                    bg = "#121B32"
                    border = "1px solid rgba(255,255,255,0.05)"
                    icon_color = "#64748B"
                    title_color = "#F8F7FF"
                    desc_color = "#64748B"
                    bottom_icon = '<div style="width: 32px; height: 32px; border-radius: 16px; background: rgba(255,255,255,0.05); color: #64748B; display: flex; align-items: center; justify-content: center; margin: 0 auto;">○</div>'

                card_html = f'''
                <div style="background: {bg}; border: {border}; border-radius: 20px; padding: 24px; position: relative; margin-bottom: 12px; height: 280px; display: flex; flex-direction: column;">
                    <div style="color: {icon_color}; font-size: 0.75rem; font-weight: 800; letter-spacing: 0.1em; margin-bottom: 12px; display: flex; align-items: center; gap: 8px; flex-shrink: 0;"><span>{story.get('icon', '📖')}</span> CASE {story['id']:02d}</div>
                    <div style="color: {title_color}; font-weight: 800; font-size: 1.1rem; margin-bottom: 8px; line-height: 1.3; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; flex-shrink: 0;">{story['title']}</div>
                    <div style="color: {desc_color}; font-size: 0.85rem; line-height: 1.4; margin-bottom: 16px; display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical; overflow: hidden; flex-grow: 1;">{story['hook']}</div>
                    <div style="margin-top: auto; flex-shrink: 0;">{bottom_icon}</div>
                </div>
                '''
                st.markdown('\n'.join(line.lstrip() for line in card_html.split('\n')), unsafe_allow_html=True)
                if st.button("Open Case", key=f"open_{story['id']}", use_container_width=True):
                    st.switch_page(PAGE_PATHS[story["id"]])

st.markdown("</div>", unsafe_allow_html=True)
