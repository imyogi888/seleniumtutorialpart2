from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj= Service("C:\\mybrowserdriver\\chromedriver.exe")
driver= webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# 1) count Number of columns and rows
no_of_columns= driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr[1]/th")
print(len(no_of_columns))

no_of_rows= driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr")
print(len(no_of_rows))

# 2) read specific row amd column data - master in selenium

# data= driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[5]/td[1]").text
# print(data)

# 3) Read all the columns and rows

# for r in range(2,len(no_of_rows)+1):
#     for c in range(1,len(no_of_columns)+1):
#         data= driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
#         print(data, end="                                   ")
#     print()

# 4) Read data based on condition (list books name whose is mukesh

for r in range(2,len(no_of_rows)+1):
    authorname= driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
    if authorname== "Mukesh":
        bookname= driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[1]").text
        price= driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[4]").text
        print(bookname,"              ",authorname,"         ",price)


