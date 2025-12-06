angka = [5,3,0,4,8,1,6,2,7,9]

for i in range(len(angka)):
    for j in range(len(angka) - 1):
        if angka[j] > angka[j + 1]:
            angka[j], angka[j + 1] = angka[j + 1], angka[j]

print(angka)