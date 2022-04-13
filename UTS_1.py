#!/usr/bin/python3
# UTS April 6 2022
# Muhammad Shofuwan Anwar (21/483339/SV/20142)

table_info = ('No', 'Karakter', 'Tipe', 'Biner', 'Hexa')
usr_data = input('str = ')

if len(usr_data) > 0:
    print('+','-'*48,'+', sep='')
    print('|{:<3}|{:<10}|{:<10}|{:<11}|{:<10}|'.format(*table_info))
    print('+','-'*48,'+', sep='')

    for i in range(len(usr_data)):
        print('|{:<3}|{:<10}|{:<10}|{:<11}|{:<10}|'.format(i+1, usr_data[i], type(usr_data[i]).__name__, bin(ord(usr_data[i])), hex(ord(usr_data[i]))))
    print('+','-'*48,'+', sep='')
else:
    print('Tidak ada data')