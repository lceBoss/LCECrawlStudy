# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class Day96Pipeline(object):

    def process_item(self, item, spider):
        '''
        每当数据需要持久化时，就会被调用
        '''
        tpl = "%s\n%s\n\n" %(item['title'],item['href'])
        self.f.write(tpl)

    def open_spider(self, spider):
        """
        爬虫开始执行时，调用
        """
        self.f = open('news.json', 'a')

    def close_spider(self, spider):
        """
        爬虫关闭时，被调用
        """
        self.f.close()
