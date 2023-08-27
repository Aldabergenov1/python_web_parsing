import requests

#response = requests.get(url='https://jsonplaceholder.typicode.com/todos/')
#print(response.json())

#.json() -- когда знаем что сайт отдаст инфу в формате json
#.text -- когда будем парсить HTML с bs4

response1 = requests.get(url='http://httpbin.org/image/jpeg')
with open('image.jpeg', 'wb') as file:
    file.write(response1.content)

#wb = write byte