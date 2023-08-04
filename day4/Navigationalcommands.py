from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj= Service("C:\\mybrowserdriver\\chromedriver.exe")
driver= webdriver.Chrome(service=service_obj)
driver.get("https://www.amazon.in/")
driver.get("https://www.flipkart.com/")
driver.back()
driver.forward()
driver.refresh()