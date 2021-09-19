# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import logging
import random

from scrapy import signals


# useful for handling different item types with a single interface


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
        proxy_list = ['112.95.20.73', '112.95.20.73', '112.95.20.73', '117.141.155.244', '59.120.147.82']
        request.meta['proxy'] = 'https://{proxy}'.format(proxy=proxy_list[random.randint(0, 4)])
        self.logger.info('Spider request: %s', request)

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        proxy_list = ['112.95.20.73', '112.95.20.73', '112.95.20.73', '117.141.155.244', '59.120.147.82']
        if response.status != 200:
            print("again response ip:")
            request.meta['proxy'] = 'https://{proxy}'.format(proxy=proxy_list[random.randint(0, 4)])
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
        self.proxy_list = ['27.191.60.137', '223.214.219.141', '27.191.60.137', '223.214.219.141', '181.129.240.43']

    def process_request(self, request, spider):
        request.meta['proxy'] = 'https://{proxy}'.format(proxy=self.proxy_list[random.randint(0, 4)])
        self.logger.info('Spider request: %s', request)

    def process_response(self, request, response, spider):
        if response.status != 200:
            print("again response ip:")
            request.meta['proxy'] = 'https://{proxy}'.format(proxy=self.proxy_list[random.randint(0, 4)])
            return request
        return response
