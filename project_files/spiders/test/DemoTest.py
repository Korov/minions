import time
import uuid

for index in range(0, 100):
    client_id = uuid.uuid1()
    print("client id:%s" % (client_id))
    print("time:%s" % (time.time_ns()))
