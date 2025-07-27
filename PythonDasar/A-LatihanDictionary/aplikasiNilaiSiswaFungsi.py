banyak = int(input("Jumlah Siswa : "))
data_siswa = []

for i in range(0, banyak):
    def predikat(ujian):
        if ujian >= 80 and ujian <= 100:
            return "Baik"
        elif ujian <= 79 and ujian >= 50:
            return "Cukup"
        elif ujian <= 49 and ujian >=0:
            return "Kurang"
        else:
            return "Tidak diketahui"
        
    print(f"\nData  ke-{i+1}")
    nama = input("Nama  : ")
    nilai = int(input("Nilai    : "))
    Predikat = predikat(nilai)
    
    siswa = {
        "nama" : nama,
        "nilai" : nilai,
        "predikat" : Predikat
    }
    
    data_siswa.append(siswa)

print("\nHasil: ")
for i in range(len(data_siswa)):
    data = data_siswa[i]
    print(f"{data['nama']} - Nilai: {data['nilai']}, predikat: {data['predikat']}")

total = 0
for i in range(len(data_siswa)):
    data = data_siswa[i]
    total = data["nilai"] + total
    
rata = total / len(data_siswa)
print(f"\nRata-rata Nilai: {rata}")

# versi GPT ==============================================================================
# def predikat(ujian):
#     if 80 <= ujian <= 100:
#         return "Baik"
#     elif 50 <= ujian <= 79:
#         return "Cukup"
#     elif 0 <= ujian <= 49:
#         return "Kurang"
#     else:
#         return "Tidak diketahui"

# banyak = int(input("Jumlah Siswa : "))
# data_siswa = []

# for i in range(banyak):
#     print(f"\nData ke-{i+1}")
#     nama = input("Nama  : ")
#     nilai = int(input("Nilai : "))
#     hasil_predikat = predikat(nilai)
    
#     siswa = {
#         "nama": nama,
#         "nilai": nilai,
#         "predikat": hasil_predikat
#     }
    
#     data_siswa.append(siswa)

# print("\nHasil:")
# for data in data_siswa:
#     print(f"{data['nama']} - Nilai: {data['nilai']}, Predikat: {data['predikat']}")

# total = sum([data["nilai"] for data in data_siswa])
# rata = total / len(data_siswa)
# print(f"\nRata-rata Nilai: {rata}")
