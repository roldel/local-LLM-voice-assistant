FROM python:slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PIP_NO_CACHE_DIR=off


RUN mkdir /app
#WORKDIR /app
COPY . /app

RUN apt update
RUN apt install -y ffmpeg
RUN pip3 install vosk

# RUN mkdir -p /app/browser-interface/media


RUN pip install -r /app/requirements.txt

RUN python /app/browser-interface/manage.py makemigrations
RUN python /app/browser-interface/manage.py migrate

CMD ["python", "/app/browser-interface/manage.py", "runserver", "0.0.0.0:8000"]


#RUN vosk-transcriber -i test.mp4 -o test.txt