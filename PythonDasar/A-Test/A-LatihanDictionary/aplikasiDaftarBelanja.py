# membuat catatan daftar belanja  dengan menyimpan nama barang dan jumlahnya

banyak = int(input("Berapa Banyak Item Belanja: "))

data_belanja = []

for i in range(0, banyak):
    print(f"\n Data ke-{i+1}")
    barang = input("Nama Barang : ")
    jumlah = input("Jumlah Barang   : ")
    
    daftar = {
        "barang" : barang,
        "jumlah" : jumlah
    }
    
    data_belanja.append(daftar)
    
print("\nDaftar Belanja:")
for i in range(len(data_belanja)):
    data = data_belanja[i]
    print(f"{i+1}. {data["barang"]} ({data["jumlah"]} pcs)")