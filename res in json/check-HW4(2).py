import requests
from bs4 import BeautifulSoup
import lxml
import json

# Находим количество категорий и страниц в категории
response = requests.get('https://parsinger.ru/html/index3_page_1.html')
response.encoding = 'utf-8'
result = []
soup = BeautifulSoup(response.text, 'lxml')
pages = [i.text for i in soup.find('div', 'pagen').find_all('a')]
cats = len(soup.find('div', 'nav_menu').find_all('a'))
# Пробегаемся по всем категориям и страницам
for i in range(1, cats+1):
    for j in pages:
        # Находим все элементы
        url = f'https://parsinger.ru/html/index{i}_page_{j}.html'
        response = requests.get(url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        elems = [i['href'] for i in soup.find_all('a', 'name_item')]
        # Пробегаемся по элементам
        for k in elems:
            url = f'https://parsinger.ru/html/{k}'
            category = k.split('/')[0]
            response = requests.get(url)
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'lxml')
            main_div = soup.find('div', 'description')
            # Находим все данные
            name = main_div.find('p', {'id': 'p_header'}).text
            article = main_div.find('p', 'article').text
            # Список ключей для вложенного словаря
            description_keys = [x['id'] for x in main_div.find('ul', {'id': 'description'}).find_all('li')]
            # Список значений для вложенного словаря
            description = [i.text for i in main_div.find('ul', {'id': 'description'}).find_all('li')]
            description_dict = {}
            # Проходимся по количеству ключей
            for l in range(len(description_keys)):
                # Добавляем к ключу значение
                description_dict[description_keys[l]] = [m.split(':')[-1] for m in description][l].strip()
            count = main_div.find('span', {'id': 'in_stock'}).text.split()[-1]
            price = main_div.find('span', {'id': 'price'}).text
            old_price = main_div.find('span', {'id': 'old_price'}).text
            
            # Вставляем все в словарь и сохраняем в json
            result.append({
                'category': category,
                'name': name,
                'article': article,
                # Готовый словарь добавляем в json
                'description': description_dict,
                'count': count,
                'price': price,
                'old_price': old_price,
                'link': url})
            with open('123.json', 'w', encoding='utf-8') as f:
                json.dump(result, f, indent=4, ensure_ascii=False)