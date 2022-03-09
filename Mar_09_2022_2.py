#!/usr/bin/python3

"""
    SOAL
    Misalkan ada 3 variabel yang diukur dari sebuah kelas di sebuah departemen di sekolah
    vokasi. Variable - variable tersebut, secara terurut, adalah Jumlah Mahasiswa, Jumlah
    Mahasiswi, dan Jumlah Total. Misalkan ada 3 kelas dalam satu angkatan yang
    informasinya akan disimpan dalam 1 variabel array. Buatlah program yang dapat
    melakukan hal tersebut. Program harus memiliki kemampuan untuk menerima masukan
    lalu menampilkan seluruh isi dari array tersebut.
"""

kelas = []

for x in range(3):
    in_mahasiswa, in_mahasiswi = input("Masukkan Jumlah Mahasiswa dan Jumlah Mahasiswi: ").split()
    combine_kelas = [int(in_mahasiswa), int(in_mahasiswi), int(in_mahasiswa)+int(in_mahasiswi)]
    kelas.append(combine_kelas)

print('Kelas:', kelas, end='\n\n')