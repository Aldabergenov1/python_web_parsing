import time
from selenium import webdriver
from selenium.webdriver.common.by import By as by
from pprint import pprint

url = 'https://whey.kz/shop/chikalab-mulatta-pasta-s-fundukom-250-gr/'
res = []

options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('user-data-dir=C:\\Users\\Appdata\\Local\\Google\\Chrome\\User Data')
options_chrome.add_argument('--headless=chrome')
options_chrome.add_argument(f"--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")

with webdriver.Chrome(options=options_chrome) as browser:
    browser.get(url)
    time.sleep(2)
    res.append({
                'Наименование': browser.find_element(by.CLASS_NAME, 'product-title.product_title.entry-title').text,
                'Производитель': browser.find_element(by.CLASS_NAME, 'yith-wcbr-brands').find_element(by.TAG_NAME, 'a').text,
                'Цена без скидки': browser.find_element(by.CLASS_NAME, 'price-wrapper').find_element(by.TAG_NAME, 'del').text,
                'Цена со скидкой': browser.find_element(by.CLASS_NAME, 'price-wrapper').find_element(by.TAG_NAME, 'ins').text,                    
                'Артикул': browser.find_element(by.CLASS_NAME, 'sku').text, 
                'Категория': browser.find_element(by.CLASS_NAME, 'product_meta').find_element(by.CLASS_NAME, 'posted_in').find_element(by.TAG_NAME, 'a').text,
                'Ссылка': url
            })

    pprint(res)