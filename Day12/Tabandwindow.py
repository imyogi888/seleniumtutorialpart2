from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

service_obj= Service("C:\\mybrowserdriver\\chromedriver.exe")
driver= webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)
# driver.get("https://demo.nopcommerce.com")
# driver.maximize_window()
# regilink=Keys.CONTROL+Keys.RETURN
# driver.find_element(By.XPATH,"//a[text()='Register']").send_keys(regilink)

#New tab- Selenium4: Opens a new tab annd switches to new tab
driver.get("https://www.opencart.com/")
driver.switch_to.new_window('tab')
driver.get("https://www.orangehrm.com/")


#New window- Selenium4 : Opens a new browser window and switches to new window

driver.get("https://www.opencart.com/")
driver.switch_to.new_window('window')
driver.get('https://www.orangehrm.com/')
