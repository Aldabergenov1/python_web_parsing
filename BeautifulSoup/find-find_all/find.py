from bs4 import BeautifulSoup

html_doc = """
<html>
    <head>
        <title>Example Page</title>
    </head>
    <body>
        <h1>Hello World</h1>
        <p class="info">This is a paragraph.</p>
        <p class="info">This is another paragraph.</p>
    </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

first_h1 = soup.find('h1')
print(first_h1)

print('----Разделитель----')

first_p = soup.find('p', {'class':'info'})
print(first_p)
