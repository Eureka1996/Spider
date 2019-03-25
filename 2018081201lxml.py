#coding=utf-8

import urllib
import urllib2
import os
import time
from lxml import etree

def loadPage(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
    request = urllib2.Request(url,headers=headers)
    response = urllib2.urlopen(request)
    html = response.read()
#    print(html)
    content = etree.HTML(html)
#    print(content)
    link_list = content.xpath('//td[@class="fl_g"]/dl/dt/a/@href')
#    print("link_list:%s"%link_list)
    for link in link_list:
        link = url + link
#        print link
        loadImage(link,url)
        

def loadImage(link,url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
    request = urllib2.Request(link,headers=headers)
    response = urllib2.urlopen(request)
    html = response.read()
#    print html
    content = etree.HTML(html)
    link_img = content.xpath('//ul[@class="bud"]/li//span[@class="avt"]/img/@src')
#    print link_img
    print "-"*50
    for img in link_img:
        img = url + img
        print img
        writeImage(img)
    
def writeImage(img):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
    request = urllib2.Request(img,headers=headers)
    response = urllib2.urlopen(request)
    img = response.read()
    start = img.rfind("/")
    filename = str(int(time.time()*1000))
    filename = "dianbook/"+filename + ".jpg"
    print filename
    if os.path.exists(filename.decode("utf-8")):
        print "图片已经存在"
    else:
        print(filename)
        with open(filename,"wb") as f:
            f.write(img)


url ="http://www.dianbook.cc/"
loadPage(url)


