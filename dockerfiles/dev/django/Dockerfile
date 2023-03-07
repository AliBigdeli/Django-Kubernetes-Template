FROM python:3.9-slim-buster

LABEL maintainer="bigdeli.ali3@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt

COPY ./core/ .

# adding access to port 8000
EXPOSE 8000

# RUN python manage.py check_database && \ 
#     yes | python manage.py makemigrations  && \
#     yes | python manage.py migrate  && \
#     python manage.py runserver 0.0.0.0:8000