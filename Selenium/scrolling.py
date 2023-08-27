import time
from selenium import webdriver

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/scroll/1/')
    for i in range(10):
        browser.execute_script("window.scrollBy(0,5000)")
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        height = browser.execute_script("return document.body.scrollHeight")
        visible_height = browser.execute_script("return window.innerHeight")
        time.sleep(2)
        print(height)
        
    """
    887 пикселей имеет видимая часть нашего сайта. 
    Иногда необходимо, чтобы требуемый элемент находился в видимой области, 
    т.к. методы .click(), .send_keys() и др. не могут быть совершены, 
    если элемент не находится в видимой области экрана.
    """