# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DbbookItem(scrapy.Item):
    title = scrapy.Field() # 书名
    rate = scrapy.Field() # 评分

    def __repr__(self):
        return "<DbbookItem {}>".format(dict(self))
