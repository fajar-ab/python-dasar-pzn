# mencari huruf dalam kata
kata = input("masukkan kata: ")
huruf_dicari = input("masukkan huruf yang dicari: ")

for huruf in kata:
    if huruf == huruf_dicari:
        print(f"huruf {huruf_dicari} ditemukan dalam kata {kata}")
        break
else:
    print(f"huruf {huruf_dicari} tidak ditemukan dalam kata {kata}")