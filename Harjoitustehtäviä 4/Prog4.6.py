import random
print('Kirjoita pisteiden määrä (kokonaisluku): \t', end='')
N=int(input())
n=0  # pisteiden määrä jäävien ympyrän sisälle
for i in range(N):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    if x**2 + y**2 <= 1:
        n+=1
pi= 4 * n/N         # mitä enemmän pisteitä,sitä tarkempi arvo
print(f'Piin likiarvo: {pi} ')