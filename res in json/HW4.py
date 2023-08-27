import requests
import json
from bs4 import BeautifulSoup

#функция для создания супа
def create_soup(url: str):
    response = requests.get(url)
    response.encoding = 'utf-8'
    return BeautifulSoup(response.text, 'lxml')

#словарь для пробежки по всем страницам и всем категориям
labels = {1: 'watch', 2: 'mobile', 3: 'mouse', 
          4: 'hdd', 5: 'headphones'}

res_json = [] #создаю резуьтирующий json

#цикл где буду пробегаться по страницам
for i in range(1, 6):
    print(f'Секция {i} из 5')
    for j in range(1, 33):
        url = f'https://parsinger.ru/html/{labels[i]}/{i}/{i}_{j}.html' #создаю url-ы
        soup = create_soup(url) 
        
        #собираю нужные мне данные, desctiption, согласно задаче, перевожу в словарь с помощью dictionary comprehension
        name = soup.find('p', id='p_header').text
        article = soup.find('p', class_='article').text
        params = {tag.get('id'):tag.text.split(': ')[1] for tag in soup.find('ul', id='description').find_all('li')}
        amount = soup.find('span', id='in_stock').text
        price = soup.find('span', id='price').text
        old_price = soup.find('span', id='old_price').text
        
        #всё пихаю в результирующий json
        res_json.append({
            "categories": labels[i],
            "name": name,
            "article": article.split(': ')[1],
            "description": params,
            "count": amount,
            "price": price,
            "old_price": old_price,
            "link": url
        })

#создаю файл
with open('res4.json', 'w', encoding='utf-8') as file:
    json.dump(res_json, file, indent=4, ensure_ascii=False)
    
print('Файл res4.json создан!')
