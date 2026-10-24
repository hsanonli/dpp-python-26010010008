# variabel untuk menyimpan nama barang, harga barang, dan jumlah barang
namabarang = input("Masukkan nama barang: ")
hargabarang = float(input("Masukkan harga barang: "))
jumlahbarang = int(input("Masukkan jumlah barang: "))

# masukan data barang dan harga barang
print(f"Nama Barang : {namabarang}")
print(f"Harga Barang : Rp {hargabarang:,.2f}")

# menghitung total belanja
totalbelanja = hargabarang * jumlahbarang
print(f"Total Belanja : Rp {totalbelanja:,.2f}")

# menghitung pajak dan total bayar
pajak = totalbelanja * 0.11
print(f"Pajak : Rp {pajak:,.2f}")

totalbayar = totalbelanja + pajak
print(f"Total Bayar : Rp {totalbayar:,.2f}")