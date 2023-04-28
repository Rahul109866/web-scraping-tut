import csv
import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.nike.com/in/w/new-mens-shoes-3n82yznik1zy7ok")
soup = BeautifulSoup(response.text, 'html.parser')
data = soup.select('div[class="product-card__body"]')

with open('nike.csv', "w", newline='',encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Shoe Name', 'MRP'])

    for x in data:
        name = x.find('div', class_="product-card__titles").text.strip()
        price = x.find('div', class_="product-card__price").text.strip()
        writer.writerow([name, price])

print("Data printed successfully to nike.csv")
