from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj= Service("C:\\mybrowserdriver\\chromedriver.exe")
driver= webdriver.Chrome(service=service_obj)
driver.implicitly_wait(9)
driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()
act= ActionChains(driver)
act.context_click(driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")).perform()