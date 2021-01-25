from python:3.6

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

copy requirements.txt .
run pip install -r requirements.txt

COPY . .