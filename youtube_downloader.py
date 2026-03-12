def download_video(url):
    try:
        yt = YouTube(url)
        print(f"Đang tải: {yt.title}")
        stream = yt.streams.get_highest_resolution()
        stream.download()
        print("Tải xuống thành công!")
    except Exception as e:
        print(f"Lỗi: {e}")

link = input("Nhập link YouTube: ")
download_video(link)
from pytube import YouTube  # Nhập thư viện pytube để làm việc với YouTube

def download_video(url):
    try:
        # Khởi tạo đối tượng YouTube từ đường dẫn (URL) truyền vào
        yt = YouTube(url)
 # Hiển thị tiêu đề của video đang chuẩn bị tải
        print(f"Đang tải: {yt.title}")
        
        # Lấy luồng video (stream) có độ phân giải cao nhất có sẵn
        stream = yt.streams.get_highest_resolution()
        
        # Thực hiện tải video về thư mục hiện tại của file code
        stream.download()
        




