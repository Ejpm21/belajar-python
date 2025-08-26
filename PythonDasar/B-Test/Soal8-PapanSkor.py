papan_skor = {
    "Budi" : 20,
    "Ani" : 50,
}

def update_skor(papan_skor, nama_pemain, skor_baru):
    if nama_pemain in papan_skor:
        papan_skor[nama_pemain] += skor_baru
    else:
        papan_skor[nama_pemain] = skor_baru
    return papan_skor

print(update_skor(papan_skor, "Budi", 30))
print(update_skor(papan_skor, "Ani", 10))
print(update_skor(papan_skor, "Asep", 100))