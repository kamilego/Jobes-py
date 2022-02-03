import requests
from bs4 import BeautifulSoup

link = r"https://moto.trojmiasto.pl/paliwa/"
website = requests.get(link)
soup = BeautifulSoup(website.text, "html.parser")
table = soup.find(class_="prices-table")
body = table.select("tr")[1:6]
for elem in body:
    petrol_station = elem.find("h3", {"class": "prices-table__name"})
    price = elem.find("span", {"class": "prices-table__price"})
    print(petrol_station.text.strip())
    print(price.text.strip()[:4]+"zł")
