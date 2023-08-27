import requests
from bs4 import BeautifulSoup

response = requests.get(url='https://parsinger.ru/html/index1_page_1.html')
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'lxml')
prices = [int(x.text.split()[0]) for x in soup.find_all('p', {'class':'price'})]

print(sum(prices))
