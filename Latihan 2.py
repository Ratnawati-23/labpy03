# latihan2.py
modal = 100000000  # modal awal 100 juta
total = 0  # total laba

for bulan in range(1, 9):
    if bulan <= 2:
        laba = 0
    elif bulan <= 4:
        laba = modal * 0.01  # 1%
    elif bulan <= 7:
        laba = modal * 0.05  # 5%
    else:
        laba = modal * 0.03  # 3%
    
    total += laba
    print(f"Laba bulan ke- {bulan} sebesar: {laba}")

print(f"Total laba adalah: {total}")