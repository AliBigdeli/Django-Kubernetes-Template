# pull official base image
FROM python:3.9-alpine

# maintainers info
LABEL maintainer="bigdeli.ali3@gmail.com"

# installing dependencies
RUN apk add --update --virtual .build-deps \
    build-base \
    postgresql-dev \
    python3-dev \
    libpq


# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt


# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy project
COPY ./core .

# adding access to port 8000
EXPOSE 8000

# collecting static files and run the project
RUN python manage.py collectstatic --no-input && \
    python manage.py migrate && \
    gunicorn --bind 0.0.0.0:8000 core.wsgi:application




