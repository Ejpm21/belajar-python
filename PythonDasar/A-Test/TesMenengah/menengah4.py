print("Pilihan Operasi:")
print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")

operasi = int(input("Masukan Pilihan Operasi (1-4): "))

if operasi in [1, 2, 3, 4]:
    banyak = int(input("Berapa data yang ingin dimasukkan? "))
    angka_pertama = int(input("Masukan angka ke-1: "))
    
    if operasi == 1:
        total = angka_pertama
        for i in range(1, banyak):
            angka = int(input(f"Masukan angka ke-{i+1}: "))
            total += angka
        print(f"Hasil dari penjumlahan tersebut adalah = {total}")

    elif operasi == 2:
        total = angka_pertama
        for i in range(1, banyak):
            angka = int(input(f"Masukan angka ke-{i+1}: "))
            total -= angka
        print(f"Hasil dari pengurangan tersebut adalah = {total}")

    elif operasi == 3:
        total = angka_pertama
        for i in range(1, banyak):
            angka = int(input(f"Masukan angka ke-{i+1}: "))
            total *= angka
        print(f"Hasil dari perkalian tersebut adalah = {total}")

    elif operasi == 4:
        total = angka_pertama
        for i in range(1, banyak):
            angka = int(input(f"Masukan angka ke-{i+1}: "))
            if angka == 0:
                print("Tidak bisa dibagi dengan 0!")
                break
            total /= angka
        else:
            print(f"Hasil dari pembagian tersebut adalah = {total}")
else:
    print("Pilihan tidak valid.")
