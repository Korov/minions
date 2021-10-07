import telnetlib
from loguru import logger

proxy_list = ['27.191.60.222:3256', '124.205.153.90:80', '124.205.153.90:80']

for proxy in proxy_list:
    try:
        ip_port = proxy.split(":")
        telnetlib.Telnet(ip_port[0], ip_port[1], timeout=3)
        logger.info(f"=========valid proxy:{proxy}")
    except Exception as e:
        logger.info(f"*********invalid proxy:{proxy}")
        pass
