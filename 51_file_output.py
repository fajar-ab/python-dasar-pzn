print("=== MENAMPILAKAN DATA NILAI ===")

file = open("nilai_siswa.txt", "r")

for line in file:
    data = line.strip().split(",")

    print(f"{data[0]} : {data[1]}")

file.close()

print("=== PROGRAM SELESAI ===")