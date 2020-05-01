FROM nginx:1.18

RUN apt-get update \
    && apt-get install -y vim htop

RUN apt-get upgrade -y \
    && apt-get autoremove -y \
    && apt-get clean

RUN rm -rf /var/lib/apt/lists/*

