from bs4 import BeautifulSoup

html = """
<html>
  <body>
    <p>This is a paragraph.</p>
  </body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')

p_element = soup.find('p')
parent_p = p_element.parent
print(parent_p)
print(parent_p.name)