import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/1/1.html'

with webdriver.Chrome() as browser:
    browser.get(url)
    inputs = browser.find_elements(By.TAG_NAME, 'input')
    button = browser.find_element(By.CLASS_NAME, 'btn')
    for input in inputs:
        input.send_keys('text')
        button.click()
    time.sleep(10)        