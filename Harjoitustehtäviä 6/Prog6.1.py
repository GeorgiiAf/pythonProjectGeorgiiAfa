import random


def heitto():
    a = 6
    x=0
    while a != x:
        x = random.randint(1, 6)
        print(f"Heitto {x}")
    else:
        print('kuutonen on')
    return
heitto()
