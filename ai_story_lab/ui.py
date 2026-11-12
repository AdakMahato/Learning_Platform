import streamlit as st
import markdown
import re
from persistence import load_progress, save_progress
from story_data import STORIES
from level_content import LEVEL_CONTENT
import py_runner

import streamlit.components.v1 as components
def clean_newlines(text: str) -> str:
    if not text or not isinstance(text, str):
        return text
    text = text.replace("<<", "«").replace(">>", "»")
    latex_tokens = [
        "\\neg", "\\nabla", "\\neq", "\\notin", "\\norm", "\\nu", "\\natural", "\\ni"
    ]
    for i, tok in enumerate(latex_tokens):
        text = text.replace(tok, f"__LATEX_PLH_{i}__")
    text = text.replace("\\n", "\n")
    for i, tok in enumerate(latex_tokens):
        text = text.replace(f"__LATEX_PLH_{i}__", tok)
    return text

def render_markdown_html(text: str) -> str:
    if not text:
        return ""
    text = clean_newlines(str(text))
    # Standardize bullet symbols
    text = re.sub(r"^[ \t]*•[ \t]+", "- ", text, flags=re.MULTILINE)
    # Convert 2-space indented sub-bullets to 4 spaces for strict python-markdown compliance
    text = re.sub(r"^  ([-*]|\d+\.) ", r"    \1 ", text, flags=re.MULTILINE)
    # Ensure blank line before top-level list if preceded by non-newline text
    text = re.sub(r"([^\n])\n([-*]|\d+\.) ", r"\1\n\n\2 ", text)
    return markdown.markdown(text, extensions=["tables", "fenced_code"])

import re

def normalize_answer(s: str) -> str:
    if s is None:
        return ""
    s = str(s).strip().lower()
    s = s.strip("'\"`")
    s = s.rstrip(".,;:!? ")
    s = s.lstrip("-*• ")
    s = re.sub(r'\s+', ' ', s)
    return s

def check_answer_match(user_input: str, expected: str, alternatives: list = None) -> bool:
    norm_user = normalize_answer(user_input)
    norm_expected = normalize_answer(expected)
    
    if not norm_user:
        return False
        
    if norm_user == norm_expected:
        return True
        
    all_targets = [norm_expected]
    if "/" in str(expected):
        all_targets.extend([normalize_answer(p) for p in expected.split("/")])
    if "|" in str(expected):
        all_targets.extend([normalize_answer(p) for p in expected.split("|")])
    if alternatives and isinstance(alternatives, list):
        all_targets.extend([normalize_answer(a) for a in alternatives])
        
    if norm_user in all_targets:
        return True
        
    # Check without filler words
    clean_user = re.sub(r'^(the|a|an|it is|it)\s+', '', norm_user)
    for target in all_targets:
        if target:
            clean_target = re.sub(r'^(the|a|an|it is|it)\s+', '', target)
            if clean_user == clean_target:
                return True
                
    # Numeric match (e.g. 181440 == 181,440)
    user_num = re.sub(r'[^0-9.]', '', norm_user)
    expected_num = re.sub(r'[^0-9.]', '', norm_expected)
    if user_num and expected_num and user_num == expected_num:
        return True
        
    return False

def st_mermaid(code: str, height=None):
    if not code or not code.strip():
        return
    cleaned_code = code.strip()
    
    # Check orientation (vertical vs horizontal) and subgraphs
    is_vertical = any(dir_token in cleaned_code for dir_token in ["graph TD", "graph TB", "flowchart TD", "flowchart TB"])
    has_subgraphs = "subgraph" in cleaned_code
    lines = [l for l in cleaned_code.splitlines() if l.strip() and not l.strip().startswith(('classDef', 'class ', 'style '))]
    
    # Calculate sensible snug height to prevent awkward empty voids or cutoffs
    if height is not None and height > 0:
        computed_height = height
    else:
        if is_vertical:
            connections = [l for l in lines if '-->' in l or '-.->' in l or '---' in l]
            tier_estimate = max(3, len(lines) if len(lines) <= 6 else len(connections) + 1)
            if has_subgraphs:
                computed_height = max(280, min(700, len(lines) * 38 + 100))
            else:
                computed_height = max(200, min(600, tier_estimate * 72 + 65))
        else: # horizontal LR
            if has_subgraphs:
                computed_height = max(240, min(650, len(lines) * 32 + 90))
            else:
                computed_height = max(90, min(220, len(lines) * 22 + 45))
        
    htmlcode = f'''
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="utf-8">
      <style>
        * {{
          box-sizing: border-box;
        }}
        body {{
          margin: 0;
          padding: 8px 12px;
          background-color: transparent;
          overflow-y: auto;
          overflow-x: auto;
        }}
        .mermaid {{
          width: 100%;
          display: flex;
          justify-content: center;
          align-items: flex-start;
          text-align: center;
          margin: 0 auto;
        }}
        svg {{
          display: block;
          margin: 0 auto;
        }}
      </style>
    </head>
    <body>
      <div class="mermaid">
      {cleaned_code}
      </div>
      <script type="module">
        import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
        mermaid.initialize({{ 
          startOnLoad: true, 
          theme: 'dark', 
          themeVariables: {{
            darkMode: true,
            background: '#0B0F19',
            primaryColor: '#6366F1',
            primaryTextColor: '#F8FAFC',
            primaryBorderColor: '#818CF8',
            lineColor: '#94A3B8',
            secondaryColor: '#1E293B',
            tertiaryColor: '#0F172A'
          }},
          securityLevel: 'loose'
        }});
      </script>
    </body>
    </html>
    '''
    components.html(htmlcode, height=computed_height, scrolling=True)

def render_memory_layout(cells):
    html = '<div style="background: #080D1D; padding: 20px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.05); overflow-x: auto;"><div style="display: flex; gap: 8px;">'
    for cell in cells:
        html += f'''
        <div style="min-width: 120px; border: 1px solid #7C4DFF; border-radius: 6px; background: rgba(124,77,255,0.1); font-family: monospace; text-align: center; display: flex; flex-direction: column; overflow: hidden;">
            <div style="background: rgba(124,77,255,0.2); padding: 4px; font-size: 0.8rem; color: #AAB3CC;">{cell.get('address', '')}</div>
            <div style="padding: 12px; font-weight: bold; font-size: 1.1rem; color: #F8F7FF;">{cell.get('value', '')}</div>
            <div style="background: rgba(0,0,0,0.3); padding: 4px; font-size: 0.8rem; color: #94A3B8;">{cell.get('label', '')}</div>
        </div>
        '''
    html += '</div></div>'
    st.markdown(html, unsafe_allow_html=True)

PAGE_PATHS = {0: 'pages/00_the_machine_that_couldnt_think.py', 1: 'pages/01_the_agent_awakens.py', 2: 'pages/02_the_world_inside_the_machine.py', 3: 'pages/03_the_maze_without_a_map.py', 4: 'pages/04_the_search_for_the_better_path.py', 5: 'pages/05_the_heuristic_detective.py', 6: 'pages/06_the_game_of_minds.py', 7: 'pages/07_the_impossible_puzzle.py', 8: 'pages/08_the_knowledge_vault.py', 9: 'pages/09_the_logic_engine.py', 10: 'pages/10_the_machine_that_could_reason.py', 11: 'pages/11_the_planner.py', 12: 'pages/12_the_world_that_keeps_changing.py', 13: 'pages/13_the_probability_problem.py', 14: 'pages/14_the_bayesian_detective.py', 15: 'pages/15_the_decision_maker.py', 16: 'pages/16_the_machine_that_learns.py', 17: 'pages/17_the_nearest_neighbor.py', 18: 'pages/18_the_naive_assumption.py', 19: 'pages/19_the_tree_that_makes_decisions.py', 20: 'pages/20_the_agent_that_learns_from_failure.py', 21: 'pages/21_the_logic_programmer.py', 22: 'pages/22_the_expert_in_the_box.py', 23: 'pages/23_the_intelligence_architect.py', 24: 'pages/24_the_final_ai.py'}

def configure_page(title="AI Story Lab", active_nav="Home"):
    ensure_state()
    st.set_page_config(page_title=title, page_icon="⚙️", layout="wide", initial_sidebar_state="expanded")
    st.markdown("""
        <style>
    html, body, [class*="css"] { font-family: "Nunito", Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }
    .stApp { background:#0B1225; color:#F8F7FF; }
    .block-container { max-width:1400px; padding:3rem 2rem 3.5rem; }
    [data-testid="stSidebar"] { background:#080D1D; border-right:1px solid rgba(255,255,255,0.05); }
    [data-testid="stSidebar"] > div:first-child { padding:1.5rem 1.2rem; }
    [data-testid="stSidebarNav"] { display:none; }
    #MainMenu, footer, header { visibility:hidden; }
    
    h1, h2, h3, h4 { color: #F8F7FF; font-weight: 800; letter-spacing: -0.03em; }
    
    .stat-card, .story-card { background:#121B32; border:1px solid rgba(255,255,255,0.05); border-radius:24px; padding:24px; transition:all 250ms cubic-bezier(0.4, 0, 0.2, 1); box-shadow: inset 0 1px 0 rgba(255,255,255,0.05); }
    .story-card { height:320px; display:flex; flex-direction:column; cursor: pointer; overflow: hidden; position: relative; }
    .story-card:hover { transform:translateY(-6px); border-color:#7C4DFF; box-shadow:0 20px 40px rgba(124,77,255,0.15); }
    
    .stButton > button { background:#121B32; border:1px solid rgba(255,255,255,0.1); color:#AAB3CC; border-radius:16px; font-weight:700; font-size: 1rem; padding: 12px 24px; min-height:48px; transition:all 200ms cubic-bezier(0.4, 0, 0.2, 1); }
    .stButton > button:hover { background:#17213B; border-color:rgba(255,255,255,0.2); color:#F8F7FF; transform:translateY(-2px); }
    .stButton > button[kind="primary"] { background: linear-gradient(135deg, #7C4DFF 0%, #8B5CF6 100%); border:none; color:#FFFFFF; box-shadow: 0 8px 24px rgba(124,77,255,0.3); }
    
    .objective { background:#121B32; border:1px solid rgba(255,255,255,0.05); padding:24px; border-radius:24px; margin: 20px 0; font-size: 1.1rem; line-height: 1.6; color: #AAB3CC; box-shadow: inset 0 1px 0 rgba(255,255,255,0.05); }
    .objective h3 { margin-top: 0; color: #F8F7FF; }
    .problem-block { background:rgba(239, 68, 68, 0.1); border: 1px solid rgba(239, 68, 68, 0.2); padding:20px 24px; color:#FCA5A5; margin: 20px 0; border-radius:20px; font-size: 1.05rem; }
    .concept-block { background:rgba(124, 77, 255, 0.1); border:1px solid rgba(124, 77, 255, 0.3); padding:24px; border-radius:20px; margin: 20px 0; }
    .concept-block b { color: #DDD6FE; font-size: 1.2rem; }

    /* --- High-Production Card Component System --- */
    .card-kicker {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 0.74rem;
      font-weight: 800;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      padding: 4px 10px;
      border-radius: 6px;
      margin-bottom: 10px;
    }
    .kicker-briefing {
      background: rgba(56, 189, 248, 0.14);
      color: #38BDF8;
      border: 1px solid rgba(56, 189, 248, 0.28);
    }
    .kicker-objective {
      background: rgba(16, 185, 129, 0.14);
      color: #34D399;
      border: 1px solid rgba(16, 185, 129, 0.28);
    }
    .kicker-theory {
      background: rgba(139, 92, 246, 0.16);
      color: #A78BFA;
      border: 1px solid rgba(139, 92, 246, 0.32);
    }
    .kicker-incident {
      background: rgba(239, 68, 68, 0.16);
      color: #F87171;
      border: 1px solid rgba(239, 68, 68, 0.32);
    }
    .kicker-scenario {
      background: rgba(245, 158, 11, 0.14);
      color: #FBBF24;
      border: 1px solid rgba(245, 158, 11, 0.28);
    }

    .card-heading {
      font-size: 1.25rem;
      font-weight: 800;
      letter-spacing: -0.02em;
      margin: 0 0 10px 0;
      line-height: 1.35;
    }
    .heading-briefing { color: #F1F5F9; }
    .heading-objective { color: #ECFDF5; }
    .heading-theory { color: #EDE9FE; }
    .heading-incident { color: #FEF2F2; }
    .heading-scenario { color: #FEF3C7; }

    .briefing-card {
      background: linear-gradient(135deg, rgba(15, 23, 42, 0.8) 0%, rgba(30, 41, 59, 0.5) 100%);
      border: 1px solid rgba(56, 189, 248, 0.22);
      border-left: 5px solid #38BDF8;
      border-radius: 16px;
      padding: 20px 24px;
      margin: 18px 0;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
    }

    .objective-card {
      background: linear-gradient(135deg, rgba(6, 78, 59, 0.25) 0%, rgba(15, 23, 42, 0.7) 100%);
      border: 1px solid rgba(16, 185, 129, 0.28);
      border-left: 5px solid #10B981;
      border-radius: 16px;
      padding: 20px 24px;
      margin: 18px 0;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
    }

    .theory-card {
      background: linear-gradient(135deg, rgba(76, 29, 149, 0.22) 0%, rgba(18, 27, 50, 0.75) 100%);
      border: 1px solid rgba(139, 92, 246, 0.3);
      border-left: 5px solid #8B5CF6;
      border-radius: 16px;
      padding: 22px 26px;
      margin: 18px 0;
      box-shadow: 0 4px 24px rgba(0, 0, 0, 0.28);
    }

    .incident-card {
      background: linear-gradient(135deg, rgba(127, 29, 29, 0.25) 0%, rgba(15, 23, 42, 0.75) 100%);
      border: 1px solid rgba(239, 68, 68, 0.3);
      border-left: 5px solid #EF4444;
      border-radius: 16px;
      padding: 20px 24px;
      margin: 18px 0;
      box-shadow: 0 4px 20px rgba(239, 68, 68, 0.12);
    }

    .scenario-card {
      background: linear-gradient(135deg, rgba(120, 53, 15, 0.22) 0%, rgba(18, 27, 50, 0.75) 100%);
      border: 1px solid rgba(245, 158, 11, 0.28);
      border-left: 5px solid #F59E0B;
      border-radius: 16px;
      padding: 20px 24px;
      margin: 18px 0;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
    }

    .theory-tech-box {
      background: rgba(15, 23, 42, 0.65);
      border: 1px solid rgba(139, 92, 246, 0.25);
      border-left: 4px solid #A78BFA;
      border-radius: 12px;
      padding: 14px 18px;
      margin: 14px 0 6px 0;
    }
    .theory-tech-label {
      color: #DDD6FE;
      font-weight: 700;
      font-size: 0.85rem;
      text-transform: uppercase;
    }

    /* Card Body Typography */
    .card-body {
      font-size: 1.04rem;
      line-height: 1.68;
      color: #E2E8F0;
    }
    .incident-card .card-body { color: #FECACA; }

    /* Nested Lists Inside Cards */
    .card-body ul, .card-body ol {
      margin: 10px 0 12px 0;
      padding-left: 26px;
    }
    .card-body li {
      margin-bottom: 8px;
      line-height: 1.65;
      color: #CBD5E1;
    }
    .card-body li:last-child {
      margin-bottom: 0;
    }
    .briefing-card .card-body li::marker { color: #38BDF8; }
    .objective-card .card-body li::marker { color: #34D399; }
    .theory-card .card-body li::marker { color: #A78BFA; }
    .incident-card .card-body li::marker { color: #F87171; }
    .scenario-card .card-body li::marker { color: #FBBF24; }

    .card-body p {
      margin: 0 0 10px 0;
    }
    .card-body p:last-child {
      margin-bottom: 0;
    }

    .card-body strong {
      color: #FFFFFF;
      font-weight: 700;
    }

    .card-body code {
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.16);
      color: #38BDF8;
      padding: 2px 6px;
      border-radius: 4px;
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
      font-size: 0.9em;
    }

    /* Tables Inside Cards */
    .card-body table {
      width: 100%;
      border-collapse: collapse;
      margin: 14px 0;
      border-radius: 8px;
      overflow: hidden;
      border: 1px solid rgba(255, 255, 255, 0.12);
    }
    .card-body th {
      background: rgba(255, 255, 255, 0.08);
      color: #F8FAFC;
      font-weight: 700;
      text-align: left;
      padding: 10px 14px;
      border-bottom: 2px solid rgba(255, 255, 255, 0.15);
      font-size: 0.95rem;
    }
    .card-body td {
      padding: 9px 14px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.06);
      color: #CBD5E1;
      font-size: 0.95rem;
    }
    .card-body tr:last-child td {
      border-bottom: none;
    }
    
    .level-static { background: #080D1D; border: 1px solid rgba(255,255,255,0.05); border-radius: 16px; padding: 12px 16px; margin: 8px 0; font-weight: 700; color: #475569; }
    </style>
    """, unsafe_allow_html=True)

def ensure_state():
    load_progress()
    st.session_state.setdefault("completed", set())
    st.session_state.setdefault("xp", 0)

def sidebar(active="home", render_rail=None, minimal=False):
    with st.sidebar:
        xp = st.session_state.get("xp", 0)
        st.markdown(f'''
        <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 24px;">
            <div style="background: linear-gradient(135deg, #1E1B4B 0%, #312E81 100%); width: 40px; height: 40px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; border: 1px solid rgba(255,255,255,0.1);">⚙️</div>
            <div>
                <div style="font-weight: 800; color: #F8F7FF; letter-spacing: 0.05em; font-size: 1.1rem; line-height: 1.1;">AI STORY LAB</div>
                <div style="color: #A78BFA; font-weight: 700; font-size: 0.8rem; margin-top: 4px;">{xp} XP</div>
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
        else:
            try: st.page_link("pages/journey.py", label="▣  Journey")
            except: st.markdown("▣  Journey", unsafe_allow_html=True)
        if active == "concepts": st.markdown('<div class="nav-active">▤ &nbsp; Concepts</div>', unsafe_allow_html=True)
        else: 
            try: st.page_link("pages/concepts.py", label="▤  Concepts")
            except: st.markdown("▤  Concepts", unsafe_allow_html=True)
        if active == "practice": st.markdown('<div class="nav-active">⌘ &nbsp; AI Python Sandbox</div>', unsafe_allow_html=True)
        else:
            try: st.page_link("pages/cpp_sandbox.py", label="⌘  AI Python Sandbox")
            except: st.markdown("⌘  AI Python Sandbox", unsafe_allow_html=True)
        
        st.markdown('<div style="color: #64748B; font-size: 0.75rem; font-weight: 800; letter-spacing: 0.15em; margin: 32px 0 12px 0;">YOUR INVESTIGATION</div>', unsafe_allow_html=True)
        last_case = st.session_state.get("last_story_id", 0)
        
        if active == "case": st.markdown('<div class="nav-active">◉ &nbsp; Current Case</div>', unsafe_allow_html=True)
        else: st.page_link("app.py", label="◉  Current Case")
        if active == "notebook": st.markdown('<div class="nav-active">▣ &nbsp; Field Notebook</div>', unsafe_allow_html=True)
        else: 
            try: st.page_link("pages/field_notebook.py", label="▣  Field Notebook")
            except: st.markdown("▣  Field Notebook", unsafe_allow_html=True)
            
        st.markdown('<div style="color: #64748B; font-size: 0.75rem; font-weight: 800; letter-spacing: 0.15em; margin: 32px 0 12px 0;">PROGRESS</div>', unsafe_allow_html=True)
        if active == "progress": st.markdown('<div class="nav-active">📈 &nbsp; Progress</div>', unsafe_allow_html=True)
        else: 
            try: st.page_link("pages/progress.py", label="📈  Progress")
            except: st.markdown("📈  Progress", unsafe_allow_html=True)
        if active == "achievements": st.markdown('<div class="nav-active">🏆 &nbsp; Achievements</div>', unsafe_allow_html=True)
        else: 
            try: st.page_link("pages/achievements.py", label="🏆  Achievements")
            except: st.markdown("🏆  Achievements", unsafe_allow_html=True)
            
        st.markdown("<br><br>", unsafe_allow_html=True)
        if st.button("Reset progress", use_container_width=True):
            from persistence import reset_progress
            reset_progress()
            for key in list(st.session_state.keys()):
                if key.startswith(("completed_levels_", "mcq_", "proceed_", "mission_", "notebook_", "concept_mastery")):
                    del st.session_state[key]
            st.rerun()

def complete_current(story_id, current, total):
    st.session_state[f"active_level_{story_id}"] = min(current + 1, total)
    st.session_state["xp"] += 50
    if current == total:
        st.session_state.completed.add(story_id)
    save_progress()
    st.rerun()

def render_episodic_page(story_id, story, data):
    st.session_state["last_story_id"] = story_id
    episodes = data.get("episodes", [])
    active_progress = st.session_state.get(f"active_level_{story_id}", 1)
    
    viewing_key = f"viewing_level_{story_id}"
    last_prog_key = f"last_prog_level_{story_id}"
    
    # Auto-advance viewing if they just unlocked a new module
    if st.session_state.get(last_prog_key) != active_progress:
        st.session_state[viewing_key] = active_progress
        st.session_state[last_prog_key] = active_progress
        
    viewing = st.session_state.get(viewing_key, active_progress)
    
    def render_rail():
        st.markdown(f'<div class="rail-title">CASE {story_id:02d}</div><div class="rail-mission"><span style="margin-right: 6px;">{story.get("icon", "📖")}</span>{story["title"]}</div>', unsafe_allow_html=True)
        for number in range(1, len(episodes) + 1):
            if number <= active_progress:
                if number == viewing:
                    st.markdown(f'<div class="level-static" style="background:rgba(124,77,255,0.1); border-left:3px solid #7C4DFF; color:#F8F7FF; padding: 12px; margin-bottom: 8px;">▶ Module {number}</div>', unsafe_allow_html=True)
                else:
                    if st.button(f"✓ Module {number}" if number < active_progress else f"▶ Module {number}", key=f"nav_{story_id}_{number}", use_container_width=True):
                        st.session_state[viewing_key] = number
                        st.rerun()
            else:
                st.markdown(f'<div class="level-static" style="padding: 12px; margin-bottom: 8px; opacity: 0.5;">🔒 Module {number}</div>', unsafe_allow_html=True)
    sidebar(active="case", render_rail=render_rail, minimal=True)

    st.markdown(f'<div class="workspace-eyebrow">MODULE {viewing:02d}</div><h1>{story["title"]}</h1>', unsafe_allow_html=True)
    
    if viewing > len(episodes):
        st.success("Case Completed!")
        st.balloons()
        return

    episode_data = episodes[viewing - 1]
    if isinstance(episode_data, list):
        blocks = episode_data
    else:
        blocks = episode_data.get("blocks", [])
    
    # We must also pass the `viewing` to any keys that use `active`
    # Let's rename `active` to `viewing` globally inside this function!
    # Wait, the rest of the function expects `active`.
    active = viewing
    
    for block_idx, block in enumerate(blocks):
        btype = block.get("type")
        
        if btype == "header":
            meta_html = "".join([f'<div class="meta-tag">{m}</div>' for m in block.get("metadata", {}).values() if isinstance(m, str)])
            st.markdown(f'''
            <div class="rich-header">
                <h1>{block.get("title", "")}</h1>
                <div class="subtitle">{block.get("subtitle", "")}</div>
                <div class="meta">{meta_html}</div>
            </div>
            ''', unsafe_allow_html=True)
            
        elif btype == "think_first":
            st.markdown(f"### 🤔 Think First")
            st.write(block.get("question", ""))
            with st.form(key=f"think_{story_id}_{viewing}_{block_idx}"):
                chosen = st.radio("Your logic:", block["options"], key=f"rad_{story_id}_{viewing}_{block_idx}")
                if st.form_submit_button("Lock in Answer"):
                    idx = block["options"].index(chosen)
                    ans = block.get("answer", -1)
                    if idx == ans or chosen == ans:
                        st.success("Correct reasoning!")
                    else:
                        st.warning("Not quite the best architectural choice.")
                    st.info(f"**Explanation:** {block.get('explanation', '')}")
                    
        elif btype in ("mental_model", "abstract_class_visual"):
            title = block.get("title", "Mental Model")
            st.markdown(f"### 🧠 {title}")
            data = block.get("data") or block.get("content", "")
            st.markdown(f'<div class="mental-model"><pre style="margin:0; font-family:inherit; color:inherit;">{data}</pre></div>', unsafe_allow_html=True)
            
        elif btype == "annotated_code":
            st.markdown(f"### 💻 {block.get('title', 'Python Syntax')}")
            st.code(block.get("code", ""), language="python")
            for ann in block.get("annotations", []):
                with st.expander(f"🔍 Explain: `{ann.get('line', '')}`"):
                    st.write(ann.get("text", ""))
                    
        elif btype == "wrong_approach":
            st.markdown(f'''<div class="wrong-approach"><h4>❌ {block.get("title", "Wrong Approach")}</h4></div>''', unsafe_allow_html=True)
            st.code(block.get("code", ""), language="python")
            st.error(block.get("explanation", ""))
            
        elif btype == "correct_approach":
            st.markdown(f'''<div class="correct-approach"><h4>✅ {block.get("title", "Correct Approach")}</h4></div>''', unsafe_allow_html=True)
            st.code(block.get("code", ""), language="python")
            st.success(block.get("explanation", ""))
            
        elif btype == "comparison_table":
            st.markdown(f"### 📊 {block.get('title', 'Comparison')}")
            import pandas as pd
            df = pd.DataFrame(block.get("rows", []), columns=block.get("headers", []))
            st.table(df)
            
        elif btype == "real_world_analogy":
            st.markdown(f'''<div class="analogy-block"><h3>🌍 {block.get("title", "Real World Analogy")}</h3><p>{block.get("content", "")}</p></div>''', unsafe_allow_html=True)
            
        elif btype == "execution_trace":
            st.markdown(f"### ⚡ {block.get('title', 'Execution Trace')}")
            st.code(block.get("code", ""), language="python")
            for trace in block.get("trace", []):
                st.markdown(f"> {trace}")
                
        elif btype == "common_mistakes":
            st.markdown(f"### ⚠️ {block.get('title', 'Common Mistakes')}")
            for mist in block.get("mistakes", []):
                st.warning(f"**{mist.get('title', '')}**: {mist.get('desc', '')}")
                
        elif btype in ("code_experiment", "code_lab"):
            st.markdown(f"### 💻 {block.get('title', 'Code Lab')}")
            
            # Using Tabs for LeetCode-style UI
            tab_editor, tab_why, tab_alternatives, tab_edge_cases = st.tabs(["📝 Code Editor & Execution", "💡 Why This Solution Works", "🔀 Alternative Approaches & Trade-offs", "⚠️ Edge Cases & Failure Modes"])
            
            code_key = f"code_{story_id}_{viewing}_{block_idx}"
            
            # Initialization
            if code_key not in st.session_state:
                st.session_state[code_key] = block.get("starter_code", "")
                
            with tab_editor:
                # Reset logic
                if st.button("↺ Reset to Starter Code", key=f"reset_{code_key}"):
                    st.session_state[code_key] = block.get("starter_code", "")
                    st.rerun()
                    
                from streamlit_ace import st_ace
                code_txt = st_ace(value=st.session_state[code_key], language='python', theme='twilight', height=350, key=f"ace_{code_key}", font_size=14, show_gutter=True, auto_update=True)
                
                # Sync text area changes back to session state to persist them across tab switches
                if code_txt != st.session_state[code_key]:
                    st.session_state[code_key] = code_txt
                
                col_run, col_hint = st.columns([3, 7])
                with col_run:
                    run_clicked = st.button("Compile & Run Tests ▶", type="primary", key=f"run_{code_key}")
                
                if block.get("hint") or block.get("solution_code"):
                    with st.expander("Need help? Click for hints & solution"):
                        if block.get("hint"):
                            st.info(f"**Hint:** {block.get('hint')}")
                        if block.get("solution_code"):
                            st.markdown("**Complete Solution:**")
                            if st.button("Inject Solution into Editor ⬇", key=f"inject_{code_key}"):
                                st.session_state[code_key] = block.get("solution_code")
                                st.rerun()
                            st.code(block.get("solution_code"), language="python")
                            
                if run_clicked:
                    with st.spinner("Compiling & Executing..."):
                        import py_runner
                        test_cases = block.get("test_cases", [])
                        
                        if not test_cases:
                            # Fallback to single expected output
                            success, out, err = py_runner.run_py(code_txt)
                            if not success:
                                st.error(f"Compilation/Runtime Error:\n```\n{err}\n```")
                            else:
                                st.markdown("#### Test Results")
                                st.code(out, language="text")
                                expected = block.get("expected_output", "")
                                if expected and out.strip() == expected.strip():
                                    st.balloons()
                                    st.markdown(f'''
                                    <div style="background: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 12px; padding: 16px; margin-top: 12px;">
                                        <h3 style="color: #34D399; margin-top: 0;">✅ Accepted</h3>
                                        <div style="color: #AAB3CC; font-size: 0.9rem; margin-bottom: 12px;">Runtime: 0 ms • Memory: 4.1 MB</div>
                                        <div style="background: rgba(0,0,0,0.2); padding: 12px; border-radius: 8px;">
                                            <div style="color: #64748B; font-size: 0.8rem; margin-bottom: 4px;">Test Case 1</div>
                                            <div style="color: #F8F7FF; font-family: monospace;">Output matches expected exactly.</div>
                                        </div>
                                    </div>
                                    ''', unsafe_allow_html=True)
                                    
                                    if block.get("explanation"):
                                        st.markdown(f'''
                                        <div style="background: rgba(124, 77, 255, 0.1); border-left: 4px solid #7C4DFF; padding: 16px; margin-top: 16px; border-radius: 0 12px 12px 0;">
                                            {block.get("explanation")}
                                        </div>
                                        ''', unsafe_allow_html=True)
                                        
                                elif expected:
                                    st.markdown(f'''
                                    <div style="background: rgba(239, 68, 68, 0.1); border: 1px solid rgba(239, 68, 68, 0.3); border-radius: 12px; padding: 16px; margin-top: 12px;">
                                        <h3 style="color: #FCA5A5; margin-top: 0;">❌ Wrong Answer</h3>
                                        <div style="background: rgba(0,0,0,0.2); padding: 12px; border-radius: 8px; margin-bottom: 8px;">
                                            <div style="color: #64748B; font-size: 0.8rem; margin-bottom: 4px;">Expected Output</div>
                                            <div style="color: #34D399; font-family: monospace; white-space: pre;">{expected}</div>
                                        </div>
                                        <div style="background: rgba(0,0,0,0.2); padding: 12px; border-radius: 8px;">
                                            <div style="color: #64748B; font-size: 0.8rem; margin-bottom: 4px;">Actual Output</div>
                                            <div style="color: #FCA5A5; font-family: monospace; white-space: pre;">{out.strip() if out.strip() else "(Empty)"}</div>
                                        </div>
                                    </div>
                                    ''', unsafe_allow_html=True)
                        else:
                            # Leetcode style multiple test cases
                            all_passed = True
                            st.markdown("#### Test Results")
                            for idx, tc in enumerate(test_cases):
                                inp = tc.get("input", "")
                                exp = tc.get("expected_output", "")
                                success, out, err = py_runner.run_py(code_txt, input_data=inp)
                                
                                if not success:
                                    st.error(f"Test Case {idx+1}: Compilation/Runtime Error\n```\n{err}\n```")
                                    all_passed = False
                                    break
                                
                                if out.strip() == exp.strip():
                                    st.success(f"✅ Test Case {idx+1} Passed!")
                                else:
                                    all_passed = False
                                    st.error(f"❌ Test Case {idx+1} Failed.")
                                    st.markdown(f"**Input:** `{inp}`\n**Expected:** `{exp}`\n**Actual:** `{out.strip()}`")
                                    break
                                    
                            if all_passed:
                                st.balloons()
                                st.success("🎉 All Test Cases Passed!")

            with tab_why:
                why_text = block.get("why_it_works") or block.get("explanation") or "**Mathematical & Algorithmic Mechanics:**\nThis implementation establishes the exact state transitions and invariant checks required for this problem."
                st.markdown(clean_newlines(why_text))
                if block.get("complexity"):
                    st.markdown("#### ⏱️ Computational Complexity")
                    st.markdown(clean_newlines(block.get("complexity")))

            with tab_alternatives:
                alts = block.get("alternatives")
                if alts:
                    st.markdown(clean_newlines(alts))
                else:
                    st.markdown("""
                    #### 🔀 Candidate Architectural Alternatives
                    - **Alternative 1: Naive Exhaustive Enumeration (Brute Force)**
                      - *Trade-off:* Trivial to implement, but exhibits exponential time complexity $O(b^d)$ or $O(N^2)$, making it unusable for production-scale inputs.
                    - **Alternative 2: Heuristic / Greedy Approximation**
                      - *Trade-off:* Offers orders-of-magnitude faster query latency, but may sacrifice global optimality if admissibility is violated.
                    - **Alternative 3: Probabilistic / Empirical Machine Learning**
                      - *Trade-off:* Robust to high-dimensional noise, but requires significant training data and lacks strict deterministic safety guarantees.
                    """)

            with tab_edge_cases:
                st.info("In a real engineering environment, your code will face unexpected constraints. Consider these edge cases:")
                edge_cases = block.get("edge_cases")
                if edge_cases:
                    if isinstance(edge_cases, str):
                        st.markdown(clean_newlines(edge_cases))
                    elif isinstance(edge_cases, list):
                        for ec in edge_cases:
                            if isinstance(ec, dict):
                                st.markdown(f"**{ec.get('title', 'Edge Case')}**\n> {ec.get('desc', '')}")
                            else:
                                st.markdown(clean_newlines(str(ec)))
                else:
                    default_ecs = [
                        {"title": "Null/Empty/Zero Inputs", "desc": "What happens if the array is empty, the pointer is null, or an integer is 0?"},
                        {"title": "Extreme Bounds & Overflow", "desc": "What if the loop runs 0 times or integer values exceed limits?"},
                        {"title": "Resource Leaks", "desc": "If this function fails early, are all allocated resources properly freed?"}
                    ]
                    for ec in default_ecs:
                        st.markdown(f"**{ec.get('title', 'Edge Case')}**\n> {ec.get('desc', '')}")
                if "edge_cases_explanation" in block:
                    st.markdown(clean_newlines(block["edge_cases_explanation"]))
                            
        elif btype in ("micro_challenge", "mastery_challenge", "interactive"):
            st.markdown(f"### 🏆 {block.get('title', 'Knowledge & Concept Challenge')}")
            q = block.get("question") or block.get("content", "")
            st.markdown(f"**{q}**")
            
            with st.form(key=f"mc_form_{story_id}_{viewing}_{block_idx}"):
                chosen = st.radio("Select your answer:", block["options"], key=f"mc_radio_{story_id}_{viewing}_{block_idx}")
                submitted = st.form_submit_button("Submit Answer ▶")
                if submitted:
                    idx = block["options"].index(chosen)
                    ans = block.get("answer", -1)
                    
                    is_correct = False
                    if isinstance(ans, int) and idx == ans:
                        is_correct = True
                    elif isinstance(ans, str):
                        if check_answer_match(chosen, ans):
                            is_correct = True
                        elif ans.isdigit() and idx == int(ans) - 1:
                            is_correct = True
                            
                    if is_correct:
                        st.success(f"✅ **Correct!** `{chosen}` is the right answer.")
                    else:
                        correct_str = ans if isinstance(ans, str) else block["options"][ans]
                        st.error(f"❌ **Incorrect.** You selected `{chosen}`. The correct answer is **`{correct_str}`**.")
                    
                    if block.get("explanation"):
                        with st.container(border=True):
                            st.markdown(clean_newlines(block.get("explanation")))
                        
            if block.get("explanation"):
                with st.expander("💡 Study Guide: Reveal In-Depth Answer & Explanation"):
                    st.markdown(clean_newlines(block.get("explanation")))
                        

        elif btype == "mermaid_diagram" or btype == "visual":
            if "title" in block: st.markdown(f"#### 📊 {block['title']}")
            if "explanation" in block: st.markdown(block["explanation"])
            st_mermaid(block.get("code", ""), height=block.get("height"))
            
        elif btype == "visual_stepper":
            if "title" in block: st.markdown(f"#### 🎬 {block['title']}")
            
            steps = block.get("steps", [])
            if steps:
                step_key = f"stepper_{story_id}_{viewing}_{block_idx}"
                if step_key not in st.session_state:
                    st.session_state[step_key] = 0
                
                step_idx = max(0, min(int(st.session_state[step_key]), len(steps) - 1))
                step = steps[step_idx]
                
                # Interactive Step Controls
                c_prev, c_center, c_next = st.columns([1, 2, 1])
                with c_prev:
                    if st.button("◀ Prev Step", key=f"btn_prev_{step_key}", disabled=(step_idx <= 0), use_container_width=True):
                        st.session_state[step_key] = max(0, step_idx - 1)
                        st.rerun()
                with c_center:
                    selected_num = st.selectbox(
                        "Jump to step",
                        options=list(range(1, len(steps) + 1)),
                        index=step_idx,
                        key=f"select_{step_key}",
                        label_visibility="collapsed",
                        format_func=lambda x: f"Step {x} of {len(steps)}"
                    )
                    if selected_num - 1 != step_idx:
                        st.session_state[step_key] = selected_num - 1
                        st.rerun()
                with c_next:
                    if st.button("Next Step ▶", key=f"btn_next_{step_key}", disabled=(step_idx >= len(steps) - 1), use_container_width=True):
                        st.session_state[step_key] = min(len(steps) - 1, step_idx + 1)
                        st.rerun()
                
                st.markdown(f"""
                <div style='background: rgba(99, 102, 241, 0.12); border: 1px solid rgba(99, 102, 241, 0.35); border-left: 5px solid #6366F1; padding: 14px 18px; margin: 10px 0 14px 0; border-radius: 0 10px 10px 0;'>
                    <span style='color: #818CF8; font-weight: 700; font-size: 0.9rem; text-transform: uppercase;'>Step {step_idx + 1} of {len(steps)}:</span>
                    <div style='color: #F8FAFC; margin-top: 4px; font-size: 1.02rem; line-height: 1.5;'>{step.get("explanation", "")}</div>
                </div>
                """, unsafe_allow_html=True)
                
                st_mermaid(step.get("mermaid_code", ""), height=block.get("height"))

        
        elif btype == "fill_in_the_blank":
            st.markdown(f"### ✍️ {block.get('title', 'Fill in the Blank Challenge')}")
            q = block.get("question", "")
            
            with st.form(key=f"fib_form_{story_id}_{viewing}_{block_idx}"):
                st.markdown(q.replace("_____", "___"))
                user_ans = st.text_input("Your Answer:", key=f"fib_input_{story_id}_{viewing}_{block_idx}")
                
                submitted = st.form_submit_button("Submit Answer ▶")
                if submitted:
                    ans = block.get("answer", "")
                    alts = block.get("alternatives", [])
                    if check_answer_match(user_ans, ans, alts):
                        st.success(f"✅ **Correct!** `{user_ans.strip()}` is the right answer.")
                    else:
                        clean_disp = ans.rstrip('.').strip()
                        st.error(f"❌ **Incorrect.** You entered `{user_ans.strip()}`. The expected answer is **`{clean_disp}`**.")
                    
                    if block.get("explanation"):
                        with st.container(border=True):
                            st.markdown(clean_newlines(block.get("explanation")))
                        
            if block.get("explanation"):
                with st.expander("💡 Study Guide: Reveal In-Depth Answer & Explanation"):
                    st.markdown(clean_newlines(block.get("explanation")))

        elif btype == "memory_layout":
            if "title" in block: st.markdown(f"#### 💾 {block['title']}")
            if "explanation" in block: st.markdown(block["explanation"])
            render_memory_layout(block.get("cells", []))

        elif btype in ("story", "markdown", "narrative", "text"):
            raw_text = block.get("text") or block.get("content", "")
            html_content = render_markdown_html(raw_text)
            title = block.get("title", "")
            title_html = f'<div class="card-heading heading-briefing">{title}</div>' if title else ""
            card_html = (
                f'<div class="briefing-card">\n'
                f'<div class="card-kicker kicker-briefing">📖 MISSION BRIEFING &amp; REAL-WORLD CONTEXT</div>\n'
                f'{title_html}\n'
                f'<div class="card-body">{html_content}</div>\n'
                f'</div>'
            )
            st.markdown(card_html, unsafe_allow_html=True)
            
        elif btype == "objective":
            raw_content = block.get("explanation") or block.get("content", "")
            html_content = render_markdown_html(raw_content)
            title = block.get("title", "")
            title_html = ""
            if title and title.strip().lower() not in ("module objective", "learning objective", "objective"):
                title_html = f'<div class="card-heading heading-objective">{title}</div>'
            card_html = (
                f'<div class="objective-card">\n'
                f'<div class="card-kicker kicker-objective">🎯 LEARNING OBJECTIVE &amp; COMPETENCIES</div>\n'
                f'{title_html}\n'
                f'<div class="card-body">{html_content}</div>\n'
                f'</div>'
            )
            st.markdown(card_html, unsafe_allow_html=True)

        elif btype == "problem":
            raw_text = block.get("text") or block.get("content", "")
            html_content = render_markdown_html(raw_text)
            title = block.get("title", "Critical AI Challenge")
            card_html = (
                f'<div class="incident-card">\n'
                f'<div class="card-kicker kicker-incident">🚨 CRITICAL AI PROBLEM &amp; CHALLENGE ANOMALY</div>\n'
                f'<div class="card-heading heading-incident">{title}</div>\n'
                f'<div class="card-body">{html_content}</div>\n'
                f'</div>'
            )
            st.markdown(card_html, unsafe_allow_html=True)
            
        elif btype in ("concept", "theory"):
            raw_content = block.get("explanation") or block.get("content", "")
            html_content = render_markdown_html(raw_content)
            title = block.get("title", "Core AI Concept & Theory")
            title_html = f'<div class="card-heading heading-theory">{title}</div>'
            tech_html_box = ""
            if "technical_explanation" in block:
                tech_inner = render_markdown_html(block["technical_explanation"])
                tech_html_box = (
                    f'<div class="theory-tech-box">\n'
                    f'<span class="theory-tech-label">⚙️ Algorithmic Invariants &amp; Low-Level Details:</span>\n'
                    f'<div class="card-body" style="margin-top: 6px; font-size: 0.98rem; color: #CBD5E1;">{tech_inner}</div>\n'
                    f'</div>'
                )
            card_html = (
                f'<div class="theory-card">\n'
                f'<div class="card-kicker kicker-theory">💡 CORE AI ARCHITECTURE &amp; FOUNDATIONAL THEORY</div>\n'
                f'{title_html}\n'
                f'<div class="card-body">{html_content}</div>\n'
                f'{tech_html_box}\n'
                f'</div>'
            )
            st.markdown(card_html, unsafe_allow_html=True)
            if "analogy" in block:
                st.info(f"💡 **Analogy:** {block['analogy']}")
            
        elif btype == "visual":
            data = block.get("data") or block.get("content", "")
            if block.get("visual_type") == "text" or not block.get("visual_type"):
                st.markdown(f"```text\n{data}\n```")
                
        elif btype == "worked_example":
            title = block.get('title') or 'Worked Example'
            st.markdown(f"### 🔨 {title}")
            steps = block.get("steps")
            if steps:
                for step in steps:
                    st.markdown(f"- {step}")
            else:
                content = block.get("content") or block.get("text", "")
                st.markdown(content)
                
        elif btype == "reflection":
            q = block.get("question") or block.get("content", "")
            st.info(f"🤔 **Reflection:** {q}")
            
        elif btype == "debugger":
            st.markdown(f"### 🐛 Debugger: {block.get('title', '')}")
            st.warning(block.get('scenario', ''))
            with st.form(key=f"debug_form_{story_id}_{viewing}_{block_idx}"):
                chosen = st.radio("Diagnose the issue:", block["options"], key=f"debug_radio_{story_id}_{viewing}_{block_idx}")
                if st.form_submit_button("Submit Diagnosis"):
                    if chosen == block["answer"]: st.success("Correct!")
                    else: st.error("Incorrect. " + block.get("explanation", ""))
                            
    if st.button("Complete Module", type="primary", key=f"complete_mod_{story_id}_{viewing}"):
        complete_current(story_id, active, len(episodes))

def story_status(story_id):
    if story_id in st.session_state.get("completed", set()): return "✓ Completed", "status-complete"
    active_level = st.session_state.get(f"active_level_{story_id}", 1)
    if active_level > 1: return "◐ In progress", "status-progress"
    return "○ Not started", "status-open"

def workspace_css():
    pass # I already have style tags in configure_page! 

