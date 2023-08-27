from bs4 import BeautifulSoup
import json, requests

def make_soup(url):
    '''возвращает готовый суп'''
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    return soup

# формирование списка ссылок на категории
url = 'https://parsinger.ru/html/index1_page_1.html'
soup = make_soup(url)
category_pages = [x['href'] for x in soup.find('div', 'nav_menu').find_all('a')]

# формирование списка ссылок на все страницы каждой категории
scheme = 'https://parsinger.ru/html/'
all_pages = []
for link in category_pages:
    soup = make_soup(f'{scheme}{link}')
    pages = [x['href'] for x in soup.find('div', 'pagen').find_all('a')]
    all_pages.extend(pages)

# формирование списка ссылок на все карточки всех страниц каждой категорий
all_cards = []
for link in all_pages:
    soup = make_soup(f'{scheme}{link}')
    cards = [x.find('a')['href'] for x in soup.find_all('div', 'sale_button')]
    all_cards.extend(cards)

# формирование списка словарей
result_json = []
for link in all_cards:
    soup = make_soup(f'{scheme}{link}')
    category = f'{scheme}{link}'.split('/')[4]
    name = soup.find('p', id='p_header').text.strip()
    article = soup.find('p', 'article').text.split(':')[1].strip()
    descr_keys = [x['id'] for x in soup.find('ul', id='description').find_all('li')]
    descr_values = [x.text.split(':')[1].strip() for x in soup.find('ul', id='description').find_all('li')]
    descr = dict(zip(descr_keys, descr_values))
    in_stock = soup.find('span', id='in_stock').text.split(':')[1].strip()
    old_price = soup.find('span', id='old_price').text
    price = soup.find('span', id='price').text
    link = scheme + link
    result_json.append({
        'category': category,
        'name': name,
        'article': article,
        'description': descr,
        'count': in_stock,
        'price': price,
        'old_price': old_price,
        'link': link
    })

# запись в json-файл
with open('res4rr.json', 'w', encoding='utf-8') as file:
    json.dump(result_json, file, indent=4, ensure_ascii=False)
    print(f'Файл {file.name} сформирован')