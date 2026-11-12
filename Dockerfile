FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PLATFORM_AUTH_MODE=multiuser \
    PLATFORM_DB_PATH=/app/data/platform.db \
    RUNNER_MAX_CONCURRENCY=4

RUN apt-get update \
    && apt-get install -y --no-install-recommends g++ \
    && rm -rf /var/lib/apt/lists/*

RUN useradd --create-home --uid 10001 --shell /bin/sh appuser

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY .streamlit/ .streamlit/
COPY app.py core_loader.py master_ui.py runners.py unified_persistence.py ./
COPY dbms_story_lab/ dbms_story_lab/
COPY ai_story_lab/ ai_story_lab/
COPY se_story_lab/ se_story_lab/
COPY cloud_story_lab/ cloud_story_lab/
COPY oop_story_lab/ oop_story_lab/
COPY dsa_story_lab/ dsa_story_lab/
COPY sd_story_lab/ sd_story_lab/
COPY ip_story_lab/ ip_story_lab/

RUN mkdir -p /app/data && chown -R appuser:appuser /app

USER appuser

EXPOSE 8501

HEALTHCHECK --interval=30s --timeout=5s --start-period=20s --retries=3 \
  CMD sh -c 'python -c "import os, urllib.request; urllib.request.urlopen(\"http://127.0.0.1:\" + os.environ.get(\"PORT\", \"8501\") + \"/_stcore/health\", timeout=3)"' || exit 1

CMD ["sh", "-c", "exec streamlit run app.py --server.port=${PORT:-8501} --server.address=0.0.0.0 --server.headless=true --server.fileWatcherType=none"]
