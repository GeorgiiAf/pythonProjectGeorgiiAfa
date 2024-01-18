print('Kirjoita laivan hyttiluokan (LUX, A, B, C)')
r=str(input())
if r=='LUX' or r=='Lux' or r=='lux':
    print('LUX on parvekkeellinen hytti yläkannella.')
elif r=='A' or r=='a':
    print('A on ikkunallinen hytti autokannen yläpuolella.')
elif r=='b' or r=='B':
    print('B on ikkunaton hytti autokannen yläpuolella.')
elif r=='c' or r=='C':
    print('C on ikkunaton hytti autokannen alapuolella.')
else:
    print('Virheellinen hyttiluokka ')