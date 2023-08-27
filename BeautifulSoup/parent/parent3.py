from bs4 import BeautifulSoup

html = """
<html>
    <body>
        <div id="content">
            <p>This is a paragraph.</p>
            <p>This is another paragraph.</p>
        </div>
    </body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')

first_p = soup.select_one('#content p:first-of-type')
parent_div = first_p.parent

print(parent_div)