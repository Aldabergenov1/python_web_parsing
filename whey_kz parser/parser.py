import time
import json
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.common.by import By as by
from selenium.webdriver.chrome.service import Service

def get_data(url):
    options_chrome = webdriver.ChromeOptions()
    options_chrome.add_argument('user-data-dir=C:\\Users\\Appdata\\Local\\Google\\Chrome\\User Data')
    options_chrome.add_argument('--headless=chrome')
    options_chrome.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")
    service = Service(executable_path='C:\chromedriver-win64\chromedriver.exe')
    res = []
    
    with webdriver.Chrome(options=options_chrome, service=service) as browser:
        browser.set_script_timeout(9999999999)
        browser.get(url)
        time.sleep(3)
        
        category_block = browser.find_element(by.CLASS_NAME, 'product-categories').find_elements(by.TAG_NAME, 'li')
        categories = [category.find_element(by.TAG_NAME, 'a').get_attribute('href') for category in category_block]
        hrefs = [] 
        
        for i in tqdm(categories): 
            browser.get(i) 
            try: 
                divs = browser.find_elements(by.CSS_SELECTOR, '.products.row.row-small.large-columns-4.medium-columns-3.small-columns-2 div.product-small') 
                hrefs += [l.find_element(by.TAG_NAME, 'a').get_attribute('href') for l in divs] 
            except: 
                print("No item in that category!") 
                
        hrefs = list(dict.fromkeys(hrefs))
                
        for link in tqdm(hrefs):
            browser.get(link)
            time.sleep(0.5)
            try:
                old_price = browser.find_element(by.CLASS_NAME, 'price-wrapper').find_element(by.TAG_NAME, 'del').text
            except:
                old_price = '-'
            try:
                article = browser.find_element(by.CLASS_NAME, 'sku').text
            except:
                article = '-'
            try:
                price = browser.find_element(by.CLASS_NAME, 'price.product-page-price.price-on-sale').find_element(by.TAG_NAME, 'ins').text
            except:
                price = browser.find_element(by.CLASS_NAME, 'price.product-page-price.price-on-sale').text
            try:
                res.append({
                    
                        'Наименование': browser.find_element(by.CLASS_NAME, 'product-title.product_title.entry-title').text,
                        'Производитель': browser.find_element(by.CLASS_NAME, 'yith-wcbr-brands').find_element(by.TAG_NAME, 'a').text,
                        'Цена без скидки': old_price,
                        'Цена': price,                  
                        'Артикул': article, 
                        'Категория': browser.find_element(by.CLASS_NAME, 'posted_in').text,
                        'Ссылка': url
                    })
            except:
                print(link)

    with open('whey_kz.json', 'w', encoding='utf-8') as file:
        json.dump(res, file, indent=4, ensure_ascii=False)
        
    print('Файл создан!')

def main():
    get_data('https://whey.kz/product-category/5-htp-tryptophan-cat/')

if __name__ == '__main__':
    main()