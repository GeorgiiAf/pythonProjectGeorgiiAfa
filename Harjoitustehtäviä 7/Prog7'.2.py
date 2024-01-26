nimet = set()
while True:
    name = input('Kirjoita nimi , tyhjä rivi lopettaa  : ')
    if not name:
        break
    if name in nimet:
        print('Aiemmin syötetty nimi ')
    else:
        nimet.add(name)
        print('Uusi nimi ')
print('Kirjoitit seuraavat nimet : ')
for name in nimet:
    print(name)
