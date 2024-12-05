## **Web Scraping**

### **Objective:**

- Learn how to fetch web content using Python.
- Extract and parse useful information from HTML.
- Understand ethical and legal considerations of web scraping.

---

### **1. pip install**

**Teacher Notes:**

- Start by explaining that we need specific libraries to handle web scraping.
- Show how to use `pip` to install these libraries.
- Emphasize the importance of a virtual environment for managing dependencies.

**Code Example:**

```bash
pip install requests beautifulsoup4
```

---

### **2. Requests: Fetching HTML Content**

**Teacher Notes:**

- Introduce the `requests` library as a tool for making HTTP requests.
- Demonstrate how to fetch the raw HTML content of a webpage.
- Highlight common HTTP response codes (e.g., 200 for success, 404 for not found).

**Code Example:**

```python
import requests

# URL to scrape
url = "https://example.com"

# Fetching the content
response = requests.get(url)

# Checking status code
if response.status_code == 200:
    print("Page fetched successfully!")
    print(response.text[:500])  # Print the first 500 characters of the page content
else:
    print(f"Failed to fetch page. Status code: {response.status_code}")
```

---

### **3. BeautifulSoup: Parsing HTML**

**Teacher Notes:**

- Explain that `BeautifulSoup` is used to navigate and parse HTML content.
- Show how to create a `BeautifulSoup` object from the HTML fetched with `requests`.
- Demonstrate basic operations like finding tags and extracting text.
- Use a simple example webpage or a live demo.

**Code Example:**

```python
from bs4 import BeautifulSoup

# Example HTML content (use response.text in a real case)
html_content = """
<html>
    <head><title>Example Page</title></head>
    <body>
        <h1>Welcome to Example.com</h1>
        <p>This is a paragraph of text.</p>
        <a href="https://example.com/page2">Link to Page 2</a>
    </body>
</html>
"""

# Parsing the HTML
soup = BeautifulSoup(html_content, "html.parser")

# Extract the title
title = soup.title.string
print(f"Page Title: {title}")

# Extract the first <h1> tag
h1_text = soup.find("h1").text
print(f"H1 Text: {h1_text}")

# Extract all links
links = soup.find_all("a")
for link in links:
    print(f"Link: {link['href']}")
```

---

### **4. Legalities: Respecting Robots.txt and Terms of Service**

**Teacher Notes:**

- Emphasize ethical scraping practices.
- Explain what `robots.txt` is and how to check it.
- Encourage participants to read the terms of service for any site they scrape.
- Discuss the potential consequences of scraping without permission.

**Code Example:**

```python
# Checking robots.txt (manually or programmatically)
robots_url = "https://example.com/robots.txt"

response = requests.get(robots_url)
if response.status_code == 200:
    print("robots.txt:")
    print(response.text)
else:
    print("robots.txt not found!")
```

---
