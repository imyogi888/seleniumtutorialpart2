from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj= Service("C:\\mybrowserdriver\\chromedriver.exe")
driver= webdriver.Chrome(service=service_obj)
driver.implicitly_wait(9)
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()

min_element= driver.find_element(By.XPATH,"//span[@class='ui-slider-handle ui-corner-all ui-state-default'][1]")
max_element= driver.find_element(By.XPATH,"//span[@class='ui-slider-handle ui-corner-all ui-state-default'][2]")
print(min_element.location)
print(max_element.location)
act= ActionChains(driver)
act.drag_and_drop_by_offset(min_element,100,0).perform()
act.drag_and_drop_by_offset(max_element,-50,0).perform()

print(min_element.location)
print(max_element.location)

