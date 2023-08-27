import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

url = 'https://parsinger.ru/table/1/index.html'

response = requests.get(url, headers)

soup = BeautifulSoup(response.text, 'lxml')
tds = soup.find_all('td')

lst = [float(i.text) for i in tds]

print(sum(set(lst)))