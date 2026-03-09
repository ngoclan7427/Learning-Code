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
