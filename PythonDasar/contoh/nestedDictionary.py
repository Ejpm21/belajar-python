kontak = {}

kontak["budi@email.com"] = {
    "nama" : "Budi Santoso",
    "telepon" : "081234567",
}

kontak["ani@email.com"] = {
    "nama" : "Ani Lestari",
    "telepon" : "087654321",
}

kontak["budi@email.com"]["telepon"] = "081111111"

cari = kontak.get("citra@email.com","Kontak tidak ditemukan")
print(cari)

for email, data in kontak.items():
    # habis di buka langsung akses datanya
    nama = data["nama"]
    telepon = data["telepon"]
    
    print(f"Email: {email} | Nama: {nama} | Telepon: {telepon}")