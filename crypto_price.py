import requests

def get_btc_price():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url).json()
    price = response['bpi']['USD']['rate']
    print(f"Giá Bitcoin hiện tại: ${price}")

get_btc_price()
