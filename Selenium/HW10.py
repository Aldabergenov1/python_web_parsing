from selenium import webdriver
from pprint import pprint

url = 'https://parsinger.ru/methods/3/index.html'
sum = 0

with webdriver.Chrome() as browser:
    browser.get(url)
    cookies = browser.get_cookies()
    for cookie in cookies:
        sum += int(cookie['value'])
        
print(sum)