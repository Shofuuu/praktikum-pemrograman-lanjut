#!/usr/bin/python3

class Satu:
    var = 'Satu'
    varSatu = 'SatuSatu'

    def coba(self):
        return 'SATU'

class Dua:
    var = 'Dua'
    varDua = 'DuaDua'

    def coba(self):
        return 'DUA'

class Sub(Dua, Satu):
    pass

obj = Sub()
print(obj.var, obj.varSatu, obj.varDua, obj.coba())