import os, sys
import urllib.parse
import validators
import requests
from datetime import datetime

print("number of arguments: ", len(sys.argv))
print("Arguments list: ", sys.argv)

url = "https://youtube.com"
if len(sys.argv) > 1:
    url = sys.argv[1]

print("Website to download:", url)

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
print(f"Current working dir: {os.getcwd()}")

if not os.path.exists("./websites"):
    os.mkdir("websites")

parsed_url = urllib.parse.urlparse(url)
print(parsed_url)

valid_flag = validators.url(url)
if valid_flag:
    print(f"Url: {url} is valid")
else:
    print(f"Url: {url} is not valid")
    raise Exception("Bad URL!")


response = requests.get(url, allow_redirects=True)
if response.ok:
    print(f"Response ok from server from url: {url}")
    now = datetime.now()
    date_string = now.strftime("%d.%m.%Y %H.%M.%S")
    print(date_string)
    file_name = f"./websites/{parsed_url.netloc} {date_string}.html"
    print(file_name)
    with open(file_name, "wb") as f:
        f.write(response.content)