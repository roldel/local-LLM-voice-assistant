FROM python:alpine

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
#ENV PIP_NO_CACHE_DIR=off

RUN mkdir /app

RUN mkdir -p /shared/input_audio
#WORKDIR /app
COPY . /app

# RUN mkdir -p /app/browser-interface/media

RUN pip install -r /app/requirements.txt

RUN python /app/manage.py migrate