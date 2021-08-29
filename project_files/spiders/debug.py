from scrapy import cmdline

# 在Run/Debug Configurations中添加python的debug，设置Script path为当前项目的begin.py，保存之后点击debug按钮就可以debug了
# 也可以在这里直接debug
# scrapy crawl <spider_name>
# cmdline.execute('scrapy crawl biquge'.split())

import redis

r = redis.Redis(host='korov.myqnapcloud.cn', port=6379, db=0)
result = r.sadd('set_test', 'bar1', 'bar2')
print(result)
values = r.smembers('set_test')
print(values)
for value in values:
    print(value.decode())

temp = 'bar2'
if temp.encode() in values:
    print("in")
else:
    print("not in")

result = r.sismember('set_test','bar1')
print(result)

result = r.srem('set_test', 'bar1')
print(result)
result = r.sismember('set_test','bar1')
print(result)