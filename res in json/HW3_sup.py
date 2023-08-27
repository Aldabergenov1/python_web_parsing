import requests
import json
from bs4 import BeautifulSoup

def create_soup(url: str):
    response = requests.get(url)
    response.encoding = 'utf-8'
    return BeautifulSoup(response.text, 'lxml')

labels = {1: 'watch', 2: 'mobile', 3: 'mouse', 
          4: 'hdd', 5: 'headphones'}

temp_url = 'https://parsinger.ru/html/index1_page_1.html'
temp_soup = create_soup(temp_url)
sections = len(temp_soup.find('div', class_='nav_menu').find_all('a'))
pages = len(temp_soup.find('div', class_='pagen').find_all('a'))

res_json = []

for i in range(sections):
    for j in range(32):
        url = f'https://parsinger.ru/html/{labels[i+1]}/{i+1}/{i+1}_{j+1}.html'
        print(url)