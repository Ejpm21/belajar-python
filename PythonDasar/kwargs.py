# misal ada sebuah function
def buat_konfigurasi(host, port, env="production", **pengaturan_lain):
    print(f"{host} : {port} : {env}")
    
# dan kita mengisi agumennya makan, argumen 1 yaitu api.domain akan mengisi parameter 1, lalu 433 akan mengisi parameter2
# tetapi setelahnya yaitu user='admin' karena tidak terdeteksi parameter user maka akan langsung dimasukan ke dalam **pengaturan lain
# dan setelah parameter itu semua argumen harus memiliki parameter yang dituju misal diisi 344 argumennya akan error karena 
# parameter yang di tuju tidak jelas misal halaman='344' maka akan dimasukan ke **
# intinya setelah posisional argumen sudah di langgar, yaitu pada saat user='admin' maka harus menyertakan parameter yang dituju
# dan jika parameter yang dituju terdapat dalam parameter maka nilainya akan masuk ke situ tetapi jika parameter yang dituju tidak ada
# maka akan masuk ke **kwargs

buat_konfigurasi('api.domain.com', 443, user='admin', timeout=30)

## contoh kasus
def buat_laporan(data_utama, **opsi_format):
    print("Membuat laporan...")
    
    # Opsi default
    format_laporan = {
        'format_file': 'pdf',
        'orientasi': 'portrait',
        'resolusi_dpi': 300
    }
    
    # Perbarui format default dengan opsi dari pengguna (kwargs)
    format_laporan.update(opsi_format)
    
    print(f"Data: {data_utama}")
    print(f"Opsi Final: {format_laporan}")

# Panggilan dasar
buat_laporan("Data Penjualan 2025")

# Panggilan dengan opsi tambahan
buat_laporan(
    "Data Kinerja Karyawan", 
    format_file="docx", 
    orientasi="landscape",
    penulis="Budi"
)