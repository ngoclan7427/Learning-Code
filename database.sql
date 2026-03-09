CREATE TABLE Users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO Users (username, email) VALUES ('admin', 'admin@example.com');
Tạo một bảng mới có tên là 'Users'
CREATE TABLE Users (
    -- Cột id: kiểu số nguyên (INT), là khóa chính (PRIMARY KEY) để định danh duy nhất mỗi hàng,
    -- và tự động tăng giá trị khi có bản ghi mới (AUTO_INCREMENT)
id INT PRIMARY KEY AUTO_INCREMENT,
    
    -- Cột username: chuỗi ký tự tối đa 50 ký tự, bắt buộc phải có giá trị (NOT NULL)
    username VARCHAR(50) NOT NULL,
    
    -- Cột email: chuỗi ký tự tối đa 100 ký tự, giá trị không được trùng lặp giữa các người dùng (UNIQUE)
    email VARCHAR(100) UNIQUE,
