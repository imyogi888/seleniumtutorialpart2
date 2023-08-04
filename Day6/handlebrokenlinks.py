# import requests
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# service_obj= Service("C:\\mybrowserdriver\\chromedriver.exe")
# driver= webdriver.Chrome(service=service_obj)
# driver.implicitly_wait(5)
# driver.get("http://www.deadlinkcity.com/")
# driver.maximize_window()
# brokelink= driver.find_elements(By.TAG_NAME,"a")
# count= 0
# for link in brokelink:
#     url= link.get_attribute('href')
#     try:
#         res = requests.head(url)
#     except:
#         None
#
#     if res.status_code >= 400:
#         print(url, "is a broken link")
#         count+=1
#     else:
#         print(url, "is valid link")
#
# print("total number of broken links:",count)
#

