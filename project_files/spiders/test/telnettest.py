import telnetlib

import requests
from loguru import logger

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": 'max-age=0',
    "Connection": "keep-alive",
    "sec-ch-ua": '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
}

proxy_list = ['222.66.202.6:80']

for proxy in proxy_list:
    try:
        ip_port = proxy.split(":")
        telnetlib.Telnet(ip_port[0], ip_port[1], timeout=3)

        proxies = {"http": f"http://{proxy}", "https": f"https://{proxy}"}
        response = requests.get(url="http://icanhazip.com", proxies=proxies, headers=headers)
        logger.info(response)
        if response.status_code == 200:
            logger.info(response.status_code)
            if ip_port[0] == str(response.text.strip()):
                logger.info(f"=========valid proxy:{proxy}")
    except Exception as e:
        logger.info(f"*********invalid proxy:{proxy}")
        pass
