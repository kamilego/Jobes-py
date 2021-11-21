import requests
from bs4 import BeautifulSoup

next_bottom = True
num_page = 1

while next_bottom:
    website = requests.get(f"https://quotes.toscrape.com/page/{num_page}")
    soup = BeautifulSoup(website.text, "html.parser")
    next_bottom = soup.select_one(".next > a")
    quotes = soup.find_all(class_="quote")
    for quote in quotes:
        text = quote.find(class_="text")
        print(f"Quote: {text.text}")
        author = quote.find(class_="author")
        print(f"Author: {author.text}")
        tags = quote.find_all(class_="tag")
        tags_list = [elem.text for elem in tags]
        print("Tags:", ", ".join(tags_list))
        print()
    print(f"Scrapped page num {num_page}\n")
    num_page += 1