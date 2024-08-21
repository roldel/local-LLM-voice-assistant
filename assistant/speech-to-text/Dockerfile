FROM pytorch/pytorch

ENV PIP_NO_CACHE_DIR=off

RUN pip install -U openai-whisper
RUN pip install flask requests

RUN python -c "import whisper; whisper.load_model('base.en')"

COPY . /app