def hitung_frekuensi(kalimat):
    kata_kata = kalimat.lower().split()
    frekuensi = {}

    for kata in kata_kata:
        # Cek apakah 'kata' sudah ada sebagai kunci di dictionary 'frekuensi'
        if kata in frekuensi:
            # Jika ya, tambahkan hitungannya dengan 1
            frekuensi[kata] += 1
        else:
            # Jika tidak, tambahkan 'kata' sebagai kunci baru dengan nilai 1
            frekuensi[kata] = 1
    return frekuensi

kalimat_tes = "saya suka makan nasi dan saya juga suka minum teh"
hasil_hitungan = hitung_frekuensi(kalimat_tes)

print(hasil_hitungan)