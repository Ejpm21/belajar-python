db_siswa = {
    '101': {'nama': 'Budi', 'jurusan': 'IT'},
    '102': {'nama': 'Ani', 'jurusan': 'Sistem Informasi'}
}

def cari_siswa(nim, data_bank):
    for key, data in data_bank.items():
        if str(nim) == key:
            return data
    return "Siswa Tidak Ditemukan"
    

cari1 = cari_siswa(101,db_siswa)
cari2 = cari_siswa(102,db_siswa)
cari3 = cari_siswa(103,db_siswa)
print(cari1)
print(cari2)
print(cari3)
