# tanpa enumerate
buah = ["apel", "mangga", "jeruk"]

for b in buah:
    print(b)
print("==================================================")

#dengan enumerate
for idx, b in enumerate(buah):
    print(idx, b)
print("==================================================")

# start index custom
for idx, b in enumerate(buah, start=1):
    print(idx, b)
