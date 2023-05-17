import sys

print("\t\t\t===================")
print("\t\t\t Nobara Sport Shop")
print("\t\t\t===================")
print("Diskon 50% Jika Pembelian lebih Dari Rp. 400.000")
print("Diskon 70% Jika Pembelian Lebih Dari Rp. 800.000")
print("\n Daftar Baju yang Tersedia\n")

print(f'{"No.":8}{"Nama Baju":35}{"Harga":30}')
print(f'{"1.":8}{"Jersey Man. United":35}{"Rp. 300.000":30}')
print(f'{"2.":8}{"Jersey Man. City":35}{"Rp. 250.000":30}')
print(f'{"3.":8}{"Jersey Chelsea":35}{"Rp. 550.000":30}')
print(f'{"4.":8}{"Jersey Persib":35}{"Rp. 750.000":30}')
print()


while True:
    pilih = int(input("Silakan Mau Pilih yang Mana (1-4) : "))
    jumlah = int(input("Jumlah Baju yang Ingin Dibeli : "))

    if int(pilih) == 1:
        namaBaju = "Jersey Man. United"
        hargaBaju = 300000
    elif pilih == 2:
        namaBaju = "Jersey Man. City"
        hargaBaju = 250000
    elif pilih == 3:
        namaBaju = "Jersey Chelsea"
        hargaBaju = 550000
    elif pilih == 4:
        namaBaju = "Jersey Chelsea"
        hargaBaju = 750000
    else :
        print("Angka yang Anda Masukkan Salah!!")
    stop = str.lower(input("Apakah mau ubah pesanan(y/n)? "))
    if stop == "n":
        break

totalHarga = hargaBaju * jumlah

if totalHarga >= 400000:
        diskon = totalHarga * 40/100
elif totalHarga >= 800000:
        diskon = totalHarga * 70/100
else:
        diskon = 0

totalBayar = totalHarga - diskon

print("="*70)
print(f'{"Nama Baju":30}{"Jumlah":20}{"Total Harga":20}')
print(f'{namaBaju:.30}{jumlah:20}{totalBayar:25}')
print("="*70)

print("\nTotal Tagihan yang Harus Anda Bayar : Rp. ", totalBayar)
print(f"{'Terima Kasih Sudah Berkunjung':^70}")
    


    