# Phase 3 Inspection Report: Dependencies, Compiler & Entry Point
**Platform:** Learning_Platform (Engineering Story Labs)  
**Date:** November 13, 2026  
**Auditor:** Antigravity DeepMind Agentic Pair Programmer  
**Inspection Scope:** Read-Only Verification of Root & Nested Dependencies, Compiler Invocations, Master Entry Point, and Cloud Compatibility  
**Status:** INSPECTION COMPLETE (Strictly Non-Destructive • Ready for Review)

---

## 1. Dependency Audit

### 1.1 Existing Root `requirements.txt`
```
streamlit>=1.37.0,<2.0.0
streamlit-ace>=0.1.1,<1.0.0
markdown>=3.4.0,<4.0.0
pandas>=2.0.0,<3.0.0
numpy>=1.24.0,<3.0.0
```

### 1.2 Full AST Import Inventory Across All 8 Tracks & Master Files

#### A. Master Architecture Files
* **`app.py`:**
  * *Standard Library:* `html`, `logging`, `typing`
  * *Third-Party:* `streamlit`
  * *Internal Modules:* `core_loader`, `master_ui`, `unified_persistence`
* **`core_loader.py`:**
  * *Standard Library:* `importlib`, `os`, `sys`, `typing`
  * *Third-Party:* None (0 external packages)
* **`master_ui.py`:**
  * *Standard Library:* `functools`, `html`, `re`, `time`, `typing`
  * *Third-Party:* `streamlit`, `streamlit-ace`, `markdown`, `pandas`
  * *Internal Modules:* `runners`, `unified_persistence`, `core_loader`
* **`runners.py`:**
  * *Standard Library:* `ast`, `json`, `os`, `platform`, `re`, `resource`, `signal`, `sqlite3`, `subprocess`, `sys`, `tempfile`, `threading`, `time`, `typing`
  * *Third-Party:* `pandas` (used for tabular SQL result framing)
* **`unified_persistence.py`:**
  * *Standard Library:* `copy`, `datetime`, `hashlib`, `hmac`, `json`, `os`, `re`, `secrets`, `sqlite3`, `threading`, `time`, `typing`
  * *Third-Party:* `streamlit` (for `st.session_state`)

#### B. Subject Curriculum Data Modules (`story_data.py` & `level_content.py`)
All 8 subject data modules (`dbms_story_lab`, `ai_story_lab`, `se_story_lab`, `cloud_story_lab`, `oop_story_lab`, `dsa_story_lab`, `sd_story_lab`, `ip_story_lab`) are pure Python data structures. They import **zero third-party packages** at module level; they only use standard library `importlib` and `os` to stitch modular part files.

#### C. Interactive Code Labs (Student Code Execution in Sandboxes)
A full AST regex scan was conducted across all 350+ interactive code labs, solution codes, and automated test suites:
* **DBMS (`dbms_story_lab`):** Live SQL sandboxes run against Python's built-in `sqlite3` using memory-mapped or temp databases with custom query authorizers.
* **DSA (`dsa_story_lab`):** Online judges run dual Python 3 and C++17. Python solutions use standard library: `collections`, `heapq`, `bisect`, `math`, `sys`.
* **Image Processing (`ip_story_lab`):** 16 code labs import `numpy` (for 2D FFT, Fourier transforms, Wiener degradation models, spatial convolution matrices). `numpy` is already pinned in root `requirements.txt`.
* **C++ OOP (`oop_story_lab`):** Compiles via `g++ -O1 -std=c++17`. Uses C++ standard headers (`<iostream>`, `<vector>`, `<string>`, `<memory>`, `<map>`, `<iomanip>`).
* **Artificial Intelligence (`ai_story_lab`):**
  * Case 12 (Probability & Uncertainty): `import scipy.stats as stats`
  * Case 17 (K-Nearest Neighbors): `from sklearn.neighbors import KNeighborsClassifier`, `from sklearn.preprocessing import StandardScaler`
  * Case 18 (Naive Bayes): `from sklearn.naive_bayes import GaussianNB, MultinomialNB`
  * Case 19 (Decision Trees): `from sklearn.tree import DecisionTreeClassifier`
  * Case 24 (Ensemble & Final AI): `from sklearn.ensemble import RandomForestClassifier`, `from sklearn.svm import SVC`, `from sklearn.neural_network import MLPClassifier`

### 1.3 Verification of Plotly
* **Audit Finding:** `plotly` is **NOT** imported anywhere in the master application (`app.py`, `core_loader.py`, `master_ui.py`, `runners.py`, `unified_persistence.py`), nor in `level_content.py` or `story_data.py` across any of the 8 disciplines.
* **Where Plotly Actually Exists:** Plotly is only referenced in legacy standalone files:
  * `dbms_story_lab/challenges.py` (legacy standalone challenge runner)
  * `ai_story_lab/capstone_project.py` (legacy standalone multi-agent prototype)
  * `ai_story_lab/engineering_labs.py` (legacy standalone script)
  * `dbms_story_lab/ui.py` (legacy standalone UI)
* **Conclusion on Plotly:** The unified master platform does **not** require Plotly to run all 147 cases and 643 modules. However, adding `plotly>=5.20.0,<6.0.0` is harmless and ensures backward compatibility if legacy standalone scripts are ever invoked directly.

### 1.4 Missing Third-Party Dependencies
To ensure all 147 cases—including the machine learning algorithms in `ai_story_lab`—execute in their sandboxes without `ModuleNotFoundError`, the following two packages should be added:
* `scipy>=1.11.0,<2.0.0` (for AI Case 12 statistical distributions)
* `scikit-learn>=1.3.0,<2.0.0` (for AI Cases 17, 18, 19, 24 classifiers)

### 1.5 Version Conflict Assessment
* `streamlit 1.37.0` to `1.40.x`
* `pandas 2.x`
* `numpy 1.24.x` to `1.26.x` / `2.x`
* `scipy 1.11+`
* `scikit-learn 1.3+`
* `markdown 3.4+`
* `streamlit-ace 0.1.1`
* **Conflict Result:** ZERO conflicts. All packages have compatible, co-installable binary wheels on Linux (x86_64 / aarch64) and macOS.

---

## 2. Compiler Audit (`packages.txt` & `g++`)

### 2.1 Existing `packages.txt`
```
g++
```
* **Content:** Exactly 4 bytes (`g++\n`).

### 2.2 Verification of C++ Compiler Invocations
In `runners.py`:
* Line 278 (`run_cpp`):
  ```python
  ["g++", "-std=c++17", "-O1", cpp_file, "-o", exe_file]
  ```
* Line 846 (`run_dsa_judge`):
  ```python
  ["g++", "-std=c++17", "-O1", cpp_file, "-o", exe_file]
  ```
* **Execution Environment:** In Debian-based Linux containers on Streamlit Cloud, `packages.txt` triggers `apt-get update && apt-get install -y g++`.
* **Adequacy:** `g++` on Debian installs the complete GNU C++ compiler suite, standard libraries (`libstdc++-dev`), header files, and assembler tools.
* **Other System Packages:**
  * *Graphviz:* **Not required.** `master_ui.py` renders Mermaid architecture diagrams via an isolated HTML/JS iframe using `https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js`. The Graphviz system package is not needed.
* **Conclusion:** `packages.txt` with `g++` is optimal and minimal. No changes or additions needed.

---

## 3. Master Entry Point Audit (`app.py` vs. `streamlit_app.py`)

### 3.1 Trace of `app.py` Execution Flow
1. **Configuration:** Sets `st.set_page_config(page_title="Engineering Story Labs", page_icon="</>", layout="wide", initial_sidebar_state="expanded")`.
2. **URL Parameter Sync (`sync_query_params`):** Reads and sanitizes `st.query_params`:
   * `?subject=home` or any registered subject ID (`dbms`, `ai`, `se`, `cloud`, `oop`, `dsa`, `sd`, `ip`).
   * `?case=<id>` jumps directly to a specific case.
3. **Workspace State:** Initializes user session and loads progress from `unified_persistence.py`.
4. **Top Navigation Bar (`render_top_bar`):** Renders "All Tracks" button + 8 discipline navigation buttons.
5. **View Delegation:**
   * If `nav_subject == "home"`: Renders master curriculum overview with track metrics (147 cases, 643 modules, 3,032 blocks) and case cards.
   * If `nav_subject` is an active track: Renders track header, sidebar case jumper, module navigation, and delegates interactive block rendering to `master_ui.render_block()`.

### 3.2 Can Streamlit Cloud Launch `app.py` Directly?
**YES.**
* Streamlit Community Cloud features an explicit configuration setting: **"Main file path"**.
* By setting **Main file path = `app.py`**, Streamlit Cloud executes `streamlit run app.py` natively.
* The previous red error `"This file does not exist"` occurred only because the input field was left at its default value (`streamlit_app.py`) while GitHub only had commit `768a00d` without any application files.

### 3.3 Is `streamlit_app.py` Technically Necessary?
* **Technically Required?** No, as long as the user sets "Main file path" to `app.py` in the Streamlit Cloud dashboard.
* **Recommended as a Zero-Config Shim?** **YES.** Creating a 6-line `streamlit_app.py` that delegates to `app.py`:
  ```python
  """Streamlit Community Cloud Entry Point Shim."""
  import runpy

  if __name__ == "__main__":
      runpy.run_path("app.py", run_name="__main__")
  ```
  This eliminates any risk of deployment failure if Streamlit Cloud resets the entry point or if a team member deploys using default settings.

### 3.4 Local Absolute Paths or Machine Assumptions
* **Scan Results:** Zero hardcoded `/Users/` or macOS-specific paths exist in `app.py`, `core_loader.py`, `master_ui.py`, `runners.py`, or `unified_persistence.py`.
* **Path Resolution:** All directories are resolved relative to `__file__`:
  ```python
  BASE_DIR = os.path.dirname(os.path.abspath(__file__))
  ```
* **Python Binary:** Dynamically resolved from `sys.executable`.
* **Resource Limits:** `runners.py` safely checks `platform.system() == "Linux"` before attempting Linux-specific kernel resource limits (`RLIMIT_AS`), ensuring seamless portability across macOS and Linux.

---

## 4. Deployment Compatibility Assessment

| Dimension | Native Streamlit Cloud | Docker / Render Container | Audit Finding |
| :--- | :--- | :--- | :--- |
| **System Compiler** | Supported via `packages.txt` | Supported via `apt-get install g++` in `Dockerfile` | `g++` handles all C++ labs |
| **Data Directory** | Auto-created at runtime by `_ensure_data_dir()` | Mounted via volume `./data:/app/data` | Works out of the box in both |
| **Persistence Mode** | Ephemeral SQLite WAL (session/guest) | Persistent disk mounted at `/app/data` | Local guest sessions work without configuration |
| **Docker Requirement** | **NOT REQUIRED** | Optional alternative | App runs 100% natively on Streamlit Cloud |

---

## 5. Consolidated Recommendations

### Proposed Dependency File (`requirements.txt`)
```
streamlit>=1.37.0,<2.0.0
streamlit-ace>=0.1.1,<1.0.0
markdown>=3.4.0,<4.0.0
pandas>=2.0.0,<3.0.0
numpy>=1.24.0,<3.0.0
scipy>=1.11.0,<2.0.0
scikit-learn>=1.3.0,<2.0.0
plotly>=5.20.0,<6.0.0
```
* **Preserves:** All 5 existing dependencies.
* **Adds:** `scipy` and `scikit-learn` (for AI track code labs), plus `plotly` (as legacy safeguard).

### Proposed System Package File (`packages.txt`)
```
g++
```
* **Status:** Already present and verified. No changes needed.

### Proposed Entry Point Strategy
* Primary: Deploy pointing to `app.py`.
* Secondary: Include `streamlit_app.py` shim for foolproof zero-config deployment.

---

*Phase 3 inspection complete. Zero modifications were applied to workspace code or Git objects.*
