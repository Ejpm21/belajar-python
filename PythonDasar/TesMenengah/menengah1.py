banyak = int(input("Berapa Jumlah Siswa? "))

data_siswa = []

for i in range(0, banyak):
    nama = input(f"Nama Siswa ke-{i+1}: ")
    nilai = int(input("Nilai: "))
    
    siswa = {
        "nama" : nama,
        "nilai": nilai
    }
    
    data_siswa.append(siswa)
    
total = 0
for i in range(len(data_siswa)):
    data = data_siswa[i]
    total = total + data["nilai"]
    
rata =  total /len(data_siswa)
print(f"\nRata-Rata nilai Siswa: {rata}")

# jadi max akan mencari 1 per 1 dari dictionary data_siswa, 1 per 1 akan dikirim melalui key dan ditaro di funtion ambil_nail
# lalu ambil nilai akan memasukannnya ke parameter lalu di return untuk mengambil nilainya saja
# jika semua sudah melalui ambil nilai, max akan mengecek data mana yang paling tinggi nilainya
# lalu memberikan semua dataya ke nilai_tertinggi
def ambil_nilai(siswa):
    return siswa["nilai"]

nilai_tertinggi = max(data_siswa, key=ambil_nilai)
# disini dari data nilai tertinggi menampilkan nama dan nilainya
print(f"Nilai tertinggi: {nilai_tertinggi['nama']} dengan nilai {nilai_tertinggi['nilai']}")