FROM python:3.8

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

COPY . /drp-flask

WORKDIR /drp-flask

RUN python3.8 -m venv venv
RUN . venv/bin/activate
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

WORKDIR /drp-flask

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV FLASK_APP=artplatform/app.py
ENV FLASK_ENV=development
ENV FLASK_RUN_HOST=0.0.0.0

CMD flask run --host=0.0.0.0 --port=${PORT:-5000}
