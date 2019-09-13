# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class DbbookPipeline(object):
    def open_spider(self, spider):
        # print("^^^^^^^^^^^^^^^^^^")
        # print(spider.settings.get('MONGO_URL'))
        # print(spider.settings.get('MONGO_DB'))
        # print(spider.settings.get('MONGO_COLLECTION'))
        # print(spider.settings.get('MONGO111', 'aaaaaaa'))

        client = pymongo.MongoClient(spider.settings.get('MONGO_URL'))
        db = client[spider.settings.get('MONGO_DB')]
        self.collection = db[spider.settings.get('MONGO_COLLECTION')]

    def close_spider(self, spider):
        pass

    def process_item(self, item, spider):
        # print(item, "++++++++++++++++++++++++++++++")
        self.collection.insert_one(dict(item))
        return item
