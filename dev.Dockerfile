# syntax=docker/dockerfile:1
FROM python:3.8.9
ARG PORT=8000
LABEL maintainer="oushesh"
ENV PYTHONUNBUFFERED 1

WORKDIR /start_project
COPY requirements.txt /start_project/

RUN apt update && \
	apt install build-essential && \
	rm -rf /var/cache/apk/* && \
	pip install --upgrade pip && \
	pip install --no-cache-dir -r requirements.txt

COPY . /start_project/

RUN chmod a+x /start_project/dev-docker-entrypoint.sh
ENTRYPOINT ["/start_project/dev-docker-entrypoint.sh"]