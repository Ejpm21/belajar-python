# mengisi list
name = ["eka","jipa","rolim"]

# menambah data ke list
name.append("joko")

# menampilkan semua isi list
print(name)

# menampilkan isi list sesuai index
print(name[0])
print(name[1])
print(name[2])
print(name[3])

# menghitung banyaknya data dalam list
print(len(name))

# menghapus data list
name.remove("rolim")

print(name)

# mengubah data list
name[0] = "Ekajpm"

print(name)

# menghapus berdasarkan index
del name[0]
print(name)

## list didalam list

angka = [[2,1],[3,1]]
# mengakses index ke 1
print(angka[1])

# mengakses index ke 1 dan dialamannya mengakses index ke 0 yaitu 3
print(angka[1][0])

# mengakses index ke 0 dan didamnya mengakses  index ke 1 yaitu 1
print(angka[0][1])