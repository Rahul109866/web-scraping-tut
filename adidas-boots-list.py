import csv
import requests
from bs4 import BeautifulSoup

headers = {
    'user-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}
response = requests.get('https://in.puma.com/in/en/mens/mens-shoes/mens-shoes-football', headers=headers)
# print(response.status_code)
soup = BeautifulSoup(response.text, 'html.parser')

h3_tags=soup.find_all('h3',class_="relative flex")
for tag in h3_tags:
    text=tag.text
    print(text)