# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from MySQLdb import *
from scrapy.conf import settings


class DoubanPipeline(object):
    def __init__(self):
        self.host = settings['MYSQL_HOST']
        self.db = settings['MYSQL_DBNAME']
        self.user = settings['MYSQL_USER']
        self.passwd = settings['MYSQL_PASSWD']
        self.port = settings['MYSQL_PORT']
        self.conn = connect(host=self.host,db=self.db,user=self.user,passwd=self.passwd,port=self.port,charset="utf8")
        self.cs = self.conn.cursor()


    def process_item(self, item, spider):
        item_list = [item["title"],item['bd'],item['star'],item['quote']]
        sql = "insert into movies(title,bd,star,quote) values(%s,%s,%s,%s)"
        self.cs.execute(sql,item_list)
        self.conn.commit()
        return item

    def close_spider(self,spider):
        self.cs.close()
        self.conn.close()

