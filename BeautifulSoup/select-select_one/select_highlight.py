from bs4 import BeautifulSoup

html = """
<html>
  <body>
    <p class="highlight">This is a highlighted paragraph.</p>
    <p>This is a normal paragraph.</p>
    <div id="div1">
      <p>This is a paragraph in a div.</p>
    </div>
  </body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

res = soup.select('.highlight')
for tag in res:
    print(tag.text)
    
print('----Разделитель----')

res = soup.select('#div1 p')
for tag in res:
    print(tag.text)