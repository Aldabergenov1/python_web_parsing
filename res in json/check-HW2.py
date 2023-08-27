import requests
from bs4 import BeautifulSoup

import json

base_url = 'https://parsinger.ru/html/'


# ----------------------------------------------------------------
def get_categories(url: str) -> list:
    response = requests.get(url=url)  # Get the response
    response.encoding = 'utf-8'

    soup = BeautifulSoup(response.text, 'lxml')
    cats = [p['href'] for p in soup.find('div', class_='nav_menu').find_all('a')]  # Get page's url from pagen
    return cats


# ----------------------------------------------------------------
def get_pagen(url_adres: str) -> list[str]:
    response = requests.get(url=url_adres)  # Get the response
    response.encoding = 'utf-8'

    soup = BeautifulSoup(response.text, 'lxml')
    pagn = [p['href'] for p in soup.find('div', class_='pagen').find_all('a')]  # Get page's url from pagen
    return pagn


# ----------------------------------------------------------------

def get_rows(urls: list[str]) -> list[dict[str, str]]:
    lines = []

    for page in urls:
        url_ = f'{base_url}{page}'
        response = requests.get(url=url_)  # Get response from page
        response.encoding = 'utf-8'

        soup = BeautifulSoup(response.text, 'lxml')

        items = soup.find_all('div', class_='item')

        for item in items:
            name = item.find('a', class_='name_item').text.strip()  # name of the item
            description = [[j.strip() for j in i.text.split(':')] for i in
                           item.find('div', class_='description').find_all('li')]  # decscription of the item (list)
            #  items of the form [name, value] split by the ':'
            price = item.find('p', class_='price').text.strip()  # price of the item
            row = dict(zip(['Имя', *[i[0] for i in description], 'Цена'], [name, *[i[1] for i in description],
                                                                           price]))  # Create row (dict): keys -
            # field_names, values - characteristics

            lines.append(row)
    return lines


def write_json(filename: str, data: list[dict[str, str]]) -> None:
    with open(filename, 'w', encoding='utf-8-sig', newline='') as json_w:
        json.dump(data, fp=json_w, indent=4, separators=(',', ':'), ensure_ascii=False)  # write data


# ----------------------------------------------------------------
if __name__ == '__main__':
    page_url = 'https://parsinger.ru/html/index1_page_1.html'

    categories: list[str] = get_categories(page_url)  # Get categories from the url
    index: list = []
    for cat in categories:
        url = f'{base_url}{cat}'
        pagen = get_pagen(url_adres=url)  # Get pages from all categories
        index.extend(pagen)

    rows = get_rows(index)
    write_json('index3.json', rows)  # Write data
    # если я использую незнакомую вам контрукцию if __name__ == '__main__' или
    # незнакомый вам язык для написания комментариев (английский)
    # это еще не значит, что я скатал код с чат гпт!
# ----------------------------------------------------------------