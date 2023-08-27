import csv
import requests
from bs4 import BeautifulSoup

#создаю файл
with open('res2.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')

#вложеннй цикл для того чтобы пробежаться по всем страницам всех разделов
for i in range(1, 6):
    for j in range(1, 5):
        url = f'https://parsinger.ru/html/index{i}_page_{j}.html'
        response = requests.get(url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')

        name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
        description = [x.text.split('\n') for x in soup.find_all('div', class_='description')]
        price = [x.text for x in soup.find_all('p', class_='price')]
        
        for item, descr, price in zip(name, description, price):
            row = item, *[x.split(':')[1] for x in descr if x], price
        
            file = open('res2.csv', 'a', encoding='utf-8-sig', newline='')
            writer = csv.writer(file, delimiter=';')
            writer.writerow(row)
        file.close()