from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj= Service("C:\\mybrowserdriver\\chromedriver.exe")
driver= webdriver.Chrome(service=service_obj)
mywait= WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[NoSuchElementException,
                                                                     ElementNotVisibleException,
                                                                     ElementNotSelectableException,
                                                                     Exception])

driver.get("https://www.google.com/")
element=driver.find_element(By.NAME,"q")
element.send_keys("selenium")
element.submit()
selenium= mywait.until(expected_conditions.presence_of_element_located((By.XPATH,"//h3[text()='Selenium']")))
selenium.click()
