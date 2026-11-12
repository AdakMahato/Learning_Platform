"""
AI & Machine Learning Lab — Engineering Platform
Main Dashboard and Unified Engineering Portal.
Features:
1. Learning Paths (9 Structured Engineering Curricula)
2. Interactive Engineering Laboratories (Motor Temp, Materials Clustering, Circuit Detection)
3. Documented Industry Case Studies (Siemens, GE, Honeywell)
4. Capstone Studio (Guided 12-Step Mini-Project)
5. Classical & Algorithmic AI Foundation Archive (Cases 00 through 24)
6. Academic Syllabus Coverage Matrix (100% ABET/Engineering Verified)
"""

import streamlit as st
import sys
import os

sys.path.append(os.path.dirname(__file__))

from ui import configure_page, workspace_css, story_status, ensure_state, sidebar
from story_data import STORIES
import learning_paths
import engineering_labs
import industry_cases
import capstone_project
import syllabus_viewer

# Configure page settings
configure_page("Home | AI & Machine Learning Engineering Lab")
workspace_css()
ensure_state()

# Navigation paths dict
PAGE_PATHS = {}
for story in STORIES:
    sid = story["id"]
    title_safe = story["title"].lower().replace(" ", "_").replace("'", "").replace("-", "_").replace(",", "")
    PAGE_PATHS[sid] = f"pages/{sid:02d}_{title_safe}.py"

NAV_OPTIONS = [
    "🏠 Platform Overview",
    "🎓 Learning Paths (1 to 9)",
    "⚡ Engineering Labs (A, B, C)",
    "🏭 Industry Case Studies",
    "🚀 Capstone Studio",
    "🏛️ Algorithmic AI Archive (00-24)",
    "📋 Syllabus Coverage Matrix"
]

def navigate_to(page_name):
    st.session_state["pending_nav"] = page_name
    st.rerun()

# Apply pending navigation before widget instantiation
if "pending_nav" in st.session_state and st.session_state["pending_nav"] in NAV_OPTIONS:
    st.session_state["main_portal_nav"] = st.session_state.pop("pending_nav")

if "main_portal_nav" not in st.session_state:
    st.session_state["main_portal_nav"] = NAV_OPTIONS[0]

# Top Navigation Tabs
nav_selection = st.sidebar.radio(
    "LABORATORY PORTAL",
    NAV_OPTIONS,
    key="main_portal_nav"
)

# Active user stats in sidebar
user_xp = st.session_state.get("xp", 300)
st.sidebar.markdown(f"""
<div style="background: rgba(124, 77, 255, 0.12); border: 1px solid #7C4DFF; border-radius: 12px; padding: 14px; margin-top: 20px;">
    <div style="color: #A78BFA; font-size: 0.75rem; font-weight: 800; letter-spacing: 0.1em; text-transform: uppercase;">ENGINEER STATUS</div>
    <div style="color: #F8F7FF; font-size: 1.3rem; font-weight: 800; margin: 4px 0;">Level 2 Practitioner</div>
    <div style="color: #34D399; font-weight: 700; font-size: 0.95rem;">⚡ {user_xp} Mastery XP</div>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------------------
# 1. PLATFORM OVERVIEW (HOME)
# -------------------------------------------------------------
if nav_selection == "🏠 Platform Overview":
    st.markdown('''
    <div style="padding: 32px 0 20px 0;">
        <div style="color: #7C4DFF; font-weight: 800; font-size: 0.85rem; letter-spacing: 0.15em; margin-bottom: 12px;">
            NEXUS ENGINEERING SIMULATOR • AI & MACHINE LEARNING
        </div>
        <h1 style="font-size: 3.2rem; line-height: 1.15; margin-bottom: 20px; color: #F8F7FF;">
            Learn Engineering AI by<br>Interacting with Systems.
        </h1>
        <p style="font-size: 1.15rem; color: #AAB3CC; max-width: 750px; line-height: 1.6; margin-bottom: 28px;">
            Explore real physical engineering problems, manipulate multi-channel sensor telemetry, 
            observe algorithmic decision boundaries, and build industrial-grade machine learning models 
            from absolute fundamentals to full capstone deployment.
        </p>
    </div>
    ''', unsafe_allow_html=True)

    # Fast Action Cards
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown("""
        <div style="background: #121B32; border: 1px solid rgba(255,255,255,0.08); border-radius: 14px; padding: 18px; height: 180px; display: flex; flex-direction: column;">
            <div style="font-size: 1.6rem; margin-bottom: 6px;">🎓</div>
            <div style="color: #F8F7FF; font-weight: 800; font-size: 1.05rem; margin-bottom: 6px;">Learning Paths</div>
            <div style="color: #AAB3CC; font-size: 0.8rem; line-height: 1.4; flex-grow: 1;">9 progressive engineering paths from Python basics to Deep Learning.</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Browse Paths →", key="home_btn_paths", use_container_width=True):
            navigate_to("🎓 Learning Paths (1 to 9)")

    with c2:
        st.markdown("""
        <div style="background: #121B32; border: 1px solid rgba(255,255,255,0.08); border-radius: 14px; padding: 18px; height: 180px; display: flex; flex-direction: column;">
            <div style="font-size: 1.6rem; margin-bottom: 6px;">⚡</div>
            <div style="color: #F8F7FF; font-weight: 800; font-size: 1.05rem; margin-bottom: 6px;">Engineering Labs</div>
            <div style="color: #AAB3CC; font-size: 0.8rem; line-height: 1.4; flex-grow: 1;">Motor temperature, materials clustering, and circuit defect neural nets.</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Launch Labs →", key="home_btn_labs", use_container_width=True):
            navigate_to("⚡ Engineering Labs (A, B, C)")

    with c3:
        st.markdown("""
        <div style="background: #121B32; border: 1px solid rgba(255,255,255,0.08); border-radius: 14px; padding: 18px; height: 180px; display: flex; flex-direction: column;">
            <div style="font-size: 1.6rem; margin-bottom: 6px;">🏭</div>
            <div style="color: #F8F7FF; font-weight: 800; font-size: 1.05rem; margin-bottom: 6px;">Industry Cases</div>
            <div style="color: #AAB3CC; font-size: 0.8rem; line-height: 1.4; flex-grow: 1;">Verified real-world deployments at Siemens, GE, and Honeywell.</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Read Cases →", key="home_btn_cases", use_container_width=True):
            navigate_to("🏭 Industry Case Studies")

    with c4:
        st.markdown("""
        <div style="background: #121B32; border: 1px solid rgba(255,255,255,0.08); border-radius: 14px; padding: 18px; height: 180px; display: flex; flex-direction: column;">
            <div style="font-size: 1.6rem; margin-bottom: 6px;">🚀</div>
            <div style="color: #F8F7FF; font-weight: 800; font-size: 1.05rem; margin-bottom: 6px;">Capstone Studio</div>
            <div style="color: #AAB3CC; font-size: 0.8rem; line-height: 1.4; flex-grow: 1;">Guided 12-step engineering mini-project with custom CSV upload.</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Start Capstone →", key="home_btn_cap", use_container_width=True):
            navigate_to("🚀 Capstone Studio")

    st.markdown("<br><hr>", unsafe_allow_html=True)
    st.markdown('<div style="font-size: 0.85rem; font-weight: 800; letter-spacing: 0.15em; color: #AAB3CC; margin-bottom: 20px;">RECOMMENDED NEXT INVESTIGATION</div>', unsafe_allow_html=True)
    
    col_rec1, col_rec2 = st.columns([2, 1])
    with col_rec1:
        st.markdown("""
        <div style="background: rgba(124, 77, 255, 0.08); border: 1px solid #7C4DFF; border-radius: 16px; padding: 24px;">
            <div style="color: #A78BFA; font-size: 0.8rem; font-weight: 800; letter-spacing: 0.1em; margin-bottom: 8px;">CASE 00 • FOUNDATIONAL ONBOARDING</div>
            <h3 style="color: #F8F7FF; margin: 0 0 10px 0;">The Machine That Couldn't Think</h3>
            <p style="color: #AAB3CC; font-size: 0.95rem; line-height: 1.6; margin-bottom: 16px;">
                Before writing code or training models, discover the fundamental philosophical and theoretical questions of AI: 
                The Turing Test, Searle's Chinese Room, and why machine learning differs fundamentally from traditional software.
            </p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Launch Case 00 Investigation →", type="primary", key="home_launch_00"):
            st.switch_page(PAGE_PATHS[0])

    with col_rec2:
        st.markdown("""
        <div style="background: #121B32; border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; padding: 24px; text-align: center;">
            <div style="color: #AAB3CC; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 8px;">Curriculum Health</div>
            <div style="color: #34D399; font-size: 2.2rem; font-weight: 800; margin-bottom: 4px;">100%</div>
            <div style="color: #AAB3CC; font-size: 0.85rem; line-height: 1.4;">46/46 Academic Topics Verified & Compliant</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("View Syllabus Matrix", key="home_view_syl", use_container_width=True):
            navigate_to("📋 Syllabus Coverage Matrix")

# -------------------------------------------------------------
# 2. LEARNING PATHS (1 TO 9)
# -------------------------------------------------------------
elif nav_selection == "🎓 Learning Paths (1 to 9)":
    active_path = st.session_state.get("active_learning_path")
    if active_path:
        learning_paths.render_active_learning_path(active_path)
    else:
        learning_paths.render_learning_paths_dashboard()

# -------------------------------------------------------------
# 3. ENGINEERING LABS (A, B, C)
# -------------------------------------------------------------
elif nav_selection == "⚡ Engineering Labs (A, B, C)":
    st.markdown("""
    <div style="margin-bottom: 24px;">
        <h1 style="color: #F8F7FF; font-size: 2.5rem; margin-bottom: 8px;">⚡ Interactive Engineering Laboratories</h1>
        <p style="color: #AAB3CC; font-size: 1.1rem; max-width: 800px; line-height: 1.6;">
            Perform hands-on empirical experimentation on real physical and metallurgical engineering datasets. 
            Tune hyperparameters, inspect residuals, and observe algorithmic convergence in real time.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    lab_tabs = st.tabs([
        "⚡ Lab A: Motor Temperature (Regression)", 
        "🔬 Lab B: Materials Clustering (K-Means)", 
        "🧠 Lab C: Faulty Circuit Detection (Neural Net)", 
        "🌀 DBSCAN Density Sandbox", 
        "👁️ CNN 2D Filter Visualizer", 
        "📈 Time-Series Forecasting Lab"
    ])
    
    with lab_tabs[0]:
        engineering_labs.render_motor_temperature_lab()
    with lab_tabs[1]:
        engineering_labs.render_materials_clustering_lab()
    with lab_tabs[2]:
        engineering_labs.render_circuit_detection_lab()
    with lab_tabs[3]:
        engineering_labs.render_dbscan_playground()
    with lab_tabs[4]:
        engineering_labs.render_cnn_filter_visualizer()
    with lab_tabs[5]:
        engineering_labs.render_timeseries_forecasting_lab()

# -------------------------------------------------------------
# 4. INDUSTRY CASE STUDIES
# -------------------------------------------------------------
elif nav_selection == "🏭 Industry Case Studies":
    industry_cases.render_all_case_studies_hub()

# -------------------------------------------------------------
# 5. CAPSTONE STUDIO
# -------------------------------------------------------------
elif nav_selection == "🚀 Capstone Studio":
    capstone_project.render_capstone_studio()

# -------------------------------------------------------------
# 6. CLASSICAL & ALGORITHMIC AI ARCHIVE (CASES 00 - 24)
# -------------------------------------------------------------
elif nav_selection == "🏛️ Algorithmic AI Archive (00-24)":
    st.markdown('''
    <div style="margin-bottom: 24px;">
        <h1 style="color: #F8F7FF; font-size: 2.5rem; margin-bottom: 8px;">🏛️ Algorithmic & Symbolic AI Foundation Archive</h1>
        <p style="color: #AAB3CC; font-size: 1.1rem; max-width: 850px; line-height: 1.6;">
            The complete 25-case algorithmic reasoning curriculum. Covers state-space search, A* heuristic proofs, 
            adversarial minimax, constraint satisfaction (CSP), first-order logic, planning, and foundational probabilistic reasoning.
        </p>
    </div>
    ''', unsafe_allow_html=True)

    # 4-column card grid for all 25 cases
    for i in range(0, len(STORIES), 4):
        cols = st.columns(4)
        for j in range(4):
            if i + j < len(STORIES):
                story = STORIES[i + j]
                with cols[j]:
                    status_text, status_class = story_status(story["id"])
                    
                    if "Completed" in status_text:
                        bg = "rgba(167, 243, 208, 0.08)"
                        border = "1px solid #34D399"
                        icon_color = "#34D399"
                        bottom_icon = '<div style="width: 28px; height: 28px; border-radius: 14px; background: #34D399; color: #064E3B; display: flex; align-items: center; justify-content: center; font-weight: 800; margin: 0 auto;">✓</div>'
                    elif "progress" in status_text:
                        bg = "rgba(124, 77, 255, 0.08)"
                        border = "2px solid #7C4DFF"
                        icon_color = "#A78BFA"
                        bottom_icon = '<div style="background: rgba(124, 77, 255, 0.2); color: #C4B5FD; border-radius: 12px; padding: 4px 0; text-align: center; font-weight: 700; font-size: 0.8rem; width: 55px; margin: 0 auto;">Active</div>'
                    else:
                        bg = "#121B32"
                        border = "1px solid rgba(255,255,255,0.06)"
                        icon_color = "#64748B"
                        bottom_icon = '<div style="width: 28px; height: 28px; border-radius: 14px; background: rgba(255,255,255,0.05); color: #64748B; display: flex; align-items: center; justify-content: center; margin: 0 auto;">○</div>'

                    card_html = f'''
                    <div style="background: {bg}; border: {border}; border-radius: 16px; padding: 18px; margin-bottom: 12px; height: 320px; display: flex; flex-direction: column;">
                        <div style="color: {icon_color}; font-size: 0.75rem; font-weight: 800; letter-spacing: 0.1em; margin-bottom: 8px; display: flex; align-items: center; gap: 8px;">
                            <span>{story.get('icon', '📖')}</span> CASE {story['id']:02d}
                        </div>
                        <div style="color: #F8F7FF; font-weight: 800; font-size: 1.05rem; margin-bottom: 8px; line-height: 1.3; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;">
                            {story['title']}
                        </div>
                        <div style="margin-bottom: 8px;">
                            <span style="background: rgba(124, 77, 255, 0.15); color: #B39DDB; padding: 3px 8px; border-radius: 4px; font-size: 0.68rem; font-weight: 700;">
                                {story.get('primary', 'Core Concept')}
                            </span>
                        </div>
                        <div style="color: #AAB3CC; font-size: 0.8rem; line-height: 1.5; margin-bottom: 12px; display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden; flex-grow: 1;">
                            {story['hook']}
                        </div>
                        <div style="margin-top: auto;">{bottom_icon}</div>
                    </div>
                    '''
                    st.markdown('\n'.join(line.lstrip() for line in card_html.split('\n')), unsafe_allow_html=True)
                    if st.button("Open Case", key=f"open_case_{story['id']}", use_container_width=True):
                        st.switch_page(PAGE_PATHS[story["id"]])

# -------------------------------------------------------------
# 7. SYLLABUS COVERAGE MATRIX
# -------------------------------------------------------------
elif nav_selection == "📋 Syllabus Coverage Matrix":
    syllabus_viewer.render_syllabus_coverage_dashboard()
