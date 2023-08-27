import csv
import requests
from bs4 import BeautifulSoup

index_labels = {1: "watch", 2: "mobile", 3: "mouse", 
                4: "hdd", 5: "headphones"}

with open('res4.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Наименование', 'Артикул', 'Бренд', 
                     'Модель', 'Наличие', 'Цена', 'Старая цена', 'Ссылка'])

for i in range(1, 6):
    print(f'Страница номер {i}')
    for j in range(1, 33):
        print(f'Товар номер {j}')
        url = f'https://parsinger.ru/html/{index_labels[i]}/{i}/{i}_{j}.html'
        response = requests.get(url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        
        name = soup.find('p', id='p_header').text
        article = soup.find('p', class_='article').text.split(': ')[1]
        brand = soup.find('li', id='brand').text.split(': ')[1]
        model = soup.find('li', id='model').text.split(': ')[1]
        amount = soup.find('span', id='in_stock').text
        price = soup.find('span', id='price').text
        old_price = soup.find('span', id='old_price').text
        
        row = name, article, brand, model, amount, price, old_price, url
        file = open('res4.csv', 'a', encoding='utf-8-sig', newline='')
        writer = csv.writer(file, delimiter=';')
        writer.writerow(row)