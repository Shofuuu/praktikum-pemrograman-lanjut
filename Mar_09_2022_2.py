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

print('Opsi :\n\t1. Tambah Data\n\t2. Tampilkan Data [0:mahasiswa, 1:mahasiswi, 2:total]\n\t3. Keluar')
print('Example : \n\tMemilih tambah data pada kelas ke-1 dengan mahasiswa 15, mahasiswi 18\n\t> 1 15:18')
print('\tMenampilkan data kelas ke-0 khusus mahasiswi\n\t> 2 0:1')
print('\tKeluar\n\t> 3 x')

while True:
    try:
        opsi, val = input("[opsi][value] > ").split()
        
        if int(opsi) == 1:
            combine_kelas = val.split(':')
            combine_kelas.append(int(combine_kelas[0])+int(combine_kelas[1]))
            kelas.append(combine_kelas)
        elif int(opsi) == 2:
            tipe_data = ['mahasiswa', 'mahasiswi', 'total']
            index = val.split(':')
            print('kelas-', index[0], ', ', tipe_data[int(index[1])], ' : ', kelas[int(index[0])][int(index[1])], sep='')
        elif int(opsi) == 3:
            print('--selesai--')
            break
    except:
        print('--Error--', end='\n\n')