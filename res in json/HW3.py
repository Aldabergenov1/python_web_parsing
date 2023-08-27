import requests
import json
from bs4 import BeautifulSoup

def create_soup(url: str):
    response = requests.get(url)
    response.encoding = 'utf-8'
    return BeautifulSoup(response.text, 'lxml')

labels = {1: 'watch', 2: 'mobile', 3: 'mouse', 
          4: 'hdd', 5: 'headphones'}

res_json = []

for i in range(1, 6):
    print(f'Секция {i} из 5')
    for j in range(1, 33):
        url = f'https://parsinger.ru/html/{labels[i]}/{i}/{i}_{j}.html'
        soup = create_soup(url)
        
        name = soup.find('p', id='p_header').text
        article = soup.find('p', class_='article').text
        params = soup.find('ul', id='description').find_all('li')
        amount = soup.find('span', id='in_stock').text
        price = soup.find('span', id='price').text
        old_price = soup.find('span', id='old_price').text
        
        res_json.append({
            'Наименование': name,
            'Артикул': article.split(': ')[1],
            [x.text.split(':')[0].strip() for x in params][0]:[x.text.split(':')[1].strip() for x in params][0],
            [x.text.split(':')[0].strip() for x in params][1]:[x.text.split(':')[1].strip() for x in params][1],
            [x.text.split(':')[0].strip() for x in params][2]:[x.text.split(':')[1].strip() for x in params][2],
            [x.text.split(':')[0].strip() for x in params][3]:[x.text.split(':')[1].strip() for x in params][3],
            [x.text.split(':')[0].strip() for x in params][4]:[x.text.split(':')[1].strip() for x in params][4],
            [x.text.split(':')[0].strip() for x in params][5]:[x.text.split(':')[1].strip() for x in params][5],
            [x.text.split(':')[0].strip() for x in params][6]:[x.text.split(':')[1].strip() for x in params][6],
            [x.text.split(':')[0].strip() for x in params][7]:[x.text.split(':')[1].strip() for x in params][7],
            'В наличии': amount,
            'Цена': price,
            'Цена без скидки': old_price
        })

with open('res3.json', 'w', encoding='utf-8') as file:
    json.dump(res_json, file, indent=4, ensure_ascii=False)
    
print('Файл res3.json создан!')