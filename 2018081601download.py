#coding=utf-8

import urllib2
import time


def writeImage(img):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
    request = urllib2.Request(img,headers=headers)
    while True:
        try:
            response = urllib2.urlopen(request,timeout=5)
            img_content = response.read()
            break
        except:
            time.sleep(1)
            print("-------------重新加载writeImage------%d------------------"%int(time.time()))
            writeImage(img)
            return 

            
    point = img.rfind("/")
    filename = img[point+1:]
    if os.path.exists(filename.decode("utf-8")):
        print "图片已经存在"
    else:
        with open(filename,"wb") as f:
            f.write(img_content)
            print("保存图片%s:%d"%(filename,int(time.time())))


writeImage("https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2")
