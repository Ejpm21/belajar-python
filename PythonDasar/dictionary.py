biodata = {
    "nama": "Sinta",
    "umur": 25
}

print(biodata["nama"])  # Output: Sinta
# atau, ini bisa digunakan jika kita tidak tau pasti apakah key "nama" beneran ada di dictionary, jika ada print nama jika tidak ya kosong
nama = biodata.get("nama", "kosng")
print(nama)

biodata["umur"] = 26    # Mengubah nilai
biodata["hobi"] = "Membaca"  # Menambah data

print(biodata)

for key, value in biodata.items():
    print(f"{key} : {value}")

# ========================================================
# bersarang

mahasiswa = {
    "001": {"nama": "Ani", "jurusan": "Informatika"},
    "002": {"nama": "Budi", "jurusan": "Sistem Informasi"}
}

print(mahasiswa["001"]["nama"])  # Output: Ani
print(mahasiswa["002"])

# ============================================================
#list dictionary
produk = [
    {"nama": "Buku", "harga": 15000},
    {"nama": "Pulpen", "harga": 5000}
]

for p in produk:
    print(f"{p['nama']} - Rp{p['harga']}")
