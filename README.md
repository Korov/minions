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
打包之后将各个module中的build中的libs中的jar包放入project_files的libs中

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