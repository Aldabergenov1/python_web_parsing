import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/4/4.html'

with webdriver.Chrome() as browser:
    browser.get(url)
    check_boxes = browser.find_elements(By.CLASS_NAME, 'check')
    for box in check_boxes:
        box.click()
    button = browser.find_element(By.CLASS_NAME, 'btn')
    button.click()
    res = browser.find_element(By.ID, 'result')
    print(res.text)
    time.sleep(10)