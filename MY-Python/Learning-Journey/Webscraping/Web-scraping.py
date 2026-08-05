#WEB-SCRAPING---//DAY-17//
#_______________________________________________________________________________________________________________________________________________________

import requests
from bs4 import BeautifulSoup
'''
url = "https://www.w3schools.com/html/html_examples.asp"

response = requests.get(url)
print(response.status_code)
content = response.content

soup = BeautifulSoup(content, 'html.parser')
print(soup.title)
print(soup.title.get_text())
print(soup.body)


tables = soup.find_all('div')
for table in tables:
    print(table)'''


url = "https://archive.ics.uci.edu/dataset/53/iris"


response = requests.get(url)
print(response.status_code)

soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find("table")

rows = table.find_all("tr")

headers = []

for th in rows[0].find_all("th"):
    headers.append(th.get_text(strip=True))

data = []

for row in rows[1:]:

    cells = row.find_all("td")

    record = {}

    for i in range(len(headers)):
        record[headers[i]] = cells[i].get_text(strip=True)

    data.append(record)

import os

print(os.getcwd())
import json

with open(r"C:\Users\rohan\Documents\github-projects\MY-Python\Learning-Journey\Webscraping\table_data.json","w",encoding="utf-8") as f:
    json.dump(data, f, indent=4)