try:
    angka = int(input("masukkan angka: "))

    print(f"{angka} adalah angka yang anda masukkan.")

except ValueError:
    print("hanya masukkan angka saja!")

finally:
    print("program selesai dijalankan")
    
else:
    print("code else")
