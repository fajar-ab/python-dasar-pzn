import random

def app_tebak_angka():
    angka_acak = random.randint(1, 10)
    maksimal_tebakan = 3
    tebakan = 0

    while tebakan < maksimal_tebakan:
        try:
            angka_user = int(input("\nmasukkan angka : "))

            if angka_user == angka_acak:
                print("tebakan anda benar!")
                break
            elif angka_user > angka_acak:
                print("angka terlalu besar")
            elif angka_user < angka_acak:
                print("angka terlalu kecil")

        except ValueError:
            print("value yang dimasukkan salah hanya integer")
            continue

        tebakan += 1
    else:
        print("anda telah melewati maksimal tebakan")
        print(f"angka acak adalah {angka_acak}")


def menu():

    while True:
        print("\n=== PROGRAM TEBAK ANGKA ===")
        print("[1] Tebak Angka")
        print("[0] Keluar")

        try:
            pilihan = int(input("Pilihan : "))

        except ValueError:
            print("masukkan angka yang benar!")

        else:
            if pilihan == 1:
                app_tebak_angka()
            elif pilihan == 0:
                break
            else:
                print("masukkan angka 1 atau 0")

menu()