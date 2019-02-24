FROM python:3
ENV PYTHONUNBUFFERED 1
RUN apt-get update -y && apt-get upgrade -y
RUN mkdir /code
RUN pip install pipenv
COPY Pipfile /code/
WORKDIR /code
RUN pipenv lock -r > requirements.txt
RUN pipenv lock -r -d > requirements-dev.txt
RUN pip install -r requirements.txt
RUN pip install -r requirements-dev.txt
COPY . /code/