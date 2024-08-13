FROM ollama/ollama

RUN mkdir /app

COPY model_pull.sh /app

RUN chmod +x /app/model_pull.sh

RUN ./app/model_pull.sh
