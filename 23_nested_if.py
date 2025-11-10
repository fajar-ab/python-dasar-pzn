username = input("masukkan username: ")
password = input("masukkan password: ")

if username == "admin":
    if password == "12345":
        print("login berhasil.\nselmat datang admin!")
    else:
        print("password salah!")
else:
    print("username salah!")