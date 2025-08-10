def palindrom(kata):
    balik = ""
    for i in kata:
        # jadi huruf diakses 1 per 1 sama i lalu dimasukan balik, lalu ditaro belakang dari variable balik
        balik = i + balik
    
    if kata == balik:
        return True
    else:
        return False

kata = input("Masukan Kata: ")

if palindrom(kata):
    print(f"{kata} adalah palindrom")
else:
    print(f"{kata} bukan palindrom") 