# untuk menyambungkan sebuah string jika menggunakan + kan cukup lama ya, seperti dibawah ini
nama_depan = "Eka"
nama_tengah = "Jipa"
nama_belakang = "rolim"

sapa = "hallo" + " " + nama_depan + " " + nama_tengah + nama_belakang
# ini sangat memakan waktu jadi gunakan format
print(sapa)

# format, sama saja tapi lebih simple
sapa = f"Hallo {nama_depan} {nama_tengah}{nama_belakang}"
print(sapa)

# contoh jika tidak pakai variable sapa
print(f"Hallo {nama_depan} {nama_tengah}{nama_belakang}")