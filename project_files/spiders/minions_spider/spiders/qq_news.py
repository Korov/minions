import copy
import json
from urllib.parse import urlencode

import scrapy

headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "origin": "https://news.qq.com",
    "referer": "https://news.qq.com/",
    "Connection": "keep-alive",
    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="92"',
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
}


class biquge(scrapy.Spider):
    name = "qq_news"
    allowed_domains = ['qq.com']
    custom_settings = {
        # 'ITEM_PIPELINES': {'minions_spider.pipelines.biquge_pipeline': 300},
        'DOWNLOAD_TIMEOUT': 120,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 2,
        'DOWNLOAD_DELAY': 10,
        'AUTOTHROTTLE_ENABLED': True,
        'AUTOTHROTTLE_START_DELAY': 5,
        'AUTOTHROTTLE_MAX_DELAY': 60,
        'AUTOTHROTTLE_TARGET_CONCURRENCY': 1.0
    }

    def start_requests(self):
        urls = [
            "https://i.news.qq.com/trpc.qqnews_web.kv_srv.kv_srv_http_proxy/list?sub_srv_id=24hours&srv_id=pc&offset=120&limit=20&strategy=1&ext={%22pool%22:[%22top%22],%22is_filter%22:7,%22check_type%22:true}"
        ]
        for url in urls:
            yield scrapy.Request(url=url, headers=headers, meta={"offset": copy.deepcopy(0)}, callback=self.parse_news)

    def parse_news(self, response, **kwargs):
        offset = response.meta['offset']
        offset = offset + 20
        body = json.loads(response.body.decode())
        news = body['data']['list']
        if len(news) != 0:
            params = {
                "sub_srv_id": "24hours",
                "srv_id": "pc",
                "offset": offset,
                "limit": 20,
                "strategy": 1,
                "ext": '{"pool":["top"],"is_filter":7,"check_type":true}'
            }
            url = "https://i.news.qq.com/trpc.qqnews_web.kv_srv.kv_srv_http_proxy/list?" + urlencode(params)
            yield scrapy.Request(url=url, headers=headers, meta={"offset": copy.deepcopy(offset)}, callback=self.parse_news)
            for new in news:
                url = new['url']
        self.logger.info(response)
