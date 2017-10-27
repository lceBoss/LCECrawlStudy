# -*- coding: utf-8 -*-
import scrapy
import sys
import io
from scrapy.http import Request
from scrapy.selector import Selector, HtmlXPathSelector
from ..items import ChoutiItem
from scrapy.dupefilters import RFPDupeFilter
from scrapy.http.cookies import CookieJar


sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

class ChoutiSpider(scrapy.Spider):
    name = "chouti"
    allowed_domains = ["chouti.com"]
    start_urls = ['http://dig.chouti.com/']

    cookie_dict = None
    def parse(self, response):
        cookie_obj = CookieJar()
        cookie_obj.extract_cookies(response, response.request)
        self.cookie_dict = cookie_obj._cookies

        # 带上用户名和密码
        yield Request(
            url="http://dig.chouti.com/login",
            method='POST',
            body='phone=8615839405523&password=123456&oneMonth=1',
            headers={'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8'},
            cookies=cookie_obj._cookies,
            callback=self.check_login
        )

    def check_login(self, response):
        # 表示登录成功
        print(response.text)
        yield Request(
            url='http://dig.chouti.com/',
            callback=self.good
        )

    def good(self, response):
        # 获取所有的新闻条然后点赞
        id_list = Selector(response=response).xpath('//div[@share-linkid]/@share-linkid').extract()
        for nid in id_list:
            url = "http://dig.chouti.com/link/vote?linksId=%s" %nid
            yield Request(
                url=url,
                method='POST',
                cookies=self.cookie_dict,
                callback=self.show
            )
        # 获取深度内所有的页码
        page_urls = Selector(response=response).xpath('//div[@id="dig_lcpage"]//a/@href').extract()
        # print(page_urls)
        for page in page_urls:
            # print(page)
            url = "http://dig.chouti.com%s" %page
            yield Request(url=url, callback=self.good)

    def show(self, response):
        print(response.text)










