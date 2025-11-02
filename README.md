# labpy03
Latihan 1 py
Menampilkan n bilangan acak yang lebih kecil dari 0.5
Nilai n diinput saat program dijalankan (runtime)
Boleh menggunakan kombinasi while dan for
Menggunakan fungsi random() dari modul random
# latihan1.py
from random import random

# Meminta input nilai n dari pengguna
n = int(input("Masukkan nilai N: "))

print()  # memberi jarak baris
for i in range(1, n + 1):
    a = random()
    if a < 0.5:
        print(f"data ke: {i} => {a}")
    else:
        # Jika lebih besar dari 0.5, buat ulang sampai < 0.5
        while a >= 0.5:
            a = random()
        print(f"data ke: {i} => {a}")

print("Selesai")
from random import random → mengimpor fungsi untuk membuat bilangan acak antara 0 sampai 1.
input("Masukkan nilai N: ") → untuk menentukan berapa banyak data yang akan ditampilkan.
for i in range(1, n + 1): → perulangan sebanyak n kali.
random() → menghasilkan bilangan acak.
if a < 0.5: → hanya menampilkan bilangan yang lebih kecil dari 0.5.
while a >= 0.5: → memastikan ulang agar hanya muncul nilai di bawah 0.5.
print("Selesai") → menandakan program selesai.

Masukkan nilai N: 5
data ke: 1 => 0.1729492204357056
data ke: 2 => 0.08717360127477924
data ke: 3 => 0.05051607654502832
data ke: 4 => 0.2753512421571644
data ke: 5 => 0.39262323000723776
Selesai

latihan 2 py
Modal awal = Rp100.000.000
Bulan 1–2 → belum ada laba (0)
Bulan 3–4 → laba 1% dari modal (Rp1.000.000)
Bulan 5–7 → laba 5% dari modal (Rp5.000.000)
Bulan 8 → laba turun jadi 3% (Rp3.000.000)
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
Laba bulan ke- 1 sebesar: 0
Laba bulan ke- 2 sebesar: 0
Laba bulan ke- 3 sebesar: 1000000.0
Laba bulan ke- 4 sebesar: 1000000.0
Laba bulan ke- 5 sebesar: 5000000.0
Laba bulan ke- 6 sebesar: 5000000.0
Laba bulan ke- 7 sebesar: 5000000.0
Laba bulan ke- 8 sebesar: 3000000.0
Total laba adalah: 19000000.0

# latihan 3.py

saldo = 1000000 → saldo awal Rp1.000.000
Program berjalan terus menggunakan while True: sampai pengguna memilih keluar atau saldo habis.
Jika memilih 1 (Tarik Uang):
Diminta input jumlah penarikan.
Dicek apakah jumlah > saldo (jika iya, ditolak).
Jika cukup, saldo dikurangi dan ditampilkan saldo terbaru.
Jika memilih 2 (Keluar) → program berhenti.
Jika saldo sudah 0, program otomatis berhenti juga.


