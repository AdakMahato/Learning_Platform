"""Unified Engineering Story Labs platform entrypoint."""

import html
import logging
from typing import Any, Dict, List, Optional

import streamlit as st

import core_loader as loader
import master_ui as ui
import unified_persistence as persistence

logger = logging.getLogger("learning_platform")

st.set_page_config(
    page_title="Engineering Story Labs",
    page_icon="</>",
    layout="wide",
    initial_sidebar_state="expanded",
)

VALID_SUBJECTS = set(loader.SUBJECT_REGISTRY.keys()) | {"home"}


def sync_query_params() -> None:
    """Synchronizes and strictly validates URL query parameters on initial session load."""
    if "nav_subject" in st.session_state:
        return

    params = st.query_params
    should_clear_case = False

    if "subject" in params:
        raw_subject = str(params["subject"]).strip()
        if raw_subject in VALID_SUBJECTS:
            st.session_state["nav_subject"] = raw_subject
        else:
            st.session_state["nav_subject"] = "home"
            st.session_state["nav_case"] = None
            st.session_state["_invalid_param_notice"] = (
                f"Unknown track parameter '{raw_subject}' was redirected to All Tracks."
            )
            st.query_params.clear()
            return
    else:
        st.session_state["nav_subject"] = "home"

    active_subject = st.session_state.get("nav_subject", "home")
    if "case" in params:
        raw_case = str(params["case"]).strip()
        if active_subject == "home":
            should_clear_case = True
            st.session_state["nav_case"] = None
        else:
            try:
                parsed_case = int(raw_case)
                data = loader.load_subject_data(active_subject)
                if parsed_case in data["stories_by_id"]:
                    st.session_state["nav_case"] = parsed_case
                else:
                    should_clear_case = True
                    st.session_state["nav_case"] = None
                    st.session_state["_invalid_param_notice"] = (
                        f"Case #{parsed_case} was not found in {active_subject.upper()}."
                    )
            except ValueError:
                should_clear_case = True
                st.session_state["nav_case"] = None
                st.session_state["_invalid_param_notice"] = (
                    f"Invalid case identifier '{raw_case}' was ignored."
                )

    if should_clear_case and "case" in st.query_params:
        del st.query_params["case"]


def update_query_params(subject_id: str, case_id: Optional[int] = None) -> None:
    """Updates shareable browser query parameters without disrupting active reruns."""
    safe_subject = subject_id if subject_id in VALID_SUBJECTS else "home"
    if st.query_params.get("subject") != safe_subject:
        st.query_params["subject"] = safe_subject
    target_case = str(case_id) if (case_id is not None and safe_subject != "home") else None
    if target_case is not None:
        if st.query_params.get("case") != target_case:
            st.query_params["case"] = target_case
    elif "case" in st.query_params:
        del st.query_params["case"]


def _navigate_to(subject_id: str, case_id: Optional[int] = None, mod_id: Optional[int] = None) -> None:
    """Navigates cleanly across tracks, catalogs, and case modules."""
    safe_subject = subject_id if subject_id in VALID_SUBJECTS else "home"
    safe_case = case_id if (case_id is not None and safe_subject != "home") else None
    st.session_state["nav_subject"] = safe_subject
    st.session_state["nav_case"] = safe_case
    if safe_case is not None:
        target_mod = mod_id if mod_id is not None else persistence.get_active_module(safe_subject, safe_case)
        st.session_state[f"active_mod_{safe_subject}_{safe_case}"] = max(1, int(target_mod))


def _on_sidebar_subject_change() -> None:
    choice = st.session_state.get("sidebar_subj_select", "home")
    if choice != st.session_state.get("nav_subject", "home"):
        _navigate_to(choice, None)


def _on_case_jumper_change(subject_id: str) -> None:
    selected_label = st.session_state.get(f"case_jumper_{subject_id}")
    if selected_label and str(selected_label).startswith("Case "):
        try:
            cid = int(str(selected_label).split(":")[0].replace("Case ", "").strip())
            if cid != st.session_state.get("nav_case"):
                _navigate_to(subject_id, cid)
        except ValueError:
            pass


def _render_account_controls(display_label: str, is_authenticated: bool) -> None:
    """Renders account sign-in, registration, and sign-out controls in the sidebar."""
    with st.expander(f"Workspace Account ({display_label})", expanded=False):
        if is_authenticated:
            st.caption(f"Signed in as {display_label}. Progress is persisted per account.")
            if st.button("Sign Out", key="sidebar_signout_btn", use_container_width=True):
                persistence.set_authenticated_user(None)
                st.rerun()
            return

        tab_in, tab_up = st.tabs(["Sign In", "Create Account"])
        with tab_in:
            with st.form("sidebar_signin_form", clear_on_submit=False):
                u_in = st.text_input("Username", key="sb_login_user", placeholder="engineer_id")
                p_in = st.text_input("Password", type="password", key="sb_login_pass")
                if st.form_submit_button("Sign In", type="primary", use_container_width=True):
                    ok, msg = persistence.authenticate_user(u_in, p_in)
                    if ok:
                        persistence.set_authenticated_user(msg)
                        st.rerun()
                    else:
                        st.error(msg)
        with tab_up:
            with st.form("sidebar_register_form", clear_on_submit=True):
                u_reg = st.text_input("New Username", key="sb_reg_user", placeholder="3-32 chars")
                p_reg = st.text_input("Password", type="password", key="sb_reg_pass", placeholder="Min 8 chars")
                if st.form_submit_button("Create Account", use_container_width=True):
                    ok, msg = persistence.register_user(u_reg, p_reg)
                    if ok:
                        persistence.set_authenticated_user(msg)
                        st.rerun()
                    else:
                        st.error(msg)


def render_auth_gate() -> None:
    """Renders the full-page authentication gate when PLATFORM_AUTH_MODE=required."""
    st.markdown(
        """
        <div class="auth-gate-card">
          <div class="auth-gate-kicker">AUTHENTICATED WORKSPACE</div>
          <h1 class="auth-gate-title">Engineering Story Labs</h1>
          <p class="auth-gate-sub">Sign in or create an engineering account to access interactive labs, isolated code sandboxes, and persistent progress telemetry.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    _, mid_col, _ = st.columns([1.2, 2.0, 1.2])
    with mid_col:
        tab_in, tab_up = st.tabs(["Sign In", "Create Account"])
        with tab_in:
            with st.form("gate_login_form", clear_on_submit=False):
                u_in = st.text_input("Username", key="gate_login_user", placeholder="engineer_id")
                p_in = st.text_input("Password", type="password", key="gate_login_pass")
                if st.form_submit_button("Sign In", type="primary", use_container_width=True):
                    ok, msg = persistence.authenticate_user(u_in, p_in)
                    if ok:
                        persistence.set_authenticated_user(msg)
                        st.rerun()
                    else:
                        st.error(msg)
        with tab_up:
            with st.form("gate_register_form", clear_on_submit=True):
                u_reg = st.text_input("Choose Username", key="gate_reg_user", placeholder="3-32 chars [a-zA-Z0-9._-]")
                p_reg = st.text_input("Password", type="password", key="gate_reg_pass", placeholder="At least 8 characters")
                if st.form_submit_button("Create Account & Enter", type="primary", use_container_width=True):
                    ok, msg = persistence.register_user(u_reg, p_reg)
                    if ok:
                        persistence.set_authenticated_user(msg)
                        st.rerun()
                    else:
                        st.error(msg)


def render_top_bar(active_subj: str, global_stats: Dict[str, Any], display_label: str) -> None:
    """Renders the compact Obsidian/Zinc top navigation header."""
    with st.container(border=True):
        c_brand, c_xp = st.columns([3.4, 2.3], vertical_alignment="center")
        with c_brand:
            st.markdown(
                """
                <div class="master-brand">
                  <div class="brand-mark">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#A5B4FC" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <polyline points="8 6 2 12 8 18"></polyline>
                      <polyline points="16 6 22 12 16 18"></polyline>
                      <line x1="14" y1="4" x2="10" y2="20"></line>
                    </svg>
                  </div>
                  <div>
                    <div class="brand-title">Engineering Story Labs</div>
                    <div class="brand-subtitle">Interactive Systems, Algorithms &amp; Architecture Workbench</div>
                  </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with c_xp:
            safe_rank = html.escape(str(global_stats["rank"]))
            safe_user = html.escape(str(display_label))
            st.markdown(
                f"""
                <div class="nav-xp-wrap">
                  <div class="nav-xp-badge">
                    <span class="xp-points">{global_stats['total_xp']:,} XP</span>
                    <span class="xp-rank">{safe_rank}</span>
                    <span class="xp-user-tag">{safe_user}</span>
                  </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown('<div class="top-nav-divider"></div>', unsafe_allow_html=True)

        nav_cols = st.columns([0.98, 0.90, 0.72, 0.72, 0.90, 1.12, 0.80, 1.16, 0.98], gap="small")
        with nav_cols[0]:
            if st.button(
                "All Tracks",
                key="top_nav_home",
                use_container_width=True,
                type="primary" if active_subj == "home" else "secondary",
            ):
                _navigate_to("home", None)
                st.rerun()

        for idx, (sid, meta) in enumerate(loader.SUBJECT_REGISTRY.items()):
            with nav_cols[idx + 1]:
                nav_label = f"{meta.get('icon', '')} {meta['short_name']}"
                if st.button(
                    nav_label,
                    key=f"top_nav_{sid}",
                    use_container_width=True,
                    type="primary" if active_subj == sid else "secondary",
                ):
                    _navigate_to(sid, None)
                    st.rerun()


def render_sidebar(
    active_subj: str,
    active_case: Optional[int],
    global_stats: Dict[str, Any],
    display_label: str,
    is_authenticated: bool,
) -> None:
    """Renders the fixed left navigation rail, module navigator, and safe reset controls."""
    with st.sidebar:
        pct = global_stats["global_pct"]
        safe_rank = html.escape(str(global_stats["rank"]))
        safe_user = html.escape(str(display_label))
        st.markdown(
            f"""
            <div class="sidebar-profile-card">
              <div class="sidebar-section-label" style="margin-top:0;">Workspace Telemetry</div>
              <div style="font-size:1.05rem;font-weight:700;color:#FAFAFA;">{safe_rank}</div>
              <div style="font-size:0.76rem;color:#71717A;margin-top:2px;">Account: {safe_user}</div>
              <div style="display:flex;justify-content:space-between;margin-top:10px;font-size:0.82rem;">
                <span style="color:#A1A1AA;">Total XP</span>
                <span style="color:#A5B4FC;font-weight:700;font-family:'JetBrains Mono',monospace;">{global_stats['total_xp']:,} XP</span>
              </div>
              <div style="display:flex;justify-content:space-between;margin-top:4px;font-size:0.82rem;">
                <span style="color:#A1A1AA;">Completed</span>
                <span style="color:#34D399;font-weight:700;font-family:'JetBrains Mono',monospace;">{global_stats['total_completed']} / {global_stats['total_cases']} ({pct}%)</span>
              </div>
              <div class="progress-track-outer">
                <div class="progress-track-fill" style="width:{pct}%;"></div>
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        _render_account_controls(display_label, is_authenticated)

        st.markdown('<div class="sidebar-section-label">Track Switcher</div>', unsafe_allow_html=True)
        subj_options = ["home"] + list(loader.SUBJECT_REGISTRY.keys())
        subj_labels = {"home": "All Tracks Overview"}
        for sid, meta in loader.SUBJECT_REGISTRY.items():
            subj_labels[sid] = meta["name"]

        st.session_state["sidebar_subj_select"] = active_subj if active_subj in subj_options else "home"
        st.selectbox(
            "Track Switcher",
            options=subj_options,
            format_func=lambda x: subj_labels.get(x, x),
            key="sidebar_subj_select",
            label_visibility="collapsed",
            on_change=_on_sidebar_subject_change,
        )

        if active_subj != "home" and active_subj in loader.SUBJECT_REGISTRY:
            data = loader.load_subject_data(active_subj)
            meta = loader.SUBJECT_REGISTRY[active_subj]
            stories = data["stories"]
            comp_cnt, total_cnt, _, xp_subj = persistence.get_subject_stats(active_subj, len(stories))

            st.markdown('<div class="sidebar-section-label">Case Jumper</div>', unsafe_allow_html=True)
            case_options = ["Select a case..."] + [f"Case {c['id']:02d}: {c['title']}" for c in stories]
            jumper_key = f"case_jumper_{active_subj}"
            if active_case is not None:
                matched_label = "Select a case..."
                for c in stories:
                    if c["id"] == active_case:
                        matched_label = f"Case {c['id']:02d}: {c['title']}"
                        break
                st.session_state[jumper_key] = matched_label
            else:
                st.session_state[jumper_key] = "Select a case..."

            st.selectbox(
                "Select Case",
                options=case_options,
                key=jumper_key,
                label_visibility="collapsed",
                on_change=_on_case_jumper_change,
                args=(active_subj,),
            )

            if active_case is not None and active_case in data["stories_by_id"]:
                episodes = loader.get_case_modules(active_subj, active_case)
                total_mods = max(1, len(episodes))
                unlocked_up_to = min(total_mods, persistence.get_active_module(active_subj, active_case))
                is_solved = active_case in st.session_state.get("completed", {}).get(active_subj, set())
                completed_mods_set = st.session_state.get("completed_modules", set())

                mod_state_key = f"active_mod_{active_subj}_{active_case}"
                viewing_mod = st.session_state.get(mod_state_key, unlocked_up_to)
                viewing_mod = max(1, min(int(viewing_mod), total_mods))

                st.markdown(
                    f'<div class="sidebar-section-label">Case {active_case:02d} Modules</div>',
                    unsafe_allow_html=True,
                )
                for m in range(1, total_mods + 1):
                    is_unlocked = (m <= unlocked_up_to) or is_solved
                    is_mod_done = is_solved or (f"{active_subj}_{active_case}_m{m}" in completed_mods_set)
                    if m == viewing_mod:
                        btn_lbl = f"Module {m} · Active"
                    elif is_mod_done:
                        btn_lbl = f"Module {m} · Done"
                    elif is_unlocked:
                        btn_lbl = f"Module {m}"
                    else:
                        btn_lbl = f"Module {m} · Locked"
                    if st.button(
                        btn_lbl,
                        key=f"sb_mod_{active_subj}_{active_case}_{m}",
                        use_container_width=True,
                        type="primary" if m == viewing_mod else "secondary",
                        disabled=not is_unlocked,
                    ):
                        st.session_state[mod_state_key] = m
                        st.rerun()
            else:
                st.markdown(
                    f'<div class="sidebar-section-label">{html.escape(meta["short_name"])} Progress</div>',
                    unsafe_allow_html=True,
                )
                st.caption(f"{xp_subj} XP  |  {comp_cnt} / {total_cnt} Solved")

        st.markdown("---")
        with st.expander("Workspace Administration", expanded=False):
            reset_nonce = st.session_state.get("_reset_nonce", 0)
            confirm_reset = st.checkbox(
                "Confirm progress reset for this workspace",
                key=f"confirm_workspace_reset_{reset_nonce}",
            )
            if active_subj != "home" and active_subj in loader.SUBJECT_REGISTRY:
                short_n = loader.SUBJECT_REGISTRY[active_subj]["short_name"]
                if st.button(
                    f"Reset {short_n} Progress",
                    key="reset_subj_btn",
                    use_container_width=True,
                    disabled=not confirm_reset,
                ):
                    persistence.reset_subject_progress(active_subj)
                    st.session_state["_reset_nonce"] = reset_nonce + 1
                    st.rerun()
            if st.button(
                "Reset All Workspace Progress",
                key="reset_all_btn",
                use_container_width=True,
                disabled=not confirm_reset,
            ):
                persistence.reset_all_progress()
                st.session_state["_reset_nonce"] = reset_nonce + 1
                _navigate_to("home", None)
                st.rerun()


def _svg_progress_ring(pct: int, color: str) -> str:
    """Renders a crisp 20x20 inline SVG circular mastery gauge."""
    clamped = max(0, min(100, int(pct)))
    radius = 7.5
    circ = 2 * 3.14159 * radius
    offset = circ * (1.0 - clamped / 100.0)
    return (
        f'<svg width="20" height="20" viewBox="0 0 20 20" aria-hidden="true">'
        f'<circle cx="10" cy="10" r="{radius}" fill="none" stroke="#23232C" stroke-width="2.2"/>'
        f'<circle cx="10" cy="10" r="{radius}" fill="none" stroke="{html.escape(color)}" stroke-width="2.2" '
        f'stroke-dasharray="{circ:.2f}" stroke-dashoffset="{offset:.2f}" stroke-linecap="round" '
        f'transform="rotate(-90 10 10)"/>'
        f'</svg>'
    )


def _rank_progress_info(total_xp: int) -> tuple:
    tiers = [
        (0, 100, "Apprentice", "Associate Engineer"),
        (100, 400, "Associate Engineer", "Systems Engineer II"),
        (400, 1000, "Systems Engineer II", "Senior Engineer"),
        (1000, 2000, "Senior Engineer", "Staff Engineer"),
        (2000, 4000, "Staff Engineer", "Principal Architect"),
    ]
    for lo, hi, cur_r, next_r in tiers:
        if total_xp < hi:
            pct = int(((total_xp - lo) / max(1, hi - lo)) * 100)
            return cur_r, next_r, max(0, min(100, pct)), hi - total_xp
    return "Principal Architect", "Max Tier", 100, 0


def _diff_chip_class(diff_str: str) -> str:
    low = (diff_str or "").lower()
    if "expert" in low:
        return "diff-expert"
    if "advanced" in low:
        return "diff-adv"
    if "intermediate" in low:
        return "diff-inter"
    return "diff-beginner"


def render_master_hub(all_subjects: List[Dict[str, Any]], global_stats: Dict[str, Any]) -> None:
    """Renders the advanced Obsidian/Zinc engineering workbench dashboard."""
    total_modules = sum(
        len(loader.get_case_modules(s["meta"]["id"], st_item["id"]))
        for s in all_subjects
        for st_item in s["stories"]
    )
    st.markdown(
        f"""
        <div class="hub-header-strip">
          <div>
            <h1 class="hub-header-title">Interactive Engineering Case Labs</h1>
            <p class="hub-header-sub">
              Production incident investigations, online Python &amp; C++ algorithm judges, SQL sandboxes, and system capacity labs.
            </p>
          </div>
          <div class="hub-stat-bar">
            <div class="hub-stat-item">
              <div class="hub-stat-label">Disciplines</div>
              <div class="hub-stat-value">{len(all_subjects)}</div>
            </div>
            <div class="hub-stat-item">
              <div class="hub-stat-label">Labs</div>
              <div class="hub-stat-value">{global_stats['total_cases']}</div>
            </div>
            <div class="hub-stat-item">
              <div class="hub-stat-label">Modules</div>
              <div class="hub-stat-value">{total_modules}</div>
            </div>
            <div class="hub-stat-item">
              <div class="hub-stat-label">Solved</div>
              <div class="hub-stat-value" style="color:#34D399;">{global_stats['total_completed']}</div>
            </div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    cur_rank, next_rank, rank_pct, xp_rem = _rank_progress_info(global_stats["total_xp"])
    rank_detail = (
        f"{xp_rem:,} XP to <strong>{html.escape(next_rank)}</strong>"
        if xp_rem > 0
        else "Top engineering tier unlocked"
    )
    st.markdown(
        f"""
        <div class="rank-strip">
          <div class="rank-meta">
            <span class="rank-badge-pill">{html.escape(cur_rank)}</span>
            <span>{rank_detail}</span>
          </div>
          <div class="rank-bar-wrap">
            <div class="rank-bar-outer"><div class="rank-bar-fill" style="width:{rank_pct}%;"></div></div>
            <span style="font-family:'JetBrains Mono',monospace;font-size:0.74rem;color:#A1A1AA;">{rank_pct}%</span>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 8-Track Live Mastery Ribbon
    seg_html = []
    for subj_bundle in all_subjects:
        m_meta = subj_bundle["meta"]
        m_sid = m_meta["id"]
        c_cnt, t_cnt, m_pct, _ = persistence.get_subject_stats(m_sid, len(subj_bundle["stories"]))
        m_col = html.escape(m_meta["color"])
        seg_html.append(
            f'<div class="mastery-seg" style="--seg-color:{m_col};">'
            f'<div class="mastery-seg-top"><span>{html.escape(m_meta.get("icon", ""))} {html.escape(m_meta["short_name"])}</span>'
            f'<span style="color:#A1A1AA;font-family:\'JetBrains Mono\',monospace;">{c_cnt}/{t_cnt}</span></div>'
            f'<div class="mastery-seg-bar"><div class="mastery-seg-fill" style="width:{m_pct}%;"></div></div>'
            f'</div>'
        )
    st.markdown(f'<div class="mastery-ribbon">{"".join(seg_html)}</div>', unsafe_allow_html=True)

    resume = global_stats.get("last_activity")
    if isinstance(resume, dict) and resume.get("subject") in loader.SUBJECT_REGISTRY:
        r_sid = resume["subject"]
        r_cid = int(resume["case_id"])
        r_mod = int(resume.get("module", 1))
        r_meta = loader.SUBJECT_REGISTRY[r_sid]
        r_data = loader.load_subject_data(r_sid)
        r_story = r_data["stories_by_id"].get(r_cid)
        if r_story:
            r_col1, r_col2 = st.columns([4.4, 1.3], vertical_alignment="center")
            with r_col1:
                st.markdown(
                    f"""
                    <div class="resume-box">
                      <div class="resume-label">Resume Active Investigation</div>
                      <div class="resume-title">{html.escape(r_meta['short_name'])} &middot; Case {r_cid:02d}: {html.escape(r_story['title'])} &middot; Module {r_mod}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            with r_col2:
                if st.button("Resume Lab", key="hub_resume_btn", type="primary", use_container_width=True):
                    _navigate_to(r_sid, r_cid, r_mod)
                    st.rerun()

    # Quick Cross-Track Lab Finder
    hub_q = st.text_input(
        "Quick Finder",
        placeholder=f"Quick search across all {global_stats['total_cases']} labs (e.g., B+ Tree, Kadane, Wiener, Rate Limiter, RAII)...",
        label_visibility="collapsed",
        key="hub_global_search",
    ).strip().lower()

    if hub_q:
        matches = []
        for s_bundle in all_subjects:
            s_meta = s_bundle["meta"]
            s_id = s_meta["id"]
            for st_item in s_bundle["stories"]:
                topics_str = " ".join(st_item.get("topics", []))
                hay = f"{s_meta['short_name']} {st_item['id']:02d} {st_item['title']} {st_item.get('hook', '')} {st_item.get('primary', '')} {topics_str}".lower()
                if hub_q in hay:
                    matches.append((s_meta, st_item))
        st.caption(f"Found {len(matches)} matching lab(s) across all disciplines" + (" (showing top 9):" if len(matches) > 9 else ":"))
        for row_s in range(0, min(len(matches), 9), 3):
            qcols = st.columns(3, gap="medium")
            for qi in range(3):
                if row_s + qi >= min(len(matches), 9):
                    break
                m_meta, m_story = matches[row_s + qi]
                m_sid = m_meta["id"]
                m_cid = int(m_story["id"])
                m_color = html.escape(m_meta["color"])
                with qcols[qi]:
                    st.markdown(
                        f"""
                        <div class="case-catalog-card" style="--track-accent:{m_color};min-height:168px;">
                          <div>
                            <div class="case-card-top">
                              <span class="case-num-pill">{html.escape(m_meta.get('icon', ''))} {html.escape(m_meta['short_name'])} &middot; CASE {m_cid:02d}</span>
                              <span class="stat-pill">{html.escape(str(m_story.get('difficulty', 'Core')))}</span>
                            </div>
                            <div class="case-card-title">{html.escape(str(m_story['title']))}</div>
                            <div class="case-card-meta">{html.escape(str(m_story.get('hook') or m_story.get('primary') or ''))}</div>
                          </div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
                    if st.button(f"Launch {m_meta['short_name']} #{m_cid:02d}", key=f"qjump_{m_sid}_{m_cid}", use_container_width=True):
                        _navigate_to(m_sid, m_cid)
                        st.rerun()

    st.markdown(
        '<div style="font-size:1.10rem;font-weight:700;letter-spacing:-0.015em;color:#FAFAFA;margin:14px 0 10px 0;">Curriculum Tracks</div>',
        unsafe_allow_html=True,
    )

    for row_start in range(0, len(all_subjects), 3):
        cols = st.columns(3, gap="medium")
        for i in range(3):
            if row_start + i >= len(all_subjects):
                break
            subj_bundle = all_subjects[row_start + i]
            meta = subj_bundle["meta"]
            sid = meta["id"]
            track_num = row_start + i + 1
            comp_cnt, total_cnt, _, subj_xp = persistence.get_subject_stats(sid, len(subj_bundle["stories"]))
            tags_html = "".join([f'<span class="tag-pill">{html.escape(t)}</span>' for t in meta["tags"][:3]])

            with cols[i]:
                safe_icon = html.escape(meta.get("icon", ""))
                safe_color = html.escape(meta["color"])
                progress_pct = int((comp_cnt / max(1, total_cnt)) * 100)
                ring_svg = _svg_progress_ring(progress_pct, meta["color"])
                st.markdown(
                    f"""
                    <div class="subject-deck-card" style="--track-accent:{safe_color};">
                      <div>
                        <div class="subject-card-top">
                          <span class="subject-track-meta">
                            <span class="subject-icon">{safe_icon}</span>
                            <span class="track-dot" style="background:{safe_color};"></span>
                            TRACK {track_num:02d}
                          </span>
                          <span class="svg-ring-wrap">{ring_svg}<span>{comp_cnt}/{total_cnt} &middot; {subj_xp} XP</span></span>
                        </div>
                        <div class="subject-card-title">{html.escape(meta['name'])}</div>
                        <div class="subject-card-tagline">{html.escape(meta['tagline'])}</div>
                      </div>
                      <div class="subject-meta-footer">
                        <div class="tag-container">{tags_html}</div>
                        <div class="card-progress-outer">
                          <div class="card-progress-fill" style="width:{progress_pct}%;background:{safe_color};"></div>
                        </div>
                      </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                if st.button(
                    f"Open {meta['short_name']}",
                    key=f"hub_enter_{sid}",
                    use_container_width=True,
                    type="primary",
                ):
                    _navigate_to(sid, None)
                    st.rerun()


def render_subject_catalog(subject_id: str) -> None:
    """Renders the case investigation grid for a selected engineering discipline."""
    meta = loader.SUBJECT_REGISTRY[subject_id]
    data = loader.load_subject_data(subject_id)
    stories = data["stories"]
    comp_cnt, total_cnt, _, xp_subj = persistence.get_subject_stats(subject_id, len(stories))
    completed_set = st.session_state.get("completed", {}).get(subject_id, set())

    safe_color = html.escape(meta["color"])
    st.markdown(
        f"""
        <div class="catalog-header" style="--track-accent:{safe_color};">
          <div>
            <div class="catalog-header-meta">
              <span class="track-dot" style="background:{safe_color};"></span>
              <span>DISCIPLINE TRACK &middot; {html.escape(meta['short_name'].upper())}</span>
            </div>
            <h1 class="catalog-header-title">{html.escape(meta.get('icon', ''))} {html.escape(meta['name'])}</h1>
            <p class="catalog-header-sub">{html.escape(meta['tagline'])}</p>
          </div>
          <div class="hub-stat-bar">
            <div class="hub-stat-item">
              <div class="hub-stat-label">Cases</div>
              <div class="hub-stat-value">{total_cnt}</div>
            </div>
            <div class="hub-stat-item">
              <div class="hub-stat-label">Solved</div>
              <div class="hub-stat-value" style="color:#34D399;">{comp_cnt}</div>
            </div>
            <div class="hub-stat-item">
              <div class="hub-stat-label">Track XP</div>
              <div class="hub-stat-value" style="color:#A5B4FC;">{xp_subj}</div>
            </div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    f_col, s_col, d_col, v_col, b_col = st.columns([2.6, 1.15, 1.15, 0.9, 1.1], vertical_alignment="center")
    with f_col:
        search_q = st.text_input(
            "Filter cases",
            placeholder="Filter cases by title, topic, or case number...",
            label_visibility="collapsed",
            key=f"catalog_search_{subject_id}",
        ).strip().lower()
    with s_col:
        status_filter = st.selectbox(
            "Status Filter",
            options=["All Statuses", "In Progress", "Completed", "Pinned"],
            label_visibility="collapsed",
            key=f"catalog_status_{subject_id}",
        )
    with d_col:
        diff_filter = st.selectbox(
            "Difficulty Filter",
            options=["All Levels", "Beginner", "Intermediate", "Advanced", "Expert"],
            label_visibility="collapsed",
            key=f"catalog_diff_{subject_id}",
        )
    with v_col:
        view_mode = st.selectbox(
            "View Mode",
            options=["Grid View", "List View"],
            label_visibility="collapsed",
            key=f"catalog_view_{subject_id}",
        )
    with b_col:
        if st.button("Back to All Tracks", key=f"cat_back_{subject_id}", use_container_width=True):
            _navigate_to("home", None)
            st.rerun()

    filtered_cases = []
    for c in stories:
        cid = int(c["id"])
        is_solved = cid in completed_set
        active_m = persistence.get_active_module(subject_id, cid)
        is_pinned = persistence.is_case_bookmarked(subject_id, cid)
        if status_filter == "Completed" and not is_solved:
            continue
        if status_filter == "In Progress" and (is_solved or active_m <= 1):
            continue
        if status_filter == "Pinned" and not is_pinned:
            continue
        if diff_filter != "All Levels" and diff_filter.lower() not in str(c.get("difficulty", "")).lower():
            continue
        topics_str = " ".join(c.get("topics", []))
        haystack = f"{cid:02d} {c['title']} {c.get('hook', '')} {c.get('primary', '')} {topics_str}".lower()
        if not search_q or search_q in haystack:
            filtered_cases.append(c)

    if not filtered_cases:
        st.info("No matching cases found for your current search or filter.")
        return

    if view_mode == "List View":
        for c in filtered_cases:
            cid = int(c["id"])
            episodes = loader.get_case_modules(subject_id, cid)
            total_mods = max(1, len(episodes))
            active_mod = persistence.get_active_module(subject_id, cid)
            is_solved = cid in completed_set
            is_pinned = persistence.is_case_bookmarked(subject_id, cid)
            status_cls = "case-status-done" if is_solved else "case-status-open"
            status_text = "COMPLETED" if is_solved else f"{min(active_mod, total_mods)}/{total_mods} MODS"
            diff_str = str(c.get("difficulty", "Core"))
            d_cls = _diff_chip_class(diff_str)
            pin_html = '<span class="case-pinned-pill">PINNED</span>' if is_pinned else ""
            lc1, lc2 = st.columns([5.2, 1.1], vertical_alignment="center")
            with lc1:
                st.markdown(
                    f'<div class="compact-case-row">'
                    f'<span style="display:flex;align-items:center;gap:10px;min-width:0;">'
                    f'<span class="case-num-pill">CASE {cid:02d}</span>'
                    f'<strong style="color:#FAFAFA;font-size:0.93rem;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">{html.escape(str(c["title"]))}</strong>'
                    f'</span>'
                    f'<span style="display:inline-flex;align-items:center;gap:6px;flex-shrink:0;">'
                    f'{pin_html}<span class="diff-chip {d_cls}">{html.escape(diff_str)}</span>'
                    f'<span class="case-status-pill {status_cls}">{status_text}</span>'
                    f'</span></div>',
                    unsafe_allow_html=True,
                )
            with lc2:
                if st.button(f"Open Case {cid:02d}", key=f"list_enter_{subject_id}_{cid}", use_container_width=True, type="primary"):
                    _navigate_to(subject_id, cid, min(active_mod, total_mods))
                    st.rerun()
        return

    for row_start in range(0, len(filtered_cases), 2):
        cols = st.columns(2, gap="medium")
        for i in range(2):
            if row_start + i >= len(filtered_cases):
                break
            c = filtered_cases[row_start + i]
            cid = int(c["id"])
            episodes = loader.get_case_modules(subject_id, cid)
            total_mods = max(1, len(episodes))
            active_mod = persistence.get_active_module(subject_id, cid)
            is_solved = cid in completed_set
            is_pinned = persistence.is_case_bookmarked(subject_id, cid)

            status_cls = "case-status-done" if is_solved else "case-status-open"
            status_text = "COMPLETED" if is_solved else f"{min(active_mod, total_mods)}/{total_mods} MODS"
            pin_html = '<span class="case-pinned-pill">PINNED</span>' if is_pinned else ""

            summary_raw = c.get("hook") or c.get("opening") or c.get("primary") or "Interactive engineering investigation."
            summary_clean = html.escape(str(summary_raw))
            primary_lbl = html.escape(str(c.get("primary") or c.get("genre") or "Systems Lab"))
            diff_val = str(c.get("difficulty", "Core"))
            d_cls = _diff_chip_class(diff_val)

            mod_progress_pct = int((min(active_mod, total_mods) / max(1, total_mods)) * 100) if not is_solved else 100

            with cols[i]:
                st.markdown(
                    f"""
                    <div class="case-catalog-card" style="--track-accent:{safe_color};">
                      <div>
                        <div class="case-card-top">
                          <span class="case-num-pill">CASE {cid:02d}</span>
                          <span style="display:inline-flex;gap:6px;align-items:center;">{pin_html}<span class="diff-chip {d_cls}">{html.escape(diff_val)}</span><span class="case-status-pill {status_cls}">{status_text}</span></span>
                        </div>
                        <div class="case-card-title">{html.escape(str(c['title']))}</div>
                        <div class="case-card-meta">{summary_clean}</div>
                      </div>
                      <div class="case-card-stats">
                        <span class="stat-pill">{total_mods} Modules</span>
                        <span class="stat-pill">{primary_lbl}</span>
                      </div>
                      <div class="card-progress-outer">
                        <div class="card-progress-fill" style="width:{mod_progress_pct}%;background:{safe_color};"></div>
                      </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                if st.button(
                    f"Open Case {cid:02d}",
                    key=f"enter_case_{subject_id}_{cid}",
                    use_container_width=True,
                    type="primary",
                ):
                    _navigate_to(subject_id, cid, min(active_mod, total_mods))
                    st.rerun()


def render_case_investigation(subject_id: str, case_id: int) -> None:
    """Renders an interactive multi-module engineering case workspace."""
    meta = loader.SUBJECT_REGISTRY[subject_id]
    data = loader.load_subject_data(subject_id)

    if case_id not in data["stories_by_id"]:
        st.warning(f"Case {case_id:02d} does not exist in {meta['short_name']}.")
        if st.button("Return to Track Catalog", key="missing_case_back"):
            _navigate_to(subject_id, None)
            st.rerun()
        return

    story = data["stories_by_id"][case_id]
    episodes = loader.get_case_modules(subject_id, case_id)
    total_mods = len(episodes)
    if total_mods == 0:
        st.warning("This case has no modules configured.")
        return

    unlocked_up_to = min(total_mods, persistence.get_active_module(subject_id, case_id))
    case_solved = case_id in st.session_state.get("completed", {}).get(subject_id, set())
    completed_mods_set = st.session_state.get("completed_modules", set())

    mod_state_key = f"active_mod_{subject_id}_{case_id}"
    viewing_mod = st.session_state.get(mod_state_key, unlocked_up_to)
    viewing_mod = max(1, min(int(viewing_mod), total_mods))
    st.session_state[mod_state_key] = viewing_mod

    persistence.set_active_module(subject_id, case_id, viewing_mod)

    # Clean Breadcrumb Bar with Prev/Next Case switcher & Bookmark toggle
    all_cids = [int(s["id"]) for s in data["stories"]]
    cur_pos = all_cids.index(case_id) if case_id in all_cids else -1
    prev_cid = all_cids[cur_pos - 1] if cur_pos > 0 else None
    next_cid = all_cids[cur_pos + 1] if 0 <= cur_pos < len(all_cids) - 1 else None

    bc1, bc2, bc3, bc_prev, bc_next, bc4 = st.columns([1.05, 1.45, 2.55, 0.72, 0.72, 1.05], gap="small", vertical_alignment="center")
    with bc1:
        if st.button("All Tracks", key="bc_home_btn", use_container_width=True):
            _navigate_to("home", None)
            st.rerun()
    with bc2:
        if st.button(f"{meta['short_name']} Catalog", key="bc_subj_btn", use_container_width=True):
            _navigate_to(subject_id, None)
            st.rerun()
    with bc3:
        st.markdown(
            f'<div style="color:#A1A1AA;font-size:0.85rem;padding-left:6px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">'
            f'{html.escape(meta.get("icon", ""))} Case {case_id:02d} &middot; <strong style="color:#FAFAFA;">{html.escape(story["title"])}</strong></div>',
            unsafe_allow_html=True,
        )
    with bc_prev:
        if st.button("← Prev", key=f"prev_case_{subject_id}_{case_id}", disabled=(prev_cid is None), use_container_width=True):
            _navigate_to(subject_id, prev_cid)
            st.rerun()
    with bc_next:
        if st.button("Next →", key=f"next_case_{subject_id}_{case_id}", disabled=(next_cid is None), use_container_width=True):
            _navigate_to(subject_id, next_cid)
            st.rerun()
    with bc4:
        is_pinned = persistence.is_case_bookmarked(subject_id, case_id)
        if st.button("★ Pinned" if is_pinned else "☆ Pin Case", key=f"pin_btn_{subject_id}_{case_id}", use_container_width=True):
            persistence.toggle_bookmark(subject_id, case_id)
            st.rerun()

    ep_idx = min(viewing_mod - 1, total_mods - 1)
    current_ep = episodes[ep_idx]
    ep_title = html.escape(str(current_ep.get("title", f"Module {viewing_mod}")))
    safe_color = html.escape(meta["color"])
    case_pct = int((viewing_mod / max(1, total_mods)) * 100)
    topics_chips = "".join(f'<span class="topic-chip">{html.escape(str(t))}</span>' for t in story.get("topics", [])[:6])
    diff_str = str(story.get("difficulty", "Core"))
    d_cls = _diff_chip_class(diff_str)

    st.markdown(
        f"""
        <div class="case-header-bar" style="--track-accent:{safe_color};">
          <div class="case-header-kicker">{html.escape(meta.get('icon', ''))} {html.escape(meta['short_name'].upper())} &middot; CASE {case_id:02d} &middot; MODULE {viewing_mod} OF {total_mods}</div>
          <h1 class="case-header-title">{html.escape(story['title'])}</h1>
          <div class="case-header-meta">{ep_title}</div>
          <div class="topic-chip-row"><span class="diff-chip {d_cls}">{html.escape(diff_str)}</span>{topics_chips}</div>
          <div class="card-progress-outer" style="margin-top:12px;">
            <div class="card-progress-fill" style="width:{case_pct}%;background:{safe_color};"></div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    mod_cols = st.columns(total_mods, gap="small")
    for m in range(1, total_mods + 1):
        is_unlocked = (m <= unlocked_up_to) or case_solved
        is_mod_done = case_solved or (f"{subject_id}_{case_id}_m{m}" in completed_mods_set)
        with mod_cols[m - 1]:
            if m == viewing_mod:
                tab_label = f"Mod {m} · Active"
            elif is_mod_done:
                tab_label = f"Mod {m} · Done"
            elif is_unlocked:
                tab_label = f"Mod {m}"
            else:
                tab_label = f"Mod {m} · Locked"
            if st.button(
                tab_label,
                key=f"mod_tab_{subject_id}_{case_id}_{m}",
                use_container_width=True,
                type="primary" if m == viewing_mod else "secondary",
                disabled=not is_unlocked,
            ):
                st.session_state[mod_state_key] = m
                st.rerun()

    st.markdown('<div class="top-nav-divider" style="margin:10px 0 18px 0;"></div>', unsafe_allow_html=True)

    for b_idx, block in enumerate(current_ep.get("blocks", [])):
        ui.render_block(block, subject_id, case_id, viewing_mod, b_idx)

    st.markdown('<div class="top-nav-divider" style="margin:26px 0 16px 0;"></div>', unsafe_allow_html=True)
    foot_l, foot_r = st.columns([3.0, 2.2], vertical_alignment="center")
    with foot_l:
        if viewing_mod > 1:
            if st.button("Previous Module", key=f"prev_mod_{subject_id}_{case_id}_{viewing_mod}"):
                st.session_state[mod_state_key] = viewing_mod - 1
                st.rerun()
    with foot_r:
        if viewing_mod < unlocked_up_to:
            if st.button(
                "Next Module",
                key=f"next_mod_{subject_id}_{case_id}_{viewing_mod}",
                type="primary",
                use_container_width=True,
            ):
                st.session_state[mod_state_key] = viewing_mod + 1
                st.rerun()
        elif viewing_mod < total_mods:
            if st.button(
                "Complete Module & Continue",
                key=f"unlock_mod_{subject_id}_{case_id}_{viewing_mod}",
                type="primary",
                use_container_width=True,
            ):
                persistence.complete_module(subject_id, case_id, viewing_mod, total_mods)
                st.session_state[mod_state_key] = viewing_mod + 1
                st.rerun()
        elif not case_solved:
            if st.button(
                "Complete Case & Claim Final XP",
                key=f"finish_case_{subject_id}_{case_id}",
                type="primary",
                use_container_width=True,
            ):
                persistence.complete_module(subject_id, case_id, viewing_mod, total_mods)
                st.success("Case investigation completed and final XP recorded.")
                st.rerun()
        else:
            if st.button(
                "Case Completed · Back to Catalog",
                key=f"done_back_{subject_id}_{case_id}",
                type="primary",
                use_container_width=True,
            ):
                _navigate_to(subject_id, None)
                st.rerun()


def main() -> None:
    """Application entrypoint with CSS injection, auth gate, and safe error boundary."""
    ui.inject_master_css()
    sync_query_params()

    if st.session_state.get("_invalid_param_notice"):
        st.warning(st.session_state.pop("_invalid_param_notice"))

    user_key, display_label, is_authenticated = persistence.get_current_identity()
    if persistence.get_auth_mode() == "required" and not user_key:
        render_auth_gate()
        return

    try:
        all_subjects = [loader.load_subject_data(sid) for sid in loader.SUBJECT_REGISTRY]
        global_stats = persistence.get_global_stats(all_subjects)
        active_subj = st.session_state.get("nav_subject", "home")
        if active_subj not in VALID_SUBJECTS:
            active_subj = "home"
            st.session_state["nav_subject"] = "home"
        active_case = st.session_state.get("nav_case", None)
        update_query_params(active_subj, active_case)

        render_top_bar(active_subj, global_stats, display_label)
        render_sidebar(active_subj, active_case, global_stats, display_label, is_authenticated)

        if active_subj == "home":
            render_master_hub(all_subjects, global_stats)
        elif active_case is not None:
            render_case_investigation(active_subj, int(active_case))
        else:
            render_subject_catalog(active_subj)
    except Exception:
        logger.exception("Unhandled error during page rendering")
        st.error("An unexpected rendering error occurred. Your progress has been preserved.")
        if st.button("Return to All Tracks", key="fatal_recover_btn"):
            _navigate_to("home", None)
            st.rerun()


main()
