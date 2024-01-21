import random
x = random.randint(1, 10)
print('Kirjoita kokonaisluku väliltä 1..10 :\t')
arvaukset=0
while True:
    y = int(input())
    arvaukset+=1
    if y > 10 or y < 1:
        print('Väärä syöte, kirjoita luku ehdon mukaan ')
    elif y > x:
        print('Liian suuri arvaus ')
    elif y < x:
        print('Liian pieni arvaus ')
    else:
        print(f'Oikein! , sait sen okein {arvaukset} kerralla')
        break
