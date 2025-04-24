# syntax=docker/dockerfile:1
FROM python:3.9-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1
WORKDIR /code

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/* \

COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/