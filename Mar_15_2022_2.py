#!/usr/bin/python3

"""
    SOAL
    terdapat 3 buah gedung dengan 15 lantai
    dan terdiri dari 20 kamar. Input berupa
    pilihan gedung, lantai, dan nomor kamar

    - Kamar tengah (8,9,10,11,12) president suite 1jt/malam
    - Lantai 14 superior suite 850k/malam
    - Deluxe Suite ujung 2 kamar ujung kanan dan kiri 700k/malam
    - Selain 3 diatas seharga 500k/malam
"""

hotel = []
building = []

def render_hotel():
    for x in range(3):
        print('══'*9, end='')
        print(' ', chr(ord('A')+x),' ', end='')
        print('═'*17, end=' ')
    print()

    for z in range(3):
        for y in range(300):
            print('│', '▓' if hotel[z][y] == 1 else '░', '\n' if y%30 == 29 else ' ', end='', sep='')

    for x in range(3):
        print('══'*20, end=' ')
    print()

if __name__ == '__main__':
    for z in range(3):
        for y in range(300):
            building.append(0)
        hotel.append(building)

    msg = ['Selamat Datang', '[contoh] booking gedung A lantai 15 kamar 8 -> A 15 8']

    while True:
        render_hotel()

        print('\n', '  '*(30-int(len(msg[0])/3)), msg[0], sep='')
        print('  '*(30-int(len(msg[1])/4)), msg[1], sep='')

        gedung, lantai, kamar = input((' '*34)+'[gedung, lantai, kamar] ').split()
        gedung = gedung.upper()
        lantai = int(lantai)
        kamar = int(kamar)

        # hotel[ord(gedung)-65][(lantai-1)*(kamar*10)] = 1