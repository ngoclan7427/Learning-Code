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
