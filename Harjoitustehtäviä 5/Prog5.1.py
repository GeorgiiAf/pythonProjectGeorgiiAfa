import random
print('Kirjoita arpakuutoiden lukumäärä (kokonaisluku):\t', end='')
lkm=int(input())
S=0                 #summa
for i in range(lkm):
    result=random.randint(1,6)
    print(f'heitto: {result}')
    S+=result
print(f'Silmälukujen summa: {S}')