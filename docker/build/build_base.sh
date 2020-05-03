#!/bin/bash

VERSION=$(git rev-parse HEAD)
SERVER=gadtakoi/ursamajor

docker build -f base/Dockerfile -t base_${VERSION} -t base_latest ../../
docker tag base_${VERSION} ${SERVER}:base_${VERSION}
docker push ${SERVER}:base_${VERSION}

