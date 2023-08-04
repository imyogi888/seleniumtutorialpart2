from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj= Service("C:\\mybrowserdriver\\chromedriver.exe")
driver= webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
driver.switch_to.frame(0)
#driver.find_element(By.ID,"datepicker").send_keys("08/09/2023")
driver.find_element(By.ID,"datepicker").click()
mon="January"
ye="2020"
da= "18"
while True:
    month = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    year = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
    if mon==month and ye==year:
        break
    else:
        driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-w']").click()

dates= driver.find_elements(By.XPATH,"//table/tbody/tr/td/a")
for date in dates:
    if date.text==da:
        date.click()
        break
