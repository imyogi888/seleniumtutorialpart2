from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj= Service("C:\\mybrowserdriver\\chromedriver.exe")
driver= webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.implicitly_wait(5)

checkbox= driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")

# Approach 1
# select all checkboxes
# for checkboxes in checkbox:
#     checkboxes.click()

# select multiple checkboxes by choice
# Approach 2
# for checkboxes in checkbox:
#     week= checkboxes.get_attribute("id")
#     if week == "monday" or week=="sunday":
#         checkboxes.click()

# Select last two checkboxes
# Approach 3
# for i in range(len(checkbox)-2,len(checkbox)):
#     checkbox[i].click()

# Select first two checkboxes
# Approach 4
# for i in range(len(checkbox)):
#     if i<2:
#         checkbox[i].click()


# 6) Clearing all the checkboxes
# for checkboxes in checkbox:
#     if checkboxes.is_selected():
#         checkboxes.click()










