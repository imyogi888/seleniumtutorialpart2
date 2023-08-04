from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj= Service("C:\\mybrowserdriver\\chromedriver.exe")
driver= webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://www.amazon.in/")
driver.maximize_window()

#TAG&ID

# driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("abc@gmail.com")
# driver.find_element(By.CSS_SELECTOR,'input#pass').send_keys("ddedh")
# driver.find_element(By.CSS_SELECTOR,'#pass').send_keys("ddedh")


#TAG AND CLASS
#driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("njfnn")

#TAG AND ATTRIBUTE

#driver.find_element(By.CSS_SELECTOR,"input[data-testid='royal_email']").send_keys("djdwdbjb")
#driver.find_element(By.CSS_SELECTOR,"[data-testid=royal_email]").send_keys("djdwdbjb")


#TAG,CLASS AND ATTRIBUTE

#driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal_pass]").send_keys("awara")

# DIFF BETWEEN ABSOLUTE AND RELATIVE XPATHS

# 1) Absoute xpaths starts from root html node
# Relative xpath directly jump to element on DOM

# 2) Absolute xpath start with /
 # Relative xpath start with //

# 3) In absolute xpath we use only tags/nodes
#   In Relative xpath we use attrtbutes

# 2 reason to choose realtive xpath
# 1) if developer introduced new element then absolute xpath will be broken
# 2) if developer changed the location then absolute xpath will be broken


driver.find_element(By.XPATH,"//input[contains(@id,'two')]").send_keys("iphone")
driver.find_element(By.XPATH,"//input[starts-with(@id,'nav')]").click()









# driver.find_element(By.LINK_TEXT,"Sign In").click()
# driver.find_element(By.XPATH,"//button[text()='Log in with Adobe ID']").click()
# driver.find_element(By.CSS_SELECTOR,"#EmailPage-EmailField").send_keys("qai18153+story@adobetest.com")
# driver.find_element(By.XPATH,"//span[text()='Continue']").click()
# driver.find_element(By.CSS_SELECTOR,"#PasswordPage-PasswordField").send_keys("Adobe123")
# driver.find_element(By.XPATH,"//span[text()='Continue']").click()