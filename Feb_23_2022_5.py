#!/usr/bin/python3

"""
SOAL
Buatlah program untuk menentukan hasil dari ujian sebuah mata kuliah! (SCORE :
10)
Nilai Akhir (NA) = 70% Nilai UAS + 30% Nilai UTS
Aturan Nilai Indeks :
● Jika NA ≥ 80 , maka “Lulus”
● Jika 80 > NA ≥ 70, maka “Lulus dengan pertimbangan”
● Jika 70 > NA ≥ 55, maka “Lulus dengan tugas”
● Jika 55 > NA ≥ 40, maka “Mengulang”
● Jika NA < 40, maka “Gagal”
Input : Nilai UAS dan Nilai UTS
Output : “Lulus” / “Lulus dengan pertimbangan” / “Lulus dengan tugas” /“Mengulang”
/ “Gagal” 
"""

# variable to save the message
msg = ''

# input the score
uas = int(input('Masukkan nilai UAS: '))
uts = int(input('Masukkan nilai UTS: '))

if uas >= 80 and uts >= 80:
    msg = 'Lulus'
elif 80 > uas >= 70 and uts >= 70:
    msg = 'Lulus dengan pertimbangan'
elif 70 > uas >= 55 and uts >= 55:
    msg = 'Lulus dengan tugas'
elif 55 > uas >= 40 and uts >= 40:
    msg = 'Mengulang'
else:
    msg = 'Gagal'

print(msg)