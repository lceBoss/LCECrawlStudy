# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
import pymysql
import re


class XiaoshuoPipeline(object):

    def __init__(self):
        # connect = pymysql.connect(
        #     user="root",
        #     password="123456",
        #     port=3306,
        #     host="10.10.8.142",
        #     db="xiaobei",
        #     charset="utf8"
        # )
        connect = pymysql.connect(
            user="root",
            password="12345678",
            port=3306,
            host="localhost",
            db="xiaobei",
            charset="utf8"
        )
        conn = connect.cursor()  # 获取游标
        try:
            conn.execute("create table xiaoshuo(chapters_id VARCHAR(256) NOT NULL PRIMARY KEY, title text, textContent text)")
        except Exception as e:
            print(e)
        self.conn = conn
        self.connect = connect


    def process_item(self, item, spider):

        tpl = "%s\n%s\n\n" %(item['title'],item['text'])
        # print(tpl)
        self.f.write(tpl)

        chapters = re.findall("\d+", str(item['title']))[0] # 章节
        titleStr = str(item['title'])  # 章节标题
        contentStr = str(item['text']) # 章节内容

        print(type(chapters), "这不是欺负人吗，是不是傻啊啊啊啊啊啊啊啊")

        sql = "insert into xiaoshuo(chapters_id, title, textContent) VALUES(%s, %s, %s)"
        self.conn.execute(sql, [chapters, titleStr, contentStr]) # 执行sql命令 创建xiaoshuo来保存信息
        self.connect.commit()  # 提交数据库，否则数据还是不能上传s

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

        self.conn.close()  # 关闭游标
        self.connect.close()  # 关闭数据库


    def database(self, title, text):
        connect = pymysql.connect(
            user="root",
            password="123456",
            port=3306,
            host="10.10.8.142",
            db="MYSQL",
            charset="utf-8"
        )
        conn = connect.cursor()  # 获取游标
        conn.execute("create database xiaobei")  # 创建数据库
        conn.execute("use xiaobei")  # 使用数据库
        conn.execute("drop table if EXISTS xiaoshuo")
        conn.execute("create table xiaoshuo (title VARCHAR(), text VARCHAR ())")
        sql = "insert into xiaoshuo(title, text)VALUES(%s, %s)"
        conn.execute(sql, [title, text])  # 执行sql命令 创建xiaoshuo来保存信息
        connect.commit()  # 提交数据库，否则数据还是不能上传
        conn.close()  # 关闭游标
        connect.close()  # 关闭数据库

        print("year, you are right")