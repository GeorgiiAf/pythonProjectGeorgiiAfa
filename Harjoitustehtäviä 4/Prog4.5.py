kt='python'
sa='rules'
i = 1
while i<=5:
    print('Kirjoita käyttäjätunnuksesi :\t' ,end='')
    a = str(input())
    i = i+1
    print('Kirjoita salasanasi :\t', end='')
    b = str(input())
    if kt==a and sa==b:
        print('Tervetuloa!')
        break
    else:
        print("käyttäjätunnus tai salasana on väärä")
else:print("Pääsy evätty")
