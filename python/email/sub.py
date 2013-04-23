#!/usr/bin/python

import datetime
from datetime import timedelta

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

from ex_date import get_date

browser = webdriver.Firefox()
browser.get("login.php")

#login
browser.find_element_by_id("email").send_keys("")
browser.find_element_by_id("password").send_keys("12345")
browser.find_element_by_xpath("//input[@type='submit']").click()

#Open Test Tools
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Development")))
browser.find_element_by_partial_link_text("Development Tools").click()
browser.find_element_by_link_text("Test Tools").click()

expiration_dates = get_date("2013-05-21", 31)
print expiration_dates
#Send expiration soon email
for expiration_date in expiration_dates:
	print expiration_date
	WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "cur_sub_date")))
	element_d = browser.find_element_by_id("cur_sub_date")
	element_d.clear()
	element_d.send_keys(expiration_date)
	browser.find_element_by_name("send_sub_emails").click()
	print browser.switch_to_alert().text
	if browser.switch_to_alert():
		browser.switch_to_alert().accept()
	WebDriverWait(browser, 3)
	#break
browser.quit()

#Check emails 
#Check different languages
#print subject	
	
	






	








