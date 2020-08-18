#!/bin/bash

if [ ! -n "$1" ] || [ ! -n "$2" ];then
  echo "command error, example: ./minions test up"
  exit 1
fi

env=$1
action=$2

if [ ${env} != "dev" -a ${env} != "test" ]
then
  echo "the first value must be dev or test, example: ./minions dev up"
  exit 1
fi

if [ ${action} != "up" -a ${action} != "stop" ]
then
  echo "the second value must be up or stop"
  exit 1
fi

if [ ${env} = "dev" ]
then
  if [ ${action} = "up" ]
  then
    docker-compose -f ./project_files/docker-compose-dev.yaml stop
    docker-compose -f ./project_files/docker-compose-dev.yaml rm --force
    docker-compose -f ./project_files/docker-compose-dev.yaml build
    docker-compose -f ./project_files/docker-compose-dev.yaml up -d
    docker-compose -f ./project_files/docker-compose-dev.yaml ps
  else
    docker-compose -f ./project_files/docker-compose-dev.yaml stop
    docker-compose -f ./project_files/docker-compose-dev.yaml rm --force
    docker-compose -f ./project_files/docker-compose-dev.yaml ps
  fi
elif [ ${env} = "test" ]
then
  if [ ${action} = "up" ]
  then
    docker network rm minions
    docker network create --driver bridge --subnet 172.31.0.0/16 minions
    docker-compose -f ./project_files/docker-compose-test.yaml stop
    docker-compose -f ./project_files/docker-compose-test.yaml rm --force
    docker rmi demo:1.0
    rm -rf ./project_files/libs/
    docker run --rm -u gradle -v "$PWD":/home/gradle/project -w /home/gradle/project gradle:6.5.1-jdk11 gradle build -x test
    docker-compose -f ./project_files/docker-compose-test.yaml build
    docker-compose -f ./project_files/docker-compose-test.yaml up -d
    docker-compose -f ./project_files/docker-compose-test.yaml ps
  else
    docker-compose -f ./project_files/docker-compose-test.yaml stop
    docker-compose -f ./project_files/docker-compose-test.yaml rm --force
    docker-compose -f ./project_files/docker-compose-test.yaml ps
    docker network rm minions
  fi
fi