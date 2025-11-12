# mencari password yang benar dengan batas percobaan

password_benar = "python123"
percobaan = 0
max_percobaan = 3

while percobaan < max_percobaan:
    password = input("masukkan password: ")
    percobaan += 1

    if password == password_benar:
        print("login, berhasil!")
        break
    else:
        print(f"password salah, sisa percobaan {max_percobaan - percobaan}")
else:
    print("terlalu banyak percobaan gagal, akses ditolak")