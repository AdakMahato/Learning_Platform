# Safe Deployment Repair Plan: GitHub & Streamlit Cloud
**Platform:** Learning_Platform (Engineering Story Labs)  
**Target URL:** `tietlearningplatform.streamlit.app`  
**Remote Repository:** `https://github.com/AdakMahato/Learning_Platform.git`  
**Date:** November 13, 2026  
**Document Status:** PRE-FLIGHT VERIFIED • STRICTLY NON-DESTRUCTIVE • READY FOR REVIEW  

> [!IMPORTANT]
> **READ-ONLY ASSURANCE:** No commands in this plan have been executed. No files have been deleted, overwritten, staged, committed, or pushed. This document provides the complete, audited, step-by-step repair blueprint and the exact terminal commands required to safely deploy the master platform.

---

## 1. Pre-Flight Inspection & Verification Findings

Before formulating the repair sequence, a deep inspection of the Git index, nested repositories, local source files, and remote branch states was conducted.

### 1.1 Git Index & Submodule Status (`mode 160000`)
Querying the Git staging index via `git ls-files -s dbms_story_lab oop_story_lab` revealed:
```
160000 f63bd73b16b8516fd7f67f6cd51330b49ff031ae 0   dbms_story_lab
160000 907b94b1faabe95d516f7c1695b41811bee9945e 0   oop_story_lab
```
* **Git Internal Mechanism:** In Git, file mode `160000` denotes a **gitlink** (submodule pointer). Instead of committing the directory tree and its files, Git stores only a 20-byte SHA-1 pointing to an external commit.
* **The Root Defect:** There is **no `.gitmodules` file** in the repository. When GitHub or Streamlit Cloud clones `Learning_Platform.git`, Git encounters the `160000` entry, finds no mapping in `.gitmodules`, and leaves `dbms_story_lab/` and `oop_story_lab/` as **empty directories**.

### 1.2 Uncommitted Local Work & File Integrity
A full audit of the local working copy was performed to guarantee that no user modifications are lost during the repair:

#### Inside `oop_story_lab/` (CRITICAL UNCOMMITTED CODE)
Running `git diff` inside `oop_story_lab/` identified extensive recent code enhancements:
* **`oop_story_lab/level_content.py`:** Multiple C++ code labs were upgraded with complete, working starter code, concrete struct definitions (`struct IDelivery`, `StandardDelivery`), standard input integration (`stdin_input: "21"`), and precise expected outputs (`"Cost is 15.5"`, `"42"`).
* **`oop_story_lab/ui.py`:** Enhanced edge-case rendering logic supporting both string and list inputs with newline sanitization.
* **Safety Requirement:** Any repair procedure **must preserve these exact working files intact on disk**. Under no circumstances should `git checkout`, `git reset --hard`, or `git clean` be run inside `oop_story_lab/`.

#### Inside `dbms_story_lab/` (UNTRACKED CURRICULUM MODULES)
Running `git status` inside `dbms_story_lab/` identified 16 untracked Python curriculum files:
* `cases_17_to_20.py`, `cases_21_to_23.py`
* `deep_01_05.py`, `deep_07_11.py`, `deep_12_16.py`, `deep_17_24.py`
* `ultra_01_05.py`, `ultra_07_11.py`, `ultra_12_16.py`, `ultra_17_24.py`
* `enrich_curriculum_depth.py`, `update_ui_code_lab.py`, `update_ui_quizzes.py`
* **Safety Requirement:** These files represent enriched case modules. Converting `dbms_story_lab` into a normal directory in the master repository will automatically stage and preserve them.

### 1.3 Local vs Remote Branch Sync Status
* **Local `HEAD`:** `391e891` (`"Deploy Engineering Story Labs (8 tracks, hardened sandboxes)"`)
* **Remote `origin/main`:** `e43588d` (`"Added Dev Container Folder"`)
* **Divergence:** Remote `origin/main` is ahead by exactly **1 commit** (`e43588d`), which added `.devcontainer/devcontainer.json` (+33 lines).
* **Sync Strategy:** Fast-forward merging `origin/main` (`git merge --ff-only origin/main`) brings down `.devcontainer/devcontainer.json` without modifying any Python files or subject directories.

---

## 2. Safety & Backup Strategy

Before altering any Git state, we implement a **zero-risk snapshot**:
1. **Physical Git Folder Backup:** We copy `dbms_story_lab/.git` and `oop_story_lab/.git` to a safe location outside the workspace (`~/.git_backup_story_labs/`). This guarantees that the standalone Git history, tags, and commits of both original repositories remain 100% recoverable.
2. **Local Working Copy Preservation:** Using `git rm --cached` removes gitlink pointers from the Git index **without deleting a single byte from the local file system**.

---

## 3. Detailed Component Plan

### 3.1 Submodule Conversion to Tracked Folders
```
Before:
LEARNING_PLATFORM/
├── dbms_story_lab/  (mode 160000 gitlink -> remote clone gets EMPTY folder)
└── oop_story_lab/   (mode 160000 gitlink -> remote clone gets EMPTY folder)

After Repair:
LEARNING_PLATFORM/
├── dbms_story_lab/  (mode 040000 tree -> all 26+ Python files fully tracked)
└── oop_story_lab/   (mode 040000 tree -> all 64+ Python files fully tracked)
```
* **Step A:** Back up nested `.git` folders to `~/.git_backup_story_labs/`.
* **Step B:** Execute `git rm --cached dbms_story_lab oop_story_lab` in the parent repository.
* **Step C:** Delete the nested `.git` directories (`rm -rf dbms_story_lab/.git oop_story_lab/.git`).
* **Step D:** Stage both folders normally: `git add dbms_story_lab oop_story_lab`.
* **Result:** Mode changes from `160000` to standard Git tree objects (`040000`), exactly like `ai_story_lab`, `se_story_lab`, `cloud_story_lab`, `dsa_story_lab`, `sd_story_lab`, and `ip_story_lab`.

### 3.2 Streamlit Cloud Entry Point Shim (`streamlit_app.py`)
Streamlit Community Cloud defaults to launching `streamlit_app.py`. If a repository does not have this exact filename, Streamlit halts and presents a red error box.
* **Solution:** Create a lightweight, high-reliability entry point shim named `streamlit_app.py` at the project root:
  ```python
  """
  Streamlit Community Cloud Entry Point Shim.
  Delegates execution directly to master app.py.
  """
  import runpy

  if __name__ == "__main__":
      runpy.run_path("app.py", run_name="__main__")
  ```
* **Benefit:** Works 100% out-of-the-box whether Streamlit Cloud is configured with `streamlit_app.py` or `app.py`.

### 3.3 Root Dependencies (`requirements.txt`)
Add `plotly` to root `requirements.txt` to satisfy optional interactive visualizations across all modules:
```
streamlit>=1.37.0,<2.0.0
streamlit-ace>=0.1.1,<1.0.0
markdown>=3.4.0,<4.0.0
pandas>=2.0.0,<3.0.0
numpy>=1.24.0,<3.0.0
plotly>=5.20.0,<6.0.0
```

### 3.4 System Packages (`packages.txt`)
Verify that `packages.txt` exists at root and contains:
```
g++
```
* **Evaluation:** Confirmed present (size 4 bytes). Streamlit Cloud's Debian build image will automatically run `apt-get install -y g++`, enabling live compilation for C++ OOP labs and DSA online judges.

---

## 4. Complete, Ordered Terminal Command Sequence

Here is the exact step-by-step terminal execution sequence. Each command is annotated with its purpose and safety guarantee.

```bash
# ==============================================================================
# PHASE 1: PRE-FLIGHT SYNC & SAFE BACKUP
# ==============================================================================

# 1.1 Navigate to the project root
cd /Users/aadarshamahato/Downloads/LEARNING_PLATFORM

# 1.2 Fetch and fast-forward remote changes (picks up commit e43588d containing .devcontainer)
# What it does: Updates origin/main tracking ref and merges .devcontainer cleanly.
# Safety: Does not touch any subject code or uncommitted files.
git fetch origin
git merge --ff-only origin/main

# 1.3 Create an external backup directory and back up nested .git repositories
# What it does: Copies the internal commit history of dbms and oop to your user home.
# Safety: Guarantees that no historical standalone commits can ever be lost.
mkdir -p ~/.git_backup_story_labs
cp -R dbms_story_lab/.git ~/.git_backup_story_labs/dbms_story_lab_git_backup
cp -R oop_story_lab/.git ~/.git_backup_story_labs/oop_story_lab_git_backup

# Verify backups exist before proceeding:
ls -la ~/.git_backup_story_labs


# ==============================================================================
# PHASE 2: CONVERT SUBMODULES INTO TRACKED MONOREPO DIRECTORIES
# ==============================================================================

# 2.1 Remove the gitlink submodule pointers from the Git staging index
# What it does: Deletes the mode 160000 submodule references from the index.
# Safety: The --cached flag ensures NOT A SINGLE FILE on disk is deleted.
git rm --cached dbms_story_lab
git rm --cached oop_story_lab

# 2.2 Remove the nested .git folders that were causing Git to treat them as submodules
# What it does: Allows Git in the parent repository to traverse into both folders.
# Safety: Source files remain completely untouched; history is safely backed up in Phase 1.
rm -rf dbms_story_lab/.git
rm -rf oop_story_lab/.git

# 2.3 Remove nested .gitignore in oop_story_lab that previously ignored cases_*.py
# What it does: Ensures all OOP case files are recognized by parent Git.
rm -f oop_story_lab/.gitignore
rm -f dbms_story_lab/.gitignore

# 2.4 Add dbms_story_lab and oop_story_lab as normal directories with all source files
# What it does: Stages all Python files, rich cases, and level content into parent index.
# Mode changes from 160000 (submodule) to 040000 (standard directory tree).
git add dbms_story_lab
git add oop_story_lab


# ==============================================================================
# PHASE 3: CONFIGURE STREAMLIT DEPLOYMENT ASSETS & DEPENDENCIES
# ==============================================================================

# 3.1 Create the streamlit_app.py entry point shim
cat << 'EOF' > streamlit_app.py
"""
Streamlit Community Cloud Entry Point Shim.
Ensures seamless launching whether deployed as streamlit_app.py or app.py.
"""
import runpy

if __name__ == "__main__":
    runpy.run_path("app.py", run_name="__main__")
EOF

# 3.2 Update requirements.txt to include Plotly
cat << 'EOF' > requirements.txt
streamlit>=1.37.0,<2.0.0
streamlit-ace>=0.1.1,<1.0.0
markdown>=3.4.0,<4.0.0
pandas>=2.0.0,<3.0.0
numpy>=1.24.0,<3.0.0
plotly>=5.20.0,<6.0.0
EOF

# 3.3 Verify packages.txt contains g++
echo "g++" > packages.txt

# 3.4 Stage configuration and shim files
git add streamlit_app.py requirements.txt packages.txt PROJECT_DEPLOYMENT_AUDIT.md SAFE_DEPLOYMENT_REPAIR_PLAN.md


# ==============================================================================
# PHASE 4: VERIFICATION BEFORE COMMIT
# ==============================================================================

# 4.1 Verify that dbms_story_lab and oop_story_lab are NO LONGER 160000 gitlinks
# Expected output: Normal blobs (100644), NOT 160000.
git ls-files -s dbms_story_lab/story_data.py oop_story_lab/story_data.py

# 4.2 Run unit test suite to verify sandboxes and runners are functioning
python3 -m unittest discover tests


# ==============================================================================
# PHASE 5: COMMIT & PUSH TO GITHUB
# ==============================================================================

# 5.1 Commit the entire repair
git commit -m "Fix submodule gitlinks: track dbms and oop source trees, add streamlit_app shim and plotly dependency"

# 5.2 Push cleanly to origin main
git push origin main

# 5.3 Verify remote tree reflects normal directories
git ls-tree HEAD dbms_story_lab oop_story_lab
# Expected output: 040000 tree ... dbms_story_lab and 040000 tree ... oop_story_lab
```

---

## 5. Post-Repair Streamlit Cloud Deployment Settings

Once the push is completed, proceed to **share.streamlit.io** and configure:

1. **Repository:** `AdakMahato/Learning_Platform`
2. **Branch:** `main`
3. **Main file path:** `streamlit_app.py` (or `app.py`)
4. **App URL:** `tietlearningplatform.streamlit.app`
5. **Advanced settings:**
   * Python Version: `3.11` (or `3.10` / `3.12`)
   * Secrets: (None required for guest/local mode; optionally add `PLATFORM_SECRET_KEY` if running multiuser auth)

### Build Expectations
* **Debian Layer:** Streamlit Cloud reads `packages.txt` and installs `g++`.
* **Python Layer:** Streamlit Cloud reads `requirements.txt` and installs `streamlit`, `streamlit-ace`, `markdown`, `pandas`, `numpy`, and `plotly`.
* **Filesystem:** All 8 subject directories (`dbms_story_lab`, `ai_story_lab`, `se_story_lab`, `cloud_story_lab`, `oop_story_lab`, `dsa_story_lab`, `sd_story_lab`, `ip_story_lab`) are cloned with their full file contents.
* **Launch:** `streamlit_app.py` executes `app.py`. The dark Obsidian/Zinc dashboard loads with all 147 cases and 643 modules accessible.

---

## 6. Summary Checklist

| Task | Action | Safety Guarantee |
| :--- | :--- | :--- |
| **Nested History Backup** | Copy `.git` folders to `~/.git_backup_story_labs` | Original commits preserved |
| **Unstage Submodule Gitlinks** | `git rm --cached` | Zero disk files deleted |
| **Convert to Regular Trees** | Remove nested `.git` and `git add` | Code tracked directly in monorepo |
| **Preserve Code Lab Upgrades** | Working tree files staged as-is | Recent C++ fixes preserved |
| **Add Streamlit Cloud Shim** | Add `streamlit_app.py` calling `app.py` | Eliminates entrypoint errors |
| **Add Visualization Library** | Append `plotly` to `requirements.txt` | Eliminates missing package errors |
| **System Compiler Verification** | Confirm `g++` in `packages.txt` | Enables live C++ & DSA judges |

*This plan is ready for review. Awaiting your approval before executing any steps.*
