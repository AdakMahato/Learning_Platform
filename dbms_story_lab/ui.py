import streamlit as st

from challenges import render_story_challenge
from story_data import STORIES
from persistence import load_progress, save_progress
from level_content import LEVEL_CONTENT

PAGE_PATHS = {7: 'pages/07_machine_lied.py', 9: 'pages/09_convoy_zero.py', 4: 'pages/04_impossible_contract.py', 0: 'pages/00_forgotten_archive.py', 10: 'pages/10_colony_laws.py', 11: 'pages/11_vanishing_hour.py', 8: 'pages/08_silence_between_signals.py', 5: 'pages/05_depth_ledger.py', 3: 'pages/03_remembered_too_much.py', 6: 'pages/06_last_broadcast.py', 1: 'pages/01_foundation.py', 2: 'pages/02_impossible_blueprint.py'}
ACCENTS = {1: '#047857', 11: '#7C3AED', 9: '#2563EB', 8: '#0891B2', 3: '#9333EA', 6: '#DC2626', 5: '#B45309', 10: '#059669', 7: '#4F46E5', 0: '#64748B', 2: '#0F766E', 4: '#B45309'}
CATEGORIES = {1: 'Foundation', 11: 'SQL', 9: 'Distributed Systems', 8: 'Performance', 3: 'Design', 6: 'Transactions', 5: 'SQL', 10: 'Distributed Systems', 7: 'Transactions', 0: 'Foundation', 2: 'Design', 4: 'Design'}


def configure_page(title="DBMS Story Lab", active_nav="Home"):
    ensure_state()
    st.set_page_config(page_title=title, page_icon="🗄️", layout="wide", initial_sidebar_state="expanded")
    st.markdown("""
        <style>
    html, body, [class*="css"] { font-family: "Nunito", Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }
    .stApp { background:#0B1225; color:#F8F7FF; }
    .block-container { max-width:1400px; padding:3rem 2rem 3.5rem; }
    [data-testid="stSidebar"] { background:#080D1D; border-right:1px solid rgba(255,255,255,0.05); }
    [data-testid="stSidebar"] > div:first-child { padding:1.5rem 1.2rem; }
    [data-testid="stSidebarNav"] { display:none; }
    #MainMenu, footer, header { visibility:hidden; }
    
    /* Typography & Headers */
    h1, h2, h3, h4 { color: #F8F7FF; font-weight: 800; letter-spacing: -0.03em; }
    
    /* Sidebar Links */
    [data-testid="stSidebar"] a[data-testid="stPageLink-Nav"] { color:#AAB3CC; border-radius:12px; min-height:44px; padding:10px 14px; margin:4px 0; font-size:.95rem; font-weight: 600; transition: all 200ms cubic-bezier(0.4, 0, 0.2, 1); }
    [data-testid="stSidebar"] a[data-testid="stPageLink-Nav"]:hover { background:#121B32; color:#F8F7FF; }
    .nav-active { background: linear-gradient(90deg, rgba(124,77,255,0.15) 0%, rgba(124,77,255,0) 100%); border-left: 3px solid #7C4DFF; color:#F8F7FF !important; border-radius:8px; padding:10px 14px; font-weight:700; margin:4px 0; text-shadow: 0 0 10px rgba(124,77,255,0.5); }
    
    /* Floating Status Bar */
    .global-status-bar { margin: 0 0 32px auto; max-width: fit-content; z-index:9999; height:56px; display:flex; align-items:center; justify-content:center; background:#121B32; border-radius: 28px; border: 1px solid rgba(255,255,255,0.1); padding: 0 24px; gap: 24px; box-shadow: 0 8px 32px rgba(0,0,0,0.4); }
    .global-status-item { display:flex; justify-content:center; align-items:center; gap:8px; color:#AAB3CC; font-size:.9rem; font-weight: 600; } 
    .global-status-item b { color:#F8F7FF; font-size:1rem; }
    .global-status-icon { color:#A78BFA; font-size:1.1rem; }
    
    /* Cards */
    .stat-card, .story-card { background:#121B32; border:1px solid rgba(255,255,255,0.05); border-radius:24px; padding:24px; transition:all 250ms cubic-bezier(0.4, 0, 0.2, 1); box-shadow: inset 0 1px 0 rgba(255,255,255,0.05); }
    .story-card { height:320px; display:flex; flex-direction:column; cursor: pointer; overflow: hidden; position: relative; }
    .story-card:hover { transform:translateY(-6px); border-color:#7C4DFF; box-shadow:0 20px 40px rgba(124,77,255,0.15); }
    
    /* Buttons */
    .stButton > button { background:#121B32; border:1px solid rgba(255,255,255,0.1); color:#AAB3CC; border-radius:16px; font-weight:700; font-size: 1rem; padding: 12px 24px; min-height:48px; transition:all 200ms cubic-bezier(0.4, 0, 0.2, 1); }
    .stButton > button:hover { background:#17213B; border-color:rgba(255,255,255,0.2); color:#F8F7FF; transform:translateY(-2px); }
    
    /* Primary CTA */
    .stButton > button[kind="primary"] { background: linear-gradient(135deg, #7C4DFF 0%, #8B5CF6 100%); border:none; color:#FFFFFF; box-shadow: 0 8px 24px rgba(124,77,255,0.3); }
    .stButton > button[kind="primary"]:hover { background: linear-gradient(135deg, #8B5CF6 0%, #A78BFA 100%); transform:translateY(-2px); box-shadow: 0 12px 32px rgba(124,77,255,0.5); }
    
    /* Inputs */
    .stTextInput input, .stTextArea textarea { background:#121B32; border:1px solid rgba(255,255,255,0.1); color:#F8F7FF; border-radius:12px; padding: 14px 16px; font-size: 1rem; transition: all 200ms ease; }
    .stTextInput input:focus, .stTextArea textarea:focus { border-color:#7C4DFF; box-shadow:0 0 0 4px rgba(124,77,255,0.1); }
    
    /* Blocks */
    .objective { background:#121B32; border:1px solid rgba(255,255,255,0.05); padding:24px; border-radius:24px; margin: 20px 0; font-size: 1.1rem; line-height: 1.6; color: #AAB3CC; box-shadow: inset 0 1px 0 rgba(255,255,255,0.05); }
    .objective h3 { margin-top: 0; color: #F8F7FF; }
    
    .problem-block { background:rgba(239, 68, 68, 0.1); border: 1px solid rgba(239, 68, 68, 0.2); padding:20px 24px; color:#FCA5A5; margin: 20px 0; border-radius:20px; font-size: 1.05rem; }
    .concept-block { background:rgba(124, 77, 255, 0.1); border:1px solid rgba(124, 77, 255, 0.3); padding:24px; border-radius:20px; margin: 20px 0; }
    .concept-block b { color: #DDD6FE; font-size: 1.2rem; }
    
    /* Navigation Rail */
    .level-static { background: #080D1D; border: 1px solid rgba(255,255,255,0.05); border-radius: 16px; padding: 12px 16px; margin: 8px 0; font-weight: 700; color: #475569; }
    
    /* Animations */
    @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
    .workspace-main { animation: fadeIn 0.4s ease-out forwards; }
    
    /* Toast overriding */
    [data-testid="stToast"] { border-radius: 16px; font-weight: 700; background: #121B32; color: #F8F7FF; border: 1px solid rgba(255,255,255,0.1); }
    </style>
    """, unsafe_allow_html=True)
    ensure_state()
    completed = len(st.session_state.completed)






def ensure_state():
    load_progress()  # Restore saved progress on first call; no-op on subsequent calls
    st.session_state.setdefault("completed", set())
    st.session_state.setdefault("xp", 0)
    st.session_state.setdefault("missions", {})


def mark_complete(story_id, amount=100, level=1, total_levels=1):
    key = f"mission_{story_id}_{level}"
    if not st.session_state.get(key):
        st.session_state[key] = True
        st.session_state.xp += amount
        if level == total_levels:
            st.session_state.completed.add(story_id)
        save_progress()


def skill_radar():
    import plotly.graph_objects as go
    categories = ["SQL", "Modeling", "Normalization", "Indexing", "Transactions", "Concurrency", "Distributed", "Recovery"]
    base = [35, 30, 28, 25, 25, 24, 20, 22]
    cleared = len(st.session_state.completed)
    values = [min(100, score + cleared * 5) for score in base]
    fig = go.Figure(go.Scatterpolar(r=values + values[:1], theta=categories + categories[:1], fill="toself", fillcolor="rgba(79,70,229,.12)", line={"color": "#4F46E5", "width": 2}))
    fig.update_layout(paper_bgcolor="#FFFFFF", font_color="#475467", showlegend=False, height=360, margin={"l":45,"r":45,"t":25,"b":25}, polar={"bgcolor":"#FFFFFF", "radialaxis":{"visible":True,"range":[0,100],"gridcolor":"#E4E7EC","linecolor":"#E4E7EC"}, "angularaxis":{"gridcolor":"#E4E7EC","linecolor":"#E4E7EC"}})
    return fig


def sidebar(active="home", render_rail=None, minimal=False):
    with st.sidebar:
        st.markdown('''
        <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 32px;">
            <div style="background: linear-gradient(135deg, #1E1B4B 0%, #312E81 100%); width: 40px; height: 40px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; border: 1px solid rgba(255,255,255,0.1);">🗄️</div>
            <div>
                <div style="font-weight: 800; color: #F8F7FF; letter-spacing: 0.05em; font-size: 1.1rem; line-height: 1.1;">DBMS STORY LAB</div>
            </div>
        </div>
        ''', unsafe_allow_html=True)
        
        if minimal:
            st.page_link("app.py", label="🏠  Home")
            st.markdown("<br>", unsafe_allow_html=True)
            if render_rail:
                render_rail()
            return

        if render_rail:
            render_rail()
            st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown('<div style="color: #64748B; font-size: 0.75rem; font-weight: 800; letter-spacing: 0.15em; margin: 32px 0 12px 0;">LEARNING</div>', unsafe_allow_html=True)
        if active == "home": st.markdown('<div class="nav-active">🏠 &nbsp; Home</div>', unsafe_allow_html=True)
        else: st.page_link("app.py", label="🏠  Home")
        if active == "map": st.markdown('<div class="nav-active">▣ &nbsp; Journey</div>', unsafe_allow_html=True)
        else: st.page_link("pages/learning_map.py", label="▣  Journey")
        if active == "concepts": st.markdown('<div class="nav-active">▤ &nbsp; Concepts</div>', unsafe_allow_html=True)
        else: st.page_link("pages/14_concepts.py", label="▤  Concepts")
        if active == "practice": st.markdown('<div class="nav-active">⌘ &nbsp; SQL Playground</div>', unsafe_allow_html=True)
        else: st.page_link("pages/13_sql_playground.py", label="⌘  SQL Playground")
        
        st.markdown('<div style="color: #64748B; font-size: 0.75rem; font-weight: 800; letter-spacing: 0.15em; margin: 32px 0 12px 0;">YOUR INVESTIGATION</div>', unsafe_allow_html=True)
        last_case = st.session_state.get("last_story_id", 0)
        from ui import PAGE_PATHS
        case_path = PAGE_PATHS.get(last_case, "app.py") if last_case else "app.py"
        
        if active == "case": st.markdown('<div class="nav-active">◉ &nbsp; Current Case</div>', unsafe_allow_html=True)
        else: st.page_link(case_path, label="◉  Current Case")
        if active == "notebook": st.markdown('<div class="nav-active">▣ &nbsp; Field Notebook</div>', unsafe_allow_html=True)
        else: st.page_link("pages/12_field_notebook.py", label="▣  Field Notebook")
        
        st.markdown('<div style="color: #64748B; font-size: 0.75rem; font-weight: 800; letter-spacing: 0.15em; margin: 32px 0 12px 0;">PROGRESS</div>', unsafe_allow_html=True)
        if active == "progress": st.markdown('<div class="nav-active">📈 &nbsp; Progress</div>', unsafe_allow_html=True)
        else: st.page_link("pages/progress.py", label="📈  Progress")
        if active == "achievements": st.markdown('<div class="nav-active">🏆 &nbsp; Achievements</div>', unsafe_allow_html=True)
        else: st.page_link("pages/achievements.py", label="🏆  Achievements")
        
        if st.button("Reset progress", use_container_width=True):
            st.session_state.completed = set()
            st.session_state.xp = 0
            st.session_state.missions = {}
            for key in list(st.session_state.keys()):
                if key.startswith(("completed_levels_", "active_level_", "level_picker_", "mcq_", "proceed_", "mission_", "notebook_", "concept_mastery", "last_")):
                    del st.session_state[key]
            try:
                from persistence import save_progress
                save_progress()
            except Exception as e:
                pass
            st.rerun()

def story_status(story_id):
    if story_id in st.session_state.completed: return "✓ Completed", "status-complete"
    if any(st.session_state.get(f"mission_{story_id}_{i}") for i in range(1, 9)): return "◐ In progress", "status-progress"
    return "○ Not started", "status-open"


def story_card(story):
    accent = ACCENTS[story["id"]]
    status, status_class = story_status(story["id"])
    badges = "".join(f'<span class="badge">{x}</span>' for x in story["topics"][:3])
    st.markdown(f'''<div class="story-card"><div class="story-icon" style="background:{accent}18">{story['icon']}</div><div class="story-category" style="color:{accent}">{CATEGORIES[story['id']].upper()} · {story['genre']}</div><h3>{story['title']}</h3><p class="story-desc">{story['hook']}</p><div class="badges">{badges}</div><div class="card-footer"><span>{story['difficulty'].upper()}</span><br><span class="{status_class}">{status}</span></div></div>''', unsafe_allow_html=True)
    if st.button("Open investigation →", key=f"enter_{story['id']}", use_container_width=True): st.switch_page(PAGE_PATHS[story["id"]])


LEVELS = [
    ("Discovery", "Read the evidence"), ("Investigation", "Trace the records"),
    ("Complexity", "Test the contradiction"), ("Failure", "Find the weak point"),
    ("Optimization", "Make it scale"), ("Conflict", "Resolve competing facts"),
    ("Disaster", "Recover the truth"), ("Final Boss", "Full reconstruction"),
]
LEVEL_XP = [20, 25, 30, 35, 40, 45, 50, 100]


def workspace_css():
    st.markdown("""
    <style>
    html, body, [class*="css"] { font-family: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }
    .stApp { background: #070B14; color: #E2E8F0; }
    .block-container { max-width: 1400px; padding: 2rem 2rem 4rem; }
    
    [data-testid="stSidebar"] { background: #0A101D; border-right: 1px solid rgba(255,255,255,0.05); }
    [data-testid="stSidebar"] > div:first-child { padding: 2rem 1.5rem; }
    [data-testid="stSidebarNav"] { display: none; }
    #MainMenu, footer, header { visibility: hidden; }
    
    h1, h2, h3, h4 { color: #F8F7FF; font-weight: 800; letter-spacing: -0.02em; }
    
    /* Sidebar Links */
    [data-testid="stSidebar"] a[data-testid="stPageLink-Nav"] { color: #94A3B8; border-radius: 8px; min-height: 40px; padding: 8px 12px; margin: 4px 0; font-size: 0.95rem; font-weight: 600; transition: all 150ms ease; }
    [data-testid="stSidebar"] a[data-testid="stPageLink-Nav"]:hover { background: rgba(255,255,255,0.05); color: #F8F7FF; }
    .nav-active { background: rgba(124, 77, 255, 0.1); border-left: 3px solid #7C4DFF; color: #F8F7FF !important; border-radius: 4px 8px 8px 4px; padding: 8px 12px; font-weight: 700; margin: 4px 0; }
    
    /* Buttons */
    .stButton > button { background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1); color: #CBD5E1; border-radius: 12px; font-weight: 600; font-size: 0.95rem; padding: 10px 20px; transition: all 150ms ease; }
    .stButton > button:hover { background: rgba(255,255,255,0.08); border-color: rgba(255,255,255,0.2); color: #F8F7FF; transform: translateY(-1px); box-shadow: 0 4px 12px rgba(0,0,0,0.2); }
    
    .stButton > button[kind="primary"] { background: #7C4DFF; border: none; color: #FFFFFF; }
    .stButton > button[kind="primary"]:hover { background: #8B5CF6; box-shadow: 0 8px 24px rgba(124, 77, 255, 0.3); }
    
    /* Blocks */
    .objective, .concept-block, .problem-block, .guided-practice-block { background: #0B1225; border: 1px solid rgba(255,255,255,0.05); padding: 32px; border-radius: 16px; margin: 24px 0; box-shadow: 0 4px 20px rgba(0,0,0,0.2); }
    .objective h3, .concept-block h3, .problem-block h3, .guided-practice-block h3 { margin-top: 0; margin-bottom: 16px; color: #F8F7FF; font-size: 1.4rem; }
    
    .concept-block { border-left: 4px solid #7C4DFF; }
    .problem-block { border-left: 4px solid #F87171; background: rgba(239, 68, 68, 0.05); }
    .guided-practice-block { border-left: 4px solid #34D399; background: rgba(52, 211, 153, 0.05); }
    
    .visual-block { background: #050811; border: 1px solid rgba(255,255,255,0.05); padding: 24px; border-radius: 12px; font-family: monospace; color: #A78BFA; overflow-x: auto; font-size: 0.9rem; line-height: 1.5; margin: 24px 0; box-shadow: inset 0 2px 10px rgba(0,0,0,0.5); }
    
    /* Navigation Rail */
    .rail-title { font-size: 0.8rem; font-weight: 800; letter-spacing: 0.15em; color: #64748B; margin-bottom: 8px; }
    .rail-mission { font-size: 1.2rem; font-weight: 700; color: #F8F7FF; margin-bottom: 24px; line-height: 1.4; }
    .level-static { background: transparent; border: 1px solid transparent; padding: 10px 16px; margin: 4px 0; font-weight: 600; color: #475569; font-size: 0.95rem; }
    
    .stRadio label { font-weight: 600 !important; font-size: 0.95rem !important; }
    
    /* Context Panel */
    .context-title { font-size: 0.75rem; font-weight: 800; letter-spacing: 0.15em; color: #64748B; margin-bottom: 16px; text-transform: uppercase; }
    .context-section { background: #0B1225; border: 1px solid rgba(255,255,255,0.05); border-radius: 12px; padding: 20px; margin-bottom: 16px; }
    .context-table { font-family: monospace; font-size: 0.85rem; color: #AAB3CC; line-height: 1.6; }
    
    </style>
    """, unsafe_allow_html=True)


def context_panel(story):
    sid = story["id"]
    st.markdown('<div class="context-title">CONTEXT PANEL</div>', unsafe_allow_html=True)
    if sid in (1, 6):
        st.markdown('''<div class="context-section"><div class="context-title">DATABASE</div><div class="context-table"><b>⌄ people</b><br>&nbsp;&nbsp;PK id<br>&nbsp;&nbsp;name<br>&nbsp;&nbsp;city<br><br><b>⌄ sightings</b><br>&nbsp;&nbsp;PK id<br>&nbsp;&nbsp;person_id<br>&nbsp;&nbsp;location<br>&nbsp;&nbsp;event_time<br><br><b>› locations</b></div></div>''', unsafe_allow_html=True)
    elif sid == 3:
        st.markdown('<div class="context-section"><div class="context-title">INDEX LAB</div><div class="context-table">○ No index<br>● <b>event_time</b><br>○ event_time + person_id<br><br>Estimated cost<br><b>18.4s → 0.03s</b></div></div>', unsafe_allow_html=True)
    elif sid in (2, 7):
        st.markdown('<div class="context-section"><div class="context-title">NODES</div><div class="context-table"><span class="node-online">●</span> Veridian-01<br><span class="node-online">●</span> Veridian-02<br><span class="node-wait">●</span> Veridian-03<br><br><b>NETWORK</b><br>A ─── B<br>&nbsp;&nbsp;✕<br>&nbsp;&nbsp;C</div></div>', unsafe_allow_html=True)
    elif sid in (5, 8):
        st.markdown('<div class="context-section"><div class="context-title">TRANSACTIONS</div><div class="context-table">T1 &nbsp;<span class="node-online">● Active</span><br>T2 &nbsp;<span class="node-wait">◐ Waiting</span><br><br><b>LOCKS</b><br>ROW: crate_42<br>X LOCK → T1</div></div>', unsafe_allow_html=True)
    elif sid in (4, 11):
        st.markdown('<div class="context-section"><div class="context-title">SCHEMA</div><div class="context-table"><b>people</b><br>person_id<br>name<br>city<br><br><b>events</b><br>event_id<br>person_id<br>event_time</div></div>', unsafe_allow_html=True)
    elif sid == 10:
        st.markdown('<div class="context-section"><div class="context-title">ENTITIES</div><div class="context-table"><b>Person</b><br><b>Location</b><br><b>Event</b><br><br><b>RELATIONSHIP</b><br>Person ─ sees ─ Location</div></div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="context-section"><div class="context-title">CASE FILE</div><div class="context-table">Evidence fragments: 12<br>Reliable sources: 3<br>Open contradictions: 1<br><br>Record each conclusion in your notes.</div></div>', unsafe_allow_html=True)
    st.divider()
    st.text_area("Scratch notes", key=f"workspace_notes_{sid}", height=130, placeholder="Record a clue…")


def render_episodic_page(story_id, story, data):
    configure_page(f"{story['title']} · DBMS Story Lab")
    workspace_css()
    episodes = data.get("episodes", [])
    completed_episodes = st.session_state.setdefault(f"completed_levels_{story_id}", set())
    active = st.session_state.setdefault(f"active_level_{story_id}", min(len(completed_episodes) + 1, len(episodes)))
    if active is None: active = min(len(completed_episodes) + 1, len(episodes))
    st.session_state[f"active_level_{story_id}"] = active
    
    st.session_state["last_story_id"] = story_id
    st.session_state["last_level"] = active
    save_progress()

    progress = len(completed_episodes)

    hide_context = st.session_state.get(f"hide_context_{story_id}", False)
    


    widths = [7, 3] if not hide_context else [10]
    columns = st.columns(widths)
    main = columns[0]
    context = columns[1] if not hide_context else None
    
    def render_rail():
        st.markdown(f'<div class="rail-title">{story["title"].upper()}</div><div class="rail-genre">{story["genre"]}</div><div class="rail-mission">{story["hook"]}</div><div class="rail-label">{len(episodes)} EPISODES</div>', unsafe_allow_html=True)
        available = list(range(1, min(progress + 2, len(episodes) + 1)))
        selected = st.radio("Episodes", available, index=max(0, min(active, len(available)) - 1), format_func=lambda n: f"{n:02d}  Episode {n}", label_visibility="collapsed", key=f"level_picker_{story_id}_{active}")
        if selected != active:
            st.session_state[f"active_level_{story_id}"] = selected; st.rerun()
        for number in range(1, len(episodes) + 1):
            if number in available: continue
            st.markdown(f'<div class="level-static locked"><b>🔒 {number:02d} &nbsp; Episode {number}</b></div>', unsafe_allow_html=True)
            
    sidebar('case', render_rail=render_rail, minimal=True)
    with main:
        if st.button("← Back to Journey", key=f"top_home_{story_id}"):
            st.session_state["last_story_id"] = None
            st.switch_page("pages/learning_map.py")
        st.markdown('<div class="workspace-main">', unsafe_allow_html=True)
        st.markdown(f'<div class="workspace-eyebrow">EPISODE {active:02d}</div><h1>{story["title"]}</h1>', unsafe_allow_html=True)
        episode_data = episodes[active - 1] if active <= len(episodes) else []
        
        episode_blocks = []
        if isinstance(episode_data, dict):
            if "title" in episode_data:
                st.markdown(f'<h2>{episode_data["title"]}</h2>', unsafe_allow_html=True)
            episode_blocks = episode_data.get("blocks", [])
        else:
            episode_blocks = episode_data

        
        def complete_current():
            levels = st.session_state.setdefault(f"completed_levels_{story_id}", set())
            current = st.session_state.get(f"active_level_{story_id}", 1)
            if current not in levels:
                levels.add(current)
                st.session_state.xp += 20
                if current == len(episodes):
                    st.session_state.xp += 30 # extra for finishing story
                    st.session_state.completed.add(story_id)
            st.session_state[f"active_level_{story_id}"] = min(current + 1, len(episodes))
            st.session_state["last_level"] = st.session_state[f"active_level_{story_id}"]
            save_progress()
            st.rerun()

        from field_notebook import advance_concept
        for i, block in enumerate(episode_blocks):
            btype = block.get("type")
            concept_id = block.get("concept_id")

            if btype == "story":
                st.markdown(f'<div class="objective"><h3>{block.get("title", "")}</h3><p>{block.get("content", block.get("text", ""))}</p></div>', unsafe_allow_html=True)
            elif btype == "problem":
                st.markdown(f'<div style="background:#FEF2F2; border-left:3px solid #EF4444; padding:15px 17px; color:#991B1B; margin: 10px 0; border-radius:0 8px 8px 0;"><b>Problem:</b> {block.get("text", "")}</div>', unsafe_allow_html=True)
            elif btype == "concept":
                if concept_id: advance_concept(concept_id, "INTRODUCED")
                st.markdown(f'<div style="background:#EFF6FF; border:1px solid #BFDBFE; padding:15px; border-radius:10px; margin: 15px 0;"><b>{block.get("title", "")}</b><br><span style="color:#1E3A8A; font-size: 0.9rem;">{block.get("summary", block.get("explanation", ""))}</span></div>', unsafe_allow_html=True)
                if "why_it_matters" in block:
                    st.markdown(f"**Why it matters:** {block['why_it_matters']}")
                if "analogy" in block:
                    st.markdown(f"**Analogy:** {block['analogy']}")
                if "technical_explanation" in block:
                    st.markdown(f"**Technical Detail:** {block['technical_explanation']}")
                if "remember" in block:
                    st.info(f"**Remember:** {block['remember']}")
            elif btype == "visual":
                if concept_id: advance_concept(concept_id, "VISUALIZED")
                if block.get("visual_type") == "image":
                    st.image(block.get("data"), use_column_width=True)
                elif block.get("visual_type") == "code":
                    st.code(block.get("data"), language="text")
                else:
                    st.markdown(f"```text\n{block.get('data')}\n```")
            elif btype == "worked_example":
                if concept_id: advance_concept(concept_id, "PRACTICED")
                st.markdown(f"### {block.get('title')}")
                for step in block.get("steps", []):
                    st.markdown(f"- {step}")
            elif btype == "reflection":
                st.info(f"🤔 **Reflection:** {block.get('question')}")

            elif btype == "query_correction":
                st.markdown(f"### 🐛 Debug the Query: {block.get('title', '')}")
                st.write(block.get('context', ''))
                st.error("The following query has an error:")
                st.code(block.get('broken_query', ''), language="sql")
                
                with st.form(key=f"qc_form_{story_id}_{active}_{i}"):
                    chosen = st.radio("What needs to be fixed?", block["options"], key=f"qc_radio_{story_id}_{active}_{i}")
                    submitted = st.form_submit_button("Submit Fix")
                    
                    if submitted:
                        if chosen == block["answer"]:
                            complete_current()
                        else:
                            we = block.get("wrong_explanations", {}).get(chosen)
                            if isinstance(we, dict):
                                st.error("❌ Incorrect Fix")
                                st.markdown(f"**WHY IT'S WRONG:** {we.get('why_wrong', '')}")
                            else:
                                st.error(we if we else "That doesn't quite fix it. Look closely at the execution order.")
                if i == active: break

            elif btype == "output_prediction":
                st.markdown(f"### 🔮 Predict the Output: {block.get('title', '')}")
                st.write(block.get('context', ''))
                st.code(block.get('query', ''), language="sql")
                
                with st.form(key=f"op_form_{story_id}_{active}_{i}"):
                    chosen = st.radio("What will this query return?", block["options"], key=f"op_radio_{story_id}_{active}_{i}")
                    submitted = st.form_submit_button("Predict")
                    
                    if submitted:
                        if chosen == block["answer"]:
                            complete_current()
                        else:
                            we = block.get("wrong_explanations", {}).get(chosen)
                            if isinstance(we, dict):
                                st.error("❌ Incorrect Prediction")
                                st.markdown(f"**WHY IT'S WRONG:** {we.get('why_wrong', '')}")
                            else:
                                st.error(we if we else "Not quite. Walk through the query step-by-step.")
                if i == active: break

            elif btype == "query_completion":
                st.markdown(f"### 🧩 Complete the Query: {block.get('title', '')}")
                st.write(block.get('context', ''))
                st.info("Fill in the missing part of the query:")
                st.code(block.get('partial_query', ''), language="sql")
                
                with st.form(key=f"comp_form_{story_id}_{active}_{i}"):
                    chosen = st.radio("Which snippet completes the query correctly?", block["options"], key=f"comp_radio_{story_id}_{active}_{i}")
                    submitted = st.form_submit_button("Complete Query")
                    
                    if submitted:
                        if chosen == block["answer"]:
                            complete_current()
                        else:
                            we = block.get("wrong_explanations", {}).get(chosen)
                            if isinstance(we, dict):
                                st.error("❌ Incorrect Snippet")
                                st.markdown(f"**WHY IT'S WRONG:** {we.get('why_wrong', '')}")
                            else:
                                st.error(we if we else "Not quite. Think about syntax and logical constraints.")
                if i == active: break

            elif btype == "data_explorer":
                st.markdown(f"### 🔍 Interactive Explorer: {block.get('title', '')}")
                st.write(block.get('context', ''))
                if block.get("scenario") == "update_anomaly":
                    import pandas as pd
                    st.markdown("**Payroll System**")
                    payroll_df = pd.DataFrame({"Name": ["John Smith"], "Address": ["Sector A"], "Salary": [50000]})
                    st.dataframe(payroll_df)
                    st.markdown("**Housing System**")
                    housing_df = pd.DataFrame({"Name": ["John Smith"], "Address": ["Sector B"], "Rent": [1200]})
                    st.dataframe(housing_df)
                    
                    if st.button("Attempt to Sync Systems"):
                        st.error("Error: No central synchronization mechanism exists in file-based systems. Data is permanently desynchronized.")
            elif btype == "debugger":
                st.markdown(f"### 🐛 Debugger: {block.get('title', '')}")
                st.warning(block.get('scenario', ''))
                
                if active not in completed_episodes:
                    with st.form(key=f"debug_form_{story_id}_{active}_{i}"):
                        chosen = st.radio("Diagnose the issue:", block["options"], key=f"debug_radio_{story_id}_{active}_{i}")
                        submitted = st.form_submit_button("Submit Diagnosis")
                        
                        if submitted:
                            if chosen == block["answer"]:
                                complete_current()
                            else:
                                st.error("❌ Incorrect Diagnosis")
                                st.info(block.get("explanation", ""))
                    break
                else:
                    st.success(f"✓ You diagnosed: {block['answer']}")
                    st.caption(block.get("explanation", ""))

            elif btype == "micro_challenge":
                st.markdown(f'<h3 style="margin-top: 20px;">Challenge</h3><p style="color:#344054;font-size:.95rem">{block.get("question", block.get("task", ""))}</p>', unsafe_allow_html=True)
                if active not in completed_episodes:
                    with st.form(key=f"mcq_form_{story_id}_{active}_{i}"):
                        st.radio("Select an option", block["options"], label_visibility="collapsed", key=f"mcq_radio_{story_id}_{active}_{i}")
                        submitted = st.form_submit_button("Submit answer")
                    if submitted:
                        chosen = st.session_state.get(f"mcq_radio_{story_id}_{active}_{i}")
                        if chosen == block["answer"]:
                            if concept_id: advance_concept(concept_id, "APPLIED")
                            complete_current()
                        else:
                            we = block.get("wrong_explanations", {}).get(chosen)
                            if isinstance(we, dict):
                                st.error("❌ Incorrect Answer")
                                st.markdown(f"**YOU CHOSE:** {chosen}")
                                st.markdown(f"**WHY IT'S WRONG:**<br>{we.get('why_wrong', '')}", unsafe_allow_html=True)
                                if we.get('confusing_with'):
                                    st.markdown(f"**YOU MAY BE CONFUSING:**<br>{we.get('confusing_with', '')}", unsafe_allow_html=True)
                                if we.get('remember'):
                                    st.info(f"**REMEMBER:** {we.get('remember', '')}")
                                if we.get('retry'):
                                    st.markdown(f"**TRY AGAIN:** {we.get('retry', '')}")
                            else:
                                st.error(we if we else "Not quite. Try again.")
                    break
                else:
                    st.success(f"✓ You answered: {block['answer']}")
                    if "explanation" in block:
                        st.caption(block["explanation"])
            elif btype == "guided_practice":
                if concept_id: advance_concept(concept_id, "PRACTICED")
                st.markdown(f"### {block.get('title', 'Guided Practice')}")
                if "context" in block:
                    st.markdown(f"<p>{block.get('context')}</p>", unsafe_allow_html=True)
                for step in block.get("steps", []):
                    st.markdown(f"- {step}")
                if "query" in block:
                    st.text_area("SQL Sandbox", value=block["query"], height=150, key=f"gp_{story_id}_{active}_{i}")
                if "question" in block:
                    st.markdown(f"**Question:** {block['question']}")
                    if active not in completed_episodes:
                        with st.form(key=f"gp_form_{story_id}_{active}_{i}"):
                            st.radio("Select an option", block["options"], label_visibility="collapsed", key=f"gp_radio_{story_id}_{active}_{i}")
                            submitted = st.form_submit_button("Verify")
                        if submitted:
                            chosen = st.session_state.get(f"gp_radio_{story_id}_{active}_{i}")
                            if chosen == block["answer"]:
                                complete_current()
                            else:
                                we = block.get("wrong_explanations", {}).get(chosen)
                                if isinstance(we, dict):
                                    st.error("❌ Incorrect Answer")
                                    st.markdown(f"**YOU CHOSE:** {chosen}")
                                    st.markdown(f"**WHY IT'S WRONG:**<br>{we.get('why_wrong', '')}", unsafe_allow_html=True)
                                    if we.get('confusing_with'):
                                        st.markdown(f"**YOU MAY BE CONFUSING:**<br>{we.get('confusing_with', '')}", unsafe_allow_html=True)
                                    if we.get('remember'):
                                        st.info(f"**REMEMBER:** {we.get('remember', '')}")
                                    if we.get('retry'):
                                        st.markdown(f"**TRY AGAIN:** {we.get('retry', '')}")
                                else:
                                    st.error(we if we else "Not quite. Review the steps and try again.")
                        break
                    else:
                        st.success(f"✓ You answered: {block['answer']}")

            elif btype == "sql_sandbox":
                st.markdown(f'<div class="concept-block" style="border-color: #3B82F6; background: rgba(59, 130, 246, 0.1);"><b>⚡ {block.get("title", "Interactive SQL Sandbox")}</b><p>{block.get("context", "")}</p></div>', unsafe_allow_html=True)
                
                if active not in completed_episodes:
                    query = st.text_area("Write your SQL here:", key=f"sql_input_{story_id}_{active}_{i}", height=150)
                    
                    col1, col2 = st.columns([1, 4])
                    with col1:
                        execute = st.button("Run Query ▶", key=f"sql_btn_{story_id}_{active}_{i}", type="primary")
                    with col2:
                        if block.get("hint") and st.button("Show Hint", key=f"hint_btn_{story_id}_{active}_{i}"):
                            st.info(block["hint"])
                    
                    if execute:
                        if not query.strip():
                            st.error("Please enter a query.")
                        else:
                            import sqlite3
                            import pandas as pd
                            try:
                                conn = sqlite3.connect(":memory:")
                                init_script = block.get("init_script", "")
                                if init_script:
                                    conn.executescript(init_script)
                                
                                user_df = pd.read_sql_query(query, conn)
                                st.markdown("**Your Result:**")
                                st.dataframe(user_df, use_container_width=True)
                                
                                solution_query = block.get("solution_query", "")
                                if solution_query:
                                    expected_df = pd.read_sql_query(solution_query, conn)
                                    
                                    user_df_str = user_df.astype(str)
                                    expected_df_str = expected_df.astype(str)
                                    
                                    if user_df_str.equals(expected_df_str):
                                        st.success("✅ Query Successful!")
                                        if block.get("explanation"):
                                            st.markdown(f'<div class="objective" style="border-left: 4px solid #10B981;">{block["explanation"]}</div>', unsafe_allow_html=True)
                                        # Use st.rerun() via callback to complete the episode
                                        def _on_sandbox_complete():
                                            complete_current()
                                        st.button("Complete Episode ›", key=f"proceed_sql_auto_{story_id}_{active}_{i}", on_click=_on_sandbox_complete, type="primary")
                                    else:
                                        st.error("❌ Results do not match the expected output.")
                                        with st.expander("Show Expected Output"):
                                            st.dataframe(expected_df, use_container_width=True)
                            except Exception as e:
                                st.error(f"SQL Error: {e}")
                            finally:
                                conn.close()
                    break
                else:
                    st.success(f"✓ SQL Sandbox complete.")
                    if "solution_query" in block:
                        with st.expander("Show Solution"):
                            st.code(block["solution_query"], language="sql")

            elif btype in ["interactive", "investigation"]:
                st.markdown(f'<h3 style="margin-top: 20px;">{"Investigation" if btype == "investigation" else "Challenge"}</h3><p style="color:#344054;font-size:.95rem">{block.get("task", "Apply your knowledge to solve the scenario.")}</p>', unsafe_allow_html=True)
                if active not in completed_episodes:
                    from challenges import render_story_challenge
                    def _on_complete():
                        if concept_id: advance_concept(concept_id, "MASTERED")
                        complete_current()
                    render_story_challenge(story, lambda sid: _on_complete(), show_progress=False)
                    break
                else:
                    st.success(f"✓ {'Investigation' if btype == 'investigation' else 'Interactive lab'} complete.")
        else:
            # This 'else' belongs to the 'for' loop. It executes if the loop didn't break (i.e. no uncompleted challenges).
            if active not in completed_episodes:
                st.markdown("<br>", unsafe_allow_html=True)
                if st.button("✓ Understood — Continue to next episode", key=f"read_continue_{story_id}_{active}", type="primary"):
                    complete_current()
                    
        if active in completed_episodes:
            # End of level recap
            st.markdown(f'''<div style="background:#F0FDF4; border:2px solid #BBF7D0; border-radius:20px; padding:24px; margin-top: 30px; box-shadow: 0 4px 12px rgba(21,128,61,0.08);">
            <div style="color:#15803D; font-size:.85rem; font-weight:800; letter-spacing:.11em; margin-bottom: 8px;">✓ EPISODE COMPLETE</div>
            <p style="margin:0 0 16px; color:#166534; font-size: 1.1rem;">You earned <b>+20 XP</b></p>
            </div>''', unsafe_allow_html=True)
            
            c1, c2 = st.columns([1, 2])
            with c1:
                if st.button("↻ Redo Exercise", key=f"redo_{story_id}_{active}", help="Erase progress for this level and try again."):
                    completed_episodes.discard(active)
                    st.rerun()

        st.markdown("<br><hr style='border:none; border-top:2px dashed #E2E8F0; margin: 30px 0;'>", unsafe_allow_html=True)
        b1, b2, b3 = st.columns([3, 4, 3])
        with b1:
            if active > 1:
                if st.button("← Previous", key=f"prev_{story_id}_{active}", use_container_width=True):
                    st.session_state[f"active_level_{story_id}"] = active - 1
                    st.rerun()
        with b3:
            if active < len(episodes) and active in completed_episodes:
                if st.button("Next →", key=f"next_{story_id}_{active}", use_container_width=True, type="primary"):
                    st.session_state[f"active_level_{story_id}"] = active + 1
                    st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)
def render_story_page(story_id):
    story = next(s for s in STORIES if s["id"] == story_id)
    level_list = LEVEL_CONTENT.get(story_id)
    if isinstance(level_list, dict) and level_list.get("format") == "episodic":
        return render_episodic_page(story_id, story, level_list)

    configure_page(f"{story['title']} · DBMS Story Lab")
    workspace_css()
    completed_levels = st.session_state.setdefault(f"completed_levels_{story_id}", set())
    active = st.session_state.setdefault(f"active_level_{story_id}", min(len(completed_levels) + 1, 8))
    
    st.session_state["last_story_id"] = story_id
    st.session_state["last_level"] = active
    save_progress()
    
    progress = len(completed_levels)

    hide_context = st.session_state.get(f"hide_context_{story_id}", False)
    
    widths = [7, 3] if not hide_context else [10]
    columns = st.columns(widths)
    main = columns[0]
    context = columns[1] if not hide_context else None
    
    def render_rail():
        st.markdown(f'<div class="rail-title">{story["title"].upper()}</div><div class="rail-genre">{story["genre"]}</div><div class="rail-mission">{story["hook"]}</div><div class="rail-label">8 LEVELS</div>', unsafe_allow_html=True)
        available = list(range(1, min(progress + 2, 9)))
        selected = st.radio("Mission levels", available, index=max(0, min(active, len(available)) - 1), format_func=lambda n: f"{n:02d}  {LEVELS[n-1][0]}", label_visibility="collapsed", key=f"level_picker_{story_id}_{active}")
        if selected != active:
            st.session_state[f"active_level_{story_id}"] = selected; st.rerun()
        for number, (name, skill) in enumerate(LEVELS, 1):
            if number in available: continue
            st.markdown(f'<div class="level-static locked"><b>🔒 {number:02d} &nbsp; {name}</b>{skill}</div>', unsafe_allow_html=True)
    sidebar('case', render_rail=render_rail, minimal=True)
    with main:
        if st.button("← Back to Journey", key=f"top_home_{story_id}"):
            st.session_state["last_story_id"] = None
            st.switch_page("pages/learning_map.py")
        st.markdown('<div class="workspace-main">', unsafe_allow_html=True)
        level_name, level_skill = LEVELS[active - 1]
        level_list = LEVEL_CONTENT.get(story_id) or [{}] * 8
        level_data = level_list[active - 1] if active <= len(level_list) else {}
        challenge_type = level_data.get("type", "interactive")

        st.markdown(
            f'<div class="workspace-eyebrow">LEVEL {active:02d} · {level_name.upper()} &nbsp;&nbsp; +{LEVEL_XP[active - 1]} XP</div>'
            f'<h1>{story["title"]}: {level_name}</h1>',
            unsafe_allow_html=True,
        )

        narrative = level_data.get("narrative", story["opening"])
        st.markdown(f'<div class="objective">{narrative}</div>', unsafe_allow_html=True)

        def complete_current(sid):
            levels = st.session_state.setdefault(f"completed_levels_{sid}", set())
            current = st.session_state.get(f"active_level_{sid}", 1)
            if current not in levels:
                levels.add(current)
                st.session_state.xp += LEVEL_XP[current - 1]
                if current == 8:
                    st.session_state.completed.add(sid)
            st.session_state[f"active_level_{sid}"] = min(current + 1, 8)
            save_progress()

        # ── Read level ─────────────────────────────────────────────────────────
        if challenge_type == "read":
            task_text = level_data.get("task", "")
            st.markdown(
                f'<p style="margin-top:1rem;color:#667085;font-size:.94rem">{task_text}</p>',
                unsafe_allow_html=True,
            )
            if active not in completed_levels:
                if st.button("✓ Understood — proceed", key=f"proceed_{story_id}_{active}"):
                    complete_current(story_id)
                    st.rerun()

        # ── MCQ level ──────────────────────────────────────────────────────────
        elif challenge_type == "mcq":
            task_text = level_data.get("task", "")
            st.markdown(
                f'<h3>Your question</h3>'
                f'<p style="margin:.5rem 0 1rem;color:#344054;font-size:.95rem">{task_text}</p>',
                unsafe_allow_html=True,
            )
            if active not in completed_levels:
                with st.form(key=f"mcq_form_{story_id}_{active}"):
                    st.radio(
                        "",
                        level_data.get("options", []),
                        label_visibility="collapsed",
                        key=f"mcq_radio_{story_id}_{active}",
                    )
                    submitted = st.form_submit_button("Submit answer")
                if submitted:
                    chosen = st.session_state.get(f"mcq_radio_{story_id}_{active}")
                    if chosen == level_data.get("answer"):
                        complete_current(story_id)
                        st.rerun()
                    else:
                        st.error(level_data.get("feedback_wrong", "Not quite. Try again."))

        # ── Interactive level (Final Boss) ──────────────────────────────────────
        else:
            task_text = level_data.get("task", "")
            st.markdown(
                f'<p style="margin-top:.5rem;color:#667085;font-size:.94rem">{task_text}</p>',
                unsafe_allow_html=True,
            )
            with st.expander("💡 Show hint"):
                st.markdown(
                    '<div class="hint-box">Start with the evidence that repeats. '
                    'Look for a pattern that connects the facts.</div>',
                    unsafe_allow_html=True,
                )
            with st.expander("Need another clue?"):
                st.write("The database is most useful when reasoning about related records as a set, not one at a time.")
            st.markdown('<h3>Interactive lab</h3>', unsafe_allow_html=True)
            render_story_challenge(story, complete_current, show_progress=False)

        # ── Success reveal ─────────────────────────────────────────────────────
        if active in completed_levels:
            if challenge_type == "mcq":
                reveal_text = level_data.get("feedback_correct", "Level complete.")
            elif challenge_type == "read":
                reveal_text = "Evidence logged. The investigation advances."
            else:
                reveal_text = f'What you discovered: <b>{story.get("primary", "")}</b>.'
            st.markdown(
                f'<div class="success-reveal"><b>✓ Level {active:02d} — {level_name} complete</b>'
                f'<br>{reveal_text}</div>',
                unsafe_allow_html=True,
            )
            
            # End of level recap
            st.markdown(f'''<div style="background:#F0FDF4; border:2px solid #BBF7D0; border-radius:20px; padding:24px; margin-top: 30px; box-shadow: 0 4px 12px rgba(21,128,61,0.08);">
            <div style="color:#15803D; font-size:.85rem; font-weight:800; letter-spacing:.11em; margin-bottom: 8px;">✓ LEVEL COMPLETE</div>
            <p style="margin:0 0 16px; color:#166534; font-size: 1.1rem;">You earned <b>+{LEVEL_XP[active - 1]} XP</b></p>
            </div>''', unsafe_allow_html=True)
            
            c1, c2 = st.columns([1, 2])
            with c1:
                if st.button("↻ Redo Exercise", key=f"redo_{story_id}_{active}", help="Erase progress for this level and try again."):
                    completed_levels.discard(active)
                    st.rerun()

        st.markdown("<br><hr style='border:none; border-top:2px dashed #E2E8F0; margin: 30px 0;'>", unsafe_allow_html=True)
        b1, b2, b3 = st.columns([3, 4, 3])
        with b1:
            if active > 1:
                if st.button("← Previous", key=f"prev_{story_id}_{active}", use_container_width=True):
                    st.session_state[f"active_level_{story_id}"] = active - 1
                    st.rerun()
        with b3:
            if active < 8 and active in completed_levels:
                if st.button("Next →", key=f"next_{story_id}_{active}", use_container_width=True, type="primary"):
                    st.session_state[f"active_level_{story_id}"] = active + 1
                    st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)
    if context:
        with context:
            if st.button("Hide panel  ›", key=f"hide_context_button_{story_id}"):
                st.session_state[f"hide_context_{story_id}"] = True; st.rerun()
            context_panel(story)
    else:
        if st.button("‹ Show context", key=f"show_context_button_{story_id}"):
            st.session_state[f"hide_context_{story_id}"] = False; st.rerun()
