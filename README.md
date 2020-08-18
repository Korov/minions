# Minions

demo项目

## 打包

首先进入项目路径下，执行以下命令

```bash
#windows系统
.\gradlew build -x test
#linux系统
./gradlew build -x test
```

## 开发环境

开发环境只会启动mysql

```bash
#windows
docker-compose -f .\project_files\docker-compose-dev.yaml build
docker-compose -f .\project_files\docker-compose-dev.yaml up -d
docker-compose -f .\project_files\docker-compose-dev.yaml ps
docker-compose -f .\project_files\docker-compose-dev.yaml stop
docker-compose -f .\project_files\docker-compose-dev.yaml rm

#linux
./minions dev up
./minions dev stop
```

## 测试环境

启动测试环境之前需要打包生成最新的服务器jar包，测试环境会启动所有服务

```bash
#windows
docker-compose -f .\project_files\docker-compose-test.yaml build
docker-compose -f .\project_files\docker-compose-test.yaml up -d
docker-compose -f .\project_files\docker-compose-test.yaml ps
docker-compose -f .\project_files\docker-compose-test.yaml stop
docker-compose -f .\project_files\docker-compose-test.yaml rm

#linux
./minions test up
./minions test stop
```

等待一段时间之后进入`localhost:8080/demo/get/1`查看服务是否正常启动

# 技术

## Spring Boot

版本：2.3.2.RELEASE

## JDK

openjdk 11.0.7

## Gradle

版本：6.5.1

## 数据库

### PostgresSQL

帐号：postgres

密码：postgres

端口：5432

### MongoDB

帐号：admin

密码：mongo

端口：27017

### Redis

密码：redis

端口：6379

## Zookeeper

端口：2181

## Kafka

端口9092

