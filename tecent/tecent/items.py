# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TecentItem(scrapy.Item):
    # define the fields for your item here like:
    position_name = scrapy.Field()
    position_link = scrapy.Field()
    position_type = scrapy.Field()
    people_num = scrapy.Field()
    work_location = scrapy.Field()
    publish_time = scrapy.Field()
    
