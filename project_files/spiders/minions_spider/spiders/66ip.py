import copy
import telnetlib

from loguru import logger
import logging

import scrapy


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": 'max-age=0',
    "Connection": "keep-alive",
    # "Cookie": "obj=1; clickbids=39094",
    "Host": "www.66ip.cn",
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

log = logging.getLogger(__name__)

class biquge(scrapy.Spider):
    name = "66ip"
    custom_settings = {
        # 'ITEM_PIPELINES': {'minions_spider.pipelines.biquge_pipeline': 300},
        'DOWNLOAD_TIMEOUT': 120,
        'CONCURRENT_REQUESTS': 32,
        # 'CONCURRENT_REQUESTS_PER_DOMAIN': 50,
        'DOWNLOAD_DELAY': 0,
        # 'AUTOTHROTTLE_ENABLED': True,
        # 'AUTOTHROTTLE_START_DELAY': 5,
        # 'AUTOTHROTTLE_MAX_DELAY': 60,
        # 'AUTOTHROTTLE_TARGET_CONCURRENCY': 1.0
    }

    def start_requests(self):
        urls = [
            "http://www.66ip.cn/2.html",
        ]
        for url in urls:
            yield scrapy.Request(url=url, headers=headers, meta={"offset": copy.deepcopy(0)}, callback=self.parse_ip)

    def parse_ip(self, response, **kwargs):
        ip_list = response.selector.xpath("//div[@align='center']/table/tr")[1:]
        for ips in ip_list:
            ip = ips.xpath("./td[1]/text()")[0].extract()
            port = ips.xpath("./td[1]/text()")[0].extract()
            try:
                telnetlib.Telnet(ip, port, timeout=3)
                logger.info(f"=========valid ip:port = {ip}:{port}")
                log.info(f"=========valid ip:port = {ip}:{port}")
            except Exception as e:
                log.info(f"*********invalid ip:{ip}, port:{port}")
                pass

        all_page = response.selector.xpath("//div[@id='PageList']/a")
        next_page = all_page[len(all_page) - 1]
        next_page_url = f"http://www.66ip.cn{str(next_page.attrib['href'])}"
        content = next_page.xpath('./text()').extract()[0]
        if "»" == content:
            # logger.info(f"{next_page_url}, {content}")
            yield scrapy.Request(url=next_page_url, headers=headers, callback=self.parse_ip)
        else:
            logger.info("over")

