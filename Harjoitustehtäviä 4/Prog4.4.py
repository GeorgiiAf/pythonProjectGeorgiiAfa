import random
x = random.randint(1,10)
print('Kirjoita kokonaisluku väliltä 1..10. ')
while True:
    try:
        y=int(input())
        if y>x:
            print('Liian suuri arvaus')
        elif y<x:
            print('Liian pieni arvaus')
        else:
            print('Oikein')
    except ValueError:(
        print('väärä syöte, käynnistä ohjelma ja kirjoita luku ehdon mukaan '))