

```Dockerfile
FROM python:slim
RUN pip install -U openai-whisper
RUN sudo apt update && sudo apt install ffmpeg
RUN whisper audio.mp3 --model tiny.en
```

```sh
pip install -U openai-whisper
sudo apt update && sudo apt install ffmpeg
whisper audio.mp3 --model tiny.en
```


