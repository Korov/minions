from kafka import KafkaProducer
from scrapy.utils.project import get_project_settings

settings = get_project_settings()
producer = KafkaProducer(
    bootstrap_servers = settings.get('BOOTSTRAP_SERVERS')
)

def on_send_success(*args, **kwargs):
    """
    发送成功的回调函数
    :param args:
    :param kwargs:
    :return:
    """
    return args


def on_send_error(*args, **kwargs):
    """
    发送失败的回调函数
    :param args:
    :param kwargs:
    :return:
    """

    return args


def send_msg(topic, key, msg):
    key = str(key).encode('utf-8')
    msg = str(msg).encode('utf-8')
    producer.send(topic, key=key, value=msg).add_callback(on_send_success).add_errback(on_send_error)
