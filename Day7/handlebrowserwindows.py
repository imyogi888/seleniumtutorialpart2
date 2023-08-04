from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj= Service("C:\\mybrowserdriver\\chromedriver.exe")
driver= webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
driver.find_element(By.LINK_TEXT,'OrangeHRM, Inc').click()
windowid= driver.window_handles

# parentwindow= windowid[0]
# childwindow= windowid[1]
# driver.switch_to.window(childwindow)
# print(driver.title)
# driver.switch_to.window(parentwindow)
# print(driver.title)



#Approach2
# for win in windowid:
#     driver.switch_to.window(win)
#     print(driver.title)



for win in windowid:
    driver.switch_to.window(win)
    if driver.title=="OrangeHRM":
        driver.close()








