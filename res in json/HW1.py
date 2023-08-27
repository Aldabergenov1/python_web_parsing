import json
import requests
from bs4 import BeautifulSoup

#создаём "промежуточный" суп для получения пагинации
url = 'https://parsinger.ru/html/index3_page_1.html'
response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')

pages = soup.find('div', class_='pagen').find_all('a') #получаем число страниц

res_json = [] #создаём результирующий json

#цикл чтобы пробежаться по страницам
for i in range(len(pages)):
    print(f'Страница {i+1} из {len(pages)}')
    #снова делаю суп, с учётом пагинации
    url = f'https://parsinger.ru/html/index3_page_{i+1}.html'
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    
    #получаем список имён, список списков описаний, список цен
    names = [x.text for x in soup.find_all('a', class_='name_item')]
    descriptions = [x.text.strip().split('\n') for x in soup.find_all('div', class_='description')]
    prices = [x.text for x in soup.find_all('p', class_='price')]

    #упаковываем всё в json, присваиваем нужнм именам нужные значения
    for name, description, price in zip(names, descriptions, prices):
        res_json.append({
            'name': name.strip(), 
            'brand': [x.split(':')[1].strip() for x in description][0],
            'type': [x.split(':')[1].strip() for x in description][1],
            'connect': [x.split(':')[1].strip() for x in description][2],
            'game': [x.split(':')[1].strip() for x in description][3],
            'prce': price
        })

#создаём json-файл
with open('res.json', 'w', encoding='utf-8') as file:
    json.dump(res_json, file, indent=4, ensure_ascii=False)

print('Ответ в виде json записан!')