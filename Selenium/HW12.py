from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By as by

url = 'https://parsinger.ru/methods/5/index.html'
max = 0
l = ''

with webdriver.Chrome() as browser:
    browser.get(url)
    hrefs = [i.get_attribute('href') for i in browser.find_elements(by.TAG_NAME, 'a')]
    for link in hrefs:
        browser.get(link)
        cookies = browser.get_cookies()
        for cookie in cookies:
            if int(cookie['expiry']) > max:
                max = int(cookie['expiry'])
                l = link
    browser.get(l)
    res = browser.find_element(by.ID, 'result').text

    print(res)