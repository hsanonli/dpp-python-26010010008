# masukan panjang dan lebar persegi panjang
panjang = float(input("Masukkan panjang persegi panjang (m): "))
lebar = float(input("Masukkan lebar persegi panjang (m): "))

# menghitung luas 
luas = panjang * lebar
print(f"Luas persegi panjang adalah: {luas}m²")

# menghitung keliling
keliling = 2*(panjang + lebar)
print(f"Keliling persegi panjang adalah: {keliling}m")

#                                   trace tabel 
# =======================================================================================
# | Baris | panjang | lebar | luas | keliling | Output                                  |
# |-------|---------|-------|------|----------|-----------------------------------------|
# | 2     | 9.0     |       |      |          |                                         |
# | 3     | 9.0     | 6.0   |      |          |                                         |
# | 5     | 9.0     | 6.0   | 54.0 |          |                                         |
# | 6     | 9.0     | 6.0   | 54.0 |          | Luas persegi panjang adalah: 54.0m²     |
# | 8     | 9.0     | 6.0   | 54.0 | 30.0     |                                         |
# | 9     | 9.0     | 6.0   | 54.0 | 30.0     | Keliling persegi panjang adalah: 30.0m  |
# =======================================================================================