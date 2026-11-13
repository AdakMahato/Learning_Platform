with open('/Users/aadarshamahato/Downloads/LEARNING_PLATFORM/ai_story_lab/app.py', 'r') as f:
    content = f.read()

# Replace radio setup and button calls
old_setup = '''# Top Navigation Tabs
nav_selection = st.sidebar.radio(
    "LABORATORY PORTAL",
    [
        "🏠 Platform Overview",
        "🎓 Learning Paths (1 to 9)",
        "⚡ Engineering Labs (A, B, C)",
        "🏭 Industry Case Studies",
        "🚀 Capstone Studio",
        "🏛️ Algorithmic AI Archive (00-24)",
        "📋 Syllabus Coverage Matrix"
    ],
    index=0,
    key="main_portal_nav"
)'''

new_setup = '''NAV_OPTIONS = [
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
)'''

content = content.replace(old_setup, new_setup)

# Replace all occurrences of direct modification
content = content.replace('st.session_state["main_portal_nav"] = "🎓 Learning Paths (1 to 9)"\n            st.rerun()',
                          'navigate_to("🎓 Learning Paths (1 to 9)")')

content = content.replace('st.session_state["main_portal_nav"] = "⚡ Engineering Labs (A, B, C)"\n            st.rerun()',
                          'navigate_to("⚡ Engineering Labs (A, B, C)")')

content = content.replace('st.session_state["main_portal_nav"] = "🏭 Industry Case Studies"\n            st.rerun()',
                          'navigate_to("🏭 Industry Case Studies")')

content = content.replace('st.session_state["main_portal_nav"] = "🚀 Capstone Studio"\n            st.rerun()',
                          'navigate_to("🚀 Capstone Studio")')

content = content.replace('st.session_state["main_portal_nav"] = "📋 Syllabus Coverage Matrix"\n            st.rerun()',
                          'navigate_to("📋 Syllabus Coverage Matrix")')

with open('/Users/aadarshamahato/Downloads/LEARNING_PLATFORM/ai_story_lab/app.py', 'w') as f:
    f.write(content)

print("Updated app.py navigation pattern!")
