from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

from selenium.webdriver.common.by import By

location= os.getcwd()

def chromesetup():
    service_obj = Service("C:\\mybrowserdriver\\chromedriver.exe")
    preferences = {"download.default_directory": location,"plugins.always_open_pdf_externally":True}
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs", preferences)
    driver = webdriver.Chrome(service=service_obj,options=ops)
    return driver

driver=chromesetup()

# def edgesetup():
#     service_obj = Service("C:\\mybrowserdriver\\chromedriver.exe")
#     preferences = {"download.default_directory": location}
#     ops = webdriver.EdgeOptions()
#     ops.add_experimental_option("prefs", preferences)
#     driver = webdriver.Edge(service=service_obj,options=ops)
#     return driver
#
#
# driver= edgesetup()



# def firefoxsetup():
#     service_obj = Service("C:\\mybrowserdriver\\chromedriver.exe")
#     ops = webdriver.FirefoxOptions()
#     ops.set_preference("browser.helperApps.neverAsk.saveToDisk","application/msword")
#     ops.set_preference("browser.download.manager.showWhenStarting",False)
#     ops.set_preference("browser.download.folderList",2)
#     ops.set_preference("browser.download.dir",location)
#
#     driver = webdriver.Firefox(service=service_obj, options=ops)
#     return driver

# driver= firefoxsetup()
driver.implicitly_wait(5)
# driver.get("https://file-examples.com/index.php/simple-documents-download/sample-doc-download/")
driver.get("https://file-examples.com/index.php/simple-documents-download/sample-pdf-download/")
driver.maximize_window()
driver.find_element(By.XPATH,"//*[@id='table-files']/tbody/tr[1]/td[5]/a").click()

