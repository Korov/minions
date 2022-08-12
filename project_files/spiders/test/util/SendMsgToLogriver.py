import json
import time

from loguru import logger

from minions_spider.util import kafka_producer

logger.add('test.log', rotation="100 MB",
           format="{time:YYYY-MM-DD HH:mm:ss.SSS} - {thread.name} - {file} - {level} - "
                  "{name}:{function}:{line} {message}",
           level="INFO")

servers = "192.168.1.19:9092"

message1 = '{"appname":"zl","key":"zl_suppression","src_port":"3306","dst_port":"145","ids.src_ip":"120.168.1.233","ids.dst_ip": "210.18.1.121", "ids.subject":"HTTP_SQL错误信息泄露_1", "src_city":"tianjing","error_message": "ddos攻击","user": "aaa_user","SystemUpTime": "1650883794364","dest_zone": "237.2.3.21.40","src_zone":"255.255.255.255.3","length":23,"over_time":"2022-05-19 00:00:00 - 2022-05-20 00:00:00","vuln":"CVE-1933","event_name":"ay测试内网网段配置3"}'

message2 = '{"appname":"zl","key":"zl_suppression","src_port":"3306","dst_port":"145","ids.src_ip":"120.168.1.233","ids.dst_ip": "20.18.1.121", "ids.subject":"HTTP_SQL错误信息泄露_1", "src_city":"tianjing","error_message": "ddos攻击","user": "aaa_user","SystemUpTime": "1650883794364","dest_zone": "237.2.3.21.40","src_zone":"255.255.255.255.3","length":23,"over_time":"2022-05-19 00:00:00 - 2022-05-20 00:00:00","vuln":"CVE-1933","event_name":"ay测试内网网段配置3"}'
message3 = '{"appname":"zl","key":"zl_suppression","src_port":"36","dst_port":"5555","ids.src_ip":"120.168.1.233","ids.dst_ip": "210.18.1.121", "ids.subject":"HTTP_SQL错误信息泄露_1", "src_city":"tianjing","error_message": "ddos攻击","user": "aaa_user","SystemUpTime": "1650883794364","dest_zone": "237.2.3.21.40","src_zone":"255.255.255.255.3","length":23,"over_time":"2022-05-19 00:00:00 - 2022-05-20 00:00:00","vuln":"CVE-1933","event_name":"ay测试内网网段配置3"}'
# kafka_producer.send_msg(bootstrap_servers=servers, topic="logriver_siem", key="", msg=message1)
# kafka_producer.send_msg(bootstrap_servers=servers, topic="logriver_siem", key="", msg=message2)
# kafka_producer.send_msg(bootstrap_servers=servers, topic="logriver_siem", key="", msg=message3)

while True:
    timestamp = int(round(time.time() * 1000))

    data1 = json.loads(message1)
    data1['timestamp'] = timestamp

    data2 = json.loads(message2)
    data2['timestamp'] = timestamp

    data3 = json.loads(message3)
    data3['timestamp'] = timestamp

    result = kafka_producer.send_msg(bootstrap_servers=servers, topic="logriver_siem", key="", msg=json.dumps(data1, ensure_ascii=False))
    result = kafka_producer.send_msg(bootstrap_servers=servers, topic="logriver_siem", key="", msg=json.dumps(data1, ensure_ascii=False))
    result = kafka_producer.send_msg(bootstrap_servers=servers, topic="logriver_siem", key="", msg=json.dumps(data1, ensure_ascii=False))
    result = kafka_producer.send_msg(bootstrap_servers=servers, topic="logriver_siem", key="", msg=json.dumps(data1, ensure_ascii=False))
    result = kafka_producer.send_msg(bootstrap_servers=servers, topic="logriver_siem", key="", msg=json.dumps(data1, ensure_ascii=False))
    result = kafka_producer.send_msg(bootstrap_servers=servers, topic="logriver_siem", key="", msg=json.dumps(data1, ensure_ascii=False))
    result = kafka_producer.send_msg(bootstrap_servers=servers, topic="logriver_siem", key="", msg=json.dumps(data1, ensure_ascii=False))
    logger.info(result)
    # result = kafka_producer.send_msg(bootstrap_servers=servers, topic="logriver_siem", key="", msg=json.dumps(data2, ensure_ascii=False))
    # result = kafka_producer.send_msg(bootstrap_servers=servers, topic="logriver_siem", key="", msg=json.dumps(data2, ensure_ascii=False))
    # logger.info(result)
    # result = kafka_producer.send_msg(bootstrap_servers=servers, topic="logriver_siem", key="", msg=json.dumps(data3, ensure_ascii=False))
    # result = kafka_producer.send_msg(bootstrap_servers=servers, topic="logriver_siem", key="", msg=json.dumps(data3, ensure_ascii=False))
    # logger.info(result)
    logger.info("============================================================================================")
    time.sleep(15)
