import string
import random

def generate_password(length):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for i in range(length))

print("Mật khẩu mới của bạn là:", generate_password(12))
# Hàm này tạo một mật khẩu ngẫu nhiên gồm chữ cái, chữ số và ký tự đặc biệt với độ dài tùy chọn
def generate_password(length):
  chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for i in range(length))
print("Mật khẩu mới của bạn là:", generate_password(12))
import string  # Nhập thư viện chứa các chuỗi ký tự mẫu (chữ cái, chữ số)
import random  # Nhập thư viện để thực hiện việc chọn ngẫu nhiên
def generate_password(length):
    # Tạo một chuỗi chứa tất cả các ký tự cho phép:
    # string.ascii_letters: bao gồm chữ hoa (A-Z) và chữ thường (a-z)
    # string.digits: bao gồm các chữ số từ 0-9
    # "!@#$%^&*": các ký tự đặc biệt tự định nghĩa thêm
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
