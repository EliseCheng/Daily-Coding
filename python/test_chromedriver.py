import time

from selenium import webdriver
import selenium.webdriver.chrome.service as service


service = service.Service('/home/chengwen/Daily-Coding/python/chromedriver')
service.start()
capabilities = {'chrome.binary': '/opt/google/chrome/chrome'}
#print service.service_url
driver = webdriver.Remote(service.service_url, capabilities)
print driver
driver.get('http://127.0.0.1:8000/accounts/login/')
time.sleep(5) # Let the user actually see something!
driver.quit()
