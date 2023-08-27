import csv
import time
import json
from tqdm import tqdm
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By as by
from selenium.webdriver.chrome.service import Service

def get_data(url):
    options_chrome = webdriver.ChromeOptions()
    options_chrome.add_argument('user-data-dir=C:\\Users\\Appdata\\Local\\Google\\Chrome\\User Data')
    options_chrome.add_argument('--headless=chrome')
    options_chrome.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")
    service = Service(executable_path='C:\chromedriver-win64\chromedriver.exe')

    with open('tamish.csv', 'w', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Наименование', 'Цена', 'Цена без скидки', 
                        'Страна производитель', 'Размеры', 'Состав',
                        'Изображения', 'Ссылка'])
    
    with webdriver.Chrome(options=options_chrome, service=service) as browser:
        browser.set_script_timeout(99999999)
        browser.get(url)
        time.sleep(3)
        
        nav_menu = browser.find_element(by.CLASS_NAME, 'level1.headcat').find_elements(by.TAG_NAME, 'li')
        categories = [a.find_element(by.TAG_NAME, 'a').get_attribute('href') for a in nav_menu]
        
        for category in tqdm(categories):
            browser.get(category)
            time.sleep(3)
            items = browser.find_element(by.XPATH, '//*[@id="content"]/div[2]').find_elements(by.TAG_NAME, 'div')
            
            for item in items:
                try:
                    link = item.find_element(by.TAG_NAME, 'a').get_attribute('href')
                except:
                    continue
                
                browser.get(link)
                time.sleep(0.5)
                name = browser.find_element(by.CLASS_NAME, 'buttons').find_element(by.TAG_NAME, 'h1').text
                price_box = browser.find_element(by.CLASS_NAME, 'pull-right.info-right.col-sm-5.nopad')
                
                try:
                    price = price_box.find_element(by.ID, 'formated_special').text
                    old_price = price_box.find_element(by.ID, 'formated_price').text
                except:
                    price = price_box.find_element(by.ID, 'formated_price').text
                    old_price = '-'
                try:
                    country = browser.find_element(by.XPATH, '//*[@id="tab-specification"]/table/tbody/tr[1]/td[2]')
                    size = browser.find_element(by.XPATH, '//*[@id="tab-specification"]/table/tbody/tr[2]/td[2]')
                    compound = browser.find_element(by.XPATH, '//*[@id="tab-specification"]/table/tbody/tr[3]/td[2]')
                except:
                    print(link)
                images = [i.get_attribute('src') for i in browser.find_element(by.CLASS_NAME, 'owl-wrapper-outer').find_elements(by.TAG_NAME, 'img')]

                row = name, price, old_price, country, size, compound, images, link
                with open('tamish.csv', 'a', encoding='utf-8-sig', newline='') as file:
                    writer = csv.writer(file, delimiter=';')
                    writer.writerow(row)    
                
        

def main():
    get_data('https://tamish.kz/')

if __name__ == '__main__':
    main()