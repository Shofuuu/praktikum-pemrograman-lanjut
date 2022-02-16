#!/usr/bin/python3

"""
SOAL
Jika anda diberi tiga buah lidi dengan masing - masing memiliki panjang tertentu, maka
tentukanlah apakah mereka bisa membentuk sebuah segitiga atau tidak. Cara yang 
paling sederhana adalah dengan menggunakan aturan bahwa sebuah segitiga hanya
dapat terbentuk dari 3 buah sisi dengan ketentuan tidak ada salah satu sisi yang
panjangnya melebihi jumlah dari kedua sisi lainnya. Buatlah program yang
menerima masukan dari user berupa panjang masing - masing sisi (3 buah sisi) dan
menampilkan YA jika kombinasinya dapat membentuk sebuah segitiga, dan TIDAK
jika sebaliknya. 
"""

# input 3 vertex length in different variable
a = int(input('Masukkan panjang sisi a: '))
b = int(input('Masukkan panjang sisi b: '))
c = int(input('Masukkan panjang sisi c: '))

# check if it is a triangle
if a + b > c and a + c > b and b + c > a:
    print('Ya, segitiga tersebut dapat terbentuk')
else:
    print('Tidak, segitiga tersebut tidak dapat terbentuk')
