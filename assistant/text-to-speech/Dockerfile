FROM python:alpine

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PIP_NO_CACHE_DIR=off

RUN apk add espeak
RUN pip install flask
RUN pip install requests

RUN mkdir -p /shared/output_audio

COPY . /app