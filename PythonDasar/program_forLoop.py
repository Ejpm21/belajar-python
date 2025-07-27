# Memasukkan input untuk menentukan jumlah data yang akan disimpan
data = int(input("Berapa banyak data yang ingin dibuat? "))

# List kosong untuk menyimpan data nama dan umur
nama = []
umur = []

# Loop untuk menginputkan data sebanyak jumlah yang diminta
# dimulai dari 0 karna range diakhiri dengan data - 1
for i in range(0, data):
    # Karena i dimulai dari 0, maka ditambah 1 agar tampilannya dimulai dari 1
    print(f"Masukkan data ke-{i + 1}")
    
    # Input nama dan umur dari user
    input_nama = input("Masukkan Nama : ")
    input_umur = int(input("Masukkan Umur : "))
    
    # Tambahkan data ke dalam list
    nama.append(input_nama)
    umur.append(input_umur)

# Menampilkan hasil data yang sudah dikumpulkan
# Variabel 'i' boleh dipakai kembali karena nilainya akan diisi ulang oleh loop baru
for i in range(0, len(nama)):
    print(f"Data ke-{i + 1}: Nama = {nama[i]}, Umur = {umur[i]}")
