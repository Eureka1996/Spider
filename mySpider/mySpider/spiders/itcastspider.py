#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import scrapy
from mySpider.items import ItcastItem

class ItcastSpider(scrapy.Spider):
    name = "buaa"
    allowed_domains = ["http://soft.buaa.edu.cn/"]
    start_urls = ["http://soft.buaa.edu.cn/szzs.htm"]

    def parse(self,response):
        teacher_list = response.xpath('//div[@class="main_rpicR"]')
        for each in teacher_list:
            item = ItcastItem()
            name = each.xpath('./h3/a/text()').extract()
            info = each.xpath('.//p[position()=1]/text()').extract()
            time = each.xpath('.//p[position()=2]/text()').extract()
            item["name"] = name[0]
            item["info"] = info[0]
            item["time"] = time[0]
            yield item
        
