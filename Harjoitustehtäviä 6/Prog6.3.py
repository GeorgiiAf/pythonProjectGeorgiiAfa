def gallona_litra(gm):
    return gm * 3.785
while True:
    gm = float(input('Kirjoita bensiinin määrä nestegallonoina:\t '))
    if gm >= 0:
        nm = gallona_litra(gm)
        print(f'\033[33mBensiinin määrä {nm:.3f} litraa\033[0m')   # tämä rivi on keltainen :)
    else:
        break
print('Syötit negatiivisen gallonamäärän')
