function checkStrength(password) {
    let strength = 0;
    if (password.length > 7) strength++;
    if (/[A-Z]/.test(password)) strength++;
    if (/[0-9]/.test(password)) strength++;
    if (/[^A-Za-z0-9]/.test(password)) strength++;
    return ["Yếu", "Trung bình", "Khá", "Mạnh"][strength - 1] || "Rất yếu";
}
console.log(checkStrength("P@ss1234"));
/**
 * Hàm kiểm tra độ mạnh của mật khẩu
 * @param {string} password - Chuỗi mật khẩu cần kiểm tra
 * @returns {string} - Trả về nhãn tương ứng với độ mạnh
 */
function checkStrength(password) {
    let strength = 0; // Biến đếm số điểm đạt được (tối đa 4 điểm)

    // Điều kiện 1: Độ dài mật khẩu phải trên 7 ký tự
    if (password.length > 7) strength++;

    // Điều kiện 2: Sử dụng Regex để kiểm tra xem có ít nhất một chữ cái VIẾT HOA không
    if (/[A-Z]/.test(password)) strength++;
// Điều kiện 3: Kiểm tra xem có ít nhất một chữ số (0-9) không
    if (/[0-9]/.test(password)) strength++;

    // Điều kiện 4: Kiểm tra xem có ít nhất một ký tự đặc biệt không
    // [^A-Za-z0-9] có nghĩa là bất kỳ ký tự nào KHÔNG phải là chữ cái hay chữ số
    if (/[^A-Za-z0-9]/.test(password)) strength++;
 /**
     * Trả về kết quả dựa trên mảng nhãn:
     * strength = 1 -> index 0: "Yếu"
     * strength = 2 -> index 1: "Trung bình"
     * strength = 3 -> index 2: "Khá"
     * strength = 4 -> index 3: "Mạnh"
     * Nếu strength = 0, kết quả của mảng là undefined, toán tử || sẽ lấy giá trị mặc định là "Rất yếu"
     */
    return ["Yếu", "Trung bình", "Khá", "Mạnh"][strength - 1] || "Rất yếu";
}
