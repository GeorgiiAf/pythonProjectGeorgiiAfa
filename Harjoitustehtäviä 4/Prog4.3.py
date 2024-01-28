numerot = []  # kaikki numerot ovat tässä
while True:
    syote_numero = input("Syötä luku (tyhjä rivi lopettaa): ")
    if syote_numero == '':
        break
    try:    # me tarvitaan vain luvut
        luku = float(syote_numero)
        numerot.append(luku)
    except ValueError:
        print("Virheellinen syöte, syötä luku.")
if numerot:
    pienin = min(numerot)
    suurin = max(numerot)
    print(f"Pienin luku: {pienin}")
    print(f"Suurin luku: {suurin}")
else:
    print("Et syöttänyt yhtään lukua.")
