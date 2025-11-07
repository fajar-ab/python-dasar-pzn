nama = "Alice"
umur = 25
kota = "Jakarta"

# menggunakan concatination
profil = "Hallo, nama saya " + nama + ", umur " + str(umur) + " tahun, tinggal di " + kota
print(profil)

# lebih jelas menggunakan f-string
profil = f"Hallo, nama saya {nama}, umur {umur} tahun, tinggal di {kota}"
print(profil)

# f-string dengan expression

harga = 100000
jumlah = 3

# operasi matematika dalam string
print(f"Total : Rp {harga * jumlah:,}")

# method calls dalam string
nama = "John Doe"
salam = f"Hello, {nama.upper()}"
print(salam)