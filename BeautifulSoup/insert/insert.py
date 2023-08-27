from bs4 import BeautifulSoup

html_doc = """
<html>
    <body>
        <div id="main">
            <ul>
                <li>Item 1</li>
                <li>Item 2</li>
                <li>Item 3</li>
            </ul>
        </div>
    </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

main_div = soup.find('div', {'id':'main'})
first_ul = main_div.find('ul')

new_tag = soup.new_tag('li')
new_tag.string = 'Item 4 insert_index'

first_ul.insert(7, new_tag)
print(first_ul)