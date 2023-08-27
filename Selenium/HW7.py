import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/7/7.html'
sum = 0

with webdriver.Chrome() as browser:
    browser.get(url)
    nums = browser.find_elements(By.TAG_NAME, 'option')
    for num in nums:
        sum += int(num.text)
    input_bar = browser.find_element(By.ID, 'input_result')
    input_bar.send_keys(sum)
    button = browser.find_element(By.CLASS_NAME, 'btn_box')
    button.click()
    time.sleep(15)