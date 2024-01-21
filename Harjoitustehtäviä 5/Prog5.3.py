print('Kirjoita arpakuutoiden kokonaisluku :\t', end='')
l=int(input())
i=0
for i in range(l):
    if l % i <> 0:
        i+=1
    print(f'heitto: {result}')
    S+=result
print(f'Silmälukujen summa: {S}')
