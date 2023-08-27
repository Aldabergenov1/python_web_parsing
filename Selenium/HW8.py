import time
import numexpr
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/6/6.html'

with webdriver.Chrome() as browser:
    browser.get(url)
    equation = browser.find_element(By.ID,'text_box').text
    print(equation)
    res = numexpr.evaluate(equation)
    variants = browser.find_elements(By.TAG_NAME, 'option')
    button = browser.find_element(By.CLASS_NAME, 'btn')
    for var in variants:
        if int(res) == int(var.text):
            var.click()
            button.click()
    time.sleep(25)