#!/usr/bin/python3

"""
SOAL
Buatlah program untuk mengubah nilai detik ke dalam jam. Nilai Jam, Menit, dan Detik
hasil konversi harus bertipe bilangan bulat. Ujilah program anda dengan 3 masukan
berikut dan program anda benar jika memberikan hasil yang sama.
Jumlah Detik Jam, Menit, Detik
3600 1 jam 0 menit 0 detik
400 0 jam 6 menit 40 detik
88888 24 jam 41 menit 28 detik 
"""

jumlah_detik = int(input('Masukkan jumlah detik: '))

# mengubah detik ke jam, menit, detik
print(jumlah_detik // 3600, 'jam', (jumlah_detik % 3600) // 60, 'menit', (jumlah_detik % 3600) % 60, 'detik')