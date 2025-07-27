pelanggan = ["eka", "jipar", "rolim"]

# mengakses semua nama pelanggan
print(pelanggan[0])
print(pelanggan[1])
print(pelanggan[2])
# misal mengakses data secara 1 1 seperti ini dan data banyak akan memakan waktu

# gunakan for dan tambahkan variable untuk penyimpanan 
for nama in pelanggan:
    print(f"Hallo {nama}")

for i in range(1, 5, 2):
    print(i)
    
# penjelasan
#
# karena len dari pelanggan itu 3 maka range(3)
# karena i menyimpan nilai range(3) itu menjadi 0, 1, 2
# dan saat i ditampilkan maka yang keluar 0 dan mengakses pelanggan dengan index 0
# jadi saat i bernilai 1 maka akan mengakses pelanggan berindex 1
for i in range(len(pelanggan)):
    print(f"{i},{pelanggan[i]}")
    
# penjelasan 
# lebih simpel untuk mengakses nama pelanggann ditambah ada indexnya
#jadi index bisa diubah sesuka hati mau itu namanya i, urutan dan lain lain memang fungsinya untuk mengakses index
# jadi tidak perlu mengakses pelanggan dengan index lagi
# dan ditambah 1 agar terlihat jelas data pelanggan ke berapa
for index, nama in enumerate(pelanggan):
    print(f"data ke-{index+1}, dengan nama {nama}")