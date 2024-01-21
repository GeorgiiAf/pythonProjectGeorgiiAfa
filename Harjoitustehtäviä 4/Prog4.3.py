numerot = [] # kaikki numerot ovat tässä
while True:
    syöte_numero = input("Syötä luku (tyhjä rivi lopettaa): ")
    if syöte_numero == '':
        break
    if syöte_numero.lstrip('-').replace('.','',1).isdigit():
        # Muutetaan syöte luvuksi ja lisätään listaan
        luku = float(syöte_numero)
        numerot.append(luku)
    else:
        print("Virheellinen syöte, syötä luku.")
if numerot:
    pienin = min(numerot)
    suurin = max(numerot)
    print(f"Pienin luku: {pienin}")
    print(f"Suurin luku: {suurin}")
else:
    print("Et syöttänyt yhtään lukua.")