from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj= Service("C:\\mybrowserdriver\\chromedriver.exe")
driver= webdriver.Chrome(service=service_obj)
driver.get("https://admin-demo.nopcommerce.com/login")
# element= driver.find_element(By.ID,"Email")
# element.clear()
# element.send_keys("hddhdggd@gmail.com")
# print("first calue", element.get_attribute('value'))
# print("second value is", element.text)

elements= driver.find_element(By.XPATH,"//button[text()='Log in']")
print("first value",elements.get_attribute("value"))
print("secondvalueis",elements.text)