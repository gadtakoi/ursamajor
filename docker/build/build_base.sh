#!/bin/bash

#VERSION=$(git rev-parse HEAD)
SERVER=gadtakoi/ursamajor

#docker build -f base/Dockerfile -t ursamajor/base:${VERSION} -t ursamajor/base:latest ../../
#docker build -f base/Dockerfile -t ursamajor/base:latest ../../
docker build -f base/Dockerfile -t base ../../


docker tag ursamajor/base:${VERSION} ${SERVER}/ursamajor/base:${VERSION}
#docker tag ursamajor/base:latest ${SERVER}/ursamajor/base:latest
#docker tag ursamajor/base:latest ${SERVER}
docker tag base ${SERVER}:base


#docker push ${SERVER}/ursamajor/base:${VERSION}
#docker push ${SERVER}/ursamajor/base:latest
docker push ${SERVER}:base

