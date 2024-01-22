print('Kirjoita kokonaisluku :\t', end='')
N = int(input())
if N == 1 or N == 0:
    print('Se ei ole alkuluku')
else:
    alkuluku = True
    for i in range(2, int(N ** 0.5) + 1):
        if N % i == 0:
            alkuluku = False
            break
    if alkuluku:
        print(f'{N} on alkuluku')
    else:
        print(f'{N} ei ole alkuluku')
