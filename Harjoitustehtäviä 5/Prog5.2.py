numerot = []  # kaikki numerot ovat tässä
while True:
    syöte_numero = input("Syötä luku (tyhjä rivi lopettaa): ")
    if syöte_numero == '':
        break
    if syöte_numero.isdigit() or (syöte_numero[0]=='' and syöte_numero[1:].isdigit()):
        # Muutetaan syöte luvuksi ja lisätään listaan
        luku = float(syöte_numero)
        numerot.append(luku)
    else:
        print("Virheellinen syöte, syötä luku.")
if numerot:
    sorted_numerot =sorted(numerot , reverse=True)[:5]
    print('\nViisi suurinta lukua suuruusjärjestyksessä:')
    i = 1
    for luku in sorted_numerot:
        print(f"  {i}, {luku}   ")
        i+=1
else:
    print("Et syöttänyt yhtään lukua.")
