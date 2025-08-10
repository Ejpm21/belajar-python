# 1============================================================
siswa = {}


nama = input("Masukkan Nama : ")
umur = input("Masukkan Umur : ")
hobi = input("Masukkan Hobi : ")


siswa["nama"] = nama
siswa["umur"] = umur
siswa["hobi"] = hobi


print("\nData Siswa:")
for key, value in siswa.items():
    print(f"{key} : {value}")

# 2============================================================
# gunakan list dictionary
banyak = int(input("\nMasukan Jumlah data: "))
data_siswa = []

for i in range(0, banyak):
    print(f"\nData ke-{i+1}")
    nama = input("Masukkan Nama : ")
    umur = input("Masukkan Umur : ")
    hobi = input("Masukkan Hobi : ")


    siswa = {
        "nama": nama,
        "umur": umur,
        "hobi": hobi
    }
    
    data_siswa.append(siswa)
    
print("\nData Yang Berhasil Disimpan")
for i in range(len(data_siswa)):
    print(f"Data siswa ke-{i+1}")
    for key, value in data_siswa[i].items():
        print(f"{key} : {value}")
        
# 3============================================================
