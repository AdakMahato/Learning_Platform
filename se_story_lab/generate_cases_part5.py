import json
import os

PART5_CASES = {}

# CASE 20: The Divergent Tree (Git & Version Control)
PART5_CASES["20"] = {
    "title": "Case 20: The Divergent Tree",
    "episodes": [
        {
            "title": "Module 1: Git Internals: The Content-Addressable DAG",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "In 2005, Linus Torvalds created **Git** in just two weeks after BitKeeper revoked the Linux kernel's free license. Unlike older centralized systems (CVS, Subversion) that stored delta diffs per file, Git is a **content-addressable filesystem** built on a cryptographically hashed Directed Acyclic Graph (DAG)."
                },
                {
                    "type": "objective",
                    "title": "Module Objective",
                    "content": "Understand Git's four core object primitives (Blobs, Trees, Commits, Annotated Tags), calculate SHA-1 content addresses, and master Fast-Forward merges vs 3-Way merges vs Rebasing."
                },
                {
                    "type": "concept",
                    "title": "Git's 4 Core Object Types",
                    "content": "Every object in `.git/objects/` is compressed with zlib and addressed by its 40-character SHA-1 (or SHA-256) hash:\n1. **Blob (Binary Large Object):** Stores pure raw file contents (no metadata, no filename, no permissions).\n2. **Tree:** Represents a directory; points to blobs (with filenames and permissions) and nested sub-trees.\n3. **Commit:** Stores snapshot pointer to top-level Tree, parent commit hash(es), author, committer, and commit message.\n4. **Tag:** A permanent reference pointing to a specific commit, with GPG signature and release notes."
                },
                {
                    "type": "visual",
                    "title": "Git Object Graph Topology",
                    "code": """graph TD
  subgraph Commits ["Commit Chain (DAG)"]
    C1["Commit A: Hash 7f2b4... (Initial)"]
    C2["Commit B: Hash 9a8c1... (Parent: A)"]
    C2 -->|"parent"| C1
  end
  subgraph TreeHierarchy ["Tree Snapshot"]
    T1["Tree: Hash 3e4f... (Root Directory)"]
    T2["Sub-Tree: Hash 5c1d... ('src/')"]
    T1 --> T2
  end
  subgraph StorageBlobs ["Content Blobs"]
    B1["Blob: Hash a81f... ('app.py')"]
    B2["Blob: Hash c902... ('README.md')"]
    T1 --> B2
    T2 --> B1
  end
  C2 -->|"points to root"| T1
  style Commits fill:#0f172a,stroke:#3b82f6
  style TreeHierarchy fill:#1e1b4b,stroke:#6366f1
  style StorageBlobs fill:#064e3b,stroke:#10b981"""
                },
                {
                    "type": "interactive",
                    "title": "Git Deduplication Challenge",
                    "question": "If you copy a 50MB video file into 10 different folders in a Git repository and commit, how many blob objects does Git store on disk?",
                    "options": [
                        "10 blobs (500MB total).",
                        "Exactly 1 blob (50MB), because Git is content-addressable: identical file content produces the exact same SHA-1 hash, so Git stores the blob once and points to it from 10 tree entries.",
                        "Zero blobs; videos are ignored.",
                        "100 blobs."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nGit addresses objects strictly by content hash ($H = \\text{SHA1}(\\text{bytes})$). Since all 10 copies have identical bytes, they share the exact same hash. Git stores a single 50MB blob in `.git/objects/` and simply references that hash in 10 separate directory trees."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Git Graph Topology Challenge",
                    "question": "The mathematical data structure that represents Git's commit history without cycles is a Directed _____ Graph (DAG).\n\nAnswer: _____",
                    "answer": "Acyclic",
                    "alternatives": ["Acyclic", "acyclic", "DAG"],
                    "explanation": "**Why Acyclic is Correct:**\nA **Directed Acyclic Graph (DAG)** ensures history flows forward along causal edges without circular loops."
                }
            ]
        },
        {
            "title": "Module 2: Fast-Forward vs. 3-Way Merge vs. Rebase",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "When integrating divergent branches, software engineers choose between **Fast-Forward Merge**, **True 3-Way Merge (`--no-ff`)**, and **Rebase**."
                },
                {
                    "type": "concept",
                    "title": "Integration Mechanisms Explained",
                    "content": "1. **Fast-Forward Merge:**\n   - Occurs when the target branch has NO new commits since the feature branch diverged.\n   - Git simply moves the branch pointer forward. No new merge commit is created.\n2. **3-Way Merge (`git merge`):**\n   - Occurs when both branches have diverged.\n   - Uses 3 snapshots: Common Ancestor ($B$), Branch 1 tip ($C$), and Branch 2 tip ($D$). Creates a new **Merge Commit** with two parents.\n3. **Rebase (`git rebase`):**\n   - Replays feature commits onto the tip of the base branch, rewriting commit SHAs to create a linear, non-branching history."
                },
                {
                    "type": "visual",
                    "title": "3-Way Merge vs. Rebase Divergence",
                    "code": """graph TD
  subgraph ThreeWayMerge ["3-Way Merge (Preserves True History)"]
    M1["Base Commit"] --> M2["Main Line"]
    M1 --> F1["Feature Line"]
    M2 & F1 --> MERGE_COMMIT["Merge Commit (2 Parents) 🔀"]
  end
  subgraph RebaseHistory ["Rebase (Rewrites to Linear History)"]
    R1["Base Commit"] --> R2["Main Line"]
    R2 --> F1_PRIME["Feature Commit (Rebased & New SHA) ➡️"]
  end
  style ThreeWayMerge fill:#1e1b4b,stroke:#6366f1
  style RebaseHistory fill:#064e3b,stroke:#10b981"""
                },
                {
                    "type": "interactive",
                    "title": "Golden Rule of Rebasing Challenge",
                    "question": "What is the 'Golden Rule of Rebasing' in software engineering?",
                    "options": [
                        "Always rebase on Fridays.",
                        "Never rebase commits that have been pushed to a public/shared repository, because rewriting shared history disrupts other developers' work.",
                        "Never use rebase if you have more than 2 files.",
                        "Rebase only on branches with merge conflicts."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nRebasing rewrites commit hashes. If other developers have based work on those commits, rebasing public branches breaks their commit history, causing severe merge conflicts and duplicate commits."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Merge Type Challenge",
                    "question": "When target branch history has not diverged from source, Git performs a fast-_____ merge without creating a merge commit.\n\nAnswer: _____",
                    "answer": "Forward",
                    "alternatives": ["Forward", "forward", "Fast-Forward", "fast-forward"],
                    "explanation": "**Why Forward is Correct:**\nA **Fast-Forward** merge simply moves the branch pointer forward along the existing linear commit chain."
                }
            ]
        },
        {
            "title": "Module 3: Git SHA-1 Blob Simulator Lab",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Let's build a working Python script that computes the exact cryptographic SHA-1 hash that Git generates for file blobs."
                },
                {
                    "type": "code_lab",
                    "title": "Git Blob Hash Calculator Lab",
                    "instructions": "Implement `compute_git_blob_hash(content_bytes)` which prepends Git's standard header `blob <size>\\0` and returns the 40-character hex SHA-1 hash.",
                    "starter_code": """import hashlib

def compute_git_blob_hash(content_bytes: bytes) -> str:
    \"\"\"
    Compute standard Git blob object hash.
    Format: 'blob <byte_length>\\0<content_bytes>'
    Hashed using SHA-1.
    \"\"\"
    # TODO: Prepend header and hash
    pass
""",
                    "solution_code": """import hashlib

def compute_git_blob_hash(content_bytes: bytes) -> str:
    header = f"blob {len(content_bytes)}\\0".encode('utf-8')
    store = header + content_bytes
    return hashlib.sha1(store).hexdigest()
""",
                    "test_code": """# Standard git hash-object test
# In git CLI: echo -n "hello world" | git hash-object --stdin
# Output: 95d09f2b10159347eece71399a7e2e907ea3df4f
raw = b"hello world"
git_hash = compute_git_blob_hash(raw)
assert git_hash == "95d09f2b10159347eece71399a7e2e907ea3df4f"

# Empty file blob
# echo -n "" | git hash-object --stdin -> e69de29bb2d1d6434b8b29ae775ad8c2e48c5391
empty_hash = compute_git_blob_hash(b"")
assert empty_hash == "e69de29bb2d1d6434b8b29ae775ad8c2e48c5391"
print("Git Blob Hash Calculator tests passed successfully!")
""",
                    "why_works": "**Why This Solution Works:**\nGit prefixes every stored object with a type header and size in bytes, terminated by a null byte `\\0`. The SHA-1 of this prefixed block matches the exact hash reported by `git hash-object`.",
                    "alternatives": "**Alternative Approaches & Trade-offs:**\n- **Git SHA-256 Migration:** Modern Git repositories can be initialized with `--object-format=sha256` to prevent theoretical SHA-1 collision vulnerabilities (SHAttered attack).\n- **Git LFS (Large File Storage):** Replaces gigabyte assets with tiny pointer text files, storing raw media in S3."
                }
            ]
        },
        {
            "title": "Module 4: Trunk-Based Development vs. GitFlow",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Branching strategies dictate how teams collaborate. While **GitFlow** defined the 2010s, high-performing engineering organizations (Google, Meta, Netflix) have migrated to **Trunk-Based Development**."
                },
                {
                    "type": "concept",
                    "title": "Trunk-Based vs. GitFlow Matrix",
                    "content": "| Dimension | GitFlow | Trunk-Based Development |\n|---|---|---|\n| **Branches** | `main`, `develop`, `release/*`, `feature/*`, `hotfix/*` | Single trunk (`main`) with short-lived feature branches (< 1-2 days) |\n| **Merge Cadence** | Sprints / Weeks (Large batch merges) | Multiple times per day via Continuous Integration |\n| **Merge Conflicts** | Frequent 'Merge Hell' when feature branches live for 4 weeks | Minimal; branches are small and constantly rebased |\n| **Feature Hiding** | Long-lived unmerged feature branches | **Feature Flags (Toggles)** in trunk |\n| **DORA Metrics** | Slower lead time; infrequent releases | Elite performance: continuous on-demand deployments |"
                },
                {
                    "type": "interactive",
                    "title": "Branching Strategy Challenge",
                    "question": "In Trunk-Based Development, how do developers deploy unfinished, partially coded features to production without exposing them to users?",
                    "options": [
                        "Keep the code on their local laptop for 6 months.",
                        "Wrap incomplete features in Feature Flags (Toggles) that are turned off in production, allowing code to be merged safely into trunk daily.",
                        "Comment out the lines of code before merging.",
                        "Encrypt the pull request with a password."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\n**Feature Flags (Toggles)** decouple code deployment from feature release. Incomplete code can be continuously merged into trunk and deployed to production multiple times a day behind a flag turned OFF, eliminating merge hell."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Continuous Delivery Mechanism Challenge",
                    "question": "The software technique of wrapping code in conditional switches to toggle visibility at runtime without redeploying is called a Feature _____.\n\nAnswer: _____",
                    "answer": "Flag",
                    "alternatives": ["Flag", "flag", "Toggle", "toggle", "Feature Flag", "Feature Toggle"],
                    "explanation": "**Why Flag is Correct:**\n**Feature Flags** are the backbone of modern Continuous Delivery and trunk-based engineering."
                }
            ]
        }
    ]
}

# CASE 21: The Continuous Assembly (CI/CD Pipelines)
PART5_CASES["21"] = {
    "title": "Case 21: The Continuous Assembly",
    "episodes": [
        {
            "title": "Module 1: The CI/CD Pipeline Architecture",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Jez Humble and David Farley published *Continuous Delivery* in 2010, demonstrating that building, testing, and deploying software must be automated into a reliable, repeatable assembly line: the **Deployment Pipeline**."
                },
                {
                    "type": "objective",
                    "title": "Module Objective",
                    "content": "Master the stages of modern CI/CD pipelines, enforce automated quality gates, and compare Blue-Green vs Canary deployment rollout strategies."
                },
                {
                    "type": "concept",
                    "title": "CI vs. CD vs. CD Distinction",
                    "content": "1. **Continuous Integration (CI):** Developers merge code to trunk daily; every commit triggers automated linting, compilation, and unit tests.\n2. **Continuous Delivery (CD):** Every build that passes all automated test gates is automatically packaged and deployable to production at the click of a button.\n3. **Continuous Deployment (CD):** Zero human intervention; every commit that passes automated testing is automatically deployed directly to production live users."
                },
                {
                    "type": "visual",
                    "title": "Standard Enterprise CI/CD Pipeline Stages",
                    "code": """graph LR
  subgraph CI ["Continuous Integration (Commit Phase)"]
    C["Code Push"] --> LINT["Lint & Static Analysis (SonarQube)"]
    LINT --> UNIT["Unit & Mutation Tests"]
    UNIT --> BUILD["Docker Container Build"]
  end
  subgraph QualityGates ["Automated Quality Gates"]
    BUILD --> SEC["Security SAST/DAST Scan"]
    SEC --> INT["Integration Test Suite"]
  end
  subgraph CD ["Continuous Deployment Phase"]
    INT --> STAGING["Staging Canary Deployment"]
    STAGING --> PROD["Production Progressive Rollout 🚀"]
  end
  style CI fill:#0f172a,stroke:#3b82f6
  style QualityGates fill:#1e1b4b,stroke:#6366f1
  style CD fill:#064e3b,stroke:#10b981"""
                },
                {
                    "type": "interactive",
                    "title": "Pipeline Terminology Challenge",
                    "question": "What is the technical distinction between Continuous Delivery and Continuous Deployment?",
                    "options": [
                        "Continuous Delivery uses Docker, whereas Continuous Deployment uses Kubernetes.",
                        "In Continuous Delivery, the release to production requires manual human approval; in Continuous Deployment, passing all automated gates deploys to production automatically without human intervention.",
                        "Continuous Delivery is for open-source projects only.",
                        "There is no difference; they are exact synonyms."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nBoth practices ensure software is always in a releasable state. The critical dividing line is automation to production: **Continuous Delivery** has a manual gate (business approval), whereas **Continuous Deployment** is fully automated from git commit to production."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "CI Acronym Challenge",
                    "question": "The software engineering practice of having developers integrate code into a shared repository several times a day with automated builds is Continuous _____.\n\nAnswer: _____",
                    "answer": "Integration",
                    "alternatives": ["Integration", "integration", "CI"],
                    "explanation": "**Why Integration is Correct:**\n**Continuous Integration (CI)** detects integration bugs within minutes of code commitment."
                }
            ]
        },
        {
            "title": "Module 2: Blue-Green vs. Canary Deployments",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Zero-downtime deployment strategies allow updating production servers without interrupting active user transactions."
                },
                {
                    "type": "concept",
                    "title": "Deployment Rollout Strategies",
                    "content": "### 1. Blue-Green Deployment\n- Maintain two identical production environments: **Blue** (currently serving live traffic) and **Green** (idle).\n- Deploy new version to Green, run smoke tests, then switch the router/load balancer to point to Green.\n- Instant rollback: switch router back to Blue if errors occur.\n\n### 2. Canary Deployment\n- Roll out the new version to a tiny subset of real production users (e.g. 2% or 5%).\n- Monitor error rates, latency, and crash telemetry.\n- If metrics remain healthy, progressively ramp up traffic (10% -> 50% -> 100%)."
                },
                {
                    "type": "visual",
                    "title": "Canary Traffic Shifting Topology",
                    "code": """graph LR
  subgraph Ingress ["Load Balancer Router"]
    LB["Envoy / NGINX Ingress"]
  end
  subgraph ProductionFleet ["Production Pods Fleet"]
    STABLE["Stable Fleet v1.4 (95% Traffic)"]
    CANARY["Canary Pods v1.5 (5% Traffic) 🐤"]
  end
  LB -->|"95% Traffic"| STABLE
  LB -->|"5% Traffic"| CANARY
  style Ingress fill:#0f172a,stroke:#3b82f6
  style STABLE fill:#1e1b4b,stroke:#6366f1
  style CANARY fill:#064e3b,stroke:#10b981"""
                },
                {
                    "type": "interactive",
                    "title": "Canary Deployment Advantage Challenge",
                    "question": "What is the primary advantage of a Canary deployment over an all-at-once deployment?",
                    "options": [
                        "It requires zero automated monitoring.",
                        "It minimizes the blast radius of unexpected defects, exposing only a tiny percentage of users to potential bugs while verifying health metrics under real production workloads.",
                        "It makes database migrations obsolete.",
                        "It eliminates the need for unit testing."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\n**Blast radius containment** is the essence of Canary releases: if a severe bug escapes into the new build, only 2% of users experience it, and automated monitors roll back before 100% of the user base is impacted."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Deployment Metaphor Challenge",
                    "question": "The name for incremental traffic shifting comes from miners using a _____ in a coal mine to detect toxic gases early.\n\nAnswer: _____",
                    "answer": "Canary",
                    "alternatives": ["Canary", "canary", "Canary Deployment"],
                    "explanation": "**Why Canary is Correct:**\nJust as miners used canaries to detect carbon monoxide before it harmed humans, **canary releases** detect software defects under a fraction of user traffic."
                }
            ]
        },
        {
            "title": "Module 3: Automated Pipeline Gate Simulator Lab",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Let's build a CI/CD Quality Gate engine that evaluates test results, code coverage, and static analysis security findings to make an automated deploy/reject decision."
                },
                {
                    "type": "code_lab",
                    "title": "CI/CD Quality Gate Verifier",
                    "instructions": "Implement `evaluate_quality_gate(test_pass_rate, coverage_pct, critical_security_flaws, high_flaws)` enforcing: pass rate == 100%, coverage >= 80%, critical flaws == 0, and high flaws <= 2.",
                    "starter_code": """def evaluate_quality_gate(test_pass_rate: float, coverage_pct: float, critical_vulns: int, high_vulns: int) -> dict:
    \"\"\"
    Enforce deployment quality gates:
      - test_pass_rate must be 100.0%
      - coverage_pct must be >= 80.0%
      - critical_vulns must be 0
      - high_vulns must be <= 2
      
    Returns dict:
      - 'status': 'PASSED' or 'FAILED'
      - 'blockers': list of str describing violated rules
    \"\"\"
    # TODO: Evaluate gate
    pass
""",
                    "solution_code": """def evaluate_quality_gate(test_pass_rate: float, coverage_pct: float, critical_vulns: int, high_vulns: int) -> dict:
    blockers = []
    
    if test_pass_rate < 100.0:
        blockers.append(f"Test pass rate {test_pass_rate}% is below required 100.0%")
    if coverage_pct < 80.0:
        blockers.append(f"Code coverage {coverage_pct}% is below required 80.0%")
    if critical_vulns > 0:
        blockers.append(f"Detected {critical_vulns} Critical security vulnerabilities (maximum allowed: 0)")
    if high_vulns > 2:
        blockers.append(f"Detected {high_vulns} High security vulnerabilities (maximum allowed: 2)")
        
    return {
        'status': 'PASSED' if len(blockers) == 0 else 'FAILED',
        'blockers': blockers
    }
""",
                    "test_code": """# Perfect build
res1 = evaluate_quality_gate(100.0, 85.5, 0, 1)
assert res1['status'] == 'PASSED'
assert len(res1['blockers']) == 0

# Failing build: test failures and critical vuln
res2 = evaluate_quality_gate(98.0, 75.0, 1, 4)
assert res2['status'] == 'FAILED'
assert len(res2['blockers']) == 4
print("Quality Gate Verifier tests passed successfully!")
""",
                    "why_works": "**Why This Solution Works:**\nAutomated quality gates provide deterministic governance. By evaluating static analysis vulnerabilities, coverage thresholds, and test pass rates programmatically, bad builds are halted before reaching production."
                }
            ]
        },
        {
            "title": "Module 4: DORA Metrics & Elite Engineering",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "The DevOps Research and Assessment (DORA) team surveyed over 30,000 engineering organizations to identify the four key metrics that distinguish **Elite** engineering teams from low performers."
                },
                {
                    "type": "concept",
                    "title": "The 4 DORA Metrics",
                    "content": "1. **Deployment Frequency:** How often an organization successfully releases to production (Elite: multiple times per day).\n2. **Lead Time for Changes:** The time it takes for a commit to get into production (Elite: less than one hour).\n3. **Change Failure Rate (CFR):** The percentage of deployments causing a degradation in service that requires a rollback or hotfix (Elite: 0% - 15%).\n4. **Time to Restore Service (MTTR):** How long it takes to restore service when a production outage occurs (Elite: less than one hour)."
                },
                {
                    "type": "interactive",
                    "title": "DORA Metric Balance Challenge",
                    "question": "A team deploys 50 times a day, but 40% of deployments crash production and require emergency rollback. What DORA metric reveals their failure?",
                    "options": [
                        "Deployment Frequency.",
                        "Change Failure Rate (CFR) — high deployment speed is meaningless if releases are defective and unstable.",
                        "Lead Time for Changes.",
                        "Lines of code per day."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nThe DORA metrics are intentionally balanced: throughput metrics (Deployment Frequency, Lead Time) are paired with stability metrics (**Change Failure Rate**, MTTR). A team with a 40% failure rate is unstable regardless of high deployment frequency."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "DORA Acronym Challenge",
                    "question": "The time it takes to recover from an unplanned production incident is Mean Time to _____ (MTTR).\n\nAnswer: _____",
                    "answer": "Restore",
                    "alternatives": ["Restore", "restore", "Recovery", "recovery", "MTTR"],
                    "explanation": "**Why Restore is Correct:**\n**Mean Time to Restore (MTTR)** measures operational recovery speed, which is vastly improved by automated rollback and canary deployment pipelines."
                }
            ]
        }
    ]
}

# CASE 22: The Legacy Curse (Software Maintenance & Evolution)
PART5_CASES["22"] = {
    "title": "Case 22: The Legacy Curse",
    "episodes": [
        {
            "title": "Module 1: Lehman's Laws of Software Evolution",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Between 1974 and 1996, Meir M. Lehman formulated eight empirical laws governing how E-type (evolutionary real-world) software systems behave over time. Lehman showed that software does not stay healthy on its own; without conscious refactoring, systems inevitably decay."
                },
                {
                    "type": "objective",
                    "title": "Module Objective",
                    "content": "Master Lehman's Laws of Software Evolution, identify Martin Fowler's code smells, and calculate Technical Debt ratios."
                },
                {
                    "type": "concept",
                    "title": "Key Lehman Laws",
                    "content": "- **1. Law of Continuing Change:** An E-type system must continually adapt or it becomes progressively less satisfactory in real-world usage.\n- **2. Law of Increasing Complexity:** As an evolving program is modified, its complexity increases unless work is done to maintain or reduce it.\n- **6. Law of Continuing Growth:** The functional content of systems must continually increase to maintain user satisfaction over its lifetime.\n- **7. Law of Declining Quality:** The quality of systems will appear to decline unless they are modified to adapt to changes in operational environments."
                },
                {
                    "type": "visual",
                    "title": "Lehman's Complexity Escalation Curve",
                    "code": """graph TD
  subgraph NaturalEntropy ["Natural Code Entropy (Unchecked Changes)"]
    V1["Version 1.0 (Clean Architecture)"] --> V2["Version 2.0 (Quick Hack Patches)"]
    V2 --> V3["Version 3.0 (Spaghetti Dependencies)"]
    V3 --> COLLAPSE["System Collapse / Stagnation 💥"]
  end
  subgraph ActiveRefactoring ["Disciplined Continuous Refactoring"]
    V1_R["Version 1.0"] --> REFACTOR["Refactoring Investment"]
    REFACTOR --> V2_R["Version 2.0 (Architecture Preserved)"]
  end
  style NaturalEntropy fill:#3f1a1a,stroke:#ef4444
  style ActiveRefactoring fill:#064e3b,stroke:#10b981"""
                },
                {
                    "type": "interactive",
                    "title": "Software Evolution Law Challenge",
                    "question": "According to Lehman's Second Law (Increasing Complexity), what happens to software systems if developers do not actively invest in refactoring?",
                    "options": [
                        "The software runs faster over time.",
                        "Its internal complexity increases monotonically with every feature and patch until modifications become prohibitively expensive.",
                        "Hardware compilers automatically refactor the code.",
                        "Complexity stays constant."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nLehman's Second Law proves that software entropy is natural: adding features into an existing architecture erodes its original conceptual structure unless engineers deliberately allocate effort to refactoring."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Evolution Law Author Challenge",
                    "question": "The computer scientist who formulated the Laws of Software Evolution is Meir _____.\n\nAnswer: _____",
                    "answer": "Lehman",
                    "alternatives": ["Lehman", "lehman", "Meir Lehman"],
                    "explanation": "**Why Lehman is Correct:**\n**Meir Lehman** established empirical laws that remain the foundation of software evolution studies."
                }
            ]
        },
        {
            "title": "Module 2: Martin Fowler's Code Smells Catalog",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "In *Refactoring*, Martin Fowler and Kent Beck defined **Code Smells**: surface indications that usually correspond to a deeper architectural flaw in the system."
                },
                {
                    "type": "concept",
                    "title": "Classic Code Smells Catalog",
                    "content": "1. **Long Method:** A method containing 80+ lines doing 5 different things. *Remedy:* Extract Method.\n2. **God Class (Large Class):** A class with 3,000 lines knowing and doing everything. *Remedy:* Extract Class.\n3. **Feature Envy:** A method in Class A is constantly querying getters of Class B to do calculations. *Remedy:* Move Method to Class B.\n4. **Data Clumps:** Groups of data variables that always travel together (e.g. `street`, `city`, `zip_code`). *Remedy:* Introduce Parameter Object.\n5. **Shotgun Surgery:** Making one small change requires touching 15 different files. *Remedy:* Move Method / Inline Class to consolidate responsibilities."
                },
                {
                    "type": "interactive",
                    "title": "Code Smell Identification Challenge",
                    "question": "A method `calculateTax()` on `Invoice` spends 90% of its lines calling methods on `CustomerLocation` to look up regional postal codes and tax zones. What code smell is present?",
                    "options": [
                        "Data Clumps.",
                        "Feature Envy (the method is more interested in the data of CustomerLocation than its own class).",
                        "Dead Code.",
                        "Refused Bequest."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\n**Feature Envy** occurs when a method utilizes data and services of another class more than those of its host class. The remedy is to move the calculation into `CustomerLocation`."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Smell Antipattern Challenge",
                    "question": "The code smell where making a single conceptual change forces you to make dozens of tiny edits across many different classes is called _____ Surgery.\n\nAnswer: _____",
                    "answer": "Shotgun",
                    "alternatives": ["Shotgun", "shotgun", "Shotgun Surgery"],
                    "explanation": "**Why Shotgun is Correct:**\n**Shotgun Surgery** is the opposite of Divergent Change: one change scatters edits across many classes, signaling that responsibilities are improperly distributed."
                }
            ]
        },
        {
            "title": "Module 3: Code Smell Detector Lab",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Let's build a static analysis rule engine that inspects Python functions and flags Long Method and Parameter List code smells."
                },
                {
                    "type": "code_lab",
                    "title": "Static Code Smell Detector",
                    "instructions": "Implement `analyze_function_smells(lines_of_code, parameter_count, cyclomatic_complexity)` flagging 'Long Method' (> 30 lines), 'Too Many Parameters' (> 4 params), and 'Excessive Complexity' (> 10).",
                    "starter_code": """def analyze_function_smells(loc: int, param_count: int, complexity: int) -> dict:
    \"\"\"
    Detect code smells based on standard thresholds:
      - loc > 30 -> 'Long Method'
      - param_count > 4 -> 'Long Parameter List'
      - complexity > 10 -> 'High Complexity'
      
    Returns dict:
      - 'smells_detected': list of str
      - 'is_clean': bool (True if no smells)
    \"\"\"
    # TODO: Detect smells
    pass
""",
                    "solution_code": """def analyze_function_smells(loc: int, param_count: int, complexity: int) -> dict:
    smells = []
    if loc > 30:
        smells.append("Long Method")
    if param_count > 4:
        smells.append("Long Parameter List")
    if complexity > 10:
        smells.append("High Complexity")
        
    return {
        'smells_detected': smells,
        'is_clean': len(smells) == 0
    }
""",
                    "test_code": """res1 = analyze_function_smells(15, 2, 4)
assert res1['is_clean'] is True
assert len(res1['smells_detected']) == 0

res2 = analyze_function_smells(85, 6, 14)
assert res2['is_clean'] is False
assert "Long Method" in res2['smells_detected']
assert "Long Parameter List" in res2['smells_detected']
assert "High Complexity" in res2['smells_detected']
print("Code Smell Detector tests passed successfully!")
""",
                    "why_works": "**Why This Solution Works:**\nFormalizing code smell heuristics into threshold checks allows teams to automate linting in pre-commit hooks, preventing long, convoluted functions from entering the codebase."
                }
            ]
        },
        {
            "title": "Module 4: Technical Debt Ratio (TDR)",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "In enterprise quality governance (e.g. SonarQube), technical debt is quantified as the **Technical Debt Ratio (TDR)**."
                },
                {
                    "type": "concept",
                    "title": "The Technical Debt Ratio Formula",
                    "content": "$$\\text{TDR} = \\frac{\\text{Remediation Cost}}{\\text{Development Cost}} \\times 100\\%$$\n\nWhere:\n- **Remediation Cost:** The estimated person-hours required to refactor and fix all detected code smells, vulnerabilities, and duplications.\n- **Development Cost:** The estimated cost to rewrite the entire codebase from scratch.\n- **Quality Rating:** $TDR \\le 5\\%$ is an 'A' rating; $TDR > 20\\%$ indicates severe architectural bankruptcy."
                },
                {
                    "type": "interactive",
                    "title": "Technical Debt Evaluation Challenge",
                    "question": "A legacy system would cost $1,000,000 to rebuild from scratch. SonarQube estimates it will take $250,000 of engineering hours to fix all outstanding bugs and code smells. What is the Technical Debt Ratio (TDR)?",
                    "options": [
                        "2.5%.",
                        "25.0% (indicating dangerous architectural debt requiring immediate refactoring sprints).",
                        "250%.",
                        "0.25%."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\n$$\\text{TDR} = \\frac{\\$250,000}{\\$1,000,000} \\times 100\\% = 25.0\\%$$\nA ratio exceeding 20% means a full quarter of the entire system's replacement value is consumed by technical debt, placing the project in an unmaintainable danger zone."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Debt Metaphor Originator Challenge",
                    "question": "The computer programmer who coined the metaphor of Technical Debt in 1992 is Ward _____.\n\nAnswer: _____",
                    "answer": "Cunningham",
                    "alternatives": ["Cunningham", "cunningham", "Ward Cunningham"],
                    "explanation": "**Why Cunningham is Correct:**\n**Ward Cunningham** (who also invented the Wiki) coined the Technical Debt metaphor to explain the cost of rushed engineering to business executives."
                }
            ]
        }
    ]
}

# CASE 23: The Estimation Mirage (Project Estimation)
PART5_CASES["23"] = {
    "title": "Case 23: The Estimation Mirage",
    "episodes": [
        {
            "title": "Module 1: Barry Boehm's COCOMO Model",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Why are software schedules notoriously inaccurate? In 1981, Barry Boehm formulated the **Constructive Cost Model (COCOMO)** based on empirical data from hundreds of aerospace and commercial projects."
                },
                {
                    "type": "objective",
                    "title": "Module Objective",
                    "content": "Master the Basic and Intermediate COCOMO formulas, calculate Effort in Person-Months (PM) and Development Time (TDEV), and understand Function Point Analysis (FPA)."
                },
                {
                    "type": "concept",
                    "title": "The Basic COCOMO Formula",
                    "content": "$$\\text{Effort (Person-Months)} = a \\times (\\text{KLOC})^b$$\n$$\\text{Development Time (Months)} = c \\times (\\text{Effort})^d$$\n\n### Project Modes:\n1. **Organic ($a=2.4, b=1.05$):** Small, experienced teams working in familiar environments with flexible requirements.\n2. **Semidetached ($a=3.0, b=1.12$):** Medium-sized teams with mixed experience levels.\n3. **Embedded ($a=3.6, b=1.20$):** Software built under tight hardware, regulation, and operational constraints (e.g. flight avionics, medical implants)."
                },
                {
                    "type": "visual",
                    "title": "COCOMO Non-Linear Scaling by Project Mode",
                    "code": """graph LR
  subgraph Modes ["COCOMO Project Complexity Scaling"]
    O["Organic (Exponent b = 1.05: Almost Linear)"]
    S["Semidetached (Exponent b = 1.12: Moderate Curvature)"]
    E["Embedded (Exponent b = 1.20: Severe Exponential Growth!)"]
  end
  style O fill:#064e3b,stroke:#10b981
  style S fill:#1e1b4b,stroke:#6366f1
  style E fill:#3f1a1a,stroke:#ef4444"""
                },
                {
                    "type": "interactive",
                    "title": "COCOMO Scaling Exponent Challenge",
                    "question": "In the COCOMO formula $\\text{Effort} = a \\times (\\text{KLOC})^b$, why is the exponent $b$ always greater than 1.0?",
                    "options": [
                        "Because larger codebases require faster computers.",
                        "Because communication and coordination overhead among developers scales quadratically with team size ($N(N-1)/2$), meaning double the code requires more than double the effort.",
                        "It is an arbitrary mathematical constant.",
                        "To account for inflation."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nAs system scale grows, communication channels explode as $N(N-1)/2$. A 100 KLOC system requires more coordination, integration testing, and documentation than two separate 50 KLOC systems, making $b > 1.0$ (diseconomies of scale)."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "KLOC Acronym Challenge",
                    "question": "In software estimation models, the acronym KLOC stands for Thousands of Lines of _____.\n\nAnswer: _____",
                    "answer": "Code",
                    "alternatives": ["Code", "code", "Lines of Code"],
                    "explanation": "**Why Code is Correct:**\n**KLOC** (Kilo Lines of Code) was the foundational sizing metric in early algorithmic estimation models."
                }
            ]
        },
        {
            "title": "Module 2: COCOMO Calculation Engine Lab",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Let's implement a functional COCOMO estimation calculator that models effort and delivery time across different project modes."
                },
                {
                    "type": "code_lab",
                    "title": "COCOMO Estimation Calculator",
                    "instructions": "Implement `estimate_cocomo_effort(kloc, mode)` supporting 'organic', 'semidetached', and 'embedded' modes to compute Effort (Person-Months) and TDEV (Duration Months).",
                    "starter_code": """def estimate_cocomo_effort(kloc: float, mode: str = 'organic') -> dict:
    \"\"\"
    Calculate Basic COCOMO effort and schedule.
    Modes:
      - organic: a=2.4, b=1.05, c=2.5, d=0.38
      - semidetached: a=3.0, b=1.12, c=2.5, d=0.35
      - embedded: a=3.6, b=1.20, c=2.5, d=0.32
      
    Effort = a * (kloc ** b)
    TDEV = c * (Effort ** d)
    Staffing = Effort / TDEV
    
    Returns dict:
      - 'effort_pm': float (rounded to 2 decimals)
      - 'duration_months': float (rounded to 2 decimals)
      - 'team_size_people': float (rounded to 1 decimal)
    \"\"\"
    # TODO: Implement COCOMO formula
    pass
""",
                    "solution_code": """def estimate_cocomo_effort(kloc: float, mode: str = 'organic') -> dict:
    coefficients = {
        'organic': (2.4, 1.05, 2.5, 0.38),
        'semidetached': (3.0, 1.12, 2.5, 0.35),
        'embedded': (3.6, 1.20, 2.5, 0.32)
    }
    a, b, c, d = coefficients.get(mode.lower(), coefficients['organic'])
    
    effort = a * (kloc ** b)
    tdev = c * (effort ** d)
    staff = effort / tdev if tdev > 0 else 0.0
    
    return {
        'effort_pm': round(effort, 2),
        'duration_months': round(tdev, 2),
        'team_size_people': round(staff, 1)
    }
""",
                    "test_code": """# 30 KLOC Organic project
res = estimate_cocomo_effort(30.0, 'organic')
assert abs(res['effort_pm'] - 85.35) < 1.0
assert abs(res['duration_months'] - 13.62) < 0.5
assert abs(res['team_size_people'] - 6.4) < 0.5

# 30 KLOC Embedded project (avionics)
res_emb = estimate_cocomo_effort(30.0, 'embedded')
assert res_emb['effort_pm'] > res['effort_pm'] # Embedded requires much more effort
print("COCOMO Calculator tests passed successfully!")
""",
                    "why_works": "**Why This Solution Works:**\nCOCOMO quantifies the nonlinear expansion of development effort as codebase size grows. An embedded 30 KLOC project requires nearly 214 person-months compared to 86 person-months for organic development due to regulatory compliance and hardware constraints."
                }
            ]
        },
        {
            "title": "Module 3: Albrecht's Function Point Analysis (FPA)",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Allan Albrecht at IBM realized that KLOC is flawed: counting lines of code rewards verbose languages (Assembly) and penalizes concise languages (Python). In 1979, he created **Function Point Analysis (FPA)** to estimate software based purely on functionality delivered to users."
                },
                {
                    "type": "concept",
                    "title": "The 5 Function Point Components",
                    "content": "1. **External Inputs (EI):** User input screens, data entry forms.\n2. **External Outputs (EO):** Reports, printable invoices, calculated summaries.\n3. **External Inquiries (EQ):** Search queries returning data without updating databases.\n4. **Internal Logical Files (ILF):** User data tables maintained inside the application boundary.\n5. **External Interface Files (EIF):** Data referenced from external systems (e.g. Stripe API records)."
                },
                {
                    "type": "interactive",
                    "title": "FPA Language Independence Challenge",
                    "question": "What is the primary conceptual advantage of Function Points over Lines of Code (KLOC)?",
                    "options": [
                        "Function Points can only be used for Java.",
                        "Function Points measure delivered business functionality independently of programming language, whereas KLOC varies wildly across different languages.",
                        "Function Points measure CPU cache hit rates.",
                        "Function Points calculate salary."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nA feature that takes 1,000 lines of C might take 50 lines of Python. Sizing by KLOC artificially inflates the perceived value of low-level languages. Function Points measure user capability regardless of syntax."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "FPA Creator Challenge",
                    "question": "The IBM researcher who invented Function Point Analysis in 1979 is Allan _____.\n\nAnswer: _____",
                    "answer": "Albrecht",
                    "alternatives": ["Albrecht", "albrecht", "Allan Albrecht"],
                    "explanation": "**Why Albrecht is Correct:**\n**Allan Albrecht** founded Function Point Analysis, which is now standardized globally by IFPUG."
                }
            ]
        },
        {
            "title": "Module 4: Brooks' Law & The Mythical Man-Month",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Fred Brooks led the development of IBM's OS/360 operating system. In *The Mythical Man-Month*, he observed the most famous law of software project management: **Brooks' Law**."
                },
                {
                    "type": "concept",
                    "title": "Brooks' Law Stated",
                    "content": "> *'Adding manpower to a late software project makes it later.'*\n\n### Why Brooks' Law Occurs:\n1. **Ramp-Up Time:** New engineers know nothing about the codebase; existing top engineers must stop coding to mentor and train them.\n2. **Communication Combinatorics:** $N$ developers have $\\frac{N(N-1)}{2}$ communication channels. Adding 5 people to a team of 5 doubles communication paths from 10 to 45.\n3. **Divisibility of Tasks:** Software engineering is like pregnancy: *'Nine women cannot make a baby in one month.'*"
                },
                {
                    "type": "interactive",
                    "title": "Brooks' Law Management Challenge",
                    "question": "A critical banking project is 3 weeks behind schedule. The vice president proposes hiring 10 contract developers immediately to catch up. What does Brooks' Law predict will happen?",
                    "options": [
                        "The project will be completed 3 weeks early.",
                        "The project will suffer even further delays because existing engineers will spend their time onboarding and untangling merge conflicts.",
                        "Communication channels will decrease.",
                        "Code quality will immediately triple."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nBrooks' Law warns that onboarding newcomers consumes the precious bandwidth of the few developers who understand the system, exacerbating delays rather than accelerating delivery."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Famous Book Author Challenge",
                    "question": "The author of 'The Mythical Man-Month' and winner of the Turing Award is Fred _____.\n\nAnswer: _____",
                    "answer": "Brooks",
                    "alternatives": ["Brooks", "brooks", "Fred Brooks"],
                    "explanation": "**Why Brooks is Correct:**\n**Fred Brooks** gave software engineering many of its most enduring insights, including 'No Silver Bullet' and Brooks' Law."
                }
            ]
        }
    ]
}

# CASE 24: The Reliable Fortress (Quality Assurance & SRE)
PART5_CASES["24"] = {
    "title": "Case 24: The Reliable Fortress",
    "episodes": [
        {
            "title": "Module 1: The ISO/IEC 25010 Quality Model",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "How do you define 'software quality' objectively? The international standard **ISO/IEC 25010** (Systems and Software Quality Requirements and Evaluation - SQuaRE) establishes the definitive taxonomy of software product quality."
                },
                {
                    "type": "objective",
                    "title": "Module Objective",
                    "content": "Master the 8 Quality Characteristics of ISO 25010, mitigate OWASP Top 10 vulnerabilities, and implement Site Reliability Engineering (SRE) SLOs and Error Budgets."
                },
                {
                    "type": "concept",
                    "title": "The 8 ISO 25010 Quality Characteristics",
                    "content": "1. **Functional Suitability:** Completeness, correctness, and appropriateness of features.\n2. **Performance Efficiency:** Time behavior (latency), resource utilization (RAM/CPU), capacity.\n3. **Compatibility:** Co-existence and interoperability with other systems.\n4. **Usability:** Appropriateness, learnability, operability, user error protection, aesthetics.\n5. **Reliability:** Maturity, availability, fault tolerance, recoverability.\n6. **Security:** Confidentiality, integrity, non-repudiation, accountability, authenticity.\n7. **Maintainability:** Modularity, reusability, analyzability, modifiability, testability.\n8. **Portability:** Adaptability, installability, replaceability."
                },
                {
                    "type": "visual",
                    "title": "ISO 25010 Product Quality Spectrum",
                    "code": """graph TD
  subgraph OperationalQualities ["Runtime Operational Qualities"]
    P["Performance Efficiency (Latency & CPU)"]
    R["Reliability (Fault Tolerance & Uptime)"]
    S["Security (Integrity & Encryption)"]
    U["Usability (UX & Error Protection)"]
  end
  subgraph ArchitecturalQualities ["Internal Architectural Qualities"]
    M["Maintainability (Modularity & Testability)"]
    PORT["Portability (Docker Container Adaptability)"]
    C["Compatibility (API Interoperability)"]
    F["Functional Suitability"]
  end
  style OperationalQualities fill:#0f172a,stroke:#3b82f6
  style ArchitecturalQualities fill:#064e3b,stroke:#10b981"""
                },
                {
                    "type": "interactive",
                    "title": "ISO Quality Classification Challenge",
                    "question": "A system survives an unexpected power failure in the primary datacenter and recovers full database operations within 4 minutes with zero data corruption. Which ISO 25010 quality characteristic does this demonstrate?",
                    "options": [
                        "Usability.",
                        "Reliability (specifically Fault Tolerance and Recoverability).",
                        "Portability.",
                        "Functional Completeness."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\n**Reliability** covers the system's ability to maintain a specified level of performance under stated conditions, including **Fault Tolerance** (withstanding component failure) and **Recoverability** (restoring state after disaster)."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "ISO Standard Number Challenge",
                    "question": "The international ISO standard governing software product quality models is ISO _____.\n\nAnswer: _____",
                    "answer": "25010",
                    "alternatives": ["25010", "ISO 25010", "ISO/IEC 25010"],
                    "explanation": "**Why 25010 is Correct:**\n**ISO/IEC 25010** replaced the older ISO 9126 standard and is the global benchmark for software quality models."
                }
            ]
        },
        {
            "title": "Module 2: The OWASP Top 10 Security Architecture",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Security is an architectural non-functional requirement. The **Open Web Application Security Project (OWASP)** publishes the consensus ranking of the most critical security vulnerabilities threatening modern applications."
                },
                {
                    "type": "concept",
                    "title": "Core OWASP Top 10 Vulnerabilities",
                    "content": "1. **Broken Access Control (A01):** Failure to enforce authorization; users can access other users' private accounts by tampering with URLs (`/users/102` -> `/users/103`).\n2. **Cryptographic Failures (A02):** Transmitting plain text passwords over HTTP or using obsolete algorithms (MD5, DES).\n3. **Injection (A03):** SQL Injection, OS command injection. Untrusted user data is concatenated directly into interpreter queries.\n4. **Insecure Design (A04):** Flaws in fundamental architecture (e.g. lacking account lockout against brute force).\n5. **Security Misconfiguration (A05):** Default passwords, enabled debug endpoints, overly permissive CORS headers."
                },
                {
                    "type": "interactive",
                    "title": "SQL Injection Remediation Challenge",
                    "question": "A developer writes: `cursor.execute(\"SELECT * FROM users WHERE email = '\" + email + \"'\")`. How should this be refactored to eliminate SQL Injection?",
                    "options": [
                        "Check if the email ends in .com.",
                        "Use parameterized queries (prepared statements): `cursor.execute(\"SELECT * FROM users WHERE email = %s\", (email,))`, ensuring user input is treated as literal data, never executable code.",
                        "Encrypt the database hard drive.",
                        "Wrap the database query in a try/except block."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\n**Parameterized queries** separate the SQL code structure from untrusted user input. The database engine compiles the query template first, rendering SQL injection mathematically impossible regardless of what strings the user inputs."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Security Consortium Challenge",
                    "question": "The international non-profit security organization that publishes the Top 10 Web Application Vulnerabilities is _____.\n\nAnswer: _____",
                    "answer": "OWASP",
                    "alternatives": ["OWASP", "owasp"],
                    "explanation": "**Why OWASP is Correct:**\n**OWASP** provides free security methodologies, standards, and vulnerability scanning tools used worldwide."
                }
            ]
        },
        {
            "title": "Module 3: Site Reliability Engineering (SRE): SLI, SLO, SLA",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "Pioneered by Ben Treynor Sloss at Google, **Site Reliability Engineering (SRE)** applies software engineering principles to operations: *'SRE is what happens when you ask a software engineer to design an operations team.'*"
                },
                {
                    "type": "concept",
                    "title": "The SRE Reliability Triad & Error Budgets",
                    "content": "- **SLI (Service Level Indicator):** The quantitative metric measured in real time (e.g. *Successful HTTP requests / Total requests = 99.95%*).\n- **SLO (Service Level Objective):** The internal target agreed by engineering and product (e.g. *99.9% uptime over a rolling 30-day window*).\n- **SLA (Service Level Agreement):** The legal/financial contract with customers promising uptime, with penalty refunds if violated.\n- **Error Budget ($1 - \\text{SLO}$):** The allowable amount of downtime. An SLO of 99.9% allows 43.8 minutes of downtime per month. This budget can be 'spent' shipping risky, innovative features."
                },
                {
                    "type": "visual",
                    "title": "The Error Budget Innovation Balance",
                    "code": """graph TD
  subgraph ErrorBudgetGate ["Monthly 99.9% SLO Error Budget: 43.8 Minutes"]
    BUDGET{"Error Budget Status"}
  end
  subgraph GreenPolicy ["Budget Healthy (> 15 min remaining)"]
    SPEED["Ship Fast! Deploy Experimental Features & Canaries 🚀"]
  end
  subgraph ExhaustedPolicy ["Budget Depleted (<= 0 min remaining)"]
    FREEZE["Feature Freeze! 100% Focus on Stability & Bug Remediation 🛡️"]
  end
  BUDGET -->|"Healthy"| SPEED
  BUDGET -->|"Exhausted"| FREEZE
  style ErrorBudgetGate fill:#0f172a,stroke:#3b82f6
  style GreenPolicy fill:#064e3b,stroke:#10b981
  style ExhaustedPolicy fill:#3f1a1a,stroke:#ef4444"""
                },
                {
                    "type": "code_lab",
                    "title": "SRE Error Budget & Downtime Calculator",
                    "instructions": "Implement `calculate_error_budget(slo_percent, days, actual_downtime_minutes)` computing allowable downtime and remaining error budget.",
                    "starter_code": """def calculate_error_budget(slo_percent: float, days: int, actual_downtime_minutes: float) -> dict:
    \"\"\"
    Compute SRE Error Budget.
    Total minutes = days * 24 * 60
    Allowable downtime = Total minutes * (1.0 - (slo_percent / 100.0))
    Remaining budget = Allowable downtime - actual_downtime_minutes
    
    Returns dict:
      - 'allowable_downtime_min': float (rounded to 2 decimals)
      - 'remaining_budget_min': float (rounded to 2 decimals)
      - 'budget_exhausted': bool (True if remaining_budget_min <= 0)
    \"\"\"
    # TODO: Implement budget calculator
    pass
""",
                    "solution_code": """def calculate_error_budget(slo_percent: float, days: int, actual_downtime_minutes: float) -> dict:
    total_minutes = days * 24 * 60
    unavailability_fraction = 1.0 - (slo_percent / 100.0)
    allowable = total_minutes * unavailability_fraction
    remaining = allowable - actual_downtime_minutes
    
    return {
        'allowable_downtime_min': round(allowable, 2),
        'remaining_budget_min': round(remaining, 2),
        'budget_exhausted': remaining <= 0
    }
""",
                    "test_code": """# 30-day window with 99.9% SLO
# Total minutes = 43200. Allowable downtime = 43.2 minutes
res1 = calculate_error_budget(99.9, 30, 10.0)
assert res1['allowable_downtime_min'] == 43.2
assert res1['remaining_budget_min'] == 33.2
assert res1['budget_exhausted'] is False

# Outage consumed 50 minutes -> budget exhausted
res2 = calculate_error_budget(99.9, 30, 50.0)
assert res2['remaining_budget_min'] == -6.8
assert res2['budget_exhausted'] is True
print("SRE Error Budget tests passed successfully!")
""",
                    "why_works": "**Why This Solution Works:**\nError budgets align incentives between Product (who wants speed) and SRE (who wants stability). When the budget is positive, product teams deploy rapidly; when an outage exhausts the budget, feature releases freeze and the team focuses 100% on resilience."
                }
            ]
        },
        {
            "title": "Module 4: The 100% Software Engineering Mastery Capstone",
            "blocks": [
                {
                    "type": "markdown",
                    "content": "From the 1968 NATO conference in Garmisch to modern cloud-native Site Reliability Engineering, software engineering has transformed from an ad-hoc craft into a rigorous, quantitative discipline."
                },
                {
                    "type": "concept",
                    "title": "The Engineering Synthesis",
                    "content": "- **Process:** Agile, Scrum, and Kanban calibrate team velocity and eliminate Lean waste.\n- **Requirements:** FURPS+, INVEST, and IEEE 830 SRS create unambiguous, traceable blueprints.\n- **Architecture:** SOLID principles, Gang of Four patterns, and Hexagonal Ports & Adapters isolate domain logic from transient frameworks.\n- **Verification:** Unit test pyramids, black-box BVA, and white-box MC/DC coverage guarantee behavioral correctness.\n- **Reliability:** Git DAGs, automated CI/CD pipelines, and SRE error budgets sustain operational availability in high-stakes production systems."
                },
                {
                    "type": "interactive",
                    "title": "Curriculum Capstone Challenge",
                    "question": "What is the primary defining characteristic of an engineering discipline compared to craft programming?",
                    "options": [
                        "Memorizing syntax rules in a single language.",
                        "The application of systematic, disciplined, and quantifiable approaches supported by empirical measurement, rigorous verification, and professional ethics.",
                        "Working without sleep during project deadlines.",
                        "Building software exclusively with microservices."
                    ],
                    "answer": 1,
                    "explanation": "**Why this is Correct:**\nAs codified in IEEE 610.12 and demonstrated across all 25 cases of this lab, true **Software Engineering** is defined by systematic methodologies, quantifiable metrics, continuous verification, and ethical stewardship of systems that humanity depends on."
                },
                {
                    "type": "fill_in_the_blank",
                    "title": "Final Graduation Challenge",
                    "question": "The foundational quality of software architecture that enables continuous adaptation without systemic collapse is conceptual _____.\n\nAnswer: _____",
                    "answer": "Integrity",
                    "alternatives": ["Integrity", "integrity", "Conceptual Integrity"],
                    "explanation": "**Why Integrity is Correct:**\nFred Brooks concluded: *'Conceptual integrity is the most important consideration in system design.'* Systems with conceptual integrity remain elegant, understandable, and maintainable across decades."
                }
            ]
        }
    ]
}

print(f"Loaded {len(PART5_CASES)} cases for Part 5 (Cases 20-24).")

with open('/Users/aadarshamahato/Downloads/LEARNING_PLATFORM/se_story_lab/cases_part5.json', 'w', encoding='utf-8') as f:
    json.dump(PART5_CASES, f, indent=4)
