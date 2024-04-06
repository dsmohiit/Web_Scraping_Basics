# EXTRACTING THE HTML CONTENT OF A WEBSITE


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Creating a service
s = Service(r"C:\Users\acmoh\Desktop\chromedriver.exe")

# Creating a driver object
driver = webdriver.Chrome(service= s)
driver.get('https://www.ajio.com/men-backpacks/c/830201001')
time.sleep(1)

old_height = driver.execute_script('return document.body.scrollHeight')

counter = 1
while True:

    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(2)

    new_height = driver.execute_script('return document.body.scrollHeight')
    counter = counter + 1

    print(counter)
    print(old_height)
    print(new_height)

    if new_height == old_height:
        break

    old_height = new_height

html = driver.page_source

with open('ajio.html', 'w', encoding= 'utf-8') as f:
    f.write(html)










