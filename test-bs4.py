import requests
from bs4 import BeautifulSoup

r = requests.get("https://xkcd.com/")
# r = requests.get("https://rahul109866.github.io/odin-recipes/recipes/gravy.html")
soup = BeautifulSoup(r.content, "html.parser")
print(soup.prettify())
