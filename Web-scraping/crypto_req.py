import requests

coins_dict = {}

def get_coin_list():
    global coins_list
    response = requests.get("https://data.messari.io/api/v1/assets?fields=id,slug,symbol,metrics/market_data/price_usd")
    if response.ok == True:
        print("Response ok")
        data = response.json()
        i = 0
        for elem in data["data"]:
            value = data["data"][i]['metrics']['market_data']['price_usd']
            coins_dict[elem["symbol"]] = round(value, 2)
            i += 1
    for key in coins_dict:
        print(f"{key}: {coins_dict[key]}$")

get_coin_list()