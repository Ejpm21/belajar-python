def daftar_peserta(list_pendaftar):
    hasil = sorted(set(list_pendaftar))
    return hasil
daftar = ["eka","jpm","ani","arif","eka","budi"]
peserta = daftar_peserta(daftar)
print(peserta)