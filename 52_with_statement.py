print("=== MENAMPILAKAN DATA NILAI ===")

with open("nilai_siswa.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")

        print(f"{data[0]} : {data[1]}")

print("=== PROGRAM SELESAI ===")