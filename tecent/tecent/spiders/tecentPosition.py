# -*- coding: utf-8 -*-
import scrapy
from tecent.items import TecentItem


class TecentpositionSpider(scrapy.Spider):
    name = "tecentPosition"
    allowed_domains = ["tencent.com"]
    offset = 1
    url = "http://hr.tencent.com/position.php?&start=%d"%((offset-1)*10)
    start_urls =[url] 
    

    def parse(self, response):
        for each in response.xpath('//tr[@class="even"]|//tr[@class="odd"]'):
            item = TecentItem()
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

        if self.offset < 100:
            self.offset += 1

        self.url = "http://hr.tencent.com/position.php?&start=%d"%((self.offset-1)*10)
        yield scrapy.Request(self.url,callback=self.parse)
