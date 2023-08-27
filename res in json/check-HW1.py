import requests
from bs4 import BeautifulSoup

import json
import re

base_url = 'https://parsinger.ru/html/'

field_names = ['Наименование', 'Бренд', 'Форм-фактор', 'Ёмкость', 'Объём буф. памяти', 'Цена']


# ----------------------------------------------------------------
def get_pagen(url: str) -> list[str]:
    response = requests.get(url=url)  # Get the response
    response.encoding = 'utf-8'

    soup = BeautifulSoup(response.text, 'lxml')
    pagen = [p['href'] for p in soup.find('div', class_='pagen').find_all('a')]  # Get page's url from pagen
    return pagen


# ----------------------------------------------------------------

def get_rows(urls: list[str]) -> list[dict]:
    lines = []

    for page in urls:
        url = f'{base_url}{page}'
        response = requests.get(url=url)  # Get response from page
        response.encoding = 'utf-8'

        soup = BeautifulSoup(response.text, 'lxml')

        items = soup.find_all('div', class_='item')

        for item in items:
            name = item.find('a', class_='name_item').text.strip()  # name of the item
            description = [re.sub(r'.+: ?', '', i.text).strip() for i in
                           item.find('div', class_='description').find_all('li')]  # decscription of the item (list)
            price = item.find('p', class_='price').text.strip()  # price of the item
            row = dict(zip(field_names,
                           [name, *description,
                            price]))  # Create row (dict): keys - field_names, values - characteristics

            lines.append(row)
    return lines


def write_json(filename: str, data: list[dict[str, str]]) -> None:
    with open(filename, 'w', encoding='utf-8', newline='') as json_w:
        json.dump(data, json_w, indent=4, separators=(',', ': '), ensure_ascii=False)


# ----------------------------------------------------------------
if __name__ == '__main__':
    page_url = 'https://parsinger.ru/html/index4_page_1.html'

    pages = get_pagen(page_url)  # Get pagen from the url
    rows = get_rows(pages)  # Get data from all pages
    write_json('index2.json', rows)  # Write data

# ----------------------------------------------------------------