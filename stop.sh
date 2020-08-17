#!/bin/bash

env=$1
if [[ ${env} = "dev" ]] || $env
then
  docker-compose -f ./project_files/docker-compose-dev.yaml stop
  docker-compose -f ./project_files/docker-compose-dev.yaml rm --force
  docker-compose -f ./project_files/docker-compose-dev.yaml ps
elif [[ ${env} = "test" ]]
then
  docker-compose -f ./project_files/docker-compose-test.yaml stop
  docker-compose -f ./project_files/docker-compose-test.yaml rm --force
  docker rmi demo:1.0
  docker-compose -f ./project_files/docker-compose-test.yaml ps
fi