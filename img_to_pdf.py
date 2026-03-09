from PIL import Image

def convert_img_pdf(img_path, pdf_path):
    image = Image.open(img_path)
    img_converted = image.convert('RGB')
    img_converted.save(pdf_path)
    print("Đã chuyển đổi xong!")

# convert_img_pdf("image.jpg", "output.pdf")
from PIL import Image  # Nhập module Image từ thư viện Pillow (PIL) để xử lý hình ảnh

def convert_img_pdf(img_path, pdf_path):
    # Mở tệp hình ảnh từ đường dẫn được cung cấp (img_path)
    image = Image.open(img_path)
 # Chuyển đổi hệ màu của ảnh sang 'RGB'
    # Bước này rất quan trọng vì PDF thường yêu cầu định dạng RGB, 
    # và nó giúp loại bỏ kênh Alpha (độ trong suốt) nếu ảnh gốc là PNG
    img_converted = image.convert('RGB')
# Lưu ảnh đã chuyển đổi dưới định dạng PDF vào đường dẫn pdf_path
    # Thư viện Pillow sẽ tự nhận diện định dạng dựa trên đuôi file .pdf
    img_converted.save(pdf_path)
    
    # Thông báo ra màn hình sau khi hoàn tất
    print("Đã chuyển đổi xong!")
