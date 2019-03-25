#coding=utf-8

import urllib
import urllib2

def loadPage(url,filename):
    print "正在下载"+filename
    
    ua_headers = {"User-Agent":"MOzilla....."}
    request = urllib2.Request(url,headers=ua_headers)
    response = urllib2.urlopen(request)    
    html = response.read()
    return html

def writePage(html,filename):
    with open(filename,"w") as f:
        f.write(html)


def tiebaSpider(url,beginPage,endPage):
    for page in range(beginPage,endPage+1):
        pn = (page -1)*50
        filename = "第" + str(page) + "页.html"
        fullurl = url + "&pn=" + str(pn)
        html = loadPage(fullurl,filename) 
        writePage(html,filename)

if __name__ == "__main__":
    kw = raw_input("请输入需要爬取的贴吧名：")
    beginPage = int(raw_input("请输入起始页："))
    endPage = int(raw_input("请输入结束页："))
    url = "http://tieba.baidu.com/f?"
    key = urllib.urlencode({"kw":kw})
    fullurl = url + key
    tiebaSpider(fullurl,beginPage,endPage)
    
    
