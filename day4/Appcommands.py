from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj= Service("C:\\mybrowserdriver\\chromedriver.exe")
driver= webdriver.Chrome(service=service_obj)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
print(driver.page_source)