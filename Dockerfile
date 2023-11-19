FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    git \
    ffmpeg \
    libsm6 \
    libxext6

RUN pip install --upgrade pip

COPY apps/ apps/

WORKDIR /apps

RUN pip install --no-cache-dir -r requirements.txt

CMD streamlit run Home.py --server.port 8080
