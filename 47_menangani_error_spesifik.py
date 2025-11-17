print("=== KALKULATOR SEDERHANA ===")

try:
    angka1 = int(input("angka pertama : "))
    angka2 = int(input("angka kedua   : "))

    hasil = angka1 / angka2

    print(f"hasil pembagian : {hasil}")

except ValueError:
    print("mohon masukkan angka yang valid!")

except ZeroDivisionError:
    print("tidak bisa dibagi dengan nol!")

except:
    print("terjadi kesalahan yang lain")

print("=== PROGRAM SELESAI ===")