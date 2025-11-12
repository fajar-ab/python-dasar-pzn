# mencetak angka 1 samapai 5
angka = 1
while angka < 5:
    print(angka)
    angka += 1

password = ""

while password != "12345":
    password = input("masukkan password: ")
    if password != "12345":
        print("password salah, coba lagi.")

print("password benar!")