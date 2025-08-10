#================================================================
siswa = {
    "nama": "Rina",
    "umur": 17,
    "kelas": "XI IPA"
}
# ubah umur
siswa["umur"] = 18
# tambah data baru hobi:membaca
siswa["Hobi"] = "Membaca"
# Menghapus key
del siswa["kelas"]
# mengecek alamat apakah ada didalm dictionary
if "alamat" in siswa:
    print("ada alamat didalam dictionary")
else:
    print("alamat tidak ada dalam dictionary")


print(siswa)
for key, value in siswa.items():
    print(f"{key} : {value}")