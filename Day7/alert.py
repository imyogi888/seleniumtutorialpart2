import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj= Service("C:\\mybrowserdriver\\chromedriver.exe")
driver= webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
driver.find_element(By.XPATH,"//button[text()='Click for JS Prompt']").click()
time.sleep(3)
alertmsg= driver.switch_to.alert
print(alertmsg.text)
alertmsg.send_keys("lya hua bhai")
#alertmsg.accept()
alertmsg.dismiss()
