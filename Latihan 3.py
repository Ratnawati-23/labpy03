# latihan3.py

saldo = 1000000  # saldo awal Rp 1.000.000

while True:
    print(f"\nSaldo saat ini: Rp {saldo}")
    print("1. Tarik Uang")
    print("2. Keluar")

    menu = input("Pilih menu (1/2): ")

    if menu == "1":
        jumlah = int(input("Masukkan jumlah penarikan: "))
        if jumlah > saldo:
            print("Saldo tidak cukup!")
        else:
            saldo -= jumlah
            print("Penarikan berhasil!")
            if saldo == 0:
                print("Saldo anda sudah habis.")
                break
    elif menu == "2":
        print("Terima kasih telah menggunakan ATM!")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")