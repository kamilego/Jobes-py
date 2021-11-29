import requests
from bs4 import BeautifulSoup
import csv


website = requests.get("https://www.britannica.com/topic/list-of-philosophers-2027173")
soup = BeautifulSoup(website.text, "html.parser")
links = soup.select(".topic-list .md-crosslink")
for link in links[:8]:
    website = requests.get(link.attrs["href"])
    soup = BeautifulSoup(website.text, "html.parser")
    try:
        author_name = soup.select_one("h1").text
        description = soup.select_one(".topic-identifier").text
        summary = soup.select_one(".topic-paragraph").text
        try:
            image = soup.select_one(".card img").attrs["src"]
        except AttributeError as error:
            image = None
        information = soup.find_all("dl")
        birth = information[0].select_one(".fact-item").text
        death = information[1].select_one(".fact-item").text
        try:
            sub_of_study = information[3].select_one("dd").find_all("a")
            subjects = ", ".join([elem.text for elem in sub_of_study])
        except IndexError as error:
            subjects = None
        print(f"{author_name}\n{description}\n{summary}\n{image}\n{birth}\n{death}\n{subjects}")
    except:
        print("Something went wrong")
    print()