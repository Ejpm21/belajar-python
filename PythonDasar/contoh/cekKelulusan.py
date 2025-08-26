data_siswa = {
    'S001': {'nama': 'Budi', 'nilai': [80, 85, 75]},
    'S002': {'nama': 'Ani', 'nilai': [70, 75, 65]},
    'S003': {'nama': 'Citra', 'nilai': [90, 95, 88]}
}

def rekap_nilai(data):
    # dictionary baru
    hasil = {}
    # melakukan loop untuk mengakses setiap values dari key
    for value in data.values():
        # membuat variable yang menyimpan nilai dari masing masing key
        nilai = value["nilai"]
        total = 0
        #mengambil total untuk rata rata
        for i in nilai:
            total += i
        rata_rata = total / len(nilai)
        # pengecekan dan pemberian status
        if rata_rata >=75 and rata_rata <=100:
            status = "lulus"
        elif rata_rata <75 and rata_rata >=0:
            status = "Tidak Lulus"
        else:
            status = "Tidak Valid"
        # menyimpan dengan nama sebagai key dan status sebagai values
        hasil[value["nama"]] = status
    return hasil

kelulusan = rekap_nilai(data_siswa)
print(f"Hasil Kelulusan: {kelulusan}")