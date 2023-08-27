import json
import requests
from bs4 import BeautifulSoup
import re

base_url = 'https://parsinger.ru/html/'
url = f'{base_url}index3_page_1.html'
response = requests.get(url=url)
soup = BeautifulSoup(response.text, 'lxml')
# записываем количество страниц с выбранным товаром в переменную "num_of_pgs"
num_of_pgs = len(soup.find('div', class_='pagen').find_all('a'))

result_json = []
for pg in range(1, num_of_pgs + 1):
    url = f'{base_url}index3_page_{pg}.html'
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    # записываем ссылки на каждый товар на странице в итератор item_urls
    item_urls = (f"{base_url}{i.find('a', class_='name_item').get('href')}" for i in soup.find_all('div', class_='item'))

    for url in item_urls:
        response = requests.get(url=url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        # собираем данные и преобразовываем к нужному виду
        category = re.search(r'https:\/{2}.+?\/.+?\/(\w+)', url).group(1)
        name = soup.find('p', id='p_header').text
        article = soup.find('p', class_='article').text
        description = dict(((i.get('id'), i.text.split(':')[1].strip()) for i in soup.find('ul', id='description').find_all('li')))
        in_stock = soup.find('span', id='in_stock').text
        price = soup.find('span', id='price').text
        old_price = soup.find('span', id='old_price').text
        result_json.append({'categories': category,
                            'name': name,
                            'article': article,
                            'description': description,
                            'count': in_stock,
                            'price': price,
                            'old_price': old_price,
                            'link': url})

filename = 'mouses.json'
with open(filename, 'w', encoding='utf-8') as file:
    json.dump(result_json, file, indent=4, ensure_ascii=False)

print(f'Файл {filename} успешно записан')