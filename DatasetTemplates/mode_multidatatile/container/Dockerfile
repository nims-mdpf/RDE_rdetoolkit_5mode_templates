FROM python:3.13-slim

COPY pip.conf /etc/pip.conf

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY main.py /app
COPY modules/ /app/modules/
