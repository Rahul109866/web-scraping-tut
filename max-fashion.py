import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
response = requests.get("https://www.maxfashion.in/in/en/search?q=%3Abadge.title.en%3ABuy%201%20Get%201&&utm_source=google&utm_medium=search&utm_campaign=1029125494&adgroupid=54250473527&utm_content=413530848214&utm_term=max%20fashion%20website&gclid=CjwKCAjwo7iiBhAEEiwAsIxQEXryV2_q5z0hU5iFR211X2qYD2ADe54ex4NvtZxusZGJrpDqrjQ5pxoCFD4QAvD_BwE", headers= headers)
print(response.status_code)