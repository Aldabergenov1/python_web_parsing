from bs4 import BeautifulSoup

html_doc = """
<html>
    <head>
        <title>Example Page</title>
    </head>
    <body>
        <p>This is a <b>bold</b> text.</p>
        <p>This is another <b>bold</b> text.</p>
    </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
bold_elements = soup.find_all('b')

for b in bold_elements:
    print(b.parent.text)