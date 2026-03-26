FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    sqlite3 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1
ENV OPENVAULT_DB=/app/data/openvault.db
ENV OPENVAULT_PORT=5000

EXPOSE 5000

RUN mkdir -p /app/data

CMD ["python", "-m", "app.main", "--host", "0.0.0.0", "--port", "5000"]
