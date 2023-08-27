import csv
import requests
from bs4 import BeautifulSoup

#создаю файл, заголовки
with open('res1.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Наименование', 'Бренд', 'Форм-фактор', 'Ёмкость', 'Объём буф. памяти', 'Цена'])

#запускаю цикл для пагинации
for i in range(1, 5):
    #готовлю суп
    url = f'https://parsinger.ru/html/index4_page_{i}.html'
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    
    #собираю данные для заполнения столбцов
    name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
    description = [x.text.split('\n') for x in soup.find_all('div', class_='description')]
    price = [x.text.split(' ')[0] for x in soup.find_all('p', class_='price')]
    
    #упаковываю данные
    for item, descr, price in zip(name, description, price):
        row = item, *[x.split(':')[1] for x in descr if x], price
        
        file = open('res1.csv', 'a', encoding='utf-8-sig', newline='')
        writer = csv.writer(file, delimiter=';')
        writer.writerow(row)
    file.close()
