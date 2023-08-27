import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/2/2.html'

with webdriver.Chrome() as browser:
    browser.get(url)
    page = browser.find_element(By.PARTIAL_LINK_TEXT, '16243162441624')
    page.click()
    res = browser.find_element(By.ID, 'result')
    print(res.text)
    
    