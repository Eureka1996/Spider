# -*- coding: utf-8 -*-
import scrapy
import json
from douyu.items import DouyuItem


class DouyumeinvSpider(scrapy.Spider):
    name = "douyumeinv"
    allowed_domains = ["capi.douyucdn.cn"]
    url = "http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset=0"
    offset = 0
    start_urls = [url+str(offset)]

    def parse(self, response):
        item = DouyuItem()
        data = json.loads(response.text)["data"]
        for each in data:
            item["nickname"] = each["nickname"]
            item["imagelink"] = each["vertical_src"]
            item["imagepath"]
            yield item
        
        self.offset += 20
        yield scrapy.Request(url+str(self.offset),callback=self.parse)

