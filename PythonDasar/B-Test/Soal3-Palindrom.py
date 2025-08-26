def cek_palindrome(kata):
    test = kata.lower().replace(" ", "")
    for i in range(len(test)//2):
        if test[i] != test[(-(i+1))]:
            return False
    return True

hasil = cek_palindrome("kasur ini rusak")
print(hasil)