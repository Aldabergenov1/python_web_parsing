import requests

user_agent = {
  "user-agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 YaBrowser/21.2.4.172 Yowser/2.5 Safari/537.36"
}

i = 1

while i <= 500:
    url = f'https://parsinger.ru/task/1/{i}.html'
    response = requests.get(url=url, headers=user_agent)
    if response.status_code == 200:
        print(url)
        break
    i += 1
