import requests
from bs4 import BeautifulSoup
import csv

headers = {"Accept-Language": "en-US"}
website = requests.get("https://www.imdb.com/title/tt0770828/", headers=headers)
soup = BeautifulSoup(website.text, "html.parser")

main_title = soup.find("h1").contents[0]
a = soup.find_all(class_="ipc-inline-list ipc-inline-list--show-dividers TitleBlockMetaData__MetaDataList-sc-12ein40-0 dxizHm baseAlt")
movie_info = []
for i in a:
    for elem in i.find_all("li"):
        movie_info.append(elem.text)

duration = movie_info[-1]
description = soup.select_one("p").contents[0].text
rate = soup.find(attrs={"class": "AggregateRatingButton__RatingScore-sc-1ll29m0-1 iTLWoV"}).text
rating_count = soup.find(attrs={"class": "AggregateRatingButton__TotalRatingAmount-sc-1ll29m0-3 jkCVKJ"}).text

cast = soup.find(class_="ipc-sub-grid ipc-sub-grid--page-span-2 ipc-sub-grid--wraps-at-above-l ipc-shoveler__grid")
cast_list = []
for elem in cast:
    actor = elem.find(class_="StyledComponents__ActorName-y9ygcu-1 eyqFnv")
    cast_list.append(actor.text)

print(f"""Title of scraped movie: {main_title}
Movie duration: {duration}
Descritpion: {description}
Rated by {rating_count.lower()} people on IMDb as {rate}/10
Cast: {", ".join(cast_list)}""")
