public class PrimeCheck {
    public static boolean isPrime(int n) {
        if (n <= 1) return false;
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) return false;
        }
        return true;
    }
    public static void main(String[] args) {
        System.out.println(isPrime(29)); // Output: true
    }
}
   if (n <= 1) return false;
// Bước 1: Các số <= 1 không phải là số nguyên tố (ví dụ: 0, 1, số âm)
 // Tại sao dùng Math.sqrt(n)? 
        // Vì nếu n có một ước số lớn hơn căn bậc hai, thì chắc chắn nó phải có một ước số khác nhỏ hơn căn bậc hai.
        // Việc này giúp vòng lặp chạy ít lần hơn, tăng tốc độ xử lý (tối ưu hóa).
        for (int i = 2; i <= Math.sqrt(n); i++) {
            // Bước 3: Nếu n chia hết cho bất kỳ số 'i' nào trong khoảng này
            // thì n không phải là số nguyên tố.
            if (n % i == 0) return false;
        }
return true;
    }

    public static void main(String[] args) {
        int number = 29;
        // Gọi hàm isPrime và in kết quả ra màn hình
        if (isPrime(number)) {
            System.out.println(number + " là số nguyên tố.");
        } else {
            System.out.println(number + " không phải là số nguyên tố.");
        }
    }
}
