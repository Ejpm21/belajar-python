gudang_a = {
    'apel': 50,
    'jeruk': 75,
    'mangga': 30
}
gudang_b = {
    'jeruk': 40,
    'mangga': 25,
    'anggur': 60
}

def gabungkan_stok(stok_a,stok_b):
    # stok_total= stok_a |jika terjadi perubahan pada stok_total maka saat memanggil stok a setelah function akan 
    # menyebabkan stok a ikut berubah jadi gunakan .copy() untuk memastikan ini 2 entitas yang berbeda
    # itu terjadi di file gudang.py
    stok_total = stok_a.copy()
    for key, value in stok_b.items():
        if key in stok_total:
            stok_total[key] += value
        else:
            stok_total[key] = value
    return stok_total

hasil = gabungkan_stok(gudang_a, gudang_b)
print(f"Stok Total Gabungan: {hasil}")
    