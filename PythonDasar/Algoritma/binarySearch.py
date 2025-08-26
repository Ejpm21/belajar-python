def binary_search(data, target):
    #definisikan kiri dan kanan yang dimana kanan adalah panjang data -1 karena index dimulai dari 0
    kiri = 0
    kanan = len(data) - 1
    
    # selagi kondisi kiri ini masih lebih kecil atau sama dengan kanan maka lakukan pengecekan
    while kiri <= kanan:
        # inisialisasi index tengah
        tengah = (kiri + kanan) // 2
        # ambil index tengah untuk dibandingkan dengan target
        nilai_tengah = data[tengah]
        # lakukan looping terus sampai nilai tengah ini == target atau kondisi false yang menyebabkan loop selesai
        if nilai_tengah ==  target:
            return tengah
        # jika nilai tengah ini lebih besar dari target berarti target berada di sisi kiri
        # maka bagian kanan dan index tengah akan dihapus dan batasnya menjadi paling kanan itu index tengah -1
        elif nilai_tengah > target:
            kanan = tengah - 1
        # jika nilai tengah ini lebih kecil berarti target berada disisi kanan dan hapus sisi kiri serta index tengah
        # untuk memperkecil kemungkinan
        else:
            kiri = tengah + 1
    return -1

data = [1,3,4,6,7,10,15]
print(binary_search(data,10))