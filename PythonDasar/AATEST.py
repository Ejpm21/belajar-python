kalimat = input("Masukan Kalimat untuk Mengecek palindrom: ")
cek = kalimat.replace(" ", "").lower()
for i in range(0, len(cek)//2):
    if cek[i] != cek[-(i+1)]:
        palindrom = 1
    else:
        palindrom = 0
        
if palindrom == 1:
    print("Bukan palindrom")
else:
    print("palindrom")


