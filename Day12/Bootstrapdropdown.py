from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj= Service("C:\\mybrowserdriver\\chromedriver.exe")
driver= webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
driver.find_element(By.ID,"select2-billing_country-container").click()
countries= driver.find_elements(By.XPATH,"//span/ul/li")
for country in countries:
    if country.text=="Albania":
        country.click()
        break