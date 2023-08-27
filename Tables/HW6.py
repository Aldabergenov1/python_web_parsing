import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

url = 'https://parsinger.ru/table/5/index.html'

response = requests.get(url, headers)

d = {}

soup = BeautifulSoup(response.text, 'lxml')
for i in range(1, 16):
    column = soup.select(f'table tr td:nth-of-type({i})')
    summ = sum([float(i.text) for i in column])
    d[f'{i} column'] = round(summ, 3)

print(d)