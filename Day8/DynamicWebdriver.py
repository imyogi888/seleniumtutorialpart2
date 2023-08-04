from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj= Service("C:\\mybrowserdriver\\chromedriver.exe")
driver= webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://opensource-demo.orangehrmlive.com")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
driver.find_element(By.XPATH,"//nav/div/ul/li[1]/a").click()
driver.find_element(By.XPATH,"//div/nav/ul/li[1]/span").click()
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li").click()
elements= driver.find_elements(By.XPATH,"//div[@class='oxd-table-body']/div/div/div[5]")

# rows= len(elements)
# count=0
# for ele in elements:
#     if ele.text == "Enabled":
#         count=count+1
# print("total number of rows",rows)
# print("total number of enabled user",count)
# print("total number of disabled user", rows-count)

# 2 nd approach

# rows= len(driver.find_elements(By.XPATH,"//div[@class='oxd-table-body']/div"))
# print("total number of rows", rows)
# count= 0
# for r in range(1,rows+1):
#     status= driver.find_element(By.XPATH,"//div[@class='oxd-table-body']/div["+str(r)+"]/div/div[5]").text
#     if status== "Enabled":
#         count= count+1
#
# print(count)

