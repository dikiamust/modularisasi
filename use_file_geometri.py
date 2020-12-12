# MENGGUNAKAN FUNGSI PADA FILE GEOMETRI
from geometri.segitiga import luas_segitiga

luas_segitiga
print(luas_segitiga(10, 6))

# ATAU MENAMBAHKAN SUATU FUNGSI DENGAN CARA MANUAL

import geometri.segitiga as a

print(a.luas_segitiga(8,4))
print(f' luas segitiga dengan alas 10cm dan tinggi 6cm maka luasnya = {a.luas_segitiga(8,4)}cm*2')

#LUAS SEGIEMPAT YANG FUNGSINYA SUDAH DISIMPAN DIFILE GEOMETRI
print(a.luas_segiempat(10,5))
print(f' luas segiempat dengan panjang 10cm dan lebar 5cm maka luasnya = {a.luas_segiempat(10,5)}cm*2')

#CARA MENGEMBALIKAN STRING
from geometri.tambahan import luas_segi, info
print(info ())

from geometri.segitiga import luas_segiempat, info
print(info ())