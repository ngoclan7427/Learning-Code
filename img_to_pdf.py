from PIL import Image

def convert_img_pdf(img_path, pdf_path):
    image = Image.open(img_path)
    img_converted = image.convert('RGB')
    img_converted.save(pdf_path)
    print("Đã chuyển đổi xong!")

# convert_img_pdf("image.jpg", "output.pdf")
