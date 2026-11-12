"""
Master UI & Design System for the Unified Engineering Learning Platform.
Delivers executive-tier, responsive, dark glassmorphism aesthetic across all 5 disciplines.
"""

import streamlit as st
import streamlit.components.v1 as components
import markdown
import html
import re
import time
import functools
from typing import Dict, Any, List, Optional
import runners
import unified_persistence as persistence
from core_loader import SUBJECT_REGISTRY, get_all_subject_metas

_LATEX_SYMBOLS = {
    "\\xrightarrow": "→",
    "\\rightarrow": "→",
    "\\leftarrow": "←",
    "\\implies": "⇒",
    "\\mapsto": "↦",
    "\\iff": "⇔",
    "\\to": "→",
    "\\neg": "¬",
    "\\land": "∧",
    "\\wedge": "∧",
    "\\lor": "∨",
    "\\forall": "∀",
    "\\exists": "∃",
    "\\models": "⊨",
    "\\notin": "∉",
    "\\in": "∈",
    "\\subseteq": "⊆",
    "\\subset": "⊂",
    "\\bigcup": "⋃",
    "\\cup": "∪",
    "\\setminus": "∖",
    "\\neq": "≠",
    "\\le": "≤",
    "\\ge": "≥",
    "\\approx": "≈",
    "\\equiv": "≡",
    "\\propto": "∝",
    "\\pm": "±",
    "\\times": "×",
    "\\cdot": "·",
    "\\circ": "∘",
    "\\odot": "⊙",
    "\\infty": "∞",
    "\\sum": "∑",
    "\\prod": "∏",
    "\\int": "∫",
    "\\partial": "∂",
    "\\nabla": "∇",
    "\\Delta": "Δ",
    "\\Sigma": "Σ",
    "\\Theta": "Θ",
    "\\Omega": "Ω",
    "\\alpha": "α",
    "\\beta": "β",
    "\\gamma": "γ",
    "\\delta": "δ",
    "\\epsilon": "ε",
    "\\eta": "η",
    "\\theta": "θ",
    "\\omega": "ω",
    "\\oplus": "⊕",
    "\\lfloor": "⌊",
    "\\rfloor": "⌋",
    "\\lceil": "⌈",
    "\\rceil": "⌉",
    "\\ll": "≪",
    "\\gg": "≫",
    "\\lambda": "λ",
    "\\mu": "μ",
    "\\nu": "ν",
    "\\pi": "π",
    "\\sigma": "σ",
    "\\phi": "φ",
    "\\dots": "…",
    "\\langle": "⟨",
    "\\rangle": "⟩",
    "\\parallel": "∥",
    "\\mid": "|",
    "\\bullet": "•",
    "\\blacktriangleright": "▶",
    "\\triangleright": "▷",
    "\\triangle": "△",
    "\\blacklozenge": "◆",
    "\\diamondsuit": "◊",
    "\\lozenge": "◊",
    "\\square": "□",
    "\\Box": "□",
    "\\multimap": "⊸",
    "\\succ": "≻",
    "\\cos": "cos",
    "\\exp": "exp",
    "\\ln": "ln",
    "\\log": "log",
    "\\lim": "lim",
    "\\max": "max",
    "\\min": "min",
    "\\arg": "arg",
    "\\quad": "  ",
    "\\left": "",
    "\\right": "",
}
_LATEX_SORTED_KEYS = sorted(_LATEX_SYMBOLS.keys(), key=len, reverse=True)

def _extract_braced(s: str, pos: int):
    if pos >= len(s) or s[pos] != "{":
        return None, pos
    depth = 0
    for i in range(pos, len(s)):
        if s[i] == "{":
            depth += 1
        elif s[i] == "}":
            depth -= 1
            if depth == 0:
                return s[pos + 1:i], i + 1
    return None, pos

def _replace_cmd_with_args(s: str, cmd: str, formatter) -> str:
    out = []
    i = 0
    n = len(s)
    while i < n:
        if s.startswith(cmd, i) and (i + len(cmd) >= n or not s[i + len(cmd)].isalpha()):
            j = i + len(cmd)
            while j < n and s[j] == " ":
                j += 1
            arg1, j1 = _extract_braced(s, j)
            if arg1 is not None:
                replaced, next_i = formatter(arg1, s, j1)
                out.append(replaced)
                i = next_i
                continue
        out.append(s[i])
        i += 1
    return "".join(out)

def _latex_to_html(expr: str) -> str:
    s = html.escape(expr.strip(), quote=False)
    for wrapper in ("\\overbrace", "\\underbrace", "\\hat", "\\bar", "\\dot", "\\norm", "\\text", "\\mathrm", "\\mathcal"):
        s = _replace_cmd_with_args(s, wrapper, lambda a, _s, j: (a, j))
    for bold_w in ("\\mathbf", "\\mathbb"):
        s = _replace_cmd_with_args(s, bold_w, lambda a, _s, j: (f"<b>{a}</b>", j))
    s = _replace_cmd_with_args(s, "\\xrightarrow", lambda a, _s, j: (f"→[{a}]", j))
    s = _replace_cmd_with_args(s, "\\sqrt", lambda a, _s, j: (f"√({a})", j))
    def _frac_fmt(num, full, pos):
        while pos < len(full) and full[pos] == " ":
            pos += 1
        den, pos2 = _extract_braced(full, pos)
        if den is not None:
            return f"({num}) / ({den})", pos2
        return num, pos
    s = _replace_cmd_with_args(s, "\\frac", _frac_fmt)
    for k in _LATEX_SORTED_KEYS:
        s = s.replace(k, _LATEX_SYMBOLS[k])
    s = re.sub(r"\^\{([^{}]+)\}", r"<sup>\1</sup>", s)
    s = re.sub(r"\^([A-Za-z0-9*′+−\-])", r"<sup>\1</sup>", s)
    s = re.sub(r"_\{([^{}]+)\}", r"<sub>\1</sub>", s)
    s = re.sub(r"_([A-Za-z0-9]+)", r"<sub>\1</sub>", s)
    s = s.replace("\\{", "{").replace("\\}", "}")
    s = s.replace("{", "").replace("}", "")
    return s

def _is_valid_inline_math(inner: str) -> bool:
    if not inner or "\n" in inner:
        return False
    # Avoid treating currency values like "$100, then trying to withdraw $100" as math
    if inner[0].isdigit() and re.search(r",\s+[A-Za-z]|[A-Za-z]{2,}\s+[A-Za-z]{2,}", inner):
        return False
    if len(inner.split()) >= 4 and not re.search(r"[\\=^_<>|+*]", inner):
        return False
    if inner[0].isdigit() and not re.search(r"[\\=^_<>|+*/]", inner):
        return False
    return True

def clean_newlines(text: str, convert_guillemets: bool = True) -> str:
    if not text or not isinstance(text, str):
        return text
    if convert_guillemets:
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

_ALERT_STYLES = {
    "NOTE": ("note", "NOTE"),
    "TIP": ("tip", "PRO TIP"),
    "IMPORTANT": ("important", "IMPORTANT"),
    "WARNING": ("warning", "ENGINEERING WARNING"),
    "CAUTION": ("caution", "CAUTION"),
}

def _convert_github_alerts(text: str, stash_fn) -> str:
    lines = text.splitlines()
    out = []
    i = 0
    while i < len(lines):
        m = re.match(r"^\s*>\s*\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]\s*(.*)$", lines[i])
        if m:
            kind = m.group(1)
            body_lines = []
            if m.group(2).strip():
                body_lines.append(m.group(2).strip())
            i += 1
            while i < len(lines) and re.match(r"^\s*>", lines[i]):
                body_lines.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            css_cls, label = _ALERT_STYLES[kind]
            inner_html = markdown.markdown("\n".join(body_lines).strip(), extensions=["tables", "fenced_code"])
            alert_html = (
                f'<div class="gh-alert gh-alert-{css_cls}">'
                f'<div class="gh-alert-title">{label}</div>'
                f'<div class="gh-alert-body">{inner_html}</div>'
                f'</div>'
            )
            out.append(stash_fn(alert_html))
        else:
            out.append(lines[i])
            i += 1
    return "\n".join(out)

_SCRIPT_TAG_RE = re.compile(r"<\s*/?\s*(script|iframe|object|embed|meta|style|form)\b[^>]*>", re.IGNORECASE)
_EVENT_ATTR_RE = re.compile(r"\s+on[a-z]+\s*=\s*(?:\"[^\"]*\"|'[^']*'|[^\s>]+)", re.IGNORECASE)
_JS_URI_RE = re.compile(r"(href|src)\s*=\s*(['\"])\s*javascript:[^'\"]*\2", re.IGNORECASE)


def _sanitize_rendered_html(rendered: str) -> str:
    """Strips dangerous executable HTML/JS constructs from rendered markdown."""
    if not rendered:
        return ""
    cleaned = _SCRIPT_TAG_RE.sub("", rendered)
    cleaned = _EVENT_ATTR_RE.sub("", cleaned)
    cleaned = _JS_URI_RE.sub(r'\1=\2#\2', cleaned)
    return cleaned


@functools.lru_cache(maxsize=2048)
def _render_markdown_cached(text: str) -> str:
    text = clean_newlines(text, convert_guillemets=False)
    placeholders = {}

    def _stash(val: str) -> str:
        tok = f"XSTASHX{len(placeholders)}XENDX"
        placeholders[tok] = val
        return tok

    # Protect fenced and inline code spans before math parsing or stereotype formatting
    def _stash_fenced(m):
        code_html = markdown.markdown(m.group(0), extensions=["fenced_code"])
        return _stash(code_html)

    text = re.sub(r"```[\s\S]*?```", _stash_fenced, text)
    inline_codes = {}
    def _stash_inline_code(m):
        tok = f"XCODEX{len(inline_codes)}XENDX"
        inline_codes[tok] = f"<code>{html.escape(m.group(1))}</code>"
        return tok
    text = re.sub(r"`([^`\n]+)`", _stash_inline_code, text)

    # Convert display math $$...$$ and valid inline math $...$ before python-markdown mangles _ or *
    def _sub_display_math(m):
        return _stash(f'<div class="math-block">{_latex_to_html(m.group(1))}</div>')
    text = re.sub(r"\$\$([\s\S]*?)\$\$", _sub_display_math, text)

    def _sub_inline_math(m):
        inner = m.group(1)
        if not _is_valid_inline_math(inner):
            return m.group(0)
        return _stash(f'<span class="math-inline">{_latex_to_html(inner)}</span>')
    text = re.sub(r"\$([^\n$]+?)\$", _sub_inline_math, text)

    # Convert UML stereotype delimiters outside protected code/math spans
    text = text.replace("<<", "«").replace(">>", "»")

    # Convert GitHub alerts > [!NOTE], > [!WARNING], etc.
    text = _convert_github_alerts(text, _stash)

    # Standardize bullet symbols and strict indentation
    text = re.sub(r"^[ \t]*•[ \t]+", "- ", text, flags=re.MULTILINE)
    text = re.sub(r"^  ([-*]|\d+\.) ", r"    \1 ", text, flags=re.MULTILINE)
    text = re.sub(r"([^\n])\n([-*]|\d+\.) ", r"\1\n\n\2 ", text)

    rendered = markdown.markdown(text, extensions=["tables", "fenced_code"])
    for tok, val in reversed(list(placeholders.items())):
        rendered = rendered.replace(tok, val)
    for tok, code_html in inline_codes.items():
        rendered = rendered.replace(tok, code_html)
    return _sanitize_rendered_html(rendered)

def render_markdown_html(text: str) -> str:
    if not text:
        return ""
    return _render_markdown_cached(str(text))

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

MERMAID_KEYWORDS = (
    "graph", "flowchart", "sequencediagram", "classdiagram", 
    "statediagram", "erdiagram", "pie", "gantt", "gitgraph", 
    "journey", "mindmap", "quadrantchart", "xychart", "timeline", "architecture"
)

def is_mermaid_diagram(code: str) -> bool:
    if not code or not isinstance(code, str):
        return False
    stripped = code.strip().lower()
    return any(stripped.startswith(kw) for kw in MERMAID_KEYWORDS)

def render_ascii_diagram(text: str, title: str = "ARCHITECTURAL SCHEMATIC"):
    if not text:
        return
    clean_txt = clean_newlines(str(text), convert_guillemets=False).strip("\n")
    escaped = html.escape(clean_txt).replace("\n", "<br>")
    safe_title = html.escape(str(title))
    card = (
        '<div style="background: #0D0D10; border: 1px solid #222226; border-radius: 8px; overflow: hidden; margin: 14px 0 18px 0;">'
        '<div style="background: #141418; padding: 7px 14px; display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid #222226;">'
        f'<span style="font-family: \'SF Mono\', Menlo, monospace; font-size: 0.70rem; font-weight: 600; color: #71717A; letter-spacing: 0.08em; text-transform: uppercase;">{safe_title}</span>'
        '<span style="font-family: \'SF Mono\', Menlo, monospace; font-size: 0.68rem; color: #52525B;">TRACE</span>'
        '</div>'
        f'<div style="padding: 16px 20px; margin: 0; color: #D4D4D8; font-family: \'JetBrains Mono\', \'SF Mono\', Menlo, monospace; font-size: 0.86rem; line-height: 1.5; white-space: pre; overflow-x: auto;">{escaped}</div>'
        '</div>'
    )
    st.markdown(card, unsafe_allow_html=True)

def st_mermaid(code: str, height=None):
    if not code or not code.strip():
        return
    cleaned_code = code.strip()
    
    if not is_mermaid_diagram(cleaned_code):
        render_ascii_diagram(cleaned_code)
        return
    
    is_vertical = any(dir_token in cleaned_code for dir_token in ["graph TD", "graph TB", "flowchart TD", "flowchart TB"])
    has_subgraphs = "subgraph" in cleaned_code
    lines = [l for l in cleaned_code.splitlines() if l.strip() and not l.strip().startswith(('classDef', 'class ', 'style '))]
    
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
        else:
            if has_subgraphs:
                computed_height = max(240, min(650, len(lines) * 32 + 90))
            else:
                computed_height = max(90, min(240, len(lines) * 22 + 45))
        
    safe_diagram = re.sub(
        r"<\s*/?\s*(div|script|iframe|object|embed|body|html)\b",
        lambda m: html.escape(m.group(0)),
        cleaned_code,
        flags=re.IGNORECASE,
    )
    htmlcode = f'''
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="utf-8">
      <style>
        * {{ box-sizing: border-box; }}
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
          align-items: center;
        }}
        .mermaid svg {{
          max-width: 100%;
          height: auto;
          max-height: 500px;
        }}
      </style>
      <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
    </head>
    <body>
      <div class="mermaid">
{safe_diagram}
      </div>
      <script>
        mermaid.initialize({{
          startOnLoad: true,
          theme: 'dark',
          flowchart: {{ useMaxWidth: false, htmlLabels: true }},
          themeVariables: {{
            darkMode: true,
            background: '#0D0D10',
            primaryColor: '#18181B',
            primaryTextColor: '#FAFAFA',
            primaryBorderColor: '#3F3F46',
            lineColor: '#71717A',
            secondaryColor: '#111114',
            tertiaryColor: '#18181B'
          }},
          securityLevel: 'strict'
        }});
      </script>
    </body>
    </html>
    '''
    components.html(htmlcode, height=computed_height, scrolling=True)

def inject_master_css():
    st.markdown("""
    <style>
    /* Global Typography, Obsidian Color Grading & Responsive Workbench Canvas */
    *, *::before, *::after {
      box-sizing: border-box;
    }

    html, body, [class*="css"] {
      font-family: -apple-system, BlinkMacSystemFont, "Inter", "SF Pro Text", "Segoe UI", Roboto, sans-serif;
    }

    .stApp {
      background-color: #09090B;
      background-image:
        radial-gradient(ellipse 85% 42% at 50% -8%, rgba(79, 70, 229, 0.14), transparent 72%),
        radial-gradient(circle at 92% 14%, rgba(6, 182, 212, 0.07), transparent 42%),
        radial-gradient(rgba(255, 255, 255, 0.035) 1px, transparent 1px);
      background-size: 100% 100%, 100% 100%, 24px 24px;
      color: #FAFAFA;
    }

    [data-testid="stMain"],
    [data-testid="stAppViewBlockContainer"],
    [data-testid="stMainBlockContainer"],
    .block-container {
      max-width: 100% !important;
      width: 100% !important;
      padding: 1.45rem 2.25rem 3.25rem !important;
      transition: padding 180ms ease;
    }

    /* Sidebar Chrome — Collapses cleanly to 0px so main view expands full-screen */
    [data-testid="stSidebar"] {
      background: #0C0C0F;
      border-right: 1px solid #1E1E22;
      transition: min-width 180ms ease, width 180ms ease;
    }
    [data-testid="stSidebar"][aria-expanded="true"] {
      min-width: 280px !important;
      max-width: 304px !important;
    }
    [data-testid="stSidebar"][aria-expanded="false"] {
      min-width: 0 !important;
      width: 0 !important;
      margin-left: 0 !important;
      border-right: none !important;
      overflow: hidden !important;
    }
    [data-testid="stSidebar"] > div:first-child {
      padding: 1.15rem 1.0rem;
    }
    [data-testid="stSidebarNav"] { display: none; }
    header[data-testid="stHeader"] {
      background: transparent !important;
      height: 2.2rem !important;
      pointer-events: none;
    }
    header[data-testid="stHeader"] button,
    [data-testid="collapsedControl"] {
      pointer-events: auto;
    }
    #MainMenu, footer, [data-testid="stToolbar"], [data-testid="stDecoration"], [data-testid="stStatusWidget"] {
      display: none !important;
    }

    /* Clean Bordered Containers */
    [data-testid="stVerticalBlockBorderWrapper"] {
      border-color: #222229 !important;
      border-radius: 10px !important;
      background: rgba(17, 17, 21, 0.72);
    }

    /* Crisp Responsive Buttons with strict overflow guard */
    .stButton > button,
    .stFormSubmitButton > button {
      background: #141419;
      border: 1px solid #27272F;
      color: #D4D4D8;
      border-radius: 7px;
      font-weight: 500;
      font-size: 0.83rem;
      padding: 6px 10px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      max-width: 100%;
      min-height: 36px;
      box-shadow: none;
      transition: background-color 140ms ease, border-color 140ms ease, color 140ms ease, transform 140ms ease, box-shadow 140ms ease;
    }
    .stButton > button:hover,
    .stFormSubmitButton > button:hover {
      background: #1C1C23;
      border-color: #464655;
      color: #FAFAFA;
      transform: translateY(-1px);
      box-shadow: 0 3px 10px rgba(0, 0, 0, 0.25);
    }
    .stButton > button[kind="primary"],
    .stFormSubmitButton > button[kind="primary"] {
      background: linear-gradient(180deg, #564EEB 0%, #4F46E5 100%);
      border: 1px solid #6366F1;
      color: #FFFFFF;
      font-weight: 600;
      box-shadow: 0 1px 2px rgba(0, 0, 0, 0.35), inset 0 1px 0 rgba(255, 255, 255, 0.12);
    }
    .stButton > button[kind="primary"]:hover,
    .stFormSubmitButton > button[kind="primary"]:hover {
      background: linear-gradient(180deg, #4E46DE 0%, #4338CA 100%);
      border-color: #818CF8;
      color: #FFFFFF;
      transform: translateY(-1px);
      box-shadow: 0 6px 16px rgba(79, 70, 229, 0.28);
    }

    /* Top Header Shell */
    .top-nav-divider {
      height: 1px;
      width: 100%;
      background: #222226;
      margin: 4px 0 6px 0;
    }
    .nav-xp-wrap {
      display: flex;
      justify-content: flex-end;
      align-items: center;
      width: 100%;
    }
    .master-brand {
      display: flex;
      align-items: center;
      gap: 11px;
      text-decoration: none;
    }
    .brand-mark {
      width: 34px;
      height: 34px;
      border-radius: 8px;
      background: #16161B;
      border: 1px solid #2C2C34;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }
    .brand-title {
      font-weight: 700;
      font-size: 1.02rem;
      letter-spacing: -0.02em;
      color: #FAFAFA;
      line-height: 1.15;
    }
    .brand-subtitle {
      font-size: 0.72rem;
      font-weight: 500;
      color: #71717A;
      letter-spacing: 0.02em;
      margin-top: 2px;
    }
    .nav-xp-badge {
      display: inline-flex;
      align-items: center;
      width: fit-content;
      gap: 10px;
      background: #16161A;
      border: 1px solid #27272A;
      padding: 6px 13px;
      border-radius: 7px;
      white-space: nowrap;
      font-variant-numeric: tabular-nums;
    }
    .xp-points {
      color: #A5B4FC;
      font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace;
      font-weight: 600;
      font-size: 0.84rem;
      white-space: nowrap;
    }
    .xp-rank {
      color: #D4D4D8;
      font-size: 0.78rem;
      font-weight: 500;
      border-left: 1px solid #27272A;
      padding-left: 10px;
      white-space: nowrap;
    }
    .xp-user-tag {
      color: #71717A;
      font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace;
      font-size: 0.74rem;
      border-left: 1px solid #27272A;
      padding-left: 10px;
      white-space: nowrap;
    }

    /* Compact Workbench Telemetry Header & Resume Strip */
    .hub-header-strip {
      background: #111114;
      border: 1px solid #222226;
      border-radius: 10px;
      padding: 20px 24px;
      margin-bottom: 18px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 18px;
    }
    .hub-header-title {
      font-size: 1.55rem;
      font-weight: 700;
      letter-spacing: -0.025em;
      color: #FAFAFA;
      margin: 0 0 4px 0;
    }
    .hub-header-sub {
      font-size: 0.90rem;
      color: #A1A1AA;
      margin: 0;
      max-width: 620px;
      line-height: 1.5;
    }
    .hub-stat-bar {
      display: flex;
      align-items: stretch;
      background: #0B0B0E;
      border: 1px solid #222226;
      border-radius: 8px;
      overflow: hidden;
      font-variant-numeric: tabular-nums;
    }
    .hub-stat-item {
      padding: 9px 16px;
      border-right: 1px solid #222226;
      min-width: 104px;
    }
    .hub-stat-item:last-child {
      border-right: none;
    }
    .hub-stat-label {
      font-size: 0.68rem;
      font-weight: 600;
      color: #71717A;
      text-transform: uppercase;
      letter-spacing: 0.06em;
    }
    .hub-stat-value {
      font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace;
      font-size: 1.05rem;
      font-weight: 700;
      color: #FAFAFA;
      margin-top: 2px;
    }

    /* Master Subject Track Cards — Color-Graded Accent Glow & Zero-Clip Layout */
    .subject-deck-card {
      --track-accent: #6366F1;
      background: linear-gradient(180deg, #131318 0%, #101014 100%);
      border: 1px solid #23232A;
      border-radius: 11px;
      padding: 18px 20px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 12px;
      min-height: 278px;
      height: auto;
      transition: border-color 220ms ease, background 220ms ease, transform 220ms cubic-bezier(0.22, 1, 0.36, 1), box-shadow 220ms ease;
      position: relative;
      overflow: hidden;
    }
    .subject-deck-card::before {
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 2px;
      background: linear-gradient(90deg, var(--track-accent), transparent 82%);
      opacity: 0.45;
      transition: opacity 220ms ease;
    }
    .subject-deck-card::after {
      content: "";
      position: absolute;
      inset: 0;
      background: radial-gradient(circle at 92% 8%, color-mix(in srgb, var(--track-accent) 16%, transparent), transparent 58%);
      opacity: 0;
      pointer-events: none;
      transition: opacity 240ms ease;
    }
    .subject-deck-card:hover {
      border-color: color-mix(in srgb, var(--track-accent) 52%, #27272A);
      transform: translateY(-4px);
      box-shadow: 0 12px 28px rgba(0, 0, 0, 0.45), 0 0 24px color-mix(in srgb, var(--track-accent) 14%, transparent);
    }
    .subject-deck-card:hover::before {
      opacity: 1;
    }
    .subject-deck-card:hover::after {
      opacity: 1;
    }
    .subject-deck-card .subject-icon {
      font-size: 1.25rem;
      line-height: 1;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 34px;
      height: 34px;
      border-radius: 8px;
      background: color-mix(in srgb, var(--track-accent) 12%, #15151B);
      border: 1px solid color-mix(in srgb, var(--track-accent) 30%, #27272A);
      flex-shrink: 0;
      transition: transform 220ms ease, border-color 220ms ease, background-color 220ms ease;
    }
    .subject-deck-card:hover .subject-icon {
      transform: scale(1.08);
      background: color-mix(in srgb, var(--track-accent) 22%, #181820);
      border-color: color-mix(in srgb, var(--track-accent) 58%, #3F3F46);
    }
    .subject-card-top {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      margin-bottom: 10px;
      position: relative;
      z-index: 1;
    }
    .subject-track-meta {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace;
      font-size: 0.70rem;
      font-weight: 600;
      color: #A1A1AA;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      min-width: 0;
    }
    .track-dot {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      display: inline-block;
      flex-shrink: 0;
    }
    .subject-case-count {
      font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace;
      font-size: 0.72rem;
      color: #A1A1AA;
      white-space: nowrap;
      flex-shrink: 0;
    }
    .subject-card-title {
      font-size: 1.12rem;
      font-weight: 700;
      letter-spacing: -0.02em;
      color: #FAFAFA;
      line-height: 1.3;
      margin-bottom: 6px;
      overflow-wrap: anywhere;
      position: relative;
      z-index: 1;
    }
    .subject-card-tagline {
      color: #A1A1AA;
      font-size: 0.85rem;
      line-height: 1.48;
      display: -webkit-box;
      -webkit-line-clamp: 3;
      -webkit-box-orient: vertical;
      overflow: hidden;
      overflow-wrap: anywhere;
      position: relative;
      z-index: 1;
    }
    .tag-container {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-top: 4px;
    }
    .tag-pill {
      background: #18181F;
      border: 1px solid #272730;
      color: #B4B4BE;
      font-size: 0.69rem;
      font-weight: 500;
      padding: 2px 8px;
      border-radius: 5px;
      max-width: 100%;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }
    .subject-meta-footer {
      border-top: 1px solid #1E1E22;
      padding-top: 12px;
      margin-top: auto;
    }

    /* Matte Editorial Card Component System */
    .card-kicker {
      display: inline-block;
      font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace;
      font-size: 0.69rem;
      font-weight: 600;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      margin-bottom: 6px;
      padding: 0;
      background: transparent;
      border: none;
    }
    .kicker-briefing { color: #38BDF8; }
    .kicker-objective { color: #34D399; }
    .kicker-theory { color: #A5B4FC; }
    .kicker-incident { color: #F87171; }
    .kicker-scenario { color: #FBBF24; }
    .kicker-concept { color: #A5B4FC; }

    .card-heading {
      font-size: 1.16rem;
      font-weight: 700;
      letter-spacing: -0.015em;
      margin: 0 0 10px 0;
      line-height: 1.35;
      color: #FAFAFA;
    }
    .heading-briefing,
    .heading-objective,
    .heading-theory,
    .heading-scenario,
    .heading-concept { color: #FAFAFA; }
    .heading-incident { color: #FEE2E2; }

    .briefing-card,
    .objective-card,
    .theory-card,
    .incident-card,
    .scenario-card,
    .concept-card {
      background: #111114;
      border: 1px solid #222226;
      border-radius: 8px;
      padding: 18px 22px;
      margin: 14px 0;
      transition: border-color 200ms ease, background-color 200ms ease;
    }
    .briefing-card:hover,
    .objective-card:hover,
    .theory-card:hover,
    .scenario-card:hover,
    .concept-card:hover {
      border-color: #2D2D32;
      background: #131316;
    }
    .incident-card:hover {
      border-color: #2A1B1E;
      background: #161113;
    }
    .briefing-card { border-left: 3px solid #38BDF8; }
    .objective-card { border-left: 3px solid #10B981; }
    .theory-card { border-left: 3px solid #6366F1; }
    .incident-card { border-left: 3px solid #EF4444; background: #141012; }
    .scenario-card { border-left: 3px solid #F59E0B; }
    .concept-card { border-left: 3px solid #818CF8; }

    .theory-tech-box {
      background: #0B0B0E;
      border: 1px solid #222226;
      border-left: 2px solid #6366F1;
      border-radius: 6px;
      padding: 12px 16px;
      margin: 14px 0 4px 0;
    }
    .theory-tech-label {
      color: #A5B4FC;
      font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace;
      font-weight: 600;
      font-size: 0.72rem;
      letter-spacing: 0.06em;
      text-transform: uppercase;
    }

    /* Card Body Typography */
    .card-body {
      font-size: 0.96rem;
      line-height: 1.65;
      color: #D4D4D8;
    }
    .incident-card .card-body { color: #FECACA; }

    .card-body ul, .card-body ol {
      margin: 8px 0 10px 0;
      padding-left: 22px;
    }
    .card-body li {
      margin-bottom: 6px;
      line-height: 1.6;
      color: #D4D4D8;
    }
    .card-body li:last-child { margin-bottom: 0; }
    .briefing-card .card-body li::marker { color: #38BDF8; }
    .objective-card .card-body li::marker { color: #34D399; }
    .theory-card .card-body li::marker { color: #818CF8; }
    .incident-card .card-body li::marker { color: #F87171; }
    .scenario-card .card-body li::marker { color: #FBBF24; }

    .card-body p { margin: 0 0 10px 0; }
    .card-body p:last-child { margin-bottom: 0; }
    .card-body strong { color: #FAFAFA; font-weight: 600; }

    .card-body code {
      background: #18181C;
      border: 1px solid #27272A;
      color: #E4E4E7;
      padding: 1px 5px;
      border-radius: 4px;
      font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace;
      font-size: 0.87em;
    }

    /* Case Grid Badge Utilities (Consolidated case-catalog-card below) */
    .case-badge-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 10px;
    }
    .case-num-badge {
      background: #18181C;
      border: 1px solid #27272A;
      color: #A1A1AA;
      font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace;
      font-size: 0.70rem;
      font-weight: 600;
      padding: 2px 8px;
      border-radius: 5px;
      letter-spacing: 0.04em;
    }
    .status-pill {
      font-size: 0.70rem;
      font-weight: 600;
      padding: 2px 8px;
      border-radius: 5px;
    }
    .status-completed {
      background: rgba(16, 185, 129, 0.12);
      color: #34D399;
      border: 1px solid rgba(16, 185, 129, 0.28);
    }
    .status-progress {
      background: rgba(245, 158, 11, 0.12);
      color: #FBBF24;
      border: 1px solid rgba(245, 158, 11, 0.28);
    }
    .status-locked {
      background: #18181C;
      color: #71717A;
      border: 1px solid #27272A;
    }

    /* GitHub-style Callout Alerts */
    .gh-alert {
      border-radius: 7px;
      padding: 12px 16px;
      margin: 12px 0;
      border: 1px solid #222226;
      border-left: 3px solid #6366F1;
      background: #141418;
    }
    .gh-alert-title {
      font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace;
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      margin-bottom: 5px;
      color: #A5B4FC;
    }
    .gh-alert-body p:last-child { margin-bottom: 0; }
    .gh-alert-tip { border-left-color: #10B981; }
    .gh-alert-tip .gh-alert-title { color: #34D399; }
    .gh-alert-important { border-left-color: #818CF8; }
    .gh-alert-important .gh-alert-title { color: #C7D2FE; }
    .gh-alert-warning { border-left-color: #F59E0B; }
    .gh-alert-warning .gh-alert-title { color: #FBBF24; }
    .gh-alert-caution { border-left-color: #EF4444; }
    .gh-alert-caution .gh-alert-title { color: #F87171; }

    /* Crisp LaTeX Math */
    .math-inline {
      font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace;
      font-size: 0.88em;
      color: #FAFAFA;
      background: #18181C;
      border: 1px solid #27272A;
      border-radius: 4px;
      padding: 1px 5px;
      white-space: nowrap;
    }
    .math-block {
      font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace;
      font-size: 0.94rem;
      color: #FAFAFA;
      background: #0D0D10;
      border: 1px solid #222226;
      border-radius: 7px;
      padding: 12px 16px;
      margin: 12px 0;
      text-align: center;
      overflow-x: auto;
    }

    /* Dark Comparison Tables */
    table {
      width: 100%;
      border-collapse: collapse;
      margin: 12px 0;
      background: #111114;
      border: 1px solid #222226;
      border-radius: 7px;
      overflow: hidden;
    }
    th {
      background: #16161B;
      color: #E4E4E7;
      font-size: 0.78rem;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      padding: 10px 14px;
      text-align: left;
      border-bottom: 1px solid #27272A;
    }
    td {
      padding: 9px 14px;
      color: #D4D4D8;
      font-size: 0.90rem;
      border-bottom: 1px solid #1E1E22;
    }
    tr:last-child td { border-bottom: none; }

    /* OOP, Memory Grid & Trace Cards */
    .oop-header-banner {
      background: #111114;
      border: 1px solid #222226;
      border-left: 3px solid #6366F1;
      border-radius: 8px;
      padding: 18px 22px;
      margin-bottom: 16px;
    }
    .concept-chip {
      display: inline-block;
      background: #18181C;
      border: 1px solid #27272A;
      color: #D4D4D8;
      font-size: 0.72rem;
      font-weight: 500;
      padding: 2px 9px;
      border-radius: 5px;
      margin: 4px 6px 0 0;
    }
    .memory-grid {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin: 12px 0;
    }
    .memory-cell {
      min-width: 115px;
      flex: 1 1 115px;
      background: #111114;
      border: 1px solid #27272A;
      border-radius: 7px;
      padding: 10px 12px;
      text-align: center;
      font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace;
    }
    .memory-addr { color: #38BDF8; font-size: 0.72rem; margin-bottom: 4px; }
    .memory-val { color: #FAFAFA; font-size: 1.02rem; font-weight: 700; margin-bottom: 4px; }
    .memory-lbl { color: #71717A; font-size: 0.74rem; }
    .trace-step {
      background: #111114;
      border: 1px solid #222226;
      border-left: 2px solid #38BDF8;
      border-radius: 6px;
      padding: 9px 14px;
      margin: 6px 0;
      color: #D4D4D8;
      font-size: 0.90rem;
    }
    .approach-wrong {
      background: #141012;
      border: 1px solid #2A1B1E;
      border-left: 3px solid #EF4444;
      border-radius: 8px;
      padding: 14px 18px;
      margin: 10px 0;
    }
    .approach-correct {
      background: #0F1412;
      border: 1px solid #1C2E26;
      border-left: 3px solid #10B981;
      border-radius: 8px;
      padding: 14px 18px;
      margin: 10px 0;
    }
    .analogy-card {
      background: #111114;
      border: 1px solid #222226;
      border-left: 3px solid #F59E0B;
      border-radius: 8px;
      padding: 16px 20px;
      margin: 10px 0;
    }
    .solved-pill {
      display: inline-block;
      background: rgba(16, 185, 129, 0.12);
      border: 1px solid rgba(16, 185, 129, 0.35);
      color: #34D399;
      font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace;
      font-size: 0.68rem;
      font-weight: 700;
      padding: 2px 8px;
      border-radius: 5px;
      margin-left: 8px;
      vertical-align: middle;
    }

    /* DSA Online Judge Studio */
    .dsa-judge-card {
      background: #111114;
      border: 1px solid #222226;
      border-left: 3px solid #06B6D4;
      border-radius: 8px;
      padding: 20px 24px;
      margin: 14px 0 18px 0;
      transition: border-color 200ms ease, background-color 200ms ease;
    }
    .dsa-judge-card:hover {
      border-color: #2D2D32;
      background: #131316;
    }
    .dsa-meta-bar {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 8px;
      margin-bottom: 14px;
    }
    .diff-pill {
      font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace;
      font-size: 0.72rem;
      font-weight: 700;
      padding: 2px 9px;
      border-radius: 5px;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }
    .diff-easy { background: rgba(16, 185, 129, 0.12); color: #34D399; border: 1px solid rgba(16, 185, 129, 0.3); }
    .diff-medium { background: rgba(245, 158, 11, 0.12); color: #FBBF24; border: 1px solid rgba(245, 158, 11, 0.3); }
    .diff-hard { background: rgba(239, 68, 68, 0.12); color: #F87171; border: 1px solid rgba(239, 68, 68, 0.3); }
    .pattern-pill {
      font-size: 0.73rem;
      font-weight: 600;
      padding: 2px 9px;
      border-radius: 5px;
      background: #18181C;
      color: #D4D4D8;
      border: 1px solid #27272A;
    }
    .complexity-pill {
      font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace;
      font-size: 0.73rem;
      font-weight: 500;
      padding: 2px 9px;
      border-radius: 5px;
      background: #18181C;
      color: #A1A1AA;
      border: 1px solid #27272A;
    }
    .dsa-example-box {
      background: #0B0B0E;
      border: 1px solid #222226;
      border-left: 2px solid #4F46E5;
      border-radius: 6px;
      padding: 12px 16px;
      margin: 8px 0;
      font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace;
      font-size: 0.85rem;
      color: #E4E4E7;
    }
    .dsa-constraint-box {
      background: #0D0D10;
      border: 1px solid #222226;
      border-radius: 6px;
      padding: 12px 16px;
      margin-top: 12px;
      font-size: 0.88rem;
      color: #D4D4D8;
    }
    .dsa-verdict-banner {
      border-radius: 7px;
      padding: 12px 16px;
      margin: 14px 0 10px 0;
      font-weight: 600;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .verdict-accepted { background: rgba(16, 185, 129, 0.12); border: 1px solid rgba(16, 185, 129, 0.35); color: #34D399; }
    .verdict-wa { background: rgba(245, 158, 11, 0.12); border: 1px solid rgba(245, 158, 11, 0.35); color: #FBBF24; }
    .verdict-err { background: rgba(239, 68, 68, 0.12); border: 1px solid rgba(239, 68, 68, 0.35); color: #F87171; }
    .dsa-tc-card {
      background: #0D0D10;
      border: 1px solid #222226;
      border-radius: 7px;
      padding: 10px 14px;
      margin: 6px 0;
      font-size: 0.85rem;
    }
    .dsa-tc-pass { border-left: 3px solid #10B981; }
    .dsa-tc-fail { border-left: 3px solid #EF4444; }

    /* Sidebar Profile & Progress Meters */
    .sidebar-profile-card {
      background: #111114;
      border: 1px solid #222226;
      border-radius: 8px;
      padding: 13px 15px;
      margin-bottom: 14px;
    }
    .sidebar-section-label {
      font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace;
      font-size: 0.68rem;
      font-weight: 600;
      color: #71717A;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin: 14px 0 7px 0;
    }
    .progress-track-outer {
      width: 100%;
      height: 5px;
      background: #1D1D22;
      border-radius: 3px;
      overflow: hidden;
      margin-top: 6px;
    }
    .progress-track-fill {
      height: 100%;
      background: #4F46E5;
      border-radius: 3px;
    }

    /* Inline Resume Strip */
    .resume-box {
      background: #111114;
      border: 1px solid #222226;
      border-left: 3px solid #4F46E5;
      border-radius: 8px;
      padding: 11px 16px;
    }
    .resume-label {
      font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace;
      font-size: 0.67rem;
      font-weight: 600;
      color: #818CF8;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-bottom: 3px;
    }
    .resume-title {
      font-size: 0.90rem;
      font-weight: 600;
      color: #FAFAFA;
      line-height: 1.35;
    }

    /* Subject Catalog Header & Case Investigation Grid */
    .catalog-header {
      --track-accent: #6366F1;
      background:
        radial-gradient(circle at 95% 10%, color-mix(in srgb, var(--track-accent) 14%, transparent), transparent 55%),
        #111116;
      border: 1px solid #23232A;
      border-left: 3px solid var(--track-accent);
      border-radius: 10px;
      padding: 20px 24px;
      margin-bottom: 18px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
    }
    .catalog-header-meta {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace;
      font-size: 0.71rem;
      font-weight: 600;
      color: #A1A1AA;
      text-transform: uppercase;
      letter-spacing: 0.07em;
      margin-bottom: 6px;
    }
    .catalog-header-title {
      font-size: 1.48rem;
      font-weight: 700;
      letter-spacing: -0.02em;
      color: #FAFAFA;
      margin: 0 0 4px 0;
      overflow-wrap: anywhere;
    }
    .catalog-header-sub {
      font-size: 0.90rem;
      color: #A1A1AA;
      margin: 0;
      max-width: 720px;
      line-height: 1.5;
    }

    .case-catalog-card {
      --track-accent: #6366F1;
      background: linear-gradient(180deg, #131318 0%, #101014 100%);
      border: 1px solid #23232A;
      border-radius: 10px;
      padding: 18px 20px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 10px;
      min-height: 224px;
      height: auto;
      position: relative;
      overflow: hidden;
      transition: border-color 220ms ease, transform 220ms cubic-bezier(0.22, 1, 0.36, 1), box-shadow 220ms ease;
    }
    .case-catalog-card::after {
      content: "";
      position: absolute;
      inset: 0;
      background: radial-gradient(circle at 95% 5%, color-mix(in srgb, var(--track-accent) 13%, transparent), transparent 60%);
      opacity: 0;
      pointer-events: none;
      transition: opacity 220ms ease;
    }
    .case-catalog-card:hover {
      border-color: color-mix(in srgb, var(--track-accent) 50%, #27272A);
      transform: translateY(-3px);
      box-shadow: 0 10px 24px rgba(0, 0, 0, 0.38), 0 0 18px color-mix(in srgb, var(--track-accent) 12%, transparent);
    }
    .case-catalog-card:hover::after {
      opacity: 1;
    }
    .case-card-top {
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 8px;
    }
    .case-num-pill {
      font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace;
      font-size: 0.70rem;
      font-weight: 600;
      color: #D4D4D8;
      background: #18181F;
      border: 1px solid #272730;
      padding: 2px 8px;
      border-radius: 5px;
      letter-spacing: 0.04em;
    }
    .case-status-pill {
      font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace;
      font-size: 0.68rem;
      font-weight: 600;
      padding: 2px 8px;
      border-radius: 5px;
      letter-spacing: 0.04em;
    }
    .case-status-done {
      background: rgba(16, 185, 129, 0.14);
      border: 1px solid rgba(16, 185, 129, 0.38);
      color: #34D399;
    }
    .case-status-open {
      background: #18181F;
      border: 1px solid #272730;
      color: #A1A1AA;
    }
    .case-pinned-pill {
      font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace;
      font-size: 0.66rem;
      font-weight: 600;
      padding: 2px 7px;
      border-radius: 5px;
      background: rgba(245, 158, 11, 0.12);
      border: 1px solid rgba(245, 158, 11, 0.35);
      color: #FBBF24;
    }
    .case-card-title {
      font-size: 1.05rem;
      font-weight: 700;
      color: #FAFAFA;
      letter-spacing: -0.015em;
      line-height: 1.35;
      margin-bottom: 6px;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
      overflow-wrap: anywhere;
    }
    .case-card-meta {
      font-size: 0.85rem;
      color: #A1A1AA;
      line-height: 1.48;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
      overflow-wrap: anywhere;
    }
    .case-card-stats {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-top: auto;
      padding-top: 10px;
      border-top: 1px solid #1E1E24;
    }
    .stat-pill {
      font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace;
      font-size: 0.69rem;
      color: #B4B4BE;
      background: #18181F;
      border: 1px solid #272730;
      padding: 2px 8px;
      border-radius: 5px;
      max-width: 100%;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }

    /* Case Investigation Header & Global Content Containment */
    .case-header-bar {
      --track-accent: #6366F1;
      background:
        radial-gradient(circle at 96% 15%, color-mix(in srgb, var(--track-accent) 12%, transparent), transparent 55%),
        #111116;
      border: 1px solid #23232A;
      border-left: 3px solid var(--track-accent);
      border-radius: 9px;
      padding: 16px 20px;
      margin: 10px 0 14px 0;
    }
    .case-header-kicker {
      font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace;
      font-size: 0.70rem;
      font-weight: 600;
      color: #A5B4FC;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-bottom: 5px;
    }
    .case-header-title {
      font-size: 1.35rem;
      font-weight: 700;
      letter-spacing: -0.02em;
      color: #FAFAFA;
      margin: 0 0 6px 0;
      overflow-wrap: anywhere;
    }
    .case-header-meta {
      font-size: 0.86rem;
      color: #A1A1AA;
      overflow-wrap: anywhere;
    }
    .card-body,
    .dsa-example-box,
    .dsa-constraint-box,
    .theory-tech-box,
    .trace-step,
    .gh-alert-body {
      overflow-wrap: anywhere;
      word-break: break-word;
      max-width: 100%;
    }
    .card-body pre,
    .dsa-example-box pre {
      overflow-x: auto;
      max-width: 100%;
      white-space: pre-wrap;
      word-break: break-word;
    }

    /* Authentication Gate Panel */
    .auth-gate-card {
      background: #111114;
      border: 1px solid #222226;
      border-radius: 10px;
      padding: 24px 28px;
      max-width: 520px;
      margin: 32px auto 18px auto;
    }
    .auth-gate-kicker {
      font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace;
      font-size: 0.70rem;
      font-weight: 600;
      color: #818CF8;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-bottom: 6px;
    }
    .auth-gate-title {
      font-size: 1.35rem;
      font-weight: 700;
      color: #FAFAFA;
      margin: 0 0 6px 0;
    }
    .auth-gate-sub {
      font-size: 0.88rem;
      color: #A1A1AA;
      margin: 0;
      line-height: 1.5;
    }

    /* Card Progress Bar (inside Subject & Case cards) */
    .card-progress-outer {
      width: 100%;
      height: 3px;
      background: #1D1D22;
      border-radius: 2px;
      overflow: hidden;
      margin-top: 8px;
    }
    .card-progress-fill {
      height: 100%;
      border-radius: 2px;
      transition: width 400ms ease;
    }

    /* Keyboard Shortcut Hint */
    .kbd-hint {
      display: inline-block;
      font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace;
      font-size: 0.66rem;
      font-weight: 600;
      color: #52525B;
      background: #18181C;
      border: 1px solid #27272A;
      padding: 1px 5px;
      border-radius: 4px;
      margin-left: 6px;
      vertical-align: middle;
    }

    /* XP Toast Animation */
    @keyframes xp-pulse {
      0% { transform: scale(1); }
      50% { transform: scale(1.08); }
      100% { transform: scale(1); }
    }
    .xp-points-animated {
      animation: xp-pulse 0.4s ease;
    }

    /* Smooth page transition */
    [data-testid="stAppViewBlockContainer"] {
      animation: fadeIn 0.25s ease-out;
    }
    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(6px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* Advanced Telemetry, Mastery Ribbon, Stepper & Compact View Styles */
    [data-testid="stVerticalBlockBorderWrapper"] {
      backdrop-filter: blur(12px);
      box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.04), 0 8px 28px rgba(0, 0, 0, 0.35);
    }

    .rank-strip {
      background: linear-gradient(90deg, rgba(79, 70, 229, 0.10), rgba(17, 17, 22, 0.85) 55%);
      border: 1px solid #24242D;
      border-radius: 9px;
      padding: 11px 16px;
      margin: 0 0 14px 0;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 14px;
    }
    .rank-meta {
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 0.84rem;
      color: #D4D4D8;
    }
    .rank-badge-pill {
      font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace;
      font-size: 0.72rem;
      font-weight: 700;
      color: #A5B4FC;
      background: rgba(79, 70, 229, 0.16);
      border: 1px solid rgba(99, 102, 241, 0.36);
      padding: 3px 9px;
      border-radius: 5px;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }
    .rank-bar-wrap {
      display: flex;
      align-items: center;
      gap: 10px;
      min-width: 240px;
      flex: 1 1 240px;
      max-width: 380px;
    }
    .rank-bar-outer {
      flex: 1;
      height: 6px;
      background: #1B1B22;
      border-radius: 4px;
      overflow: hidden;
    }
    .rank-bar-fill {
      height: 100%;
      background: linear-gradient(90deg, #6366F1, #38BDF8);
      border-radius: 4px;
      transition: width 350ms ease;
    }

    .mastery-ribbon {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(115px, 1fr));
      gap: 8px;
      margin: 0 0 14px 0;
    }
    .mastery-seg {
      --seg-color: #6366F1;
      background: #111116;
      border: 1px solid #22222A;
      border-radius: 7px;
      padding: 8px 10px;
      transition: border-color 180ms ease, background-color 180ms ease;
    }
    .mastery-seg:hover {
      border-color: color-mix(in srgb, var(--seg-color) 55%, #27272A);
      background: #15151C;
    }
    .mastery-seg-top {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.72rem;
      font-weight: 600;
      color: #E4E4E7;
      margin-bottom: 5px;
      white-space: nowrap;
      overflow: hidden;
    }
    .mastery-seg-bar {
      height: 3px;
      background: #1D1D24;
      border-radius: 2px;
      overflow: hidden;
    }
    .mastery-seg-fill {
      height: 100%;
      background: var(--seg-color);
      border-radius: 2px;
    }

    .svg-ring-wrap {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace;
      font-size: 0.70rem;
      color: #A1A1AA;
      white-space: nowrap;
    }

    .topic-chip-row {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 6px;
      margin-top: 10px;
    }
    .topic-chip {
      font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace;
      font-size: 0.68rem;
      color: #B4B4BE;
      background: #17171E;
      border: 1px solid #262630;
      padding: 2px 8px;
      border-radius: 5px;
    }
    .diff-chip {
      font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace;
      font-size: 0.68rem;
      font-weight: 700;
      padding: 2px 8px;
      border-radius: 5px;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }
    .diff-beginner { background: rgba(16, 185, 129, 0.12); border: 1px solid rgba(16, 185, 129, 0.34); color: #34D399; }
    .diff-inter { background: rgba(56, 189, 248, 0.12); border: 1px solid rgba(56, 189, 248, 0.34); color: #38BDF8; }
    .diff-adv { background: rgba(245, 158, 11, 0.12); border: 1px solid rgba(245, 158, 11, 0.34); color: #FBBF24; }
    .diff-expert { background: rgba(244, 63, 94, 0.12); border: 1px solid rgba(244, 63, 94, 0.34); color: #FB7185; }

    .compact-case-row {
      background: #111116;
      border: 1px solid #22222A;
      border-radius: 8px;
      padding: 11px 16px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      transition: border-color 160ms ease, background-color 160ms ease;
    }
    .compact-case-row:hover {
      border-color: #3F3F4C;
      background: #15151C;
    }

    /* Enhanced scrollbar */
    ::-webkit-scrollbar {
      width: 6px;
      height: 6px;
    }
    ::-webkit-scrollbar-track {
      background: #09090B;
    }
    ::-webkit-scrollbar-thumb {
      background: #27272A;
      border-radius: 3px;
    }
    ::-webkit-scrollbar-thumb:hover {
      background: #3F3F46;
    }
    </style>
    """, unsafe_allow_html=True)

def _solved_badge(challenge_key: str) -> str:
    if persistence.has_solved_challenge(challenge_key):
        return '<span class="solved-pill">SOLVED</span>'
    return ""

def _award_xp_with_feedback(subject_id: str, amount: int, challenge_key: str):
    if persistence.award_challenge_xp(subject_id, amount, challenge_key=challenge_key):
        st.toast(f"+{amount} XP Earned")

def _check_exec_cooldown(cooldown_sec: float = 0.6) -> bool:
    """Rate-limits interactive sandbox execution per user session."""
    now = time.monotonic()
    last = st.session_state.get("_last_exec_ts", 0.0)
    if now - last < cooldown_sec:
        st.warning("Sandbox rate limit: please wait a moment before running again.")
        return False
    st.session_state["_last_exec_ts"] = now
    return True

def _render_ace_or_textarea(state_key: str, default_code: str, language: str, height: int = 260, allow_solution: str = None):
    ver_key = f"{state_key}_ver"
    if state_key not in st.session_state:
        st.session_state[state_key] = default_code
    if ver_key not in st.session_state:
        st.session_state[ver_key] = 0

    cols = st.columns([1.2, 1.3, 3.5] if allow_solution else [1.2, 4.8])
    with cols[0]:
        if st.button("Reset Starter", key=f"reset_{state_key}", use_container_width=True):
            st.session_state[state_key] = default_code
            st.session_state[ver_key] += 1
            st.rerun()
    if allow_solution:
        with cols[1]:
            if st.button("Load Solution", key=f"sol_load_{state_key}", use_container_width=True):
                st.session_state[state_key] = allow_solution
                st.session_state[ver_key] += 1
                st.rerun()

    ace_widget_key = f"ace_{state_key}_{st.session_state[ver_key]}"
    try:
        from streamlit_ace import st_ace
        edited = st_ace(
            value=st.session_state[state_key],
            language=language,
            theme="tomorrow_night",
            font_size=14,
            tab_size=4,
            height=height,
            key=ace_widget_key,
        )
    except Exception:
        edited = st.text_area("Code Editor:", value=st.session_state[state_key], height=height, key=f"ta_{ace_widget_key}")
    if edited is not None:
        st.session_state[state_key] = edited
    return st.session_state[state_key]

def _render_mcq_challenge(
    block: Dict[str, Any],
    subject_id: str,
    case_id: int,
    module_idx: int,
    block_idx: int,
    *,
    form_prefix: str,
    icon: str,
    title: str,
    xp_reward: int = 15,
    submit_label: str = "Submit Answer",
    guide_title: str = "Reveal Explanation",
    explanation_key: str = "explanation",
    preamble_html: str = "",
    radio_label: str = "Select your answer:",
    is_strategic: bool = False,
):
    ckey = f"{subject_id}_{case_id}_m{module_idx}_b{block_idx}"
    safe_title = html.escape(str(title))
    st.markdown(f'<h3 style="margin-top:16px;margin-bottom:8px;">{safe_title}{_solved_badge(ckey)}</h3>', unsafe_allow_html=True)
    if preamble_html:
        st.markdown(preamble_html, unsafe_allow_html=True)

    q = block.get("question") or block.get("content", "")
    if q:
        st.markdown(render_markdown_html(f"**{q}**"), unsafe_allow_html=True)

    options = block.get("options", [])
    exp_text = block.get(explanation_key) or block.get("explanation") or ""

    if not options:
        if exp_text:
            st.markdown(render_markdown_html(exp_text), unsafe_allow_html=True)
        return

    with st.form(key=f"{form_prefix}_form_{ckey}"):
        chosen = st.radio(radio_label, options, key=f"{form_prefix}_radio_{ckey}")
        submitted = st.form_submit_button(submit_label)
        if submitted and chosen is not None:
            idx = options.index(chosen)
            ans = block.get("answer", -1)
            is_correct = False
            correct_str = ""
            if isinstance(ans, int) and 0 <= ans < len(options):
                is_correct = (idx == ans)
                correct_str = str(options[ans])
            elif isinstance(ans, str):
                if ans.isdigit() and 0 <= int(ans) < len(options):
                    is_correct = (idx == int(ans))
                    correct_str = str(options[int(ans)])
                else:
                    is_correct = check_answer_match(chosen, ans)
                    correct_str = ans

            if is_correct:
                if is_strategic:
                    st.success(f"**Optimal Decision:** `{chosen}` balances technical integrity with business constraints.")
                else:
                    st.success(f"**Correct:** `{chosen}` is the right answer.")
                _award_xp_with_feedback(subject_id, xp_reward, ckey)
            else:
                clean_corr = correct_str.rstrip(".").strip()
                if is_strategic:
                    st.warning(f"**Suboptimal Path Selected:** `{chosen}` introduces higher risk or debt. Recommended: **`{clean_corr}`**.")
                else:
                    st.error(f"**Incorrect:** You selected `{chosen}`. Correct answer: **`{clean_corr}`**.")

            if exp_text:
                with st.container(border=True):
                    st.markdown(render_markdown_html(exp_text), unsafe_allow_html=True)

    if exp_text:
        with st.expander(guide_title):
            st.markdown(render_markdown_html(exp_text), unsafe_allow_html=True)

def _render_sql_sandbox(block: Dict[str, Any], subject_id: str, case_id: int, module_idx: int, block_idx: int):
    ckey = f"{subject_id}_{case_id}_m{module_idx}_b{block_idx}"
    safe_title = html.escape(str(block.get("title", "Query Lab")))
    st.markdown(f'<h3 style="margin-top:16px;margin-bottom:8px;">SQL Sandbox: {safe_title}{_solved_badge(ckey)}</h3>', unsafe_allow_html=True)
    if block.get("context"):
        st.markdown(render_markdown_html(block["context"]), unsafe_allow_html=True)

    init_script = block.get("init_script", "")
    sol_query = block.get("solution_query", "")

    if init_script.strip():
        tables = runners.inspect_sql_schema(init_script)
        if tables:
            with st.expander(f"Schema & Seed Rows ({len(tables)} table{'s' if len(tables) != 1 else ''})", expanded=True):
                t_cols = st.columns(min(len(tables), 2))
                for idx_t, (tname, df) in enumerate(tables.items()):
                    with t_cols[idx_t % min(len(tables), 2)]:
                        st.markdown(f"**Table `{tname}`** — `{len(df)}` rows × `{len(df.columns)}` cols")
                        st.dataframe(df, use_container_width=True, hide_index=True)

    editor_key = f"sql_editor_{ckey}"
    starter_sql = block.get("starter_query") or "-- Write your SQL query below\n"
    user_sql = _render_ace_or_textarea(editor_key, starter_sql, language="sql", height=180, allow_solution=sol_query or None)

    c_run, c_hint = st.columns([1.3, 4.7])
    with c_run:
        run_sql_btn = st.button("Execute SQL", type="primary", key=f"run_sql_{ckey}", use_container_width=True)
    if block.get("hint"):
        with st.expander("Query Hint"):
            st.markdown(render_markdown_html(block["hint"]), unsafe_allow_html=True)

    if run_sql_btn and _check_exec_cooldown():
        ok, res, err = runners.run_sql(user_sql, schema_ddl=init_script)
        if not ok:
            st.error(f"**SQL Execution Error:**\n\n`{err}`")
        else:
            if hasattr(res, "columns"):
                st.success(f"**Query Executed** — Returned {len(res)} row(s).")
                st.dataframe(res, use_container_width=True, hide_index=True)
            else:
                st.success(f"**{res}**")

            if sol_query.strip():
                check = runners.verify_sql_sandbox(user_sql, sol_query, schema_ddl=init_script)
                if check.get("passed"):
                    st.success("**Verified!** Your query output & database state match the target solution.")
                    _award_xp_with_feedback(subject_id, 25, ckey)
                else:
                    detail = check.get("error") or "Output or resulting database schema differs from target solution."
                    st.warning(f"**Query ran cleanly, but check mismatch:** {detail}")
                    exp_df = check.get("expected_df")
                    if exp_df is not None and hasattr(exp_df, "columns"):
                        with st.expander("Expected Output Preview"):
                            st.dataframe(exp_df, use_container_width=True, hide_index=True)
            else:
                _award_xp_with_feedback(subject_id, 25, ckey)

    if block.get("explanation"):
        with st.expander("Architectural Breakdown & Query Explanation"):
            st.markdown(render_markdown_html(block["explanation"]), unsafe_allow_html=True)

def _render_code_lab(block: Dict[str, Any], subject_id: str, case_id: int, module_idx: int, block_idx: int):
    ckey = f"{subject_id}_{case_id}_m{module_idx}_b{block_idx}"
    explicit_lang = (block.get("language") or "").strip().lower()
    is_cpp = (explicit_lang in ("cpp", "c++", "c_cpp")) if explicit_lang else (subject_id == "oop")
    editor_lang = "c_cpp" if is_cpp else "python"
    sol_code = block.get("solution_code") or block.get("solution") or ""

    safe_title = html.escape(str(block.get("title", "Interactive Implementation Lab")))
    st.markdown(f'<h3 style="margin-top:16px;margin-bottom:8px;">{safe_title}{_solved_badge(ckey)}</h3>', unsafe_allow_html=True)
    instr = block.get("instructions") or block.get("instruction") or ""
    if instr:
        st.markdown(render_markdown_html(instr), unsafe_allow_html=True)

    tab_code, tab_why, tab_alternatives, tab_edge_cases = st.tabs([
        "Code Editor & Execution",
        "Why It Works & Complexity",
        "Alternatives & Trade-offs",
        "Edge Cases & Failure Modes"
    ])

    with tab_code:
        starter = block.get("starter_code", "// Write C++ code here\n" if is_cpp else "# Write Python code here\n")
        user_code = _render_ace_or_textarea(f"code_editor_{ckey}", starter, language=editor_lang, height=280, allow_solution=sol_code or None)

        default_stdin = block.get("stdin_input", "")
        stdin_data = default_stdin
        if default_stdin or any(tok in (starter + sol_code) for tok in ("std::cin", "cin >>", "getline(", "input(")):
            stdin_data = st.text_input(
                "Program Stdin Input:",
                value=default_stdin,
                key=f"stdin_{ckey}",
                help="Standard input passed to std::cin / input()."
            )

        if block.get("hint"):
            with st.expander("Implementation Hint"):
                st.markdown(render_markdown_html(block["hint"]), unsafe_allow_html=True)

        run_pressed = st.button("Run & Verify Code", type="primary", key=f"run_btn_{ckey}")
        if run_pressed and _check_exec_cooldown():
            with st.spinner("Compiling & executing in isolated sandbox..."):
                if is_cpp:
                    success, stdout, stderr = runners.run_cpp(user_code, input_data=stdin_data)
                else:
                    test_code = block.get("test_code", "")
                    success, stdout, stderr = runners.run_py(user_code, input_data=stdin_data, extra_code=test_code)

                if not success:
                    st.error("**Execution Error Encountered:**")
                    st.code(stderr if stderr else stdout, language="text")
                else:
                    st.success("**Code Executed Successfully**")
                    if stdout and stdout.strip():
                        st.code(stdout, language="text")
                    else:
                        st.info("(Program finished cleanly with no console output)")

                    expected_out = (block.get("expected_output") or "").strip()
                    if expected_out:
                        actual_norm = "\n".join(ln.rstrip() for ln in (stdout or "").strip().splitlines())
                        exp_norm = "\n".join(ln.rstrip() for ln in expected_out.splitlines())
                        if actual_norm == exp_norm:
                            st.success("**Exact Expected Output Matched**")
                            _award_xp_with_feedback(subject_id, 30, ckey)
                        else:
                            st.warning("**Output Mismatch:** Compare your actual output against expected output below.")
                            c_e1, c_e2 = st.columns(2)
                            with c_e1:
                                st.markdown("**Expected Output:**")
                                st.code(expected_out, language="text")
                            with c_e2:
                                st.markdown("**Your Output:**")
                                st.code((stdout or "").strip() or "(empty)", language="text")
                    else:
                        _award_xp_with_feedback(subject_id, 30, ckey)

    with tab_why:
        why_text = block.get("why_it_works") or block.get("why_works") or block.get("explanation") or ""
        comp_text = block.get("complexity") or ""
        if why_text:
            st.markdown(render_markdown_html(why_text), unsafe_allow_html=True)
        if comp_text:
            st.markdown("#### Time & Space Complexity")
            st.markdown(render_markdown_html(comp_text), unsafe_allow_html=True)
        if not why_text and not comp_text:
            st.info("Ensure strict type contracts, clean modularity, and deterministic state transitions.")

    with tab_alternatives:
        alts = block.get("alternatives")
        if isinstance(alts, list) and alts:
            for item in alts:
                if isinstance(item, dict):
                    st.markdown(render_markdown_html(f"- **{item.get('title', 'Alternative')}**: {item.get('desc', '')}"), unsafe_allow_html=True)
                else:
                    st.markdown(render_markdown_html(f"- {item}"), unsafe_allow_html=True)
        elif isinstance(alts, str) and alts.strip():
            st.markdown(render_markdown_html(alts), unsafe_allow_html=True)
        else:
            st.info("Evaluate memory vs CPU trade-offs and synchronous vs decoupled execution paths.")

    with tab_edge_cases:
        ec = block.get("edge_cases")
        if isinstance(ec, list) and ec:
            for item in ec:
                if isinstance(item, dict):
                    st.markdown(
                        f'<div class="gh-alert gh-alert-warning">'
                        f'<div class="gh-alert-title">{html.escape(str(item.get("title", "Edge Case")))}</div>'
                        f'<div class="gh-alert-body">{render_markdown_html(str(item.get("desc", "")))}</div>'
                        f'</div>',
                        unsafe_allow_html=True,
                    )
                else:
                    st.markdown(render_markdown_html(f"- {item}"), unsafe_allow_html=True)
        elif isinstance(ec, str) and ec.strip():
            st.markdown(render_markdown_html(ec), unsafe_allow_html=True)
        else:
            st.info("Test for empty inputs, null boundaries, concurrency races, and integer overflow/precision limits.")

def _render_dsa_problem(block: Dict[str, Any], subject_id: str, case_id: int, module_idx: int, block_idx: int):
    ckey = f"{subject_id}_{case_id}_m{module_idx}_b{block_idx}"
    title = html.escape(str(block.get("title", "DSA Coding Challenge")))
    diff = str(block.get("difficulty", "Medium")).strip()
    diff_cls = {"easy": "diff-easy", "medium": "diff-medium", "hard": "diff-hard"}.get(diff.lower(), "diff-medium")
    pattern = html.escape(str(block.get("pattern", "Algorithm Design")))
    t_time = html.escape(str(block.get("target_time", "O(N)")))
    t_space = html.escape(str(block.get("target_space", "O(N)")))
    source_tag = html.escape(str(block.get("platform_style", "Online Judge Problem")))

    stmt_html = render_markdown_html(block.get("statement", ""))

    examples_html = ""
    for ex_idx, ex in enumerate(block.get("examples", []), 1):
        ex_in = html.escape(str(ex.get("input", "")))
        ex_out = html.escape(str(ex.get("output", "")))
        ex_exp = render_markdown_html(str(ex.get("explanation", ""))) if ex.get("explanation") else ""
        exp_line = f'<div style="color:#D4D4D8;font-family:inherit;margin-top:6px;"><strong>Explanation:</strong> {ex_exp}</div>' if ex_exp else ""
        examples_html += (
            f'<div class="dsa-example-box">'
            f'<div style="color:#A5B4FC;font-weight:700;font-size:0.72rem;text-transform:uppercase;margin-bottom:4px;">Example {ex_idx}</div>'
            f'<div><strong style="color:#71717A;">Input:</strong> <code>{ex_in}</code></div>'
            f'<div><strong style="color:#71717A;">Output:</strong> <code style="color:#34D399;">{ex_out}</code></div>'
            f'{exp_line}</div>'
        )

    constraints = block.get("constraints", [])
    cons_html = ""
    if constraints:
        items_li = "".join(f"<li>{render_markdown_html(str(c))}</li>" for c in constraints)
        cons_html = (
            f'<div class="dsa-constraint-box">'
            f'<div style="color:#71717A;font-weight:700;font-size:0.72rem;text-transform:uppercase;margin-bottom:6px;">Constraints &amp; Bounds</div>'
            f'<ul style="margin:0;padding-left:20px;">{items_li}</ul></div>'
        )

    st.markdown(
        f'<div class="dsa-judge-card">'
        f'<div class="card-kicker" style="color:#38BDF8;">{source_tag}</div>'
        f'<div class="card-heading" style="color:#FAFAFA;font-size:1.30rem;margin-bottom:10px;">{title}{_solved_badge(ckey)}</div>'
        f'<div class="dsa-meta-bar">'
        f'<span class="diff-pill {diff_cls}">{html.escape(diff)}</span>'
        f'<span class="pattern-pill">Pattern: {pattern}</span>'
        f'<span class="complexity-pill">Time: {t_time}</span>'
        f'<span class="complexity-pill">Space: {t_space}</span>'
        f'</div>'
        f'<div class="card-body">{stmt_html}</div>'
        f'{examples_html}{cons_html}</div>',
        unsafe_allow_html=True,
    )

    tab_solve, tab_approach, tab_dry, tab_edges = st.tabs([
        "Code & Online Judge",
        "Approach Ladder",
        "Dry Run & Complexity",
        "Edge Cases & Follow-ups",
    ])

    with tab_solve:
        lang_choice = st.radio(
            "Select Judge Language:",
            ["Python 3", "C++17 (STL)"],
            horizontal=True,
            key=f"dsa_lang_{ckey}",
        )
        is_cpp = ("C++" in lang_choice)
        lang_suffix = "cpp" if is_cpp else "py"
        starter = block.get("starter_cpp" if is_cpp else "starter_py", "")
        sol_code = block.get("solution_cpp" if is_cpp else "solution_py", "")
        harness = block.get("harness_cpp" if is_cpp else "harness_py", "")
        preamble = block.get("preamble_cpp" if is_cpp else "preamble_py", "")

        user_code = _render_ace_or_textarea(
            f"dsa_editor_{ckey}_{lang_suffix}",
            starter,
            language="c_cpp" if is_cpp else "python",
            height=330,
            allow_solution=sol_code or None,
        )

        if block.get("hint"):
            with st.expander("Algorithm Hint"):
                st.markdown(render_markdown_html(block["hint"]), unsafe_allow_html=True)

        c_run, c_sub, _ = st.columns([1.4, 1.6, 2.0])
        with c_run:
            run_samples = st.button("Run Sample Tests", key=f"dsa_sample_{ckey}", use_container_width=True)
        with c_sub:
            submit_all = st.button("Submit Solution", type="primary", key=f"dsa_submit_{ckey}", use_container_width=True)

        if (run_samples or submit_all) and _check_exec_cooldown():
            sample_only = bool(run_samples and not submit_all)
            with st.spinner("Compiling & judging against test cases..."):
                res = runners.run_dsa_judge(
                    "cpp" if is_cpp else "python",
                    user_code,
                    harness,
                    preamble_code=preamble,
                    sample_only=sample_only,
                    timeout=8,
                )
            st.session_state[f"dsa_res_{ckey}"] = (sample_only, lang_choice, res)
            if not sample_only and res.get("verdict") == "Accepted":
                _award_xp_with_feedback(subject_id, 35, ckey)

        saved_res = st.session_state.get(f"dsa_res_{ckey}")
        if saved_res:
            is_sample_mode, used_lang, res = saved_res
            verdict = res.get("verdict", "Runtime Error")
            passed_cnt = res.get("passed_count", 0)
            total_cnt = res.get("total_count", 0)
            mode_lbl = "Sample Run" if is_sample_mode else "Full Judge Submission"

            if verdict == "Accepted":
                v_cls = "verdict-accepted"
                v_msg = f"{verdict} — {passed_cnt}/{total_cnt} Test Cases Passed"
            elif verdict == "Wrong Answer":
                v_cls = "verdict-wa"
                v_msg = f"Wrong Answer — {passed_cnt}/{total_cnt} Test Cases Passed"
            else:
                v_cls = "verdict-err"
                v_msg = f"{verdict}"

            st.markdown(
                f'<div class="dsa-verdict-banner {v_cls}">'
                f'<span>{html.escape(v_msg)}</span>'
                f'<span style="font-size:0.78rem;opacity:0.9;">{html.escape(used_lang)} · {mode_lbl}</span>'
                f'</div>',
                unsafe_allow_html=True,
            )

            if res.get("error_detail"):
                st.code(res["error_detail"], language="text")

            for tc in res.get("cases", []):
                tc_ok = bool(tc.get("passed"))
                tc_cls = "dsa-tc-pass" if tc_ok else "dsa-tc-fail"
                tc_badge = "PASS" if tc_ok else "FAIL"
                tc_color = "#34D399" if tc_ok else "#F87171"
                err_html = f'<div style="color:#FCA5A5;margin-top:4px;"><strong>Error:</strong> <code>{html.escape(str(tc["error"]))}</code></div>' if tc.get("error") else ""
                st.markdown(
                    f'<div class="dsa-tc-card {tc_cls}">'
                    f'<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:4px;">'
                    f'<strong style="color:#FAFAFA;">{html.escape(str(tc.get("name", "Test")))}</strong>'
                    f'<span style="color:{tc_color};font-weight:700;font-family:\'JetBrains Mono\',monospace;">{tc_badge} <span style="color:#71717A;font-weight:500;margin-left:8px;">{tc.get("time_ms", 0)} ms</span></span>'
                    f'</div>'
                    f'<div style="font-family:\'JetBrains Mono\',Menlo,monospace;color:#D4D4D8;font-size:0.82rem;">'
                    f'<div><span style="color:#71717A;">Input:</span> {html.escape(str(tc.get("input", "")))}</div>'
                    f'<div><span style="color:#71717A;">Expected:</span> <span style="color:#93C5FD;">{html.escape(str(tc.get("expected", "")))}</span></div>'
                    f'<div><span style="color:#71717A;">Output:</span> <span style="color:{tc_color};">{html.escape(str(tc.get("actual", "")))}</span></div>'
                    f'{err_html}</div></div>',
                    unsafe_allow_html=True,
                )

            if res.get("debug_stdout"):
                with st.expander("Console Stdout / Debug Output", expanded=True):
                    st.code(res["debug_stdout"], language="text")

    with tab_approach:
        ladder = block.get("approach_ladder", {})
        if isinstance(ladder, dict) and ladder:
            steps_meta = [
                ("brute", "Step 1: Brute Force Baseline", "#F87171"),
                ("better", "Step 2: Intermediate Optimization", "#FBBF24"),
                ("optimal", "Step 3: Optimal Production Solution", "#34D399"),
            ]
            for k_step, label_step, col_step in steps_meta:
                if ladder.get(k_step):
                    st.markdown(
                        f'<div class="trace-step" style="border-left-color:{col_step};">'
                        f'<strong style="color:{col_step};">{label_step}</strong>'
                        f'<div style="margin-top:6px;">{render_markdown_html(str(ladder[k_step]))}</div>'
                        f'</div>',
                        unsafe_allow_html=True,
                    )
        else:
            st.info("Analyze the bottleneck in nested brute-force scans and replace O(N) lookups with O(1)/O(log N) structures or monotonic invariants.")

    with tab_dry:
        if block.get("dry_run"):
            st.markdown(render_markdown_html(block["dry_run"]), unsafe_allow_html=True)
        if block.get("complexity_analysis"):
            st.markdown(render_markdown_html(block["complexity_analysis"]), unsafe_allow_html=True)
        elif not block.get("dry_run"):
            st.markdown(f"**Target Time:** `{block.get('target_time', 'O(N)')}` · **Target Space:** `{block.get('target_space', 'O(N)')}`")

    with tab_edges:
        edges = block.get("edge_cases", [])
        if isinstance(edges, list) and edges:
            for item in edges:
                if isinstance(item, dict):
                    st.markdown(
                        f'<div class="gh-alert gh-alert-warning">'
                        f'<div class="gh-alert-title">{html.escape(str(item.get("title", "Edge Case")))}</div>'
                        f'<div class="gh-alert-body">{render_markdown_html(str(item.get("desc", "")))}</div></div>',
                        unsafe_allow_html=True,
                    )
                else:
                    st.markdown(render_markdown_html(f"- {item}"), unsafe_allow_html=True)
        elif isinstance(edges, str) and edges.strip():
            st.markdown(render_markdown_html(edges), unsafe_allow_html=True)
        if block.get("follow_ups"):
            st.markdown("#### Follow-up Variations")
            st.markdown(render_markdown_html(block["follow_ups"]), unsafe_allow_html=True)

def render_block(block: Dict[str, Any], subject_id: str, case_id: int, module_idx: int, block_idx: int):
    btype = block.get("type")
    
    if btype in ("story", "markdown", "narrative", "text"):
        raw_text = block.get("text") or block.get("content", "")
        html_content = render_markdown_html(raw_text)
        title = block.get("title", "")
        title_html = f'<div class="card-heading heading-briefing">{html.escape(str(title))}</div>' if title else ""
        card_html = (
            f'<div class="briefing-card">\n'
            f'<div class="card-kicker kicker-briefing">MISSION BRIEFING</div>\n'
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
            title_html = f'<div class="card-heading heading-objective">{html.escape(str(title))}</div>'
        card_html = (
            f'<div class="objective-card">\n'
            f'<div class="card-kicker kicker-objective">LEARNING OBJECTIVE</div>\n'
            f'{title_html}\n'
            f'<div class="card-body">{html_content}</div>\n'
            f'</div>'
        )
        st.markdown(card_html, unsafe_allow_html=True)
        
    elif btype in ("concept", "theory"):
        raw_content = block.get("explanation") or block.get("content", "")
        html_content = render_markdown_html(raw_content)
        title = html.escape(str(block.get("title", "Core Architecture & Theory")))
        title_html = f'<div class="card-heading heading-theory">{title}</div>'
        tech_html_box = ""
        if "technical_explanation" in block:
            tech_inner = render_markdown_html(block["technical_explanation"])
            tech_html_box = (
                f'<div class="theory-tech-box">\n'
                f'<span class="theory-tech-label">Architectural Invariants &amp; Mechanics</span>\n'
                f'<div class="card-body" style="margin-top: 6px; font-size: 0.93rem; color: #D4D4D8;">{tech_inner}</div>\n'
                f'</div>'
            )
        card_html = (
            f'<div class="theory-card">\n'
            f'<div class="card-kicker kicker-theory">ARCHITECTURE &amp; THEORY</div>\n'
            f'{title_html}\n'
            f'<div class="card-body">{html_content}</div>\n'
            f'{tech_html_box}\n'
            f'</div>'
        )
        st.markdown(card_html, unsafe_allow_html=True)
        if "analogy" in block:
            st.info(f"**Analogy:** {block['analogy']}")
            
    elif btype == "problem":
        raw_text = block.get("text") or block.get("content", "")
        html_content = render_markdown_html(raw_text)
        title = html.escape(str(block.get("title", "Architectural Incident")))
        card_html = (
            f'<div class="incident-card">\n'
            f'<div class="card-kicker kicker-incident">INCIDENT REPORT</div>\n'
            f'<div class="card-heading heading-incident">{title}</div>\n'
            f'<div class="card-body">{html_content}</div>\n'
            f'</div>'
        )
        st.markdown(card_html, unsafe_allow_html=True)

    elif btype in ("mermaid_diagram", "visual"):
        if "title" in block: st.markdown(f"#### {block['title']}")
        if "explanation" in block: st.markdown(clean_newlines(block["explanation"]))
        diag_code = block.get("code") or block.get("data") or block.get("mermaid", "")
        v_type = block.get("visual_type")
        if v_type == "text" or not is_mermaid_diagram(diag_code):
            render_ascii_diagram(diag_code, title=block.get("title", "ARCHITECTURAL SCHEMATIC"))
        else:
            st_mermaid(diag_code, height=block.get("height"))

    elif btype == "visual_stepper":
        if "title" in block: st.markdown(f"#### {block['title']}")
        steps = block.get("steps", [])
        if steps:
            step_key = f"stepper_{subject_id}_{case_id}_{module_idx}_{block_idx}"
            if step_key not in st.session_state:
                st.session_state[step_key] = 0
            
            step_idx = max(0, min(int(st.session_state[step_key]), len(steps) - 1))
            step = steps[step_idx]
            
            c_prev, c_center, c_next = st.columns([1, 2, 1])
            with c_prev:
                if st.button("Prev Step", key=f"btn_prev_{step_key}", disabled=(step_idx <= 0), use_container_width=True):
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
                if st.button("Next Step", key=f"btn_next_{step_key}", disabled=(step_idx >= len(steps) - 1), use_container_width=True):
                    st.session_state[step_key] = min(len(steps) - 1, step_idx + 1)
                    st.rerun()
            
            step_html = (
                f'<div class="trace-step" style="border-left-width:3px;padding:12px 16px;margin:10px 0 14px 0;">\n'
                f'<span style="color: #A5B4FC; font-family: \'JetBrains Mono\', monospace; font-weight: 600; font-size: 0.78rem; text-transform: uppercase;">Step {step_idx + 1} of {len(steps)}</span>\n'
                f'<div style="color: #FAFAFA; margin-top: 4px; font-size: 0.96rem; line-height: 1.55;">{render_markdown_html(step.get("explanation", ""))}</div>\n'
                f'</div>'
            )
            st.markdown(step_html, unsafe_allow_html=True)
            st_mermaid(step.get("mermaid_code", ""), height=block.get("height"))

    elif btype == "header":
        meta = block.get("metadata", {}) or {}
        diff = html.escape(str(meta.get("difficulty", "Core")))
        dur = html.escape(str(meta.get("time", "15m")))
        chips = "".join(f'<span class="concept-chip">{html.escape(str(c))}</span>' for c in meta.get("concepts", []))
        banner = (
            f'<div class="oop-header-banner">'
            f'<div class="card-kicker kicker-objective">MODULE BRIEFING · {diff.upper()} · {dur}</div>'
            f'<div style="font-size:1.25rem;font-weight:700;color:#FAFAFA;margin-bottom:4px;">{html.escape(str(block.get("title", "")))}</div>'
            f'<div style="color:#A1A1AA;font-size:0.92rem;margin-bottom:8px;">{html.escape(str(block.get("subtitle", "")))}</div>'
            f'<div>{chips}</div>'
            f'</div>'
        )
        st.markdown(banner, unsafe_allow_html=True)

    elif btype == "worked_example":
        title = html.escape(str(block.get("title", "Worked Walkthrough")))
        steps = block.get("steps", [])
        rows_html = ""
        for idx_s, s_item in enumerate(steps, 1):
            txt_s = s_item.get("text") or str(s_item) if isinstance(s_item, dict) else str(s_item)
            txt_s = re.sub(r"^\d+\.\s*", "", txt_s.strip())
            rows_html += f'<div class="trace-step"><strong>Step {idx_s}:</strong> {render_markdown_html(txt_s)}</div>'
        st.markdown(
            f'<div class="concept-card"><div class="card-kicker kicker-concept">WORKED EXAMPLE</div>'
            f'<div class="card-heading heading-concept">{title}</div>{rows_html}</div>',
            unsafe_allow_html=True,
        )

    elif btype == "reflection":
        ckey = f"{subject_id}_{case_id}_m{module_idx}_b{block_idx}"
        q_html = render_markdown_html(block.get("question", ""))
        st.markdown(
            f'<div class="scenario-card"><div class="card-kicker kicker-scenario">ENGINEERING REFLECTION</div>'
            f'<div class="card-body">{q_html}</div></div>',
            unsafe_allow_html=True,
        )
        note_key = f"refl_{ckey}"
        note = st.text_area("Jot down your engineering hypothesis (optional):", key=note_key, height=85, placeholder="Write your reasoning before advancing...")
        if st.button("Save Reflection Note", key=f"refl_btn_{ckey}"):
            if note.strip():
                st.success("Reflection captured in your active investigation session.")
            else:
                st.info("Write a brief thought above to record your synthesis.")

    elif btype == "data_explorer":
        st.markdown(f"### Interactive Data Explorer: {block.get('title', '')}")
        if block.get("context"):
            st.markdown(render_markdown_html(block["context"]), unsafe_allow_html=True)
        if block.get("scenario") == "update_anomaly":
            import pandas as pd
            c1, c2 = st.columns(2)
            with c1:
                st.markdown("**Payroll Department Ledger (Stale)**")
                st.dataframe(pd.DataFrame({"Name": ["John Smith"], "Address": ["Sector A"], "Salary": [50000]}), use_container_width=True, hide_index=True)
            with c2:
                st.markdown("**Housing Department Ledger (Updated)**")
                st.dataframe(pd.DataFrame({"Name": ["John Smith"], "Address": ["Sector B"], "Rent": [1200]}), use_container_width=True, hide_index=True)
            if st.button("Attempt Cross-File Synchronization", key=f"sync_{subject_id}_{case_id}_{module_idx}_{block_idx}"):
                st.error("Synchronization Failed: Flat file silos lack foreign keys or atomic transactions — permanent update anomaly detected.")

    elif btype == "mental_model":
        title = block.get("title", "Mental Model")
        data = str(block.get("data") or block.get("content") or "")
        if is_mermaid_diagram(data):
            st.markdown(f"#### {title}")
            st_mermaid(data)
        else:
            render_ascii_diagram(data, title=title)

    elif btype == "annotated_code":
        st.markdown(f"#### Code Dissection: {block.get('title', 'Annotated Implementation')}")
        code_txt = block.get("code", "")
        lang = block.get("language") or ("cpp" if subject_id == "oop" else "python")
        st.code(code_txt, language=lang)
        for ann in block.get("annotations", []):
            line_ref = html.escape(str(ann.get("line", "")))
            ann_txt = render_markdown_html(str(ann.get("text", "")))
            st.markdown(
                f'<div class="trace-step"><code style="color:#A5B4FC;">{line_ref}</code><div style="margin-top:4px;">{ann_txt}</div></div>',
                unsafe_allow_html=True,
            )

    elif btype == "execution_trace":
        st.markdown(f"#### Execution Trace: {block.get('title', '')}")
        lang = block.get("language") or ("cpp" if subject_id == "oop" else "python")
        if block.get("code"):
            st.code(block["code"], language=lang)
        for idx_t, step_t in enumerate(block.get("trace", []), 1):
            st.markdown(f'<div class="trace-step"><strong>Trace #{idx_t}:</strong> {render_markdown_html(str(step_t))}</div>', unsafe_allow_html=True)

    elif btype == "memory_layout":
        st.markdown(f"#### RAM & Memory Layout: {block.get('title', '')}")
        if block.get("explanation"):
            st.markdown(render_markdown_html(block["explanation"]), unsafe_allow_html=True)
        cells_html = "".join(
            f'<div class="memory-cell">'
            f'<div class="memory-addr">{html.escape(str(c.get("address", "")))}</div>'
            f'<div class="memory-val">{html.escape(str(c.get("value", "")))}</div>'
            f'<div class="memory-lbl">{html.escape(str(c.get("label", "")))}</div>'
            f'</div>'
            for c in block.get("cells", [])
        )
        st.markdown(f'<div class="memory-grid">{cells_html}</div>', unsafe_allow_html=True)

    elif btype in ("wrong_approach", "correct_approach"):
        is_bad = (btype == "wrong_approach")
        cls = "approach-wrong" if is_bad else "approach-correct"
        kicker = "ANTIPATTERN / FRAGILE APPROACH" if is_bad else "IDIOMATIC ENGINEERING APPROACH"
        st.markdown(
            f'<div class="{cls}"><div class="card-kicker" style="color:{"#F87171" if is_bad else "#34D399"};">{kicker}</div>'
            f'<div class="card-heading" style="color:#FAFAFA;">{html.escape(str(block.get("title", "")))}</div></div>',
            unsafe_allow_html=True,
        )
        if block.get("code"):
            st.code(block["code"], language=block.get("language") or ("cpp" if subject_id == "oop" else "python"))
        if block.get("explanation"):
            st.markdown(render_markdown_html(block["explanation"]), unsafe_allow_html=True)

    elif btype == "comparison_table":
        st.markdown(f"#### {block.get('title', 'Technical Comparison')}")
        headers = block.get("headers", [])
        rows = block.get("rows", [])
        th = "".join(f"<th>{html.escape(str(h))}</th>" for h in headers)
        tb = "".join(
            "<tr>" + "".join(f"<td>{html.escape(str(cell))}</td>" for cell in row) + "</tr>"
            for row in rows
        )
        st.markdown(f"<table><thead><tr>{th}</tr></thead><tbody>{tb}</tbody></table>", unsafe_allow_html=True)

    elif btype == "real_world_analogy":
        title = html.escape(str(block.get("title", "Real-World Analogy")))
        body = render_markdown_html(block.get("content", ""))
        st.markdown(
            f'<div class="analogy-card"><div class="card-kicker" style="color:#FBBF24;">REAL-WORLD ANALOGY</div>'
            f'<div class="card-heading" style="color:#FAFAFA;">{title}</div><div class="card-body">{body}</div></div>',
            unsafe_allow_html=True,
        )

    elif btype == "common_mistakes":
        st.markdown(f"#### Common Pitfalls: {block.get('title', '')}")
        for m in block.get("mistakes", []):
            m_title = html.escape(str(m.get("title", "Pitfall"))) if isinstance(m, dict) else "Pitfall"
            m_desc = render_markdown_html(str(m.get("desc", ""))) if isinstance(m, dict) else render_markdown_html(str(m))
            st.markdown(
                f'<div class="gh-alert gh-alert-caution"><div class="gh-alert-title">{m_title}</div>'
                f'<div class="gh-alert-body">{m_desc}</div></div>',
                unsafe_allow_html=True,
            )

    elif btype in ("micro_challenge", "mastery_challenge", "interactive"):
        _render_mcq_challenge(
            block, subject_id, case_id, module_idx, block_idx,
            form_prefix="mc", icon="", title=block.get("title", "Concept Check"), xp_reward=15,
        )

    elif btype == "think_first":
        _render_mcq_challenge(
            block, subject_id, case_id, module_idx, block_idx,
            form_prefix="tf", icon="", title=block.get("title", "Think First: Predict the Outcome"), xp_reward=15,
            submit_label="Check Prediction",
        )

    elif btype == "debugger":
        scen_html = (
            f'<div class="gh-alert gh-alert-warning">'
            f'<div class="gh-alert-title">SYSTEM BUG SCENARIO</div>'
            f'<div class="gh-alert-body">{render_markdown_html(block.get("scenario", ""))}</div>'
            f'</div>'
        )
        _render_mcq_challenge(
            block, subject_id, case_id, module_idx, block_idx,
            form_prefix="dbg", icon="", title=f"Root-Cause Debugger: {block.get('title', '')}",
            xp_reward=20, submit_label="Diagnose Bug", preamble_html=scen_html,
            radio_label="Select the root cause:",
        )

    elif btype in ("scenario_decision", "dilemma", "tradeoff_dilemma"):
        scenario_html = render_markdown_html(block.get("scenario") or block.get("content", ""))
        title = block.get("title", "Engineering Decision Dilemma")
        scen_card = (
            f'<div class="scenario-card">\n'
            f'<div class="card-kicker kicker-scenario">ARCHITECTURAL TRADE-OFF</div>\n'
            f'<div class="card-heading heading-scenario">{html.escape(str(title))}</div>\n'
            f'<div class="card-body">{scenario_html}</div>\n'
            f'</div>'
        )
        _render_mcq_challenge(
            block, subject_id, case_id, module_idx, block_idx,
            form_prefix="scen", icon="", title=title, xp_reward=25,
            submit_label="Submit Strategic Decision",
            guide_title="Reveal Trade-off Breakdown & Best Practice",
            explanation_key="rationale", preamble_html=scen_card,
            radio_label="Choose your course of action:", is_strategic=True,
        )

    elif btype in ("calculation_challenge", "metric_challenge"):
        ckey = f"{subject_id}_{case_id}_m{module_idx}_b{block_idx}"
        safe_title = html.escape(str(block.get("title", "Engineering Metric Calculation")))
        st.markdown(f'<h3 style="margin-top:16px;margin-bottom:8px;">{safe_title}{_solved_badge(ckey)}</h3>', unsafe_allow_html=True)
        if block.get("formula"):
            st.markdown(
                f'<div style="background: #111114; border: 1px solid #222226; border-left: 3px solid #3B82F6; border-radius: 8px; padding: 12px 16px; margin-bottom: 12px;">'
                f'<span style="color: #60A5FA; font-family: \'JetBrains Mono\', monospace; font-weight: 600; font-size: 0.74rem; text-transform: uppercase; letter-spacing: 0.05em;">Governing Formula &amp; Invariants</span>'
                f'<div style="color: #FAFAFA; margin-top: 6px; font-size: 1.00rem;">{render_markdown_html(block["formula"])}</div>'
                f'</div>',
                unsafe_allow_html=True,
            )

        p = block.get("problem") or block.get("question", "")
        st.markdown(f'<div class="card-body" style="margin-bottom: 12px;">{render_markdown_html(p)}</div>', unsafe_allow_html=True)

        with st.form(key=f"calc_form_{ckey}"):
            user_val = st.text_input("Calculated Metric Value:", key=f"calc_input_{ckey}")
            submitted = st.form_submit_button("Verify Metric")
            if submitted:
                expected_val = str(block.get("answer", ""))
                alts = block.get("alternatives", [])
                if check_answer_match(user_val, expected_val, alts):
                    st.success(f"**Exact Calculation!** `{user_val.strip()}` is mathematically correct.")
                    _award_xp_with_feedback(subject_id, 20, ckey)
                else:
                    st.error(f"**Calculation Mismatch.** You computed `{user_val.strip()}`. Expected value: **`{expected_val}`**.")

                if block.get("step_by_step") or block.get("explanation"):
                    with st.container(border=True):
                        st.markdown("#### Step-by-Step Derivation")
                        st.markdown(render_markdown_html(block.get("step_by_step") or block.get("explanation")), unsafe_allow_html=True)

        if block.get("step_by_step") or block.get("explanation"):
            with st.expander("Reveal Full Mathematical Derivation"):
                st.markdown(render_markdown_html(block.get("step_by_step") or block.get("explanation")), unsafe_allow_html=True)

    elif btype in ("diagram_critique", "spot_the_flaw"):
        st.markdown(f"### {block.get('title', 'Diagram Review & Flaw Detection')}")
        if block.get("scenario"):
            st.markdown(f'<div class="card-body" style="margin-bottom: 12px;">{render_markdown_html(block["scenario"])}</div>', unsafe_allow_html=True)
        if block.get("code"):
            st_mermaid(block["code"], height=block.get("height"))
        _render_mcq_challenge(
            block, subject_id, case_id, module_idx, block_idx,
            form_prefix="crit", icon="", title="Identify the Flaw", xp_reward=25,
            submit_label="Submit Diagnostic Review",
            guide_title="Reveal Flaw Analysis & Correction",
            explanation_key="remedy", radio_label="Select detected defect:",
        )

    elif btype == "fill_in_the_blank":
        ckey = f"{subject_id}_{case_id}_m{module_idx}_b{block_idx}"
        safe_title = html.escape(str(block.get("title", "Fill in the Blank Challenge")))
        st.markdown(f'<h3 style="margin-top:16px;margin-bottom:8px;">{safe_title}{_solved_badge(ckey)}</h3>', unsafe_allow_html=True)
        q = block.get("question", "")

        with st.form(key=f"fib_form_{ckey}"):
            st.markdown(render_markdown_html(q.replace("_____", "___")), unsafe_allow_html=True)
            user_ans = st.text_input("Your Answer:", key=f"fib_input_{ckey}")
            submitted = st.form_submit_button("Submit Answer")
            if submitted:
                ans = block.get("answer", "")
                alts = block.get("alternatives", [])
                if check_answer_match(user_ans, ans, alts):
                    st.success(f"**Correct:** `{user_ans.strip()}` is the right answer.")
                    _award_xp_with_feedback(subject_id, 20, ckey)
                else:
                    clean_disp = str(ans).rstrip(".").strip()
                    st.error(f"**Incorrect.** You entered `{user_ans.strip()}`. Expected answer: **`{clean_disp}`**.")

                if block.get("explanation"):
                    with st.container(border=True):
                        st.markdown(render_markdown_html(block.get("explanation")), unsafe_allow_html=True)

        if block.get("explanation"):
            with st.expander("Reveal Answer Explanation"):
                st.markdown(render_markdown_html(block.get("explanation")), unsafe_allow_html=True)

    elif btype == "sql_sandbox":
        _render_sql_sandbox(block, subject_id, case_id, module_idx, block_idx)

    elif btype == "dsa_problem":
        _render_dsa_problem(block, subject_id, case_id, module_idx, block_idx)

    elif btype in ("code_lab", "code_experiment"):
        _render_code_lab(block, subject_id, case_id, module_idx, block_idx)

    else:
        fallback_title = block.get("title") or str(btype or "Note").replace("_", " ").title()
        fallback_body = block.get("content") or block.get("text") or block.get("explanation") or ""
        if fallback_body:
            st.markdown(
                f'<div class="briefing-card"><div class="card-heading heading-briefing">{html.escape(str(fallback_title))}</div>'
                f'<div class="card-body">{render_markdown_html(str(fallback_body))}</div></div>',
                unsafe_allow_html=True,
            )
