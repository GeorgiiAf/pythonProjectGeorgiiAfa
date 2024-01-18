print('Kirjoita kuhan pituuden senttimetreinä')
a=int(input())
if a<37:
    print('alimmasta sallitusta pyyntimitasta puuttuu ', 37-a ,' cm')
elif a>=37:
    print('kaikki on OK')