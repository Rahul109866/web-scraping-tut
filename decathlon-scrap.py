import requests
from bs4 import BeautifulSoup


response = requests.get('https://www.decathlon.in/men-s-tops/men-tshirts-17107?id=17107&type=c&id=1710717107&type=c')
response.raise_for_status()
# print(response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')
brand = soup.findAll("div", class_='capitalize text-14 lg:text-14 whitespace-nowrap overflow-ellipsis overflow-hidden '
                                   'mt-1' )
