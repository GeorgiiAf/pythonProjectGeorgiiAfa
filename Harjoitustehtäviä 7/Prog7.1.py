vuodenajat = ('talvi', 'kevät', 'kesä', 'syksy')


try:
    kk = int(input("Syötä kuukauden numero (1-12): "))
    if 1 <= kk <= 12:  # kk - kuukausi
        vuodenaika_index = (kk % 12) // 3
        vastaava_vuodenaika = vuodenajat[vuodenaika_index]
        print(f"Kuukausi {kk} vastaa vuodenaikaa {vastaava_vuodenaika}.")
    else:
        print("Virheellinen kuukauden numero. Syötä numero väliltä 1-12.")
except ValueError:
        print("Virheellinen syöte. Syötä kelvollinen kuukauden numero kokonaislukuna.")





"""  väärä versio 
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
    print('Virheellinen kuukauden numero. Syötä luku 1-12')"""
