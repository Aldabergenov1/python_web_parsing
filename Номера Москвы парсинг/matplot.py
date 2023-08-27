import requests
from bs4 import BeautifulSoup

soup_url = 'https://telspravki.info/rossiya/moskovskaya-oblast/stolitsa-rossii/moskva?serchStreet=%21&amp;amp;ysclid=ll9qcz28mt781375002'

header = {'user-agen': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}

def get_soup(url):
    response = requests.get(url, header, timeout=1000)
    response.encoding = 'utf-8'
    return BeautifulSoup(response.text, 'lxml')

main_soup = get_soup(soup_url)
all_links = ['https:'+a['href'] for a in main_soup.find('div', class_='outInfo').find_all('a', href=True)][1:]

for link in all_links:
    temp_soup = get_soup(link)
    additional_links = ['http:'+a['href'] for a in temp_soup.find('div', class_='outInfo').find_all('a', href=True)]
    for l in additional_links:
        

print(all_links)

print('Готово')