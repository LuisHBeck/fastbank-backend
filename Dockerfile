FROM python:3.11.3-alpine3.18

LABEL mantainer="github.com/LuisHBeck"

ENV PYTHONUNBUFFERED 1

ADD "https://www.random.org/cgi-bin/randbyte?nbytes=10&format=h" skipcache

WORKDIR /code

COPY requirements.txt /code

EXPOSE 8000

RUN pip install -r requirements.txt

COPY . /code