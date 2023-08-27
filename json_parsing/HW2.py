import requests

url = 'https://parsinger.ru/downloads/get_json/res.json'
response = requests.get(url).json()

res = {}

for item in response:
    if item['categories'] not in res:
        res.update({item['categories']: int(item['count'])*int(item['price'].split(' ')[0])})
    else:
        res.update({
            item['categories']: res.get(item['categories']) + int(item['count'])*int(item['price'].split(' ')[0])
        })

print(res)