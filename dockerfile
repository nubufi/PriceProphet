FROM python:3.11-slim

WORKDIR /app
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN git config --global credential.helper store
COPY app .

CMD ["python", "main.py"]
