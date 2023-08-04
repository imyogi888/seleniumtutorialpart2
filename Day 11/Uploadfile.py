from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj= Service("C:\\mybrowserdriver\\chromedriver.exe")
driver= webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://www.foundit.in/")
driver.maximize_window()
driver.find_element(By.XPATH,"//div[@class='heroSection-buttonContainer_secondaryBtn secondaryBtn']").click()
driver.find_element(By.CSS_SELECTOR,"#file-upload").send_keys("C:\\Users\\DeLL\\Documents//Resume (8).pdf")