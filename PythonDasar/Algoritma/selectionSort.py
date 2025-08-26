def selection_sort(data_list):
    n = len(data_list)
    
    # Loop luar: Berjalan dari posisi pertama hingga kedua terakhir
    # i adalah batas antara bagian terurut dan belum terurut
    for i in range(1):
        # elemen awal sebagai perbandingan, agar saat i sudah bertambah bukan 0 bisa 1 atau 2 maka index sebelunya
        # tidak akan dibandingkan lagi
        posisi_min = i
        # Loop dimulai dari i digunakan sebagai posisi min dan akan dibandingkan dengan index yang dimulai i+1 
        # yaitu index 1
        for j in range(i + 1, n):
            # karena j adalah 1 maka akan dibandingkan apakah value j > dari min yaitu i yang pada saat ini 0
            if data_list[j] < data_list[posisi_min]:
                # jika index j < index i maka posisi min akan diisi oleh J yaitu saat ini 1
                posisi_min = j
        
        # jika sudah ditentukan posisi min maka posisi min akan bertukar tempat dengan i
        # Operasi penukaran ini hanya terjadi SEKALI per putaran luar
        data_list[i], data_list[posisi_min] = data_list[posisi_min], data_list[i]
        
    return data_list

# Data yang akan diurutkan
angka_acak = [64, 25, 12,14,90]
print(f"Data awal: {angka_acak}")
print(f"Hasil Selection Sort: {selection_sort(angka_acak)}")