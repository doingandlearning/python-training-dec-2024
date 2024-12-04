import requests

url = "https://bbc.co.uk"

response = requests.get(url)
print("Here i am :) ")
print(response)
if response.status_code == 200:
    print("Page fetched successfully!")
    print(response.content[:500])
else:
    print(f"Failed to fetch page. Status code {response.status_code}")