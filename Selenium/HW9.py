import time
from selenium import webdriver
from selenium.webdriver.common.by import By as by

url = 'https://parsinger.ru/methods/1/index.html'

with webdriver.Chrome() as browser:
    browser.get(url)
    flag = True
    while flag:
        res = browser.find_element(by.ID, 'result').text
        if res.isdigit():
            print(res)
            flag = False
        browser.refresh()