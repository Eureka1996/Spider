#coding=utf-

import requests
from Queue import Queue
from lxml import etree
import json
import threading



class ThreadCrawl(threading.Thread):
    def __init__(self,threadName,pageQueue,dataQueue):
        super(ThreadCrawl,self).__init__();
        self.threadName = threadName
        self.pageQueue = pageQueue
        self.dataQueue = dataQueue
        self.headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"} 

    def run(self):
        while not CRAWL_EXIT:
            try:
                page = self.pageQueue.get(False)
                url = "https://www.qiushibaike.com/text/page/%d/"%page
                print "%s:%s"%(self.threadName,url)
                content = requests.get(url,headers=self.headers).text
                self.dataQueue.put(content)
            except:
                pass


class ThreadParse(threading.Thread):
    def __init__(self,threadName,dataQueue,file1,lock):
        super(ThreadParse,self).__init__()
        self.threadName = threadName
        self.dataQueue = dataQueue
        self.file1 = file1
        self.lock = lock

    def run(self):
        while not PARSE_EXIT:
            try:
                html = self.dataQueue.get(False)
#                print html
                self.parse(html)
            except:
                pass

    def parse(self,html):
        content = etree.HTML(html)
        text_list = content.xpath('//div[@class="content"]')
        print len(text_list)
        for text in text_list:
            duanzi = text.xpath('.//span')[0].text
            print type(duanzi)
            with self.lock:
                self.file1.write(json.dumps(duanzi,ensure_ascii=False).encode("utf-8")+"\n")

        
        
CRAWL_EXIT = False
PARSE_EXIT = False



def main():

    pageQueue = Queue(10)
    dataQueue = Queue()
    lock = threading.Lock()
    file1 = open("duanzi.txt","a")

    for page in range(1,11):
        pageQueue.put(page)

    crawl_list = ["采集线程1号","采集线程2号","采集线程3号"]

    threadcrawl = []
    for threadname in crawl_list:
        thread = ThreadCrawl(threadname,pageQueue,dataQueue)
        thread.start()
        threadcrawl.append(thread)

    parse_list = ["解析线程1号","解析线程2号","解析线程3号"]
    threadparse = []
    for threadName in parse_list:
        thread = ThreadParse(threadName,dataQueue,file1,lock)
        thread.start()
        threadparse.append(thread)    


    while not pageQueue.empty():
#        print "fuckliyuqing-------------------"
        pass

    while not dataQueue.empty():
        pass
        

    global CRAWL_EXIT
    global PARSE_EXIT
    CRAWL_EXIT = True
    PARSE_EXIT = True
    
    print "pageQueue为空"
    print "dataQueue为空"

    for thread in threadcrawl:
        thread.join()
        print "fuckliyuqing"

    for thread in threadparse:
        thread.join()
        print "fuckliyuqingsecond"

if __name__ == "__main__":
    main()
        

