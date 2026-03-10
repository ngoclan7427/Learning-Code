import os
import shutil

path = "/Users/YourName/Downloads"
files = os.listdir(path)

for file in files:
    filename, extension = os.path.splitext(file)
    extension = extension[1:]
    if os.path.exists(path+'/'+extension):
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
    else:
        os.makedirs(path+'/'+extension)
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
import os
import shutil

# Đoạn code này tự động phân loại và di chuyển các tệp tin vào thư mục riêng dựa trên phần mở rộng (đuôi file) của chúng
path = "/Users/YourName/Downloads"
files = os.listdir(path)
for file in files:
    filename, extension = os.path.splitext(file)
    extension = extension[1:]
    if os.path.exists(path+'/'+extension):
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
