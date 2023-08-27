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

first_list_item = soup.li 
print(first_list_item)

next_sibling = first_list_item.next_sibling
while next_sibling:
    print(next_sibling)
    next_sibling = next_sibling.next_sibling