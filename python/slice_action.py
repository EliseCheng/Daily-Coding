#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import time

browser = webdriver.Chrome()
browser.get("http://127.0.0.1:8000/accounts/login/")

browser.find_element_by_id('login-name').send_keys('test')
browser.find_element_by_id('login-pass').send_keys('test')
browser.find_element_by_class_name('btn-lg').click()

#browser.find_element_by_class_name('view_more_icon').click()
#browser.find_element_by_xpath('//div[@class="slice_list_block"]/div[@class="row"]').click()

browser.get('http://127.0.0.1:8000/slice/detail/105')
#print browser.find_element_by_id('slice_qt').get_attribute('style')
j = 0
#for i in range(1, 10000):
while True:
    #print "**loop**"
    #try:
    #    alt = browser.switchTo().alert();
    #    alt.accept()
    #except:
    #    pass
    if browser.find_element_by_id('slice_qt').get_attribute('style') == 'cursor: pointer;':
        print '----%d-----' % (j)
        browser.find_element_by_id('slice_qt').click()
        j = j+1

