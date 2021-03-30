import requests
from bs4 import BeautifulSoup

# This is for parsing text from any website

url = "https://www.nytimes.com/international/"
r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

for line in soup.find_all('p'):
    if line.string != 'None':
        print(line.string)
