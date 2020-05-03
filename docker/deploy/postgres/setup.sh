#!/bin/bash
docker network create main
docker-compose stop database;
docker-compose up -d database;

