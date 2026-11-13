import streamlit as st
from persistence import load_progress, save_progress
from story_data import STORIES
from level_content import LEVEL_CONTENT
import cpp_runner

import streamlit.components.v1 as components
def st_mermaid(code: str, height=600):
    htmlcode = f'''
    <div class="mermaid" style="display: flex; justify-content: center; margin: 20px 0;">
    {code}
    </div>
    <script type="module">
      import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
      mermaid.initialize({{ startOnLoad: true, theme: 'dark', securityLevel: 'loose' }});
    </script>
    '''
    components.html(htmlcode, height=height, scrolling=True)

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

PAGE_PATHS = {0: 'pages/00_the_code_that_outgrew_its_creator.py'}

def configure_page(title="OOP Story Lab", active_nav="Home"):
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
                <div style="font-weight: 800; color: #F8F7FF; letter-spacing: 0.05em; font-size: 1.1rem; line-height: 1.1;">OOP STORY LAB</div>
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
        if active == "practice": st.markdown('<div class="nav-active">⌘ &nbsp; C++ Sandbox</div>', unsafe_allow_html=True)
        else:
            try: st.page_link("pages/cpp_sandbox.py", label="⌘  C++ Sandbox")
            except: st.markdown("⌘  C++ Sandbox", unsafe_allow_html=True)
        
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
    
    for i, block in enumerate(blocks):
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
            with st.form(key=f"think_{story_id}_{active}_{i}"):
                chosen = st.radio("Your logic:", block["options"], key=f"rad_{story_id}_{active}_{i}")
                if st.form_submit_button("Lock in Answer"):
                    idx = block["options"].index(chosen)
                    if idx == block.get("answer", -1):
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
            st.markdown(f"### 💻 {block.get('title', 'C++ Syntax')}")
            st.code(block.get("code", ""), language="cpp")
            for ann in block.get("annotations", []):
                with st.expander(f"🔍 Explain: `{ann.get('line', '')}`"):
                    st.write(ann.get("text", ""))
                    
        elif btype == "wrong_approach":
            st.markdown(f'''<div class="wrong-approach"><h4>❌ {block.get("title", "Wrong Approach")}</h4></div>''', unsafe_allow_html=True)
            st.code(block.get("code", ""), language="cpp")
            st.error(block.get("explanation", ""))
            
        elif btype == "correct_approach":
            st.markdown(f'''<div class="correct-approach"><h4>✅ {block.get("title", "Correct Approach")}</h4></div>''', unsafe_allow_html=True)
            st.code(block.get("code", ""), language="cpp")
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
            st.code(block.get("code", ""), language="cpp")
            for trace in block.get("trace", []):
                st.markdown(f"> {trace}")
                
        elif btype == "common_mistakes":
            st.markdown(f"### ⚠️ {block.get('title', 'Common Mistakes')}")
            for mist in block.get("mistakes", []):
                st.warning(f"**{mist.get('title', '')}**: {mist.get('desc', '')}")
                
        elif btype in ("code_experiment", "code_lab"):
            st.markdown(f"### 💻 {block.get('title', 'Code Lab')}")
            
            # Using Tabs for LeetCode-style UI
            tab_editor, tab_edge_cases = st.tabs(["📝 Code Editor & Tests", "⚠️ Edge Cases & Analysis"])
            
            code_key = f"code_{story_id}_{active}_{i}"
            
            # Initialization
            if code_key not in st.session_state:
                st.session_state[code_key] = block.get("starter_code", "")
                
            with tab_editor:
                # Reset logic
                if st.button("↺ Reset to Starter Code", key=f"reset_{code_key}"):
                    st.session_state[code_key] = block.get("starter_code", "")
                    st.rerun()
                    
                from streamlit_ace import st_ace
                code_txt = st_ace(value=st.session_state[code_key], language='c_cpp', theme='twilight', height=350, key=f"ace_{code_key}", font_size=14, show_gutter=True, auto_update=True)
                
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
                            st.code(block.get("solution_code"), language="cpp")
                            
                if run_clicked:
                    with st.spinner("Compiling & Executing..."):
                        import cpp_runner
                        test_cases = block.get("test_cases", [])
                        
                        if not test_cases:
                            # Fallback to single expected output
                            success, out, err = cpp_runner.run_cpp(code_txt)
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
                                success, out, err = cpp_runner.run_cpp(code_txt, input_data=inp)
                                
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
                            
        elif btype in ("micro_challenge", "mastery_challenge"):
            st.markdown(f"### 🏆 {block.get('title', 'Challenge')}")
            q = block.get("question") or block.get("content", "")
            st.write(q)
            with st.form(key=f"mc_form_{story_id}_{active}_{i}"):
                chosen = st.radio("Select answer:", block["options"], key=f"mc_radio_{story_id}_{active}_{i}")
                if st.form_submit_button("Submit"):
                    idx = block["options"].index(chosen)
                    if idx == block.get("answer", -1):
                        st.success("Correct!")
                        if block.get("explanation"): st.info(block.get("explanation"))
                    else:
                        st.error("Incorrect.")
                        if block.get("explanation"): st.info(block.get("explanation"))
                        

        elif btype == "mermaid_diagram":
            if "title" in block: st.markdown(f"#### 📊 {block['title']}")
            if "explanation" in block: st.markdown(block["explanation"])
            st_mermaid(block.get("code", ""), height=block.get("height", 400))

        elif btype == "memory_layout":
            if "title" in block: st.markdown(f"#### 💾 {block['title']}")
            if "explanation" in block: st.markdown(block["explanation"])
            render_memory_layout(block.get("cells", []))

        elif btype == "story":

            text = block.get("text") or block.get("content", "")
            title_html = f"<h3>{block.get('title')}</h3>" if block.get("title") else ""
            st.markdown(f'<div class="objective">{title_html}<p>{text}</p></div>', unsafe_allow_html=True)
            
        elif btype == "problem":
            text = block.get("text") or block.get("content", "")
            st.markdown(f'<div class="problem-block"><b>Problem:</b> {text}</div>', unsafe_allow_html=True)
            
        elif btype == "concept":
            expl = block.get("explanation") or block.get("content", "")
            title_html = f"<b>{block.get('title')}</b><br>" if block.get("title") else ""
            st.markdown(f'<div class="concept-block">{title_html}<span style="color:#AAB3CC;">{expl}</span></div>', unsafe_allow_html=True)
            if "analogy" in block: st.info(f"💡 **Analogy:** {block['analogy']}")
            if "technical_explanation" in block: st.markdown(f"⚙️ **Technical:** {block['technical_explanation']}")
            
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
            with st.form(key=f"debug_form_{story_id}_{active}_{i}"):
                chosen = st.radio("Diagnose the issue:", block["options"], key=f"debug_radio_{story_id}_{active}_{i}")
                if st.form_submit_button("Submit Diagnosis"):
                    if chosen == block["answer"]: st.success("Correct!")
                    else: st.error("Incorrect. " + block.get("explanation", ""))
                            
    if st.button("Complete Module", type="primary", key=f"complete_mod_{story_id}_{active}"):
        complete_current(story_id, active, len(episodes))

def story_status(story_id):
    if story_id in st.session_state.get("completed", set()): return "✓ Completed", "status-complete"
    active_level = st.session_state.get(f"active_level_{story_id}", 1)
    if active_level > 1: return "◐ In progress", "status-progress"
    return "○ Not started", "status-open"

def workspace_css():
    pass # I already have style tags in configure_page! 

