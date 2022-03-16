#!/usr/bin/python3

"""
    SOAL
    terdapat 3 buah gedung dengan 15 lantai
    dan terdiri dari 20 kamar. Input berupa
    pilihan gedung, lantai, dan nomor kamar

    - Kamar tengah paling atas (8,9,10,11,12) president suite 1jt/malam
    - Lantai 14 superior suite 850k/malam
    - Deluxe Suite ujung 2 kamar ujung kanan dan kiri 700k/malam
    - Selain 3 diatas seharga 500k/malam
"""

hotel = []
building = []
suite_type = {1 : 'President Suite', 0.7 : 'Deluxe Suite', 0.85 : 'Superior Suite', 0.5 : 'standard Suite'}

for _building in range(3):
    for _floor in range(15):
        for _room in range(20):
            building.append(0)
    hotel.append(building)
    building = []

while True:
    usr_hotel, usr_floor, usr_room = map(int, input("[gedung] [lantai] [kamar] > ").split())

    usr_hotel = (0 if usr_hotel < 1 else usr_hotel-1)
    usr_floor = (0 if usr_floor < 1 else usr_floor-1)
    usr_room = (0 if usr_room < 1 else usr_room-1)
    side_room = (usr_room%20 == 0 or usr_room%20 == 20) or (usr_room%21 == 0 or usr_room%21 == 21) or (usr_room%18 == 0 or usr_room%18 == 18) or (usr_room%19 == 0 or usr_room%19 == 19)

    total_bill = 1 - (
        0 if usr_floor == 14 and usr_room in [7, 8, 9, 10, 11] else (
            0.15 if usr_floor == 13 and not side_room else (
                0.3 if side_room and (usr_floor == 14 or usr_floor == 13) else 0.5
            )
        )
    )

    hotel[usr_hotel][(299 - ((usr_floor * 20) + usr_room))] = 1

    print('\n\t', '='*6, 'Hotel ', usr_hotel+1, '='*7, '\n\t', end='', sep='')
    for x in range(300):
        print('#' if hotel[usr_hotel][x] != 1 else '+', end='')
        if x%20 == 19 and x != 299: print('\n\t', end='', sep='')
    print('\n\t', '='*6, 'Hotel ', usr_hotel+1, '='*7, '\n\t', end='', sep='')

    print('\n\t', 'Anda memilih kamar ', suite_type[total_bill], '\n\tdengan harga Rp.', '{:,}'.format(total_bill*1000000), '\r\n\n', end='', sep='')