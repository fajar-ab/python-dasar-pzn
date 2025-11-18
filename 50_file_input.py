""" Mode File

Mode    Deskripsi           Contoh Penggunaan    
----------------------------------------------------------------------
r       Read (baca)         Membaca file yang sudah ada
w       Write (tulis)       Menulis file baru atau menimpa file lama
a       Append (tambah)     Menambah data di akhir file
x       Create (buat)       Membuat file baru, error jika sudah ada
"""

print("=== SIMPAN DATA NILAI ===")

file = open("nilai_siswa.txt", "w")

while True:
    nama = input("Tuliskan nama siswa (enter untuk selesai) \n : ")

    if nama == "":
        break
    
    nilai = input("Input nilai siswa \n : ")

    file.write(f"{nama},{nilai}\n")
    print(f"Data {nama} berhasil disimpan.")

file.close()
print("=== PROGRAM SELESAI ===")