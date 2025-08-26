gudang = {
    'ID001': {'nama': 'Buku Tulis', 'stok': 20},
    'ID002': {'nama': 'Pensil 2B', 'stok': 50},
    'ID004': {'nama': 'Penggaris', 'stok': 15}
}
pengiriman_baru = [
    ('ID002', 40), 
    ('ID005', 25)  
]

def update_stok(stok_saat_ini, catatan_pengiriman):
    # 1. Loop melalui setiap item di catatan pengiriman
    # 'id_barang' akan berisi 'ID002', 'jumlah_baru' akan berisi 40, dst.
    for id_barang, jumlah_baru in catatan_pengiriman:
        
        # 2. Cek apakah ID barang sudah ada sebagai kunci di dictionary gudang
        if id_barang in stok_saat_ini:
            # Jika ada, akses dictionary bagian dalam dan tambahkan stoknya
            stok_saat_ini[id_barang]['stok'] += jumlah_baru
        else:
            # Jika tidak ada, buat entri baru.
            # Kita perlu menambahkan nama barang secara manual sesuai soal.
            nama_barang_baru = "Unknown" # Default name
            if id_barang == 'ID005':
                nama_barang_baru = 'Pulpen'
                
            stok_saat_ini[id_barang] = {'nama': nama_barang_baru, 'stok': jumlah_baru}
            
    return stok_saat_ini

# Panggil fungsi dan cetak hasilnya
gudang_terbaru = update_stok(gudang, pengiriman_baru)
print(f"Kondisi akhir gudang: {gudang_terbaru}")

for i in gudang:
    print(i)