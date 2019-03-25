#coding=utf-8

import urllib
import urllib2
import re


class Spider(object):

    def __init__(self):
        pass

    
    def load_page(self,page):
        url = "http://jandan.net/duan/page-" + str(page) + "#comments"
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
        request = urllib2.Request(url,headers=headers)
        response = urllib2.urlopen(request)
        html = response.read()
        pattern = re.compile('<div class="text">.*?<p>(.*?)</p>',re.S)
        content_list = pattern.findall(html)
        self.deal_page(content_list)        

    def write_page(self,content):
        with open("duanzi.txt","a") as f:
            f.write(content)

    def deal_page(self,content_list):
        for content in content_list:
            content = content.replace("<br />","")
            self.write_page(content)


spider = Spider()
content_list = spider.load_page(78)




