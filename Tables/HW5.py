import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

url = 'https://parsinger.ru/table/5/index.html'

response = requests.get(url, headers)

soup = BeautifulSoup(response.text, 'lxml')
oranges = [float(i.text) for i in soup.find_all('td', class_='orange')]
blues = [float(i.text) for i in soup.find_all('td')[14::15]]
res = []

for i1, i2 in zip(oranges, blues):
    res.append(i1*i2)

print(sum(res))