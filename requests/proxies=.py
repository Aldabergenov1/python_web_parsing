import requests

url = 'http://httpbin.org/ip'
proxy = {
    'http': 'http://103.177.45.3:80',
    'https': 'https://103.177.45.3:80',

}

response = requests.get(url=url, proxies=proxy)
print(response.json())