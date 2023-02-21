# syntax=docker/dockerfile:1
FROM python:3.8
ENV PYTHONUNBUFFERED=1
RUN apt-get update && apt-get -y dist-upgrade
COPY . /whrs/