import os

inventaris = [
    {'id': 'A001', 'nama': 'Buku Tulis', 'stok': 20, 'harga': 5000},
    {'id': 'A002', 'nama': 'Pensil 2B', 'stok': 50, 'harga': 2000},
    {'id': 'B001', 'nama': 'Penghapus', 'stok': 30, 'harga': 1500}
]

def clear_screen():
    os.system('cls')
    
def tampilkan_barang():
    for i in inventaris:
        print("=======================================")
        print(f"ID: {i["id"]}\tNama: {i["nama"]}")
        print(f"Stok: {i["stok"]}\tHarga: {i["harga"]}")
    print("=======================================")
    while True:  
        pilih = input("Ketik X untuk Keluar: ")
        if pilih.lower() == "x":
            break
        else:
            print("Input Tidak Valid Tolong Masukan X jika ingin keluar")
    
    
def tambah_barang(data):
    while True:
        ada = False
        id = input("Masukan ID: ")
        for i in data:
            if id.replace(" ", "").lower() == i["id"].replace(" ", "").lower():
                ada = True
        if ada:
            print("Maaf ID sudah digunakan")
        else:
            nama = input("Masukan Nama: ")
            stok = int(input("Masukan stok: "))
            harga = float(input("Masukan Harga: "))
        
            return {
                "id": id.upper(),
                "nama": nama.title(),
                "stok": stok,
                "harga": harga
            }

def cari_barang(inventaris, nama="none", id="none"):
    if id == "none":
        for i in range(len(inventaris)):
            if nama == inventaris[i]["nama"].replace(" ","").lower():
                return i 
        return -1
    else:
        data = inventaris.copy()
        n = len(data)
        for i in range(n-1):
            min = i
            for j in range(i+1, n):
                if data[j]["id"] < data[min]["id"]:
                    min = j
            data[i], data[min] = data[min], data[i] 
        
        kiri = 0
        kanan = n - 1
        while kiri<=kanan:
            tengah = (kiri + kanan) //2
            nilai_tengah = data[tengah]["id"].replace(" ","").lower()
            
            if nilai_tengah ==  id:
                for i in range(len(inventaris)):
                    if inventaris[i]["id"].replace(" ","").lower() == id:
                        return i
                break
            elif nilai_tengah > id:
                kanan = tengah - 1
            else:
                kiri = tengah + 1
        return -1
        
def urutkan_inventaris(inventaris, opsi, order = 0):
    n = len(inventaris)
    if opsi == 1:
        # berdasarkan nama
        for i in range(n-1):
            for j in range(0, n-i-1):
                if inventaris[j]["nama"].lower() > inventaris[j+1]["nama"].lower():
                    inventaris[j], inventaris[j+1] = inventaris[j+1], inventaris[j]
        return inventaris
    else:
        # ASC harga
        if order == 1:
            for i in range(n-1):
                min = i
                for j in range(i+1, n):
                    if inventaris[j]["harga"] < inventaris[min]["harga"]:
                        min = j
                inventaris[min], inventaris[i] = inventaris[i], inventaris[min]
            return inventaris
        else:
            for i in range(n-1):
                max = i
                for j in range(i+1, n):
                    if inventaris[j]["harga"] > inventaris[max]["harga"]:
                        max = j
                inventaris[max], inventaris[i] = inventaris[i], inventaris[max]
            return inventaris
            

while True:
    # clear_screen()
    print("=========================")
    print("======   Pilihan   ======")
    print("1. Tampilkan semua Barang")
    print("2. Tambah Barang Baru")
    print("3. Cari Barang")
    print("4. Urutkan Barang Berdasarkan Nama/Harga")
    print("5. Keluar")
    pilihan = int(input("Masukan Pilihan: "))
    
    if pilihan == 1:
        clear_screen()
        tampilkan_barang()
        print("\n\n")
        
    elif pilihan == 2:
        clear_screen()
        tambah = tambah_barang(inventaris)
        inventaris.append(tambah)
        print("Barang Berhasil Ditambahkan!\n\n")
        
    elif pilihan == 3:
        clear_screen()
        pilih = int(input("Ketik 1 jika ingin mencari lewat nama, 2 untuk mencari ID: "))
        
        if pilih == 1:
            target = input("Masukan Nama produk yang diicari: ")
            data = cari_barang(inventaris, nama=target.replace(" ","").lower())
            
            if data == -1:
                print("Data tidak ditemukan")
            else:
                print(f"data dengan nama {target} ditemukan pada index ke-{data}")
                print(f"ID: {inventaris[data]["id"]} | Nama: {inventaris[data]["nama"]} | Stok: {inventaris[data]["stok"]} | Harga: {inventaris[data]["harga"]}\n\n")
                
        elif pilih == 2:
            target = input("Masukan ID produk yang dicari: ")
            hasil = cari_barang(inventaris, id=target.replace(" ","").lower())
            
            if hasil == -1:
                print("Data tidak ditemukan")
            else:
                print(f"data dengan ID {target} ditemukan pada index ke-{hasil}")
                print(f"ID: {inventaris[hasil]["id"]} | Nama: {inventaris[hasil]["nama"]} | Stok: {inventaris[hasil]["stok"]} | Harga: {inventaris[hasil]["harga"]}\n\n")
            
        else:
            print("Angka Tidak Valid")
    
    elif pilihan == 4:
        clear_screen()
        print("===   Pilihan   ===")
        print("1. Urutkan Berdasarkan Nama")
        print("2. Urutkan Berdasarkan Harga")
        opsi = int(input("Masukan Pilihan:"))
        if opsi == 1:
            urutkan_inventaris(inventaris, 1)
        elif opsi == 2:
            print("\n\ningin menampilkan dengan ASC atau DESC?")
            print("1. ASC")
            print("2. DESC")
            order = int(input("Pilihan: "))
            if order == 1:
                urutkan_inventaris(inventaris, 2, 1)
            elif order == 2:
                urutkan_inventaris(inventaris, 2, 2)
            else:
                print("Inputan Tidak Valid")
        else:
            print("Inputan Tidak Valid")
        print("Data Berhasil Di Urutkan Bisa Dilihat Di Menu Nomor 1\n\n")
    elif pilihan == 5:
        break
    else:
        print("Inputan Tidak Valid, tolong Input sesuai yang ada di Menu!")

print("Terimakasih")
