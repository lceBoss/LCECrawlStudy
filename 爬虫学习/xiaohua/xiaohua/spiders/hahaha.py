# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.http import Request
from ..items import HahahaItem

class HahahaSpider(scrapy.Spider):
    name = 'hahaha'
    allowed_domains = ['xiaohua.com']
    start_urls = ['http://www.xiaohuar.com/2014.html']

    def parse(self, response):

        # print (response.text)
        hxs = Selector(response=response).xpath('//div[@class="demo clearfix"]//div/div[@class="item_t"]/div[@class="img"]/a')
        for obj in hxs:
            href = obj.xpath('.//@src').extract_first()
            name = obj.xpath('.//@alt').extract_first()

            if (href.startswith("http://")):
                img_href = href
            else:
                img_href = "http://www.xiaohuar.com" + href

            item_obj = HahahaItem(name = name, href = img_href)
            yield item_obj





