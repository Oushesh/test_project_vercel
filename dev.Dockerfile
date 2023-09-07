# syntax=docker/dockerfile:1
FROM python:3.8.9
ARG PORT=8000
LABEL maintainer="oushesh"
ENV PYTHONUNBUFFERED 1

WORKDIR /test_project
COPY requirements_old.txt /test_project/


RUN apt update && \
	apt install build-essential && \
	rm -rf /var/cache/apk/* && \
	pip install --upgrade pip && \
	pip install --no-cache-dir -r requirements_old.txt

COPY . /test_proejct/

RUN chmod a+x /test_project/dev-docker-entrypoint.sh
ENTRYPOINT ["/test_project/dev-docker-entrypoint.sh"]

