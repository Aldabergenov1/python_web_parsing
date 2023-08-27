import requests
from bs4 import BeautifulSoup

res = []

for i in range(1, 5):
    url = f'https://parsinger.ru/html/index3_page_{i}.html'
    response = requests.get(url=url)
    response.encoding = 'utf-8'

    soup = BeautifulSoup(response.text, 'lxml')
    
    name_tags = [x.text for x in soup.find_all('a', {'class':'name_item'})]
    
    res.append(name_tags)

print(res)
