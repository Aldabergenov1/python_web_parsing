import requests
import json
from bs4 import BeautifulSoup


def create_soup(url):
    response = requests.get(url)
    response.encoding = 'UTF-8'
    return BeautifulSoup(response.text, 'lxml')


result_json = []
main_part_url = 'https://parsinger.ru/html/'
for i in range(3, 4):
    for y in range(1, 5):
        url = f'{main_part_url}index{i}_page_{y}.html'
        soup = create_soup(url)

        for item in soup.findAll('div', class_='item'):
            name = item.find('a', class_='name_item').text.strip()
            price = item.find('p', class_='price').text
            description = [value.text.split(':')[1].strip() for value in item.findAll('li')]
            result_json.append({
                'name': name,
                'brand': description[0],
                'type': description[1],
                'connect': description[2],
                'game': description[3],
                'price': price
            })

with open('resss.json', 'w', encoding='utf-8') as file:
    json.dump(result_json, file, indent=4, ensure_ascii=False)