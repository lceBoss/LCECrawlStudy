
from scrapy import signals

class MyExtens:


    def __init__(self, crawler):

        self.crawler = crawler
        crawler.signals.connect(self.start, signals.engine_started)
        crawler.signals.connect(self.close, signals.spider_closed)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def start(self):
        print('signals.engine_started 哈哈哈哈哈')

    def close(self):
        print('signals.spider_closed  当爬虫结束时调用此方法')