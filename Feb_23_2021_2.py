#!/usr/bin/python3

"""
SOAL
Buatlah sebuah program yang meminta user menebak sebuah angka yang digenerate
terlebih dahulu oleh random number generator. Kesempatan yang diberikan adalah 3
kali. Angka ini berada pada rentang 5-8. Jika ada salah satu dari tebakan tersebut
benar, maka program akan berhenti dan menyampaikan pesan bahwa tebakan tepat.
Untuk anda sudah diupload sebuah file program python yang menjadi tempat anda
mengerjakan tugas nomor ini, bernama Tugas2.py. Anda hanya boleh menambahkan
program pada area yang sudah disiapkan dalam program dan tidak boleh mengubah
atau menghapus program yang sudah ada. Gunakanlah variabel bernama tebak1, tebak2
dan tebak3 untuk menampung 3 kesempatan tebakan user. 
"""

import random

print('Tebak angka dari 5-8:')
for retry in range(3):
    rand_number = random.randint(5, 8)

    guessed_number = int(input('Masukkan tebakan: '))
    if guessed_number == rand_number:
        print('Tebakan tepat!')
        break
    else:
        print('Tebakan salah!')
        print('yang benar adalah', rand_number)
        print('Tebakan ke-', retry + 1)

print('Tebakan sudah habis!')