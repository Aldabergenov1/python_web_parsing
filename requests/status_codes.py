import requests
import time

url = 'http://httpbin.org/sds/'
response = requests.get(url)
if response.ok:
    print('status_code OK')
else:
    print('status_code is NOT OK')

if not response.ok:
    time.sleep(60)
else:
    print('status_code is OK, continuing')