FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project, including templates/ and static/.
COPY . /app

# Fail during build if the required Flask templates were not uploaded.
RUN test -f /app/app.py \
 && test -f /app/templates/index.html \
 && test -f /app/templates/base.html \
 && test -d /app/static

EXPOSE 10000

CMD ["sh", "-c", "exec gunicorn --bind 0.0.0.0:${PORT:-10000} --workers 1 --threads 4 --timeout 120 app:app"]
