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