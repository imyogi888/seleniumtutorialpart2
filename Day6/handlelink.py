from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj= Service("C:\\mybrowserdriver\\chromedriver.exe")
driver= webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
# driver.find_element(By.LINK_TEXT,"Digital downloads").click()
# driver.find_element(By.LINK_TEXT,"Digital").click()

elements= driver.find_elements(By.TAG_NAME,"a")
# print(len(elements))

for links in elements:
    link_name= links.text
    print(link_name)