# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.utils.project import get_project_settings
from scrapy.pipelines.images import ImagesPipeline
import os

class ImagesPipeline(object):
    images_store = get_project_settings().get("IMAGES_STORE")

    def get_media_requests(self,item,info):
        image_url = item["imagelink"]
        yield scrapy.Request(image_url)

    def item_completed(self,result,item,info):
        image_path = [x["path"] for ok, x in result if ok]
        os.rename(self.images_store + "/" + image_path[0],self.images_store + "/" + item["nickname"] + ".jpg"
        item["imagepath"] = self.images_store + "/" + item["nickname"]
        return item
