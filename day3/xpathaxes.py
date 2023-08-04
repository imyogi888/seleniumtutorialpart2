from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj= Service("C:\\mybrowserdriver\\chromedriver.exe")
driver= webdriver.Chrome(service=service_obj)
driver.implicitly_wait(4)
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()

#self

# text_msg= driver.find_element(By.XPATH,"//a[contains(text(),'Vaibhav Global')]/self::a").text
# print(text_msg)

#parent
# text_msg= driver.find_element(By.XPATH,"//a[contains(text(),'Vaibhav Global')]/parent::td").text
# print(text_msg)

#child

# text_msg= driver.find_elements(By.XPATH,"//a[contains(text(),'Vaibhav Global')]/ancestor::tr/child::*")
# print(len(text_msg))

#ancestor

# text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'Vaibhav Global')]/ancestor::tr").text
# print(text_msg)

#Descendent
# text_msg=driver.find_elements(By.XPATH,"//a[contains(text(),'Vaibhav Global')]/ancestor::tr/descendant::*")
# print(len(text_msg))

#Following

# textmsg= driver.find_elements(By.XPATH,"//a[contains(text(),'Vaibhav Global')]/ancestor::tr/following::*")
# print(len(textmsg))

#Following-sibling
# textmsg= driver.find_elements(By.XPATH,"//a[contains(text(),'Vaibhav Global')]/ancestor::tr/following-sibling::*")
# print(len(textmsg))


#proceeding
#
# textmsg= driver.find_elements(By.XPATH,"//a[contains(text(),'Vaibhav Global')]/ancestor::tr/preceding::*")
# print(len(textmsg))

textmsg= driver.find_elements(By.XPATH,"//a[contains(text(),'Vaibhav Global')]/ancestor::tr/preceding-sibling::*")
print(len(textmsg))
