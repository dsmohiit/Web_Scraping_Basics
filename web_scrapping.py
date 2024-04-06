# LEARNING BASICS OF AUTOMATION

# Open google.com
# Search "CampusX"
# learnwith.campusx.in
# DSMP enroll page

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Create a Chrome service instance
s = Service(r"C:\Users\acmoh\Desktop\chromedriver.exe")

# Create a Chrome WebDriver instance and pass the service
driver = webdriver.Chrome(service=s)

# Now opening the google
driver.get("http://google.com")
time.sleep(2)

# Fetching the search bar
user_input = driver.find_element(by=By.XPATH,
                                 value="/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea")
user_input.send_keys("CampusX")
time.sleep(1)

user_input.send_keys(Keys.ENTER)
time.sleep(1)

link = driver.find_element(by=By.XPATH,
                           value='//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a')
link.click()
time.sleep(1)

link2 = driver.find_element(by=By.XPATH,
                            value='//*[@id="1698390585510d"]/div/div[1]/div/div/div/div[1]/div/div/div[2]/a[2]')
link2.click()
time.sleep(100)
