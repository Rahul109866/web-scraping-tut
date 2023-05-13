import csv
import requests
from bs4 import BeautifulSoup


try:
    response = requests.get("https://www.nike.com/in/w/new-mens-shoes-3n82yznik1zy7ok")
    response.raise_for_status()
    print("Page Accessed Successfully!")
except requests.exceptions.RequestException as e:
    print(f"Page Access Failed {e}")

soup = BeautifulSoup(response.text, 'html.parser')
data = soup.select('div[class="product-card__body"]')

with open('nikenew.csv', "w", newline='',encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Shoe Name', 'MRP'])

    for x in data:
        name = x.find('div', class_="product-card__titles").text.strip()
        price = x.find('div', class_="product-card__price").text.strip()
        writer.writerow([name, price])

print("Data printed successfully to nike.csv")
