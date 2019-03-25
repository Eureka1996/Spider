#coding=utf-8

import urllib
import urllib2

headers = {
"Host":"www.baidu.com",
"Connection":"keep-alive",
#"Upgrade-Insecure-Requests":"1",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"DNT":"1",
"Referer":"https://passport.baidu.com/v2/api/?login",
#"Accept-Encoding":"gzip, deflate, br",
"Accept-Language":"zh-CN,zh;q=0.9",
#"Cookie":"PSTM=1529557066; BIDUPSID=E20A6767028E29297DE12AAAE7D7C22D; BAIDUID=B00EB6238A1AD4E453D54F68F276801F:FG=1; sug=3; sugstore=0; ORIGIN=2; bdime=0; BD_UPN=12314753; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; H_PS_PSSID=; BD_CK_SAM=1; PSINO=7; BD_HOME=0; FP_UID=214100ab51b706f790cb204443f23989; BDUSS=kFaWVhmZlB-WGNLMHpJYlFoMXNLTjM3M3kyWW5EeEVucDlTQX5ULXVuREh5cEJiQVFBQUFBJCQAAAAAAAAAAAEAAACxO3grd3VmdXFpYW5nNQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMc9aVvHPWlbZ"
}

url = "http://i.baidu.com/"

request = urllib2.Request(url,headers=headers)

response = urllib2.urlopen(request)

print response.read()
