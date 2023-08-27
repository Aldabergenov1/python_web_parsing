import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/3/3.html'
sum = 0

with webdriver.Chrome() as browser:
    browser.get(url)
    p_els = browser.find_elements(By.TAG_NAME, 'p')
    for p in p_els:
        sum += int(p.text)

print(sum)