import string
import random

def generate_password(length):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for i in range(length))

print("Mật khẩu mới của bạn là:", generate_password(12))
# Hàm này tạo một mật khẩu ngẫu nhiên gồm chữ cái, chữ số và ký tự đặc biệt với độ dài tùy chọn
def generate_password(length):
