import json
import requests
from bs4 import BeautifulSoup

#создаю функцию, чтобы каждый раз не прописывать создание супа
def create_soup(url: str):
    response = requests.get(url)
    response.encoding = 'utf-8'
    return BeautifulSoup(response.text, 'lxml')

#делаю временный суп чтобы получить количество разделов и страниц(хоть и знаю их кол-во, это сделает парсер более гибким)
temp_soup = create_soup(url='https://parsinger.ru/html/index3_page_1.html')
sections = temp_soup.find('div', class_='nav_menu').find_all('a')
pages = temp_soup.find('div', class_='pagen').find_all('a')

#создаю результирующий json
res_json = []

#цикл для пробежки по всем разделам и по всем страницам
for i in range(len(sections)):
    for j in range(len(pages)):
        print(f'Раздел {i+1}, страница {j+1}')
        url = f'https://parsinger.ru/html/index{i+1}_page_{j+1}.html'
        soup = create_soup(url)
        
        #добываю нужные мне данные со страницы
        names = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
        params = [x.text.strip().split('\n') for x in soup.find_all('div', class_='description')]
        prices = [x.text.strip() for x in soup.find_all('p', class_='price')]
        
        #цикл для упаковки json
        for name, par, price in zip(names, params, prices):
            res_json.append({
                'Наимновение': name,
                #использую такую конструкцию, ибо параметры разных товаров разные
                [x.split(':')[0].strip() for x in par][0]: [x.split(':')[1].strip() for x in par][0], 
                [x.split(':')[0].strip() for x in par][1]: [x.split(':')[1].strip() for x in par][1],
                [x.split(':')[0].strip() for x in par][2]: [x.split(':')[1].strip() for x in par][2],
                [x.split(':')[0].strip() for x in par][3]: [x.split(':')[1].strip() for x in par][3],
                'Цена': price
            })

#записываю результат в файл
with open('res2.json', 'w', encoding='utf-8') as file:
    json.dump(res_json, file, indent=4, ensure_ascii=False)

print('Результат записан в файл res2.json!')