# masukan angkau suhu
angka = input("Masukkan suhu dalam Celcius: ")

# mengubah suhu dari celcius ke fahrenheit 
fahrenheit =  float(angka)*(9/5) + 32
print(f"Suhu dalam Fahrenheit adalah: {fahrenheit} °F")

# mengubah suhu dari celcius ke kelvin
kelvin = float(angka) + 273.15
print(f"Suhu dalam Kelvin adalah: {kelvin} K")