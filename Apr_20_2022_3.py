#!/usr/bin/python3

data = "Sekolah Vokasi ugM, Yogyakarta"
data_converted = [data.split(','), data.lower().capitalize(), data.title(), data.upper().replace(' ', '*')]
for x in data_converted:
    print(x)