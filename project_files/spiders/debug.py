import random
import time

from scrapy import cmdline

# 在Run/Debug Configurations中添加python的debug，设置Script path为当前项目的begin.py，保存之后点击debug按钮就可以debug了
# 也可以在这里直接debug
# scrapy crawl <spider_name>
cmdline.execute('scrapy crawl qq_news'.split())
