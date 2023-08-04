from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj= Service("C:\\mybrowserdriver\\chromedriver.exe")
driver= webdriver.Chrome(service=service_obj)
driver.implicitly_wait(4)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,"input[name='username']").send_keys("Admin")
driver.find_element(By.CSS_SELECTOR,"input[name='password']").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
title= driver.title
if title=="OrangeHRM":
    print("pass")
else:
    print("fail")