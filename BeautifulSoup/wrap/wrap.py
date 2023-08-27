from bs4 import BeautifulSoup

html_doc = """
<body>
  <p>Some text</p>
</body>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# Обернем первый тег p внутри body с помощью тега div
p_tag = soup.body.p
p_tag.wrap(soup.new_tag("div", class_='wrap_tag'))

print(soup)