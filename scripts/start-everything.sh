#!/bin/sh

if [[ $1 == "" ]] ; then
    echo 'Script usage: sh start-everything.sh <env file directory>'
    exit 0
fi

docker stop $(docker ps -a | grep whrs_db_host | awk '{print $1}')
docker stop $(docker ps -a | grep whrs_server | awk '{print $1}')

docker-compose --env-file $1 up -d