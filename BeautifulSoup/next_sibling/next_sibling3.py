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

first_item = soup.li 
print(first_item.text)

print('----Разделитель----')

next_el = first_item.next_sibling
while next_el:
    print(next_el.text)
    next_el = next_el.next_sibling