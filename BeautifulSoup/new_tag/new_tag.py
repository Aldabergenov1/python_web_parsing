from bs4 import BeautifulSoup

html_doc = """
<html>
    <body>
        <p>Hello World!</p>
    </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# Создадим новый тег h1
new_h1 = soup.new_tag("h1", class_='new_class_tag')

# Добавим текст в новый тег h1
new_h1.string = "Welcome"

# Вставим новый тег h1 в документ
soup.body.insert(0, new_h1)

print(soup)