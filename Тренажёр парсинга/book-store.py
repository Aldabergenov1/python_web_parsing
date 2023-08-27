import json
import requests
from bs4 import BeautifulSoup

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}
rating_dict = {
    'One': '1/5',
    'Two': '2/5',
    'Three': '3/5',
    'Four': '4/5', 
    'Five': '5/5'
}
res = []

def get_soup(url):
    response = requests.get(url, headers, timeout=10000)
    response.encoding = 'utf-8'
    return BeautifulSoup(response.text, 'lxml')

url = 'http://books.toscrape.com/catalogue/category/books_1/page-1.html'
main_soup = get_soup(url)
pages_count = int(main_soup.find('li', class_='current').text.split()[-1])

for i in range(pages_count):
    print(f'Страница {i+1} из {pages_count}')
    url = f'http://books.toscrape.com/catalogue/category/books_1/page-{i+1}.html'
    page_soup = get_soup(url)
    book_links = set(['http://books.toscrape.com/catalogue' + a['href'][5:] for a in page_soup.find('ol', class_='row').find_all('a', href=True)])
    for link in book_links:
        book_soup = get_soup(link)
        description = [i.text for i in book_soup.find_all('td')]
        res.append({
            'Наименование': book_soup.find('h1').text,
            'UPC': description[0],
            'Стоимость': description[2],
            'Стоимость с учётом налогов': description[3],
            'Объём налога': description[4], 
            'В наличии': description[5].split()[2][1:],
            'Рецензий': description[6],
            
        })
        
        
with open('book_parse_res.json', 'w', encoding='utf-8') as file:
    json.dump(res, file, indent=4, ensure_ascii=False)
    
print('Файл создан!')