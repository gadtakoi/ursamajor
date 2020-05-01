FROM python:3.8.2
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -y vim htop

RUN apt-get upgrade -y \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get install -y libcurl4-openssl-dev libssl-dev

RUN mkdir /docker
RUN mkdir /docker/config
ADD requirements.txt /docker/config/
RUN pip install --upgrade pip
RUN pip install -r /docker/config/requirements.txt  --upgrade
