import streamlit as st
from ui import sidebar, configure_page, story_status, CATEGORIES, PAGE_PATHS
from persistence import load_progress
from story_data import STORIES

load_progress()
st.session_state.setdefault("completed", set())
st.session_state.setdefault("xp", 0)
st.session_state.setdefault("missions", {})
st.session_state.setdefault("last_story_id", 0)
st.session_state.setdefault("last_level", 1)

configure_page("DBMS Story Lab")
sidebar(active="home")

last_case_id = st.session_state.get("last_story_id")
if last_case_id is None:
    last_case_id = 0
last_story = next((s for s in STORIES if s["id"] == last_case_id), STORIES[0])
last_level = st.session_state.get("last_level", 1)

# Simplify top navigation
st.markdown('''

<style>
/* Top Nav Container */
.top-nav-container { display: flex; align-items: center; justify-content: flex-start; gap: 32px; padding: 16px 32px; margin-bottom: 48px; border-bottom: 1px solid rgba(255,255,255,0.05); }
.top-nav-brand { font-weight: 800; color: #F8F7FF; letter-spacing: 0.1em; font-size: 1.1rem; }
.top-nav-links { display: flex; gap: 24px; }
.top-nav-link { color: #AAB3CC; font-weight: 600; text-decoration: none; transition: color 0.2s; }
.top-nav-link:hover { color: #F8F7FF; }
.top-nav-progress { margin-left: auto; color: #64748B; font-size: 0.9rem; font-weight: 700; display: flex; align-items: center; gap: 12px; }
.progress-bar-small { width: 100px; height: 6px; background: rgba(255,255,255,0.1); border-radius: 3px; overflow: hidden; }
.progress-bar-small-fill { height: 100%; background: #7C4DFF; }
</style>

''', unsafe_allow_html=True)

# Fake a top nav bar natively via columns
nav1, nav2, nav3, nav4, nav5 = st.columns([2, 1, 1, 1, 4])
with nav1: st.markdown('<div class="top-nav-brand">DBMS STORY LAB</div>', unsafe_allow_html=True)
with nav2: st.page_link("app.py", label="Journey")
with nav3: st.page_link("pages/13_sql_playground.py", label="Practice")
with nav4: st.page_link("pages/progress.py", label="Progress")
with nav5:
    total_progress = int((len(st.session_state.completed) / 11) * 100)
    st.markdown(f'''

<div class="top-nav-progress">
<span>{total_progress}% Complete</span>
<div class="progress-bar-small"><div class="progress-bar-small-fill" style="width: {total_progress}%;"></div></div>
</div>

''', unsafe_allow_html=True)

# Main Hero
st.markdown(f'''

<div style="margin-bottom: 64px;">
<div style="font-size: 0.8rem; font-weight: 800; letter-spacing: 0.2em; color: #A78BFA; margin-bottom: 16px;">YOUR DBMS INVESTIGATION</div>
<h1 style="font-size: 3.5rem; line-height: 1.1; margin-bottom: 24px; color: #F8F7FF;">Learn databases by solving cases.</h1>
<p style="font-size: 1.2rem; color: #AAB3CC; max-width: 600px; line-height: 1.6; margin-bottom: 32px;">
Explore real database problems,<br>
understand the concepts behind them,<br>
then use SQL to solve the mystery.
</p>
</div>

''', unsafe_allow_html=True)

col_hero1, col_hero2 = st.columns([1.5, 1])
with col_hero1:
    if st.button("Continue Investigation →", type="primary", use_container_width=False):
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
    # A beautiful visual representation of a database investigation
    st.markdown('''

<div style="background: rgba(124, 77, 255, 0.05); border: 1px solid rgba(124, 77, 255, 0.2); border-radius: 24px; padding: 32px; position: relative; overflow: hidden;">
<div style="position: absolute; top: -50%; left: -50%; width: 200%; height: 200%; background: radial-gradient(circle at center, rgba(124, 77, 255, 0.1) 0%, transparent 70%); z-index: 0;"></div>
<div style="position: relative; z-index: 1; font-family: monospace; color: #A78BFA; font-size: 0.9rem; line-height: 1.6;">
> SELECT * FROM system.logs<br>
> WHERE timestamp > '03:00'<br>
> AND user = 'admin';<br><br>
[1 rows returned]<br><br>
<span style="color: #F87171;">CRITICAL EXCEPTION</span><br>
> Access granted.<br>
> Erasing tracks...
</div>
</div>

''', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# Current Case Card
st.markdown('<div style="font-size: 0.8rem; font-weight: 800; letter-spacing: 0.2em; color: #AAB3CC; margin-bottom: 24px;">CURRENT CASE</div>', unsafe_allow_html=True)

st.markdown(f'''

<div style="background: #121B32; border: 1px solid rgba(255,255,255,0.05); border-radius: 24px; display: flex; overflow: hidden; box-shadow: 0 24px 48px rgba(0,0,0,0.4);">
<div style="flex: 1; padding: 48px;">
<div style="color: #64748B; font-weight: 800; font-size: 0.85rem; letter-spacing: 0.15em; margin-bottom: 12px;">CASE {last_case_id:02d} · DATABASE INVESTIGATION</div>
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
<div>• Database Architecture</div>
<div>• Tables & Relationships</div>
<div>• SQL Queries</div>
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
<!-- Visual representation of database relationship -->
<div style="font-family: monospace; color: #AAB3CC; font-size: 0.85rem;">
<pre style="background: transparent; color: #A78BFA; border: none;">
  ┌───────────────┐
  │   EMPLOYEES   │
  ├───────────────┤
  │ id            │◄──┐
  │ department_id │   │
  │ access_level  │   │
  └───────────────┘   │
                      │
  ┌───────────────┐   │
  │ DEPARTMENTS   │   │
  ├───────────────┤   │
  │ id            │───┘
  │ name          │
  │ secure_zone   │
  └───────────────┘
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
                <div style="background: {bg}; border: {border}; border-radius: 20px; padding: 24px; position: relative; margin-bottom: 12px; height: 220px; display: flex; flex-direction: column;">
                    <div style="color: {icon_color}; font-size: 0.75rem; font-weight: 800; letter-spacing: 0.1em; margin-bottom: 12px; display: flex; align-items: center; gap: 8px;"><span>{story.get('icon', '📖')}</span> CASE {story['id']:02d}</div>
                    <div style="color: {title_color}; font-weight: 800; font-size: 1.1rem; margin-bottom: 8px; line-height: 1.3;">{story['title']}</div>
                    <div style="color: {desc_color}; font-size: 0.85rem; line-height: 1.4; margin-bottom: auto;">{story['hook']}</div>
                    {bottom_icon}
                </div>
                '''
                st.markdown('\n'.join(line.lstrip() for line in card_html.split('\n')), unsafe_allow_html=True)
                if st.button("Open Case", key=f"open_{story['id']}", use_container_width=True):
                    st.switch_page(PAGE_PATHS[story["id"]])

st.markdown("</div>", unsafe_allow_html=True)

