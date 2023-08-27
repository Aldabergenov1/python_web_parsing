import time
from selenium import webdriver

options_chrome = webdriver.ChromeOptions()
options_chrome.add_extension(r'C:\Users\makha\AppData\Local\Google\Chrome\User Data\Default\Extensions\gkkmpbaijflcgbbdfjgihbgmpkhgpgof\0.2_0.crx')

with webdriver.Chrome(options= options_chrome) as browser:
    url = 'https://yandex.ru/'
    browser.get(url)
    time.sleep(30)