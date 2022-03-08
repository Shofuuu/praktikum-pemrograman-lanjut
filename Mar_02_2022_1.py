#!/usr/bin/python3

"""
SOAL
Program untuk menampilkan segitiga bintang dengan masukan berupa jumlah baris
"""

rows = int(input("Masukkan jumlah baris: "))

for x in range(rows):
        print("*" * ((x+1) if x <= (rows/2)-1 else ((rows-x))))