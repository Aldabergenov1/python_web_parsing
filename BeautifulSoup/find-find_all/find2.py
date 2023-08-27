from bs4 import BeautifulSoup

html_doc = """
<html>
    <head>
        <title>Example Page</title>
    </head>
    <body>
        <div id="main">
            <h1>Hello World</h1>
            <p class="info">This is a paragraph.</p>
            <p class="info">This is another paragraph.</p>
            <ul>
                <li>Item 1</li>
                <li>Item 2</li>
                <li>Item 3</li>
            </ul>
        </div>
        <div id="secondary">
            <p>Some additional information.</p>
        </div>
    </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

main_div = soup.find('div', {'id':'main'})
print(main_div)

print('----Разделитель----')

first_h1 = main_div.find('h1')
print(first_h1)

print('----Разделитель----')

info_p = main_div.find('p', {'class':'info'})
print(info_p)

print('----Разделитель----')

firts_ul = main_div.find('ul')
print(firts_ul)