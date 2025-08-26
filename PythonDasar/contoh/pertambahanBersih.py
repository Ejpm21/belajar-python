def jumlah(*angka):
    total = 0
    for i in angka:
        total += i
    #yang di return 1 nilai memiliki 2 data yaitu total dan angka, dan didalam angka ada data lagi
    return (total, angka)

def bersih(angka):
    for idx, i in enumerate(angka[1]):
        if idx == 0:
            print(i,end="")
        else:
            print(f" + {i}", end="")
    print(f" = {angka[0]}")

bersih(jumlah(10,20,30,40,10))