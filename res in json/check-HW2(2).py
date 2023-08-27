import requests
import json
from bs4 import BeautifulSoup

url = 'https://parsinger.ru/html/index1_page_1.html'
scheme = 'https://parsinger.ru/html/'

response = requests.get(url=url)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'lxml')

categories_urls = [category['href'] for category in soup.find('div', class_='nav_menu').find_all('a')]

result_json = []

for i, url in enumerate(categories_urls, start=1):
    category_response = requests.get(f'{scheme}{url}')
    category_response.encoding = 'utf-8'

    categories_soup = BeautifulSoup(category_response.text, 'lxml')

    desc = [''.join([category.text.split(': ')[0] for category in item])
            for item in categories_soup.find('div', class_='description').find_all('li')]

    desc.insert(0, 'Наименование')
    desc.append('Цена')

    dict_pattern = dict.fromkeys(desc)

    pages = [page.text for page in BeautifulSoup(response.text, 'lxml').find('div', class_='pagen').find_all('a')]

    for j in pages:
        page_response = requests.get(url=f'{scheme}index{i}_page_{j}.html')
        page_response.encoding = 'utf-8'

        page_soup = BeautifulSoup(page_response.text, 'lxml')

        names = tuple(name.text.strip() for name in page_soup.find_all('a', class_='name_item'))
        descriptions = tuple(tuple(x.split(':')[1].strip() for x in item.text.strip().split('\n'))
                             for item in page_soup.find_all('div', class_='description'))
        prices = tuple(name.text.strip() for name in page_soup.find_all('p', class_='price'))

        for name, desc, price in zip(names, descriptions, prices):
            current_data = dict_pattern.copy()

            for key, value in zip(dict_pattern, (name, *desc, price)):
                current_data[key] = value

            result_json.append(current_data)

with open('goods_data.json', 'w', encoding='utf-8') as file:
    json.dump(result_json, file, indent=4, ensure_ascii=False)