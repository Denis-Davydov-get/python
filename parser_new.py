import csv
import requests
from bs4 import BeautifulSoup

url = 'https://tsaritsyno-museum.ru/the_museum/collection/skulptura/'
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
parse_element = soup.findAll('div', class_='flex')
title_link = []
link = []

for page in parse_element:
    product_name = page.find('a', class_='product-name').text
    product_url = page.find('a', class_='product-name').get('href')
    title_link.append(product_name)
    link.append(product_url)

with open("parse.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(
        ('title', 'link')
    )
spisok = [[title_link],[link]]

for result in spisok:
    with open("parse.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow(
            result
        )


