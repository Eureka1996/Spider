#coding=utf-8

import urllib2
import json
import jsonpath


url = "https://www.lagou.com/lbs/getAllCitySearchLabels.json"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}

request = urllib2.Request(url,headers=headers)

response = urllib2.urlopen(request)

html = response.read()

unicodestr = json.loads(html)

cityname_list = jsonpath.jsonpath(unicodestr,"$..name")

for cityname in cityname_list:
    print("%s/"%cityname)

array = json.dumps(cityname_list,ensure_ascii=False)

with open("lagoucity.json","w") as f:
    f.write(array.encode("utf-8"))
