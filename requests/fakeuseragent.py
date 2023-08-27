import requests
import time
from fake_useragent import UserAgent

ua = UserAgent()

for _ in range(10):
    try:
        fake_ua = {'user-agent': ua.random}
        response = requests.get(url = 'http://httpbin.org/user-agent', headers=fake_ua)
        print(response.text)
        time.sleep(3)
    except Exception as _ex:
        continue