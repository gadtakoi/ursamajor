#!/bin/bash

VERSION=1.18
SERVER=gadtakoi/ursamajor

docker build -f nginx/Dockerfile -t nginx_${VERSION} -t nginx_latest ../../

docker tag nginx_${VERSION} ${SERVER}:nginx_${VERSION}
docker tag nginx_latest ${SERVER}:nginx_latest

docker push ${SERVER}:nginx_${VERSION}
docker push ${SERVER}:nginx_latest
