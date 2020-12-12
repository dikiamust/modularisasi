# MENGHITUNG LUAS SEGITIGA

alas = 20
tinggi = 10
luas_segitiga = alas * tinggi * 1 / 2
print( f' sebuah segitiga dengan alas {alas} & tinngi {tinggi} maka luasnya = {luas_segitiga}' )


# JIKA KITA PUNYA DATA YANG BERBEDA BISA DENGAN SINTAKS

def luas_segitiga(alas, tinggi):
    luas_segitiga = alas * tinggi / 2
    return luas_segitiga


print( luas_segitiga( 4, 2 ) )
print( luas_segitiga( 6, 2 ) )


