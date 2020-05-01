#!/bin/bash

docker-compose stop;

DATE=`date '+%Y-%m-%d %H:%M:%S'`
echo  'STOP '${DATE} >> ../recent_work_hashes.txt
