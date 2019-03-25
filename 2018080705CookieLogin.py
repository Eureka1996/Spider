#coding=utf-8

import urllib
import urllib2
import cookielib

cookie = cookielib.CookieJar()
cookie_handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(cookie_handler)
opener.addheaders = [("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")]

url = "http://www.renren.com/PLogin.do"

form_data = {
    "email":"mr_mao_hacker@163.com",
    "password":"alarmchimewufuqiang"

}
data = urllib.urlencode(form_data)
request = urllib2.Request(url,data=data)
response = opener.open(request)
response = opener.open("http://www.renren.com/410043129/profile")
print response.read()
