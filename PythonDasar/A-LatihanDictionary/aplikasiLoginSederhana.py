# Data akun yang sudah tersedia
akun = {
    "user1": "password123",
    "admin": "admin123",
    "rina": "hobiMembaca"
}

# Input dari user
username = input("Masukkan Username: ")
password = input("Masukkan Password: ")

# Cek apakah username ada dan passwordnya cocok
if username in akun:
    if akun[username] == password:
        print("Login berhasil!")
    else:
        print("Password salah.")
else:
    print("Username tidak ditemukan.")
