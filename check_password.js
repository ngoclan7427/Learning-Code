function checkStrength(password) {
    let strength = 0;
    if (password.length > 7) strength++;
    if (/[A-Z]/.test(password)) strength++;
    if (/[0-9]/.test(password)) strength++;
    if (/[^A-Za-z0-9]/.test(password)) strength++;
    return ["Yếu", "Trung bình", "Khá", "Mạnh"][strength - 1] || "Rất yếu";
}
console.log(checkStrength("P@ss1234"));
