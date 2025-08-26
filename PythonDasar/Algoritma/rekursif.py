# Misal kita dalam kasus faktorial, dan bandingkan penggunaan loop iteratif dan juga rekursif

# Loop iteratif
def faktorial_loop(n):
    total = 1
    for i in range(1, n + 1):
        total *= i
    return total

print(f"Versi Loop: {faktorial_loop(5)}")

# Versi Rekursif
# Jadi logikanya 5 * 4!
def faktorial_rekursif(n):
    # 1. Base Case (Kasus Dasar): Faktorial dari 1 adalah 1. Ini kondisi berhenti kita.
    if n == 1:
        return 1
    # 2. Recursive Step (Langkah Rekursif): Kalikan n dengan faktorial dari (n-1).
    else:
        return n * faktorial_rekursif(n - 1)

print(f"Versi Rekursif: {faktorial_rekursif(5)}")

# misal dalam kasus rekursif(4)
# function akan mengecek apakah n = 1, jika tidak maka n akan dikali function rekursif lagi tetapi n -1
# jadi function rekursif(4) akan dikali function rekursif(3) di function rekursif(3) akan dicek apakah n =1 karena
# n =3 maka akan dilanjut dikali dengan 3-1 yaitu rekursif(2)  sampai n=1 karena n==1 itu return 1
# maka di rekursif(2) n yaitu 2 dikalikan dengan 1 di return nilainya ke rekursif(3) seterusnya sampai ada di
# rekursif(4) maka akan mereturn hasilnya
# jadi intinya dari 4->3->2->1 base case lalu return nilainya 1->2->3->4