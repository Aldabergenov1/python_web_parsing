import requests
from bs4 import BeautifulSoup

res_list = []
index_labels = {1: "watch", 2: "mobile", 3: "mouse", 
                4: "hdd", 5: "headphones"}

for i in range(1, 6):
    for j in range(1, 33):
        url = f'https://parsinger.ru/html/{index_labels[i]}/{i}/{i}_{j}.html'
        response = requests.get(url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        
        amount = soup.find('span', {'id':'in_stock'}).text
        price = soup.find('span', {'id':'price'}).text
        
        num_amount = int(''.join(c for c in amount if c.isdigit()))
        num_price = int(''.join(c for c in price if c.isdigit()))
        
        res_list.append(num_amount*num_price)

print(sum(res_list))