from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj= Service("C:\\mybrowserdriver\\chromedriver.exe")
driver= webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
driver.find_element(By.ID,"dob").click()
dropdown= Select(driver.find_element(By.CSS_SELECTOR,".ui-datepicker-month"))
dropdown.select_by_visible_text("Jan")
dropdown2= Select(driver.find_element(By.CSS_SELECTOR,".ui-datepicker-year"))
dropdown2.select_by_visible_text("2008")

dates= driver.find_elements(By.XPATH,"//table/tbody/tr/td/a")
for date in dates:
    if date.text=="17":
        date.click()
        break
