def hitung_luas_lingkaran(radius):
    pi = 3.14159
    luas = pi * (radius ** 2)
    return luas

luas1 = hitung_luas_lingkaran(5)
luas2 = hitung_luas_lingkaran(10)

print(f"luas lingkaran radius 5 = {luas1}")
print(f"luas lingkaran radius 10 = {luas2}")
print(f"total luas = {luas1 + luas2}")