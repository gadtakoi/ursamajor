#!/bin/bash

INPUT_VERSION=$1;

if [ -z "${INPUT_VERSION}" ]; then
    INPUT_VERSION=latest;
fi

export VERSION=${INPUT_VERSION};

docker-compose pull ursamajor_app_1;
docker-compose pull ursamajor_nginx;

