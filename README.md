# Engineering Story Labs

Unified, interactive computer science & systems engineering workbench spanning **8 engineering disciplines**, **147 incident-driven case studies**, and **643 interactive modules**.

## Curriculum Tracks

| Track | Discipline | Highlights |
| :--- | :--- | :--- |
| 01 | **Database Management Systems (DBMS)** | Interactive SQLite sandboxes, ACID anomaly labs, query plan verification |
| 02 | **Artificial Intelligence & Machine Learning** | Math foundations, NumPy/scikit-learn labs, architectural diagnostics |
| 03 | **Software Engineering & Processes** | Requirements engineering, UML/DFD modeling, testing & CI/CD investigations |
| 04 | **Cloud Computing & Distributed Storage** | AWS decoupling, virtualization, MapReduce labs, sustainability scenarios |
| 05 | **Object-Oriented Programming (C++17)** | Live `g++` compiler sandbox, memory layout grids, vtable/RAII traces |
| 06 | **Data Structures & Algorithms (DSA)** | Theory visualizers + 19 dual-language Python 3 / C++17 Online Judges |
| 07 | **System Design (HLD & LLD)** | Capacity math calculators, rate limiters, consistent hashing & architecture labs |
| 08 | **Image Processing** | Sampling, 2-D FFT & homomorphic filters, Wiener restoration, HSI, Wavelets, morphology, MPEG/SVC |

## Production Architecture & Security Controls

- **Sandboxed Execution (`runners.py`):**
  - Static AST/regex safety gates block OS, filesystem, subprocess, network, and dynamic evaluation primitives (`os`, `subprocess`, `socket`, `open`, `eval`, `exec`, `system()`).
  - Subprocesses execute inside isolated temporary directories with scrubbed environment variables, POSIX `setsid()` + `RLIMIT_CPU`/`RLIMIT_FSIZE`/`RLIMIT_CORE`/`RLIMIT_NOFILE`, strict timeouts, output truncation, path masking (`<sandbox>`), process-group `killpg` cleanup, and a global semaphore (`RUNNER_MAX_CONCURRENCY`).
  - SQLite labs enforce `set_authorizer` (blocking `ATTACH`, `DETACH`, `load_extension`, and `writable_schema`) plus a `2.5s` `set_progress_handler` query deadline.
- **Persistent Multi-User State (`unified_persistence.py`):**
  - SQLite WAL database (`data/platform.db`) replaces flat shared JSON mutation.
  - Password hashing via `PBKDF2-HMAC-SHA256` (260,000 iterations), constant-time verification, process-wide brute-force lockout, and `HMAC-SHA256` session tokens.
  - Configurable modes via `PLATFORM_AUTH_MODE`: `local` (default local developer profile + optional sign-in), `multiuser` (default in Docker: isolated per-session guest workspaces + accounts), or `required` (full login gate).
- **UI Hardening (`master_ui.py` & `app.py`):**
  - Markdown output sanitization stripping executable tags/event handlers/javascript URIs, HTML escaping on user/case titles, Mermaid `securityLevel: 'strict'`, query-parameter allowlist validation, execution rate limiting, and Streamlit XSRF protection with minimal toolbar and suppressed raw error tracebacks.

## Local Development

```bash
python -m pip install -r requirements.txt
streamlit run app.py --server.port 8501
```

## Testing

```bash
python -m unittest discover -s tests -v
```

## Deployment Options

### 1. Streamlit Community Cloud (Fastest Free Hosting)
1. Push this repository to GitHub (`.gitignore` excludes local DBs/secrets/legacy directories).
2. On [share.streamlit.io](https://share.streamlit.io), select the repo, branch, and main file `app.py`.
3. `requirements.txt` installs Python packages and `packages.txt` installs `g++` for C++ OOP & DSA Online Judge labs.
4. Set App Secrets (`PLATFORM_AUTH_MODE = "multiuser"` and a random `PLATFORM_SECRET_KEY`).

### 2. Render / Railway / Fly.io / Cloud Run (Docker)
- `Dockerfile` supports dynamic `$PORT`, includes `g++` and non-root `appuser`, and exposes `/_stcore/health`.
- On **Render**, connect the repository and use the included `render.yaml` Blueprint (auto-provisions `/app/data` persistent disk, `PLATFORM_SECRET_KEY`, and health checks).

### 3. Self-Hosted VPS (Docker Compose + Nginx TLS)
```bash
cp .env.example .env
# Edit .env and set a 64-char random PLATFORM_SECRET_KEY (openssl rand -hex 32)
docker compose up -d --build
```
Configure TLS termination and WebSocket proxying in front of `127.0.0.1:8501` using `nginx.conf.example`.
