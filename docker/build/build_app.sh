#!/bin/bash

INPUT_VERSION=$1;

if [ -z "${INPUT_VERSION}" ]; then
    INPUT_VERSION=latest;
fi

VERSION=$(git rev-parse HEAD)
BASE_IMAGE_VERSION=${INPUT_VERSION}
SERVER=gadtakoi/ursamajor


docker build -f app/Dockerfile -t app_${VERSION} -t app_latest ../../ --build-arg VERSION=${BASE_IMAGE_VERSION}

docker tag app_${VERSION} ${SERVER}:app_${VERSION}
docker push ${SERVER}:app_${VERSION}

docker tag app_latest ${SERVER}:app_latest
docker push ${SERVER}:app_latest
