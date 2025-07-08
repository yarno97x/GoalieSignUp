from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome()  
driver.get('https://goalieup.com/en/user')

def connect() :
    driver.find_element(By.NAME, "name").send_keys("yarnogrenier@gmail.com")
    driver.find_element(By.NAME, "pass").send_keys("9jaz84P6&abc")
    driver.find_element(By.NAME, "op").click() 
    time.sleep(100)

connect()

# Print page title
print(driver.title)

# Close the browser
driver.quit()

