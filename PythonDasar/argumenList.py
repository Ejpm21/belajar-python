def jumlah(*angka):
    for i in angka:
        total = 0
        total += i
    print(f"Total {angka} = {total}")
    
jumlah(20, 15, 30)

def hallo(sapa,*nama):
    for i in nama:
        print(f"{sapa}, {i}" )
        
hallo("selamat pagi", "eka", "jipa" ,"rolim")