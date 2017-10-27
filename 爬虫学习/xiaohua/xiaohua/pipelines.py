# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import requests

class XiaohuaPipeline(object):
    def process_item(self, item, spider):
        print(spider, item)

        tpl = "%s\n%s\n\n" %(item['name'] , item['href'])
        f = open("xiaohua.json", "a+")
        f.write(tpl)
        f.close()

class XiaohuaImagePopeline(object):
    def process_item(self, item, spider):

        img_response = requests.get(item['href'])

        fileName = item['name'] + ".jpg"

        with open("xiaohua/xiaohua/hahaha/%s" %fileName, "wb") as f:
            f.write(img_response.content)