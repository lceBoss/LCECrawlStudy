# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.http.cookies import CookieJar
from scrapy.selector import Selector
from ..items import XiaoshuoItem

# class ChangyuebaSpider(scrapy.Spider):
#     name = 'changyueba'
#     allowed_domains = ['changyueba.com']
#     start_urls = ['http://m.changyueba.com/book/74/74320/index.html']
#     # start_urls = ['http://m.changyueba.com/book/74/74320/17987774.html']
#
#     cookie_dict = None
#     def parse(self, response):
#         cookie_obj = CookieJar()
#         cookie_obj.extract_cookies(response, response.request)
#         self.cookie_dict = cookie_obj._cookies
#
#         hxs = Selector(response=response).xpath('//div[@class="nr_zp"]//a')
#         for obj in hxs:
#             href = obj.xpath('./@href').extract_first()
#             name = obj.xpath('./text()').extract_first()
#
#             # item_obj = XiaoshuoItem(name=name, href=href)
#             # yield item_obj
#             # print(name)
#
#             yield Request(url=href, callback=self.download)
#
#             # 获取所有页码
#
#
#
#     def download(self, response):
#         # print(response.text)
#         title = Selector(response=response).xpath('//div[@class="text_c_bottom"]//span[@class="read_title"]/text()').extract()
#         text = Selector(response=response).xpath('//div[@class="text_c_bottom"]//p/text()').extract()
#
#         item_obj = XiaoshuoItem(title=title, text=text)
#
#         print(title)
#         yield item_obj


class ChangyuebaSpider(scrapy.Spider):
    name = 'changyueba'
    allowed_domains = ['changyueba.com']
    start_urls = ['http://m.changyueba.com/book/74/74320/17987774.html']

    cookie_dict = None
    def parse(self, response):

        title = Selector(response=response).xpath('//div[@class="text_c_bottom"]//span[@class="read_title"]/text()').extract()
        text = Selector(response=response).xpath('//div[@class="text_c_bottom"]//p/text()').extract()
        next_url = Selector(response=response).xpath('//div[@class="next_page_C"]//a[@class="three"]/@href').extract_first()

        print(next_url + "擦擦擦擦擦擦擦擦擦擦擦啊擦擦擦擦擦")
        item_obj = XiaoshuoItem(title=title, text=text)
        yield item_obj
        # 请求下一页
        yield Request(url=next_url, callback=self.parse)

