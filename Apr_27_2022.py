#!/usr/bin/python3

class Kardus:
    def __init__(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
    
    def volumeKardus(self):
        return self.panjang * self.lebar * self.tinggi
    
    def luasPermukaanKardus(self):
        return 2 * (self.panjang * self.lebar + self.panjang * self.tinggi + self.tinggi * self.lebar)
    
    def massaJenis(self, massa):
        return massa / self.volumeKardus()

if __name__ == "__main__":
    KotakBiru = Kardus(10, 8, 4)
    print("Volume: {}, luas permukaan: {}, massa jenis: {}".format(KotakBiru.volumeKardus(), KotakBiru.luasPermukaanKardus(), KotakBiru.massaJenis(100)))

    KotakMerah = Kardus(15, 5, 1)
    print("Volume: {}, luas permukaan: {}, massa jenis: {}".format(KotakMerah.volumeKardus(), KotakMerah.luasPermukaanKardus(), KotakMerah.massaJenis(100)))
