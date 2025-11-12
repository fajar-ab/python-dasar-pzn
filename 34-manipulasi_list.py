# mengakses elemen
buah = ["apel", "jeruk", "pisang", "mangga"]
print(buah[0])
print(buah[1])
print(buah[2])
print(buah[3])

# mengubah elemen
warna = ["merah", "biru", "hijau"]
print(warna)
warna[1] = "kuning"
print(warna )

buah = ["apel", "jeruk"]
print(buah)

# menambahkan ke paling belakang
buah.append("durian")
print(buah )

# meyisipkan di antara
buah.insert(1, "kelengkeng")
print(buah)

# menghapus item dalam elemen list
buah.remove("jeruk")
print(buah)

# menghapus paling belakang
buah.pop()
print(buah)

del buah[0]
print(buah )

# mengecek panjang elemen di list
buah = ["apel", "jeruk", "mangga"]
print(len(buah))

# menggabungkan list
list1 = [1,2,3,4,5]
print(list1)
list2 = [6,7,8,9,10]
print(list2)

gabungan = list1 + list2
print(gabungan)