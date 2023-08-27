import requests
from random import choice
from fake_useragent import UserAgent

with open('user_agent.txt') as file:
    lines = file.read().split('\n')

for line in lines:
    user_agent = {'user-agent': choice(lines)}

response = requests.get(url='http://httpbin.org/user-agent', headers=user_agent)
print(f'Юзер-агент методом рандом: {response.text}')
