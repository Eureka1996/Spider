# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from TecentPositionSpider.items import TecentpositionspiderItem


class TencentSpider(CrawlSpider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['http://hr.tencent.com/position.php?&start=0#a']
    pagelink = LinkExtractor(allow=("start=\d+"))
    rules = (
        Rule(pagelink, callback='parse_item', follow=True),
    )



    def parse_item(self, response):
        

        for each in response.xpath('//tr[@class="even"]|//tr[@class="odd"]'):
            item = TecentpositionspiderItem()
            item['position_name'] = each.xpath('.//td[1]/a/text()').extract()[0]
            item['position_link'] = each.xpath('.//td[1]/a/@href').extract()[0]
            position_type = each.xpath('.//td[2]/text()')
            if len(position_type) == 0:
                item['position_type'] = ""
            else:
                item['position_type'] = position_type.extract()[0]
            item['people_num'] = each.xpath('.//td[3]/text()').extract()[0]
            item['work_location'] = each.xpath('.//td[4]/text()').extract()[0]
            item['publish_time'] = each.xpath('.//td[5]/text()').extract()[0]
            yield item

        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()

