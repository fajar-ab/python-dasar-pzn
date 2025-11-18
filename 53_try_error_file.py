print("=== MENAMPILAKAN DATA NILAI ===")

try:
    with open("nilai_siswa.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")

            print(f"{data[0]} : {data[1]}")

except FileNotFoundError:
    print("file tidak ditemukan!")

print("=== PROGRAM SELESAI ===")