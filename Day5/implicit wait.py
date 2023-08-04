from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj= Service("C:\\mybrowserdriver\\chromedriver.exe")
driver= webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://www.google.com/")
driver.maximize_window()
element= driver.find_element(By.NAME,"q")
element.send_keys("selenium")
element.submit()


# 1) implicit wait
# driver.implicitly_wait(10)

#Adv

# 1) Single statement
# 2) Performance will not be reduced. (If the element is available within the time it proceed to execute further
# statements )

# Dis
#
# 1) If the element is not available within the time mentioned , still there is a chance of getting exception.

# 2) Explicit wait

# Explicit wait works based on condition
#
# Adv
#
# More effectively works.
#
# Dis
#
# Multiple places
# Feel some difficulty