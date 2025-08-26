def bubble_sort(data_list):
    n = len(data_list)
    # loop sebenarnya bisa menggunakan n-1 tetapi untuk mempermudah kode gunakan langsung n karena saat loop terakhir
    # j in range(0,5-4-1) yang otomatis (0,0) jadi akan kosong dan tidak merubah hasil, tetapi untuk efisiensi gunakan n-1
    # i = 0 -> 4
    for i in range(n):
        #ini loop untuk membandingkan per putaran yaitu putaran 0 -> 4
        # untuk putaran 0 maka j in range(0,5-0-1) maka j akan 0 -> 3 karena loop membandingkan [j] dan [j+1]
        # maka jika tidak ada - 1 yang ada disini (n-i-1) pada loop akan terjadi error soalnya [j+1] akan mengakses keluar list
        # selain itu gunanya -i ini agar tidak perlu membandingkan dengan element terakhir yang sudah pasti paling besar
        # jika putaran 0 sudah selesai maka element akhir sudah paling besar begitupun seterusnya
        for j in range(0, n-i-1): 
            # Bandingkan elemen bersebelahan, jika benar tukar posisinya, jika ingin desc tinggal dibalik perbandingannya
            if data_list[j] > data_list[j+1]:
                # ini fitur untuk swap tetapi kalau algoritma yang benar, secara manual untuk semua pemrograman
                # data_list[j], data_list[j+1] = data_list[j+1], data_list[j]
                temp = data_list[j]
                data_list[j] = data_list[j+1]
                data_list[j+1] = temp
    return data_list

angka_acak = [64, 34, 25, 12, 22]
print(f"Hasil Bubble Sort: {bubble_sort(angka_acak)}")
