print("=== KALKULATOR SEDERHANA ===")

try:
    angka1 = int(input("angka pertama : "))
    angka2 = int(input("angka kedua   : "))

    hasil = angka1 / angka2

    print(f"hasil : {hasil}")
except:
    print("terjadi error dalam perhitungan")

print("=== PROGRAM SELESAI ===")