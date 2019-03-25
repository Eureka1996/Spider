#coding=utf-8

import urllib
import urllib2

url = "https://movie.douban.com/j/search_subjects?"

ua_headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}

formdata = {
"type":"movie",
"tag":"热门",
"sort":"recommend",
"page_start":"0",
"page_limit":"40"
}

data = urllib.urlencode(formdata)



if __name__ == "__main__":
    request = urllib2.Request(url,data=data,headers=ua_headers);
    response = urllib2.urlopen(request)
    print response.read()
