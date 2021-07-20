'''

Script de python que crea una simple animación por consola en base a la manipulación de strings con el método zfill().

'''

from time import sleep



d0 = '0000000000000000000000000000'
d1 = '0000000000110000110000000000'
d2 = '0000000000110000110000000000'
d3 = '0000000000000000000000000000'
d4 = '0000001100000000000011000000'
d5 = '0000000110000000000110000000'
d6 = '0000000011000000001100000000'
d7 = '0000000000111111110000000000'
d8 = '0000000000000000000000000000'

i = 1
while i < 30:
    i += 1
    d0 = d0[:-1]
    d0 = d0.zfill(29)
    d1 = d1[:-1]
    d1 = d1.zfill(29)
    d2 = d2[:-1]
    d2 = d2.zfill(29)
    d3 = d3[:-1]
    d3 = d3.zfill(29)
    d4 = d4[:-1]
    d4 = d4.zfill(29)
    d5 = d5[:-1]
    d5 = d5.zfill(29)
    d6 = d6[:-1]
    d6 = d6.zfill(29)
    d7 = d7[:-1]
    d7 = d7.zfill(29)
    d8 = d8[:-1]
    d8 = d8.zfill(29)
    
    sleep(0.08)
    
    print(d0)
    print(d1)
    print(d2)
    print(d3)
    print(d4)
    print(d5)
    print(d6)
    print(d7)
    print(d8)
    print(' ')
    
    
