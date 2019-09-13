# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http.response.html import HtmlResponse
from ..items import DbbookItem


class BookSpider(CrawlSpider):
    name = 'book'
    allowed_domains = ['douban.com']
    start_urls = ['https://book.douban.com/tag/%E7%BC%96%E7%A8%8B']

    # follow=False 不跟进
    rules = (
        Rule(LinkExtractor(allow=r'start=\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response:HtmlResponse):
        print(response.url)

        for subject in response.xpath('//li[@class="subject-item"]'):
            item = DbbookItem()

            title = subject.xpath('.//h2/a//text()').extract()
            item['title'] = "".join(map(lambda x:x.strip(), title))
            # print("".join(map(lambda x:x.strip(), title)))

            rate = subject.xpath('.//span[@class="rating_nums"]//text()').get() # extract_first
            item['rate'] = rate if rate else '0'

            yield item