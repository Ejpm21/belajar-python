data_penjualan = [('Apel', 50), ('Jeruk', 30), ('Apel', 20), ('Mangga', 40)]

def rekap_penjualan(data):
    penjualan = {}
    for nama, value in data:
        if nama in penjualan:
            penjualan[nama] += value
        else:
            penjualan[nama] = value
    return penjualan

print(rekap_penjualan(data_penjualan))
    