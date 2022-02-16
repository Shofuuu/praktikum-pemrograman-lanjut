#!/usr/bin/python3

"""
SOAL
Buatlah sebuah program untuk menjumlahkan dua buah matriks berbeda (A dan B)
berukuran 2 x 2 dengan terlebih dahulu memasukkan elemen – elemen dari matriks –
matriks tersebut. Ikutilah aturan penjumlahan matriks yang berlaku umum.
"""

matrix_a = [[],[]]
matrix_b = [[],[]]
matrix_result = [[],[]]

print('Masukkan elemen matriks A:')
for i in range(2):
    for j in range(2):
        matrix_a[i].append(int(input('A[{},{}] : '.format(j, i))))

print('Masuukkan elemen matriks B:')
for i in range(2):
    for j in range(2):
        matrix_b[i].append(int(input('B[{},{}] : '.format(j, i))))

# summing the matrix
for i in range(2):
    for j in range(2):
        matrix_result[i].append(matrix_a[i][j] + matrix_b[i][j])

# showing the result
print('Hasil penjumlahan matriks A dan B:')
for i in range(2):
    for j in range(2):
        print('{} '.format(matrix_result[i][j]), end='')
    print()