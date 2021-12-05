import requests
from bs4 import BeautifulSoup


choice = input("Enter product which you wanna buy: ")
free_shipping = input("Wanna free shiping? (Y/N): ")
max_price = float(input("What is the max value?: "))

for num in range(1, 5):
    website = requests.get(f"https://www.ebay.com/sch/i.html?_nkw={choice}&_sacat=0&_pgn={num}")
    soup = BeautifulSoup(website.text, "html.parser")

    items = soup.select(".srp-results .s-item")
    for elem in items:
        name = elem.h3.text
        price = elem.select_one(".s-item__price").text
        print(price)
        if "," in price:
            price = price.replace(",", "")
        if price.count("$") == 2:
            price = float(price.split()[-1][1:])
        else:
            price = price[1:]
        try:
            shipping = elem.select_one(".s-item__shipping").text
        except:
            shipping = None
        if float(price) <= max_price:
            if free_shipping.lower() == "y":
                if "Free" in shipping:
                    print(f"{name}\n{price}\n{shipping}")
            else:
                print(f"{name}\n{price}\n{shipping}")

    print(f"Scraped page no. {num}")
    print("============================================================")
