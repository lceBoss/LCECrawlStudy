# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.selector import  Selector, HtmlXPathSelector
from ...items import ChoutiItem

class ChoutiSpider(scrapy.Spider):
    name = 'chouti'
    allowed_domains = ['chouti.com']
    start_urls = ['http://dig.chouti.com/']

    visited_urls = set()

    def parse(self, response):
        # 找到文档中所有A标签
        # hxs = Selector(response=response).xpath('//a') #标签对象列表
        # for i in hxs:
        #     print(i) # 标签对象
        '''
        # 对象转成字符串
        hxs = Selector(response=response).xpath('//div[@id="content-list"]/div[@class="item"]')

        # print(hxs)
        i = 0
        for obj in hxs:
            a = obj.xpath('.//a[@class="show-content color-chag"]/text()').extract_first()
            # print(a)
            if a:
                i += 1
                print(str(i) + a.strip())
        '''

        hxs1 = Selector(response=response).xpath('//div[@id="content-list"]/div[@class="item"]')
        for obj in hxs1:
            title = obj.xpath('.//a[@class="show-content color-chag"]/text()').extract_first().strip()
            href = obj.xpath('.//a[@class="show-content color-chag"]/@href').extract_first().strip()
            item_obj = ChoutiItem(title = title, href = href)

            # 将item对象床底给pipeline

            yield item_obj


        '''
        # hxs = Selector(response=response).xpath('//div[@id="dig_lcpage"]//a/@href').extract()
        hxs2 = Selector(response=response).xpath('//a[starts-with(@href, "/all/hot/recent/")]/@href').extract()
        for url in hxs2:
            print(url)
            md5_url = self.md5(url)
            if md5_url in self.visited_urls:
                pass
            else:
                print(url)
                self.visited_urls.add(md5_url)
                url = "http://dig.chouti.com%s" %url
                # 将新要访问的url添加到调度器
                yield Request(url=url, callback=self.parse)

        # a/@href 获取属性
        # //a[starts-with(@href, "/all/hot/recent/")]/@href')  以xx开始
        # //a[re:text(@href, "/all/hot/recent/")]/@href')      正则
        # yield Request(url=url, callback=self.parse)          # 将新要访问的url添加到调度器
        '''


    def md5(self,url):
        import hashlib
        obj = hashlib.md5()
        obj.update(bytes(url, encoding='utf-8'))
        return obj.hexdigest()
