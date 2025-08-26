def linear_search(data_list, target):
    for i in range(len(data_list)):
        # Bandingkan elemen saat ini dengan target
        if data_list[i] == target:
            return i  # Kembalikan indeks jika ditemukan
    
    # Kembalikan -1 jika loop selesai dan tidak menemukan target
    return -1

daftar_nilai = [88, 92, 77, 65, 99, 81]
nilai_dicari = 99
indeks_hasil = linear_search(daftar_nilai, nilai_dicari)

if indeks_hasil != -1:
    print(f"Nilai {nilai_dicari} ditemukan di indeks ke-{indeks_hasil}.")
else:
    print(f"Nilai {nilai_dicari} tidak ditemukan dalam daftar.")

# Contoh lain
print(linear_search(daftar_nilai, 100))