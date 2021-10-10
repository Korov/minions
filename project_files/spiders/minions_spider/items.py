# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BiqugeItem(scrapy.Item):
    # define the fields for your item here like:
    book_name = scrapy.Field()
    book_description = scrapy.Field()
    book_category = scrapy.Field()
    book_author = scrapy.Field()
    book_url = scrapy.Field()
    chapter_url = scrapy.Field()
    chapter_name = scrapy.Field()
    chapter_content = scrapy.Field()
    chapter_body = scrapy.Field()
    timestamp = scrapy.Field()
    date_time = scrapy.Field()
