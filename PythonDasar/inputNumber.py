print("Anggka Pertama")
a = input()

print("Angka Kedua")
b = input()

hasil = a + b
print(f"{a} + {b} = {hasil}")
# hasilnya akan 55, kenapa? karna default dari input itu string jadi teks 5 ditambah teks 5

# ini mengubah inputan menjadi int  
print("angka pertama")
c = int(input())
print("angka kedua")
d = int(input())

hasil2 = c + d
print(f"{c} + {d} adalah {hasil2}")