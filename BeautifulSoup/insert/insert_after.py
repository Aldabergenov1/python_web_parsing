from bs4 import BeautifulSoup

html_doc = """
<html>
    <body>
        <p>Paragraph 1</p>
        <p>Paragraph 2</p>
    </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# Создаём тег который будем добавлять
new_tag = soup.new_tag("b", id='insert_after_tag')
new_tag.string = "Important"

first_p = soup.find("p")
first_p.insert_after(new_tag)

print(soup)