# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class DownMiddleware1(object):

    def process_request(self, request, spider):
        '''
        请求需要被下载时，经过所有下载器中间件的process_request调用
        :param request:
        :param spider:
        :return:
            None, 继续后续中间件中去下载；
            Response对象，停止process_request的执行，开始执行process_response
            Request对象，停止中间件的执行，将Request重新调度器
            raise IgnoreRequest异常，停止process_request的执行，开始执行process_exception
        '''
        print("帮我下载", request.url)

    def process_response(self, request, response, spider):
        """
        spider处理完成，返回时调用
        :param request:
        :param response:
        :param spider:
        :return:
            Response对象：转交给其他中间件process_response
            Request 对象：停止中间件，request会被重新调度下载
            raise IgnoreRequest 异常：调用Request.errback
        """
        # 如果不加返回值，结果就不会到spider
        return response

    def process_exception(self, request, exception, spider):
        """
        当下载处理器（download handler）或process_request() (下载中间件)抛出异常
        :param request:
        :param exception:
        :param spider:
        :return:
            None：继续交给后续中间件处理异常；
            Response对象：停止后续process_exception方法
            Request对象：停止中间件，Request将会被重新调用下载
        """

        print("报错啦啦啦啦啦啦啦啊", request.url)

        return None
