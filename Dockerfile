FROM python:3.13
LABEL authors="lkh"

RUN mkdir /app

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.cargo/bin:$PATH"

COPY . /app/
RUN uv sync

EXPOSE 7878

CMD ["gunicorn", "WebDjango:application", "--bind", "0.0.0.0:7878"]
