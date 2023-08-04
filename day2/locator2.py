from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\mybrowserdriver\\chromedriver.exe")
driver= webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("http://automationpractice.com/index.php")
driver.maximize_window()
sliders= driver.find_elements(By.CLASS_NAME,'homeslider-container')
print(sliders)
links= driver.find_elements(By.TAG_NAME,'a')
print(links)
