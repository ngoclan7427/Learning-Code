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
 # Gửi yêu cầu GET đến URL và chuyển đổi nội dung phản hồi (JSON) thành một Dictionary trong Python
    response = requests.get(url).json()
    
    # Truy cập vào các khóa trong Dictionary để lấy giá trị 'rate' (giá Bitcoin) của đồng USD
    # Cấu trúc JSON: response -> 'bpi' -> 'USD' -> 'rate'
    price = response['bpi']['USD']['rate']
 # In giá Bitcoin hiện tại ra màn hình
    print(f"Giá Bitcoin hiện tại: ${price}")



  
