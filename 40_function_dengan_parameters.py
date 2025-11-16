# membuat function dengan parameter
def sapa_nama(nama):
    print(f"hello, {nama}")
    print("senang bertemu dengan anda!")

# memanggil function dengan argument
sapa_nama("alice")
sapa_nama("bob")

def hitung_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    print(f"luas persegi panjang = {luas}")

hitung_persegi_panjang(10, 5)
hitung_persegi_panjang(8, 3)