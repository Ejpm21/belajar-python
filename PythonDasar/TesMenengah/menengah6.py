kalimat = input("Masukkan kata: ")

# List untuk menampung huruf vokal
vokal = ['a', 'e', 'i', 'o', 'u']
huruf_vokal = []


# Looping untuk memeriksa setiap huruf dalam kata
for huruf in kalimat:
    # menggunakan lower agar huruf sama semua
    if huruf.lower() in vokal:  
        huruf_vokal.append(huruf)

kata = kalimat.split()
banyak_kalimat = len(kata)

print("Jumlah kata dalam kalimat adalah:", banyak_kalimat)
print("jumlah huruf vokal yang ada dalam kalimat:", len(huruf_vokal))
