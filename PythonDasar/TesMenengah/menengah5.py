data_siswa = []

while True:
    print("\n===== MENU =====")
    print("1. Masukkan Data")
    print("2. Tampilkan Data")
    print("3. Selesai")

    pilihan = input("Pilih menu (1/2/3): ")

    if pilihan == "1":
        nama = input("Masukkan nama: ")
        nilai = int(input("Masukkan nilai: "))
        #shortcut seperti pada soal pertama, kalau yang ini langsung memasukan directory ke list
        data_siswa.append({"nama": nama, "nilai": nilai})
        print("Data berhasil disimpan!")

    elif pilihan == "2":
        if not data_siswa:
            print("Belum ada data.")
        else:
            print("\n=== DATA SISWA ===")
            # i = 1
            # for item in data:
            #     print(i, item)
            #     i += 1
            # jika dilakukan tanpa enumerate
            # i akan mengambil index data yang dimulai dari 1, item akan mengambil data dari dalam directory
            for i, item in enumerate(data_siswa, start=1):
                print(f"{i}. {item['nama']} - Nilai: {item['nilai']}")
                
            total = 0
            for i in range(len(data_siswa)):
                data = data_siswa[i]
                total = total + data["nilai"]
                
            rata = total / len(data_siswa)
            print(f"Nilai Rata-ratanya: {rata}")
            
            def nilai(siswa):
                return siswa["nilai"]
            
            nilai_tertinggi = max(data_siswa, key=nilai)
            print(f"Nilai tertinggi: {nilai_tertinggi['nama']} dengan nilai {nilai_tertinggi['nilai']}")
            
            nilai_terendah = min(data_siswa, key=nilai)
            print(f"Nilai terendah: {nilai_terendah['nama']} dengan nilai {nilai_terendah['nilai']}")

    elif pilihan == "3":
        print("Program selesai. Terima kasih!")
        break

    else:
        print("Pilihan tidak valid. Coba lagi.")
