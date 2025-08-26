def faktorial(n):
    total = 1
    print(f"Hasil dari {n}! =", end="")
    for i in range(n,0,-1):
        total *= i
        if i == 1:
            print(f"{i} =", end="")
        else:
            print(f" {i} * ", end="")
    print(f" {total}")
    
faktorial(5)