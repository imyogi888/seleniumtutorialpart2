from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj= Service("C:\\mybrowserdriver\\chromedriver.exe")
driver= webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()

dropdown= Select(driver.find_elements(By.ID,"country_id"))
# dropdown.select_by_visible_text("Australia")
# dropdown.select_by_value("10")
# dropdown.select_by_value(13)
# alloptions= dropdown.options
# print(len(alloptions))
#
# for option in alloptions:
#     print(option.text)
#
#
# for option in alloptions:
#     if option.text=="India":
#         option.click()
#         break

# alloptions= driver.find_elements(By.XPATH,"//select[@id='input-country']/option")
# print(len(alloptions))
# driver.find_element(By.XPATH,"//select[@id='input-country']/option[3]")

