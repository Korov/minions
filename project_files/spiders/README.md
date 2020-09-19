# 安装步骤

## 安装依赖

```
pip install -r requirements.txt
```

## 运行爬虫

运行之前需要修改`minions_spider/settings.py`中的`BOOTSTRAP_SERVERS`为对应的kafka端口

```
scrapy crawl hero
```

# 其他命令

更新依赖文件
pip freeze > requirements.txt

安装依赖
pip install -r requirements.txt

查看当前爬虫
scrapy list
运行指定爬虫
scrapy crawl hero


项目部署
首先开启服务
pip install scrapyd
scrapyd

pip install -r requirements.txt
pip install scrapyd-client
scrapyd-deploy minions_spider -p minions_spider -v v1

更换环境
export SCRAPY_PROJECT=test