# membuat set dengan data
buah_buahan = {"apel", "jeruk", "pisang"}

print(buah_buahan)

# menambah elemen
buah_buahan.add("mangga")
buah_buahan.add("mangga")
print(buah_buahan)

# menghapus elemen 
buah_buahan.remove("jeruk")
print(buah_buahan)

# menampilkan elemen
for buah in buah_buahan:
    print(f"buah {buah}")