START = 10
END = 30
SERVER_HOST = "nas.korov.org"

# Mongo
MONGO_URL = "mongodb://spider:spider@%s:27017/spider" % (SERVER_HOST)

# Redis
REDIS_HOST = SERVER_HOST
REDIS_PORT = 6379
REDIS_USER = "root"
REDIS_PASSWORD = "zl7636012086"

PROXY_SET = {'136.228.233.20:8010', '136.228.221.22:8010', '136.228.200.22:8009', '60.191.11.249:3128',
             '200.54.22.74:80', '179.157.4.228:80', '112.14.47.6:52024', '218.75.69.50:57903'}
