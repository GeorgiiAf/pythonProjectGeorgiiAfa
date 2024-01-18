print('Kirjoita sukupuoli')
a=str(input())
if a=='nainen' or a=='Nainen' or a=='NAINEN':
    print('Kirjoita hemoglobiiniarvo g/l. ')
    b=float(input())
    if b>=117 and b<=175:
        print('hemoglobiiniarvo on normaali')
    elif b<117:
        print('hemoglobiiniarvo on alhainen ')
    elif b>175:
        print('hemoglobiiniarvo on korkea')
elif a=='mies' or a=='MIES' or a=='Mies':
    print('Kirjoita hemoglobiiniarvo g/l. ')
    b=float(input())
    if b>=134 and b<=195:
        print('hemoglobiiniarvo on normaali')
    elif b<134:
        print('hemoglobiiniarvo on alhainen ')
    elif b>195:
        print('hemoglobiiniarvo on korkea')


