#!/usr/bin/python

import datetime
from datetime import timedelta

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

browser = webdriver.Firefox()
browser.get("https://staging.acdid.acdsystems.com/ACDID/admin/login.php")

#login
browser.find_element_by_id("email").send_keys("antony.zhu@neudigit.com")
browser.find_element_by_id("password").send_keys("12345")
browser.find_element_by_xpath("//input[@type='submit']").click()

#Open Test Tools
browser.get("https://staging.acdid.acdsystems.com/ACDID/admin/dev_testtools.php?am=6")
browser.find_element_by_id("cur_sub_date").send_keys("2013-04-19")
browser.find_element_by_name("sen_sub_emails").click()

def get_sub_date(create_date):
	
	






	








