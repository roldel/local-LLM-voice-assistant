FROM python:alpine

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PIP_NO_CACHE_DIR=off

RUN mkdir /app

RUN mkdir -p /shared/input_audio

COPY requirements.txt /app

RUN pip install -r /app/requirements.txt

COPY . /app

RUN python /app/manage.py migrate