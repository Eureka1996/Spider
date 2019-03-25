#coding=utf-8

import urllib
import urllib2

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule/"
key = raw_input("请输入要翻译的文字：")
formdata = {
    "i":key,
    "from":"en",
    "to":"zh-CHS",
    "smartresult":"dict",
    "client":"fanyideskweb",
    "doctype":"json",
    "version":2.1,
    "keyfrom":"fanyi.web",
    "xmlVersion":1.8,
    "action":"FY_BY_REALTIME",
    "typoResult":"false"
}

data = urllib.urlencode(formdata)
ua_headers = {
    "Accept":"application/json, text/javascript, */*; q=0.01",
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With":"XMLHttpRequest",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}

request = urllib2.Request(url,data=data,headers=ua_headers)
response = urllib2.urlopen(request)

print response.read()
