FROM python:3.7-alpine
MAINTAINER umairkhancis

# This won't let the python buffer the output to avoid complexities when running in docker conatiner.
ENV PYTHONUNBUFFERED 1

# Seting up the working directory.
WORKDIR backend

COPY . .

# Install the dependencies.
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev
RUN pip install -r requirements.txt
RUN apk del build-deps

# Use a new user to use application to avoid using default root user; for security purposes.
RUN adduser -D appuser
USER appuser

# Switch to src directory and start server.
WORKDIR src