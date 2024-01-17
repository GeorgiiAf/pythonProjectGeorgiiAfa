import random
print('kolmenumeroinen koodi: ')
for i in range(3):
    print(random.randint(0,9), end='')
print()
print('nelinumeroinen koodi: ')
for j in range(4):
    print(random.randint(1, 6), end='')
