FROM python:3
ENV PYTHONUNBUFFERED 1
RUN apt-get update -y && apt-get upgrade -y
RUN mkdir /code
ADD requirements.txt /code/
WORKDIR /code
RUN pip install -r requirements.txt
COPY . /code/
