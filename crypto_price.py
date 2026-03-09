import requests

def get_btc_price():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url).json()
    price = response['bpi']['USD']['rate']
    print(f"Giá Bitcoin hiện tại: ${price}")

get_btc_price()
import requests  # Import thư viện requests để gửi yêu cầu HTTP đến API

def get_btc_price():
    # URL của API CoinDesk cung cấp giá Bitcoin thời gian thực (định dạng JSON)
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
