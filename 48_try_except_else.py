try:
    angka = int(input("masukkan angka : "))

except ValueError:
    print("input tidak valid, hanya masukkan angka")

else:
    print(f"angka yang ada masukkan {angka}")

    if angka > 0:
        print("angka positif")
    elif angka < 0:
        print("angka negatif")
    else:
        print("angka nol")