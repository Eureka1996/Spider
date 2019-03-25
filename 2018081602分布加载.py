#coding=utf-8

import unittest
from selenium import webdriver
from bs4 import BeautifulSoup

class douyu(unittest.TestCase):
	
    def setUp(self):
        self.driver = webdriver.PhantomJS()

    def testDouyu(self):
        self.driver.get("https://www.douyu.com/directory/all")
        count = 0
        while True:
            soup = BeautifulSoup(self.driver.page_source,"lxml")
            names = soup.find_all("h3",{"class":"ellipsis"})
            numbers = soup.find_all("span",{"class":"dy-num fr"})
            
            for name,number in zip(names,numbers):
                print u"房间名：" + name.get_text().strip() + u",观众人数：" + number.get_text()
                count += 1
            
            print "shark-paper-next" + str(self.driver.page_source.find("shark-pager-disable-next"))

            if self.driver.page_source.find("shark-pager-disable-next") != -1:
                break
            
            self.driver.find_element_by_class_name("shark-pager-next").click()
        print "count:"+str(count)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
