from bs4 import BeautifulSoup

html_doc = """
<html>
    <head>
        <title>Example Page</title>
    </head>
    <body>
        <div id="main">
            <h1>Hello World</h1>
            <p class="info">This is a paragraph.</p>
            <p class="info">This is another paragraph.</p>
            <ul>
                <li>Item 1</li>
                <li>Item 2</li>
                <li>Item 3</li>
            </ul>
        </div>
        <div id="secondary">
            <p>Some additional information.</p>
        </div>
    </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# Найдёт первый div с идентификатором "main"
main_div = soup.find('div', {'id': 'main'})

# Найдёт первый h1 внутри "основного" div
main_h1 = main_div.find('h1')

# Извлекает тег h1 из документа
main_h1.extract()

# Тег h1 больше не доступен в документе
print(soup)