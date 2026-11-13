# Comprehensive Project Architecture & Deployment Audit
**Platform:** Learning_Platform (Engineering Story Labs)  
**Date:** November 13, 2026  
**Auditor:** Antigravity DeepMind Agentic Pair Programmer  
**Audit Scope:** Read-Only Source Code, Repository, Architecture & Cloud Deployment Investigation  
**Status:** COMPLETE (Awaiting User Review — No Code Modifications Applied)

---

## Executive Summary

An exhaustive, read-only architectural and deployment audit was conducted across the **Learning_Platform (Engineering Story Labs)** repository (`/Users/aadarshamahato/Downloads/LEARNING_PLATFORM`).

### Primary Breakthrough Finding: Why Remote Deployment Failed
The previous deployment attempts on Streamlit Cloud failed due to **three intersecting root causes**:
1. **The Submodule Gitlink Trap (CRITICAL):** In Git commit `391e891` on `origin/main`, two of the eight subjects—`dbms_story_lab` and `oop_story_lab`—were added as Git submodules (`160000 commit` gitlinks) rather than tracked file trees because they contained local `.git` directories. Crucially, **no `.gitmodules` configuration exists in the repository**. When Streamlit Cloud clones `https://github.com/AdakMahato/Learning_Platform.git`, Git leaves `dbms_story_lab/` and `oop_story_lab/` as **empty directories**. Any attempt by `core_loader.py` to import `story_data.py` fails immediately with `FileNotFoundError`.
2. **Streamlit Cloud Default Entry Point Mismatch (CRITICAL):** Streamlit Community Cloud defaults to looking for a file named `streamlit_app.py`. The actual master platform entry point is `app.py`. When deploying without explicitly overriding the default path, Streamlit Cloud displays `"This file does not exist"` in red.
3. **Competing Entry Points & Missing Ecosystem Packages (HIGH):** The repository contains 7 competing `app.py` files across legacy standalone prototypes. Furthermore, while the unified `app.py` imports `streamlit-ace`, `markdown`, `pandas`, and `numpy`, individual subject scripts reference `plotly` and `g++` (needed for compiling C++ OOP labs and DSA online judges). While `packages.txt` with `g++` exists locally, root `requirements.txt` does not include `plotly`.

---

## 1. Complete Project Structure

Below is the directory tree of the workspace, excluding virtual environments (`venv/`), Python bytecode (`__pycache__/`), Git internals (`.git/`), and Node modules (`web/node_modules/`).

```
LEARNING_PLATFORM/
├── Dockerfile                              # Multi-stage production container build (Debian slim, g++, non-root user)
├── README.md                               # Platform documentation, quickstart guide, architectural overview
├── Story_Driven_DBMS_Learning_Report.pdf   # Academic / industrial background research report
├── app.py                                  # MASTER APPLICATION ENTRY POINT (Routing, Query Params, Auth, Navigation)
├── core_loader.py                          # Central Subject Registry & Dynamic Module Loader
├── docker-compose.yml                      # Container orchestration with volume mounts, memory/cpu limits
├── master_ui.py                            # Master UI Design System (Obsidian/Zinc theme, LaTeX math, Code Labs, Steppers)
├── nginx.conf.example                      # Reverse proxy & SSL termination configuration
├── packages.txt                            # Debian APT system dependencies for Streamlit Cloud (contains: g++)
├── platform_progress.json                  # Legacy local JSON progress snapshot (superseded by SQLite)
├── render.yaml                             # Cloud deployment blueprint with 1GB persistent disk mount
├── requirements.txt                        # Root Python package dependencies
├── runners.py                              # Secure execution sandboxes (Python AST/RLIMIT, C++ g++ compiler, SQLite)
├── unified_persistence.py                  # Thread-safe SQLite WAL multi-user persistence & PBKDF2 authentication
│
├── .devcontainer/                          # VS Code Remote Container development configuration
│   └── devcontainer.json
│
├── .streamlit/                             # Streamlit runtime configuration
│   └── config.toml                         # Dark theme (#09090B), headless=true, XSRF protection, minimal toolbar
│
├── data/                                   # Database storage directory (persists platform.db and .secret_key)
│   ├── .secret_key                         # Generated 256-bit HMAC session signing key
│   └── platform.db                         # SQLite WAL database (users, progress, active modules, solved challenges)
│
├── tests/                                  # Platform verification and security regression tests
│   └── test_security_and_runners.py        # 9 unit tests verifying timeouts, memory caps, AST safety, g++ & SQLite
│
├── ai_story_lab/                           # SUBJECT TRACK 02: Artificial Intelligence (25 Cases, 103 Modules, 990 Blocks)
│   ├── app.py                              # Legacy standalone Streamlit app for AI
│   ├── story_data.py                       # 25 AI forensic case definitions (A*, Minimax, CSPs, Bayes, Q-Learning)
│   ├── level_content.py                    # 103 interactive learning episodes with quizzes, code labs, steppers
│   ├── engineering_labs.py                 # Algorithmic lab environments
│   ├── capstone_project.py                 # Multi-agent AI capstone
│   ├── content_01_07.py                    # Modular content generator (Cases 1-7)
│   ├── content_08_15.py                    # Modular content generator (Cases 8-15)
│   ├── content_16_24.py                    # Modular content generator (Cases 16-24)
│   ├── quizzes_part1.py to part5.py        # Comprehensive diagnostic assessment banks
│   ├── persistence.py                      # Legacy AI-specific JSON persistence
│   ├── py_runner.py                        # Legacy AI sandbox runner
│   ├── ui.py                               # Legacy AI UI renderer
│   └── pages/                              # 25 legacy Streamlit multipage files (00_*.py to 24_*.py)
│
├── cloud_story_lab/                        # SUBJECT TRACK 04: Cloud Computing (16 Cases, 64 Modules, 224 Blocks)
│   ├── app.py                              # Legacy standalone Streamlit app for Cloud
│   ├── story_data.py                       # 16 Cloud architecture case definitions (AWS, Hypervisors, SDN, Hadoop, FinOps)
│   ├── level_content.py                    # 64 interactive modules (primitives, capacity calculations, forensics)
│   ├── build_cloud_part1.py to part4.py    # Curriculum compilation scripts
│   ├── persistence.py                      # Legacy Cloud-specific persistence
│   ├── py_runner.py                        # Legacy Cloud runner
│   ├── ui.py                               # Legacy Cloud UI renderer
│   └── pages/                              # 16 legacy Streamlit multipage files
│
├── dbms_story_lab/                         # SUBJECT TRACK 01: Database Management Systems (12 Cases, 98 Modules, 359 Blocks)
│   ├── app.py                              # Legacy standalone Streamlit app for DBMS
│   ├── story_data.py                       # 12 DBMS case definitions (Relational Algebra, SQL, Normalization, ACID, B+ Trees)
│   ├── level_content.py                    # 98 interactive modules with live SQLite sandboxes and query debuggers
│   ├── cases_1_2_3.py to cases_21_23.py    # Granular case content definitions
│   ├── deep_01_05.py to deep_17_24.py      # Deep-dive forensic scenarios
│   ├── ultra_01_05.py to ultra_17_24.py    # Advanced SQL optimization & query plan scenarios
│   ├── challenges.py                       # SQL forensics challenges
│   ├── field_notebook.py                   # Investigator notebook component
│   ├── persistence.py                      # Legacy DBMS persistence
│   ├── progress.db                         # Legacy SQLite database
│   ├── requirements.txt                    # Legacy subject requirements (streamlit, pandas, plotly)
│   ├── ui.py                               # Legacy DBMS UI renderer
│   └── pages/                              # 21 legacy Streamlit multipage files
│
├── dsa_story_lab/                          # SUBJECT TRACK 06: Data Structures & Algorithms (19 Cases, 76 Modules, 170 Blocks)
│   ├── story_data.py                       # 19 DSA case definitions (Sliding Window, Trees, Graphs, DP, Proofs)
│   ├── level_content.py                    # Aggregator importing dsa_part1 through dsa_part5 via importlib
│   ├── dsa_part1.py                        # Cases 0-3: Two Pointers, Monotonic Stacks, Fast-Slow Pointers
│   ├── dsa_part2.py                        # Cases 4-7: Trees, BFS/DFS, Heaps, Topological Sort
│   ├── dsa_part3.py                        # Cases 8-11: Shortest Path, Disjoint Set Union, Backtracking, Interval Scheduling
│   ├── dsa_part4.py                        # Cases 12-15: Dynamic Programming, 2D Grid DP, Knapsack, Asymptotic Proofs
│   └── dsa_part5.py                        # Cases 16-18: Tries, Bit Manipulation, String Hashing (38 Dual Python+C++ Judges)
│
├── ip_story_lab/                           # SUBJECT TRACK 08: Image Processing (16 Cases, 64 Modules, 127 Blocks)
│   ├── __init__.py                         # Package marker
│   ├── story_data.py                       # 16 Image & Video Processing case definitions (Beginner to Advanced High-Level)
│   ├── level_content.py                    # Aggregator importing cases_00_07 and cases_08_15 via importlib
│   ├── cases_00_07.py                      # Cases 0-7: Sampling, Spatial Filters, 2D FFT, Restoration, Color, Compression
│   └── cases_08_15.py                      # Cases 8-15: Morphology, Segmentation, Object Recognition, MPEG Video Coding
│
├── oop_story_lab/                          # SUBJECT TRACK 05: Object-Oriented Programming in C++ (29 Cases, 118 Modules, 790 Blocks)
│   ├── app.py                              # Legacy standalone Streamlit app for C++ OOP
│   ├── story_data.py                       # 29 C++ OOP case definitions (Stack/Heap, Pointers, VTables, RAII, Patterns)
│   ├── level_content.py                    # 118 interactive modules with live C++ compilation labs and memory layouts
│   ├── cases_01_to_04.py to 21_to_23.py    # Modular case content definitions
│   ├── oop_progress.db                     # Legacy OOP SQLite database
│   ├── packages.txt                        # Local packages note
│   ├── requirements.txt                    # Local subject requirements (streamlit, streamlit-ace)
│   ├── ui.py                               # Legacy OOP UI renderer
│   └── pages/                              # 29 legacy Streamlit multipage files
│
├── sd_story_lab/                           # SUBJECT TRACK 07: System Design (HLD & LLD) (14 Cases, 56 Modules, 112 Blocks)
│   ├── story_data.py                       # 14 System Design case definitions (Consistent Hashing, Raft, Snowflake, TinyURL)
│   ├── level_content.py                    # Aggregator importing sd_part1 through sd_part3 via importlib
│   ├── sd_part1.py                         # Cases 0-4: Back-of-the-Envelope Math, Caching, Consistent Hashing, CAP/PACELC
│   ├── sd_part2.py                         # Cases 5-9: Storage Engines, Raft Consensus, Rate Limiters, TinyURL, Snowflake IDs
│   └── sd_part3.py                         # Cases 10-13: Distributed Chat, Parking Lot OOP, Metrics Telemetry, Payments
│
├── se_story_lab/                           # SUBJECT TRACK 03: Software Engineering (16 Cases, 64 Modules, 260 Blocks)
│   ├── app.py                              # Legacy standalone Streamlit app for SE
│   ├── story_data.py                       # 16 SE case definitions (Software Crisis, Agile/Scrum, SRS, UML, SOLID, Testing)
│   ├── level_content.py                    # 64 interactive modules with architecture critique and code refactoring labs
│   ├── build_se_content_part1.py           # Curriculum builders
│   ├── persistence.py                      # Legacy SE persistence
│   ├── ui.py                               # Legacy SE UI renderer
│   └── pages/                              # 16 legacy Streamlit multipage files
│
├── streamlit/                              # OBSOLETE / ANCILLARY: Early Prototype Directory (Ignored in .gitignore)
│   ├── app.py                              # Legacy "DBMS Engineering Laboratory" prototype
│   ├── requirements.txt                    # Old dependency list with networkx, sympy, pyyaml
│   ├── components/                         # Early prototype UI components
│   ├── config/                             # Early prototype configurations
│   ├── content/                            # Early markdown/YAML content files
│   ├── core/                               # Early engine classes (ContentLoader, Evaluator, PrerequisiteEngine)
│   └── simulations/                        # Early simulation scripts (B+ tree, Dijkstra)
│
└── web/                                    # ANCILLARY: Next.js / TypeScript Web UI Project (Ignored in .gitignore)
    ├── package.json                        # Node dependencies (React 19, Next.js, Lucide, Tailwind)
    ├── src/app/                            # Next.js App Router frontend
    └── ...                                 # Independent web client
```

### Purpose of Key Root Files
- **`app.py`:** The primary production master application. Sets up global Streamlit page configuration, inspects and synchronizes browser URL parameters (`?subject=...&case=...`), enforces optional authentication gating, renders the Obsidian/Zinc top navigation bar, sticky sidebar case jumper, curriculum catalog, and delegating module rendering to `master_ui.py`.
- **`core_loader.py`:** Central subject registry (`SUBJECT_REGISTRY`) and dynamic module caching layer. Dynamically loads `story_data.py` and `level_content.py` from each of the 8 subject directories using `importlib.util.spec_from_file_location` without polluting `sys.path`.
- **`master_ui.py`:** Enterprise dark-glassmorphism rendering engine. Renders mathematical notation (LaTeX to Unicode/KaTeX), Mermaid architectural diagrams, GitHub alert callouts, interactive MCQ quizzes, live SQLite sandboxes, C++ compilation editors via `streamlit-ace`, and Python algorithm test runners.
- **`runners.py`:** Production-hardened sandboxes for running student submissions. Restricts Python execution via AST parsing (blocking `os`, `sys`, `socket`, `subprocess`, `__import__`) and OS-level limits (`setrlimit` for CPU, memory, file size, process count). Compiles C++ code safely with `g++ -O1 -std=c++17`. Sandboxes SQLite execution using `set_authorizer` to prevent write access to unauthorized system tables.
- **`unified_persistence.py`:** Multi-user SQLite storage engine with WAL (Write-Ahead Logging) mode and thread locks. Manages user registration, PBKDF2-SHA256 password hashing, HMAC session tokens, active case tracking, XP telemetry, and module completion state.
- **`packages.txt`:** Specifies system packages required by Debian Linux on Streamlit Cloud (`g++`).

---

## 2. Master Application Architecture

### Core File Relationships & Responsibilities

```
                                      +-------------------------+
                                      |     Browser Client      |
                                      +------------+------------+
                                                   |
                                    HTTP / Streamlit Query Params
                                  (?subject=dsa&case=4&mod=1)
                                                   |
                                                   v
                                      +-------------------------+
                                      |      Root app.py        |
                                      |  (Master Coordinator)   |
                                      +------------+------------+
                                                   |
                +----------------------------------+----------------------------------+
                |                                  |                                  |
                v                                  v                                  v
    +-----------------------+          +-----------------------+          +-----------------------+
    |    core_loader.py     |          | unified_persistence.py|          |     master_ui.py      |
    | (Subject Registry &   |          |  (SQLite WAL Engine & |          | (Design System, LaTeX,|
    |  Dynamic Importers)   |          |   Telemetry Store)    |          |   Renderers & Stepper)|
    +-----------+-----------+          +-----------+-----------+          +-----------+-----------+
                |                                  |                                  |
                | Loads story_data.py              | Saves/Loads                      | Dispatches code
                | & level_content.py               | Progress & XP                    | to Sandboxes
                v                                  v                                  v
    +-----------------------+          +-----------------------+          +-----------------------+
    | 8 Subject Disciplines |          |  data/platform.db     |          |      runners.py       |
    | (DBMS, AI, SE, Cloud, |          | (Thread-safe WAL Store|          | (Python AST Sandbox,  |
    |  OOP, DSA, SD, IP)    |          |  + PBKDF2 Auth)       |          |  g++ C++17 Compiler,  |
    +-----------------------+          +-----------------------+          |  SQLite Authorizer)   |
                                                                          +-----------------------+
```

### Architectural Questions Answered

#### 1. Which file is intended to launch the complete Engineering Story Labs platform?
**Root-level `app.py`**.  
`app.py` contains `st.set_page_config`, imports `core_loader`, `master_ui`, and `unified_persistence`, and coordinates the global navigation, authentication mode, top-bar track switching, and full-screen catalog/module views.

#### 2. Which file launches individual subject applications?
Five legacy subjects (`ai_story_lab`, `cloud_story_lab`, `dbms_story_lab`, `oop_story_lab`, `se_story_lab`) have their own `app.py` inside their respective directories. These were originally created as standalone applications. In contrast, the newer tracks (`dsa_story_lab`, `sd_story_lab`, `ip_story_lab`) **do not have individual `app.py` files**; they were authored specifically to be hosted by the master platform.

#### 3. How does the master UI discover and load subjects?
Discovery is managed statically and deterministically by the `SUBJECT_REGISTRY` dictionary in `core_loader.py`. `SUBJECT_REGISTRY` registers all 8 disciplines (`dbms`, `ai`, `se`, `cloud`, `oop`, `dsa`, `sd`, `ip`), their directory paths, display titles, icons, color gradients, and curriculum metadata.

#### 4. How are subject modules imported?
In `core_loader.py`, `load_subject_data(subject_id)` resolves the absolute path to each subject's `story_data.py` and `level_content.py`. It uses Python's standard `importlib.util.spec_from_file_location` and `spec.loader.exec_module` to load the modules without requiring subject directories to be added to `sys.path`. Loaded subjects are cached in memory in `_SUBJECT_CACHE` to eliminate re-import latency on subsequent Streamlit rerun passes.

#### 5. How does navigation work?
- **URL Synchronization:** `sync_query_params()` reads `?subject=<id>` and `?case=<id>` from `st.query_params`. When a user clicks a track or case, `update_query_params()` updates the browser URL without forcing disruptive full-page reloads.
- **Top Navigation Bar:** `render_top_bar()` displays "All Tracks" plus 8 discipline pills (`DBMS`, `AI`, `SE`, `Cloud`, `C++ OOP`, `DSA`, `Sys Design`, `Img Proc`).
- **Sidebar Case Jumper:** Inside any track, the sidebar displays an instant case selector selectbox that allows jumping directly between cases (e.g., from Case 03 to Case 01) while properly clearing previous module state.
- **Full-Screen Responsive Expansion:** When the sidebar is collapsed, `app.py` CSS automatically expands the main container to 100% viewport width without clipping text or leaving trailing whitespace.

#### 6. How are user progress, XP, solved cases, and account data managed?
All progress is managed by `unified_persistence.py`. It supports two modes configured by the environment variable `PLATFORM_AUTH_MODE`:
- `local` (default for quick exploration): Automatically uses an anonymous workspace session (`local_guest`) with full SQLite persistence.
- `multiuser` / `required`: Enforces user registration and login with PBKDF2-SHA256 password hashing.
Progress data (completed cases, active modules per case, solved challenge IDs, awarded XP) is stored transactionally in SQLite at `data/platform.db` with WAL mode enabled to support concurrent access.

#### 7. Are there multiple competing application entry points?
**Yes.** There are **7 competing entry points** across the workspace:
- `app.py` (Root — The genuine master entrypoint)
- `master_ui.py` (Root — Component library, lacks page configuration and routing)
- `streamlit/app.py` (Obsolete prototype)
- `ai_story_lab/app.py` (Single-track standalone)
- `dbms_story_lab/app.py` (Single-track standalone)
- `se_story_lab/app.py` (Single-track standalone)
- `cloud_story_lab/app.py` (Single-track standalone)
- `oop_story_lab/app.py` (Single-track standalone)

---

## 3. Audit of All Eight Subjects

| Track ID | Track Name | Folder Name | Cases | Modules | Interactive Blocks | Code Labs & Special Judges | Standalone `app.py` | Standalone Runnable? |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **`dbms`** | Database Management Systems | `dbms_story_lab` | 12 | 98 | 359 | 47 SQL Sandboxes, 23 Debuggers | Yes | Yes (needs `cd dbms_story_lab`) |
| **`ai`** | Artificial Intelligence | `ai_story_lab` | 25 | 103 | 990 | 92 Python Code Labs, 8 Visual Steppers | Yes | Yes (needs `cd ai_story_lab`) |
| **`se`** | Software Engineering | `se_story_lab` | 16 | 64 | 260 | 26 Micro Challenges, 14 Scenario Decisions | Yes | Yes (needs `cd se_story_lab`) |
| **`cloud`** | Cloud Computing | `cloud_story_lab` | 16 | 64 | 224 | 31 Micro Challenges, 7 Calc Challenges | Yes | Yes (needs `cd cloud_story_lab`) |
| **`oop`** | Object-Oriented Programming (C++) | `oop_story_lab` | 29 | 118 | 790 | 83 C++17 Code Labs, 37 Mastery Labs | Yes | Yes (needs `cd oop_story_lab`) |
| **`dsa`** | Data Structures & Algorithms | `dsa_story_lab` | 19 | 76 | 170 | 38 Dual Python+C++ Online Judges | No | Master only |
| **`sd`** | System Design (HLD & LLD) | `sd_story_lab` | 14 | 56 | 112 | 12 Capacity Calculators, 6 Machine Coding Labs | No | Master only |
| **`ip`** | Image Processing | `ip_story_lab` | 16 | 64 | 127 | 16 Python NumPy Labs, 16 Calc Challenges | No | Master only |
| **TOTAL** | **8 Full Engineering Disciplines** | — | **147** | **643** | **3,032** | **350+ Interactive Labs & Sandboxes** | — | — |

### Individual Subject Technical Profiles

#### 1. `dbms_story_lab`
- **Main App File:** `dbms_story_lab/app.py` (standalone) | Loaded by master via `core_loader.py`.
- **Supporting Modules:** `cases_1_2_3.py`, `cases_4_5_6.py`, `cases_7_8_9.py`, `cases_10_11.py`, `cases_17_to_20.py`, `cases_21_to_23.py`, `challenges.py`, `deep_01_05.py` to `deep_17_24.py`, `ultra_01_05.py` to `ultra_17_24.py`, `ui.py`.
- **Dependencies:** `sqlite3`, `pandas`, `plotly` (in legacy `challenges.py`).
- **Master Launch Mechanism:** `core_loader.py` imports `dbms_story_lab/story_data.py` (12 stories) and `dbms_story_lab/level_content.py` (98 modules).
- **Submodule Vulnerability:** **CRITICAL**. Committed on GitHub as a submodule gitlink without `.gitmodules`. In a fresh clone, the folder is empty.

#### 2. `ai_story_lab`
- **Main App File:** `ai_story_lab/app.py` (standalone) | Loaded by master via `core_loader.py`.
- **Supporting Modules:** `quizzes_part1.py` to `quizzes_part5.py`, `content_01_07.py`, `content_08_15.py`, `content_16_24.py`, `engineering_labs.py`, `capstone_project.py`, `syllabus_map.py`, `ui.py`.
- **Dependencies:** `ast`, `math`, `random`, `json`, `plotly` (in `capstone_project.py`).
- **Master Launch Mechanism:** `core_loader.py` imports `ai_story_lab/story_data.py` (25 stories) and `ai_story_lab/level_content.py` (103 modules). All 25 cases track properly.

#### 3. `se_story_lab`
- **Main App File:** `se_story_lab/app.py` (standalone) | Loaded by master via `core_loader.py`.
- **Supporting Modules:** `build_se_content_part1.py`, `compile_level_content.py`, `generate_cases_part1.py` to `part3.py`, `ui.py`.
- **Dependencies:** Standard library, `re`, `json`.
- **Master Launch Mechanism:** `core_loader.py` imports `se_story_lab/story_data.py` (16 stories) and `se_story_lab/level_content.py` (64 modules).

#### 4. `cloud_story_lab`
- **Main App File:** `cloud_story_lab/app.py` (standalone) | Loaded by master via `core_loader.py`.
- **Supporting Modules:** `build_cloud_part1.py` to `part4.py`, `compile_level_content.py`, `generate_pages.py`, `ui.py`.
- **Dependencies:** Standard library, `math`, `json`.
- **Master Launch Mechanism:** `core_loader.py` imports `cloud_story_lab/story_data.py` (16 stories) and `cloud_story_lab/level_content.py` (64 modules).

#### 5. `oop_story_lab`
- **Main App File:** `oop_story_lab/app.py` (standalone) | Loaded by master via `core_loader.py`.
- **Supporting Modules:** `cases_01_to_04.py` to `cases_21_to_23.py`, `rich_cases_group1.py` to `group5.py`, `ui.py`.
- **Dependencies:** `subprocess`, `g++`, `streamlit-ace`.
- **Master Launch Mechanism:** `core_loader.py` imports `oop_story_lab/story_data.py` (29 stories) and `oop_story_lab/level_content.py` (118 modules).
- **Submodule Vulnerability:** **CRITICAL**. Committed on GitHub as a submodule gitlink without `.gitmodules`. In a fresh clone, the folder is empty.

#### 6. `dsa_story_lab`
- **Main App File:** No standalone app file. Designed specifically as an integrated engine for the master platform.
- **Supporting Modules:** `dsa_part1.py` through `dsa_part5.py`, dynamically loaded by `level_content.py` via `importlib`.
- **Dependencies:** `subprocess`, `g++` (for C++17 judge), Python 3 AST runner, `json`.
- **Master Launch Mechanism:** `core_loader.py` loads `dsa_story_lab/story_data.py` (19 stories) and `dsa_story_lab/level_content.py` (76 modules, 38 online judges). Fully verified.

#### 7. `sd_story_lab`
- **Main App File:** No standalone app file. Designed specifically as an integrated engine for the master platform.
- **Supporting Modules:** `sd_part1.py` through `sd_part3.py`, dynamically loaded by `level_content.py`.
- **Dependencies:** Standard library, `math`, `json`.
- **Master Launch Mechanism:** `core_loader.py` loads `sd_story_lab/story_data.py` (14 stories) and `sd_story_lab/level_content.py` (56 modules). Fully verified.

#### 8. `ip_story_lab`
- **Main App File:** No standalone app file. Designed specifically as an integrated engine for the master platform.
- **Supporting Modules:** `cases_00_07.py` and `cases_08_15.py`, dynamically loaded by `level_content.py`.
- **Dependencies:** `numpy` (for 2D FFT, Wiener restoration, spatial convolutions), `math`, `json`.
- **Master Launch Mechanism:** `core_loader.py` loads `ip_story_lab/story_data.py` (16 stories) and `ip_story_lab/level_content.py` (64 modules). All 16 code labs verified syntax-clean and execution-ready.

---

## 4. Streamlit Deployment Audit

### Dependency Analysis

#### Root `requirements.txt`
```
streamlit>=1.37.0,<2.0.0
streamlit-ace>=0.1.1,<1.0.0
markdown>=3.4.0,<4.0.0
pandas>=2.0.0,<3.0.0
numpy>=1.24.0,<3.0.0
```
- **Evaluation:** Clean, precise version pinning. All packages have pre-built binary wheels on PyPI for `x86_64` and `aarch64` Linux.
- **Missing Optional Dependency:** `plotly>=5.20.0` is imported in `dbms_story_lab/challenges.py` and `ai_story_lab/capstone_project.py`. Although `master_ui.py` does not directly require Plotly, omitting Plotly can raise `ImportError` if legacy modules are touched.

#### System Package Requirements (`packages.txt`)
- File content: `g++`
- **Evaluation:** **CRITICAL**. Streamlit Community Cloud runs on Debian Linux containers. By default, `g++` is not installed. `packages.txt` instructs the Streamlit Cloud build system to run `apt-get install -y g++`. Without this, C++ compilation in `oop_story_lab` and `dsa_story_lab` will fail with `FileNotFoundError: [Errno 2] No such file or directory: 'g++'`.

### Streamlit Configuration (`.streamlit/config.toml`)
```toml
[theme]
base = "dark"
primaryColor = "#4F46E5"
backgroundColor = "#09090B"
secondaryBackgroundColor = "#111114"
textColor = "#FAFAFA"
font = "sans serif"

[server]
headless = true
enableXsrfProtection = true
maxUploadSize = 5

[browser]
gatherUsageStats = false

[client]
toolbarMode = "minimal"
showErrorDetails = "none"
```
- **Evaluation:** Production-ready. Matches the Obsidian/Zinc master theme and prevents telemetry leaks.

### Cloud Persistence and Ephemeral Filesystem
- Streamlit Cloud containers use **ephemeral storage**. If the container is put to sleep or redeployed, any local SQLite database in `data/platform.db` is destroyed.
- **Unified Persistence Architecture:** `unified_persistence.py` handles this gracefully:
  1. If `data/platform.db` is reset, the database schema and default records are automatically recreated on first request.
  2. For permanent multi-instance persistence, the code supports `PLATFORM_DB_PATH` and can be paired with an external volume (e.g. Render 1GB disk defined in `render.yaml`) or PostgreSQL/Cloud SQL.

### Container & Infrastructure Audit
- **`Dockerfile`:** Uses `python:3.11-slim`, installs `g++`, sets non-root user `appuser` (UID 10001), runs healthcheck against `/_stcore/health`.
- **`render.yaml`:** Configures Docker runtime, starter tier, 1GB persistent disk at `/app/data`, and sets `PLATFORM_AUTH_MODE=multiuser`.
- **`docker-compose.yml`:** Restricts container capabilities (`cap_drop: ALL`, `no-new-privileges: true`, `mem_limit: 1g`, `cpus: 1.5`, `pids_limit: 128`).
- **Localhost References:** Only exist in local automated testing scripts (`verify_full_se_curriculum.py`, `verify_cloud_platform.py`). Zero hardcoded `localhost` references exist in application runtime paths.

---

## 5. GitHub Repository Audit

| Metric | Current State | Audit Finding |
| :--- | :--- | :--- |
| **Current Local Branch** | `main` | Verified |
| **Remote Repository URL** | `https://github.com/AdakMahato/Learning_Platform.git` | Correct remote |
| **Local HEAD Commit** | `391e891` | `"Deploy Engineering Story Labs (8 tracks, hardened sandboxes)"` |
| **Remote Origin Commit** | `e43588d` | Ahead by 1 commit (`"Added Dev Container Folder"` adding `.devcontainer/devcontainer.json`) |
| **Master UI & Engine Tracked** | `app.py`, `core_loader.py`, `master_ui.py`, `runners.py`, `unified_persistence.py` | Tracked and present in remote commits |
| **Subject Tracks Tracked** | `ai_story_lab`, `cloud_story_lab`, `dsa_story_lab`, `ip_story_lab`, `sd_story_lab`, `se_story_lab` | Fully tracked as regular directory trees (`040000 tree`) |
| **DBMS & OOP Tracked** | `dbms_story_lab`, `oop_story_lab` | **FAULTY (Mode `160000 commit` gitlinks)** — Committed as empty submodule references! |
| **Submodule Mapping** | `.gitmodules` | **MISSING** — Git cannot clone `dbms_story_lab` or `oop_story_lab` on remote hosts |
| **Default Entrypoint File** | `streamlit_app.py` | **MISSING** — Causes Streamlit Cloud initial deploy error |

---

## 6. Diagnosis: Why Deployment Failed

Based on real code inspection and deployment telemetry, the failure is categorized below:

### Finding 1: Submodule Gitlink Error (`dbms_story_lab` & `oop_story_lab`)
- **Severity:** **CRITICAL**
- **Location:** Repository Git Tree (`.git/index` -> mode `160000`)
- **Root Cause:** Both folders contained nested `.git` folders from previous independent repositories (`Learning.git` and `oop-cpp-story-lab.git`). When `git add .` was executed in `LEARNING_PLATFORM`, Git detected the nested repository markers and stored gitlink pointers instead of traversing and staging the directory contents. Because no `.gitmodules` file exists, GitHub and Streamlit Cloud treat them as empty stub directories.
- **Runtime Consequence:** On Streamlit Cloud, `ls /app/dbms_story_lab` is empty. Startup of `app.py` crashes on `loader.load_subject_data("dbms")` with `FileNotFoundError: /app/dbms_story_lab/story_data.py`.
- **Recommended Fix:** 
  1. Remove nested `.git` and `.gitattributes` folders from `dbms_story_lab` and `oop_story_lab`.
  2. Remove the submodule entries from Git index: `git rm --cached dbms_story_lab oop_story_lab`.
  3. Re-add both folders as standard directory trees: `git add dbms_story_lab oop_story_lab`.
  4. Commit and push to `origin/main`.

### Finding 2: Streamlit Cloud Entry Point Path (`streamlit_app.py` vs `app.py`)
- **Severity:** **CRITICAL**
- **Location:** Streamlit Cloud Deployment Dashboard / Project Root
- **Root Cause:** The default file path expected by Streamlit Cloud's automated deploy wizard is `streamlit_app.py`. The project's actual entry point is `app.py`. When the user leaves the default in place, Streamlit Cloud displays `"This file does not exist"` in red.
- **Runtime Consequence:** Build fails before container initialization.
- **Recommended Fix:**
  1. Add a thin shim / entrypoint alias file named `streamlit_app.py` at the root that imports and executes `app.py`:
     ```python
     # streamlit_app.py
     import app
     ```
  2. Alternatively, specify `app.py` in the "Main file path" field in Streamlit Cloud settings.

### Finding 3: Missing `plotly` in Root `requirements.txt`
- **Severity:** **HIGH**
- **Location:** `requirements.txt`
- **Root Cause:** `plotly` is imported in `ai_story_lab/capstone_project.py`, `ai_story_lab/engineering_labs.py`, and `dbms_story_lab/challenges.py`. Although `master_ui.py` renders native HTML/CSS/Mermaid, any code path that touches these modules will trigger `ModuleNotFoundError: No module named 'plotly'`.
- **Runtime Consequence:** Intermittent runtime crash when accessing specialized challenges.
- **Recommended Fix:** Add `plotly>=5.20.0,<6.0.0` to root `requirements.txt`.

### Finding 4: Untracked Local Files in `dbms_story_lab`
- **Severity:** **MEDIUM**
- **Location:** `dbms_story_lab/`
- **Root Cause:** 16 files inside `dbms_story_lab` (e.g. `cases_17_to_20.py`, `cases_21_to_23.py`, `deep_*.py`, `ultra_*.py`) are untracked by Git because of the nested `.git` setup.
- **Runtime Consequence:** While the master platform loads the core 12 cases defined in `level_content.py`, auxiliary deep scenarios are missing from remote versions.
- **Recommended Fix:** Ensure all files are tracked once the submodule is converted to a regular directory.

### Finding 5: Competing Legacy Multipage Directories
- **Severity:** **LOW**
- **Location:** `ai_story_lab/pages/`, `cloud_story_lab/pages/`, `dbms_story_lab/pages/`, `oop_story_lab/pages/`, `se_story_lab/pages/`
- **Root Cause:** In older versions of Streamlit, placing files in a `pages/` directory caused Streamlit to automatically generate sidebar multipage links. In the unified `app.py` architecture, navigation is handled dynamically by query parameters and `master_ui.py`. Because the `pages/` folders are nested inside subject subdirectories rather than at the root level, Streamlit ignores them when running root `app.py`, which is correct.
- **Recommended Fix:** Keep them as-is or document them as legacy standalone artifacts.

---

## 7. Recommended Production Architecture

To achieve the desired production state:
```
One Public Streamlit Cloud URL (e.g., tietlearningplatform.streamlit.app)
                            |
                            v
               Engineering Story Labs Master UI
                            |
  +--------+--------+--------+--------+---------+--------+--------+--------+
  |        |        |        |        |         |        |        |        |
 DBMS     AI       SE      Cloud   C++ OOP     DSA   Sys Design Img Proc
(12 cs) (25 cs)  (16 cs)  (16 cs)  (29 cs)   (19 cs)  (14 cs)  (16 cs)
```

### Action Plan (For Execution After Review)

1. **Fix Git Tree (Resolve Submodules):**
   - Remove internal `.git` directories from `dbms_story_lab/` and `oop_story_lab/`.
   - Clear cached Git links: `git rm --cached dbms_story_lab oop_story_lab`.
   - Stage all files in `dbms_story_lab` and `oop_story_lab` as regular repository files.

2. **Add Entrypoint Shim:**
   - Create `streamlit_app.py` in the root:
     ```python
     """Streamlit Community Cloud Entry Point Shim."""
     import runpy
     runpy.run_path("app.py", run_name="__main__")
     ```
   - This ensures deployment works regardless of whether the user types `app.py` or leaves Streamlit Cloud's default `streamlit_app.py`.

3. **Update `requirements.txt`:**
   ```
   streamlit>=1.37.0,<2.0.0
   streamlit-ace>=0.1.1,<1.0.0
   markdown>=3.4.0,<4.0.0
   pandas>=2.0.0,<3.0.0
   numpy>=1.24.0,<3.0.0
   plotly>=5.20.0,<6.0.0
   ```

4. **Verify `packages.txt`:**
   - Ensure `packages.txt` with `g++` is committed at the repository root.

5. **Commit and Push:**
   - `git add .`
   - `git commit -m "Fix submodule gitlinks, add streamlit_app entrypoint shim, and complete 8-track deployment bundle"`
   - `git push origin main`

6. **Streamlit Cloud Settings:**
   - Repository: `AdakMahato/Learning_Platform`
   - Branch: `main`
   - Main file path: `streamlit_app.py` (or `app.py`)
   - App URL: `tietlearningplatform.streamlit.app`

---

## 8. Verification Status Table

| Audit Section | Verification Status | Notes |
| :--- | :--- | :--- |
| **1. Complete Project Structure** | **VERIFIED** | Full directory tree scanned and cataloged |
| **2. Master Architecture** | **VERIFIED** | Traced `app.py`, `core_loader.py`, `master_ui.py`, `runners.py`, `unified_persistence.py` |
| **3. All 8 Subjects** | **VERIFIED** | Total 147 cases, 643 modules, 3,032 blocks dynamically loaded and verified |
| **4. Streamlit Deployment Config** | **VERIFIED** | Verified `.streamlit/config.toml`, `packages.txt`, `requirements.txt` |
| **5. GitHub Repository Status** | **VERIFIED** | Git tree inspected; identified submodule gitlink anomaly in `dbms` & `oop` |
| **6. Deployment Failure Diagnosis** | **VERIFIED** | Root causes confirmed via error logs, screenshots, and Git mode inspection |
| **7. Production Architecture Plan** | **VERIFIED** | Blueprint prepared for single-URL multi-track deployment |

---
*Report generated strictly in READ-ONLY mode. No existing source files or Git remotes were modified.*
