#!/bin/bash

env=$1
if [[ ${env} = "dev" ]] || $env
then
  docker-compose -f ./project_files/docker-compose-dev.yaml stop
  docker-compose -f ./project_files/docker-compose-dev.yaml rm --force
  docker-compose -f ./project_files/docker-compose-dev.yaml build
  docker-compose -f ./project_files/docker-compose-dev.yaml up -d
  docker-compose -f ./project_files/docker-compose-dev.yaml ps
elif [[ ${env} = "test" ]]
then
  docker-compose -f ./project_files/docker-compose-test.yaml stop
  docker-compose -f ./project_files/docker-compose-test.yaml rm --force
  docker rmi demo:1.0
  rm -rf ./project_files/libs/
  ./gradlew clean build -x test
  docker-compose -f ./project_files/docker-compose-test.yaml build
  docker-compose -f ./project_files/docker-compose-test.yaml up -d
  docker-compose -f ./project_files/docker-compose-test.yaml ps
fi