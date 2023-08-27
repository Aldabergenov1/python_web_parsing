from bs4 import BeautifulSoup

html = """
<html>
    <body>
        <h1>Заголовок 1</h1>
        <p class="text-class">Текст 1</p>
        <p class="text-class">Текст 2</p>
        <p id="text-id">Текст 3</p>
        <a href="https://google.com">Google</a>
        <a href="https://yandex.ru">Yandex</a>
    </body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')

hrefs = soup.find_all('a', href=True)
for tag in hrefs:
    print(tag['href'], tag.text)