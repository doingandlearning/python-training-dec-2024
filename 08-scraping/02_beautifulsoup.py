from bs4 import BeautifulSoup

html_content = """
<html>
    <head>
        <title>Example Page</title>
    </head>
    <body>
        <h1>Welcome to Example.com</h1>
        <p>This is a paragraph of text.</p>
        <a href="https://example.com/page2">Link to page 2</a>
    </body>
</html>
"""

soup = BeautifulSoup(html_content, "html.parser")

print(soup.title.string)

h1_text = soup.find("h1").text
print(h1_text)

links = soup.find_all("a")
for link in links:
    print(f"Link: {link['href']}, {link.text}")