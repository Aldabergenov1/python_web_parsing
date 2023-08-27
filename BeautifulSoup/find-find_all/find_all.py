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

all_p = soup.find_all('p')
for tag in all_p:
    print(tag.text)

print('----Разделитель----')

all_p_text = soup.find_all('p', attrs={'class':'text-class'})
for tag in all_p_text:
    print(tag.text)

print('----Разделитель----')

all_p_id = soup.find_all('p', attrs={'id':'text-id'})
for tag in all_p_id:
    print(tag.text)