# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import logging
import random

import redis
import requests
from scrapy import signals
from scrapy.downloadermiddlewares.retry import RetryMiddleware
from scrapy.utils.response import response_status_message

# useful for handling different item types with a single interface
from minions_spider import constant


class MinionsSpiderSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        self.logger.info('Spider opened: %s', spider.name)


class MinionsSpiderDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.redis_db = redis.Redis(host=constant.REDIS_HOST, port=constant.REDIS_PORT, db=1,
                                    username=constant.REDIS_USER,
                                    password=constant.REDIS_PASSWORD)

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        proxy_list = constant.PROXY_SET
        request.meta['proxy'] = 'https://{proxy}'.format(proxy=proxy_list[random.randint(0, 6)])
        self.logger.info('Spider request: %s', request)

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        self.proxy_list = constant.PROXY_SET
        if response.status != 200:
            proxies = self.redis_db.zrangebyscore("proxies:biquge", min=90, max=100, num=10, start=0, withscores=True)
            proxy = proxies[random.randint(0, len(proxies))][0].decode('utf8')
            request.meta['proxy'] = f"https://{proxy}"
            logging.info(f"download with anther ip:{proxy}, response:{response}")
            return request
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        self.logger.info('Spider opened: %s', spider.name)


class BiqugeMiddleware:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.proxy_list = list(constant.PROXY_SET)
        self.start_index = 0
        self.redis_db = redis.Redis(host=constant.REDIS_HOST, port=constant.REDIS_PORT, db=1,
                                    username=constant.REDIS_USER,
                                    password=constant.REDIS_PASSWORD)

    def process_request(self, request, spider):
        index = self.start_index
        if self.start_index >= len(self.proxy_list):
            index = 0
        proxy = self.proxy_list[index]
        self.start_index = self.start_index + 1
        if self.start_index > len(self.proxy_list):
            self.start_index = 0

        proxies = self.redis_db.zrangebyscore("proxies:biquge", min=90, max=100, num=10, start=0, withscores=True)
        request.meta['proxy'] = f"https://{proxies[random.randint(0, len(proxies))][0].decode('utf8')}"
        self.logger.info(f"index:{index}, length:{len(self.proxy_list)}, get proxy:{proxy}, for request:{request}")

    def process_response(self, request, response, spider):
        if response.status != 200:
            proxies = self.redis_db.zrangebyscore("proxies:biquge", min=90, max=100, num=10, start=0, withscores=True)
            proxy = proxies[random.randint(0, len(proxies))][0].decode('utf8')
            request.meta['proxy'] = f'https://{proxy}'
            logging.info(f"get response with proxy:{proxy}, response:{response}")
            return request
        return response


class BiqugeRetryMiddleware(RetryMiddleware):
    def __init__(self, settings):
        super().__init__(settings)
        self.redis_db = redis.Redis(host=constant.REDIS_HOST, port=constant.REDIS_PORT, db=1,
                                    username=constant.REDIS_USER,
                                    password=constant.REDIS_PASSWORD)

    def process_response(self, request, response, spider):
        if request.meta.get('dont_retry', False):
            return response

        if response.status in self.retry_http_codes:
            old_proxy = request.meta['proxy']
            constant.PROXY_SET.remove(old_proxy)
            reason = response_status_message(response.status)
            try:
                proxies = self.redis_db.zrangebyscore("proxies:biquge", min=90, max=100, num=10, start=0,
                                                      withscores=True)
                proxy = proxies[random.randint(0, len(proxies))][0].decode('utf8')
                request.meta['proxy'] = f"https://{proxy}"
                logging.info(f"retry with proxy:{proxy}")
            except requests.exceptions.RequestException as e:
                logging.error(f'获取讯代理ip失败！, exception:{e}')

            return self._retry(request, reason, spider) or response
        return response

    def process_exception(self, request, exception, spider):
        if isinstance(exception, self.EXCEPTIONS_TO_RETRY) and not request.meta.get('dont_retry', False):
            try:
                proxy = list(constant.PROXY_SET)[0]
                request.meta['proxy'] = 'https://' + proxy
            except requests.exceptions.RequestException:
                print('获取讯代理ip失败！')
                spider.logger.error('获取讯代理ip失败！')

            return self._retry(request, exception, spider)
