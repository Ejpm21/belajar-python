def jumlah(*angka):
    total = 0
    for i in angka:
        total += i
    # nilai yang di return terdapat 2 index yaitu index total[0] dan index angak[1]
    return (total, angka)

# dalam artian penjulaham = (total, angka)
penjumlahan = jumlah(20, 15, 30)
print(f" {penjumlahan[1]} totalnya adalah {penjumlahan[0]}")

# bisa melakukan looping untuk mengakses semua datanya
for i in penjumlahan[1]:
    print(i)
print(f"dan totalnya yaitu {penjumlahan[0]}")

# tidak bisa karena tidak mengembalikan nilai karena print hanya untuk output, jadi tidak bisa disimpan dalam variable
def jumlahh(*angka):
    total = 0
    for i in angka:
        total += i
    print(f"totalnya adalah {total}")

anjay = jumlahh(10, 10, 10)
print(anjay)

#contoh impelemntasi pada pajak barang
# jadi method  pajak menyimpan nilai totalPajak saay variable x berisik method pajak dengan parameter
# maka akan dihitung dan menjadi nilai dari x
 
def pajak(pajakk, harga):
    totalPajak = harga + (harga * pajakk / 100)
    return totalPajak

x = pajak(10, 100)
print(f"total harga barang ditambah pajak yaitu {x}")