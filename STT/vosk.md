

Dockerfile
```Dockerfile
FROM python:slim

RUN pip3 install vosk
RUN apt update
RUN apt install ffmpeg
RUN vosk-transcriber -i test.mp4 -o test.txt
```


sh
```sh
pip3 install vosk
apt update
apt install ffmpeg
vosk-transcriber -i test.mp3 -o test.txt
```
