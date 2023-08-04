from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

service_obj= Service("C:\\mybrowserdriver\\chromedriver.exe")
driver= webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

#Capture Cookies from the browser
cookies= driver.get_cookies()
print("size of cookies",len(cookies))

#print details of cookies

# for c in cookies:
#     print(c.get("name"),":",c.get("value"))
#     print(c)



#Add new cookie to the browser

driver.add_cookie({"name":"mycookie","value":"123456"})
cookies= driver.get_cookies()
print("size of cookies after adding one:",len(cookies))

# delete specific  cookie from the browser

driver.delete_cookie("mycookie")
cookies= driver.get_cookies()
print("size of cookies after deleting one:",len(cookies))

#delete all ten cookies

driver.delete_all_cookies()
cookies= driver.get_cookies()
print("size of cookies after deleted one:",len(cookies))
