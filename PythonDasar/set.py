nama = {"Eka", "eka", "jipa"}
nama.add("jpm")
print(nama)

for i in nama:
    print(i)


# Untuk membuat set kosong, gunakan set(), bukan {}
set_kosong = set() 
bukan_set_kosong = {} # Ini akan membuat dictionary kosong

# misal ada kondisi list dan kita ingin mengubahnya agar tidak terjadi duplikat
# contoh kasus unya daftar ID pengguna yang melakukan aktivitas
# dan Anda hanya ingin tahu berapa banyak pengguna unik yang aktif
id_pengguna_aktif = [101, 102, 103, 101, 104, 102]
pengguna_unik = set(id_pengguna_aktif)
print(f"Jumlah pengguna unik yang aktif: {len(pengguna_unik)}")