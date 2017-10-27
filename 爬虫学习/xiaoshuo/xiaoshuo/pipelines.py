# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem

class XiaoshuoPipeline(object):
    def process_item(self, item, spider):

        tpl = "%s\n%s\n\n" %(item['title'],item['text'])
        print(tpl)
        self.f.write(tpl)
        raise DropItem()

    def open_spider(self, spider):
        """
        爬虫开始执行时，调用
        """
        print("爬虫开始")
        self.f = open('yemeigui.json', 'a')

    def close_spider(self, spider):
        """
        爬虫关闭时，被调用
        """
        print("爬虫关闭")
        self.f.close()