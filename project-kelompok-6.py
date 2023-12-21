import os
import sys
os.system("cls")
pin = 123456
i = 0
limit = 3


def main():
    saldo = 0
    while True:
        # Tampilkan menu utama
        print("1. Cek saldo")
        print("2. Tarik tunai")
        print("3. Setor tunai")
        print("4. Transfer")
        print("5. Keluar")

        # Masukkan pilihan pengguna
        pilihan = int(input("Masukkan pilihan Anda (1-5): "))

         # Lakukan proses sesuai pilihan pengguna
        if pilihan == 1:
            # Cek saldo
            print("Saldo Anda saat ini adalah:", saldo)
        elif pilihan == 2:
            #memasukan jumlah yg ingin di tarik
            jumlah_tarik = int(input("Masukkan jumlah uang yang ingin Anda tarik tunai: "))
            #mengecek jumlah jika melebihi batas penarikan
            if jumlah_tarik <= saldo:
                saldo =- jumlah_tarik
                print("Jumlah uang yang telah Anda tarik tunai adalah:", jumlah_tarik)
            else:
                print("Jumlah uang yang ingin Anda tarik tunai melebihi saldo Anda.")
        elif pilihan == 3:
            # Setor tunai
            print("Masukkan jumlah uang yang ingin Anda setor tunai: ")
            jumlah_setor = int(input())
            saldo += jumlah_setor
            print("Jumlah uang yang telah Anda setor tunai adalah:", jumlah_setor)
        elif pilihan == 4:
            #Transfer
            print("Masukkan nomor rekening tujuan transfer: ")
            nomor_rekening_tujuan = input()
            print("Masukkan jumlah uang yang ingin Anda transfer: ")
            jumlah_transfer = int(input())
            if jumlah_transfer <= saldo:
                saldo -= jumlah_transfer
                print("Jumlah uang yang telah Anda transfer ke rekening tujuan adalah:", jumlah_transfer)
            else:
                print("Jumlah uang yang ingin Anda transfer melebihi saldo Anda.")
        elif pilihan == 5:
            # Keluar
            print("Terima kasih telah menggunakan ATM kami.")
            sys.exit()
        else:
            print("masukan pilihan yang bener kaks")

        lanjut = input("Ingin melakukan transaksi lagi (y/n)? ").lower()
        if lanjut != "y":
            print("Terima kasih telah berkunjung ke ATM kami")
            sys.exit()



while True:
    i+=1
    masukan = int(input("masukan pin anda : "))
    if masukan == pin:
        print("login berhasil....")
        main()
    else:
        if i == limit:
            print("Anda di blokir")
            break
        else:
            print(f"pin anda salah tersisa {limit - i} kesempatan")