FROM python:3.6.2
MAINTAINER Ronald Theodoro<ronaldtheodoro@gmail.com>
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/