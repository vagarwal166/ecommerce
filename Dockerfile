# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /mysite
COPY requirements.txt /mysite/
RUN pip install -r requirements.txt
COPY . /mysite/