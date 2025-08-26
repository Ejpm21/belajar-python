kalimat = input("Masukkan sebuah kalimat: ").lower()

# Variabel untuk menghitung, dimulai dari 0
jumlah_vokal = 0

# Definisikan huruf vokal
vokal = "aiueo"

# Lakukan perulangan untuk setiap huruf dalam kalimat
for huruf in kalimat:
    # Cek apakah huruf saat ini adalah salah satu dari vokal, in digunakan untuk apakah huruf ada didalam vokal
    if huruf in vokal:
        # Jika ya, tambah hitungan
        jumlah_vokal += 1

# Cetak hasil akhir setelah loop selesai
print(f"Jumlah huruf vokal dalam kalimat tersebut adalah: {jumlah_vokal}")