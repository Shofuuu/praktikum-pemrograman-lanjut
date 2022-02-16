#!/usr/bin/python3

"""
SOAL
Buatlah sebuah program untuk menampilkan secara terbalik (reversed) kembali
karakter demi karakter tulisan: “Sekolah Vokasi UGM” yang bertipe data strings
dengan menggunakan FOR/WHILE.
"""

msg = "Sekolah Vokasi UGM"

for x in range(len(msg)):
    print(msg[len(msg)-x-1], end="")
print()