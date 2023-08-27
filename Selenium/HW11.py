from selenium import webdriver

url = 'https://parsinger.ru/methods/3/index.html'
sum = 0

with webdriver.Chrome() as browser:
    browser.get(url)
    cookies = browser.get_cookies()
    for cookie in cookies:
        if int(cookie['name'].split('_')[-1])%2 == 0:
            sum += int(cookie['value'])

print(sum)