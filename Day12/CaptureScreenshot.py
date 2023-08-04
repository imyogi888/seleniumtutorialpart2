from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os

service_obj= Service("C:\\mybrowserdriver\\chromedriver.exe")
driver= webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
# driver.save_screenshot("C:\\Users\\DeLL\\PycharmProjects\\seleniumtutorialpart2\\Day12\\homepage.png")
# driver.save_screenshot(os.getcwd()+"//homepage2.png")
# driver.get_screenshot_as_file(os.getcwd()+"homepage3.png")
# driver.get_screenshot_as_file()
# driver.get_screenshot_as_base64()