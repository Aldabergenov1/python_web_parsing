import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

url = 'https://parsinger.ru/table/1/index.html'

response = requests.get(url, headers)

soup = BeautifulSoup(response.text, 'lxml')
trs = [float(i.text) for i in soup.select('td:first-child')]

print(sum(trs))