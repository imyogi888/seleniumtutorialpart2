from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\mybrowserdriver\\chromedriver.exe")
driver= webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()

searchbox= driver.find_element(By.ID,"small-searchterms")
print(searchbox.is_displayed())

radio= driver.find_element(By.ID,"gender-male")
print(radio.is_selected())

driver.find_element(By.ID,"gender-male").click()
print(radio.is_selected())