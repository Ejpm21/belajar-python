def konversi_detik(total_detik):
    jam = total_detik // 3600
    sisa_detik = total_detik % 3600
    menit = sisa_detik // 60
    detik = sisa_detik % 60
    print(f"Output: {jam} jam {menit} menit {detik} detik")

    
input = int(input("Input Detik: "))
konversi_detik(input)