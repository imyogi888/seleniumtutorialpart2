from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def headless():
    service_obj= Service("C:\\mybrowserdriver\\chromedriver.exe")
    ops= webdriver.ChromeOptions()
    ops.headless=True
    driver= webdriver.Chrome(service=service_obj,options=ops)
    return driver

driver= headless()
driver.get("https://demo.nopcommerce.com/")
print(driver.title)