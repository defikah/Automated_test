from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.google.com/")
driver.find_element_by_name("q").send_keys("belajar python satu hari")
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[2]/div[1]/div[3]/center/input[1]").click()
time.sleep(5)
driver.close()
print ("success running robot program")
