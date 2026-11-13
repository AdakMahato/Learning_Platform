import streamlit as st
from ui import sidebar, configure_page

configure_page("SQL Playground")
sidebar(active="practice")

st.markdown("""
    <style>
    .playground-container { display: flex; flex-direction: column; gap: 20px; }
    .db-panel { background: #121B32; border: 1px solid rgba(255,255,255,0.05); padding: 20px; border-radius: 12px; height: 100%; }
    .editor-panel { background: #0B1225; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; }
    .table-list { color: #AAB3CC; font-family: monospace; font-size: 0.9rem; line-height: 1.8; }
    </style>
""", unsafe_allow_html=True)

st.title("SQL Playground")
st.markdown("<p style='color: #AAB3CC; margin-bottom: 30px;'>Practice your queries against the investigation databases.</p>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 3])

with col1:
    st.markdown("""
        <div class="db-panel">
            <h4 style="color:#F8F7FF; margin-top:0; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom:10px;">DATABASE</h4>
            <div class="table-list">
                ▶ customers<br>
                ▶ orders<br>
                ▶ products<br>
                ▶ security_logs
            </div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    query = st.text_area("SQL Editor", "SELECT *\nFROM customers\nLIMIT 5;", height=150, label_visibility="collapsed")
    if st.button("▶ Run Query", type="primary"):
        st.success("Query executed successfully. (Simulated output)")
        st.markdown("""
            <div style="background: #121B32; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; padding: 20px; font-family: monospace; overflow-x: auto;">
                <table style="width:100%; text-align:left; color:#AAB3CC; border-collapse: collapse;">
                    <tr style="border-bottom: 1px solid rgba(255,255,255,0.1); color:#F8F7FF;">
                        <th>id</th><th>name</th><th>city</th>
                    </tr>
                    <tr><td>101</td><td>Aisha</td><td>Delhi</td></tr>
                    <tr><td>102</td><td>Rahul</td><td>Mumbai</td></tr>
                    <tr><td>103</td><td>Sara</td><td>Pune</td></tr>
                </table>
            </div>
        """, unsafe_allow_html=True)
