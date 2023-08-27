from bs4 import BeautifulSoup

html = """
<html>
    <body>
        <h1>Example Page</h1>
        <p>This is some text.</p>
        <ul>
            <li>Item 1</li>
            <li>Item 2</li>
            <li>Item 3</li>
        </ul>
        <p>This is some more text.</p>
        <p>This is even more text.</p>
    </body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')

last_p = soup.find_all('p')[-1]

prev_sibling = last_p.previous_sibling

print(prev_sibling.previous_sibling)

"""Используя last_p = soup.find_all('p')[-1], находится последний тег <p> в HTML-структуре: <p>This is even more text.</p>.
last_p.previous_sibling вернет символы новой строки и пробелы между последним и предпоследним тегами <p>, которые представляют собой текстовый узел.
Чтобы получить предыдущий тег <p>, нужно ещё раз вызвать .previous_sibling. Таким образом, last_p.previous_sibling.previous_sibling вернет предпоследний тег <p>: <p>This is some more text.</p>.
"""