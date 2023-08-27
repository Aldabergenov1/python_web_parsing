import requests
from bs4 import BeautifulSoup

response = requests.get(url='https://parsinger.ru/html/hdd/4/4_1.html')
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'lxml')
old_price = int(soup.find('span', {'id':'old_price'}).text.split()[0])
new_price = int(soup.find('span', {'id':'price'}).text.split()[0])

sale = (old_price-new_price)*100/old_price

print(round(sale,1))