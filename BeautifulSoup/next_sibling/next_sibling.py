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
    </body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')

header = soup.h1
print(header)
print(header.next_sibling)
#header.next_sibing = \n
