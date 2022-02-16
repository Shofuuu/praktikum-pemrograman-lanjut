#!/usr/bin/python3

"""
SOAL
Program untuk menampilkan segitiga bintang dengan masukan berupa jumlah baris
"""

rows = int(input("Masukkan jumlah baris: "))

for x in range(int(rows/2)):
    print("*" * (x+1))
for y in range(int(rows/2)-1, -1, -1):
    print("*" * (y+1))