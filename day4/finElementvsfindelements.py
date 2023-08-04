from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj= Service("C:\\mybrowserdriver\\chromedriver.exe")
driver= webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

#1) Locator matching with single webelement

# elements= driver.find_element(By.ID,"small-searchterms")
# elements.send_keys("iphone")

#2) Locator matching with multiple webelements

# element= driver.find_element(By.XPATH,"//div[@class='footer']//a")
# print(element.text)

# 3) Element not avaialble then throw nosuchelementexception

# element= driver.find_element(By.LINK_TEXT,"log")
# element.click()


# find_elements()- Returns multiple webElements

# 1)Locator matching with single webelement

# elements= driver.find_elements(By.ID,"small-searchterms")
# print(len(elements))
# elements[0].send_keys("iphone")

# 2) Locator matching with multiple webelements

# Elements= driver.find_elements(By.XPATH,"//div[@class='footer']//li/a")
# print(len(Elements))
# for ele in Elements:
#     print(ele.text)

# 3) Elements not avaialble

# element= driver.find_elements(By.LINK_TEXT,"log")
# print(len(element))