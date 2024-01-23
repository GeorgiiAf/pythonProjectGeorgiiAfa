import random
def heitto(tm):
    return random.randint(1,tm) # tm - tahkojen määrä
sl=0
hm=0      # hm - heittojen määrä
ml=int(input('Kirjoita maksimiluku: '))
tm=int(input('Kirjoita tahkojen määrä:   '))
while sl != ml:
    sl = heitto(tm)    # silmäluku
    hm+=1 # heittojen määrä
    print(f'Heitto {hm}  :  {sl}')
print(f'Maksimiluku {ml} saavutettu heitolla {hm}. ')
