FROM python:3.13.11-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

WORKDIR /app

ENV PATH="/app/.venv/bin:$PATH"

COPY pyproject.toml .python-version uv.lock ./
RUN uv sync --locked

COPY ingest_data.py .
COPY taxi_zone_lookup.csv green_tripdata_2025-11.parquet .

ENTRYPOINT ["uv", "run", "python", "ingest_data.py"]
