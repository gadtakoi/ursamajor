#!/bin/bash

INPUT_VERSION=$1;

if [ -z "${INPUT_VERSION}" ]; then
    INPUT_VERSION=latest;
fi

export VERSION=${INPUT_VERSION};

docker-compose up -d;

DATE=`date '+%Y-%m-%d %H:%M:%S'`
echo  'START '${DATE}' '${INPUT_VERSION} >> ../recent_work_hashes.txt
