#!/bin/bash

VERSION=$(git rev-parse HEAD)
SERVER=gadtakoi/ursamajor

docker build -f base/Dockerfile -t base_${VERSION} -t base_latest ../../
#docker build -f base/Dockerfile -t ursamajor/base:latest ../../
#docker build -f base/Dockerfile -t base ../../


docker tag base_${VERSION} ${SERVER}:base_${VERSION}
#docker tag ursamajor/base:latest ${SERVER}/ursamajor/base:latest
#docker tag ursamajor/base:latest ${SERVER}
#docker tag base ${SERVER}:base


#docker push ${SERVER}/ursamajor/base:${VERSION}
#docker push ${SERVER}/ursamajor/base:latest
docker push ${SERVER}:base_${VERSION}

