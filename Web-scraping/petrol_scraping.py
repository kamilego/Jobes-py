import requests
from bs4 import BeautifulSoup


def scrap_site():
    link = r"https://moto.trojmiasto.pl/paliwa/"
    website = requests.get(link)
    soup = BeautifulSoup(website.text, "html.parser")
    table = soup.find(class_="prices-table")
    body = table.select("tr")[1:11]
    return body

def create_petrol_dict(body):        
    petrol_dict = {}
    for elem in body:
        petrol_station = elem.find("h3", {"class": "prices-table__name"})
        price = elem.find("span", {"class": "prices-table__price"})
        petrol_station =  petrol_station.text.strip()
        price =  float(price.text.strip()[:4])
        if not petrol_station in petrol_dict:
            petrol_dict[petrol_station] = [price]
        else:
            petrol_dict[petrol_station].append(price)
    return petrol_dict

def main():
    scrapped_element = scrap_site()
    petrol_dict = create_petrol_dict(scrapped_element)
    for key, value in petrol_dict.items():
        print(f"{key}: {min(value)}zł")
if __name__ == '__main__':
    main()
