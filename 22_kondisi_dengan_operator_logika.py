umur = int(input("masukkan umur: "))
punya_sim = input("punya sim? (ya/tidak): ")

if umur >= 17 and punya_sim == "ya":
    print("boleh mengendarai motor!")
else:
    print("tidak boleh mengendarai motor!")