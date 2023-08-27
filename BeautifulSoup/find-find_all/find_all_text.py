from bs4 import BeautifulSoup

html = """
<html>
    <body>
        <h1>Заголовок 1</h1>
        <p class="text-class">Текст 1</p>
        <p class="text-class">Текст 2</p>
        <p id="text-id">Текст 3</p>
    </body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')

res = soup.find_all('p', string='Текст 1')
for tag in res:
    print(tag.text)

print('----Раздлитель----')

res = soup.find_all('p', string=lambda x: 'Текст' in x)
for tag in res:
    print(tag.text)