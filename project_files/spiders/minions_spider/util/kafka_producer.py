from kafka import KafkaProducer


def on_send_success(*args, **kwargs):
    print("send success")
    return args


def on_send_error(*args, **kwargs):
    print("send failed")
    return args


def send_msg(server="korov-linux.org:9092", topic="test", key="demo-key", msg="demo-msg"):
    producer = KafkaProducer(bootstrap_servers=server)
    key = str(key).encode('utf-8')
    msg = str(msg).encode('utf-8')
    future = producer.send(topic, key=key, value=msg).add_callback(on_send_success).add_errback(on_send_error)
    result = future.get(timeout=60)
    print(result)
