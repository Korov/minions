# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class biquge_item(scrapy.Item):
    # define the fields for your item here like:
    book_url = scrapy.Field()
    book_name = scrapy.Field()
    author_name = scrapy.Field()
