def tentukan_grade(nilai):
    if nilai >=90 and nilai <=100:
        hasil = "A"
    elif nilai >=80:
        hasil = "B"
    elif nilai >=70:
        hasil = "C"
    elif nilai >=60:
        hasil = "D"
    elif nilai < 60 and nilai >= 0:
        hasil = "E"
    else:
        hasil = "Nilai Tidak Valid"
    return hasil

print(tentukan_grade(80))
    
