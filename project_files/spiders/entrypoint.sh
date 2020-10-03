#!/usr/bin/env bash

WORK_DIR="/spider"
cd ${WORK_DIR}

scrapyd

scrapyd-deploy minions_spider -p minions_spider -v v1
