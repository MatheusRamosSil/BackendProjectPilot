FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED=1
COPY requirements.txt requirements.txt
COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt