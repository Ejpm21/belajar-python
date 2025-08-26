def analisis_teks(teks):
    hasil = {}
    kata = teks.split()
    total = len(kata)
    unik = len(set(kata))
    frekuensi = {}
    for i in kata:
        if i in frekuensi:
            frekuensi[i] +=1
        else:
            frekuensi[i] = 1
    hasil["Total_kata"] = total
    hasil["Jumlah_kata_unik"] = unik
    hasil["frekuensi_kata"] = frekuensi
    return hasil
         
print(analisis_teks("saya eka jiparolim saya sedang belajar python dan juga belajar mysql"))