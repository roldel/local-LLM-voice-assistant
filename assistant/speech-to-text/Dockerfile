FROM pytorch/pytorch

RUN pip install -U openai-whisper
RUN pip install flask 
RUN pip install requests

RUN python -c "import whisper; whisper.load_model('base.en')"

COPY . /app


