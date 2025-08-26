def pisah_ganjil_genap(*list_angka):
    genap = []
    ganjil = []
    for i in list_angka:
        if i % 2 == 0:
            genap.append(i)
        else:
            ganjil.append(i)
    return genap,ganjil

hasil = pisah_ganjil_genap(2,1,4,5,7,4,2,23,4,2,34,644)
print(f"Genap: {hasil[0]} | Ganjil: {hasil[1]}")