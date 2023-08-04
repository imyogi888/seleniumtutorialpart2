from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj= Service("C:\\mybrowserdriver\\chromedriver.exe")
ops= webdriver.ChromeOptions()
ops.add_argument("--disable-notification")
driver= webdriver.Chrome(service=service_obj,options=ops)
driver.get("https://whatmylocation.com/")
driver.maximize_window(),