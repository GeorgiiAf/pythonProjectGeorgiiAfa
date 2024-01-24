import math
def pizzan_hinta(d, h):
    S = (math.pi * d ** 2 / 4) / 10000  # koska neliömetri
    h_m = h / S              # hinta/pinta-ala neliömetri
    return h_m
d = float(input('Kirjoita halkaisija sm : '))
h = float(input('Kirjoita  hinta eur : '))
h_m1 = pizzan_hinta(d, h)
d = float(input('Kirjoita halkaisija sm : '))
h = float(input('Kirjoita  hinta eur : '))
h_m2 = pizzan_hinta(d, h)
if h_m1 > h_m2:
    print(f'Pizza 2 on parempi , hinta {h_m2}')
elif h_m1 == h_m2:
    print('Pizzat ovat samanlaisia')
else:
    print(f'Pizza 1 on parempi , hinta {h_m1}')
