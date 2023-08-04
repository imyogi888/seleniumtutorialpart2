from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj= Service("C:\\mybrowserdriver\\chromedriver.exe")
driver= webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://text-compare.com/")
driver.maximize_window()
input1= driver.find_element(By.ID,"inputText1")
input2= driver.find_element(By.ID,"inputText2")

input1.send_keys("welcome to home")

act= ActionChains(driver)
#input1-----> ctrl+a select the text

act.key_down(Keys.CONTROL)
act.send_keys("a")
act.key_up(Keys.CONTROL)
act.perform()



# COPY
act.key_down(Keys.CONTROL)
act.send_keys("c")
act.key_up(Keys.CONTROL)
act.perform()


#TAB
act.send_keys(Keys.TAB).perform()


# Pastefi

act.key_down(Keys.CONTROL)
act.send_keys("v")
act.key_up(Keys.CONTROL)
act.perform()