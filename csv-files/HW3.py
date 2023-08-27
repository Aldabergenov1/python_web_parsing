import csv
import requests
from bs4 import BeautifulSoup

with open('res3.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    first_row = ['Наименование', 'Артикул', 'Бренд', 
                 'Модель', 'Тип', 'Технология экрана', 
                 'Материал корпуса', 'Материал браслета', 'Размер', 
                 'Сайт производителя', 'Наличие', 'Цена', 'Старая цена', 
                 'Ссылка на карточку с товаром']
    writer.writerow(first_row)

for i in range(1, 33):
    url = f'https://parsinger.ru/html/watch/1/1_{i}.html'
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    
    name = soup.find('p', id='p_header').text
    article = soup.find('p', class_='article').text.split(': ')[1]
    brand = soup.find('li', id='brand').text.split(': ')[1]
    model = soup.find('li', id='model').text.split(': ')[1]
    typpe = soup.find('li', id='type').text.split(': ')[1]
    display = soup.find('li', id='display').text.split(': ')[1]
    frame_material = soup.find('li', id='material_frame').text.split(': ')[1]
    bracer_material = soup.find('li', id='material_bracer').text.split(': ')[1]
    size = soup.find('li', id='size').text.split(': ')[1]
    site = soup.find('li', id='site').text.split(': ')[1]
    amount = soup.find('span', id='in_stock').text.split(': ')[1]
    price = soup.find('span', id='price').text
    old_price = soup.find('span', id='old_price').text
    
    row = name, article, brand, model, typpe, display, frame_material, bracer_material, size, site, amount, price, old_price, url
        
    file = open('res3.csv', 'a', encoding='utf-8-sig', newline='')
    writer = csv.writer(file, delimiter=';')
    writer.writerow(row)