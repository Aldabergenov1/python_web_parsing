import requests
from bs4 import BeautifulSoup

res = []

for i in range(1, 33):
    url = f'https://parsinger.ru/html/mouse/3/3_{i}.html'
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    
    res.append(soup.find('p', {'class':'article'}).text)

new_res = [int(i.split(': ')[-1]) for i in res]
print(sum(new_res))