START = 10
END = 30
SERVER_HOST = "nas.korov.org"

# Mongo
MONGO_URL = "mongodb://spider:spider@%s:27017/spider" % (SERVER_HOST)

# Redis
REDIS_HOST = SERVER_HOST
REDIS_PORT = 6379
REDIS_USER = "REDIS_USER"
REDIS_PASSWORD = "REDIS_PASSWORD"

proxy_list = ['124.205.153.90:80']
