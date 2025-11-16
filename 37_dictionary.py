# membuat dictionary dengan data
siswa = {
    "nama": "John",
    "umur": 21,
    "kelas": "12A"
}

print(siswa)
print(siswa["nama"])
print(siswa["umur"])
print(siswa["kelas"])

# mengubah nilai
siswa["umur"] = 22
print(siswa)

# menghapus key-value
del siswa["kelas"]
print(siswa)

# menginterasi keys
for key in siswa:
    print(key, "-", siswa[key])

# mengiterasi key-value pairs
for key, value in siswa.items():
    print(f"{key} - {value}")