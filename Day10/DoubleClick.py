from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj= Service("C:\\mybrowserdriver\\chromedriver.exe")
driver= webdriver.Chrome(service=service_obj)
driver.implicitly_wait(9)
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")
driver.maximize_window()
driver.switch_to.frame("iframeResult")
elements= driver.find_element(By.ID,"field1")
elements.clear()
elements.send_keys("good morning")
act= ActionChains(driver)
act.double_click(driver.find_element(By.XPATH,"//button[text()='Copy Text']")).perform()
