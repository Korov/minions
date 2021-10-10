START = 10
END = 30
SERVER_HOST = "nas.korov.org"

# Mongo
MONGO_URL = "mongodb://spider:spider@%s:27017/spider" % (SERVER_HOST)

# Redis
REDIS_HOST = SERVER_HOST
REDIS_PORT = 6379
REDIS_USER = "root"
REDIS_PASSWORD = "***"

PROXY_SET = {'101.99.95.54:80', '1.55.113.222:9999', '103.134.30.137:8080'}
