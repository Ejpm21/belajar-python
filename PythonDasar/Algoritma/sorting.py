def bubble_sort_trace(lst):
    n = len(lst)
    print(f"Data awal: {lst}\n")
    for i in range(n):
        print(f"Putaran ke-{i+1}:")
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]  # tukar
            print(f"  Step {j+1}: {lst}")
        print()
    return lst

data = [5, 3, 8, 4, 2]
hasil = bubble_sort_trace(data)
print(f"Hasil akhir: {hasil}")

print("===================================================")
def selection_sort_trace(lst):
    n = len(lst)
    print(f"Data awal: {lst}\n")
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if lst[j] < lst[min_index]:
                min_index = j
        # Tukar jika ditemukan nilai lebih kecil
        lst[i], lst[min_index] = lst[min_index], lst[i]
        print(f"Putaran ke-{i+1}: {lst}")
    return lst

data2 = [64, 25, 12, 22, 11]
hasil = selection_sort_trace(data2)
print(f"\nHasil akhir: {hasil}")
