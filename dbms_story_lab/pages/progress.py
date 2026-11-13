import streamlit as st
from ui import sidebar, configure_page
from persistence import load_progress

load_progress()
configure_page("Progress")
sidebar(active="progress")

st.markdown('''
<style>
.mastery-card { background: #121B32; border: 1px solid rgba(255,255,255,0.05); border-radius: 20px; padding: 32px; margin-bottom: 32px; }
.mastery-row { display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; }
.mastery-label { color: #F8F7FF; font-weight: 700; font-size: 1rem; flex: 1; }
.mastery-bar-container { flex: 2; height: 12px; background: rgba(255,255,255,0.05); border-radius: 6px; overflow: hidden; margin: 0 24px; }
.mastery-bar-fill { height: 100%; background: linear-gradient(90deg, #7C4DFF, #A78BFA); border-radius: 6px; }
.mastery-value { color: #AAB3CC; font-weight: 700; font-size: 0.9rem; width: 40px; text-align: right; }
.stat-box { background: #0B1225; border: 1px solid rgba(255,255,255,0.05); border-radius: 16px; padding: 24px; text-align: center; }
.stat-value { font-size: 2.5rem; font-weight: 800; color: #F8F7FF; margin-bottom: 8px; line-height: 1; }
.stat-label { color: #64748B; font-weight: 800; font-size: 0.75rem; letter-spacing: 0.1em; text-transform: uppercase; }
</style>
''', unsafe_allow_html=True)

st.title("Your Mastery")
st.markdown("<p style='color: #AAB3CC; margin-bottom: 48px;'>Track your understanding of database concepts.</p>", unsafe_allow_html=True)

total_cases = 11
completed_cases = len(st.session_state.completed)
mastery_percentage = int((completed_cases / total_cases) * 100)

col1, col2 = st.columns(2)
with col1:
    st.markdown(f'''
    <div class="stat-box">
        <div class="stat-value">{completed_cases} / {total_cases}</div>
        <div class="stat-label">CASES SOLVED</div>
    </div>
    ''', unsafe_allow_html=True)
with col2:
    st.markdown(f'''
    <div class="stat-box">
        <div class="stat-value">{mastery_percentage}%</div>
        <div class="stat-label">OVERALL FOUNDATIONS</div>
    </div>
    ''', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown('<div class="mastery-card">', unsafe_allow_html=True)
st.markdown('<h3 style="margin-top: 0; margin-bottom: 24px;">Concept Mastery</h3>', unsafe_allow_html=True)

def render_mastery(label, value):
    st.markdown(f'''
    <div class="mastery-row">
        <div class="mastery-label">{label}</div>
        <div class="mastery-bar-container"><div class="mastery-bar-fill" style="width: {value}%;"></div></div>
        <div class="mastery-value">{value}%</div>
    </div>
    ''', unsafe_allow_html=True)

# Fake values based on overall completion for now
render_mastery("Database Basics", min(100, completed_cases * 30))
render_mastery("Tables & Records", min(100, max(0, (completed_cases - 1) * 25)))
render_mastery("Relationships", min(100, max(0, (completed_cases - 2) * 20)))
render_mastery("SQL Basics", min(100, max(0, (completed_cases - 3) * 15)))
render_mastery("Joins & Aggregations", min(100, max(0, (completed_cases - 4) * 15)))

st.markdown('</div>', unsafe_allow_html=True)

