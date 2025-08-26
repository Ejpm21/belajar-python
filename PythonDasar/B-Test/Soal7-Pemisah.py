def gabung_kalimat(pemisah, *kata_kata):
    hasil = pemisah.join(kata_kata)
    return hasil

print(gabung_kalimat("-", "eka", "jipa", "rolim", "anjay", "mabar"))