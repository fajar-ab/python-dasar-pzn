nama = "budi"
umur = 24

# cara yang salah (akan error)
# pesan = "nama saya " + nama + " umur saya " + umur

# cara yang benar
pesan = "nama saya " + nama + " umur saya " + str(umur)

print(pesan)

# melihat penjang string
print(len(nama))
print(len(pesan))