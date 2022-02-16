#!/usr/bin/python3

"""
SOAL
 Program di bawah ini adalah program untuk LOG IN ke dalam akun email dengan
rincian sebagai berikut:
- Program meminta user memasukkan username berupa NIM masing-masing
praktikan
- Program meminta user memasukkan password yakni abc1234
- Tuliskan pesan LOG IN BERHASIL lalu program selesai jika username dan
password benar dan jika salah satu salah akan menampilkan GAGAL, COBA
LAGI
- Jika user salah dalam memasukkan baik username maupun password, sistem akan
looping meminta user memasukkan identitas yang benar kecuali user memilih
pilihan NO untuk membatalkan proses LOG IN. 
"""

while True:
    print('**** LOG IN ****')
    usr_name = str(input('Username : '))
    pwd = str(input('Password : '))
    print('****************')

    if (usr_name == '483339' and pwd == 'abc1234'):
        print('LOG IN BERHASIL')
        print('SELAMAT BERAKTIVITAS')
        break
    else:
        print('GAGAL, COBA LAGI')
        retry = str(input('Apakah anda ingin mencoba lagi? (Y/N) : '))
        if retry.upper() == 'N':
            break