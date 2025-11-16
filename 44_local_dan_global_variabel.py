def fungsi_test():
    x = 10 # local variabel
    print(f"nilai dari x adalah {x}")

fungsi_test()
# print(x) # tidak bisa mengakses local variabel dari luar function

nama_global = "alice"

def tampilkan_nama():
    print(f"nama : {nama_global}")

def ubah_nama():
    global nama_global
    nama_global = "bob" # mengubah global variabel

tampilkan_nama()
ubah_nama()
tampilkan_nama()