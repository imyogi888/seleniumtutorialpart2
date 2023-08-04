from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\mybrowserdriver\\chromedriver.exe")
driver= webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
driver.find_element(By.ID,"small-searchterms").send_keys("iphone 11")
driver.find_element(By.PARTIAL_LINK_TEXT,"Reg").click()