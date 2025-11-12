# game tebak angka dengan break
angka_rahasia = 7

while True:
    tebakan = int(input("tebak angka (1-10): "))

    if tebakan == angka_rahasia:
        print("selamat! angka benar")
        break
    else:
        print("salah, coba lagi")\


# mencetak angka ganjil saja dengan continue
for i in range(10):
    if i % 2 == 0:
        continue
        
    print(i)