FROM python:3.11

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /Fit_Library
WORKDIR /Fit_Library

COPY requirements.txt /Fit_Library/

RUN pip install --upgrade pip && pip install -r requirements.txt

ADD . /Fit_Library/

RUN chmod +x ./docker/backend/web-entrypoint.sh
