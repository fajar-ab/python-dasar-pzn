def perkenalan(nama, umur, kota):
    print(f"nama : {nama}")
    print(f"umur : {umur} tahun")
    print(f"kota : {kota}")
    print("---")

# positional argument (urutan harus sesuai)
perkenalan("fajar", 23, "padangsidimpuan")

# keyword argument (urutan bebas)
perkenalan(kota="bandung", nama="boblazar", umur=30)
perkenalan(umur=28, kota="surabaya", nama="charlie")


def buat_profil(nama, umur, kota="jakarta", pekerjaan="belum bekerja"):
    print("==== POFIL ====")
    print(f"nama\t\t: {nama.upper()}")
    print(f"umur\t\t: {umur}")
    print(f"kota\t\t: {kota}")
    print(f"pekerjaan\t: {pekerjaan}\n")

# positional + keyword argument
buat_profil("alice", 25)
buat_profil("bob", 30, kota="bandung")
buat_profil("charlie", 28, pekerjaan="developer")
buat_profil("diana", 32, kota="surabaya", pekerjaan="designer")