def penjumlahan():
    try:
        print("\n=== program penjumlahan ===")

        angka1 = int(input("angka 1 : "))
        angka2 = int(input("angka 2 : "))

        hasil = angka1 + angka2

        print(f"hasil penjumlahan {angka1} + {angka2} = {hasil}")
        print("=== program penjumlahan selesai ===")

    except ValueError:
        print("masukkan angka")

    finally:
        input("Enter untuk lanjut ")


def pengurangan():
    try:
        print("\n=== program pengurangan ===")

        angka1 = int(input("angka 1 : "))
        angka2 = int(input("angka 2 : "))

        hasil = angka1 - angka2

        print(f"hasil pengurangan {angka1} - {angka2} = {hasil}")
        print("=== program pengurangan selesai ===")

    except ValueError:
        print("masukkan angka")

    finally:
        input("Enter untuk lanjut ")


def perkalian():
    try:
        print("\n=== program perkalian selesai ===")

        angka1 = int(input("angka 1 : "))
        angka2 = int(input("angka 2 : "))

        hasil = angka1 * angka2

        print(f"hasil perkalian {angka1} * {angka2} = {hasil}")
        print("=== program perkalian selesai ===")

    except ValueError:
        print("masukkan angka")
    
    finally:
        input("Enter untuk lanjut ")


def pembagian():
    try:
        print("\n=== program pembagian ===")

        angka1 = int(input("angka 1 : "))
        angka2 = int(input("angka 2 : "))

        hasil = angka1 / angka2

        print(f"hasil pembagian {angka1} / {angka2} = {hasil}")
        print("=== program pembagian selesai ===")

    except ValueError:
        print("masukkan angka")

    except ZeroDivisionError:
        print("tidak bisa dibagi nol")
    
    finally:
        input("Enter untuk lanjut ")


def menu():

    while True:
        print("\n=== Program Kalkulator Sederhana ===")
        print("[1] Penjumlahan")
        print("[2] Pengurangan")
        print("[3] Perkalian")
        print("[4] Pembagian")
        print("[0] Keluar")
        print()

        pilihan = int(input("Pilihan : "))

        match pilihan:
            case 1:
                penjumlahan()
            case 2:
                pengurangan()
            case 3:
                perkalian()
            case 4:
                pembagian()
            case 0:
                print("=== Sampai Jumpa Lagi ===")
                break
            case _:
                print("pilih lagi yang benar")


menu()