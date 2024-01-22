Nimet=[]
print('Kirjoita kaupungien nimet :\t', end='')
for i in range(5):
    Nimet.append(str(input()))
print('kirjoita mitä tahansa merkki tai paina enter ')
x=input()
for kaupunki in Nimet:
    print(f'Kaupungin nimi {kaupunki} ')


