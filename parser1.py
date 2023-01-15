import requests
from bs4 import BeautifulSoup

url = 'https://www.caprigoshop.ru'
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
parse = soup.findAll('div', class_='styles-list-M1e9B')
data = []

for page in parse:
    product_name = page.find('a', class_='product-name').text
    product_reference = page.find('a', class_='product_reference').text
    data.append([product_name, product_reference])
    print("название:", product_name, '; артикул:', product_reference)
for x in data:
    print(i)