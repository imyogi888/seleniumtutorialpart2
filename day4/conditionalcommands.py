from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj= Service("C:\\mybrowserdriver\\chromedriver.exe")
driver= webdriver.Chrome(service=service_obj)
driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()

# is displayed() and is enabled()
#B search_box= driver.find_element(By.CSS_SELECTOR,'#small-searchterms')
# print(search_box.is_enabled())
# print(search_box.is_displayed())


# male_radio= driver.find_element(By.CSS_SELECTOR,"#gender-male")
# female_radio= driver.find_element(By.CSS_SELECTOR,"#gender-female")
# 87
# print("before selection",male_radio.is_selected())
# print("before selection",female_radio.is_selected())
#
# male_radio.click()
#
# print("after selection",male_radio.is_selected())
# print("after selection",female_radio.is_selected())
