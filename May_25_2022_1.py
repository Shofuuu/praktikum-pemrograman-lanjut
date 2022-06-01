#!/usr/bin/python3

class Siswa:
    __mapel = []
    __nilai = []

    def __init__(self, nama, alamat):
        self.nama = nama
        self.alamat = alamat
    
    def getNama(self):
        return self.nama
    
    def tambahNilaiMapel(self, mapel, nilai):
        self.__mapel.append(mapel)
        self.__nilai.append(nilai)
    
    def ambilNilai(self):
        print(self.__nilai)
        print(self.__mapel)

s = Siswa("Shofuwan", "Jogjakarta")
print(s.nama)
print(s.alamat)
s.tambahNilaiMapel("Matematika", 90)
s.tambahNilaiMapel("Fisika", 80)
print(s.getNama())
s.ambilNilai()