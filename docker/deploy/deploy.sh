#!/bin/bash

INPUT_VERSION=$1;

if [ -z "${INPUT_VERSION}" ]; then
    INPUT_VERSION=latest;
fi

export VERSION=${INPUT_VERSION};

docker-compose stop ursamajor_app_1;
docker-compose up -d ursamajor_app_1;

docker-compose stop ursamajor_app_2;
docker-compose up -d ursamajor_app_2;
