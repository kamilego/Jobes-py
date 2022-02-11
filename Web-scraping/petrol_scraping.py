import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os
import matplotlib.pyplot as plt


def scrap_site() -> list:
    link = r"https://moto.trojmiasto.pl/paliwa/"
    website = requests.get(link)
    soup = BeautifulSoup(website.text, "html.parser")
    table = soup.find(class_="prices-table")
    body = table.select("tr")[1:11]
    return body


def save_scrapped_petrol_data(body: list, file_name_path: str) -> None:        
    petrol_dict = {}
    for elem in body:
        petrol_station_name = elem.find("h3", {"class": "prices-table__name"}).text.strip()
        petrol_station_location = elem.find("span", {"class": "prices-table__location"}).text.strip()
        price = elem.find("span", {"class": "prices-table__price"})
        price = float(price.text.strip()[:4])
        petrol_dict[petrol_station_name, petrol_station_location] = price
    with open(file_name_path, "w") as f:
        for key, value in petrol_dict.items():
            f.write(f"{key[0]}: {value}zł, {key[1]}\n")
    return petrol_dict


def load_petrol_data(folder_name: str) -> dict:
    data_list = os.listdir(folder_name)
    petrol_read_dict = {}
    for file in data_list:
        file_name_path = os.path.join(folder_name, file)
        with open(file_name_path, "r") as f:
            petrol_data = f.readlines()
            date = file.replace(".txt", "")
            petrol_read_dict[date] = []
            for elem in petrol_data:
                if "Gdańsk" in elem and "Baltic" not in elem:
                    petrol_read_dict[date].append(elem.replace("\n", ""))
            petrol_read_dict[date] = petrol_read_dict[date][0]
    return petrol_read_dict


def plot_graph(data_dict: dict) -> None:
    for date, price in data_dict.items():
        data_dict[date] = float(price.split(",")[0].split()[-1][:-2])
    plt.bar(data_dict.keys(), data_dict.values(), width=0.1)
    plt.title("Wykres najniższych ceny paliw")
    plt.xlabel("Data")
    plt.ylabel("Cena za litr [zł]")
    plt.ylim([5, 5.5])
    plt.show()


def execution_func(folder_name: str) -> None:
    todays_date = datetime.now().strftime("%d-%m-%y")
    file_check_path = os.path.join(folder_name, todays_date+".txt")
    if os.path.exists(file_check_path) == False:
        scrapped_element = scrap_site()
        save_scrapped_petrol_data(scrapped_element, file_check_path)
    petrol_read_dict = load_petrol_data(folder_name)
    plot_graph(petrol_read_dict)


def main():
    folder_name = "saved_data"
    execution_func(folder_name)
if __name__ == '__main__':
    main()
