import requests

response = requests.get(url='https://parsinger.ru/video_downloads/videoplayback.mp4', stream=True)
with open('file.mp4', 'wb') as file:
    file.write(response.content)