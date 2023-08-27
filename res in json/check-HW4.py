import requests
from bs4 import BeautifulSoup
import json

url = 'http://parsinger.ru/html/index1_page_1.html'
site= 'http://parsinger.ru/html/'
cards = [] # тут будем хранить данные с карточек
count = 0

# тут получаем данные с сайта и варим суп
soup = lambda x: BeautifulSoup(requests.get(url=x).content.decode('utf-8'), 'lxml')

# тут генерим линки
links = lambda soup, tag1, class_1, tag2='a', class_2= '': [site + i['href'] for i in soup.find(tag1, class_1).find_all(tag2, class_2)]

# получаем пару ключ: значение
get_item = lambda s, div, **kwargs: s.find(div, **kwargs).text.split(':')[-1].strip()

# собираем ссылки на все категории и идем по ним
soup_face = soup(url)
link_cats =  links(soup_face, 'div', 'nav_menu')

# идем по категориям
for link_cat in link_cats:

    # Запоминаем категорию.
    soup_cat = soup(link_cat)
    categories = soup_cat.find('div', class_='nav_menu').find('a', href=link_cat[-18:]).find('div')['id']

    # собираем ссылки на все страницы по категории
    link_pages = links(soup_cat, 'div',"pagen")

    #  идем по каждой странице
    for link_page in link_pages:
        soup_page = soup(link_page)
        link_cards = links(soup_page, 'div', 'item_card', 'a', 'name_item')

        # проходим по каждой карточке
        for link_card in link_cards:
            soup_card = soup(link_card)
            description = {i['id']: i.text.split(':')[-1].strip() for i in
                           soup_card.find('ul', id='description').find_all('li')}
            card = ({
                'categories': categories,
                'name': get_item(soup_card, 'p', id="p_header"),
                'article': get_item(soup_card, 'p', class_="article"),
                'description': description,
                'count': get_item(soup_card, 'span', id="in_stock"),
                'price': get_item(soup_card, 'span', id='price'),
                'old_price': get_item(soup_card, 'span', id="old_price"),
                'link': link_card
                         })
            cards.append(card)
            print(f'Обработано {[count := count + 1, count][0]} из 160')

with open('res4.json', 'w', encoding='utf-8') as file:
    json.dump(cards, file, indent=4, ensure_ascii=False)

print("Данные с сайта записаны в файл 'res4.json'")