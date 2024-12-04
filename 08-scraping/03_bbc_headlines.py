import requests
from bs4 import BeautifulSoup
import re
url = "https://bbc.co.uk/news"

response = requests.get(url)

if response.status_code != 200:
    raise Exception(f"Failed status code: {response.status_code}" )

soup = BeautifulSoup(response.content, "html.parser")

print(soup.title.text)

paragraphs = soup.find_all('p', class_=re.compile(r'PromoHeadline$'))

headlines = []
for para in paragraphs:
   if para.text not in headlines:
       headlines.append(para.text)


print(headlines)