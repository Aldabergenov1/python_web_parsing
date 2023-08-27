from bs4 import BeautifulSoup

with open('index\\index.html', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'lxml')
    print(soup)