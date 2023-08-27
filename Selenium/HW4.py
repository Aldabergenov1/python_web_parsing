import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/3/3.html'
sum = 0

with webdriver.Chrome() as browser:
    browser.get(url)
    nums = browser.find_elements(By.XPATH, "//div[@class='text']/p[2]")
    for n in nums:
        sum += int(n.text)
    
print(sum)
    