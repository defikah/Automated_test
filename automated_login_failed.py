from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://github.com/login")
time.sleep(2)
driver.find_element_by_id("login_field").send_keys("gmail")
time.sleep(1)
driver.find_element_by_id("password").send_keys("wrong password")
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[3]/main/div/div[4]/form/input[14]").click()
time.sleep(5)
driver.close()
print ("Failed")
