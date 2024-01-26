kk_vuodenajat = {
    1: 'talvi',
    2: 'talvi',
    3: 'talvi',
    4: 'kevät',
    5: 'kevät',
    6: 'kevät',
    7: 'kesä',
    8: 'kesä',
    9: 'kesä',
    10: 'syksy',
    11: 'syksy',
    12: 'syksy'}

kk = int(input('Kirjoita kuukauden numero : '))
if 1<= kk <=12:
    vuodenaika = kk_vuodenajat[kk]
    print(f'Kuukausi {kk} on vuodenaika : {vuodenaika}')
else:
    print('Virheellinen kuukauden numero. Syötä luku 1-12')
