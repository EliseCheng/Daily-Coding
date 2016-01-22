#!/usr/bin/python

from selenium import webdriver
import time
import threading


def open_ccf():
    browser = webdriver.Chrome()
#browser.get("http://192.168.5.120/accounts/login/")
    browser.get("http://127.0.0.1:8000/accounts/login/")

    browser.find_element_by_id('login-name').send_keys('test')
    browser.find_element_by_id('login-pass').send_keys('test')
    browser.find_element_by_class_name('btn-lg').click()

#browser.find_element_by_class_name('view_more_icon').click()
#browser.find_element_by_xpath('//div[@class="slice_list_block"]/div[@class="row"]').click()

    browser.get('http://127.0.0.1:8000/slice/detail/105/1/')
    return browser
#browser.get('http://192.168.5.120/slice/detail/55/1/')
#print browser.find_element_by_id('slice_qt').get_attribute('style')


id = '639_qt'

class Task(threading.Thread):

    def run(self):
        j = 0
        browser = open_ccf()
        while True:
            if browser.find_element_by_id(id).get_attribute('style') == 'cursor: pointer;':
                print "----%s------%d----" % (self.name, j)
                browser.find_element_by_id(id).click()

if __name__ == "__main__":
        t = Task()
        s = Task()
        t.start()
        s.start()
