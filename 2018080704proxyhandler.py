#eoding=utf-8

import urllib2

proxyswitch = True

httpproxy_handler = urllib2.ProxyHandler({"http":"61.135.217.7:80"})

nullproxy_handler= urllib2.ProxyHandler({})

if proxyswitch:
    opener = urllib2.build_opener(httpproxy_handler)
else:
    opener = urllib2.build_opener(nullproxy_handler)

request = urllib2.Request("http://www.baidu.com/")
urllib2.install_opener(opener)

response = urllib2.urlopen(request)

print response.read()
