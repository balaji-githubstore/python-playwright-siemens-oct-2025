import time

from selenium import webdriver
from selenium.webdriver.common.by import By


options=webdriver.ChromeOptions()
options.binary_location=r"D:\Balaji\Components\chrome-win64\chrome-win64\chrome.exe";

driver=webdriver.Chrome(options=options)

driver1=webdriver.Chrome(options=options)

driver.maximize_window()

print(type(driver))

driver.get("https://facebook.com")

print(driver.title)

driver.find_element(By.ID,"email").send_keys("hello@gmail.com")

time.sleep(5)

print(driver.current_url)
driver.quit()





