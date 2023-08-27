from bs4 import BeautifulSoup

html_doc = """
<html>
  <body>
    <div>
      <p>Paragraph 1</p>
      <p>Paragraph 2</p>
    </div>
  </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

new_tag = soup.new_tag('h1', id='insert_before_tag')
new_tag.string = 'Header'

first_p = soup.find('p')
first_p.insert_before(new_tag)

print(soup)