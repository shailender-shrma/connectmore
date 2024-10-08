FROM python:3.11-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/conuser

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . usr/src/conuser

COPY . .

