FROM python:3.13
LABEL authors="lkh"

RUN mkdir /app

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/root/.local/bin:$PATH"

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

COPY . /app/
RUN uv sync --frozen --no-cache

EXPOSE 7878

CMD ["gunicorn", "WebDjango:application", "--bind", "0.0.0.0:7878"]
