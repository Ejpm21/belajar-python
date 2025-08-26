data_asli = [1, 2, 2, 3, 4, 3, 5, 1, 6]
data_unik = []

for i in data_asli:
    if i not in data_unik:
        data_unik.append(i)
        
print(f"List asli: {data_asli}")
print(f"List setelah duplikat dihapus: {data_unik}")

# cara cepat
# data_unik_cepat = list(set(data_asli))
# print(data_unik_cepat)