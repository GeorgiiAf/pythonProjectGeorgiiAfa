import math
def pizzan_hinta(d, h):
    S = (math.pi * d ** 2 / 4) / 10000  # koska neliömetri
    h_m = h / S              # hinta/pinta-ala neliömetri
    return h_m
d = float(input('Kirjoita pizzan halkaisija senttimetreinä : '))
h = float(input('Kirjoita  pizzan hinta eur : '))
h_m1 = pizzan_hinta(d, h)
d = float(input('Kirjoita pizzan halkaisija senttimetreinä : '))
h = float(input('Kirjoita  pizzan hinta eur : '))
h_m2 = pizzan_hinta(d, h)
if h_m1 > h_m2:
    print(f'Pizza 2 on parempi , sen yksikköhinta {h_m2} , pizzan 1 yksikköhinta {h_m1}')
elif h_m1 == h_m2:
    print('Pizzojen hinta/pinta-ala arvot ovat samanlaisia')
else:
    print(f'Pizza 1 on parempi , sen yksikköhinta {h_m1}, pizzan 2 yksikköhinta {h_m2}')
