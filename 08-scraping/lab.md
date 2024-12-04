## Lab Instructions

### Objective

Scrape a simple website (e.g., Wikipedia) to extract all the titles of links on the homepage.

### Prerequisites

- Basic knowledge of Python
- Familiarity with HTML and web scraping concepts
- Installed libraries: `requests`, `beautifulsoup4`

### Steps

1. **Setup the Environment**

   - Ensure you have Python installed on your machine.
   - Install the required libraries using pip:
     ```bash
     pip install requests beautifulsoup4
     ```

2. **Write the Script**

   - Create a Python script named `scrape_links.py`.
   - Import the necessary libraries:
     ```python
     import requests
     from bs4 import BeautifulSoup
     ```

3. **Fetch the Webpage**

   - Use the `requests` library to fetch the content of the webpage:
     ```python
     url = 'https://www.wikipedia.org/'
     response = requests.get(url)
     ```

4. **Parse the HTML**

   - Parse the fetched HTML content using BeautifulSoup:
     ```python
     soup = BeautifulSoup(response.text, 'html.parser')
     ```

5. **Extract Link Titles**

   - Find all the link elements and extract their titles:
     ```python
     links = soup.find_all('a')
     for link in links:
     	title = link.get('title')
     	if title:
     		 print(title)
     ```

6. **Run the Script**
   - Execute the script and observe the output:
     ```bash
     python scrape_links.py
     ```

### Notes

- Ensure you comply with the website's `robots.txt` file and terms of service.
- This lab is for educational purposes only and should not be used in production.

### Extension: Save Data to CSV

To extend the script and save the extracted link titles into a CSV file, follow these additional steps:

1. **Import the CSV Library**

   - Add the `csv` library to your imports:
     ```python
     import csv
     ```

2. **Write to CSV**

   - Modify the script to write the extracted titles to a CSV file:

     ```python
     with open('link_titles.csv', 'w', newline='') as csvfile:
     	fieldnames = ['Title']
     	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

     	writer.writeheader()
     	for link in links:
     		 title = link.get('title')
     		 if title:
     				writer.writerow({'Title': title})
     ```

3. **Run the Script**

   - Execute the script and check the `link_titles.csv` file for the extracted data:
     ```bash
     python scrape_links.py
     ```
