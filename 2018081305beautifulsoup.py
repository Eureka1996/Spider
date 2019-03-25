#coding=utf-8

from bs4 import BeautifulSoup
import requests
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


def zhihuLogin():
    sess = requests.Session()
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
    html = sess.get("http://www.xuetangx.com/v2/login_ajax",headers=headers).text
#    print html
    bs = BeautifulSoup(html,"lxml")
#    print bs
    query = bs.find("input",attrs={"name":"username"}).get("value")
    print query

    

if __name__ == "__main__":
    zhihuLogin()
