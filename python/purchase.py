#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.support.ui import Select

browser=webdriver.Firefox()
products=[]

def fill_bill_info(browser):
	browser.find_element_by_id("form_billinginfo_firstName").send_keys("sheldon")
	browser.find_element_by_id("form_billinginfo_lastName").send_keys("cooper")
	browser.find_element_by_id("form_billinginfo_companyName").send_keys("Google")
	browser.find_element_by_id("form_billinginfo_addressLine1").send_keys("Mountain View")
	browser.find_element_by_id("form_billinginfo_addressLine2").send_keys("zhongguancun")
	browser.find_element_by_id("form_billinginfo_city").send_keys("Beijing")
	browser.find_element_by_id("form_billinginfo_province").send_keys("Beijing")
	browser.find_element_by_id("form_billinginfo_postalCode").send_keys("100100")
	Select(browser.find_element_by_id("form_billinginfo_country")).select_by_visible_text("China")
	browser.find_element_by_id("form_billinginfo_phoneNumber").send_keys("4008123123")
	browser.find_element_by_id("form_billinginfo_emailAddress").send_keys("alice.cheng@neudigit.com")

def pay_with_creditcard(browser):
		browser.find_element_by_id("CreditCard").click()
		browser.find_element_by_id("CreditCardType_cardNum").send_keys("4003000123456781")
		Select(browser.find_element_by_id("CreditCardType_expDate_month")).select_by_visible_text("12")
		Select(browser.find_element_by_id("CreditCardType_expDate_year")).select_by_visible_text("2015")
		browser.find_element_by_id("CreditCardType_cvNum").send_keys("123")
		

def purchase(product):
	browser=webdriver.Firefox()
	browser.get(product)
	assert "acd Shopping Cart" in browser.title

	fill_bill_info(browser)
	pay_with_creditcard(browser)
	browser.find_element_by_id("tosAccepted").click()

	#proceed
	browser.find_element_by_id("submitBottom").click()

	#submit order
	browser.find_element_by_xpath("//input[@src='/image/submitorder.png']").click()
	browser.quit()

def auto_buy():
	for product in products:
		try:
			purchase(product)
		except:
			print product
			pass

def get_product_links():
	browser.get("http://demo.shop.acdsee.com/index")
	buylist=browser.find_elements_by_tag_name("a")
		
	for buy in buylist:
		products.append(buy.get_attribute("href"))

	print products
	browser.quit()

if __name__=="__main__":
	get_product_links()
	auto_buy()
