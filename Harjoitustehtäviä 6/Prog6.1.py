import random
def heitto():
    return random.randint(1,6)
sl=0
i=0
while sl != 6:
    sl = heitto()    # silmäluku
    i+=1 # heittojen määrä
    print(f'Heitto {i}  :  {sl}')
print(f'Kuutonen saatiin heitolla {sl} . ')
