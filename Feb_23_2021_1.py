#!/usr/bin/python3

"""
SOAL
Buatlah program menggunakan pencabangan IF untuk mengubah suhu/temperature
dari dan ke untuk Celcius dan Fahrenheit. Untuk memudahkan anda, gunakanlah angka
sebagai penanda pilihan seperti 1-Fahrenheit dan 2-Celcius. Penggunaan
string/character untuk logika pencabangan akan diajarkan pada modul perulangan.
Masukannya berasal dari user saat program dijalankan. Jangan lupa menampilkan
satuan yang benar untuk hasilnya. Tampilkan pesan error jika ada pilihan konversi suhu
bukan antara angka 1 atau 2 dan gunakan pembulatan agar suhu hasil konversi
berbilangan bulat.
Note: Anda boleh browsing rumus konversi suhu dari dan ke untuk kedua ukuran
temperature tersebut. 
"""

# reading input from user
print('Pilih konversi suhu:')
print('1. Celcius ke Fahrenheit')
print('2. Fahrenheit ke Celcius')
user_select = int(input('Pilih nomor: '))

if user_select == 1:
    celsius = float(input('Masukkan suhu dalam Celcius: '))
    fahrenheit = (celsius * 1.8) + 32
    print(int(fahrenheit), 'Fahrenheit')
elif user_select == 2:
    fahrenheit = float(input('Masukkan suhu dalam Fahrenheit: '))
    celsius = (fahrenheit - 32) / 1.8
    print(int(celsius), 'Celcius')
else:
    print('Error: Pilihan tidak valid')
