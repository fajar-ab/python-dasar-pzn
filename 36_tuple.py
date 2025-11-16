poin = (5, 10)

print(poin)
print(poin[0])
print(poin[1])

# untuk data yang tidak berubah
tanggal_lahir = (15, 11, 2001) # tangga, bulan, tahun
print(f"tanggal lahir : {tanggal_lahir}")

# iterasi tuple
for e in tanggal_lahir:
    print(e)

# iterasi tuple dengan index
for i in range(len(tanggal_lahir)):
    print(tanggal_lahir[i])