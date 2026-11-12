import streamlit as st
import sys
import os

sys.path.append(os.path.dirname(__file__))

from ui import configure_page, workspace_css, story_status, ensure_state, sidebar, PAGE_PATHS
from story_data import STORIES

configure_page("Home | Cloud Story Lab")
workspace_css()
ensure_state()
sidebar("home")

last_case_id = st.session_state.get("last_story_id", 0)
last_story = next((s for s in STORIES if s["id"] == last_case_id), STORIES[0])
last_level = st.session_state.get(f"active_level_{last_case_id}", 1)

# Hero Section
st.markdown('''
<div style="padding: 32px 0 20px 0;">
    <div style="color: #38BDF8; font-weight: 800; font-size: 0.85rem; letter-spacing: 0.15em; margin-bottom: 12px;">ENTERPRISE CLOUD COMPUTING & DISTRIBUTED SYSTEMS LAB</div>
    <h1 style="font-size: 3.2rem; line-height: 1.1; margin-bottom: 20px; color: #F8F7FF;">Architect resilient systems<br>on the global cloud continuum.</h1>
    <p style="font-size: 1.15rem; color: #AAB3CC; max-width: 650px; line-height: 1.6; margin-bottom: 28px;">
        Master hypervisor virtualization, AWS core services (EC2, S3, SQS, IAM), 
        HDFS & MapReduce distributed data clusters, NoSQL CAP consistency, and Green Cloud sustainability metrics.
    </p>
</div>
''', unsafe_allow_html=True)

col_hero1, col_hero2 = st.columns([1.4, 1])
with col_hero1:
    if st.button("Enter Current Case →", key="enter_investigation", type="primary"):
        st.switch_page(PAGE_PATHS[last_case_id])
    
    st.markdown(f'''
    <div style="margin-top: 24px; max-width: 420px; background: rgba(14, 165, 233, 0.08); border: 1px solid rgba(56, 189, 248, 0.25); border-radius: 16px; padding: 18px 22px;">
        <div style="color: #38BDF8; font-size: 0.75rem; font-weight: 800; letter-spacing: 0.1em; margin-bottom: 6px;">CURRENT CASE: {last_case_id:02d}</div>
        <div style="color: #F8F7FF; font-weight: 800; font-size: 1.1rem; margin-bottom: 8px;">{last_story['title']}</div>
        <div style="color: #94A3B8; font-size: 0.85rem; line-height: 1.4;">Active Module: {last_level} • Focus: {last_story.get('primary', 'Cloud Architecture')}</div>
    </div>
    ''', unsafe_allow_html=True)

with col_hero2:
    st.markdown('''
    <div style="background: rgba(15, 23, 42, 0.9); border: 1px solid rgba(56, 189, 248, 0.3); border-radius: 20px; padding: 24px; font-family: monospace; font-size: 0.82rem; color: #94A3B8; line-height: 1.6;">
        <div style="color: #38BDF8; font-weight: bold; margin-bottom: 8px;">// Cloud Event Processing & Serverless Worker</div>
        <span style="color: #F43F5E;">import</span> <span style="color: #38BDF8;">boto3</span>, <span style="color: #38BDF8;">json</span><br><br>
        <span style="color: #F43F5E;">def</span> <span style="color: #38BDF8;">handle_s3_upload</span>(event, context):<br>
        &nbsp;&nbsp;s3 = boto3.client(<span style="color: #34D399;">'s3'</span>)<br>
        &nbsp;&nbsp;sqs = boto3.client(<span style="color: #34D399;">'sqs'</span>)<br>
        &nbsp;&nbsp;bucket = event[<span style="color: #34D399;">'Records'</span>][0][<span style="color: #34D399;">'s3'</span>][<span style="color: #34D399;">'bucket'</span>][<span style="color: #34D399;">'name'</span>]<br>
        &nbsp;&nbsp;key = event[<span style="color: #34D399;">'Records'</span>][0][<span style="color: #34D399;">'s3'</span>][<span style="color: #34D399;">'object'</span>][<span style="color: #34D399;">'key'</span>]<br>
        &nbsp;&nbsp;<span style="color: #64748B;"># Asynchronously dispatch to SQS queue</span><br>
        &nbsp;&nbsp;sqs.send_message(QueueUrl=QUEUE_URL, MessageBody=json.dumps({<span style="color: #34D399;">'bucket'</span>: bucket, <span style="color: #34D399;">'key'</span>: key}))<br>
        &nbsp;&nbsp;<span style="color: #F43F5E;">return</span> {<span style="color: #34D399;">'statusCode'</span>: 202, <span style="color: #34D399;">'status'</span>: <span style="color: #34D399;">'QUEUED'</span>}
    </div>
    ''', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(f'<div style="font-size: 0.85rem; font-weight: 800; letter-spacing: 0.2em; color: #AAB3CC; margin-bottom: 20px;">ALL {len(STORIES)} SYLLABUS CASES & INVESTIGATIONS</div>', unsafe_allow_html=True)

# Grid of Stories (4 per row)
for i in range(0, len(STORIES), 4):
    cols = st.columns(4)
    for j in range(4):
        if i + j < len(STORIES):
            story = STORIES[i + j]
            with cols[j]:
                status_text, status_class = story_status(story["id"])
                
                if "Completed" in status_text:
                    bg = "rgba(16, 185, 129, 0.08)"
                    border = "1px solid #10B981"
                    icon_color = "#10B981"
                    title_color = "#F8FAFC"
                    desc_color = "#AAB3CC"
                    bottom_icon = '<div style="width: 28px; height: 28px; border-radius: 14px; background: #10B981; color: #064E3B; display: flex; align-items: center; justify-content: center; font-weight: 800; margin: 0 auto;">✓</div>'
                elif "progress" in status_text:
                    bg = "rgba(14, 165, 233, 0.12)"
                    border = "2px solid #0EA5E9"
                    icon_color = "#38BDF8"
                    title_color = "#F8FAFC"
                    desc_color = "#CBD5E1"
                    bottom_icon = '<div style="background: rgba(14, 165, 233, 0.3); color: #BAE6FD; border-radius: 10px; padding: 4px 10px; text-align: center; font-weight: 700; font-size: 0.8rem; margin: 0 auto; width: 64px;">Active</div>'
                else:
                    bg = "#121B32"
                    border = "1px solid rgba(255,255,255,0.06)"
                    icon_color = "#64748B"
                    title_color = "#F8FAFC"
                    desc_color = "#64748B"
                    bottom_icon = '<div style="width: 28px; height: 28px; border-radius: 14px; background: rgba(255,255,255,0.05); color: #64748B; display: flex; align-items: center; justify-content: center; margin: 0 auto;">○</div>'

                card_html = f'''
                <div style="background: {bg}; border: {border}; border-radius: 20px; padding: 22px; position: relative; margin-bottom: 12px; height: 310px; display: flex; flex-direction: column;">
                    <div style="color: {icon_color}; font-size: 0.75rem; font-weight: 800; letter-spacing: 0.1em; margin-bottom: 10px; display: flex; align-items: center; gap: 8px; flex-shrink: 0;">
                        <span>{story.get('icon', '☁️')}</span> CASE {story['id']:02d} • {story.get('difficulty', 'Intermediate')}
                    </div>
                    <div style="color: {title_color}; font-weight: 800; font-size: 1.05rem; margin-bottom: 8px; line-height: 1.3; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; flex-shrink: 0;">{story['title']}</div>
                    <div style="margin-bottom: 10px;"><span style="background: rgba(14, 165, 233, 0.2); color: #7DD3FC; padding: 3px 8px; border-radius: 4px; font-size: 0.7rem; font-weight: 700; letter-spacing: 0.05em;">{story.get('primary', 'Cloud Computing')}</span></div>
                    <div style="color: {desc_color}; font-size: 0.82rem; line-height: 1.45; margin-bottom: 12px; display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical; overflow: hidden; flex-grow: 1;">{story['hook']}</div>
                    <div style="margin-top: auto; flex-shrink: 0;">{bottom_icon}</div>
                </div>
                '''
                st.markdown('\n'.join(line.lstrip() for line in card_html.split('\n')), unsafe_allow_html=True)
                if st.button("Open Case", key=f"open_{story['id']}", use_container_width=True):
                    st.switch_page(PAGE_PATHS[story["id"]])
