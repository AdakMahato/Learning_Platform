import streamlit as st
import streamlit.components.v1 as components
import sys
import os
import re
import markdown

from persistence import load_progress, save_progress
from story_data import STORIES
import py_runner

def clean_newlines(text: str) -> str:
    if not text or not isinstance(text, str):
        return text
    # Convert UML stereotype delimiters << and >> to standard typographic guillemets « and »
    # so they render safely in HTML/Markdown without being swallowed as unknown tags
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

from story_data import STORIES, get_page_path

PAGE_PATHS = {s["id"]: get_page_path(s["id"], s["title"]) for s in STORIES}

def configure_page(title="Cloud Story Lab", active_nav="Home"):
    ensure_state()
    st.set_page_config(page_title=title, page_icon="💻", layout="wide", initial_sidebar_state="expanded")
    workspace_css()

def workspace_css():
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
    .rail-title { color: #64748B; font-size: 0.75rem; font-weight: 800; letter-spacing: 0.15em; margin-bottom: 4px; }
    .rail-mission { color: #F8F7FF; font-weight: 800; font-size: 1.05rem; margin-bottom: 20px; line-height: 1.3; }
    .nav-active { background: rgba(124,77,255,0.15); border-left: 3px solid #7C4DFF; color: #F8F7FF; padding: 10px 14px; border-radius: 8px; font-weight: 700; }
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
            <div style="background: linear-gradient(135deg, #0C4A6E 0%, #0369A1 100%); width: 40px; height: 40px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; border: 1px solid rgba(56,189,248,0.3);">☁️</div>
            <div>
                <div style="font-weight: 800; color: #F8F7FF; letter-spacing: 0.05em; font-size: 1.1rem; line-height: 1.1;">CLOUD STORY LAB</div>
                <div style="color: #38BDF8; font-weight: 700; font-size: 0.8rem; margin-top: 4px;">{xp} XP</div>
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
        
        st.markdown('<div style="color: #64748B; font-size: 0.75rem; font-weight: 800; letter-spacing: 0.15em; margin: 32px 0 12px 0;">YOUR INVESTIGATION</div>', unsafe_allow_html=True)
        if active == "case": st.markdown('<div class="nav-active">◉ &nbsp; Current Case</div>', unsafe_allow_html=True)
        else: st.page_link("app.py", label="◉  Current Case")
            
        st.markdown('<div style="color: #64748B; font-size: 0.75rem; font-weight: 800; letter-spacing: 0.15em; margin: 32px 0 12px 0;">PROGRESS</div>', unsafe_allow_html=True)
        completed_count = len(st.session_state.get("completed", set()))
        pct = int((completed_count / max(1, len(STORIES))) * 100)
        st.markdown(f'''
        <div style="background: rgba(255,255,255,0.05); padding: 12px 16px; border-radius: 12px; margin-bottom: 16px;">
            <div style="display: flex; justify-content: space-between; font-size: 0.8rem; font-weight: 700; color: #AAB3CC; margin-bottom: 6px;">
                <span>Curriculum</span>
                <span>{completed_count}/{len(STORIES)} Cases ({pct}%)</span>
            </div>
            <div style="width: 100%; height: 6px; background: rgba(255,255,255,0.1); border-radius: 3px; overflow: hidden;">
                <div style="width: {pct}%; height: 100%; background: #7C4DFF;"></div>
            </div>
        </div>
        ''', unsafe_allow_html=True)
            
        st.markdown("<br><br>", unsafe_allow_html=True)
        if st.button("Reset progress", use_container_width=True):
            from persistence import reset_progress
            reset_progress()
            for key in list(st.session_state.keys()):
                if key.startswith(("completed_levels_", "mcq_", "proceed_", "mission_", "fib_")):
                    del st.session_state[key]
            st.rerun()

def complete_current(story_id, current, total):
    st.session_state[f"active_level_{story_id}"] = min(current + 1, total)
    st.session_state["xp"] += 50
    if current == total:
        st.session_state.completed.add(story_id)
    save_progress()
    st.rerun()

def story_status(story_id):
    completed = st.session_state.get("completed", set())
    if story_id in completed:
        return "Completed", "completed"
    active_level = st.session_state.get(f"active_level_{story_id}", 1)
    if active_level > 1:
        return f"In progress (Mod {active_level})", "progress"
    return "Not started", "locked"

def render_episodic_page(story_id, story, data):
    st.session_state["last_story_id"] = story_id
    episodes = data.get("episodes", [])
    active_progress = st.session_state.get(f"active_level_{story_id}", 1)
    
    viewing_key = f"viewing_level_{story_id}"
    last_prog_key = f"last_prog_level_{story_id}"
    
    if st.session_state.get(last_prog_key) != active_progress:
        st.session_state[viewing_key] = active_progress
        st.session_state[last_prog_key] = active_progress
        
    viewing = st.session_state.get(viewing_key, active_progress)
    
    def render_rail():
        st.markdown(f'<div class="rail-title">CASE {story_id:02d}</div><div class="rail-mission"><span style="margin-right: 6px;">{story.get("icon", "💻")}</span>{story["title"]}</div>', unsafe_allow_html=True)
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

    sidebar(active="case", render_rail=render_rail)
    
    if not episodes:
        st.warning("No curriculum modules loaded for this case yet.")
        return

    current_ep = episodes[viewing - 1]
    
    st.markdown(f"# {current_ep.get('title', f'Module {viewing}')}")
    st.markdown(f"**Case {story_id:02d}: {story['title']}** • *Primary Focus: {story.get('primary', 'Core Architecture')}*")
    st.markdown("---")

    blocks = current_ep.get("blocks", [])
    for block_idx, block in enumerate(blocks):
        render_block(block, story_id, viewing, block_idx)

    st.markdown("<br><br>", unsafe_allow_html=True)
    col_c1, col_c2, col_c3 = st.columns([1, 2, 1])
    with col_c1:
        if viewing < len(episodes):
            is_unlocked = viewing < active_progress
            btn_label = "Proceed to Next Module ▶" if is_unlocked else "Complete Module & Unlock Next ▶"
            if st.button(btn_label, type="primary", key=f"next_btn_{story_id}_{viewing}", use_container_width=True):
                if not is_unlocked:
                    complete_current(story_id, viewing, len(episodes))
                st.session_state[viewing_key] = viewing + 1
                st.rerun()
        else:
            is_done = story_id in st.session_state.get("completed", set())
            btn_label = "Review Complete Investigation" if is_done else "Complete Case Investigation 🏆"
            if st.button(btn_label, type="primary", key=f"finish_case_{story_id}", use_container_width=True):
                if not is_done:
                    complete_current(story_id, viewing, len(episodes))
                    st.balloons()
                st.switch_page("app.py")

def render_block(block, story_id, viewing, block_idx):
    btype = block.get("type")
    
    if btype in ("story", "markdown", "narrative", "text"):
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
        
    elif btype in ("concept", "theory"):
        raw_content = block.get("explanation") or block.get("content", "")
        html_content = render_markdown_html(raw_content)
        title = block.get("title", "Core Architecture & Theory")
        title_html = f'<div class="card-heading heading-theory">{title}</div>'
        tech_html_box = ""
        if "technical_explanation" in block:
            tech_inner = render_markdown_html(block["technical_explanation"])
            tech_html_box = (
                f'<div class="theory-tech-box">\n'
                f'<span class="theory-tech-label">⚙️ Architectural Invariants &amp; Low-Level Details:</span>\n'
                f'<div class="card-body" style="margin-top: 6px; font-size: 0.98rem; color: #CBD5E1;">{tech_inner}</div>\n'
                f'</div>'
            )
        card_html = (
            f'<div class="theory-card">\n'
            f'<div class="card-kicker kicker-theory">💡 CORE ARCHITECTURE &amp; FOUNDATIONAL THEORY</div>\n'
            f'{title_html}\n'
            f'<div class="card-body">{html_content}</div>\n'
            f'{tech_html_box}\n'
            f'</div>'
        )
        st.markdown(card_html, unsafe_allow_html=True)
        
    elif btype == "problem":
        raw_text = block.get("text") or block.get("content", "")
        html_content = render_markdown_html(raw_text)
        title = block.get("title", "Critical Architectural Incident")
        card_html = (
            f'<div class="incident-card">\n'
            f'<div class="card-kicker kicker-incident">🚨 CRITICAL ARCHITECTURAL INCIDENT &amp; FAILURE ANOMALY</div>\n'
            f'<div class="card-heading heading-incident">{title}</div>\n'
            f'<div class="card-body">{html_content}</div>\n'
            f'</div>'
        )
        st.markdown(card_html, unsafe_allow_html=True)

    elif btype in ("mermaid_diagram", "visual"):
        if "title" in block: st.markdown(f"#### 📊 {block['title']}")
        if "explanation" in block: st.markdown(clean_newlines(block["explanation"]))
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
            
            step_html = (
                f'<div style="background: rgba(99, 102, 241, 0.12); border: 1px solid rgba(99, 102, 241, 0.35); border-left: 5px solid #6366F1; padding: 14px 18px; margin: 10px 0 14px 0; border-radius: 0 10px 10px 0;">\n'
                f'<span style="color: #818CF8; font-weight: 700; font-size: 0.9rem; text-transform: uppercase;">Step {step_idx + 1} of {len(steps)}:</span>\n'
                f'<div style="color: #F8FAFC; margin-top: 4px; font-size: 1.02rem; line-height: 1.5;">{step.get("explanation", "")}</div>\n'
                f'</div>'
            )
            st.markdown(step_html, unsafe_allow_html=True)
            st_mermaid(step.get("mermaid_code", ""), height=block.get("height"))

    elif btype in ("micro_challenge", "mastery_challenge", "interactive"):
        st.markdown(f"### 🏆 {block.get('title', 'Knowledge & Concept Challenge')}")
        q = block.get("question") or block.get("content", "")
        st.markdown(f"**{clean_newlines(q)}**")
        
        with st.form(key=f"mc_form_{story_id}_{viewing}_{block_idx}"):
            chosen = st.radio("Select your answer:", block.get("options", []), key=f"mc_radio_{story_id}_{viewing}_{block_idx}")
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
                    st.session_state["xp"] = st.session_state.get("xp", 0) + 15
                else:
                    correct_str = ans if isinstance(ans, str) else block["options"][ans]
                    st.error(f"❌ **Incorrect.** You selected `{chosen}`. The correct answer is **`{correct_str.rstrip('.').strip()}`**.")
                
                if block.get("explanation"):
                    with st.container(border=True):
                        st.markdown(render_markdown_html(block.get("explanation")), unsafe_allow_html=True)
                    
        if block.get("explanation"):
            with st.expander("💡 Study Guide: Reveal In-Depth Answer & Explanation"):
                st.markdown(render_markdown_html(block.get("explanation")), unsafe_allow_html=True)

    elif btype in ("scenario_decision", "dilemma", "tradeoff_dilemma"):
        scenario_text = block.get("scenario") or block.get("content", "")
        scenario_html = render_markdown_html(scenario_text)
        title = block.get("title", "Engineering Decision Dilemma")
        scen_card = (
            f'<div class="scenario-card">\n'
            f'<div class="card-kicker kicker-scenario">⚖️ ARCHITECTURAL TRADE-OFF &amp; STRATEGIC DILEMMA</div>\n'
            f'<div class="card-heading heading-scenario">{title}</div>\n'
            f'<div class="card-body">{scenario_html}</div>\n'
            f'</div>'
        )
        st.markdown(scen_card, unsafe_allow_html=True)
        
        q = block.get("question", "Which architectural or process decision should the engineering team make?")
        st.markdown(f"**{clean_newlines(q)}**")
        
        with st.form(key=f"scen_form_{story_id}_{viewing}_{block_idx}"):
            chosen = st.radio("Choose your course of action:", block.get("options", []), key=f"scen_radio_{story_id}_{viewing}_{block_idx}")
            submitted = st.form_submit_button("Submit Strategic Decision ▶")
            if submitted:
                idx = block["options"].index(chosen)
                ans = block.get("answer", -1)
                is_best = (idx == ans)
                if is_best:
                    st.success(f"🏆 **Optimal Decision!** `{chosen}` balances technical integrity with business constraints.")
                    st.session_state["xp"] = st.session_state.get("xp", 0) + 25
                else:
                    opt_str = block["options"][ans] if isinstance(ans, int) and ans < len(block["options"]) else "Recommended Path"
                    st.warning(f"⚠️ **Suboptimal Path Selected.** While tempting, `{chosen}` incurs higher risk or technical debt. The recommended approach is **`{opt_str}`**.")
                    
                if block.get("rationale") or block.get("explanation"):
                    with st.container(border=True):
                        st.markdown("#### ⚖️ Trade-off & Consequence Analysis")
                        st.markdown(render_markdown_html(block.get("rationale") or block.get("explanation")), unsafe_allow_html=True)
        
        if block.get("rationale") or block.get("explanation"):
            with st.expander("💡 Reveal Trade-off Breakdown & Industrial Best Practice"):
                st.markdown(render_markdown_html(block.get("rationale") or block.get("explanation")), unsafe_allow_html=True)

    elif btype in ("calculation_challenge", "metric_challenge"):
        st.markdown(f"### 🧮 {block.get('title', 'Software Metric Calculation')}")
        if block.get("formula"):
            st.markdown(f"""
            <div style="background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(59, 130, 246, 0.3); border-left: 4px solid #3B82F6; border-radius: 8px; padding: 12px 16px; margin-bottom: 12px;">
                <span style="color: #60A5FA; font-weight: 700; font-size: 0.82rem; text-transform: uppercase; letter-spacing: 0.05em;">Governing Metric Formula &amp; Invariants:</span>
                <div style="color: #F8FAFC; margin-top: 6px; font-size: 1.05rem; font-family: monospace;">{clean_newlines(block['formula'])}</div>
            </div>
            """, unsafe_allow_html=True)
            
        p = block.get("problem") or block.get("question", "")
        st.markdown(f'<div class="card-body" style="margin-bottom: 12px;">{render_markdown_html(p)}</div>', unsafe_allow_html=True)
        
        with st.form(key=f"calc_form_{story_id}_{viewing}_{block_idx}"):
            user_val = st.text_input("Calculated Metric Value:", key=f"calc_input_{story_id}_{viewing}_{block_idx}")
            submitted = st.form_submit_button("Verify Metric ▶")
            if submitted:
                expected_val = str(block.get("answer", ""))
                alts = block.get("alternatives", [])
                if check_answer_match(user_val, expected_val, alts):
                    st.success(f"✅ **Exact Calculation!** `{user_val.strip()}` is mathematically correct.")
                    st.session_state["xp"] = st.session_state.get("xp", 0) + 20
                else:
                    st.error(f"❌ **Calculation Mismatch.** You computed `{user_val.strip()}`. The correct value is **`{expected_val}`**.")
                    
                if block.get("step_by_step") or block.get("explanation"):
                    with st.container(border=True):
                        st.markdown("#### 📐 Step-by-Step Derivation")
                        st.markdown(render_markdown_html(block.get("step_by_step") or block.get("explanation")), unsafe_allow_html=True)
                        
        if block.get("step_by_step") or block.get("explanation"):
            with st.expander("💡 Reveal Full Mathematical Derivation"):
                st.markdown(render_markdown_html(block.get("step_by_step") or block.get("explanation")), unsafe_allow_html=True)

    elif btype in ("diagram_critique", "spot_the_flaw"):
        st.markdown(f"### 🔍 {block.get('title', 'Diagram Review & Flaw Detection')}")
        if block.get("scenario"):
            st.markdown(f'<div class="card-body" style="margin-bottom: 12px;">{render_markdown_html(block["scenario"])}</div>', unsafe_allow_html=True)
        if block.get("code"):
            st_mermaid(block["code"], height=block.get("height"))
            
        q = block.get("question", "What specification defect, modeling error, or architectural antipattern is present in this diagram?")
        st.markdown(f"**{clean_newlines(q)}**")
        
        with st.form(key=f"crit_form_{story_id}_{viewing}_{block_idx}"):
            chosen = st.radio("Select detected defect:", block.get("options", []), key=f"crit_radio_{story_id}_{viewing}_{block_idx}")
            submitted = st.form_submit_button("Submit Diagnostic Review ▶")
            if submitted:
                idx = block["options"].index(chosen)
                ans = block.get("answer", -1)
                if idx == ans:
                    st.success(f"✅ **Defect Accurately Identified!** `{chosen}` violates the standard modeling rule.")
                    st.session_state["xp"] = st.session_state.get("xp", 0) + 25
                else:
                    corr = block["options"][ans] if isinstance(ans, int) and ans < len(block["options"]) else ""
                    st.error(f"❌ **Review Missed the Core Flaw.** You selected `{chosen}`. The actual defect is **`{corr}`**.")
                    
                if block.get("remedy") or block.get("explanation"):
                    with st.container(border=True):
                        st.markdown("#### 🔧 Architectural Remediation")
                        st.markdown(render_markdown_html(block.get("remedy") or block.get("explanation")), unsafe_allow_html=True)
                        
        if block.get("remedy") or block.get("explanation"):
            with st.expander("💡 Reveal Detailed Flaw Analysis & Correction"):
                st.markdown(render_markdown_html(block.get("remedy") or block.get("explanation")), unsafe_allow_html=True)

    elif btype == "fill_in_the_blank":
        st.markdown(f"### ✍️ {block.get('title', 'Fill in the Blank Challenge')}")
        q = block.get("question", "")
        
        with st.form(key=f"fib_form_{story_id}_{viewing}_{block_idx}"):
            st.markdown(clean_newlines(q.replace("_____", "___")))
            user_ans = st.text_input("Your Answer:", key=f"fib_input_{story_id}_{viewing}_{block_idx}")
            
            submitted = st.form_submit_button("Submit Answer ▶")
            if submitted:
                ans = block.get("answer", "")
                alts = block.get("alternatives", [])
                if check_answer_match(user_ans, ans, alts):
                    st.success(f"✅ **Correct!** `{user_ans.strip()}` is the right answer.")
                    st.session_state["xp"] = st.session_state.get("xp", 0) + 20
                else:
                    clean_disp = ans.rstrip('.').strip()
                    st.error(f"❌ **Incorrect.** You entered `{user_ans.strip()}`. The expected answer is **`{clean_disp}`**.")
                
                if block.get("explanation"):
                    with st.container(border=True):
                        st.markdown(render_markdown_html(block.get("explanation")), unsafe_allow_html=True)
                    
        if block.get("explanation"):
            with st.expander("💡 Study Guide: Reveal In-Depth Answer & Explanation"):
                st.markdown(render_markdown_html(block.get("explanation")), unsafe_allow_html=True)

    elif btype == "code_lab":
        st.markdown(f"### 💻 {block.get('title', 'Implementation Lab')}")
        if block.get("instructions"):
            st.markdown(clean_newlines(block["instructions"]))
            
        tab_code, tab_why, tab_alternatives, tab_edge_cases = st.tabs([
            "🖥️ Code Editor & Execution", 
            "💡 Why This Solution Works", 
            "🔀 Alternative Approaches & Trade-offs", 
            "⚠️ Edge Cases & Failure Modes"
        ])
        
        with tab_code:
            starter = block.get("starter_code", "# Write Python code here\n")
            editor_key = f"code_editor_{story_id}_{viewing}_{block_idx}"
            
            if editor_key not in st.session_state:
                st.session_state[editor_key] = starter

            col_top1, col_top2 = st.columns([1, 4])
            with col_top1:
                if st.button("↺ Reset Starter", key=f"reset_{editor_key}"):
                    st.session_state[editor_key] = starter
                    st.rerun()

            # Editor: use streamlit_ace if available, fallback to st.text_area
            try:
                from streamlit_ace import st_ace
                user_code = st_ace(
                    value=st.session_state[editor_key],
                    language='python',
                    theme='twilight',
                    height=280,
                    key=f"ace_{editor_key}",
                    font_size=14,
                    show_gutter=True,
                    auto_update=True
                )
            except Exception:
                user_code = st.text_area("Python Implementation:", value=st.session_state[editor_key], height=240, key=f"txt_{editor_key}")

            if user_code != st.session_state[editor_key]:
                st.session_state[editor_key] = user_code

            c_run, c_sol = st.columns([3, 7])
            with c_run:
                run_btn = st.button("Compile & Run Tests ▶", key=f"run_btn_{editor_key}", type="primary")

            if block.get("solution_code") or block.get("hint"):
                with st.expander("💡 Need help? Click for Hints & Complete Reference Solution"):
                    if block.get("hint"):
                        st.info(f"**Hint:** {block.get('hint')}")
                    if block.get("solution_code"):
                        st.markdown("**Complete Architectural Solution:**")
                        if st.button("Inject Solution into Editor ⬇", key=f"inject_{editor_key}"):
                            st.session_state[editor_key] = block.get("solution_code")
                            st.rerun()
                        st.code(block.get("solution_code"), language="python")

            if run_btn:
                with st.spinner("Executing Python in isolated sandbox..."):
                    test_code = block.get("test_code")
                    test_cases = block.get("test_cases", [])
                    expected_output = block.get("expected_output")

                    if test_code:
                        full_code = user_code + "\n\n" + test_code
                        ok, out, err = py_runner.run_py(full_code)
                        if ok:
                            st.balloons()
                            st.markdown(f'''
                            <div style="background: rgba(16, 185, 129, 0.12); border: 1px solid rgba(16, 185, 129, 0.4); border-radius: 12px; padding: 16px; margin-top: 12px;">
                                <h3 style="color: #34D399; margin-top: 0;">✅ All Automated Test Cases Passed!</h3>
                                <div style="color: #AAB3CC; font-size: 0.9rem; margin-bottom: 8px;">Execution verified in sandboxed Python runner.</div>
                                <div style="background: rgba(0,0,0,0.25); padding: 12px; border-radius: 8px;">
                                    <div style="color: #F8F7FF; font-family: monospace;">{out.strip() or "All unit test assertions passed successfully!"}</div>
                                </div>
                            </div>
                            ''', unsafe_allow_html=True)
                            st.session_state["xp"] = st.session_state.get("xp", 0) + 30
                        else:
                            st.markdown(f'''
                            <div style="background: rgba(239, 68, 68, 0.12); border: 1px solid rgba(239, 68, 68, 0.4); border-radius: 12px; padding: 16px; margin-top: 12px;">
                                <h3 style="color: #FCA5A5; margin-top: 0;">❌ Test Suite Assertion / Runtime Failure</h3>
                                <div style="color: #AAB3CC; font-size: 0.9rem; margin-bottom: 8px;">Your code raised an error or failed one of the unit tests:</div>
                                <div style="background: rgba(0,0,0,0.25); padding: 12px; border-radius: 8px;">
                                    <div style="color: #F87171; font-family: monospace; white-space: pre-wrap;">{err or out}</div>
                                </div>
                            </div>
                            ''', unsafe_allow_html=True)
                    elif test_cases:
                        all_passed = True
                        st.markdown("#### Test Results")
                        for idx, tc in enumerate(test_cases):
                            inp = tc.get("input", "")
                            exp = tc.get("expected", "")
                            ok, out, err = py_runner.run_py(user_code, input_data=inp)
                            if not ok:
                                st.error(f"❌ Test Case {idx+1} Runtime Error:")
                                st.code(err)
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
                            st.success("🎉 All Test Cases Passed! You solved this engineering challenge.")
                            st.session_state["xp"] = st.session_state.get("xp", 0) + 30
                    elif expected_output:
                        ok, out, err = py_runner.run_py(user_code)
                        if ok and out.strip() == expected_output.strip():
                            st.balloons()
                            st.success("✅ Output matches expected exactly!")
                            st.code(out)
                            st.session_state["xp"] = st.session_state.get("xp", 0) + 30
                        else:
                            st.error("❌ Output did not match expected output.")
                            st.code(err or out)
                    else:
                        ok, out, err = py_runner.run_py(user_code)
                        if ok:
                            st.success("✅ Code Executed Successfully!")
                            st.code(out or "(No output)")
                        else:
                            st.error("❌ Execution Error:")
                            st.code(err or out)

        with tab_why:
            why_text = block.get("why_works") or block.get("why_it_works") or block.get("explanation") or "**Software Engineering Mechanics:**\nThis implementation establishes the exact architectural separation of concerns, invariants, and interface contracts required for production maintainability."
            st.markdown(clean_newlines(why_text))
            if block.get("complexity"):
                st.markdown("#### ⏱️ Asymptotic Complexity & Resource Budgets")
                st.markdown(clean_newlines(block.get("complexity")))

        with tab_alternatives:
            alts = block.get("alternatives")
            if alts:
                if isinstance(alts, list):
                    for alt in alts:
                        if isinstance(alt, dict):
                            st.markdown(f"**{alt.get('title', 'Alternative')}**\n> {alt.get('desc', '')}")
                        else:
                            st.markdown(clean_newlines(str(alt)))
                else:
                    st.markdown(clean_newlines(str(alts)))
            else:
                st.markdown("""
                #### 🔀 Candidate Architectural Alternatives
                - **Alternative 1: Monolithic Procedural Scripting**
                  - *Trade-off:* Quick to prototype for MVP, but accumulates crushing technical debt, high coupling, and zero unit-testability at scale.
                - **Alternative 2: Object-Oriented Composition & Dependency Inversion**
                  - *Trade-off:* Higher upfront abstraction cost and interface verbosity, but delivers modular pluggability and isolated test doubles.
                - **Alternative 3: Event-Driven Asynchronous Pipeline**
                  - *Trade-off:* Maximizes throughput and decouples producers from consumers, but introduces eventual consistency, network partition risks, and distributed tracing complexity.
                """)

        with tab_edge_cases:
            st.info("In production software engineering, real systems face unpredictable edge cases:")
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
                    {"title": "Null / Uninitialized References & NoneType", "desc": "What happens if incoming payload lacks mandatory keys or pointers are null?"},
                    {"title": "Concurrent Access & Race Conditions", "desc": "What happens when multiple threads or microservice workers modify shared state simultaneously?"},
                    {"title": "Resource Leaks & Connection Starvation", "desc": "If an exception is raised midway, are open database sockets and file handles deterministically closed?"}
                ]
                for ec in default_ecs:
                    st.markdown(f"**{ec.get('title', 'Edge Case')}**\n> {ec.get('desc', '')}")
            if "edge_cases_explanation" in block:
                st.markdown(clean_newlines(block["edge_cases_explanation"]))
