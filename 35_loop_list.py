# mengakses list dengan looping
buah_buahan = ["apel", "mangga", "jeruk"]

for buah in buah_buahan:
    print(buah)

# mengakses list dengan loop melalui indexnya
for i in range(len(buah_buahan)):
    print(f"{i} - {buah_buahan[i]}")


# pengecekan dengan in
if "apel" in buah_buahan:
    print("ada apel")
else:
    print("tidak ada apel")