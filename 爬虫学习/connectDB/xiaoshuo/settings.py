# -*- coding: utf-8 -*-

# Scrapy settings for xiaoshuo project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'xiaoshuo'

SPIDER_MODULES = ['xiaoshuo.spiders']
NEWSPIDER_MODULE = 'xiaoshuo.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'xiaoshuo (+http://www.yourdomain.com)'
# 小说请求头（非正式）
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'

# Obey robots.txt rules
'''是否遵循爬虫规则'''
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
'''设置请求并发数'''
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
'''下载延迟，每几秒下载多少次'''
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
'''每个域名最大并发数是多少'''
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
'''每个ip最大并发数是多少'''
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
'''是否获取cookie'''
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
'''爬取过程中监听爬取情况'''
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
'''默认的请求头'''
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
'''爬虫中间件'''
#SPIDER_MIDDLEWARES = {
#    'xiaoshuo.middlewares.XiaoshuoSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
'''下载中间件'''
# DOWNLOADER_MIDDLEWARES = {
#    'xiaoshuo.middlewares.DownMiddleware1': 543,
# }

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'xiaoshuo.pipelines.XiaoshuoPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 2
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 10
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# 深度
DEPTH_LIMIT = 0

