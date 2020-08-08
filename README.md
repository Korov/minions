# Minions

demo项目

## 开发环境

### 打包

首先进入项目路径下，执行以下命令

```bash
#windows系统
.\gradlew build -x test
#linux系统
./gradlew build -x test
```

### 启动mysql

开发环境只会启动mysql

```bash
#windows
docker-compose -f .\project_files\docker-compose-dev.yaml build
docker-compose -f .\project_files\docker-compose-dev.yaml up -d
docker-compose -f .\project_files\docker-compose-dev.yaml ps
docker-compose -f .\project_files\docker-compose-dev.yaml stop
docker-compose -f .\project_files\docker-compose-dev.yaml rm

#linux
docker-compose -f ./project_files/docker-compose-dev.yaml build
docker-compose -f ./project_files/docker-compose-dev.yaml up -d
docker-compose -f ./project_files/docker-compose-dev.yaml ps
docker-compose -f ./project_files/docker-compose-dev.yaml stop
docker-compose -f ./project_files/docker-compose-dev.yaml rm
```

等待一段时间之后进入`localhost:8080/demo/get/1`查看服务是否正常启动

## 测试环境

### 打包

首先进入项目路径下，执行以下命令

```bash
#windows系统
.\gradlew build -x test -Dprofile=test
#linux系统
./gradlew build -x test -Dprofile=test
```

测试环境会启动所有服务

```
#windows
docker-compose -f .\project_files\docker-compose-test.yaml build
docker-compose -f .\project_files\docker-compose-test.yaml up -d
docker-compose -f .\project_files\docker-compose-test.yaml ps
docker-compose -f .\project_files\docker-compose-test.yaml stop
docker-compose -f .\project_files\docker-compose-test.yaml rm

#linux
docker-compose -f ./project_files/docker-compose-test.yaml build
docker-compose -f ./project_files/docker-compose-test.yaml up -d
docker-compose -f ./project_files/docker-compose-test.yaml ps
docker-compose -f ./project_files/docker-compose-test.yaml stop
docker-compose -f ./project_files/docker-compose-test.yaml rm
```

