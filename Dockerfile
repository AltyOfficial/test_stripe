FROM python:3.10-slim

WORKDIR /project

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt --no-cache-dir

COPY project/stripe_api/ .

COPY project/ .