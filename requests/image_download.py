import requests

for i in range(1, 161):
    url = f'https://parsinger.ru/img_download/img/ready/{i}.png'
    response = requests.get(url)
    with open(f'image_code{i}.jpeg', 'wb') as file:
        file.write(response.content)