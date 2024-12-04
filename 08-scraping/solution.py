import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org"

response = requests.get(url)

if response.status_code != 200:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
    exit(1)

soup = BeautifulSoup(response.text, "html.parser")

links = soup.find_all("a")
titles_and_links = [
    (link.get('title'), link.get('href'))
    for link in links
    if link.get('title') and link.get('href')
]

exclude_prefixes = ['/wiki/Help', '/wiki/Special', '/wiki/Wikipedia', '/w/', '/wiki/Portal',
                    '//en.wikipedia.org/wiki/Wikipedia',
                    '/wiki/Main_Page',
                    '/wiki/Talk',
                    'https://',
                    '/wiki/English_language',
                    '/wiki/Free_content']

filtered_titles_and_links = [
    (title, link)
    for title, link in titles_and_links
    if not any(link.startswith(prefix) for prefix in exclude_prefixes)
]
print(filtered_titles_and_links)

import csv

with open('filtered_link_titles.csv', "w") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["Title", "Link"])
    writer.writeheader()

    for title, link in filtered_titles_and_links:
        writer.writerow({'Title': title, 'Link': f"https://en.wikipedia.org{link}"})

