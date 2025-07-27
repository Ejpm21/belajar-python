data_siswa = [
    {"nama": "Andi", "nilai": 80},
    {"nama": "Budi", "nilai": 95},
    {"nama": "Citra", "nilai": 90}
]

nilai_tertinggi = max(data_siswa, key=lambda x: x["nilai"])["nilai"]
print(nilai_tertinggi)