import sys
import time
from calendar import monthrange
from datetime import datetime, timedelta

from dateutil import relativedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

days_dict = {
    "Monday": "Pon",
    "Tuesday": "Wt",
    "Wednesday": "Śr",
    "Thursday": "Czw",
    "Friday": "Pt",
    "Saturday": "Sob",
    "Sunday": "N"
}

months_dict = {
    "1": "Styczeń",
    "2": "Luty",
    "3": "Marzec",
    "4": "Kwiecień",
    "5": "Maj",
    "6": "Czerwiec",
    "7": "Lipiec",
    "8": "Sierpień",
    "9": "Wrzesień",
    "10": "Pażdziernik",
    "11": "Listopad",
    "12": "Grudzień"
}

PATH = r"C:\Users\kamil.legowicz\Downloads\chromedriver.exe"
WEBSITE = "https://www.google.pl/"
search_text = sys.argv[1]
print(search_text)

options = webdriver.ChromeOptions()
# options.add_argument("headless")
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(PATH, options=options)
driver.maximize_window()
driver.get(WEBSITE)

cookies = driver.find_element(By.ID, "L2AGLb").click()
search = driver.find_element(By.ID, "APjFqb")

search.send_keys(search_text)
time.sleep(1)
search.send_keys(Keys.ENTER)
time.sleep(1)
options = driver.find_elements(By.CLASS_NAME, "oFoqE")[1].click()
time.sleep(1)
one = driver.find_elements(By.XPATH, "//div[@jsname='ibnC6b']")
for elem in one:
    if "W jedną stronę" in elem.text:
        elem.click()

day = datetime.today().day + 1
month = datetime.today().month
timestamp = f"{day}. {month}"

timestamp_input = driver.find_element(By.CLASS_NAME, "oRRgMc").clear()
timestamp_input = driver.find_element(By.CLASS_NAME, "oRRgMc")
timestamp_input.send_keys(timestamp)
timestamp_input.send_keys(Keys.ENTER)

done = driver.find_element(By.CLASS_NAME, "eE8hUfzg9Na__overlay").click()
time.sleep(0.2)

timestamp = datetime.today() + timedelta(days=1)
price = driver.find_element(By.CLASS_NAME, "GARawf").text.replace("zł", "").replace(" ","")

pol_month = months_dict[str(timestamp.month)]
pol_day = days_dict[timestamp.strftime("%A")]
data = {pol_month:{f"{timestamp.day:<2} {pol_day:<3}": int(price)}}

month_sum = 2
nextmonth1 = timestamp + relativedelta.relativedelta(months=1)
nextmonth2 = timestamp + relativedelta.relativedelta(months=2)
for elem in [timestamp, nextmonth1, nextmonth2]:
    month_sum += monthrange(elem.year, elem.day)[1]

for _ in range(month_sum):
    timestamp += timedelta(days=1)
    next = driver.find_element(By.CLASS_NAME, "hLDSxb").click()
    time.sleep(0.3)
    price = driver.find_element(By.CLASS_NAME, "GARawf").text.replace("zł", "").replace(" ","")
    pol_day = days_dict[timestamp.strftime("%A")]
    pol_month = months_dict[str(timestamp.month)]
    if pol_month not in data:
        data[pol_month] = {f"{timestamp.day:<2} {pol_day:<3}": int(price)}
    else:
        data[pol_month][f"{timestamp.day:<2} {pol_day:<3}"] = int(price)

print("-"*30)
for key in data:
    data[key] = sorted(data[key].items(), key=lambda x: x[1])[:3]
    print(data[key])
    for k, v in sorted(data[key], key=lambda x: int(list(x).split(" ")[0])):
        print(f"{key:<11}", k, v, "zł")
    print("-"*30)


# driver.quit()
