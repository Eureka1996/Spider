#coding=utf-8

import urllib
import urllib2

url = "http://www.baidu.com/s"
keyword = raw_input("请输入查询的关键字")

wd = {"wd":keyword}
wd = urllib.urlencode(wd)
print wd
url = url + "?" + wd
ua_headers = {"User-Agent":"Mozilla...."}
request = urllib2.Request(url,headers=ua_headers)

response = urllib2.urlopen(request)

print response.read()
